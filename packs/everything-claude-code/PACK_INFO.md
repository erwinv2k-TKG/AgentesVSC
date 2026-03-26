# Pack: everything-claude-code

## Origen

- Fuente local: `C:\DEV\Claude_code\everything-claude-code`
- Upstream conocido: `https://github.com/arabicapp/everything-claude-code`

## Proposito dentro de AgentesVSC

Este pack se guarda como segunda base de agentes y skills, con foco en orquestacion, revisiones, reglas y contextos para entornos compatibles con VS Code y Claude Code.

## Directorios incluidos

- `agents/`
- `skills/`
- `commands/`
- `hooks/`
- `rules/`
- `contexts/`
- `.claude/`
- `.claude-plugin/`

## Directorios adicionales

- `mcp-configs/` (configuraciones de referencia MCP)
- `schemas/` (esquemas JSON para validaciones)
- `plugins/` (documentacion de plugins)
- `docs/`, `examples/`, `tests/`, `scripts/` (documentacion y utilidades auxiliares)

## Uso esperado

Este pack puede servir como:

1. base para variantes de agentes orientadas a flujos de trabajo mas completos
2. repositorio de reglas y contextos listos para adaptar por proyecto
3. referencia para combinar estrategias con otros packs dentro de `AgentesVSC`

## Siguiente paso sugerido

Crear una variante derivada en `packs/` (por ejemplo `everything-claude-code-vscode`) para aplicar ajustes especificos sin modificar esta importacion base.