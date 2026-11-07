# Registro de calibración de Dirsi

Aquí quedan anotadas las afirmaciones decisivas y comprobables que Dirsi
le entrega a Antonio, junto a su nivel de evidencia, y aquí mismo se marca
lo que la realidad terminó diciendo: confirmada, parcial o refutada.

Para qué sirve: convertir la confianza en una cifra. Hoy la mejora de Dirsi
se cuenta con anécdotas; con este registro se cuenta con aciertos y fallos
verificados. Una afirmación refutada nunca se borra ni se reescribe: se
marca, se anota qué falló y queda como lección permanente.

Creado el 3 de noviembre de 2026, por elección expresa de Antonio, como
primera pieza del sistema de mejora de Dirsi a nivel de sistema (sin tocar
el motor).

## Cómo funciona

Se registra una afirmación cuando cumple las tres condiciones:

1. Es decisiva: Antonio puede actuar o decidir apoyándose en ella.
2. Es comprobable: existe una fuente o un evento futuro que la resuelve.
3. Aún no está resuelta en el acto: lo ya verificado de primera mano al
   entregarla es nivel A demostrado y no necesita registro.

Cada entrada lleva: fecha de la afirmación, la afirmación en una línea y
en forma falsable, el nivel de evidencia al entregarla, con qué se
verifica y su estado. Cuando la realidad responde, se rellena la fecha de
resolución y el resultado, y se actualiza el marcador.

El porcentaje de acierto se calcula solo sobre entradas resueltas
(confirmada = 1, parcial = 0,5, refutada = 0). Las categorías por tema se
añadirán cuando haya al menos 10 resueltas.

## Marcador

| Resueltas | Confirmadas | Parciales | Refutadas | Acierto | Pendientes |
|---|---|---|---|---|---|
| 2 | 1 | 1 | 0 | 75 % | 4 |

## Pendientes

### C-003 · 2026-11-03 · Precios
- **Afirmación:** La cotización regional escrita de 4Geeks para
  Venezuela/LatAm, cuando llegue, será inferior a los precios globales
  publicados (AI Fluency $900 total; AI Engineering $15,999 en el enlace
  de referido de Antonio).
- **Nivel al entregarla:** inferencia B (patrón regional demostrado en el
  caso de Antonio: su Full Stack costó $2,198 frente a precios de EE. UU.
  varias veces mayores; no es un precio confirmado).
- **Se verifica con:** la respuesta del contacto que Antonio ya consultó
  o la cotización escrita de Admisiones.
- **Nota de refutación (3 nov 2026, primera pasada del protocolo):**
  afirmación DEBILITADA, sin tocar el texto original. Para AI Engineering
  la contratación por país es real (TyC §5.3; campus de Caracas), así que
  un precio menor sigue siendo plausible; para AI Fluency no hay
  mecanismo regional documentado — precio único €900/$900 y variación por
  elegibilidad de beca según el FAQ oficial —, así que su rebaja, si la
  hay, sería por beca y de monto desconocido. La afirmación queda como
  probabilidad, no como certeza futura. Detalle en PROTOCOLO-REFUTACION.md.

### C-004 · 2026-11-01 · Estados técnicos
- **Afirmación:** La papelera de Gmail se vaciará sola a los ~30 días
  (≈1 dic 2026) y liberará los ~227 MB de los 14 correos pesados que
  Antonio autorizó mover (14/14 verificados en papelera, y solo esos 14).
- **Nivel al entregarla:** A (comportamiento documentado de Gmail y
  conteo verificado en la cuenta).
- **Se verifica con:** el espacio libre de la cuenta después del 1 dic 2026.

### C-005 · 2026-10-25 · Estados técnicos
- **Afirmación:** La primera revisión quincenal del fork ECC correrá el
  domingo 8 nov 2026 (~16:03 Caracas) y entregará informe aunque no haya
  cambios en el upstream.
- **Nivel al entregarla:** A (trabajo programado creado y verificado:
  ecc-fork-biweekly-review, cada 336 h).
- **Se verifica con:** el informe de la revisión del 8 nov 2026.

### C-006 · 2026-11-07 · Diseño
- **Afirmación:** La primera aplicación del sistema `diseno_vitrina`
  (destilado de Grok Build el mismo día) — el rediseño completo del
  portafolio de Antonio — produce un acabado visiblemente superior al
  borrador anterior ya en la primera pasada, sin correcciones de
  composición ni de jerarquía durante la verificación visual.
- **Nivel al entregarla:** juicio propio verificado con el ojo visual
  (capturas de escritorio y móvil leídas de primera mano, comparadas
  contra las del borrador del 21 oct 2026). Las dos correcciones
  aplicadas fueron técnicas, no de diseño: el revelado por scroll pasó a
  mejora progresiva (sin JS el contenido se ve siempre) y un enlace dejó
  de partirse en móvil.
- **Se verifica con:** el juicio de Antonio sobre el resultado entregado
  el 7 nov 2026. Si lo juzga al nivel del borrador o peor, la afirmación
  queda refutada; si lo juzga mejor pero no «de vitrina», parcial.

## Resueltas

La primera resolución fue C-002, el 4 nov 2026 (parcial); la segunda,
C-001, el mismo día (confirmada).

| Nº | Afirmación (resumen) | Resultado | Fecha de resolución | Qué se aprendió |
|---|---|---|---|---|
| C-001 | Moonshot publicará los pesos abiertos de Kimi K3.1 Pro el 4 nov 2026 | Confirmada | 2026-11-04 | El chequeo de las ~10:15 dio negativo de primera mano (404; 19 modelos, ningún K3.1) y el repo se hizo público la tarde del mismo día: Antonio lo detectó ~14:29 y Dirsi lo verificó por la API de HF minutos después (público, sin gating, 112 archivos, 96 shards, 1.561.355.969.963 bytes; licencia K3.1-Pro leída de primera mano: mismo esquema que la de K3, sin restricción a afinar ni a crear derivados; puerta MaaS >US$20M/año). Lecciones: un chequeo negativo vale para su hora, no para todo el día prometido; y el `createdAt` de HF (2 nov) refleja la creación/carga del repo, no su visibilidad pública. |
| C-002 | La grabación de la sesión de Commit Academy del 3 nov llegaría por correo | Parcial | 2026-11-04 | El correo de seguimiento llegó (4 nov, 04:30 Caracas, de Marti de Commit Academy, leído de primera mano) pero trae los apuntes del taller y la venta de su curso pago: ningún enlace a la grabación en el cuerpo, y el «examen» del asunto tampoco aparece en el cuerpo. Puede que la grabación esté dentro de los apuntes enlazados (no abiertos) o que no llegue. Lección: «la página de registro incluye X» no equivale a «el correo traerá X». |

## Antecedentes (no puntuados)

Este registro nace de errores reales y documentados, anteriores a su
creación:

- 23 oct 2026: dos resúmenes de segunda mano fabricaron contenido con gran
  verosimilitud (videos e Instagram). De ahí salió la regla de contrastar
  siempre contra la fuente primaria.
- 1 nov 2026: Dirsi afirmó que no podía ver el medidor de uso sin haber
  ejecutado la comprobación; Antonio lo cuestionó, la comprobación se hizo
  y la lectura existía. De ahí: comprobar la herramienta antes de declarar
  un límite.
- 2 nov 2026: dos despliegues de Blockali fallaron por empaquetar sin
  verificar el contenido del paquete; la tercera versión se verificó
  cadena por cadena antes de subirla y funcionó.

No puntúan porque son anteriores al registro, pero son su motivo.
