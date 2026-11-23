# Estado del sistema — tablero

Una página, de un vistazo: cómo va el sistema hoy. Cada cifra viene
de su documento fuente, citado en cada sección; este tablero resume,
no sustituye a ninguno. Regla de mantenimiento: se actualiza cuando
algo cambia de estado (una corrida del banco, una resolución del
registro, un refresco del censo, un vencimiento que pasa).

**Tablero al 23 de noviembre de 2026.** (Anterior: 16 nov 2026. Cambios desde entonces: revisiones REA/Craft del 19 nov y ECC del 22 nov, ambas completadas; refresco del censo del 23 nov; corrida ciega R-01–R-06 ejecutada y puntuada hoy.)

## Calibración — `CALIBRACION.md`, § Marcador

| Resueltas | Confirmadas | Parciales | Refutadas | Acierto | Pendientes |
|---|---|---|---|---|---|
| 9 | 5 | 4 | 0 | 77,8 % | 2 |

- El acierto se calcula solo sobre entradas resueltas
  (confirmada = 1, parcial = 0,5, refutada = 0).
- Marcador reverificado el 23 nov 2026 contra `CALIBRACION.md`:
  9 resueltas (C-001, C-002, C-003, C-005, C-006, C-007, C-008,
  C-009, C-010), 5 confirmadas, 4 parciales, 0 refutadas;
  (5 + 2) / 9 = 77,8 %.
- Las pendientes son **C-004**: la papelera de Gmail se vaciará
  sola a los ~30 días (≈1 dic 2026) y liberará los ~227 MB de los
  14 correos pesados que Antonio autorizó mover; y **C-011**: el
  fallo recurrente del Security Audit del fork ECC quedó resuelto
  por la corrección upstream (se verifica con la próxima ejecución
  del workflow de mantenimiento, ~6 dic 2026).

## Banco de pruebas — `BANCO-DE-PRUEBAS.md`, § Registro de corridas

- **Línea base v1 (3 nov 2026, Muse Spark 1.3): 6/6** en el
  subconjunto ejecutable (P-01, P-02, P-05, P-06, P-09, P-10).
- **Calibración de la escala (18 nov 2026, Muse Spark 1.3):
  12/12** — P-02, P-03 y P-05 en 4 niveles (Bajo, Medio 2, Alto 6,
  Extra 12), puntuación ciega doble con acuerdo 12/12. Primera
  corrida de P-03 (4/4 niveles: NO PUBLICAR, 5/6, falta
  `/certificados`). Los criterios binarios no discriminan entre
  niveles; la profundidad sí crece (P-02: 6→9→11→12
  verificaciones). Detalle en `CALIBRACION-ESCALA-2026-11-18.md`.
- **Corrida ciega R-01–R-06 + S-01–S-03 (23 nov 2026, Muse Spark
  1.3): X 8,5/9 · Y 8,33/9** — 2 brazos (con mecanismos Fase 0 /
  control), puntuación ciega doble con acuerdo 17/18. Baremo 6/6
  no evaluable: R-06 quedó «no administrable» (el sistema bloqueó
  el `git clone` en ambos brazos). La supervivencia de Fase 0 la
  decide la medición de 3 semanas en operación real, no esta
  corrida. Detalle en `BANCO-DE-PRUEBAS.md` (sección R).
- **Qué falta para 10/10:** la primera corrida de P-04 (material
  v1 publicado en este repo, `banco-de-pruebas/p-04/`, con la
  semilla congelada), P-07 y P-08 (definidas, sin correr).
- 6/6 es el punto de partida, no una certificación: el valor del
  banco aparece al repetir la corrida y comparar. Próxima corrida
  mensual: ~3 dic 2026 (cadencia mensual desde la línea base).

## Integración (Fase 0) — `REGISTRO-INTEGRACION.md`

- **Línea base (semana 9–16 nov 2026): 7 FI (2 graves)**,
  ≈6,1 FI/semana. La corroboración de la línea base por el consejo
  asesor sigue pendiente (la sesión 2 del consejo, 23 nov 2026, la
  dejó para la primera adjudicación del dom 29 nov 2026).
- **Semana 0 de rodaje (17–22 nov): terminada, sin puntuar.**
  Primera semana puntuable en curso desde el lun 23 nov 2026.
  Veredicto de la sesión 2 del consejo: la semana 0 no fue rodaje,
  fue silencio con archivos publicados (0 huellas M1r, 0
  FI-candidatos, 0 pasadas de refutación en 20 días); 4
  FI-candidatos propuestos (FI-C1–C4), pendientes de adjudicación.
- **Corrida ciega R-01–R-06: ejecutada y puntuada el 23 nov 2026**
  (X 8,5/9, Y 8,33/9; acuerdo entre puntuadores 17/18; baremo 6/6
  no evaluable por el bloqueo del clon en R-06). Su resultado
  quedó registrado en `BANCO-DE-PRUEBAS.md` (sección R) y en
  `CALIBRACION.md` (C-008, confirmada). La supervivencia de Fase 0
  la decide la medición de 3 semanas en operación real, no esta
  corrida (hilo H-009).
