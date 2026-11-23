# Decisiones — registro ligero

El repo registra QUÉ se aprendió; este archivo registra POR QUÉ se
decidió lo que se decidió. Cada ficha resume una decisión ya tomada
en otro lugar del repo o de la memoria, con su contexto, las
alternativas que se descartaron y la fuente exacta donde vive.

## Reglas del registro

- **Ninguna ficha sin fuente.** Cada ficha cita el archivo y la
  sección de origen, con la frase fuente entrecomillada.
- **Ninguna decisión nueva.** Este archivo no decide nada: solo
  recoge decisiones que ya existen. Si algo no está decidido en
  ninguna parte, no entra aquí.
- **Estado vigente o revisada.** Una decisión que caduca o cambia
  NO se borra: se marca `revisada`, se escribe qué evidencia la
  cambió y se enlaza la ficha que la sustituye (si la hay).
- **Una ficha, una decisión.** Si una decisión tiene dos partes
  que pueden cambiar por separado, son dos fichas.
- **Formato fijo.** Todas las fichas llevan los mismos campos y
  en el mismo orden: Decisión, Fecha, Estado, Contexto,
  Alternativas descartadas, Fuente.

## Índice

| Ficha | Decisión | Fecha | Estado |
|-------|----------|-------|--------|
| D-01 | FreeLLMAPI en el portátil, no en el teléfono | 23 oct 2026 | vigente |
| D-02 | Nunca comprar mentoría de alto precio | 24 oct 2026 | vigente |
| D-03 | Nicho faceless: web3 | 25 oct 2026 | vigente |
| D-04 | Go antes que Rust para herramientas | 26 oct 2026 | vigente |
| D-05 | SQLite en Block Ethos; Postgres con más de un escritor | 26 oct 2026 | vigente |
| D-06 | Render solo si Zinli pasa la verificación | 26 oct 2026 | vigente |
| D-07 | Demo en PythonAnywhere mientras no haya tarjeta | 26 oct 2026 | vigente |
| D-08 | Diseño en Dirsi/portátil; teléfono para texto rápido | 27 oct 2026 | vigente |
| D-09 | Portafolio de un solo archivo, sin dependencias | 7 nov 2026 | vigente |
| D-10 | Upwork en espera de LinkedIn | 11 nov 2026 | vigente |
| D-11 | Fase 0 de la auditoría de integración, adoptada condicionalmente | 17 nov 2026 | vigente |
| D-12 | Escala de razonamiento por número de agentes | 17 nov 2026 | vigente |

---

## D-01 — FreeLLMAPI en el portátil, no en el teléfono

- **Decisión:** FreeLLMAPI se instala en el portátil, no en el
  teléfono.
- **Fecha:** 23 oct 2026 (verificación del proyecto; instalado
  en el portátil el 6 nov 2026).
- **Estado:** vigente (verificado 16 nov 2026: instalado en el
  portátil, app de escritorio v0.16.20, funcionando de extremo
  a extremo a 0,00 $).
- **Contexto:** FreeLLMAPI es un router local (MIT) que reúne
  las claves gratuitas del usuario detrás de un solo endpoint
  compatible con la API de OpenAI, con failover automático
  entre proveedores. Es una herramienta de escritorio: su
  valor es amplitud de catálogo más failover a mitad de tarea,
  y las claves quedan cifradas en la propia máquina del
  usuario.
- **Alternativas descartadas:**
  - *Instalarlo en el teléfono:* descartado; es app de
    escritorio y el teléfono es el entorno de aprendizaje y
    texto rápido, no de herramientas pesadas (ver D-08).
  - *Usarlo como nube con claves compartidas:* descartado por
    falso — corre en la propia máquina, no es una nube.
- **Fuente:** `aprendido/agentes-e-ia.md`, «FreeLLMAPI: el
  router local» — «Decisión tomada: instalarlo en el portátil,
  no en el teléfono»; «Instalado en el portátil el 6 nov 2026:
  app de escritorio v0.16.20, gateway local en
  `http://127.0.0.1:31415/v1`, funcionando de extremo a extremo
  a 0,00 $». Matiz registrado en la misma fuente: la
  configuración de OpenCode mezcló la credencial de Zen con
  la clave del router (error 401); la corrección quedó
  pendiente de verificar. Eso no cambia la decisión de
  ubicación.

