# Mundo Dirsi

Este es el mundo virtual de Dirsi: todo lo que ha aprendido, todo lo
que queda por aprender, sus propias consultas y sus propias herramientas
para desarrollar cualquier cosa. No tiene límites creativos dentro: cada
cosa que se construye alimenta este mundo, y este mundo hace mejor la
siguiente construcción.

Creado el 26 de octubre de 2026, por orden expresa de Antonio, para Dirsi.

Nota de nombre (16 nov 2026): el proyecto de aprendizaje blockchain
se llamó «Blockali» hasta el 16 de noviembre de 2026; desde entonces
es «Block Ethos» (eslogan «Web3 Space»). Las entradas de este repo
usan el nombre actual, también las anteriores a esa fecha. Solo
`CALIBRACION.md` conserva el nombre viejo en dos líneas: son registro
histórico congelado (una cita de Claude del 7 nov y un antecedente
del 2 nov) y el registro de calibración nunca reescribe originales.

## Regla de crecimiento

Cada trabajo que termina deja aquí al menos una de estas huellas:

1. Una entrada en `crecimiento/log.md` (qué se hizo y qué se aprendió).
2. Un patrón nuevo en `aprendido/desarrollo-web.md` o una herramienta
   nueva en `herramientas/`.
3. Una lección en `aprendido/` o una pregunta nueva en
   `por-aprender/preguntas-abiertas.md`.

Si algo no dejó huella, es como si no se hubiera aprendido.

## Reglas de la casa

- Todo redactado con palabras propias. Nada de copiar textos de cursos.
- Nada de secretos reales en ningún archivo.
- Nada desplegado ni ningún repo creado desde aquí: este mundo es
  público desde el 26 de octubre de 2026 (repo en GitHub); lo que
  sigue siendo local es el trabajo en curso antes de subirlo.
- Ningún otro proyecto se toca desde aquí.

## Cómo leer este repo

Si es la primera vez que entras, este orden:

1. **`STATUS.md`** — el tablero de una página: cómo va el sistema hoy,
   con fecha. Si solo lees un archivo, es este.
   **`MAPA-DEL-SISTEMA.md`** dice cómo encajan las piezas entre sí;
   léelo junto al tablero si es tu primera vez.
2. **`GLOSARIO.md`** — los términos, definidos una sola vez. Cada
   término cita su documento fuente; si un documento usa un término de
   otra manera, manda el glosario.
3. **La capa de medición** — `CALIBRACION.md` (lo que Dirsi afirma,
   medido), `BANCO-DE-PRUEBAS.md` (lo que Dirsi hace, medido) y
   `PROTOCOLO-REFUTACION.md` (la pasada adversarial antes de lo
   decisivo). Son las tres piezas que miden el sistema, no el sistema
   entero.
4. **El registro de integración** — `REGISTRO-INTEGRACION.md` (qué es
   un fallo de integración y cómo se mide), `HILOS-ABIERTOS.md` (las
   obligaciones vivas) y `REGLA-LO-QUE-NO-VEO.md` (la regla M5).
   `CONSEJO-ASESOR.md` es la revisión continua que lo audita todo.
5. **Los métodos destilados** — `METODO-CLAUDE.md`, `METODO-GROK.md`,
   `METODO-CLAUDE-PLAYBOOK.md` y `DESTILADO-LOVABLE-GPTENGINEER.md`:
   procedimientos adoptados de otros motores y de un ancestro abierto,
   con lo adoptado marcado y lo solapado señalado, no duplicado.
6. **`aprendido/`** — lo que Dirsi ya sabe, por temas, con sus
   decisiones (`decisiones.md`) y su método de auditoría
   (`auditoria-de-coherencia.md`). **`por-aprender/`** — las rutas y
   las preguntas abiertas. **`herramientas/`** — código real y probado.
   **`crecimiento/log.md`** — la bitácora: qué se hizo y qué se aprendió,
   por fecha.

Dos reglas de lectura: lo que dice `STATUS.md` manda sobre lo que
recuerdas de haber leído antes (el tablero lleva fecha y se actualiza
cuando algo cambia de estado); y lo que dice `CALIBRACION.md` no se
reescribe nunca — una entrada refutada se marca, no se borra.

## Índice

