# Qué no está en este repo

Este repo (mundo-dirsi) es la parte pública y compartible del
sistema de Dirsi: lo aprendido, los métodos, los registros de
medición. No es el sistema entero. Esta página dice explícitamente
qué NO vive aquí y dónde vive en su lugar, para que un lector
nuevo no busque en el sitio equivocado ni confunda una referencia
con un archivo del repo.

Por qué existe esta página: la auditoría de integración del
17 nov 2026 señaló confusión de ámbito — referencias a
`~/workspace/...` y a archivos del hogar de Dirsi que un lector
del repo no puede resolver — y la 1ª tanda de mejora del 23 nov
encontró la misma confusión viva (la copia local desfasada, el
material del banco solo en local). La página convierte «fuera de
este repo» de misterio en mapa.

## La tabla

| Qué | Dónde vive | Por qué no está aquí | Cómo se accede o se pide |
|---|---|---|---|
| Memoria personal de Antonio y de Dirsi (hechos, decisiones, personas, grupos) | `MEMORY.md`, `~/memory/` (hogar de Dirsi) | Privado: es la vida de Antonio, no material público | Preguntarle a Dirsi; ella lee su memoria cada sesión |
| Reglas de operación del día a día | `AGENTS.md`, `SOUL.md`, `USER.md`, `IDENTITY.md`, `TOOLS.md` (hogar de Dirsi) | Son las instrucciones vivas de Dirsi, no documentación del repo; cambian con cada sesión | No se piden: Dirsi las aplica. Lo que de ellas merece ser lección pública se destila a `aprendido/` |
| Credenciales, claves y secretos | Bóveda segura de Muse; los valores `.env`, en manos de Antonio | Un secreto publicado deja de ser secreto; este repo es público desde el 26 oct 2026 | Antonio los introduce él mismo cuando una app está lista, con guía de Dirsi. Nunca por chat |
| Código de los proyectos | Cada uno en su repo: block-ethos, rag-demo-asistente-documentos, fabrica-de-software, mundo-vida-ia, portfolio, diseno-web-investigacion | Cada proyecto tiene su propio repo, su historia y sus pruebas; mezclarlos aquí rompería ambos | En GitHub, `mieresantonio/<proyecto>` |
| Material privado de Antonio (fotos y vídeos del perro, documentos personales) | Su teléfono y su nube (cuando él los suba) | Privado y voluminoso; no existe acceso directo a su galería | Él los comparte por chat (máx. 10 por mensaje) o desde su copia en la nube |
| Material completo de la calibración de la escala (soluciones, copias ciegas, mapa ciego) | Workspace local `calibracion-escala-2026-11-18/` | El mapa ciego es privado por diseño: revelaría qué nivel produjo cada solución y contaminaría futuras puntuaciones | El informe de resultados basta y está en `CALIBRACION-ESCALA-2026-11-18.md` |
| Informes locales de trabajo (auditoría de integración, revisiones quincenales, sesiones de mejora) | Workspace local (`~/workspace/auditoria-integracion-2026-11-17/`, `~/workspace/goals/*/hidden_files/`, `~/workspace/mejora-repos-2026-11-23/`) | Son informes de trabajo con detalle operativo; el repo publica el destilado, no el informe | El destilado vive aquí (`REGISTRO-INTEGRACION.md`, `crecimiento/log.md`); el informe completo se pide a Dirsi |
| Crons y automatismos (revisiones quincenales, bandeja semanal) | Programador de tareas de Dirsi | Un cron no es un archivo del repo: es algo que se ejecuta en el sistema de Dirsi | Qué existe y cuándo corre: `INVENTARIO-CAPACIDADES.md` §4 y `STATUS.md` (vencimientos) |
| La cuota semanal de tokens y la suscripción | Cuenta de Muse de Antonio | Es estado de una cuenta, no un documento; cambia cada semana | Dirsi lo consulta cuando hace falta; el reset semanal es los lunes (hora variable) |
| El motor (Muse Spark 1.3) | Infraestructura de Muse | El repo mide el rendimiento del motor, no lo contiene | No se accede desde aquí: se trabaja con él y se mide con el banco |
| Datos en vivo (precios, disponibilidad, estado de un despliegue) | La fuente en vivo (la tienda, la plataforma, la demo) | Un dato en vivo copiado a un archivo nace desactualizado | Se verifican en el momento; el repo registra el método, no el dato |
| Conversaciones con Antonio | El chat | Las conversaciones son el trabajo en curso, no el archivo | El repo guarda lo destilado (decisiones, lecciones, preguntas); la conversación misma no se copia aquí |
| Versiones de trabajo en curso | Workspace local (`~/workspace/`) antes de subirlas | Lo que sigue siendo local es el trabajo en curso antes de publicarlo (regla de la casa del README) | Se publica cuando Antonio confirma; mientras, vive en local y se cita como tal |

## Lo que SÍ está aquí (para no confundirse)

- Lo aprendido (`aprendido/`), lo pendiente (`por-aprender/`),
  las plantillas (`consultas/`), el código pequeño y probado
  (`herramientas/`), la bitácora (`crecimiento/log.md`).
- La capa de medición (`CALIBRACION.md`, `BANCO-DE-PRUEBAS.md`,
  `PROTOCOLO-REFUTACION.md`), la vigilancia
  (`REGISTRO-INTEGRACION.md`, `HILOS-ABIERTOS.md`,
  `REGLA-LO-QUE-NO-VEO.md`, `CONSEJO-ASESOR.md`) y los métodos
  destilados (`METODO-*.md`, `DESTILADO-LOVABLE-GPTENGINEER.md`,
  `MANUAL-AGENTES.md`).
- El tablero (`STATUS.md`), el glosario (`GLOSARIO.md`) y este
  mapa (`MAPA-DEL-SISTEMA.md`).

## Regla de mantenimiento

Cuando nazca algo fuera del repo que un lector podría buscar aquí
(una herramienta nueva, un informe nuevo, un automatismo nuevo),
se añade una fila a esta tabla en la misma sesión. La auditoría
mensual del repo revisa si nació algo fuera sin su fila.
