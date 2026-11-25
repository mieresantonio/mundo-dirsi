# Mundo Dirsi

Este repositorio documenta el aprendizaje y las herramientas de Dirsi, agente personal de IA: todo lo aprendido, todo lo que queda por aprender, sus consultas y sus herramientas de trabajo. Cada trabajo realizado deja constancia aquí y mejora el siguiente.

El sistema que este repositorio documenta trabaja así: Antonio dirige y decide, describe la idea exacta del producto o proyecto y delega su construcción en Dirsi. Detrás trabajan varios agentes de IA a la vez — Dirsi dirige qué se construye, qué se modifica y qué se revisa — y Antonio verifica cada proyecto por su cuenta, revisando y ejecutando el código directamente.

Creado el 26 de octubre de 2026 por Antonio, para Dirsi, y publicado en GitHub desde ese día.

## Cómo crece este repositorio

Cada trabajo completado deja constancia aquí, en al menos una de estas formas:

1. Una entrada en `crecimiento/log.md` (qué se hizo y qué se aprendió).
2. Un patrón nuevo en `aprendido/desarrollo-web.md` o una herramienta nueva en `herramientas/`.
3. Una lección en `aprendido/` o una pregunta nueva en `por-aprender/preguntas-abiertas.md`.

## Alcance

- Todo el contenido está redactado con palabras propias; no se reproducen textos de cursos ni de terceros.
- El trabajo en curso se publica aquí una vez terminado.
- Su ámbito es la documentación, las herramientas y el registro de aprendizaje de este proyecto: no incluye despliegues, no crea otros repositorios y no modifica otros proyectos.

## Cómo leer este repositorio

Lectura recomendada para quien entra por primera vez, en este orden:

1. **`STATUS.md`** — el tablero de estado en una página, con fecha. Es el punto de partida recomendado. **`MAPA-DEL-SISTEMA.md`** explica cómo encajan las piezas entre sí.
2. **`GLOSARIO.md`** — los términos del sistema, definidos una sola vez, cada uno con su documento fuente. Cuando un documento usa un término de otra manera, prevalece la definición del glosario.
3. **La capa de medición** — `CALIBRACION.md` (las afirmaciones de Dirsi, medidas), `BANCO-DE-PRUEBAS.md` (su rendimiento, medido) y `PROTOCOLO-REFUTACION.md` (la pasada adversarial previa a lo decisivo). Son las tres piezas que miden el sistema.
4. **El registro de integración** — `REGISTRO-INTEGRACION.md` (qué es un fallo de integración y cómo se mide), `HILOS-ABIERTOS.md` (las obligaciones vivas) y `REGLA-LO-QUE-NO-VEO.md` (la regla M5). `CONSEJO-ASESOR.md` documenta la revisión continua que audita el conjunto.
5. **Los métodos destilados** — `METODO-CLAUDE.md`, `METODO-GROK.md`, `METODO-CLAUDE-PLAYBOOK.md` y `DESTILADO-LOVABLE-GPTENGINEER.md`: procedimientos destilados de otros sistemas de IA y de un proyecto abierto, con lo adoptado y lo solapado indicados en cada documento, sin duplicar contenido.
6. **`aprendido/`** — lo aprendido, por temas, con sus decisiones (`decisiones.md`) y su método de auditoría (`auditoria-de-coherencia.md`). **`por-aprender/`** — las rutas y las preguntas abiertas. **`herramientas/`** — código real y probado. **`crecimiento/log.md`** — la bitácora: qué se hizo y qué se aprendió, por fecha.

Quien vaya a trabajar en este sistema debe leer además, en primer lugar, **`ONBOARDING.md`**, que reúne en una sola página las reglas de trabajo.

Dos principios rigen la lectura de este repositorio: `STATUS.md` prevalece sobre cualquier lectura anterior, porque el tablero lleva fecha y se actualiza cuando algo cambia de estado; y las entradas de `CALIBRACION.md` no se reescriben nunca — una entrada refutada se marca como tal y se conserva.

## Índice

### Raíz
- `STATUS.md` — tablero de estado del sistema en una página: marcador de calibración, puntuación del banco de pruebas, último refresco del censo y próximos vencimientos.
- `ONBOARDING.md` — primera lectura para un agente nuevo que va a trabajar en este sistema: modo propuestas, la guarda, falsación, M5, refutación y dónde está cada cosa, en una sola página.
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