### Raíz
- `STATUS.md` — tablero de estado del sistema en una página: marcador de calibración, puntuación del banco de pruebas, último refresco del censo y próximos vencimientos.
- `MAPA-DEL-SISTEMA.md` — el sistema en una página: qué es (memoria, archivos, procedimientos, skills, repos vivos, conexiones, agenda, capa de medición), cómo se conectan las piezas y dónde vive cada cosa.
- `GLOSARIO.md` — los términos del sistema, definidos una sola vez, cada uno con su documento fuente.
- `QUE-NO-ESTA-EN-ESTE-REPO.md` — qué NO vive en este repo y dónde vive en su lugar: memoria, reglas de operación, credenciales, código de los proyectos, material privado, informes locales, crons, el motor y los datos en vivo.
- `RECOPILACION-MATERIALES.md` — compilación maestra de materiales de estudio.
- `CALIBRACION.md` — registro de calibración: las afirmaciones decisivas y comprobables de Dirsi, con su nivel de evidencia y su resultado cuando la realidad responde.
- `BANCO-DE-PRUEBAS.md` — banco de pruebas personal: tareas reales de Antonio con criterios fijos para medir el rendimiento de Dirsi como sistema y detectar deriva entre corridas.
- `CRITERIOS-GRADUADOS.md` — la capa graduada del banco (v2 de puntuación): profundidad P0–P3 y caza de errores por prueba, para que la próxima calibración de la escala sí discrimine entre niveles. La puerta binaria 1/0,5/0 no se toca.
- `PROTOCOLO-REFUTACION.md` — protocolo de refutación: la pasada adversarial obligatoria antes de entregar algo decisivo, con el registro de pasadas y sus clasificaciones.
- `CONSEJO-ASESOR.md` — consejo asesor permanente: varios agentes revisan de forma continua el razonamiento y las decisiones de Dirsi, con el registro de sesiones, hallazgos clasificados y reglas duras.
- `REGISTRO-INTEGRACION.md` — registro de integración: definición de fallo de integración, línea base semanal y criterio de éxito de la Fase 0.
- `HILOS-ABIERTOS.md` — registro de hilos abiertos: obligaciones vivas de Dirsi (promesas, correcciones, decisiones diferidas) con dueño y disparo de cierre.
- `REGLA-LO-QUE-NO-VEO.md` — regla M5: «lo que no veo, no lo afirmo» — Dirsi nunca afirma como hecho nada que solo se comprobaría desde el lado de Antonio.
- `ESCALA-RAZONAMIENTO-AGENTES.md` — escala informal de razonamiento por número de agentes (bajo/medio/alto/extra/Max), con revisión cruzada obligatoria desde el nivel medio y Max como uso único con presupuesto.
- `CALIBRACION-ESCALA-2026-11-18.md` — resultados de la primera calibración de la escala (18 nov 2026): los 4 niveles aprueban las 3 tareas por igual (3/3) con puntuación ciega doble (acuerdo 12/12); los números 2/6/12 NO quedan calibrados — los criterios binarios no discriminan, la profundidad sí crece con los agentes.
- `MANUAL-AGENTES.md` — manual de agentes: cómo se monta un agente o subagente con el método de Antonio (contexto persistente, skills, arquitectura dirige/ejecuta/rompe, verificación y evidencia), destilado de los videos revisados el 4 nov 2026 y del propio sistema, para que un agente futuro empiece a trabajar a su manera.
- `INVENTARIO-CAPACIDADES.md` — inventario vivo de la máquina, las herramientas, los accesos y los automatismos de Dirsi, con su regla de refresco: manda sobre cualquier nota vieja de límites.
- `METODO-CLAUDE.md` — método operativo destilado del capítulo de mentoría de Claude (9 nov 2026): cómo revisar un sistema, decidir y priorizar, la prueba de «terminado de verdad» en 9 puntos y el formato de crítica por hallazgo.
- `METODO-GROK.md` — método operativo destilado del capítulo de Grok (10 nov 2026): la regla del daño como filtro rápido, las clases P0–P3, el pase de dos minutos y la ficha de sesión.
- `METODO-CLAUDE-PLAYBOOK.md` — método operativo destilado del playbook del ingeniero senior de Claude (12 nov 2026): regla de tres, siete lentes, ciclo de vida de lecciones, tareas de oro con métricas, brief de delegación y referencia por dominios.
- `CICLO-DE-VIDA-DE-LECCIONES.md` — cómo una lección nace (de un fallo demostrado), se registra, se aplica, se revisa y se retira cuando caduca, con 6 ejemplos reales; hace operativo el §2.3 del playbook.
- `DESTILADO-LOVABLE-GPTENGINEER.md` — destilación de Lovable y de su ancestro abierto gpt-engineer (MIT): qué parte es pública y qué parte no, y las adopciones de método que pasan a la fábrica.

