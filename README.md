# AgentesVSC

Repositorio base para almacenar y versionar multiples packs de agentes, skills, comandos y hooks orientados a VS Code y herramientas compatibles.

La idea no es guardar un solo agente suelto, sino una coleccion organizada de packs reutilizables y modificables. Cada pack puede venir de una fuente distinta y mantener sus propios agentes, skills, manifests y notas de integracion.
En cada carpeta esta toda la informacion del fabricante muchos son modificados para ser utilizados en VScode pero pueden ser utiles

## Objetivo

Este repositorio sirve para:

1. Centralizar copias de agentes personalizados o adaptados.
2. Mantener varias familias de agentes sin mezclar archivos entre si.
3. Tener una base lista para VS Code, Cursor, Claude Code, Codex u otras herramientas compatibles.
4. Poder modificar un pack sin tocar el resto.

## Estructura

```text
AgentesVSC/
├── README.md
├── catalog.json
└── packs/
    └── <pack>/
        ├── agents/
        ├── skills/
        ├── commands/
        ├── hooks/
        ├── .claude-plugin/
        ├── .cursor-plugin/
        ├── .codex/
        ├── .opencode/
        ├── README.md
        └── PACK_INFO.md
```

## Copias de proyecto incluidas

Actualmente el repositorio contiene las siguientes copias dentro de `packs/`, junto con un resumen de su objetivo principal:

1. `everything-claude-code`: base amplia de agentes, skills, reglas, contextos y utilidades para flujos de trabajo asistidos en Claude Code y entornos compatibles con VS Code.
2. `G0DM0D3`: interfaz abierta de chat multimodelo orientada a experimentación, red teaming e interacción avanzada con modelos vía OpenRouter.
3. `incidentfox`: plataforma AI SRE para investigación automática de incidentes, correlación de alertas, análisis de logs y búsqueda de causa raíz.
4. `MiroFish`: motor multiagente de predicción y simulación colectiva que crea mundos digitales para ensayar escenarios y generar reportes predictivos.
5. `ollama`: runtime y plataforma para ejecutar, administrar e integrar modelos abiertos en local mediante CLI, API REST y conectores.
6. `pentagi`: sistema autónomo de pentesting asistido por IA con agentes especializados, herramientas de seguridad, memoria y despliegue self-hosted.
7. `superpowers`: pack base de agentes y skills de desarrollo asistido, útil como referencia funcional y punto de partida para personalizaciones.
8. `vscode-local-overrides`: contenedor local para derivaciones y ajustes específicos de VS Code sin modificar directamente los packs importados.

## Resumen por tipo

- Packs base de agentes y automatizacion: `superpowers`, `everything-claude-code`, `vscode-local-overrides`.
- Proyectos de asistentes, modelos o interfaces IA: `G0DM0D3`, `ollama`, `MiroFish`.
- Proyectos orientados a operaciones y seguridad: `incidentfox`, `pentagi`.

Nota de convivencia: al usar multiples packs al mismo tiempo puede haber nombres de agentes repetidos (por ejemplo `code-reviewer`). En esos casos conviene definir una prioridad por pack o crear variantes derivadas con nombres unicos.

## Criterio de organizacion

Cada pack debe vivir dentro de su propia carpeta en `packs/`.

Eso permite:

1. conservar manifests y convenciones del pack original
2. aplicar modificaciones locales sin romper otros packs
3. publicar o exportar cada pack por separado si despues hace falta

El catalogo del repo conserva el origen como referencia historica, pero evita depender de rutas locales para que el repositorio siga siendo portable.

## Uso con VS Code

Este repositorio no fuerza un solo runtime. En cambio, conserva el contenido fuente para que luego puedas:

1. apuntar Cursor o Claude Code al pack que quieras usar
2. copiar o enlazar skills para Codex
3. reutilizar instrucciones o agentes en extensiones de VS Code
4. derivar versiones modificadas por proyecto o por equipo

## Agregar otro pack

Proceso recomendado:

1. crear `packs/<nombre-del-pack>`
2. copiar dentro sus carpetas `agents`, `skills`, `commands`, `hooks` y manifests relevantes
3. agregar `PACK_INFO.md` con origen, fecha y notas de modificacion
4. actualizar `catalog.json`
5. documentar cualquier ajuste especifico para VS Code o la herramienta objetivo

## Flujo para copias modificables en VS Code

Para mantener una estrategia limpia de cambios:

1. no modificar directamente los packs importados cuando el ajuste sea local
2. copiar el archivo original hacia `packs/vscode-local-overrides/`
3. renombrar la derivacion para evitar colisiones de nombres
4. documentar el cambio en `packs/vscode-local-overrides/docs/CHANGELOG_LOCAL.md`
5. validar en VS Code y, si aplica, promover luego a un pack propio

## Política de preservación de copias

El objetivo de este repositorio es conservar copias completas de herramientas y proyectos útiles disponibles en GitHub para que no se pierdan.

Reglas que aplican a toda importación nueva:

1. Importar el contenido completo de la carpeta del proyecto, sin dejar repositorios git anidados (`/.git` interno).
2. Antes de hacer `git add`, eliminar el `.git` interno si el proyecto ya tiene uno propio.
3. Registrar el pack en `catalog.json` con su upstream, fecha de importación y resumen de contenidos.
4. Actualizar el listado en este README.
5. No modificar el contenido original del autor. Si se requiere un ajuste local, crear una copia en `vscode-local-overrides`.

## Notas

`AgentesVSC` es un repositorio contenedor. La compatibilidad final con cada plataforma depende de los manifests y del mecanismo de carga de esa plataforma.

El catálogo completo y los upstream de cada copia se mantienen en `catalog.json`.
