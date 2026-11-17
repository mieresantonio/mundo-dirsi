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
- **Disparo de cierre:** el README de rag-demo documenta las preguntas de
  ejemplo clicables y el historial, verificado por relectura del README.
- **Evidencia:** verificado 17 nov 2026: `~/workspace/rag-demo/README.md`
  (225 líneas) no menciona preguntas de ejemplo ni historial
  (`grep -i ejemplo|historial` sin resultados en ese sentido).

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
- **Disparo de cierre:** el archivo tiene modo +x en el repo publicado,
  verificado desde GitHub (no basta el `chmod` local: la subida por snapshot
  no conserva modos).
- **Evidencia:** verificado 17 nov 2026: `~/workspace/block-ethos/render_build.sh`
  sigue en 644 (`-rw-rw----`). La demo viva en PythonAnywhere no se ve
  afectada; solo fallaría un despliegue en Render desde el repo.
