# Superpowers in VS Code (Copilot)

Esta guia adapta el pack superpowers al flujo de personalizaciones de VS Code.

## Que se habilita

El repositorio agrega customizaciones en `.github/`:

- instrucciones globales: `.github/copilot-instructions.md`
- instrucciones: `.github/instructions/superpowers-workflow.instructions.md`
- agente: `.github/agents/superpowers-code-reviewer.agent.md`
- prompts:
  - `.github/prompts/superpowers-brainstorm.prompt.md`
  - `.github/prompts/superpowers-write-plan.prompt.md`
  - `.github/prompts/superpowers-execute-plan.prompt.md`
  - `.github/prompts/superpowers-autonomous-start.prompt.md`

## Como usar

1. Abre este repositorio en VS Code.
2. Inicia un chat de Copilot.
3. Para ejecucion automatica por defecto, trabaja normal y Copilot usara `.github/copilot-instructions.md`.
4. Si quieres forzar el modo, usa el prompt `superpowers-autonomous-start`.
5. Usa prompts por nombre para iniciar flujo guiado:
   - brainstorm (diseno)
   - write-plan (plan)
   - execute-plan (ejecucion)
6. Para revision, invoca el agente `superpowers-code-reviewer`.

## Recomendacion operativa

- Usa `packs/superpowers/` como base de referencia.
- Para cambios propios de VS Code, deriva en `packs/vscode-local-overrides/`.
- Documenta cada ajuste local en `packs/vscode-local-overrides/docs/CHANGELOG_LOCAL.md`.

## Limitacion importante

No todos los mecanismos nativos de plugins de Claude/Cursor son equivalentes 1:1 en Copilot. Esta adaptacion prioriza un flujo operativo equivalente mediante instrucciones, prompts y agente de revision.
