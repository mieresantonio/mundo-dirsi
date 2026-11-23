# Ciclo de vida de lecciones

Cómo una lección nace, se registra, se aplica, se revisa y se
retira cuando caduca. Este documento hace operativo lo que el
playbook adoptó el 12 nov 2026 (`METODO-CLAUDE-PLAYBOOK.md`
§2.3) y lo que el glosario define en «lección»: antes de este
procedimiento, el ciclo existía como idea adoptada pero ninguna
lección de `aprendido/` llevaba procedencia, confianza ni fecha
de revisión — la diferencia entre un archivo de lecciones y un
sistema de lecciones.

Por qué existe: la 1ª tanda de mejora del 23 nov 2026 encontró
una lección ya falsa en el repo (el permiso de GitHub, redactada
el 16 nov y refutada el 17) y una lección sin registrar (la
caducidad de PythonAnywhere, conocida por correo del 19 nov).
Sin ciclo de vida, las lecciones se pudren en silencio.

## Los estados

```
candidata ──► confirmada ──► regla ──► retirada
    │              │            │           ▲
    │              └─────► (contradicha / obsoleta / sin uso 90 días)
    └─────► retirada directa (si nace refutada)
```

| Estado | Qué significa | Condición de entrada |
|---|---|---|
| **Candidata** | Vista una vez; se aplica con cautela | Un fallo demostrado o una observación con evidencia (ver § Nacimiento) |
| **Confirmada** | Reproducida o útil en al menos 2 tareas, o respaldada por documentación oficial | Segunda ocurrencia con evidencia, o la fuente oficial lo respalda |
| **Regla** | Se aplica siempre; romperla exige motivo registrado | Útil en al menos 3 tareas distintas sin contraejemplos; **la promoción la aprueba un humano** (Antonio) como diff |
| **Retirada** | Ya no se aplica; queda marcada con su motivo, nunca borrada | Contradicha por evidencia nueva, obsoleta por un cambio de versión, o sin uso en 90 días |

Una lección retirada no desaparece: se marca `~~retirada: <motivo>
<fecha>~~` donde estaba, para que nadie la reaprenda como nueva.
Igual que el registro de calibración nunca reescribe una entrada
refutada, el archivo de lecciones nunca borra una retirada.

## Nacimiento: de un fallo demostrado

Una lección nace solo de un fallo demostrado o de una observación
con evidencia — nunca de una corazonada ni de «sería bueno que».
El nacimiento exige tres cosas, escritas en el momento:

1. **El fallo o la observación**, con fecha y evidencia (qué pasó,
   dónde se vio: un LOG, un mensaje de Antonio, una verificación).
2. **La procedencia**: `observado` (visto de primera mano),
   `documentado` (lo dice una fuente oficial) o `inferido`
   (deducido; las inferidas no se promueven sin verificar).
3. **La forma aplicable**: qué hacer distinto la próxima vez, en
   una frase que un agente futuro pueda ejecutar sin adivinar.

Formato de registro (una entrada por lección, en `aprendido/` o
en `AGENTS.md` según su ámbito — ver § Dónde vive cada lección):

```
- **<nombre corto>** (<fecha>, <procedencia>, <estado>)
  <qué pasó y dónde se vio>. <Qué hacer distinto.>
  Usada en: <tarea 1>, <tarea 2>. Revisión: <fecha>.
```

## Dónde vive cada lección

- **`aprendido/*.md`** — lecciones de conocimiento por tema
  (desarrollo web, agentes e IA, despliegue, blockchain, empleo,
  herramientas, ingeniería inversa). Son el archivo de lecciones.
- **`AGENTS.md`** — lecciones de operación que cambian cómo
  trabaja Dirsi cada día (convenciones, reglas duras, umbrales).
  Una lección sube a `AGENTS.md` cuando se promueve a regla de
  operación; mientras es candidata o confirmada, vive en
  `aprendido/` y se cita desde ahí.
- **Este documento** — el procedimiento mismo. No es una lección:
  es el mecanismo que las gestiona.

## Revisión: cuándo y quién

- **Al cierre de cada tarea significativa**: la huella en
  `crecimiento/log.md` anota si la tarea confirmó, contradijo o
  dejó sin usar alguna lección (una línea basta).
- **En la auditoría mensual del repo**: se revisan todas las
  lecciones con fecha de revisión vencida; las sin uso en 90 días
  se retiran (marcando, no borrando); las candidatas con 2 usos
  se confirman; las confirmadas con 3 usos sin contraejemplos se
  proponen como regla a Antonio.
- **En cada sesión de mejora de repos**: las lecciones nuevas de
  la sesión se registran con su procedencia antes de cerrar.
- **Primera revisión de caducidad**: ≈24 ene 2027 (90 días desde
  las primeras lecciones del 26 oct 2026). Hasta entonces, ninguna
  lección puede retirarse por desuso: el sistema no tiene 90 días.

Si un archivo de lecciones pasa de unas 150 líneas, consolidar:
agrupar por tema, resumir, archivar lo antiguo (regla del
playbook §2.3).

## Ejemplos trabajados (reales)

### 1. La ventana perdida → regla de emergencia (candidata → regla en un día)

