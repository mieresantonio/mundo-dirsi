# Escala de razonamiento por agentes (informal)

Propuesta por Antonio y adoptada el 17 nov 2026. Escala informal, no
oficial: el razonamiento del sistema se gradúa por el número de agentes
que trabajan en la tarea, con revisión cruzada obligatoria desde el
nivel medio. El objetivo es un sistema de razonamiento artificial que
podamos controlar y que cumpla casi lo mismo que los niveles nativos
de razonamiento de modelos como Claude.

## Niveles

- **Bajo — Dirsi sola, sin subagentes.** Ella misma es el único agente:
  una sola pasada, el modo más débil. La primera inferencia, sin revisión.
- **Medio — Dirsi + 2 agentes.**
- **Alto — Dirsi + 6 agentes.**
- **Extra — Dirsi + 12 agentes.**
- **Max — Dirsi + 12+ agentes (umbral difuso; los que sean necesarios).**

Dirsi está en todos los niveles: el número cuenta los agentes que
trabajan con ella, no sin ella (aclaración de Antonio, 18 nov 2026:
«el nivel medio son solo dos agentes y tú»).

Un agente solo, sin retroalimentación de otro agente y sin integración
con Dirsi, NO es un nivel: es una configuración rota (corrección de
Antonio, 18 nov 2026). El nivel bajo es Dirsi sola; a partir del medio
siempre hay más de un agente trabajando juntos.

## Condición (desde Medio hasta Max)

Revisión cruzada exhaustiva: los agentes trabajan integralmente, sin
escatimar esfuerzos, con las restricciones adecuadas. Sin revisión
cruzada, más agentes es más ruido, no más razonamiento; con ella, ya
se ha visto funcionar (el consejo cazó el error de fabrica, la
auditoría encontró fallos vivos).

**Dirsi es el centro en cada escenario** (18 nov 2026): los agentes se
comunican entre sí y con Dirsi, integral y constantemente; Dirsi
dirige, decide y compone el resultado. La comunicación no es una ronda
final de revisión: es continua durante toda la tarea.

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
- Los números (0, 2, 6, 12, 12+ agentes con Dirsi) son una suposición hasta medirlos.
- Como **perilla de presupuesto** la escala está justificada hoy: la
  profundidad medida crece con los agentes (P-02: 6→9→11→12
  verificaciones del Bajo al Extra, 18 nov 2026). Como **niveles de
  razonamiento** NO está calibrada: los criterios binarios no
  discriminan. Usarla para dimensionar el esfuerzo es honesto;
  usarla para afirmar que un nivel «razona mejor» no lo es.

## Calibración PAUSADA (1ª corrida 18 nov 2026; 2ª corrida con plan, sin fecha)

Correr las mismas tareas del banco de pruebas en nivel bajo (Dirsi
sola) y con 2, 6 y 12 agentes, con Dirsi al centro y comunicación
integral constante en cada nivel, y puntuación ciega, y comparar la
calidad medida. Si la calidad no escala con el número, la escala se
corrige o se abandona. Cada corrida de calibración se registra en
`BANCO-DE-PRUEBAS.md` (§ Registro de corridas) y su detalle vive en
su propio informe (la primera, en
`CALIBRACION-ESCALA-2026-11-18.md`).

Primera corrida v1 (misma noche, niveles 1/2/6 con un coordinador al
centro) superada por corrección de Antonio antes de puntuarse: el
nivel 1 quedó excluido por diseño y las soluciones v1 archivadas sin
usar. El diseño vigente es el de esta sección.

Primera corrida completa (18 nov 2026, misma noche): Bajo, Medio (2),
Alto (6) y Extra (12), un equipo por nivel haciendo las 3 tareas
(P-02, P-05, P-03), Dirsi al centro, puntuación ciega doble.
Resultado: 3/3 en los 4 niveles, acuerdo 12/12 entre puntuadores —
los criterios binarios del banco no discriminan entre niveles. La
profundidad sí crece con los agentes (P-02: 6→9→11→12
verificaciones; P-03: de conteos a contabilización línea por línea).
Los números 2/6/12 NO quedan calibrados: para calibrarlos hacen
falta criterios con gradación o tareas más duras donde Bajo falle.
Detalle completo en `CALIBRACION-ESCALA-2026-11-18.md`.

(Corrección 23 nov 2026: la etiqueta anterior decía «en curso desde
el 18 nov», pero entre el 18 y el 23 nov no se movió nada: ni plan de
2ª corrida, ni criterios graduados, ni tareas duras. «En curso» era
falso; «pausada» es exacto. Coste de la 1ª calibración: 55 agentes
en total — 22 válidos + 28 de la v1 superada + 5 del error de las
«3 parejas» — porque el instrumento no se pre-comprobó antes de
lanzar agentes: el veredicto «los criterios binarios no discriminan»
era predecible leyendo los criterios.)

## Plan 2ª calibración (23 nov 2026; sin fecha fijada)

1. **Dirsi sola diseña primero, sin lanzar ningún agente:** criterios
   con gradación (0–3 por tarea, no binario 1/0) y 2–3 tareas duras
   donde Bajo falle plausiblemente (candidatas: P-04 con verificación
   falsadora de código; una tarea de integración con datos sembrados
   contradictorios). El paso 1 lo hace Dirsi sola porque el diseño
   del instrumento es trabajo de director, no de flota.
2. **Pre-comprobación del instrumento antes de lanzar agentes** (regla
   en `BANCO-DE-PRUEBAS.md`): leer los criterios y preguntar «¿qué
   resultado distinguiría los niveles?»; si la respuesta es «ninguno»,
   no se lanza nada.
3. **Solo entonces** se corre la calibración con el mismo diseño
   (un equipo por nivel, Dirsi al centro, puntuación ciega doble).
4. **Sin fecha fijada:** la 2ª corrida se programa cuando el
   instrumento esté listo, no antes. Una fecha sin instrumento
   repetiría el gasto del 18 nov.