## D-02 — Nunca comprar mentoría de alto precio

- **Decisión:** no se compra ni se empuja hacia cursos o
  mentorías de alto precio del ecosistema de divulgadores.
  La decisión por defecto es empezar sin pagar.
- **Fecha:** 24 oct 2026 (rechazo de la oferta de MasterTube,
  3.000 €; la regla quedó registrada en
  `aprendido/portafolio-y-empleo.md`).
- **Estado:** vigente (verificado 16 nov 2026: regla dura en
  vigor, ninguna compra de este tipo realizada).
- **Contexto:** el método útil ya está en la capa gratuita
  verificada. Las ofertas de miles de euros o dólares con
  seguimiento personalizado no aportan un método que no esté
  ya disponible gratis.
- **Alternativas descartadas:**
  - *Pagar MasterTube (3.000 €) u otra mentoría equivalente:*
    descartado; empezar sin pagar y retomar la oferta más
    tarde solo si el intento en solitario falla.
  - *Pagar por un plan superior de herramienta por anticipado:*
    descartado con la misma regla — solo se justifica cuando
    el volumen de ayuda lo exige, no antes.
- **Fuente:** `aprendido/portafolio-y-empleo.md`, «Regla dura:
  nunca comprar mentoría de alto precio» — «No se compra ni se
  empuja hacia cursos o mentorías de alto precio del ecosistema
  de divulgadores (ofertas de miles de euros o dólares con
  seguimiento personalizado). El método útil ya está en la capa
  gratuita verificada»; «Antes de cualquier pago, se exigen por
  escrito precio, condiciones de reembolso y la alternativa
  gratuita. Sin eso, no hay decisión de pago».

## D-03 — Nicho faceless: web3

- **Decisión:** el nicho del contenido sin rostro (faceless)
  es web3, con calidad sobre cantidad: menos canales, pero
  fuertes.
- **Fecha:** 25 oct 2026.
- **Estado:** vigente (verificado 16 nov 2026: el nicho sigue
  siendo web3; el proyecto de contenido está aparcado por
  decisión de Antonio, no abandonado ni cambiado).
- **Contexto:** web3 es novedoso, todavía no viral como
  sistema globalmente reconocido, pero con recorrido esperado
  en los próximos años. Antonio no quiere ser «más del
  montón»: prefiere contenido exigente y menos canales
  fuertes que multiplicar canales mediocres.
- **Alternativas descartadas:**
  - *Nicho de trading:* descartado por demasiado difícil y
    poco atractivo.
  - *Nicho «del bootcamp al primer empleo»:* descartado por
    audiencia demasiado estrecha; la gente quiere contenido
    interesante y pragmático.
  - *Multiplicar canales:* descartado; solo tiene sentido si
    cada canal mantiene el nivel.
- **Fuente:** `aprendido/portafolio-y-empleo.md`, «Rutas de
  ingreso: qué se decidió» — «Contenido sin rostro (faceless):
  el nicho decidido es web3 — novedoso, todavía no viral como
  sistema globalmente reconocido, pero con recorrido esperado
  en los próximos años. Se descartaron el nicho de trading
  (demasiado difícil, poco atractivo) y el de "del bootcamp al
  primer empleo" (audiencia demasiado estrecha…».

## D-04 — Go antes que Rust para herramientas

- **Decisión:** empezar por Go para herramientas de uso diario
  (CLIs); dejar Rust para una segunda fase, solo cuando una
  herramienta concreta exija rendimiento o garantías que Go
  no da.
- **Fecha:** 26 oct 2026 (creación de mundo-dirsi y de la
  Ruta 3).
- **Estado:** vigente (verificado 16 nov 2026: ninguna
  herramienta construida en Go se ha quedado corta de
  rendimiento; no hay evidencia en contra).