- **Nacimiento (16 nov 2026, observado):** Antonio pidió un clip
  «en 3 minutos» — era el tiempo que quedaba para el reset de la
  cuota, no la duración del vídeo. La respuesta larga se comió la
  ventana y el clip salió de la semana nueva.
- **Confirmación (misma noche):** la auditoría de integración
  (17 nov) lo clasificó FI-07, grave: una aclaración larga
  también cuesta tiempo.
- **Regla (17 nov, aprobada por Antonio en la Fase 0):** con una
  cuenta atrás activa de menos de 5 minutos y una acción
  reversible disponible, la acción sale antes que la explicación.
  Vive en `AGENTS.md` («Regla de emergencia»).

### 2. El clon fresco que no lo era (candidata → regla, por falsación)

- **Nacimiento (16 nov 2026, observado):** el consejo asesor
  (sesión 1) encontró que la «simulación de clon fresco» de la
  fábrica era una copia del clon de trabajo: todos los `.sh`
  conservaban `+x`, así que la verificación confirmaba lo que ya
  se creía.
- **Regla:** la verificación se construye para falsar la
  afirmación, no para confirmarla; un clon fresco se verifica con
  un `git clone` real, o quitando `+x` a TODO. Verificada con un
  clon real y corregida. Vive en `AGENTS.md` («Lección del clon
  fresco»).

### 3. El permiso permanente de GitHub (lección retirada por refutación)

- **Nacimiento (16 nov 2026, inferido):** `aprendido/
  herramientas-y-conexiones.md` registró que con el permiso
  permanente «ya no hace falta pedir aprobación por cada cambio».
- **Refutación (17 nov, observado):** la captura de Antonio de
  las 00:31 mostró la tarjeta de aprobación de
  `CONSEJO-ASESOR.md`: las tarjetas SIGUEN apareciendo. El
  permiso cambió la DECISIÓN, no la presentación.
- **Retirada y corrección (23 nov, 1ª tanda, R3):** la afirmación
  falsa se corrigió en el repo. Lección del caso: una lección
  inferida sin verificar puede nacer falsa; por eso las inferidas
  no se promueven sin verificar, y por eso el ciclo exige
  procedencia.

### 4. «Las cifras heredadas son hipótesis» (candidata → confirmada, 3 veces en un día)

- **Nacimiento (23 nov 2026, observado):** la sesión de mejora
  encontró tres cifras heredadas falsas en un día: el MD5 del
  encargo de rag-demo era de una copia vieja (`d976b50e…` local
  vs `7423c8c3…` en HEAD); el README de mundo-vida-ia decía 128
  tests, no 114; el encargo de fabrica nombraba `prueba-humo` y
  scripts en la raíz que no existen.
- **Confirmación:** tres ocurrencias independientes en la misma
  sesión, cada una verificada de primera mano por su trabajador.
  Estado actual: **confirmada**; su promoción a regla (verificar
  nombres y cifras del encargo contra el repo antes de repartir)
  se propone a Antonio con esta entrega.

### 5. La línea de estado del proxy (candidata, 23 nov 2026)

- **Nacimiento (23 nov 2026, observado):** el triaje A midió «1
  commit» en 11 repos — falso: eran 403 por cuota agotada,
  ocultos porque el proxy de la VM antepone `HTTP/1.1 200
  Connection Established` y la comprobación leía la primera
  línea. Los conteos verdaderos (9–392) se verificaron por dos
  métodos independientes (página HTML + feed Atom).
- **Forma aplicable:** leer la ÚLTIMA línea de estado de la
  respuesta, no la primera; y para cada dato cuantitativo de una
  tabla de decisión, una segunda fuente barata.
- Estado actual: **candidata** (una sola ocurrencia; se confirma
  con la segunda).

### 6. El ojo visual (lección retirada porque cambió la premisa)

- **Nacimiento (2–3 nov 2026, inferido):** «la VM no tiene
  navegador visual» se declaró como límite sin comprobar el caché.
- **Refutación (3 nov, observado):** el Chromium headless de
  Playwright YA estaba descargado (`~/.cache/ms-playwright`); con
  `playwright-core` y `~/workspace/tools-visual/shot.mjs` Dirsi
  captura páginas locales y las ve. El límite se retiró el mismo
  día y nació su lección inversa: no afirmar un límite de
  herramienta sin revisar primero qué hay instalado (hoy, el
  censo de capacidades manda sobre cualquier nota vieja).
- Estado actual: la lección inversa es **regla** (censo de
  capacidades, desde el 4 nov 2026); el «límite» original queda
  como ejemplo de retirada por premisa falsa.

## Lo que este procedimiento NO hace (siguiente paso definido)

Etiquetar las lecciones existentes de `aprendido/` con
procedencia, confianza y fecha de revisión (idea #9 de la
1ª tanda) es una sesión dedicada, no parte de esta entrega:
requiere leer `aprendido/` entero con criterio (qué se usó, qué
no, qué contradice a qué). Cuando se haga, su checklist es:

1. Leer cada archivo de `aprendido/` y listar sus lecciones.
2. Asignar a cada una: procedencia, estado actual (por sus usos
   registrados) y fecha de revisión.
3. Marcar las contradichas para retirar y las sin uso para
   revisar a los 90 días.
4. Registrar el resultado en `crecimiento/log.md` con la fecha.
