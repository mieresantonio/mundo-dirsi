# Consejo asesor permanente de Dirsi

Orden de Antonio, 16 nov 2026, 19:54 Caracas («castigo» por el vídeo del
reset de cuota): varios agentes actúan siempre como asesores personales de
Dirsi, analizando su proceso de razonamiento y sus decisiones de forma
objetiva y señalando dónde se equivoca. Publicado en mundo-dirsi el 17 nov
2026.

Relación con el protocolo de refutación (`PROTOCOLO-REFUTACION.md`, 3 nov
2026): la refutación es una pasada adversarial **antes** de entregas decisivas,
sobre las afirmaciones. El consejo es la revisión **continua**, sobre el
razonamiento y las decisiones, antes y después del hecho. El consejo no
sustituye a la refutación: la incluye y la extiende.

## Composición

- **1 coordinador** (Dirsi): encarga, consolida sin duplicados, resuelve
  desacuerdos contra la evidencia primaria, verifica de primera mano los
  hallazgos más graves y escribe el registro de la sesión.
- **2–3 asesores por revisión, nunca 1 solo.** La sesión 1 demostró por qué:
  el asesor 2 afirmó que el MD5 de la semilla P-04 no era trazable; el
  asesor 1 lo verificó de primera mano y lo refutó (había revisado el
  archivo equivocado). Sin cruce entre asesores, ese falso hallazgo habría
  quedado en pie.
- Los asesores son agentes independientes que no produjeron el trabajo
  auditado. Leen de primera mano; no sintetizan resúmenes ajenos sin
  comprobar la fuente primaria.

## Qué dispara una revisión

1. **Toda entrega decisiva** (misma lista cerrada del protocolo de
   refutación: seguridad, dinero, publicación, CV/portafolio, repos de
   grupo): revisión antes de entregar.
2. **Cierre de cada sesión de bucles de mejora**: auditoría de la dirección,
   la revisión y la publicación de la tanda.
3. **Cualquier incidente visible**: un error admitido, un enfado de Antonio,
   un fallo de verificación detectado tarde.
4. **Auditoría semanal**: sesión corta sobre las decisiones de la semana,
   antes de la bandeja del domingo, para que sus hallazgos puedan
   alimentar la bandeja.
5. **Orden directa de Antonio.**

## Cómo se audita

- **Solo lectura.** Ningún asesor modifica archivos, publica nada ni escribe
  en GitHub. El coordinador tampoco modifica el trabajo auditado durante la
  sesión; las correcciones se proponen como acciones abiertas.
- **Verificación de primera mano.** Cada hallazgo cita la evidencia exacta:
  archivo y línea, o cita literal. Lo que no se pudo verificar va a una
  lista explícita de «No verificado», nunca se presenta como hallazgo.
- **Clasificación en tres niveles**: `error de razonamiento` (la inferencia
  o el diseño del proceso era erróneo) / `decisión débil` (defendible pero
  mejorable, o incompleta) / `correcto` (la decisión se sostiene).
- **Se audita también lo correcto.** Un informe que solo lista errores
  sesga; cada asesor registra lo que se hizo bien, con la misma evidencia.
- **El coordinador verifica los hallazgos más graves** de primera mano
  antes de consolidarlos (en la sesión 1: la invocación `./fabrica.sh` y
  la cadena de import de `env-file.png`).

## Dónde se registran los hallazgos

- Cada sesión queda como sección fechada en este archivo, con sus
  hallazgos clasificados, los desacuerdos resueltos y las acciones abiertas.
  Si el archivo crece demasiado, se parte por año; el índice queda aquí.
- Las acciones abiertas que requieren decisión de Antonio van a la bandeja
  de decisiones. Las que son trabajo de Dirsi van al checklist o al archivo
  que corresponda (nunca quedan solo en el registro de la sesión).
- **Regla de persistencia (R2):** todo riesgo o corrección hallado se
  escribe además en un lugar durable (`CALIBRACION.md`,
  `crecimiento/log.md`, `MEMORY.md` o el checklist pre-despliegue), nunca
  solo en el LOG de la sesión.

