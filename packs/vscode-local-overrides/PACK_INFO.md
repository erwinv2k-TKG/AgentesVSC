# PACK_INFO

- name: vscode-local-overrides
- status: active
- owner: local-team
- target: VS Code
- purpose: mantener copias modificadas para uso operativo

## Origen

Este pack no viene de un upstream unico. Es un contenedor local de derivaciones creadas desde packs existentes.

## Reglas

1. No editar archivos dentro de otros packs cuando el cambio sea especifico de VS Code.
2. Cada cambio debe incluir nota corta en `docs/CHANGELOG_LOCAL.md`.
3. Si una derivacion se vuelve estable, evaluar promoverla a un pack propio.
