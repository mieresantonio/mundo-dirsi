# Protocolo de refutación de Dirsi

Antes de que algo decisivo llegue a Antonio, una pasada adversarial
intenta refutarlo. No pulirlo: refutarlo. Si una afirmación sobrevive al
ataque, su confianza sube con motivo; si no sobrevive, Antonio se entera
antes de actuar, no después.

Nació de errores reales: el 23 oct 2026, dos resúmenes de segunda mano
fabricaron contenido con gran verosimilitud y casi pasan por hechos; el
1 nov se declaró un límite sin haber ejecutado la comprobación; el 2 nov
se empaquetó dos veces sin verificar el contenido. En los tres casos, una
pasada cuyo único trabajo fuera atacar el resultado los habría cazado.

Creado el 3 de noviembre de 2026, por elección expresa de Antonio, como
tercera pieza del sistema de mejora de Dirsi a nivel de sistema. Cierra el
bucle con las otras dos: el registro de calibración mide lo que Dirsi
afirma, el banco de pruebas mide lo que Dirsi hace, y este protocolo
intercepta lo que Dirsi está a punto de entregar.

## Cuándo se dispara

La pasada es obligatoria cuando el entregable es decisivo en alguno de
estos sentidos:

- **Investigación con consecuencias:** conclusiones sobre las que Antonio
  (o alguien por su recomendación) puede actuar — precios, elegibilidad,
  si algo es real, está cerrado o es humo.
- **Dinero:** cotizaciones, ofertas, pagos, promesas comerciales.
- **Publicación o despliegue:** lo que va a salir a un repo público, a
  producción o a otra persona en nombre de Antonio.
- **Afirmaciones que entran al registro de calibración:** reciben la
  pasada *antes* de entrar, para que el registro mida afirmaciones ya
  examinadas.

No se dispara en conversación casual, en datos ya demostrados de primera mano en el mismo acto (nivel A), en trabajo creativo ni en entregas bajo cuenta atrás de menos de 5 minutos con acción reversible (regla de emergencia, AGENTS.md: la acción precede a la pasada; la línea auditable dice `refutación: diferida por emergencia`). Refutarlo todo
convertiría el protocolo en ruido y dejaría de significar algo.

## Disparador auditable (23 nov 2026)

Ninguna subida por snapshot a un repo público se ejecuta sin una línea en
el LOG de la tarea que diga `refutación: [fecha] [agente]
[refutadas/debilitadas/resisten]` o `refutación: no dispara porque
[motivo de la lista de exclusiones]`. La línea es comprobable por el
consejo desde el registro; una pregunta («¿refuté?») no lo es.

Límite honesto: la línea es un checkbox auditable, no una función
forzadora — la escribe el mismo agente que podría olvidar la pasada, y
«refutación: no dispara porque…» puede inventarse con la misma facilidad
con la que hoy se omite. No se vende como garantía de que la pasada
ocurra. La función forzadora real sería una verificación por un segundo
agente antes del snapshot-push; mientras no exista, el consejo audita la
línea en su muestreo semanal.

## La pasada, paso a paso

1. **Congelar las afirmaciones decisivas.** Se extrae la lista corta de
   afirmaciones de las que depende la conclusión, cada una con el apoyo
   que se le atribuye (fuente, cálculo, lectura).
2. **Ataque independiente.** Un agente que **no** produjo el trabajo
   recibe solo las afirmaciones y sus apoyos, con una única orden:
   refutar. Para cada afirmación intenta:
   - ¿La fuente dice realmente esto, o dice menos / otra cosa?
   - ¿Existe una fuente más fuerte que la contradiga?
   - ¿La aritmética, las fechas, las unidades y la moneda están bien?
   - ¿El dato sigue vigente hoy, o era verdad en otra fecha?
   - ¿Qué tendría que ser verdad para que esta afirmación sea falsa?
   Cuando el trabajo lo produjo la propia Dirsi sin delegar, la pasada la
   corre igualmente un agente separado; la autocrítica en el mismo acto es
   la forma débil del protocolo y se declara como tal.
3. **Clasificación de cada afirmación atacada:**
   - **Refutada:** el ataque la mata. Se corrige o se retira antes de
     entregar; nunca se entrega como estaba.
   - **Debilitada:** sobrevive, pero con una salvedad real. La salvedad
     entra *dentro* de la entrega, visible, no en letra pequeña.
   - **Resiste:** el ataque no la mueve. Su nivel de confianza sube con
     motivo registrado.
4. **Entrega con el resultado visible.** Antonio ve qué se atacó y qué
   cambió. En lo decisivo no hay correcciones silenciosas: si la
   refutación cambió una conclusión, él lo sabe.