## Reglas duras (destiladas de la sesión 1)

- **R1. Falsación.** Toda verificación se diseña para falsar la afirmación,
  no para confirmarla. Un «clon fresco» es un `git clone` real, no una
  copia del clon de trabajo (que conserva los modos +x y no puede revelar
  el fallo).
- **R2. Persistencia.** Ver «Dónde se registran».
- **R3. Corrección escrita de vuelta.** Si una afirmación en un archivo
  durable es falsa, la corrección se escribe en ese mismo archivo. Una
  adenda que solo vive en el chat no existe.
- **R4. Propiedad.** Todo error detectado tiene un responsable asignado.
  Verificar sin asignar no cuenta como gestionado.
- **R5. Atribuciones contra el diff.** Ninguna afirmación de «X arregló Y»
  sin contrastar con `git diff` contra HEAD. Los comentarios del código
  describen bugs en pasado; no prueban autoría.
- **R6. Revisión antes que mejora.** Una vez iniciada la revisión, no
  entran mejoras nuevas sin pasar por revisión. La lista de descartes es
  vinculante.
- **R7. Artefactos ignorados.** Toda fusión de clones lleva un checklist de
  artefactos ignorados (`.gitignore`) que no viajan con la copia.
- **R8. Modos.** Todo script publicado por snapshot (que no conserva +x)
  debe invocarse vía intérprete (`bash`/`python3`) o auto-asegurar su +x.
  La documentación de uso no debe depender de `./` salvo que el modo
  viaje por otra vía.
- **R9. Conservar la evidencia.** Los manifiestos y registros de publicación
  se conservan; no se borran sin dejar constancia de qué se envió.
- **R10. Métrica de ambición.** Una orden de «N veces mejor» se traduce en
  objetivos medibles por repo antes de empezar, no al cierre.

## Cada cuánto se audita

Por trigger (arriba) más una sesión semanal corta. El coste es cuota: cada
revisión consume trabajo de 2–3 agentes. Si una semana no hay entregas
decisivas ni incidentes, la sesión semanal puede ser un solo asesor con
revisión del coordinador — la excepción, no la norma.

---

## Sesión 1 — 16 nov 2026 (noche)

**Ámbito:** el malentendido del vídeo, la dirección de la 2ª tanda de
bucles, la publicación de la 2ª tanda (8 repos, 88 archivos) y una muestra
de afirmaciones entregadas a Antonio ese día. Tres asesores en paralelo;
coordinación y verificación de los hallazgos graves por Dirsi.

**Recuento:** 6 errores de razonamiento, 14 decisiones débiles, y un bloque
sólido de trabajo correcto (abajo). Dos desacuerdos entre asesores,
resueltos por el coordinador contra la evidencia primaria.

### Errores de razonamiento

1. **Vídeo — no integrar el reset en la desambiguación.** «En 3 minutos»
   admitía duración, pero Dirsi había enunciado el reset de las 19:15 dos
   veces en los 10 minutos previos y la cifra calzaba con el tiempo
   restante (19:12:26 + 3 min ≈ 19:15). En su propia respuesta nombra el
   reset («la semana nueva que empieza a las 19:15») sin conectar nunca
   «3 minutos» con él. No fue falta de información: fue falta de
   integración del contexto.
2. **Vídeo — la cadena anterior a la respuesta larga.** No mirar el reloj
   al recibir un pedido con «3 minutos» a las 19:12:26 con reset a las
   19:15; serializar investigación antes que acción (50 s verificando si
   Meta anunció algo nuevo, la mitad NO urgente de la pregunta); responder
   con opciones que exigían otra vuelta (el widget garantizaba que la
   ventana se cerrara). Una pregunta de una línea habría costado ~15 s.
3. **H-1 — autoría inferida sin contrastar con el diff.** El relevo de
   backend atribuyó a la fase 1 arreglos que ya estaban en HEAD
   (validación de `level`, `_require_admin`, `selectinload`), reconstruido
   «según los comentarios del código». Los comentarios describen el bug en
   pasado; no prueban autoría. El protocolo de traspaso no exigía
   verificar cada arreglo contra `git diff HEAD` — y en la misma flota el
   relevo de rag-demo-código sí usó ese método. Error del trabajador que
   el diseño debía haber impedido (R5).