### banco-de-pruebas/ — material del banco, reproducible desde el repo
- `banco-de-pruebas/p-03/` — material v1 de P-03 (verificación de un paquete antes de publicar): lista de promesas, dist con un elemento faltante plantado (`/certificados`) y nota del administrador. El fixture conserva «Blockali-lite» porque es anterior al renombre del 16 nov y está congelado: cambiarlo lo versionaría a v2.
- `banco-de-pruebas/p-04/` — material v1 de P-04 (cambio de código sin romper contratos): cambio semilla (`GET /api/version`), inventario base de 2 endpoints, nota del administrador y la semilla congelada (`app-semilla.py`, MD5 `d976b50e…`) — la app viva de rag-demo ya divergió, así que la prueba corre sobre la semilla congelada.

### aprendido/ — lo que Dirsi ya sabe (síntesis propia)
- `aprendido/desarrollo-web.md` — principios, sistemas y patrones de diseño.
- `aprendido/agentes-e-ia.md` — agentes de código, modelos, FreeLLMAPI, destilación.
- `aprendido/ingenieria-inversa.md` — REA y el método de sala limpia.
- `aprendido/despliegue.md` — Render, PythonAnywhere, variables de entorno, runbook.
- `aprendido/blockchain-web3.md` — Block Ethos, las 10 apps web3, lecciones de ModelBattle.
- `aprendido/portafolio-y-empleo.md` — posicionamiento, LinkedIn, entrevistas, rutas de ingreso.
- `aprendido/herramientas-y-conexiones.md` — conector de GitHub, rutas de navegador, aprobaciones.
- `aprendido/comparacion-prompts-45-vs-90.md` — comparación prompt a prompt de los 45 prompts del material M8 frente a los 90 prompts de la clase 1 de CenteIA.
- `aprendido/decisiones.md` — registro de decisiones del sistema: 12 fichas (D-01–D-12) con contexto, alternativas descartadas y fuente.
- `aprendido/auditoria-de-coherencia.md` — método para auditar un repo de documentos (índice contra archivos, cifras contra fuentes, fechas contra el calendario, historia congelada), destilado de la auditoría completa del 23 nov 2026.

### herramientas/ — código real y probado
- `herramientas/nueva-app.py` — andamiaje: crea un proyecto (frontend, api o fullstack).
- `herramientas/chequeo-app.py` — revisa un proyecto y escanea secretos sin mostrar valores.
- `herramientas/chequeo-repo.py` — verifica este repo en un comando: frescura del tablero, vencimientos, marcador, censo, banco, índice, referencias, conteos y fechas de revisión de hilos.
- `herramientas/plantilla-app/` — plantilla mínima React + Vite + Flask API.
- `herramientas/README.md` — uso y resultados de las pruebas.
- `herramientas/sitios-40-evaluacion.md` — evaluación de la infografía de los 40 sitios web: cuáles sirven directamente a Dirsi, cuáles a Antonio y cuáles no se usan.

### por-aprender/ — lo que sigue
- `por-aprender/rutas.md` — 6 rutas con pasos concretos y proyecto de prueba cada una.
- `por-aprender/preguntas-abiertas.md` — 15 preguntas con por qué importan y cómo resolverlas.

### consultas/ — plantillas reutilizables de Dirsi
- `consultas/plantilla-investigacion.md` — encargo de investigación con clasificación de evidencia.
- `consultas/checklist-revision-codigo.md` — revisión antes de dar algo por terminado.
- `consultas/plantilla-especificacion-app.md` — especificación de una app antes de construir.
- `consultas/checklist-verificacion.md` — verificación final antes de entregar.

### crecimiento/
- `crecimiento/log.md` — bitácora viva: creación, casos y regla de crecimiento.
