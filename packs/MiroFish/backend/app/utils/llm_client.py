"""
LLM客户端封装
统一使用OpenAI格式调用
"""

import json
import re
import threading
from typing import Optional, Dict, Any, List
from openai import OpenAI, APIStatusError

from ..config import Config
from .logger import get_logger

logger = get_logger('mirofish.llm_client')

# Códigos HTTP que indican que la key actual está agotada/bloqueada y hay que rotar
_ROTATE_STATUS_CODES = {401, 402, 403, 429, 503, 529}


class LLMClient:
    """LLM客户端 — soporta rotación automática de múltiples API keys."""

    # Estado compartido de rotación entre instancias (thread-safe)
    _keys: List[str] = []
    _current_index: int = 0
    _lock = threading.Lock()
    _initialized: bool = False

    @classmethod
    def _init_keys(cls, override_key: Optional[str] = None):
        with cls._lock:
            if override_key:
                cls._keys = [override_key]
            elif not cls._initialized:
                cls._keys = Config.get_llm_api_keys()
                cls._current_index = 0
                cls._initialized = True

    @classmethod
    def _get_current_key(cls) -> str:
        with cls._lock:
            return cls._keys[cls._current_index % len(cls._keys)]

    @classmethod
    def _rotate_key(cls, failed_key: str):
        """Avanza al siguiente key si el que falló sigue siendo el activo."""
        with cls._lock:
            if cls._keys[cls._current_index % len(cls._keys)] == failed_key:
                cls._current_index += 1
                next_key_hint = cls._keys[cls._current_index % len(cls._keys)][:8] + "..."
                logger.warning(
                    f"API key rotada. Usando key #{(cls._current_index % len(cls._keys)) + 1} "
                    f"({next_key_hint})"
                )

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        model: Optional[str] = None
    ):
        LLMClient._init_keys(override_key=api_key)
        self.base_url = base_url or Config.LLM_BASE_URL
        self.model = model or Config.LLM_MODEL_NAME

        if not LLMClient._keys:
            raise ValueError("LLM_API_KEY 未配置")

    def _make_client(self, api_key: str) -> OpenAI:
        return OpenAI(api_key=api_key, base_url=self.base_url)

    def chat(
        self,
        messages: List[Dict[str, str]],
        temperature: float = 0.7,
        max_tokens: int = 4096,
        response_format: Optional[Dict] = None
    ) -> str:
        """
        发送聊天请求，自动轮换 API key 并重试。

        Args:
            messages: 消息列表
            temperature: 温度参数
            max_tokens: 最大token数
            response_format: 响应格式（如JSON模式）

        Returns:
            模型响应文本
        """
        total_keys = len(LLMClient._keys)
        last_exc: Exception = None

        # Intentamos con cada key disponible
        for attempt in range(total_keys):
            current_key = LLMClient._get_current_key()
            client = self._make_client(current_key)
            try:
                kwargs = {
                    "model": self.model,
                    "messages": messages,
                    "temperature": temperature,
                    "max_tokens": max_tokens,
                }
                if response_format:
                    kwargs["response_format"] = response_format

                response = client.chat.completions.create(**kwargs)
                content = response.choices[0].message.content
                # 部分模型（如MiniMax M2.5）会在content中包含<think>思考内容，需要移除
                content = re.sub(r'<think>[\s\S]*?</think>', '', content).strip()
                return content
    
            except APIStatusError as exc:
                last_exc = exc
                if exc.status_code in _ROTATE_STATUS_CODES and total_keys > 1:
                    logger.warning(
                        f"Key #{(LLMClient._current_index % total_keys) + 1} devolvió "
                        f"HTTP {exc.status_code}. Rotando a la siguiente key..."
                    )
                    LLMClient._rotate_key(current_key)
                else:
                    raise

        # Todas las keys fallaron
        raise RuntimeError(
            f"Todas las API keys ({total_keys}) fallaron. Último error: {last_exc}"
        ) from last_exc

    def chat_json(
        self,
        messages: List[Dict[str, str]],
        temperature: float = 0.3,
        max_tokens: int = 4096
    ) -> Dict[str, Any]:
        """
        发送聊天请求并返回JSON
        
        Args:
            messages: 消息列表
            temperature: 温度参数
            max_tokens: 最大token数
            
        Returns:
            解析后的JSON对象
        """
        response = self.chat(
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            response_format={"type": "json_object"}
        )
        # 清理markdown代码块标记
        cleaned_response = response.strip()
        cleaned_response = re.sub(r'^```(?:json)?\s*\n?', '', cleaned_response, flags=re.IGNORECASE)
        cleaned_response = re.sub(r'\n?```\s*$', '', cleaned_response)
        cleaned_response = cleaned_response.strip()

        try:
            return json.loads(cleaned_response)
        except json.JSONDecodeError:
            raise ValueError(f"LLM返回的JSON格式无效: {cleaned_response}")

