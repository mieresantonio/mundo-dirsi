# Hilos abiertos

> Publicado en mundo-dirsi el 17 nov 2026 (Fase 0 de la auditoría de integración, aprobada por Antonio). Fuente: auditoría nocturna del 17 nov 2026 (`~/workspace/auditoria-integracion-2026-11-17/INFORME.md`, §3.4).

Registro de obligaciones vivas: preguntas de Antonio sin responder, promesas
de Dirsi pendientes, confirmaciones que ella espera, decisiones diferidas,
correcciones pendientes de escribir de vuelta. Resuelve fallos de persistencia
y seguimiento, no fallos de inferencia en primera pasada.

**Reglas:** cada hilo tiene dueño único y disparo de cierre observable y
verificable por un tercero (nunca «verificado» a secas). Tope de 12 activos
(ABIERTO + EN-ESPERA); antes de añadir el 13º hay que cerrar, promover a la
bandeja, fusionar o caducar uno en el mismo turno. Se lee una vez por sesión.
**Cero recordatorios a Antonio:** los hilos con dueño Antonio no generan
recordatorios automáticos; se mencionan como máximo en la bandeja semanal si
se promueven. Un ítem de la bandeja nunca se copia aquí; promoción en un solo
sentido (hilo que necesita decisión de Antonio y sobrevive >48 h → bandeja, se
cierra aquí con puntero `→ bandeja #N`).

**Alcance (aclaración 23 nov 2026):** las confirmaciones que esperan a un
cron SÍ entran al registro (p. ej. H-006): el hilo es el recordatorio de
verificar el resultado cuando el cron corra; el cron ejecuta, el hilo
verifica. Lo que no entra es el trabajo rutinario del cron en sí.

## Hilos

### H-001 — Riesgos de redespliegue de Block Ethos
- **Tipo:** PROMESA · **Estado:** EN-ESPERA · **Abierto:** 16 nov 2026 (2ª tanda)
- **Dueño:** Dirsi (sesión de laptop)
- **Disparo de cierre:** en la próxima sesión de laptop, antes de redesplegar,
  (1) confirmar qué ve `remote_addr` en producción tras el proxy
  (vía `ProxyFix` con un solo proxy de confianza) y (2) contar duplicados
  `(user_id, learning_path_id)` en la BD viva antes de aplicar la migración
  de unicidad de certificados. Ambos controles ya están en
  `~/workspace/plan-proxima-sesion-laptop.md` (sección 3).
- **Evidencia:** `~/workspace/plan-proxima-sesion-laptop.md`, sección 3.

### H-002 — Documentar la funcionalidad nueva de rag-demo
- **Tipo:** CORRECCIÓN · **Estado:** ABIERTO · **Abierto:** 16 nov 2026
  (consejo asesor, sesión 1)
- **Dueño:** Dirsi
- **Disparo de cierre:** el README publicado de rag-demo documenta las
  preguntas de ejemplo clicables y el historial, verificado por relectura
  del README publicado en GitHub.
- **Evidencia:** verificado 23 nov 2026 (revisión del sistema, clon fresco):
  README publicado (393 líneas, commit da95c69) no documenta preguntas
  clicables ni historial (`historial` 0, `clicable` 0, «preguntas de
  ejemplo» 0). La copia local (225 líneas, 2 nov) está desactualizada y no
  es repo git; el disparo se refiere a la copia publicada. (La evidencia
  del 17 nov apuntó a la copia local; la conclusión —abierto— es la misma
  en ambas copias.) Revisión cruzada del trabajador de rag-demo (23 nov,
  14:10): confirmó que los ejemplos clicables y el historial existen en
  código y que su propuesta de README los documenta; estado: documentado
  en propuesta, pendiente de publicar. **Este hilo NO se cierra en esta
  sesión:** la documentación la trabaja el trabajador de rag-demo de la
  sesión de mejora del 23 nov 2026; la coordinadora verificará el cierre
  por relectura del README cuando ese trabajo se publique.

### H-003 — Cifra 44/89 en archivos locales
- **Tipo:** CORRECCIÓN · **Estado:** CERRADO · **Abierto:** 17 nov 2026
  (auditoría, hallazgo L1) · **Cerrado:** 17 nov 2026
- **Dueño:** Dirsi
- **Disparo de cierre:** `~/workspace/block-ethos/README.md:129` dice 48/93.
- **Evidencia:** verificado 17 nov 2026: línea 129 dice
  «Soy el autor con más commits del repositorio original (48 de 93)».
  La mención restante de «44 de 89» en `mundo-dirsi/CALIBRACION.md:120`
  es registro histórico que cita el README viejo; se conserva a propósito,
  no es texto vigente.