- **Contexto:** Go tiene sintaxis pequeña, compilación rápida,
  concurrencia sencilla con goroutines y binarios estáticos
  fáciles de distribuir; cubre el 90 % de las CLIs que hacen
  falta. Rust da control fino y rendimiento máximo, pero con
  una curva de aprendizaje pronunciada.
- **Alternativas descartadas:**
  - *Empezar por Rust:* descartado por curva larga para
    herramientas que Go cubre bien.
  - *Reescribir todo el catálogo en Rust si una herramienta
    se queda corta:* descartado; solo esa herramienta
    concreta sería candidata a reescribirse, no todo el
    catálogo.
- **Fuente:** `por-aprender/rutas.md`, Ruta 3, Paso 1 —
  «empezar por Go para herramientas de uso diario, porque su
  curva es corta, sus binarios se distribuyen sin fricción y
  cubre el 90% de las CLIs que hacen falta; dejar Rust para la
  segunda fase, cuando una herramienta concreta exija
  rendimiento o garantías que Go no da»; «si alguna sí [se
  queda corta], esa herramienta concreta es la candidata a
  reescribir en Rust, no todo el catálogo».

## D-05 — SQLite en Block Ethos; Postgres con más de un escritor

- **Decisión:** Block Ethos corre sobre SQLite. La migración
  a Postgres se hará solo cuando aparezca una señal clara:
  varios procesos escribiendo a la vez, necesidad de tipos o
  búsquedas avanzadas, o un despliegue con más de una
  instancia.
- **Fecha:** 26 oct 2026 (creación de mundo-dirsi y de la
  Ruta 5, donde quedó escrita la regla; Block Ethos corre
  sobre SQLite y su README y About lo dicen).
- **Estado:** vigente (verificado 16 nov 2026: Block Ethos
  sigue con un solo escritor; ninguna señal de migración
  presente).
- **Contexto:** SQLite es un archivo, sin servidor, perfecto
  para un solo proceso y prototipos. Postgres es un servidor
  con usuarios, permisos, tipos avanzados, índices
  concurrentes y escritura concurrente real. La elección se
  justifica por escrito, no por costumbre.
- **Alternativas descartadas:**
  - *Postgres desde el principio para Block Ethos:*
    descartado; un solo proceso escritor no justifica un
    servidor de base de datos.
  - *Quedarse en SQLite cuando aparezcan varios escritores:*
    descartado; esa es la señal de migrar.
- **Fuente:** `por-aprender/rutas.md`, Ruta 5, Paso 4 —
  «SQLite es un archivo, sin servidor, perfecto para un solo
  proceso y prototipos; Postgres es un servidor con usuarios,
  permisos, tipos avanzados, índices concurrentes y escritura
  concurrente real. Señales de que hay que migrar: varios
  procesos escribiendo a la vez…»; Block Ethos sobre SQLite:
  memoria del usuario (MEMORY.md, entrada Block Ethos) — su
  README y About dicen SQLite con la demo en vivo.

## D-06 — Render solo si Zinli pasa la verificación

- **Decisión:** Render vuelve a ser viable solo si la tarjeta
  virtual Visa prepago de Zinli pasa su verificación. Si el
  procesador la rechaza por ser prepaga, se deja de considerar
  Render y no se pierde más tiempo con intentos.
- **Fecha:** 26 oct 2026 (Zinli identificada como opción ese
  día).
- **Estado:** vigente (verificado 16 nov 2026: la pregunta
  sigue abierta — pregunta 2 de
  `por-aprender/preguntas-abiertas.md` — y el experimento
  aún no se ha hecho).
- **Contexto:** Render pide una tarjeta para verificar la
  cuenta. Una tarjeta de débito en moneda local puede no
  funcionar; una billetera digital en dólares con tarjeta
  virtual Visa prepago internacional, apta para comercio
  electrónico, encaja en principio con la verificación. La
  incertidumbre sin resolver es si el procesador de Render
  rechaza específicamente las tarjetas prepago. Solo probarlo
  lo resuelve, y un rechazo no cuesta nada.
