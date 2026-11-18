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

## Índice

### Raíz
- `STATUS.md` — tablero de estado del sistema en una página: marcador de calibración, puntuación del banco de pruebas, último refresco del censo y próximos vencimientos.
- `GLOSARIO.md` — los términos del sistema, definidos una sola vez, cada uno con su documento fuente.
- `RECOPILACION-MATERIALES.md` — compilación maestra de materiales de estudio.
- `CALIBRACION.md` — registro de calibración: las afirmaciones decisivas y comprobables de Dirsi, con su nivel de evidencia y su resultado cuando la realidad responde.
- `BANCO-DE-PRUEBAS.md` — banco de pruebas personal: tareas reales de Antonio con criterios fijos para medir el rendimiento de Dirsi como sistema y detectar deriva entre corridas.
- `PROTOCOLO-REFUTACION.md` — protocolo de refutación: la pasada adversarial obligatoria antes de entregar algo decisivo, con el registro de pasadas y sus clasificaciones.
- `CONSEJO-ASESOR.md` — consejo asesor permanente: varios agentes revisan de forma continua el razonamiento y las decisiones de Dirsi, con el registro de sesiones, hallazgos clasificados y reglas duras.
- `REGISTRO-INTEGRACION.md` — registro de integración: definición de fallo de integración, línea base semanal y criterio de éxito de la Fase 0.
- `HILOS-ABIERTOS.md` — registro de hilos abiertos: obligaciones vivas de Dirsi (promesas, correcciones, decisiones diferidas) con dueño y disparo de cierre.
- `REGLA-LO-QUE-NO-VEO.md` — regla M5: «lo que no veo, no lo afirmo» — Dirsi nunca afirma como hecho nada que solo se comprobaría desde el lado de Antonio.
- `ESCALA-RAZONAMIENTO-AGENTES.md` — escala informal de razonamiento por número de agentes (bajo/medio/alto/extra/Max), con revisión cruzada obligatoria desde el nivel medio y Max como uso único con presupuesto.
- `MANUAL-AGENTES.md` — manual de agentes: cómo se monta un agente o subagente con el método de Antonio (contexto persistente, skills, arquitectura dirige/ejecuta/rompe, verificación y evidencia), destilado de los videos revisados el 4 nov 2026 y del propio sistema, para que un agente futuro empiece a trabajar a su manera.
- `INVENTARIO-CAPACIDADES.md` — inventario vivo de la máquina, las herramientas, los accesos y los automatismos de Dirsi, con su regla de refresco: manda sobre cualquier nota vieja de límites.
- `METODO-CLAUDE.md` — método operativo destilado del capítulo de mentoría de Claude (9 nov 2026): cómo revisar un sistema, decidir y priorizar, la prueba de «terminado de verdad» en 9 puntos y el formato de crítica por hallazgo.
- `METODO-GROK.md` — método operativo destilado del capítulo de Grok (10 nov 2026): la regla del daño como filtro rápido, las clases P0–P3, el pase de dos minutos y la ficha de sesión.
- `METODO-CLAUDE-PLAYBOOK.md` — método operativo destilado del playbook del ingeniero senior de Claude (12 nov 2026): regla de tres, siete lentes, ciclo de vida de lecciones, tareas de oro con métricas, brief de delegación y referencia por dominios.
- `DESTILADO-LOVABLE-GPTENGINEER.md` — destilación de Lovable y de su ancestro abierto gpt-engineer (MIT): qué parte es pública y qué parte no, y las adopciones de método que pasan a la fábrica.

### aprendido/ — lo que Dirsi ya sabe (síntesis propia)
- `aprendido/desarrollo-web.md` — principios, sistemas y patrones de diseño.
- `aprendido/agentes-e-ia.md` — agentes de código, modelos, FreeLLMAPI, destilación.
- `aprendido/ingenieria-inversa.md` — REA y el método de sala limpia.
- `aprendido/despliegue.md` — Render, PythonAnywhere, variables de entorno, runbook.
- `aprendido/blockchain-web3.md` — Block Ethos, las 10 apps web3, lecciones de ModelBattle.
- `aprendido/portafolio-y-empleo.md` — posicionamiento, LinkedIn, entrevistas, rutas de ingreso.
- `aprendido/herramientas-y-conexiones.md` — conector de GitHub, rutas de navegador, aprobaciones.
- `aprendido/comparacion-prompts-45-vs-90.md` — comparación prompt a prompt de los 45 prompts del material M8 frente a los 90 prompts de la clase 1 de CenteIA.
- `aprendido/decisiones.md` — registro de decisiones del sistema: 10 fichas (D-01–D-10) con contexto, alternativas descartadas y fuente.

### herramientas/ — código real y probado
- `herramientas/nueva-app.py` — andamiaje: crea un proyecto (frontend, api o fullstack).
- `herramientas/chequeo-app.py` — revisa un proyecto y escanea secretos sin mostrar valores.
- `herramientas/plantilla-app/` — plantilla mínima React + Vite + Flask API.
- `herramientas/README.md` — uso y resultados de las pruebas.
- `herramientas/sitios-40-evaluacion.md` — evaluación de la infografía de los 40 sitios web: cuáles sirven directamente a Dirsi, cuáles a Antonio y cuáles no se usan.

### por-aprender/ — lo que sigue
- `por-aprender/rutas.md` — 6 rutas con pasos concretos y proyecto de prueba cada una.
- `por-aprender/preguntas-abiertas.md` — 14 preguntas con por qué importan y cómo resolverlas.

### consultas/ — plantillas reutilizables de Dirsi
- `consultas/plantilla-investigacion.md` — encargo de investigación con clasificación de evidencia.
- `consultas/checklist-revision-codigo.md` — revisión antes de dar algo por terminado.
- `consultas/plantilla-especificacion-app.md` — especificación de una app antes de construir.
- `consultas/checklist-verificacion.md` — verificación final antes de entregar.

### crecimiento/
- `crecimiento/log.md` — bitácora viva: creación, casos y regla de crecimiento.