### H-004 — Licencia de block-ethos
- **Tipo:** DECISIÓN-DIFERIDA · **Estado:** CERRADO (→ bandeja #10)
  · **Abierto:** 16 nov 2026
- **Dueño:** Antonio
- **Disparo de cierre:** promovido a la bandeja de decisiones (#10); no se
  duplica aquí.
- **Evidencia:** bandeja de decisiones, ítem 10.

### H-005 — `render_build.sh` de block-ethos en 644
- **Tipo:** CORRECCIÓN · **Estado:** ABIERTO · **Abierto:** 16 nov 2026
  (consejo asesor, sesión 1)
- **Dueño:** Dirsi
- **Disparo de cierre (reformulado 23 nov 2026):** el despliegue no depende
  del modo +x del archivo: `render.yaml` invoca vía `bash render_build.sh`
  (o el script auto-asegura su +x) y la documentación no depende de `./`,
  verificado en el repo publicado. Alternativa: modo +x en el repo
  publicado, si alguna vía lo entrega. (El disparo original exigía +x en
  el repo publicado, pero la subida por snapshot no conserva modos: tal
  como estaba redactado, el hilo era incerrrable por la vía de
  publicación disponible. La reformulación sigue la regla R8 del consejo.)
- **Evidencia:** verificado 23 nov 2026 (revisión del sistema, clon fresco):
  `100644` en GitHub (blob 6eb2490); copia local en 660. Sin +x. Nota: la
  evidencia del 17 nov citaba «644 (`-rw-rw----`)», internamente
  inconsistente: `-rw-rw----` es 660, no 644. El fondo (sin +x) era
  correcto. La demo viva en PythonAnywhere no se ve afectada; solo
  fallaría un despliegue en Render desde el repo.

### H-006 — Verificación de la corrección del Security Audit de ECC
- **Tipo:** CONFIRMACIÓN-ESPERADA · **Estado:** ABIERTO · **Abierto:** 23 nov 2026
  (revisión del sistema)
- **Dueño:** Dirsi
- **Disparo de cierre:** en la próxima ejecución programada del workflow de
  mantenimiento del fork ECC (~6 dic 2026), el paso Security Audit pasa en
  el primer intento, sin re-ejecutar.
- **Evidencia:** revisión ECC 22 nov 2026: el upstream corrigió ese paso
  (npm 11.21.2 fijado, f17308d5). El fallo fue recurrente (9 y 16 nov,
  mismo job, mismo paso); un re-ejecutar en verde prueba el día, no el
  patrón. Ver también C-011 en CALIBRACION.md.

### H-007 — Re-extensión de la demo de Block Ethos antes del 23 dic 2026
- **Tipo:** PROMESA · **Estado:** ABIERTO · **Abierto:** 23 nov 2026
  (revisión del sistema)
- **Dueño:** Dirsi
- **Disparo de cierre:** antes del 23 dic 2026, extender de nuevo la demo
  en PythonAnywhere (pestaña Web de BC123, «Run until 1 month from today»)
  y registrar la nueva fecha de caducidad en MEMORY.md.
- **Evidencia:** la demo caduca mensualmente si no se extiende; Dirsi la
  extendió el 23 nov 2026 hasta el 23 dic 2026 con el login guardado en
  la bóveda. (La extensión anterior —aviso 19 nov, resuelta 23 nov—
  vivió y murió sin hilo: es la clase que M3 existe para cazar.)

### H-008 — Relectura de los CONNECTOR.md de github e instagram
- **Tipo:** CORRECCIÓN · **Estado:** ABIERTO · **Abierto:** 23 nov 2026
  (revisión del sistema)
- **Dueño:** Dirsi
- **Disparo de cierre:** los CONNECTOR.md de github e instagram releídos,
  con la fecha de relectura anotada en este hilo (o cierre con evidencia
  si la relectura ya ocurrió).
- **Evidencia:** los avisos de relectura no existen en ningún archivo
  durable (0 menciones en notas, hilos, registro, consejo y bandeja):
  imposible verificar si se releyeron. GitHub se operó 3 veces en la
  semana 0; instagram no se usó en absoluto en ese periodo.

### H-009 — Corrida ciega R-01–R-06 de la Fase 0
- **Tipo:** PROMESA · **Estado:** ABIERTO · **Abierto:** 23 nov 2026
  (sesión de mejora «modo quemar tokens Full»)
- **Dueño:** Dirsi (coordinación paralela de la sesión)
- **Disparo de cierre:** la corrida ciega R-01–R-06 está ejecutada y
  su resultado registrado en `REGISTRO-INTEGRACION.md`, con el
  veredicto sobre la Fase 0 (sobrevive / se prorroga / se corrige).
- **Evidencia:** la corrida se ejecutó y puntuó el 23 nov 2026
  (X 8,5/9, Y 8,33/9; acuerdo entre puntuadores 17/18; baremo 6/6 no
  evaluable por el bloqueo del clon en R-06); su resultado quedó
  registrado en `BANCO-DE-PRUEBAS.md` (sección R), en
  `CALIBRACION.md` (C-008, confirmada) y en
  `REGISTRO-INTEGRACION.md` («Estado al 23 nov 2026»). Este hilo no
  se cierra con la corrida lanzada, sino con el veredicto sobre la
  Fase 0, que decide la medición de 3 semanas en operación real.

### H-010 — Corrección del error 401 de Zen sin verificar
- **Tipo:** CONFIRMACIÓN · **Estado:** ABIERTO · **Abierto:** 23 nov 2026
  (registrado en esta sesión; el hecho es del 6 nov 2026)
- **Dueño:** Antonio (prueba en el portátil) / Dirsi (sesión de laptop)
- **Disparo de cierre:** una prueba en el portátil confirma que Zen
  conecta sin error 401 tras volver a ejecutar `/connect` con la
  clave Zen, o una sesión de laptop lo verifica de primera mano.
- **Evidencia:** la configuración de OpenCode del portátil mezcló la
  credencial de Zen con la clave unificada del router FreeLLMAPI
  (error 401); Antonio volvió a ejecutar `/connect` con la clave
  Zen, pero la corrección quedó sin verificar (prueba TUI
  pendiente). Fuente: `aprendido/agentes-e-ia.md` («FreeLLMAPI: el
  router local») y la memoria del sistema.
