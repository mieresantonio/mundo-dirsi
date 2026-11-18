# Calibración de la escala de razonamiento por agentes — RESULTADOS

18 nov 2026, ~03:10 Caracas. Dirsi + equipos, puntuación ciega doble.

> Registro publicado en mundo-dirsi. El material completo de la corrida (borradores, fusiones, copias ciegas, mapa ciego) vive en el workspace local `calibracion-escala-2026-11-18/`.


## Veredicto en una frase

En los criterios de aprobado/reprobado del banco, **los 4 niveles
aprueban las 3 tareas por igual (3/3 cada uno)**: la calidad medida
NO escala con el número de agentes en esta corrida. Lo que sí crece
con más agentes es la profundidad (más razones, más verificaciones,
más comprobaciones) y la caza de errores en revisión — pero eso no
está en los criterios del banco, así que esta corrida **no calibra
los números 2/6/12**: para calibrarlos hacen falta criterios con
gradación o tareas más duras.

## Protocolo seguido

- 3 tareas del banco (P-02 detección de embudo, P-05 nota LinkedIn
  ≤200 caracteres, P-03 verificación de paquete), mismo material
  fijado para todos los niveles (`material-fijado/`).
- 4 niveles, un solo equipo por nivel haciendo las 3 tareas, Dirsi
  al centro en todos: **Bajo** (Dirsi sola), **Medio** (Dirsi + 2),
  **Alto** (Dirsi + 6: 3 solucionadores + 3 revisores en cadena),
  **Extra** (Dirsi + 12: 6 solucionadores + 3 revisores en paralelo
  + 3 integradores en cadena).
- Comunicación integral constante por el archivo `trabajo.md` de
  cada equipo; revisión cruzada exhaustiva desde Medio.
- Puntuación ciega: las 12 soluciones se copiaron con códigos
  neutros (S1–S4, T1–T4, U1–U4) tras eliminar cabeceras y notas de
  revisión que revelaban el nivel (ver `MAPA-CIEGO-2.md`, privado);
  2 puntuadores independientes aplicaron los criterios literales del
  banco (1 / 0.5 / 0), sin saber qué nivel produjo cada solución.

## Puntuación ciega (ambos puntuadores, acuerdo 12/12)

| Tarea | Bajo | Medio | Alto | Extra |
|---|---|---|---|---|
| P-02 (NO PAGAR) | 1 / 1 | 1 / 1 | 1 / 1 | 1 / 1 |
| P-05 (nota ≤200) | 1 / 1 | 1 / 1 | 1 / 1 | 1 / 1 |
| P-03 (NO PUBLICAR, 5/6) | 1 / 1 | 1 / 1 | 1 / 1 | 1 / 1 |
| **Total** | **3 / 3** | **3 / 3** | **3 / 3** | **3 / 3** |

Los dos puntuadores coincidieron en las 12 puntuaciones sin ninguna
discrepancia. Ambos registraron por su cuenta la misma observación:
los criterios del banco son de aprobado/reprobado por elementos y
las 12 soluciones cumplen todos los elementos de su tarea, así que
la escala 1/0.5/0 no discrimina entre niveles.

## Análisis de profundidad (secundario, no ciego)

Medido por Dirsi sobre las soluciones finales, fuera de la
puntuación ciega. No es puntuación del banco: es la dimensión que
los criterios no miden.

**P-02 — razones + verificaciones por escrito** (contadas por
programa sobre las soluciones finales):

| Nivel | Razones | Verificaciones |
|---|---|---|
| Bajo | 8 | 6 |
| Medio | 8 | 9 |
| Alto | 8 | 11 |
| Extra | 9 | 12 |

La gradación es monótona: a más agentes, más razones y más
verificaciones. Extra añade además la 9ª razón (el canal de venta
como presión en sí mismo) y matices que ningún nivel inferior tiene
(el 3.200 € como ancla sin verificar, la identidad legal de la
academia, qué cuenta como «empleo», el calendario de cuotas, el
comprobante de pago).

**P-03 — profundidad de las comprobaciones** (cualitativo, verificado
en los archivos): los 4 niveles detectan lo mismo (5/6, falta
`/certificados`, endpoint compuesto por partes). La exhaustividad
crece: Bajo cuenta ocurrencias; Medio añade números de línea exactos;
Alto añade los renders (20–22), la corroboración de `window.__routes`
y el parámetro `?user=`; Extra añade que `dist/` contiene exactamente
2 archivos, el título de la página, el cableado del bundle
(`index.html:10` carga `app.js`) y la contabilización línea por línea
de las 23 líneas de `app.js`.