- **Alternativas descartadas:**
  - *Insistir con la tarjeta local que ya falló:* descartado;
    un intento fallido puede dejar la cuenta sin tarjeta
    registrada, sin servicios y sin cargos, como si el
    intento no hubiera ocurrido.
  - *Dar Render por viable sin probar:* descartado; la
    incertidumbre solo la resuelve el experimento.
- **Fuente:** `aprendido/despliegue.md`, «Render: lo que hay
  que saber antes de prometer nada» — «Una billetera digital
  en dólares con tarjeta virtual Visa prepago internacional,
  apta para comercio electrónico, encaja en principio con la
  verificación de Render. Queda una incertidumbre sin
  resolver: si el procesador de Render rechaza
  específicamente las tarjetas prepago. Solo probarlo lo
  resuelve, y un rechazo no cuesta nada»;
  `por-aprender/preguntas-abiertas.md`, pregunta 2 — «si
  Zinli funciona, Render vuelve a ser viable para despliegues
  con base de datos permanente; si el procesador la rechaza
  por ser prepaga, hay que dejar de considerarlo».

## D-07 — Demo en PythonAnywhere mientras no haya tarjeta

- **Decisión:** la demostración pública de Block Ethos vive
  en PythonAnywhere (cuenta gratuita, sin tarjeta) mientras
  no haya una tarjeta que pase la verificación de Render.
- **Fecha:** 26 oct 2026 (primera demostración pública real
  ese día).
- **Estado:** vigente (verificado 16 nov 2026: la demo sigue
  en vivo en PythonAnywhere; no hay tarjeta verificada en
  Render).
- **Contexto:** la cuenta gratuita de PythonAnywhere no pide
  tarjeta y sirve para una primera demostración pública real.
  Sus límites conocidos: las consolas gratuitas no tienen
  Node ni npm, y el despliegue de un frontend ya construido
  exige otros medios. Para una demo personal sirve; para un
  cliente, el nivel gratuito no basta (ver el piso de
  producción en `aprendido/despliegue.md`).
- **Alternativas descartadas:**
  - *Esperar a tener tarjeta antes de tener demo pública:*
    descartado; PythonAnywhere permitió una demo real sin
    tarjeta desde el primer día.
  - *Usar el nivel gratuito para un cliente:* descartado;
    duerme servicios, las bases de datos caducan y no hay
    copias de seguridad serias.
- **Fuente:** `aprendido/despliegue.md`, «PythonAnywhere: el
  camino sin tarjeta» — «La cuenta gratuita no pide tarjeta y
  sirve para una primera demostración pública real»;
  `crecimiento/log.md`, 2026-10-26 — «Primera demostración
  pública real: cuenta BC123, URL
  https://BC123.pythonanywhere.com, con el repo clonado,
  migraciones aplicadas y seed completo».

## D-08 — Diseño en Dirsi/portátil; teléfono para texto rápido

- **Decisión:** el trabajo de diseño y las demostraciones exigentes
  se hacen en Dirsi o en el portátil; el teléfono queda para
  aprender y para cambios rápidos de texto o código ligero.
- **Fecha:** 27 oct 2026 (experiencia origen: 21 oct 2026).
- **Estado:** vigente (verificado 16 nov 2026: sigue siendo la
  regla práctica en uso).
- **Contexto:** Antonio trabaja casi siempre desde el teléfono
  pero exige calidad visual alta. El 21 oct 2026 el modelo
  pequeño del teléfono decepcionó en diseño, y las demos
  (barbería, portfolio, web3) las construyó Dirsi, no el
  teléfono. El teléfono tiene además límites reales: pantalla
  pequeña para diseño visual, batería y permisos del sistema,
  y ausencia de GPU.
- **Alternativas descartadas:**
  - *Diseñar en el teléfono con el modelo pequeño:* descartado
    por la experiencia del 21 oct — la calidad no alcanzó el
    listón exigido.
  - *Prometer en el teléfono lo que solo sale bien en el
    portátil:* descartado; saber dónde está el límite real
    evita prometer de más.