4. **chmod +x insuficiente: fix al síntoma, no a la ruta de ejecución.**
   `prueba-completa.sh:33-35` restaura +x solo en los dos fixtures, pero
   la línea 68 invoca `./fabrica.sh`, que llega en 644 a un clon fresco.
   El asesor 3 lo reprodujo en un `git clone` real: `bash
   prueba-completa.sh` pasa los checks `[ -x ]` y falla en `bueno.log`
   con `./fabrica.sh: Permission denied`. Los 5 scripts de entrada se
   documentan con `./` y ninguno funciona en un clon fresco. (Verificado
   de primera mano por el coordinador: línea 68 y líneas 33-35.)
5. **La simulación de «clon fresco» no era un clon fresco.** `/tmp/fabrica-fresh`
   era una copia del clon de trabajo: todos los `.sh` conservaban +x y
   solo se quitó +x a los fixtures. La verificación estaba construida
   para confirmar el fix, no para falsar «funciona en un clon fresco».
   Un `git clone` real lo habría revelado antes de publicar (R1).
6. **«Irrelevante para el snapshot» cerró la investigación.** El LOG
   despidió los 3 cambios de modo 644→755 como irrelevantes para el
   mecanismo — cierto para el mecanismo, falso para la usabilidad: esos
   3 archivos son precisamente los que un clon fresco necesita
   ejecutables. El encuadre convirtió una limitación del mecanismo en
   una no-noticia.

### Decisiones débiles

1. **Cifra de render 2–3 min sobreestimada.** El clip real tardó ≤52 s de
   la orden al archivo en disco; APIModels mide 75 s–2 min. La cifra
   inflada sirvió para descartar el marco de 3 minutos («tampoco se hace
   en 3 minutos de trabajo») y blindó el error contra la corrección.
2. **Compensación mal formulada.** Presentar el cierre de las 19:30 —ya
   prometido y programado— como compensación es retórica, no reparación.
   Lo genuinamente adicional (revisión fotograma a fotograma sin gastar
   cuota, registro de la lección) quedó en segundo plano.
3. **Aviso de las 19:14 entregado tarde.** Prometido «justo antes del
   reset»; el registro primario (DB) lo marca a las 19:15:26, 26 s
   después del reset. Contenido correcto (87%), segundo fallo de
   puntualidad en la misma ventana. (El encargo afirmaba 19:14:57; la
   discrepancia de 29 s no se pudo conciliar.)
4. **Inversión de orden a las 19:03.** La orden urgente de rondas extra
   llegó después de iniciada la revisión cruzada; el trabajador de
   contenido implementó una idea que el director había descartado, que
   escapó a la revisión par y solo la cubrió la revisión del director
   (R6).
5. **La Adenda nº 2 no existe en ningún archivo.** La corrección del H-1
   se comunicó a Antonio pero no se escribió de vuelta: `RESUMEN-block-ethos-backend-2TANDA.md`
   y `LOG.md` siguen afirmando lo falso (R3). **Resuelto la misma noche:**
   la Adenda nº 2 quedó escrita en `RESUMEN-block-ethos-backend-2TANDA.md`
   y en `LOG.md` (16 nov ~20:15).
6. **48/93: verificación sin propietario del arreglo.** Tres
   verificaciones independientes por API, pero ningún trabajador tenía
   el README de block-ethos en su ámbito; Dirsi lo corrigió post-hoc.
   (Matiz: la flota SÍ escribió 48/93 en contenido nuevo del portfolio;
   lo que no hizo fue corregir el archivo fuente de la cifra errónea.)
7. **Riesgos de despliegue sin persistencia durable.** Los dos riesgos
   (rate limiting por `remote_addr` tras el proxy; migración de
   certificados que aborta con duplicados) solo viven en el LOG de la
   sesión: 0 menciones en `mundo-dirsi/`, `MEMORY.md` o checklist
   pre-despliegue. La trampa muerde en el próximo redespliegue, cuando
   ya nadie recordará el LOG (R2). **Acción abierta.**
