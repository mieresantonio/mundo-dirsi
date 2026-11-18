# Escala de razonamiento por agentes (informal)

Propuesta por Antonio y adoptada el 17 nov 2026. Escala informal, no
oficial: el razonamiento del sistema se gradúa por el número de agentes
que trabajan en la tarea, con revisión cruzada obligatoria desde el
nivel medio. El objetivo es un sistema de razonamiento artificial que
podamos controlar y que cumpla casi lo mismo que los niveles nativos
de razonamiento de modelos como Claude.

## Niveles

- **Bajo — 1 agente (Dirsi sola).** Una sola pasada; el modo más débil.
  La primera inferencia, sin revisión.
- **Medio — 2 agentes.**
- **Alto — 6 agentes.**
- **Extra — 12 agentes.**
- **Max — 12+ agentes (umbral difuso; los que sean necesarios).**

## Condición (desde Medio hasta Max)

Revisión cruzada exhaustiva: los agentes trabajan integralmente, sin
escatimar esfuerzos, con las restricciones adecuadas. Sin revisión
cruzada, más agentes es más ruido, no más razonamiento; con ella, ya
se ha visto funcionar (el consejo cazó el error de fabrica, la
auditoría encontró fallos vivos).

## Max

Diseño de Antonio: Max no tendría limitaciones. Límite real: la cuota
semanal — el 16 nov 2026, 22 agentes gastaron el 87% de la semana.
Por tanto Max es un uso único con presupuesto explícito, no un modo.
Cada uso de Max se decide y se presupuesta antes de lanzarlo.

## Qué es y qué no es

- Esta escala es **amplitud** (más ángulos, más chequeo), no la
  profundidad de una sola cadena de pensamiento que tienen los niveles
  de razonamiento nativos de un modelo. Formas distintas, no lo mismo.
- Todos los agentes corren sobre el mismo motor: comparten puntos
  ciegos. La revisión cruzada los reduce, no los elimina.
- Los números (1, 2, 6, 12, 12+) son una suposición hasta medirlos.

## Calibración (pendiente)

Correr las mismas tareas del banco de pruebas con 1, 2 y 6 agentes y
comparar la calidad medida. Si la calidad no escala con el número, la
escala se corrige o se abandona. La calibración vive en
`BANCO-DE-PRUEBAS.md`.