- **Fuente:** `por-aprender/preguntas-abiertas.md`, pregunta 11
  (cerrada el 27 oct 2026) — «Regla resultante: diseño en
  Dirsi/portátil, teléfono para aprendizaje y texto rápido»;
  `aprendido/agentes-e-ia.md`, «Teléfono (Termux + OpenCode)
  frente a portátil» — «diseño y demostraciones exigentes, en
  el agente grande o en el portátil; el teléfono, para aprender
  y para cambios rápidos».

## D-09 — Portafolio de un solo archivo, sin dependencias

- **Decisión:** el portafolio es un solo archivo HTML+CSS,
  sin dependencias externas, con el sistema diseno_vitrina.
- **Fecha:** 7 nov 2026 (rediseño; publicado en repo propio
  con GitHub Pages el 16 nov 2026).
- **Estado:** vigente (verificado 16 nov 2026: publicado tal
  cual, HTTP 200 verificado).
- **Contexto:** el borrador anterior (21 oct) cargaba Tailwind
  por CDN. El rediseño del 7 nov lo sustituyó por un solo
  archivo sin dependencias externas: tema claro editorial,
  acento marino, datos reales, Block Ethos destacado, correo
  visible y objetivo «Full Stack» sin especializar. Sin la
  frase «con usuarios reales»: Block Ethos aún no los tiene.
- **Alternativas descartadas:**
  - *Mantener el borrador con Tailwind por CDN:* descartado
    en el rediseño del 7 nov; dependencia externa innecesaria
    para una página estática.
  - *Especializar el objetivo en Frontend:* descartado por
    orden de Antonio; el objetivo queda solo «Full Stack».
  - *Afirmar usuarios reales en Block Ethos:* descartado;
    aún no los tiene y no se afirma en público.
- **Fuente:** `aprendido/portafolio-y-empleo.md`,
  «Actualización 16 nov 2026 — portafolio publicado y repos
  ordenados» — «Un solo archivo HTML+CSS, sin dependencias
  externas, sistema diseno_vitrina: Block Ethos destacado,
  correo visible, objetivo «Full Stack» sin especializar. Sin
  la frase «con usuarios reales»: Block Ethos aún no los
  tiene».

## D-10 — Upwork en espera de LinkedIn

- **Decisión:** completar el perfil de Upwork espera a que
  LinkedIn esté listo, porque Upwork enlazado a LinkedIn se
  lee más profesional.
- **Fecha:** 11 nov 2026 (cuenta creada por Antonio ese día;
  decisión tomada el mismo día).
- **Estado:** vigente (verificado 16 nov 2026: el borrador
  sigue listo y sin completar; LinkedIn sigue en preparación).
- **Contexto:** la cuenta de Upwork ya existe y el borrador
  de perfil está listo. Quedan pendientes la tarifa por hora,
  el método de pago y la renovación de la cédula (vencida),
  que bloquea la verificación de identidad en Upwork y demás
  plataformas.
- **Alternativas descartadas:**
  - *Completar Upwork ahora, sin LinkedIn:* descartado por
    decisión de Antonio; enlazado a LinkedIn se lee más
    profesional.
  - *Dejar Upwork para después del primer empleo:* no se
    descartó el canal; solo se ordenó la secuencia —
    LinkedIn primero, Upwork después.
- **Fuente:** `aprendido/portafolio-y-empleo.md`,
  «Actualización 16 nov 2026» — «Upwork: cuenta creada por
  Antonio el 11 nov 2026; borrador de perfil listo.
  Completarlo espera a LinkedIn, por decisión suya: Upwork
  enlazado a LinkedIn se lee más profesional».

## D-11 — Fase 0 de la auditoría de integración, adoptada condicionalmente

- **Decisión:** adoptar el primer paquete de mecanismos contra los
  fallos de integración (M5, M1r, M3, M6 y la regla de emergencia),
  de forma condicional: nada sobrevive sin la corrida ciega
  R-01–R-06, con una semana 0 de rodaje sin puntuar (17–22 nov
  2026) antes de la primera semana puntuable.
- **Fecha:** 17 nov 2026 (auditoría nocturna 01:03–01:13;
  adopción por Antonio a las 18:07).