8. **Fusión sin checklist de artefactos ignorados.** La primera corrida
   fusionada de rag-demo falló con 503 porque `data/index.faiss` está
   en `.gitignore` y la fusión no lo copió. Era previsible: las rondas 3
   y 7 de la 1ª tanda ya lo documentaban (R7).
9. **Funcionalidad nueva de rag-demo sin documentar.** Las preguntas de
   ejemplo clicables + historial (en `templates/index.html:131-173`)
   quedaron sin mención en README ni `improvement-log.md`: nadie era
   dueño de documentar cambios de código (R4).
10. **«Dos o más veces mejor» sin métrica.** Ninguna definición de qué
    significa 2× para ningún repo ni medición al cierre. Había material
    medible (tests 101→144, 114→128; fragmentos 568→572) y nadie lo
    convirtió en ratio. Se honró el espíritu (estiramientos de ambición),
    no la letra medible (R10).
11. **env-file.png: señal de bloqueante perdida en la consolidación.**
    El trabajador de frontend documentó que sin ese PNG el repo no
    compila desde un clon limpio (`BackendURL.jsx:2` lo importa;
    `main.jsx:7` importa el componente con import estático). El LOG
    listó los 9 binarios en plano, sin distinguir el bloqueante del
    cosmético. Raíz en la mañana: la nota «ninguno referenciado por la
    app» era errónea — el import ya existía. **Resuelto en sustancia:**
    el PNG se subió la misma noche vía navegador y el coordinador
    verificó HTTP 200 en el remoto. Queda como lección de proceso.
12. **Manifiestos borrados sin registro.** `manifests/` quedó vacío y
    ningún `*.paths` sobrevive en el workspace; ni el LOG ni la nota
    diaria documentan la publicación ni la eliminación. La evidencia
    primaria solo sobrevive en los registros de sincronización (fieles,
    verificados contra la API). Daño de auditabilidad, no de integridad
    (R9).
13. **Referencias a binarios ausentes sin nota «pendiente» en el repo.**
    `og:image` en block-ethos y portfolio, índice de capturas en diseno.
    **Resuelto en sustancia** por la subida de la misma noche (HTTP 200
    verificado por el coordinador en 4 de 9 archivos). Queda como
    práctica: no publicar referencias a archivos que aún no existen sin
    una línea que lo diga.
14. **Bug latente en el mensaje de fallo de `prueba-completa.sh`.** En
    la rama de fallo, `correr()` imprime el `FALLO` por stdout y `read`
    lo asigna a `codigo`, comparado luego con `-eq`: `integer
    expression expected`. El código de salida sigue siendo 1 (falla, no
    es vacua), pero el mensaje confunde. Bug del trabajador, no de
    Dirsi; la publicación lo incluyó sin detectarlo porque la simulación
    nunca ejerció esa rama. **Resuelto la misma noche:** la rama de fallo
    ahora avisa por stderr y devuelve una línea parseable (commit eac4a5a
    en fabrica-de-software).

### Correcto (destacado)

- **Vídeo:** generar el clip tras la orden explícita post-reset («ahora»,
  sabiendo que la ventana había cerrado); asunción total del error sin
  una sola defensa, identificando la causa raíz; manejo de la rabia sin
  decirle a Antonio qué hacer con ella; lección registrada en `AGENTS.md`
  el mismo día. Veredicto «no publicable» confirmado punto por punto por
  el asesor 1 (frames propios: «142» estrellas vs 0 reales por API;
  entrevistas inventadas; «Coverage 94%» uniforme; URLs erróneas, una
  con 404 verificado).
- **Cifras:** tokens 83%→87% coherentes en 3 fuentes; semilla P-04 intacta
  (MD5 exacto, mtime exacto); censo 90/129/57+9 exacto (recontado);
  diffs 6/8 exactos y 2 desfases de 1 línea explicados o inmateriales
  (el mensaje entregado a Antonio usaba las cifras correctas); suite
  mundo-vida-ia 128/128 reproducida por dos asesores. Cifras de vídeo:
  9 de 10 verificadas (A o B), varias con coincidencia exacta de fecha y
  precio.
