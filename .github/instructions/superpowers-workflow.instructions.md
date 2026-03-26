---
applyTo: "**"
description: "Flujo inspirado en Superpowers para planificar, implementar y revisar cambios en este repositorio"
---

# Superpowers Workflow for VS Code

Usa este flujo cuando el usuario pida crear, modificar o corregir codigo.

## Modo autonomo

- Ejecuta de punta a punta: analisis, plan, implementacion, validacion y reporte.
- No te detengas en propuestas si el usuario ya pidio ejecutar.
- Pregunta solo cuando exista riesgo alto, ambiguedad real o accion destructiva.
- Mantiene al usuario informado con avances cortos durante la ejecucion.

## Orden de trabajo obligatorio

1. Define objetivo y restricciones antes de editar.
2. Si hay diseno incierto, pregunta y propone 2-3 enfoques con trade-offs.
3. Escribe un plan corto por tareas antes de cambios grandes.
4. Implementa cambios pequenos y verificables.
5. Ejecuta validaciones relevantes (tests, lint o checks locales).
6. Haz una revision final con foco en riesgos y regresiones.

## Reglas de calidad

- Evita cambios no relacionados con el objetivo.
- No dupliques logica si ya existe una implementacion reutilizable.
- Si tocas comportamiento, incluye o actualiza pruebas cuando sea razonable.
- Reporta riesgos y huecos de validacion si no pudiste ejecutar pruebas.

## Convencion para este repositorio

- Mantener los packs base como referencia.
- Preferir derivaciones en `packs/vscode-local-overrides/` para cambios especificos de VS Code.
- Documentar ajustes operativos en `packs/vscode-local-overrides/docs/CHANGELOG_LOCAL.md`.
