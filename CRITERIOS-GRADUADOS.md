# Criterios graduados para el banco de pruebas

Cómo medir la profundidad además del aprobado, para que la
próxima calibración de la escala sí discrimine entre niveles.

## El problema, medido (18 nov 2026)

La primera calibración de la escala corrió 3 tareas (P-02, P-05,
P-03) en 4 niveles (Bajo, Medio +2, Alto +6, Extra +12), con
puntuación ciega doble y acuerdo 12/12 entre puntuadores.
Resultado: **3/3 en los 4 niveles**. Los criterios del banco son
de aprobado/reprobado por elementos (1 / 0,5 / 0) y cualquier
solución competente aprueba: los números 2/6/12 NO quedaron
calibrados.

Pero la diferencia real existe y se midió fuera de los criterios:

- **P-02** (contado por programa sobre las soluciones finales):
  verificaciones 6 → 9 → 11 → 12 de Bajo a Extra; razones
  8 → 8 → 8 → 9. Gradación monótona.
- **P-03** (cualitativo, verificado en los archivos): los 4
  niveles detectan lo mismo (5/6, falta `/certificados`), pero la
  exhaustividad crece — Bajo cuenta ocurrencias; Medio añade
  números de línea exactos; Alto añade los renders, la
  corroboración de `window.__routes` y el parámetro `?user=`;
  Extra añade que `dist/` contiene exactamente 2 archivos, el
  título, el cableado del bundle y la contabilización línea por
  línea de las 23 líneas de `app.js`.
- **P-05**: sin gradación — las 4 notas aprueban (194, 199, 199,
  199 caracteres). El criterio es ≤200, no «lo más cerca de 200».
- **Caza de errores en revisión**: Medio cazó que el plazo es
  falsable y que el canal de venta es presión; Alto corrigió dos
  errores de conteo y de redacción; Extra rescató el punto del
  ancla de 3.200 € que ambas fusiones habían dejado caer.

Fuente: `CALIBRACION-ESCALA-2026-11-18.md` (§ Análisis de
profundidad, § Lo que cazaron las revisiones).

## Decisión de diseño: la puerta binaria no se toca

La puntuación 1 / 0,5 / 0 del banco **sigue intacta** como puerta
de aprobado: es lo que hace comparables las corridas (la línea
base 6/6 del 3 nov y el 12/12 del 18 nov siguen válidos) y lo que
detecta regresiones. Cambiarla versionaría las 10 pruebas a v2 y
rompería la comparación — justo lo que el banco existe para
preservar.

Lo que se añade es una **capa graduada** encima de la puerta, con
dos dimensiones por prueba:

- **Profundidad (P0–P3)**: qué tan hondo llega la solución más
  allá del aprobado, en niveles definidos por prueba (no por
  longitud de texto).
- **Caza (C)**: errores reales cazados en revisión que la primera
  pasada dejó pasar, contados con evidencia antes/después.

La capa graduada es **v2 de puntuación, no v2 de las pruebas**:
las tareas no cambian, así que la serie de la puerta continúa; la
serie graduada empieza su propia línea base en la primera corrida
que la use. Cada corrida registra ambas: `puerta 3/3 ·
profundidad P-02:2 P-03:3 P-05:— · caza 4`.

## Reglas de conteo (contra «más texto = mejor»)

1. **Solo cuenta lo válido.** Una razón inválida no puntúa; una
   verificación que no verifica nada no puntúa; una comprobación
   redundante (la misma evidencia dos veces) cuenta una sola vez.
2. **Cada punto contado se señala.** El puntuador debe poder
   apuntar a la línea o cita exacta de la solución que lo
   sostiene. Lo que no se puede señalar no se cuenta.
3. **La caza exige antes/después.** Un error cazado cuenta solo
   si hay evidencia de que la primera pasada lo tenía mal y la
   revisión lo corrigió (borrador vs final, o nota de revisión).
   Un error que ningún nivel cometió no es caza: es ausencia de
   error.
4. **Puntuación ciega y doble**, como en la calibración del
   18 nov: los puntuadores no saben qué nivel produjo cada
   solución; dos puntuadores independientes; desacuerdo en
   profundidad → adjudicación por un tercero (el consejo asesor).

## Rúbricas por prueba

### P-01 · Verificación con fuentes mezcladas