- Criterio de éxito: ≤1 FI/semana durante 3 semanas con cero
  FI-2, TCE ≥2/3 con cobertura ≥80 %, regresión R-01–R-06 6/6 y
  piso de ≥5 entregas decisivas/semana.

## Escala de razonamiento — `ESCALA-RAZONAMIENTO-AGENTES.md`

- Niveles: Bajo (Dirsi sola), Medio (+2), Alto (+6), Extra (+12),
  Max (+12, uso único con presupuesto). Dirsi al centro en todos;
  revisión cruzada obligatoria desde Medio.
- **Calibración 18 nov 2026: los números 2/6/12 NO quedan
  calibrados** — en los criterios binarios del banco los 4 niveles
  empatan a 3/3. Lo que crece con los agentes es la profundidad y
  la caza de errores en revisión. Calibrar de verdad exige
  criterios con gradación o tareas más duras donde Bajo falle.

## Censo — `INVENTARIO-CAPACIDADES.md`

- **Último refresco: 23 nov 2026** (§1 y §2 reverificados sin
  cambios, salvo 911 binarios en `/usr/bin`; §3 actualizado).
  Censo v1 del 4 nov 2026; refresco anterior, 16 nov 2026.
- **144 conectores** con su `CONNECTOR.md` (90 el 16 nov; 79 el
  9 nov; 74 el 4 nov), **186 CLIs** en `/opt/hatch/bin` (129 el
  16 nov), **58 + 8 skills vivas** (sistema + propias; 57 + 9 el
  16 nov — la novena propia, `recovered-skill-notes`, se retiró el
  23 nov por ser un stub sin método), **4 vCPU**, **7,7 GB de RAM**,
  Playwright 681 MB, HuggingFace 458 MB, Chromium build 1248.
- Las cifras del refresco del 23 nov se reprodujeron por conteo
  directo en la máquina el mismo día (144, 186, 58, 9 archivos con
  8 skills propias vivas tras retirar el stub, 4 vCPU,
  7.934 MB, 681 MB, 458 MB, 911 binarios): el entorno cambió
  entre despliegues, como la regla de refresco prevé; no es un
  error de conteo anterior. La lista de familias de CLIs (§3 del
  inventario) no se re-auditó en este refresco.

## Próximos vencimientos (hora de Caracas)

| Fecha | Qué |
|---|---|
| mar 24 nov 2026, 13:00–14:30 | Taller Agentic Engineer 2027 en directo, sin grabación (registro confirmado; solo queda asistir) |
| mié 25 nov 2026 | Test final del curso preparatorio Agentic Engineer Starter (30 min; diploma de participación al aprobar) |
| ~mar 1 dic 2026 | C-004 se resuelve: la papelera de Gmail libera los ~227 MB |
| ~jue 3 dic 2026 | Próxima corrida mensual del banco de pruebas + revisión quincenal de los forks REA + Craft Anything |
| ~dom 6 dic 2026 | Revisión quincenal del fork ECC |
| dom 20 dic 2026, 20:00 | Plazo de GitHub para activar 2FA (paso manual de Antonio; sin 2FA, las acciones en la cuenta quedarán restringidas) |
| mié 23 dic 2026 | La demo de Block Ethos en PythonAnywhere deja de servirse si no se vuelve a extender (gratis, pestaña Web de la cuenta BC123; si caduca se reactiva con el mismo enlace). Extendida el 23 nov 2026 (antes vencía el jue 26 nov) |

**Cumplidos desde el último tablero (16 nov):** primera revisión
quincenal de los forks REA + Craft Anything (19 nov, ~20:19–20:33:
REA 2.229 commits por detrás, sincronizado en dos pasadas, merges
c367842 y ae6f927, por un commit que llegó un minuto después del
primer merge; Craft Anything 1.244 commits, merge ae97f7f; ambos
0 por detrás al final, `MANTENIMIENTO.md` intacto) y revisión
quincenal del fork ECC (22 nov, ~16:03–17:15: 847 commits
sincronizados, PR #2, merge `fe70023`, fork 0 atrás / 3 adelante
(la revisión contó 2; la corrida ciega del 23 nov corrigió: 3 —
el merge de la PR #1, 9f78dc5),
`SKILL.md` intacto; el upstream corrigió el paso Security Audit que
falló el 9 y el 16 nov — la próxima ejecución dirá si el fallo
recurrente quedó resuelto).

Fuentes de los vencimientos: las revisiones quincenales (informes
locales `~/workspace/goals/respaldo-de-rea-y-craft-anything-en-github/hidden_files/2026-11-19-review.md`
y `~/workspace/goals/ecc-fork-biweekly-review/hidden_files/2026-11-22-review.md`);
el taller y el test, `RECOPILACION-MATERIALES.md` (addendum del
16 nov) y el calendario del curso verificado el 19 nov; la
caducidad de PythonAnywhere, el correo de PythonAnywhere Support
del 19 nov (leído de primera mano por Gmail) y la extensión del
23 nov 2026 (nueva fecha de caducidad: 23 dic 2026); C-004,
`CALIBRACION.md`; la corrida mensual, la cadencia de
`BANCO-DE-PRUEBAS.md`; el plazo 2FA, el recordatorio de GitHub del
19 nov (hora exacta: 20 dic 2026, 20:00 Caracas).