- **Estado:** vigente (verificado 23 nov 2026: semana 0
  terminada; primera semana puntuable en curso desde el 23 nov;
  corrida ciega R-01–R-06 ejecutada y puntuada el mismo día, X 8,5/9
  e Y 8,33/9, baremo 6/6 no evaluable por el bloqueo del clon en
  R-06; la supervivencia la decide la medición de 3 semanas).
- **Contexto:** la auditoría de integración (11 agentes) encontró
  0 de 28 fallos por dato ausente — todo era integración — y que
  en 4 de 6 incidentes la regla ya existía y no se aplicó. La
  línea base era 7 FI en la semana 9–16 nov (2 graves). La
  respuesta no fue añadir proceso por añadir: cada mecanismo
  nuevo debía justificarse por un fallo demostrado y medirse con
  una corrida ciega.
- **Alternativas descartadas:**
  - *No adoptar nada hasta la corrida ciega:* descartado; las
    piezas de coste ~0 (M5, el registro de hilos) valían desde
    el primer día, y la semana 0 de rodaje permitía probarlas
    sin puntuar.
  - *Adoptar los 6 mecanismos propuestos sin condición de
    medición:* descartado; la adopción es condicional a la
    corrida ciega, y M4f (perspectiva fusionada) no entró en
    la Fase 0.
  - *Mover el umbral si no se cumple:* descartado por diseño;
    si no se cumple, se prorroga y se registra qué condición
    falló.
- **Fuente:** `REGISTRO-INTEGRACION.md` — «Publicado en
  mundo-dirsi el 17 nov 2026 (Fase 0 de la auditoría de
  integración, aprobada por Antonio)»; «Si no se cumple, no se
  mueve el umbral: se prorroga y se registra qué condición
  falló»; informe de la auditoría
  (`~/workspace/auditoria-integracion-2026-11-17/INFORME.md`,
  fuera de este repo).

## D-12 — Escala de razonamiento por número de agentes

- **Decisión:** graduar el razonamiento del sistema por el número
  de agentes que trabajan con Dirsi al centro: Bajo (Dirsi sola),
  Medio (+2), Alto (+6), Extra (+12), Max (+12, uso único con
  presupuesto explícito). Desde Medio, revisión cruzada
  exhaustiva obligatoria y comunicación integral constante.
- **Fecha:** 17 nov 2026 (propuesta por Antonio y adoptada el
  mismo día; correcciones de diseño el 18 nov).
- **Estado:** vigente (verificado 23 nov 2026: la primera
  calibración, 18 nov, no calibró los números 2/6/12 — en los
  criterios binarios del banco los 4 niveles empatan a 3/3 —,
  pero la escala sigue vigente como amplitud con revisión
  cruzada; lo que crece con los agentes es la profundidad y la
  caza de errores).
- **Contexto:** Antonio propuso la escala como forma de controlar
  un sistema de razonamiento artificial que cumpliera casi lo
  mismo que los niveles nativos de razonamiento de modelos como
  Claude. La escala es amplitud (más ángulos, más chequeo), no
  la profundidad de una sola cadena de pensamiento; todos los
  agentes corren sobre el mismo motor y comparten puntos ciegos.
- **Alternativas descartadas:**
  - *Un agente solo, sin retroalimentación ni integración con
    Dirsi, como nivel:* descartado por Antonio; no es un
    nivel, es una configuración rota.
  - *Equipos fijos por tarea (3 parejas en Medio):* probado y
    descartado el 18 nov; el diseño vigente es un solo equipo
    por nivel, con Dirsi al centro.
  - *Usar los niveles nativos de razonamiento del modelo:*
    descartado por inexistente en este chat; no hay mando de
    razonamiento, el motor es la palanca.
- **Fuente:** `ESCALA-RAZONAMIENTO-AGENTES.md` — «Propuesta por
  Antonio y adoptada el 17 nov 2026»; «Un agente solo, sin
  retroalimentación de otro agente y sin integración con Dirsi,
  NO es un nivel: es una configuración rota»; «Dirsi es el
  centro en cada escenario»; `CALIBRACION-ESCALA-2026-11-18.md`
  (primera calibración: 3/3 en los 4 niveles, acuerdo 12/12).
