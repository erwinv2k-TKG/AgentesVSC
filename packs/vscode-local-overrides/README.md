# vscode-local-overrides

Pack local para mantener copias modificadas de agentes, skills, comandos y hooks orientados a VS Code.

## Objetivo

Este pack se usa para:

1. Guardar variantes locales sin tocar los packs importados.
2. Probar cambios de forma segura antes de promoverlos.
3. Mantener una referencia clara de que version usa cada equipo o proyecto.

## Estructura

```text
vscode-local-overrides/
├── agents/
├── skills/
├── commands/
├── hooks/
├── docs/
├── README.md
└── PACK_INFO.md
```

## Flujo recomendado

1. Copiar el agente original desde otro pack a `agents/` o `skills/`.
2. Renombrar el archivo para evitar colisiones de nombres.
3. Documentar cambios en `docs/CHANGELOG_LOCAL.md`.
4. Probar en VS Code y anotar notas de compatibilidad.

## Convencion de nombres

- agentes: `nombre-origen.vscode.agent.md`
- skills: `nombre-origen.vscode.skill.md`
- instrucciones: `nombre-origen.vscode.instructions.md`

Esta convencion ayuda a distinguir la version local de la version importada.