5. **Retroalimentación.** Toda refutada o debilitada deja huella: la
   lección va a las reglas de operación y, si la afirmación ya estaba en
   el registro de calibración, se anota allí sin reescribir la afirmación
   original.

## Límites declarados

- La pasada reduce errores; no los elimina. Un refutador también puede
  equivocarse, por eso sus ataques se juzgan contra la evidencia, no se
  aceptan por autoridad.
- Refutar no es dudar de todo: una afirmación con fuente primaria leída de
  primera mano resiste rápido, y eso también es un resultado útil.
- El protocolo no autoriza nada por sí mismo: ni envíos, ni pagos, ni
  publicaciones — esas decisiones siguen siendo de Antonio.

## Registro de pasadas

| Fecha | Entregable atacado | Afirmaciones | Refutadas | Debilitadas | Resisten |
|---|---|---|---|---|---|
| 2026-11-03 | Investigación 4Geeks: referido y precios para la conocida de Antonio | 3 | 0 | 3 | 0 |
| 2026-11-03 | Autoevaluación con/sin sistema (índice propio 0–100) | 10 dimensiones | compuesto (+26) refutado como medición | 8 notas rebajadas | 1 (percepción visual: ganancia cero) |
| 2026-11-23 | Revisión del sistema: informes de los 5 asesores (A–E) | ~70 | 3 | ~15 | ~45 |

**Brecha 4–23 nov 2026: sin pasadas.** Entregas decisivas sin pasada en
ese periodo: publicación de Block Ethos standalone (16 nov), 2ª tanda
(16 nov), destilado del Playbook (16 nov), evaluación de los 7 enlaces
(16 nov), investigación Muse/Meta AI (17 nov), veredictos del Ejercicio 3
(17–18 nov), 1ª revisión REA/Craft (19 nov), revisión ECC + PR #2
(22 nov). Causa: el disparador dependía de que Dirsi recordara correr la
pasada; ningún paso mecánico la exigía. No se rellenan pasadas
retroactivas: las entregas ya hechas y verificadas no ganan nada con un
teatro de refutación posterior. La próxima entrega decisiva estrena el
disparador auditable de arriba.

### Detalle por pasada

#### 2026-11-03 · Investigación 4Geeks (referido y precios) · 0 refutadas, 3 debilitadas, 0 resisten

Primera pasada del protocolo, corrida por un agente que no produjo la
investigación, contra su informe y fuentes primarias de 4Geeks.

- **Afirmación 1 — «el referido es neutro y la página de partners paga
  15 % a quien refiere»: DEBILITADA.** El núcleo resiste (ningún mecanismo
  de recargo: ella no paga más; tampoco hay descuento documentado), pero
  el 15 % estaba mal atribuido: los términos oficiales de partners son un
  contrato B2B de otra entidad (4Geeks Global LTD) para servicios
  (AI Studio, Perks, Talent…), y la matrícula de la Academy no aparece en
  su tabla de comisiones; qué gana Antonio por su cupón concreto consta
  en términos no públicos de la Academy. Además, el descuento debe
  figurar como «no verificado» — que es lo que el propio informe decía —
  y no como «inexistente», que fue como se resumió al entregarlo.
- **Afirmación 2 — «la cotización regional será inferior a los precios
  globales» (= C-003 del registro): DEBILITADA.** Para AI Engineering la
  contratación por país es real (TyC §5.3: el contrato «refleja las
  condiciones específicas aplicables al país, estado o región»; existe
  campus de Caracas), así que un precio venezolano menor es plausible.
  Para AI Fluency no hay mecanismo regional documentado: precio único
  nominal €900/$900 a ambos lados del Atlántico y, según el FAQ oficial,
  la variación depende de la elegibilidad de beca de cada candidato —
  cualquier rebaja sería por beca, de monto desconocido, sin base para
  esperar los ~$200 estimados. Y la afirmación está formulada con certeza
  futura («será») sobre un documento que aún no existe: es probabilidad,
  no hecho pendiente de trámite. Anotada en CALIBRACION.md sin tocar la
  afirmación original.
- **Afirmación 3 — «la garantía Job or Refund es solo EE. UU. y
  Canadá»: DEBILITADA.** Es uniforme en el marketing actual de AI
  Engineering (todas las páginas del programa, incluida Caracas, dicen
  «solo EE. UU. y Canadá»), pero como enunciado absoluto es falso: el
  propio «Acuerdo de Trabajo Garantizado» oficial en español la define
  como específica por campus y territorio, con variantes internacionales
  documentadas. La respuesta vinculante es la de Admisiones para su
  cohorte — que ya era la pregunta 7 del informe y ya va en el mensaje
  borrador preparado para la conocida.

