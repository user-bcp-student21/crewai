# Requerimiento de arquitectura

Usa los datos de la funcionalidad seleccionada que aparecen a continuación como entrada del diseño.

## Issue / feature

- **Título:** $issue_title
- **Descripción:** $issue_description

## Criterios de aceptación

$acceptance_criteria

## Contexto del producto e interfaces existentes

Analiza las interfaces, contratos y restricciones del producto si se describen en la información
anterior o en contexto adicional aprobado que te haya sido proporcionado. No tienes acceso
implícito al repositorio, al backlog ni a otros sistemas: no afirmes haberlos inspeccionado.
Si no se describen interfaces existentes, explica qué información hace falta y anótala como
supuesto o pregunta pendiente. Distingue claramente los contratos existentes de las propuestas
de diseño.

## Alcance del rol

Define componentes, responsabilidades, dependencias, límites del cambio y context boundary.
Especifica el contrato de API con método, ruta, entradas, validaciones, respuestas exitosas,
errores y ejemplos representativos. Mapea cada criterio de aceptación a un componente y a una
condición observable/verificable. Declara supuestos, preguntas pendientes, riesgos y dependencias.
Incluye observabilidad como responsabilidad arquitectónica transversal: logs estructurados,
métricas, trazas/IDs de correlación, señales para diagnosticar errores y latencia y protección
de datos sensibles. Refleja los componentes e interacciones en un diagrama Mermaid válido dentro
de `architecture.md`.

No implementes código ni migraciones, no ejecutes pruebas ni despliegues y no afirmes resultados
que no se hayan observado. Los criterios verificables describen requisitos; no son evidencia de
implementación o ejecución.
