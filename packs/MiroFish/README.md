<div align="center">

<img src="./static/image/MiroFish_logo_compressed.jpeg" alt="MiroFish Logo" width="75%"/>

<a href="https://trendshift.io/repositories/16144" target="_blank"><img src="https://trendshift.io/api/badge/repositories/16144" alt="666ghj%2FMiroFish | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

Motor universal de inteligencia colectiva — predice cualquier cosa
</br>
<em>A Simple and Universal Swarm Intelligence Engine, Predicting Anything</em>

<a href="https://www.shanda.com/" target="_blank"><img src="./static/image/shanda_logo.png" alt="666ghj%2MiroFish | Shanda" height="40"/></a>

[![Docker](https://img.shields.io/badge/Docker-Build-2496ED?style=flat-square&logo=docker&logoColor=white)](https://hub.docker.com/)

[![Discord](https://img.shields.io/badge/Discord-Join-5865F2?style=flat-square&logo=discord&logoColor=white)](http://discord.gg/ePf5aPaHnA)
[![X](https://img.shields.io/badge/X-Follow-000000?style=flat-square&logo=x&logoColor=white)](https://x.com/mirofish_ai)
[![Instagram](https://img.shields.io/badge/Instagram-Follow-E4405F?style=flat-square&logo=instagram&logoColor=white)](https://www.instagram.com/mirofish_ai/)

[English](./README-EN.md) | [中文文档](./README.md) | [Español](./README.md)

</div>

## ⚡ Descripción del proyecto

**MiroFish** es un motor de predicción IA de nueva generación basado en tecnología multi-agente. A partir de información semilla del mundo real (noticias de última hora, borradores de políticas, señales financieras), construye automáticamente un mundo digital paralelo de alta fidelidad. En ese espacio, miles de agentes con personalidad independiente, memoria a largo plazo y lógica de comportamiento interactúan libremente y evolucionan socialmente. Puedes inyectar variables dinámicamente desde una «perspectiva divina» para predecir con precisión el curso del futuro — **deja que el futuro se ensaye en un sandbox digital y que las decisiones venzan tras cientos de simulaciones**.

> Solo necesitas: subir material semilla (informe de análisis o una historia de ficción interesante) y describir el objetivo de predicción en lenguaje natural.
> MiroFish devolverá: un informe de predicción detallado y un mundo digital de alta fidelidad con el que podrás interactuar en profundidad.

### Nuestra visión

MiroFish aspira a construir un espejo de inteligencia colectiva que mapee la realidad, capturando la emergencia grupal generada por interacciones individuales para superar las limitaciones de las predicciones tradicionales:

- **A nivel macro**: somos el laboratorio de ensayo de los tomadores de decisiones, permitiendo probar políticas y estrategias de comunicación sin riesgo.
- **A nivel micro**: somos el sandbox creativo del usuario individual — ya sea para predecir el final de una novela o explorar ideas descabelladas, de forma divertida y accesible.

Desde predicciones serias hasta simulaciones lúdicas, hacemos que cada «¿qué pasaría si…?» pueda ver su resultado y que predecir cualquier cosa sea posible.

## 🌐 Demo en línea

Visita el entorno de demostración en línea para experimentar una predicción de eventos de opinión pública que hemos preparado para ti.

## 📸 Capturas de pantalla

<div align="center">
<table>
<tr>
<td><img src="./static/image/Screenshot/运行截图1.png" alt="截图1" width="100%"/></td>
<td><img src="./static/image/Screenshot/运行截图2.png" alt="截图2" width="100%"/></td>
</tr>
<tr>
<td><img src="./static/image/Screenshot/运行截图3.png" alt="截图3" width="100%"/></td>
<td><img src="./static/image/Screenshot/运行截图4.png" alt="截图4" width="100%"/></td>
</tr>
<tr>
<td><img src="./static/image/Screenshot/运行截图5.png" alt="截图5" width="100%"/></td>
<td><img src="./static/image/Screenshot/运行截图6.png" alt="截图6" width="100%"/></td>
</tr>
</table>
</div>

## 🎬 Videos de demostración

### 1. Predicción de opinión pública de la Universidad de Wuhan + explicación del proyecto MiroFish

<div align="center">
<a href="https://www.bilibili.com/video/BV1VYBsBHEMY/" target="_blank"><img src="./static/image/武大模拟演示封面.png" alt="MiroFish Demo Video" width="75%"/></a>

Haz clic en la imagen para ver el video de demostración completo con predicción basada en el «Informe de opinión pública de la Universidad de Wuhan» generado por BettaFish.
</div>

### 2. Predicción del final perdido de «El sueño del pabellón rojo»

<div align="center">
<a href="https://www.bilibili.com/video/BV1cPk3BBExq" target="_blank"><img src="./static/image/红楼梦模拟推演封面.jpg" alt="MiroFish Demo Video" width="75%"/></a>

Haz clic en la imagen para ver cómo MiroFish predice en profundidad el final perdido basándose en los primeros 80 capítulos de «El sueño del pabellón rojo».
</div>

> Próximamente: ejemplos de **predicción financiera** y **predicción de noticias de política actualidad**...

## 🔄 Flujo de trabajo

1. **Construcción del grafo**: extracción de semillas reales, inyección de memoria individual y grupal, construcción de GraphRAG.
2. **Configuración del entorno**: extracción de relaciones entre entidades, generación de perfiles de agentes, inyección de parámetros de simulación.
3. **Inicio de simulación**: simulación paralela en dos plataformas, análisis automático de requisitos de predicción, actualización dinámica de memoria temporal.
4. **Generación de reporte**: el ReportAgent dispone de un conjunto rico de herramientas para interactuar en profundidad con el entorno post-simulación.
5. **Interacción profunda**: conversa con cualquier agente del mundo simulado o con el ReportAgent.

## 🚀 Inicio rápido

### Opción 1 — Despliegue desde código fuente (recomendado)

#### Requisitos previos

| Herramienta | Versión requerida | Descripción | Verificación |
|-------------|-------------------|-------------|--------------|
| **Node.js** | 18+ | Entorno de ejecución del frontend, incluye npm | `node -v` |
| **Python** | ≥3.11, ≤3.12 | Entorno de ejecución del backend | `python --version` |
| **uv** | última versión | Gestor de paquetes Python | `uv --version` |

#### 1. Configurar variables de entorno

```bash
# Copiar el archivo de configuración de ejemplo
cp .env.example .env

# Editar .env y rellenar las claves de API necesarias
```

**Variables de entorno requeridas:**

```env
# Configuración de la API LLM (compatible con cualquier API en formato OpenAI SDK)
# Se recomienda el modelo qwen-plus de Alibaba Cloud Bailian: https://bailian.console.aliyun.com/
# Ten en cuenta el consumo elevado; empieza con simulaciones de menos de 40 rondas
LLM_API_KEY=tu_api_key
LLM_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
LLM_MODEL_NAME=qwen-plus

# Configuración de Zep Cloud
# La cuota gratuita mensual es suficiente para uso básico: https://app.getzep.com/
ZEP_API_KEY=tu_zep_api_key
```

#### 2. Instalar dependencias

```bash
# Instalar todas las dependencias con un solo comando (raíz + frontend + backend)
npm run setup:all
```

O paso a paso:

```bash
# Instalar dependencias Node (raíz + frontend)
npm run setup

# Instalar dependencias Python (backend, crea entorno virtual automáticamente)
npm run setup:backend
```

#### 3. Iniciar los servicios

```bash
# Iniciar frontend y backend simultáneamente (ejecutar desde la raíz del proyecto)
npm run dev
```

**URLs de los servicios:**
- Frontend: `http://localhost:3000`
- API Backend: `http://localhost:5001`

**Inicio individual:**

```bash
npm run backend   # solo backend
npm run frontend  # solo frontend
```

### Opción 2 — Docker

```bash
# 1. Configurar variables de entorno (igual que en despliegue desde fuente)
cp .env.example .env

# 2. Descargar imagen e iniciar
docker compose up -d
```

Lee el archivo `.env` de la raíz por defecto y mapea los puertos `3000 (frontend) / 5001 (backend)`.

> En `docker-compose.yml` se incluyen comentarios con imágenes espejo aceleradas — sustitúyelas según necesites.

## 📬 Contacto y comunidad

<div align="center">
<img src="./static/image/QQ群.png" alt="Grupo QQ" width="60%"/>
</div>

&nbsp;

El equipo de MiroFish busca colaboradores a tiempo completo e internos. Si te interesa el desarrollo de aplicaciones multi-agente, envía tu CV a: **mirofish@shanda.com**

## 📄 Agradecimientos

**¡MiroFish cuenta con el apoyo estratégico e incubación del Grupo Shanda!**

El motor de simulación de MiroFish está impulsado por **[OASIS](https://github.com/camel-ai/oasis)**. Agradecemos sinceramente la contribución open source del equipo de CAMEL-AI.