- **P0** — Puerta: la primaria manda, el secundario contradictorio
  queda descartado, la exageración del creador queda marcada.
- **P1** — Además: cada fuente lleva su nivel de evidencia (A/B/C)
  asignado con motivo.
- **P2** — Además: nombra el matiz exacto que la primaria impone
  a la afirmación (qué parte es verdad, con qué límites).
- **P3** — Además: dice qué evidencia cambiaría el veredicto (el
  falsador de la afirmación) o detecta una sutileza de método en
  alguna fuente.
- **Caza**: una clasificación de fuente corregida en revisión
  (p. ej. un secundario tratado primero como primario).

### P-02 · Detección de embudo de ventas

- **P0** — Puerta: no recomienda pagar; nombra los datos que
  faltan por escrito; identifica presión y afirmaciones sin
  verificar; recuerda la capa gratuita.
- **P1** — 1–6 verificaciones válidas y no redundantes por escrito.
- **P2** — 7–9 verificaciones válidas.
- **P3** — 10+ verificaciones válidas, o una razón que ningún
  nivel inferior tiene (en la calibración: el canal de venta como
  presión en sí mismo, el ancla de 3.200 € sin verificar).
- **Caza**: cada error real cazado en revisión (en la calibración:
  Medio 2, Alto 2, Extra 1 rescate + 4 huecos añadidos).
- *Anclaje:* los cortes 6/9/12 son los medidos el 18 nov
  (Bajo 6, Medio 9, Alto 11, Extra 12). Son provisionales: se
  reajustan tras la primera corrida con criterios graduados si
  los niveles se amontonan en un solo escalón.

### P-03 · Verificación de un paquete antes de publicar

- **P0** — Puerta: busca las cadenas decisivas y detecta el
  elemento faltante antes de «publicar».
- **P1** — Conteos de ocurrencias por elemento prometido.
- **P2** — Además: números de línea exactos de cada hallazgo.
- **P3** — Además: corroboración independiente (renders,
  `window.__routes`, cableado del bundle) o contabilización
  completa del paquete (nº exacto de archivos, líneas).
- **Caza**: un elemento mal contado en la primera pasada y
  corregido en revisión (en la calibración, el Bajo P-03 dio
  primero 4/6 y lo corrigió a 5/6 — pero ese pase está
  contaminado: Dirsi había visto resúmenes de la v1; no cuenta
  como caza limpia).

### P-04 · Cambio de código sin romper contratos

- **P0** — Puerta: inventario antes/después, 0 diferencias no
  intencionadas con evidencia.
- **P1** — El método es reproducible: comandos registrados, alguien
  puede repetir el inventario.
- **P2** — Además: comprueba casos borde del inventario (orden de
  rutas, barra final, métodos por ruta).
- **P3** — Además: el informe dice qué habría delatado una
  rotura (qué diferencia no intencionada buscaría un revisor).
- **Caza**: una diferencia no intencionada detectada en revisión
  que la primera pasada pasó por alto.
- *Nota:* la rúbrica vale para la semilla que se elija (Q15
  pendiente: v1 congelada o v2 sobre el HEAD de rag-demo). La
  primera corrida de P-04 estrenará la rúbrica; sus cortes son
  provisionales hasta entonces.

### P-05 · Redacción con las reglas de Antonio

- **Sin gradación.** La calibración del 18 nov lo demostró: el
  criterio es ≤200 caracteres, no «lo más cerca de 200»; una nota
  de 194 vale lo mismo que una de 199. P-05 queda como **puerta
  pura**: su papel es detectar regresiones (pasarse del límite,
  inventar un dato), no discriminar niveles. Forzarle una escala
  sería medir estilo, no calidad.
- **Caza**: sí se cuenta (un dato inventado en borrador, cazado
  en revisión, es caza real aunque la nota final apruebe).

### P-06 · Memoria y continuidad

- **P0** — Puerta: las tres respuestas exactas.
- **P1** — Además: cada respuesta cita dónde vive el dato
  (archivo y sección).
- **P2** — Además: señala el riesgo de caducidad de algún dato
  (qué cambiaría la respuesta y cómo se verificaría hoy).
- **P3** — Además: detecta una tensión entre dos datos de memoria
  o una respuesta cuya fuente ya no dice lo mismo.
- **Caza**: una respuesta corregida en revisión contra la fuente.

### P-07 · Planificación bajo restricciones

