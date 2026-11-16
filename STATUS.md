# Estado del sistema — tablero

Una página, de un vistazo: cómo va el sistema hoy. Cada cifra viene
de su documento fuente, citado en cada sección; este tablero resume,
no sustituye a ninguno. Regla de mantenimiento: se actualiza cuando
algo cambia de estado (una corrida del banco, una resolución del
registro, un refresco del censo, un vencimiento que pasa).

**Tablero al 16 de noviembre de 2026.**

## Calibración — `CALIBRACION.md`, § Marcador

| Resueltas | Confirmadas | Parciales | Refutadas | Acierto | Pendientes |
|---|---|---|---|---|---|
| 6 | 3 | 3 | 0 | 75 % | 1 |

- El acierto se calcula solo sobre entradas resueltas
  (confirmada = 1, parcial = 0,5, refutada = 0).
- La única pendiente es **C-004**: la papelera de Gmail se vaciará
  sola a los ~30 días (≈1 dic 2026) y liberará los ~227 MB de los
  14 correos pesados que Antonio autorizó mover.

## Banco de pruebas — `BANCO-DE-PRUEBAS.md`, § Registro de corridas

- **Línea base v1 (3 nov 2026, Muse Spark 1.3): 6/6** en el
  subconjunto ejecutable (P-01, P-02, P-05, P-06, P-09, P-10).
- **Qué falta para 10/10:** la primera corrida de P-03 y P-04
  (material v1 preparado el 5 nov 2026, aún sin publicar en este
  repo) y de P-07 y P-08 (definidas, sin correr).
- 6/6 es el punto de partida, no una certificación: el valor del
  banco aparece al repetir la corrida y comparar. Próxima corrida
  mensual: ~3 dic 2026 (cadencia mensual desde la línea base).

## Censo — `INVENTARIO-CAPACIDADES.md`

- **Último refresco: 16 nov 2026** (§1 y §2 reverificados sin
  cambios; §3 actualizado). Censo v1 del 4 nov 2026.
- **90 conectores** con su `CONNECTOR.md` (79 el 9 nov; 74 el
  4 nov), **129 CLIs** en `/opt/hatch/bin`, **57 + 9 skills**
  (sistema + propias), **4 vCPU**, **7,7 GB de RAM**,
  Playwright 681 MB, HuggingFace 458 MB.
- Las cifras del refresco del 16 nov se reprodujeron por conteo
  directo en la máquina el mismo día (90, 129, 57, 9, 4 vCPU,
  681 MB, 458 MB): el entorno cambió entre despliegues, como la
  regla de refresco prevé; no es un error de conteo anterior.

## Próximos vencimientos (hora de Caracas)

| Fecha | Qué |
|---|---|
| jue 19 nov 2026, ~20:20 | Primera revisión quincenal de los forks REA + Craft Anything (cron `rea-craft-biweekly-review`; aún sin correr) |
| dom 22 nov 2026, ~16:03 | Revisión quincenal del fork ECC (cron `ecc-fork-biweekly-review`; última corrida: 8 nov, en verde) |
| mar 24 nov 2026, 13:00 | Taller Agentic Engineer 2027 en directo, sin grabación (registro confirmado; solo queda asistir) |
| ~mar 1 dic 2026 | C-004 se resuelve: la papelera de Gmail libera los ~227 MB |
| ~jue 3 dic 2026 | Próxima corrida mensual del banco de pruebas |
| dom 20 dic 2026 | Plazo de GitHub para activar 2FA (paso manual de Antonio; sin 2FA, las acciones en la cuenta quedarán restringidas) |

Fuentes de los vencimientos: las dos revisiones, el programador de
tareas (próximas corridas verificadas el 16 nov 2026) y
`RECOPILACION-MATERIALES.md` (addendum del 16 nov: taller y 2FA;
addendum del 5 nov: primera corrida REA/Craft el 19 nov);
C-004, `CALIBRACION.md`; la corrida mensual, la cadencia de
`BANCO-DE-PRUEBAS.md`.
