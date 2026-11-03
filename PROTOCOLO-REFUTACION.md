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

No se dispara en conversación casual, en datos ya demostrados de primera
mano en el mismo acto (nivel A) ni en trabajo creativo. Refutarlo todo
convertiría el protocolo en ruido y dejaría de significar algo.

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