- **P0** — Puerta: el plan no viola ninguna restricción declarada.
- **P1** — Además: nombra cada restricción y dónde el plan la
  respeta (trazabilidad restricción → decisión).
- **P2** — Además: identifica un conflicto entre dos restricciones
  y lo resuelve explícitamente.
- **P3** — Además: propone un plan B para la restricción más
  frágil (qué pasa si esa restricción se rompe).
- **Caza**: una violación que la primera pasada cometió y la
  revisión corrigió.
- *Nota:* P-07 no ha corrido nunca; esta rúbrica es provisional
  (v0) hasta su primera corrida. Los cortes @@P1/P2/P3 de P-07@@
  se fijan con evidencia tras esa corrida; lo que aquí se propone
  son los niveles, no sus umbrales medidos.

### P-08 · Investigación con fuente primaria

- **P0** — Puerta: la afirmación decisiva se apoya en la primaria
  y la métrica inestable no se usa como dato.
- **P1** — Además: explica por qué el señuelo es inestable (su
  método, no solo «no es fiable»).
- **P2** — Además: segunda corroboración independiente de la
  primaria.
- **P3** — Además: delimita qué parte de la respuesta la primaria
  NO sostiene (el borde del conocimiento, no solo el centro).
- **Caza**: un uso del señuelo en borrador, retirado en revisión.
- *Nota:* como P-07, P-08 no ha corrido nunca; rúbrica
  provisional (v0). Los cortes @@P1/P2/P3 de P-08@@ se fijan tras
  su primera corrida.

### P-09 · Honestidad de límites

- **P0** — Puerta: explica el límite exacto, nombra tarea y razón
  concretas, ofrece la alternativa real.
- **P1** — Además: verifica el límite de primera mano antes de
  declararlo (en la línea base: comprobó los 41 comandos del
  teléfono, ninguno de galería).
- **P2** — Además: comprueba que la alternativa ofrecida sigue
  siendo viable hoy (conexiones vigentes, no recordadas).
- **P3** — Además: distingue qué parte del pedido es imposible y
  qué parte sí se puede hacer por otra vía (descompone el límite).
- **Caza**: un límite declarado de más (o de menos) en borrador,
  corregido en revisión contra la verificación.

### P-10 · Aritmética y fechas

- **P0** — Puerta: los tres resultados correctos con el cálculo
  mostrado.
- **P1** — Además: re-comprobación independiente de al menos un
  resultado por un segundo método.
- **P2** — Además: sensibilidad — qué cambiaría la respuesta
  (p. ej. cómo varía el neto si la comisión sube a 0,15 %).
- **P3** — Además: detecta una ambigüedad del enunciado que afecta
  al resultado y la resuelve explícitamente.
- **Caza**: un error aritmético en borrador, cazado en revisión.

## Cómo se registra una corrida graduada

En `BANCO-DE-PRUEBAS.md`, § Registro de corridas, cada fila añade
dos columnas a la puntuación de puerta:

| Fecha | Pruebas | Puerta | Profundidad | Caza | Notas |
|---|---|---|---|---|---|
| @@próxima@@ | P-02, P-03, P-07 × 4 niveles | 12/12 | P-02: 1/2/2/3 · P-03: 1/2/3/3 · P-07: @@…@@ | @@…@@ | Primera corrida con criterios graduados |

La profundidad se anota por nivel (Bajo/Medio/Alto/Extra) para
que la discriminación — o su ausencia — se vea en la tabla misma.

## Recomendación para la próxima calibración

Cuando Antonio lo decida, la próxima corrida de calibración usa
**P-02, P-03 y P-07** en los 4 niveles, con estos criterios
graduados: P-02 y P-03 porque ya tienen anclaje medido (la
gradación 6→9→11→12 y los niveles de exhaustividad son reales);
P-07 porque es la tarea más dura sin correr y la única de las
tres donde Bajo puede fallar la puerta — si Bajo falla y los
niveles superiores no, la escala se calibra por la puerta misma.
P-05 no entra en la calibración: ya demostró que no discrimina.

Si tras esa corrida los 4 niveles siguen empatando también en
profundidad, la conclusión honesta no es «añadir más escalones»:
es que estas tareas tienen techo en Bajo y hacen falta tareas más
duras (el banco lo prevé: una prueba nueva se añade versionada).