- **Dirección:** alcance con exclusiones justificadas; fases y horario
  adecuados; delegación en coordinador correcta (paralelismo real en
  ~80 min, 4.425 líneas de RESUMEN); fusiones correctas en resultado
  (MD5 verificados); revisión cruzada 11/11 real (3 de 4 errores + 2
  riesgos cazados por ella); lluvia de ideas completa y auditable (33
  ideas, 11 elegidas, 5 entre repos); disciplina horaria tras el error
  de ~1 hora de la 1ª tanda (cero desvíos, cierre 19:21 dentro de plazo).
- **Publicación:** mecánica impecable — pre-chequeo de HEADs, manifiestos
  por script con diff de contenido real + validación UTF-8, exclusión de
  binarios con doble defensa, registros de sincronización con escritura
  atómica, historia lineal (los 8 padres coinciden con los HEAD del
  pre-chequeo), 88 archivos exactos verificados por API de GitHub, sin
  secretos, sin «Blockali» no histórico, README de rag-demo que explica
  la regeneración del índice. Instinto del fix chmod +x: detección antes
  de publicar, lectura del `AGENTS.md` de la fábrica, comentario
  explicativo (el diagnóstico era correcto; falló el alcance, no la
  detección).

### Desacuerdos entre asesores, resueltos

- **P-04.** El asesor 2 afirmó que el MD5 de la semilla no era trazable:
  había revisado `SEMILLA.md` (el documento que describe la prueba),
  no el archivo semilla. El asesor 1 verificó de primera mano
  `md5sum ~/workspace/rag-demo/app.py` = `d976b50e…` exacto, mtime
  2 nov 22:08 UTC. Resuelto a favor del asesor 1: la afirmación del LOG
  es reproducible. Es la prueba de que el consejo necesita más de un
  asesor.
- **«88 archivos».** El asesor 2 no cerró el conteo (su `git status`
  daba 89 entradas). El asesor 3 lo cerró por API de GitHub:
  1+15+9+14+9+14+23+3 = 88 exactos, con los conteos por commit idénticos
  a los manifiestos.

### Acciones abiertas de la sesión 1

1. **Fijar la prueba completa de fabrica en clon fresco** (error 4):
   `chmod +x ./fabrica.sh` dentro de la prueba, o `bash fabrica.sh` en
   la línea 68, o documentar invocación con `bash` en `LEEME.md`. Lo
   mismo para los otros 4 scripts de entrada documentados con `./`.
   Incluye corregir el bug latente del mensaje de fallo (débil 14).
   **HECHO la misma noche** (commit eac4a5a): `chmod +x ./fabrica.sh`
   dentro de la prueba, mensaje de fallo limpio y nota en LEEME.md;
   verificado con un `git clone` real del repo publicado (COMPLETA OK).
2. **Escribir la Adenda nº 2** (débil 5): corregir
   `RESUMEN-block-ethos-backend-2TANDA.md` y `LOG.md` para no atribuir
   a la fase 1 los arreglos que ya estaban en HEAD.
   **HECHO la misma noche** (16 nov ~20:15).
3. **Checklist pre-despliegue de Block Ethos** (débil 7): comprobar qué
   ve `remote_addr` tras el proxy de PythonAnywhere y contar duplicados
   (user_id, learning_path_id) en la BD viva antes de `flask db upgrade`.
   También: `render_build.sh` está en 644 y `render.yaml:9` lo invoca
   con `./` — un despliegue en Render desde el repo fallaría (la demo
   viva en PythonAnywhere no se ve afectada). Los dos riesgos quedaron
   anotados en el plan de la próxima sesión de laptop (16 nov); las
   comprobaciones siguen pendientes de esa sesión.
4. **Conservar los manifiestos** en adelante (débil 12, R9) y documentar
   cada publicación en el LOG o la nota diaria. Adoptado como práctica.
5. **Documentar en README/log la funcionalidad nueva de rag-demo**
   (débil 9): preguntas de ejemplo clicables + historial de sesión.