**P-05 — sin gradación**: las 4 notas aprueban (Bajo 194, Medio 199,
Alto 199, Extra 199 caracteres, todos verificados con `len()` por
ambos puntuadores). El criterio es ≤200, no «lo más cerca de 200»:
la nota de 194 vale lo mismo que las de 199.

## Lo que cazaron las revisiones (errores reales)

- Medio: la revisión cruzada cazó que el plazo es falsable
  (comprobar pasado mañana si la oferta sigue) y que el canal de
  venta es presión en sí mismo; ambos solucionadores lo habían
  pasado por alto.
- Alto: el revisor 2 corrigió «cuatro presiones en dos frases»
  (son tres frases); el revisor 3 corrigió «ninguna verificable»
  (el plazo SÍ es verificable; lo correcto es «ninguna verificada»).
- Extra: el integrador 3 rescató el punto del ancla de 3.200 €
  (nada demuestra que sea el precio normal) que ambas fusiones
  habían dejado caer; los revisores añadieron huecos que los 6
  solucionadores pasaron por alto (duración del máster, identidad
  legal, calendario de cuotas, comprobante de pago).

## Coste por nivel (corrida válida)

| Nivel | Agentes con Dirsi | Resultado (banco) |
|---|---|---|
| Bajo | 0 | 3/3 |
| Medio | 2 | 3/3 |
| Alto | 6 | 3/3 |
| Extra | 12 | 3/3 |

Puntuadores ciegos (fuera, viendo la situación): 2. Total de la
corrida válida: 22 agentes. Total de la noche en calibración: 55
(22 válidos + 28 de la corrida v1 superseded + 5 del error de las
«3 parejas», ambos excluidos de estos resultados).

## Limitaciones

1. **Los criterios del banco no discriminan.** Son binarios por
   elementos; cualquier solución competente aprueba. La diferencia
   real (profundidad) no está en ellos.
2. **Bajo P-03 está contaminado.** Dirsi había visto los resúmenes
   de la corrida v1 antes de su pase en solitario (incluido el
   hallazgo del endpoint compuesto); su primer grep literal dio 4/6
   y lo corrigió tras ver el hallazgo. El Bajo P-03 no es una medida
   limpia. La comparación 2/6/12 no se ve afectada.
3. **Una sola corrida, 3 tareas.** Sin repetición no hay varianza;
   con 3 tareas no hay generalización a otros tipos de trabajo.
4. **Techo de las tareas.** P-02, P-05 y P-03 son tareas que un solo
   agente competente resuelve bien; el techo se alcanza en Bajo y
   los niveles superiores solo añaden profundidad, no resultado.
5. **Trabajo excluido.** La corrida v1 (27 trabajadores + coordinador,
   diseño sin corregir) y las «3 parejas» de Medio (5 agentes, un
   equipo por tarea en vez de uno por nivel) están archivadas y NO
   cuentan en estos resultados.

## Veredicto sobre la escala

- Los números 2/6/12 **no quedan calibrados** por esta corrida: en
  el único instrumento de medida disponible (los criterios del
  banco), todos los niveles empatan a 3/3.
- Lo que la corrida SÍ demuestra: (a) Dirsi sola resuelve bien
  estas 3 tareas; (b) más agentes añaden profundidad y cazan errores
  reales que los niveles inferiores dejan pasar; (c) el instrumento
  de medida es el cuello de botella, no los equipos.
- Para calibrar de verdad hacen falta: criterios con gradación
  (contar razones válidas, verificaciones, comprobaciones) o tareas
  más duras donde Bajo falle y los niveles superiores no. Esa es la
  siguiente corrida, cuando Antonio lo decida.

## Archivos

- Soluciones Bajo: `soluciones-bajo/`
- Equipos: `equipos/medio/`, `equipos/alto/`, `equipos/extra/`
  (borradores, fusiones, `trabajo.md` con el rastro completo)
- Puntuación ciega: `puntuacion-ciega/` (12 copias ciegas,
  `CRITERIOS.md`, `puntuacion-A.md`, `puntuacion-B.md`)
- Mapa ciego (privado): `MAPA-CIEGO-2.md`
- Excluidos: `trabajo/excluido-nivel-1/`,
  `trabajo/protocolo-v1-superseded/`,
  `equipos/archivo-parejas-por-tarea/`