**Efecto práctico:** las recomendaciones entregadas no cambian (cotización
escrita antes de pagar; preguntar por la garantía de su cohorte; el
referido no le cuesta más). Lo que cambia es la precisión: el 15 % deja de
atribuirse al cupón de Antonio, el descuento pasa a «no verificado» y la
confianza de C-003 baja a probabilidad con la salvedad de AI Fluency
visible.

#### 2026-11-03 · Autoevaluación con/sin sistema · compuesto refutado como medición

Dirsi se puntuó con un índice propio (borrador: 44 → 70, +26) y la tabla
pasó por este protocolo antes de publicarse. El refutador la desarmó: la
era «sin sistema» ya tenía parte de la disciplina (el trabajo fuerte de
verificación es del 2 nov, anterior a las tres piezas); la base se
reconstruyó con incidentes sin denominador; la columna «con sistema»
tiene un día y una corrida parcial del banco; la calibración no tiene
desempeño que puntuar (0 resueltas); backend, diseño y automatización no
muestran ganancia atribuible todavía (P-04 sin correr; ningún cron nuevo
ha disparado). Compuesto corregido: ≈ +5,5 como techo ilustrativo, no
como estimación. Lo que sí quedó demostrado: ganancia de gobernanza y
auditabilidad, no de capacidad. La evaluación completa, con el borrador y
la corrección lado a lado, vive en BANCO-DE-PRUEBAS.md. Corrección de
términos (la señaló Antonio el mismo día): la comparación era «el sistema
sin capa de medición» contra «el sistema con capa de medición» — el
sistema entero (memoria, procedimientos, repos) existe desde oct 2026 —,
no una Dirsi con sistema contra otra sin sistema.

#### 2026-11-23 · Revisión del sistema: informes de los 5 asesores · 3 refutadas, ~15 debilitadas, ~45 resisten

Pasada adversarial sobre los 5 informes de asesores de la revisión del
sistema (sesión 2 del consejo), corrida por un agente que no produjo
ninguno de ellos, verificando de primera mano contra archivos primarios,
re-ejecutando comandos literales, diffs contra clones frescos de GitHub
y consultas propias a la transcripción completa (33 mensajes de Antonio,
59 de Dirsi, 17–23 nov).

- **Refutada — A1, la propuesta («101 → 129 tests» en MEMORY.md).**
  129 es la fase 1 de la 2ª tanda, no el final: `LOG.md:940-941` y
  `RESUMEN:151` dicen 144 passed (101 base → 129 fase 1 → 144 fase 2).
  Además son 115 archivos en HEAD, no 104. El diagnóstico (MEMORY.md
  obsoleto) resiste; la cifra de reemplazo introduciría un error nuevo.
- **Refutada — D-C3 («el informe REA afirma que la fusión por API/MCP no
  tiene permiso de escritura»).** La frase no existe en la revisión REA
  (su :14 dice con precisión «falló con 403»); la frase parecida vive en
  la revisión ECC del 8 nov, ya calificada («para fusionar»). La adenda
  propuesta iba al archivo equivocado.
- **Refutada — A8, segunda mitad («44 de 89» muerto en bandeja:66).** La
  cita es del fork grupal, cuyas copias locales siguen diciendo 44/89;
  el asesor grepó el README del repo standalone. Añadir «(hoy 48 de 93)»
  introduciría un error.
- **Debilitadas (~15):** la mayoría ya debilitadas por los propios
  asesores (A6, B H4c, B H8, C-4/O-3, C B-5, D-R4, D-S1 como acusación,
  E 1.3, E 1.4, E 2.2 como coste); más la dirección de la resolución del
  conteo WhatsApp (A4: la hipótesis 17 nov = 4º fallo real, 19 nov = 5º,
  no se puede descartar sin el historial de notificaciones).
- **Resisten (~45):** el patrón central —la regla existe y no se aplica,
  también en la capa de medición— no se pudo refutar en ningún punto:
  los ceros son ceros en archivos, mtimes, clones frescos, crons y
  transcripción. Incluye la verificación de los comandos literales del
  censo (144/186/58/9) y de los 3 disparos de refutación del 16–22 nov.

**Efecto práctico:** la consolidación adopta los cambios de los informes
con las 3 correcciones de esta pasada y rechaza 10 propuestas (ver
CONSEJO-ASESOR.md, sesión 2). Informe completo del falsificador en
`revision-sistema-2026-11-23/trabajo/falsificador.md` (local, no
publicado).
