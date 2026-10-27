# Recopilación de materiales — Antonio

Compilado el 27 de octubre de 2026 a partir de 10 enlaces enviados por Antonio
el 27 de octubre de 2026 a las 02:49 (hora de Caracas), más los materiales
previos que ya estaban analizados. Actualizado el mismo día con un segundo
lote enviado a las 10:58: la guía de 11 skills para YouTube, 3 repositorios
de skills del mismo autor y la copia del PDF de automatizaciones que
faltaba (M9, ahora leído). Redactado con palabras propias: este
archivo NO contiene textos de cursos ni archivos con copyright, solo
resúmenes y estructuras. Los PDFs originales NO están en este repo
(están en la carpeta de trabajo local, fuera de mundo-dirsi).

## 1. Propósito y cómo usarlo

Si eres una IA (Claude, ChatGPT, Dirsi u otra) y Antonio te pasa este
archivo, úsalo como contexto completo: quién es, qué busca, qué materiales
tiene, qué se puede usar ya y qué queda guardado para otros contextos.
Es, en la práctica, su "cerebro de contexto": el documento que evita
empezar de cero en cada conversación.

Reglas para quien lo lea:

- Usa las estructuras, ideas y criterios aquí destilados, con tus propias
  palabras. No republicar textos de cursos.
- Respeta los estados: lo marcado "no legible" o "parcial" NO lo des por
  leído ni inventes su contenido.
- Respeta los niveles de evidencia: A = demostrado de primera mano
  (leído aquí o en análisis previos del equipo); B = resumen fiable de
  segunda mano, verificado contra el índice o la fuente; C = afirmación
  del creador o marketing, no un hecho; X = retractado (aquí no hay
  ninguno, pero la regla rige).
- Si algo dice "sin verificar", no lo presentes como hecho.

## 2. Quién es Antonio (10 líneas)

1. Antonio José Mieres Garabote, 31 años, Venezuela (zona America/Caracas).
2. Graduado de 4Geeks como Full Stack Developer con IA (React, Flask,
   Python, JavaScript, SQL, JWT, APIs REST); sin experiencia laboral aún.
3. Busca trabajo remoto; meta: concretar en noviembre/diciembre de 2026
   una beca, un freelance o un contrato (aspira a un piso de ~$800 en un
   empleo).
4. Nicho elegido para contenido: web3; quiere vivir creando contenido en
   YouTube y TikTok.
5. Proyecto final Blockali (plataforma de aprendizaje blockchain con rutas,
   quizzes y certificados verificables), en vivo en PythonAnywhere.
6. Posicionamiento en curso: GitHub ordenado (perfil, repos propios),
   LinkedIn pendiente de publicar (titular, sobre mí, alertas por
   reconfigurar, contacto con una reclutadora IT pendiente).
7. Brecha honesta: poca fluidez de sintaxis; trabaja entendiendo dónde
   modificar siguiendo lo que la IA le indica. Prefiere efectividad y
   pipeline antes que pulido infinito.
8. Teléfono primero (Xiaomi 14T Pro); laptop ASUS con Claude web (plan
   Free). No puede copiar líneas aisladas en el móvil: el texto copiable
   va en mensaje o archivo propio.
9. Regla de evidencia: hechos demostrados o clasificados; el marketing
   no es un hecho; no se copian textos de cursos.
10. Delegación total en Dirsi para repos y despliegues; el único paso
    manual que guarda son las claves y valores .env.

## 3. Catálogo de materiales

### Hoy, 27 de octubre de 2026 (10 fuentes, más segundo lote)

#### M1. Guía de agentes con Google (CenteIA) — LEÍDO [A]

- Enlace: https://drive.google.com/file/d/1KZVfkcMkvVrd1-Inl2emGcQQ1L8buzU6/view?usp=drivesdk
- Tipo: PDF de CenteIA, modificado el 13 de octubre de 2026, guía
  revisada el 13/10/2026.
- Resumen: guía práctica (20–30 min, cero código) para crear un primer
  agente con herramientas de Google. Explica que Google ofrece tres
  puertas (el estudio de agentes de Gemini Enterprise como recomendada,
  la vía técnica en Google Cloud y el estudio dentro de Workspace) y que
  la diferencia frente a un chatbot es que el agente consulta buscador y
  mapas en el momento y trabaja con los documentos y el correo del
  usuario, así que responde con datos actuales y no con lo memorizado.
  Da un método en 8 pasos (abrir la app, crear el agente, describirlo en
  chat, elegir datos y archivos, revisar el lienzo que dibuja, probarlo,
  programarlo y publicarlo) y una plantilla para describirlo (nombre,
  equipo, objetivo concreto, cuándo trabaja, qué datos usa, qué entrega,
  tono, idioma y límites). Incluye 5 agentes listos por área: radar
  semanal de competencia con buscador, prospector de negocios locales
  con mapas, primer borrador de respuestas de soporte desde correo y
  documentos, control semanal de facturas en correo y hojas de cálculo,
  e informe del lunes que combina documentos, correos y noticias.
  Reglas que repite: empezar por una tarea pequeña y repetitiva, poner
  límites de longitud y formato, pedir que cite fuentes y que diga
  cuando no sabe algo, probar antes de publicar y no dejar que envíe
  correos ni pague sin aprobación.
- Usable AHORA: la plantilla para describir un agente y la regla de
  "una tarea pequeña, límites claros, revisión antes de enviar" sirven
  para cualquier agente que Antonio pida, en cualquier herramienta. Los
  5 agentes son modelos adaptables a su propio trabajo (por ejemplo,
  un radar de noticias web3 o un informe semanal).
- Guardado PARA DESPUÉS: la instalación en Gemini Enterprise o Workspace
  Studio exige cuenta de Google de empresa y planes de pago (el precio
  orientativo que cita, unos 21 $ por usuario al mes con compromiso
  anual a julio de 2026, es [C] y hay que confirmarlo antes de
  contratar). No aplica hoy con su cuenta personal.
- Estado: leído íntegro de primera mano.

#### M2. OmniRoute paso a paso (CenteIA) — LEÍDO [A]

- Enlace: https://drive.google.com/file/d/1RUcsJUQespxQWZkEDn1t4Ety1RUVdbxb/view?usp=drivesdk
- Tipo: PDF de CenteIA, modificado el 16 de octubre de 2026, guía
  revisada el 14/10/2026.
- Resumen: guía de instalación (10 min, gratis, licencia MIT) de un
  router local y de código abierto que conecta herramientas de
  programación con IA (Claude Code, Cursor, Copilot y otras) a muchos
  proveedores de modelos. Su idea es una carrera de relevos: cuando un
  proveedor agota su cuota, salta solo al siguiente sin cortar la
  sesión, y además comprime los prompts antes de enviarlos para gastar
  menos tokens. Se instala con Node.js 22 o 24, se abre un panel local
  y desde ahí se conectan proveedores y se eligen modos automáticos
  según se priorice programar, ir rápido o gastar poco. Se conecta a
  cada herramienta con una dirección local y una clave. Advierte que
  los modelos gratuitos varían en calidad, que el código y los prompts
  pasan por proveedores externos (no usar con datos confidenciales de
  clientes) y que hay que respetar las condiciones de cada proveedor.
- Usable AHORA: el concepto (relevo automático + compresión) y la ruta
  de instalación para la laptop, cuando Antonio se siente en ella. Es
  una alternativa a evaluar frente a la ruta de router local que ya
  tiene preparada (FreeLLMAPI); no se presenta como reemplazo, sino
  como opción a comparar.
- Guardado PARA DESPUÉS: la configuración multi-proveedor y los modos
  automáticos, para cuando use Claude Code, Cursor o Copilot de forma
  habitual.
- Estado: leído íntegro de primera mano. Cautelas: el ahorro de tokens
  en torno al 89 % y los "más de 150 proveedores gratuitos" son
  afirmaciones del propio proyecto [C], no verificadas aquí. El
  repositorio que cita la guía no se ha verificado de primera mano.

#### M3. Página CenteIA de profesiones IA — CERRADO: la fuente no aporta más

- Enlace: https://training.centeia.com/profesiones-ia/?utm_term=01a179c7-8b7a-74ee-b1f7-8fd539b204f1&fbclid=PAT01DUAVM9RpleHRuA2FlbQIxMABwZG9mAnNydGMGYXBwX2lkDzU2NzA2NzM0MzM1MjQyNwABp2YzBl_wSWIin9p_BON5syvcNHQVvAH_TdR_XBcZCrqw80j5MJziZ1Cq7zHP_aem_MgJtZOYozHMnj_sRVJCD9w
- Tipo: página web (landing) de CenteIA.
- Resumen: solo se extrajo el encabezado. Es una landing de captación
  para un "Diagnóstico ocupacional" que plantea una pregunta: cuánto
  le queda a un trabajo tal y como se hace hoy. Muestra horarios por
  zona. No se extrajo contenido sustantivo.
- Usable AHORA: casi nada, salvo la pregunta que plantea, útil como
  reflexión para posicionamiento (qué partes de un trabajo resisten
  frente a la IA y cuáles no).
- Guardado PARA DESPUÉS: nada; la fuente es una landing de captación
  y no hay más contenido que extraer de ella.
- Estado: cerrado el 27 oct 2026 — la fuente no aporta más que el
  encabezado y la pregunta que plantea. No se inventa contenido.

#### M4. ChatGPT sin sonar a IA (CenteIA) — LEÍDO [A]

- Enlace: https://drive.google.com/file/d/159FPBBZnEl5YHO7w4DcsaJcZheGdtErw/view?usp=drivesdk
- Tipo: PDF de CenteIA, modificado el 20 de octubre de 2026, guía
  revisada el 14/10/2026.
- Resumen: guía (10 min, gratis, para ChatGPT web y app) para que los
  textos dejen de delatarse como escritos por IA. Aclara primero que
  lo que delata un texto no es una marca oculta (en 2025 se detectaron
  caracteres invisibles en algunos textos y el proveedor dijo que era
  un efecto secundario del entrenamiento, ya corregido; hoy no hay
  marca), sino cómo está escrito: palabras repetidas, estructuras
  calcadas y un tono que no suena a nadie. El método tiene 2 prompts y
  un ajuste: primero pedir que lea la guía pública de Wikipedia sobre
  señales de escritura de IA y liste los patrones con ejemplos en
  español; después convertir esa lista en reglas permanentes breves y
  guardarlas en la personalización, sin borrar lo que ya hubiera. Da
  un ejemplo de antes y después, un modo de revisar textos que ya se
  tienen y un aviso de uso responsable: sirve para sonar como uno
  mismo, no para presentar como propio un trabajo que piden hacer sin
  IA; la mejor señal humana sigue siendo tener algo propio que decir.
- Usable AHORA: las reglas de escritura, parafraseadas: frases cortas
  y variadas, una idea por frase, evitar muletillas típicas de IA y
  estructuras calcadas (como la negación seguida de afirmación o los
  cierres con resumen), no exagerar la importancia de las cosas, decir
  "no sé" cuando no se sabe, y revisar el texto antes de entregarlo.
  Aplica a sus posts de LinkedIn, CV, mensajes a reclutadores y
  guiones de contenido.
- Guardado PARA DESPUÉS: el ajuste de personalización en ChatGPT
  (2 minutos), para cuando use ChatGPT de forma habitual.
- Estado: leído íntegro de primera mano. Nota: la guía incluye su
  propia plantilla de reglas; aquí NO se reproduce, solo se resume,
  por la regla de no copiar textos de cursos.

#### M5. Instagram Skills, manual (CenteIA) — LEÍDO [A]

- Enlace: https://drive.google.com/file/d/1x2Cbw62qbg8h7uS6On_g_l-XcvIbUHvu/view?usp=drivesdk
- Tipo: PDF de CenteIA, modificado el 19 de octubre de 2026, guía
  revisada el 14/10/2026.
- Resumen: manual (10 min, gratis, licencia MIT) de un paquete de 9
  habilidades para Claude, orientadas a Instagram: escribir copies con
  el gancho en los primeros caracteres según el objetivo (guardados,
  compartidos, comentarios o seguidores); planificar carruseles de
  hasta 10 diapositivas (portada con gancho, valor y cierre); analizar
  el gancho de un reel o carrusel viral y encajarlo en una de 10
  fórmulas con plantilla para rellenar; elegir 3 a 5 hashtags mezclando
  nicho, alcance medio y amplio; quitar el tono de IA con modo de
  auditoría antes de publicar; planificar la semana (formatos, temas,
  ganchos y horas); convertir un post, blog o guion en carrusel o
  copy; auditar y reescribir perfil (bio, enlace, destacadas, fijados)
  con puntuación; y buscar tendencias por hashtag y datos de cuentas
  (esto último exige cuenta en otro servicio). Se instala pegando un
  enlace en la sección de habilidades de Claude, y advierte que hay
  copias del paquete publicadas por otras cuentas: instalar solo desde
  el original. El truco central que enseña: tomar 3 publicaciones que
  funcionaron, entender por qué, y convertirlas en algo propio (guion
  de reel, opciones de primera frase, pasada por el humanizador). La
  publicación automática opcional pasa por otro servicio con registro
  gratuito, exige cuenta de empresa o creador y algo de configuración
  técnica; el consejo de la guía es empezar publicando a mano y
  automatizar solo cuando se confíe en el resultado. Buenas prácticas:
  dar ejemplos de los mejores posts propios para captar la voz, no
  copiar a otros palabra por palabra, no llenar de hashtags, verificar
  datos antes de publicar, responder comentarios uno mismo y medir
  qué gancho funciona para repetirlo.
- Usable AHORA: el método (analizar qué funcionó, extraer la fórmula,
  convertirlo en algo propio con tus palabras), la regla de 3 a 5
  hashtags, la pasada de humanizador y la estructura del plan semanal.
  Sirve para su futuro contenido en Instagram/TikTok aunque las
  habilidades en sí sean para Claude, no para Dirsi.
- Guardado PARA DESPUÉS: la instalación completa del paquete cuando
  use Claude (web, escritorio o Code), y la publicación automática
  solo después de confiar en los resultados.
- Estado: leído íntegro de primera mano. Cautela: el repositorio
  original que cita la guía no se ha verificado de primera mano.

#### M6. Arena de vídeo (arena.ai) — PARCIAL, corrección sobre "gratis y open source"

- Enlace: https://arena.ai/video?utm_term=01a179c7-8b7a-74ee-b1f7-8fd539b204f1
- Tipo: herramienta web interactiva ("Video Arena: compara los mejores
  generadores de vídeo con IA"), de votación y comparación.
- Resumen: es una herramienta, no un artículo. Permite comparar
  generadores de vídeo con IA mediante votación. No se extrajo un
  veredicto ni un ranking aprovechable.
- Corrección (27 de octubre, segundo lote): gratis SÍ con cuenta
  (según guía externa de octubre de 2026: se entra con cuenta, la
  arena genera dos vídeos de modelos anónimos por prompt, se comparan,
  se vota y se puede descargar; hay rankings públicos por texto,
  imagen, vídeo y agente). Open source NO establecido para la
  plataforma: arena.ai es una plataforma alojada que exige cuenta; la
  pieza de código abierto es un agente de desarrollador aparte (Sarus
  Arena), no la plataforma misma. No afirmar que arena.ai es open
  source.
- Usable AHORA: como comparador antes de elegir una herramienta de
  vídeo para producir contenido (relevante para su meta de YouTube y
  TikTok y para los límites de generación de vídeo que ya conoce).
- Guardado PARA DESPUÉS: una evaluación a fondo cuando vaya a elegir
  herramienta de vídeo.
- Estado: parcial (herramienta registrada, sin veredicto extraído).

#### M7. 3 proyectos de IA para dejar de empezar de cero (Doc) — LEÍDO [A]

- Enlace: https://docs.google.com/document/d/1OXBzuSMEyW-aRoVbYQQlXkwAc9uA6WgFqD4CVy6CVtk/edit?usp=drivesdk
- Tipo: documento de Google, recurso gratuito de CenteIA Education
  2026, sin fecha conocida.
- Resumen: un plan de fin de semana, un proyecto por día, para dejar
  de empezar de cero en tres momentos habituales. Sábado: crear un
  "cerebro de contexto", una carpeta con cinco documentos (quién soy
  y qué hago; audiencia, clientes y proyectos; oferta y mensajes
  clave; voz y ejemplos; reglas de trabajo) que se sube a un proyecto
  de ChatGPT o Claude o se adjunta al inicio de una conversación
  importante, con plantillas para crear ese contenido y para usarlo
  después. Domingo: convertir publicaciones guardadas de Instagram en
  ideas propias, con una base de notas con cinco campos (referencia,
  por qué se guardó, idea central, adaptación para la marca, estado)
  y una revisión semanal de las cinco mejores, analizando qué
  mecanismo hace que funcione y creando ideas originales con gancho,
  idea central y ejemplo práctico, sin copiar el texto ni el ejemplo.
  Lunes: dejar lista la base de una newsletter semanal con tres
  documentos (fuentes, plantilla y voz), guardando durante la semana
  solo las fuentes que se podrían explicar a otra persona, y con una
  lista de comprobación antes de enviar (cada afirmación con fuente
  real, nada que no se pueda defender, asunto reescrito hasta decir
  qué gana el lector). Regla para los tres proyectos: la IA ordena,
  resume y propone; la persona decide qué conserva, publica o envía.
- Usable AHORA: el concepto de cerebro de contexto (este mismo
  archivo es una versión de él) y la regla de "un proyecto por día"
  como antídoto contra la niebla: una sola cosa, no cinco. El método
  de guardados a ideas sirve directamente para su contenido futuro.
- Guardado PARA DESPUÉS: la base de newsletter, para cuando tenga
  audiencia o lista a la que escribir.
- Estado: leído íntegro de primera mano (texto completo extraído vía
  conector de Docs).

#### M8. Multiplica tu productividad con IA, 45 prompts (CenteIA) — LEÍDO [A/B]

- Enlace: https://training.centeia.com/wp-content/uploads/2026/06/Multiplica-tu-productividad-y-aumenta-tu-valor-profesional-utilizando-Inteligencia-Artificial_compressed.pdf
- Tipo: PDF de CenteIA, junio de 2026, 45 prompts listos para copiar y
  pegar en ChatGPT (o herramienta similar).
- Resumen: guía de introducción amable (qué es un prompt, por qué
  cuanto más clara y específica sea la instrucción, mejor el
  resultado) seguida de 45 prompts en 15 roles profesionales, 3 por
  rol. Cada rol abre con su perfil y tareas clave, y cada prompt sigue
  la misma estructura en 6 campos: acción, pasos, persona, contexto,
  restricciones y plantilla. Los 15 roles son: administrativo general,
  responsable de facturación, contable, asistente de dirección,
  especialista en marketing digital, diseñador gráfico/multimedia,
  docente o formador interno, técnico de soporte IT, analista de
  datos, psicólogo organizacional o coach interno, responsable de
  recursos humanos, responsable de operaciones, logística o almacén,
  legal o asesor jurídico interno, y gestor de proyectos. En líneas
  generales, los prompts sirven para ordenar trabajo repetitivo de
  oficina y de gestión (documentos, agendas, correos, facturas,
  cierres, informes, planes, diagnósticos y comparaciones) y devolver
  salidas cortas y usables: tablas, checklists, borradores e informes
  breves. El cierre presenta los 45 prompts como kit de referencia,
  insiste en que la clave es ser claro y dar contexto, recuerda que
  las decisiones siguen siendo humanas, anima a adaptar y experimentar
  con los prompts, e invita a un club gratuito de IA por WhatsApp
  llamado Círculo CenteIA.
- Usable AHORA: la estructura de 6 campos como plantilla para pedir
  bien a cualquier IA (es la misma estructura del bloque de
  productividad de los 90 prompts de la clase 1), y los roles más
  cercanos a Antonio: marketing digital, diseño gráfico, gestor de
  proyectos y docente/formador (estos dos últimos, para su contenido
  y para enseñar).
- Guardado PARA DESPUÉS: el resto de roles como kit de referencia
  para una futura operación freelance (administración, facturación,
  contabilidad, legal, operaciones, logística).
- Estado: leído completo (líneas 0–490 de primera mano; 490–2388
  mediante lectura delegada, verificada contra el índice y el cierre
  leídos de primera mano). NO se reproducen los 45 prompts: solo su
  estructura y su función, por la regla de no copiar textos de cursos.
- Solapamiento a tener en cuenta: los 15 roles coinciden con el
  bloque de productividad de los 90 prompts de la clase 1 (ver P1).
  La identidad prompt a prompt entre ambos documentos NO está
  verificada; queda como pregunta abierta.

#### M9. 5 Automatizaciones y Agentes de IA (CenteIA) — LEÍDO [A] (segundo lote)

- Enlace: https://training.centeia.com/wp-content/uploads/2026/07/5-Automatizaciones-y-Agentes-de-IA_compressed.pdf
- Copia aportada por Antonio:
  https://drive.google.com/file/d/15plDQYAt2CzvLDpritQ9TET1mQxq3NmE/view?usp=drivesdk
- Tipo: PDF de CenteIA, 17 páginas, solo imágenes, sin capa de texto
  (3,36 MB). Leído página por página como imagen el 27 de octubre de
  2026. Análisis completo en
  `~/workspace/centeia-materiales/automatizaciones-analisis.md`.
- Resumen: guía de 5 automatizaciones construidas en Make.com, cada
  una con problema, flujo paso a paso, módulos, cliente ideal, precio
  sugerido, upsell y blueprint JSON. Antes explica las dos plataformas
  (Make.com visual sin código, con blueprints JSON exportables; n8n
  como alternativa de código abierto autoalojable, con la misma
  lógica) y cómo importar un blueprint en Make (cuenta, Scenarios,
  Import Blueprint, conectar cuentas, ajustar variables, activar).
  Consejo de venta que repite: no se vende la automatización, se
  vende el resultado; el setup es el ingreso grande de golpe y el
  mantenimiento mensual es el ingreso recurrente.
- Las 5: (01) analista de CV con IA para RRHH — Drive, OpenAI
  (Assistants API + Vector Store), Markdown, Google Docs; entrega
  resumen, nota 0–5 de encaje y preguntas de entrevista; 800–1500 €;
  blueprint `1_-_Recursos_Humanos.json`. (02) procesador automático
  de facturas con GPT Vision — Gmail, PDF.co, GPT Vision, ChatGPT,
  Sheets; extrae emisor, NIF/CIF, concepto, fecha, base, IVA, total,
  número y pago; 1000–2000 € + 200–400 €/mes; blueprint
  `2_-_Facturacion.json`. (03) captación de leads con Google Maps +
  IA — SerpAPI, Gemini, Sheets; 50/100/200 negocios con teléfono,
  dirección, web y valoración; 500–1500 €; blueprint
  `3_-_Captacion_de_Leads.json`. (04) generador de contenido
  multicanal — Google Forms, router en 3 ramas (Instagram, LinkedIn,
  Blog) con ChatGPT + Ideogram; 1500–3000 € + 300–800 €/mes; blueprint
  `4_-_Redes_Sociales.json`. (05) avatares con IA vía Telegram —
  Telegram, OpenAI (transcripción), ChatGPT (guion), ElevenLabs (voz
  clonada), HeyGen (vídeo), Drive; 2000–4000 € + 500–1000 €/mes.
- Usable AHORA: como especificación de servicios productizados (ruta
  de sistemas de IA para negocios locales): las 5 son fichas vendibles
  completas, reimplementables en código sin depender de Make. Más
  cercanas a Antonio: la 02 y la 03 (patrones que ya domina en
  concepto y conexión directa con negocios locales); la 04 con su
  deseo de contenido; la 05 con avatares y contenido faceless; la 01
  como patrón de análisis de CV reutilizable para su propia búsqueda.
- Guardado PARA DESPUÉS: los blueprints JSON (se nombran pero no
  vienen dentro de este PDF; dependen de su acceso a Círculo), la
  venta como servicio (necesita clientes y cuentas conectadas) y la
  verificación del plan gratuito de Make y del acceso API de LinkedIn
  para publicar en perfiles personales.
- Estado: leído íntegro de primera mano (17 páginas como imagen).
  Cautelas: los precios son sugeridos por la guía, no tarifas
  verificadas; la promesa de portada ("+1500 €/mes") y el
  "+20h/semana" son marketing [C]; la guía tiene 2 errores de edición
  (la página de la 04 repite la frase-resumen de la 02, y la caja de
  blueprint de la 05 repite la de la 03, así que el nombre real del
  JSON de la 05 no aparece); la publicación automática en perfil de
  LinkedIn vía API está restringida en la práctica y conviene
  verificarla antes de vender esa rama; la voz clonada "idéntica" y
  el "lip-sync perfecto" son afirmaciones de la guía [C] y clonar la
  voz de un cliente exige su consentimiento explícito.

#### M10. Clase 1 en vivo "Tu segundo yo 24/7" (YouTube) — LEÍDO vía transcripción [A/B]

- Enlace: https://www.youtube.com/live/we3gUsC7_80?si=Fk2kmbZAn_ePv48-
- Tipo: vídeo en directo de YouTube, primera clase del curso CenteIA
  (CenteIA Education, Jordi Segura y Armand Pujadó; en la página
  figuraba con 53.801 vistas al consultarla).
- Resumen: clase de unas 2 h 18 min leída por transcripción automática
  (sin entrar con cuenta, sin suscribirse). Estructura: bienvenida al
  evento de 3 días (pasar de pedir texto a delegar trabajo); qué se
  verá cada día (día 1: que la IA trabaje por ti; día 2: con tu
  información, experiencia y criterio; día 3: herramientas y ofrecerlo
  como servicio); 3 aprendizajes del día 1 (qué pasa hoy en IA, un
  método concreto para encargar trabajo, cómo la IA trabaja con el
  criterio del usuario); errores a evitar (usar la IA como antes,
  copiar prompts sin entenderlos, guardar herramientas sin método,
  probarla una semana y abandonarla); oportunidad y datos de mercado
  por perfil (empleados, profesionales libres, dueños de empresa,
  nueva vía de ingresos); ejemplos previos (inmobiliaria, entrenador,
  constructora, ferretería); historia del proyecto y testimonios (la
  experiencia del usuario es lo que da valor, no solo la herramienta);
  breve historia de la IA (años cincuenta, especializada, generativa
  desde noviembre de 2022, agéntica hacia 2026); el método ROCE con
  demostración comparativa; qué es un agente y su mapa de capacidades
  con la demo del panel inmobiliario; demos conectadas a Drive y Gmail
  para prospección y seguimiento; cómo lograr que trabaje "como tú"
  (las skills); recapitulación, regalo final (mapa para decidir qué
  delegar) y convocatoria al día siguiente a las 19:00 hora de Madrid
  (14:00 Caracas).
- El método ROCE (técnica de 4 pasos para redactar un buen prompt,
  para ChatGPT, Gemini, Claude, DeepSeek y Copilot; la idea de fondo
  es que el usuario no controla el interior del modelo, sino la
  entrada): R — Rol (en qué experto debe convertirse la IA); O —
  Objetivo (concreto, claro, conciso, directo y medible si se puede;
  primero una parte delimitada, no todo el proyecto); C — Contexto
  (explayarse: quién es el usuario, qué hace, cómo lo hace, dónde
  vive su información, cuáles son sus archivos; la experiencia y el
  criterio propios valen oro aquí); E — Estructura (exactamente cómo
  debe devolver la respuesta: pestañas de un Excel, títulos y orden
  de un informe; la letra que suele olvidarse).
- Demostración en vivo (caso de ejemplo, inmobiliaria Brisa Hábitat;
  cliente Marta, piso Olivo): se descarga la app de escritorio de
  ChatGPT y se crea un proyecto con acceso a una carpeta local de
  confianza (tono, Excel de inmuebles y clientes, consultas,
  protocolos, permisos, proceso semanal, notas, horarios, actividad,
  finanzas). Primero exploración sin cambios (leer todo, tabla de qué
  contiene cada archivo y para qué sirve, preguntas, sin modificar ni
  redactar). Luego se compara un prompt mediocre (responder a Marta y
  proponer visita) con un prompt ROCE (rol comercial, objetivo de
  redactar propuesta, contexto de los archivos, salida en borrador con
  fuentes de cada dato y una pregunta pendiente para Marta): el ROCE
  sale más específico y trazable. Demo agéntica: panel visual de
  cartera para el equipo comercial (contactos, inmuebles, encajes,
  estado de clientes, consultas, inventario, actividad, finanzas,
  acciones del día), con búsqueda en el navegador para comprobar la
  vigencia de información municipal de transporte en Benimaclet,
  Valencia; la IA toma el navegador, se equivoca en algún paso, corrige
  y sigue sin que la toquen; tardó unos 4 minutos y 37 segundos. Demo
  conectada: con enlace de Drive y conectores de Gmail, lee etiqueta y
  archivos, filtra contactos por presupuesto y criterios, crea
  subcarpeta de seguimiento y deja un borrador de correo.
- Límites explícitos ("se detiene donde debe"): en la exploración, no
  cambiar ni redactar nada, solo analizar y preguntar; antes de
  escribir, comprobar si ya existe; en el correo, crear borrador pero
  NO enviarlo (destinatarios en copia oculta, listo para revisión y
  visto bueno); en la respuesta ROCE, entregar borrador con fuentes y
  pregunta pendiente, no inventar ni cerrar el tema; en el panel,
  verificar vigencia externa antes de incorporar; en general, el
  agente tiene control humano y puede limitarse, no tiene que ser
  autónomo si el usuario no quiere.
- Reglas para que trabaje con tus reglas: centraliza y ordena tu
  contexto antes de pedir (si está disperso, el resultado también);
  dale acceso, no subidas repetidas (proyecto o carpeta de confianza,
  enlace de Drive, conectores de las apps que ya usas); especifica
  rol, objetivo y sobre todo formato de salida; añade reglas de no
  hacer (qué no modifica, qué no envía, qué verifica antes de
  escribir); enséñale con ejemplos de trabajo bien y mal hecho,
  referencias propias, marca y tono, no solo instrucciones abstractas;
  encapsula ese conocimiento en una skill (modelo + instrucciones +
  referencias de buen trabajo + contexto + marca + archivos de apoyo),
  reutilizable muchas veces y transportable a otros modelos; empieza
  con una sola herramienta (recomiendan ChatGPT) antes de dispersarte;
  el agente como equipo (control humano, delegación, memoria que
  mejora con el uso, herramientas, corrección de rumbo); el criterio
  humano sigue siendo el límite y el valor (la IA ejecuta lo pesado,
  la persona revisa, decide y envía).
- Usable AHORA: ROCE como plantilla de encargo (compatible con la
  plantilla anti-invención de P3 y la estructura de 6 campos de P1 y
  M8); la regla borrador-sin-enviar; la exploración sin cambios como
  primer paso ante cualquier carpeta; la skill como forma de guardar
  criterio propio (conecta con la ficha voice.md de M11–M14).
- Guardado PARA DESPUÉS: revisión cuando lleguen las clases 2 y 3
  (día 2: con tu información y criterio; día 3: herramientas y
  servicio).
- Estado: leído vía transcripción automática (sin login), recorrida
  desde el inicio hasta ~2 h 18 min. Límites: el vídeo en sí no se
  reprodujo (el reproductor quedó cubierto por un aviso de acceso),
  así que no se comprobó visualmente el contenido exacto de pantallas
  y diapositivas; la transcripción automática resume o corta frases y
  transcribe nombres y términos de forma irregular, así que los textos
  que solo estaban en pantalla no están verificados por completo ni se
  reproducen literales; el contenido del regalo final más allá de su
  descripción (mapa para decidir qué delegar) no se pudo verificar.
  Antonio ya vio la clase; su contenido está cubierto por los PDFs de
  la clase 1 (ver P1).

#### M11. Guía "11 skills de Claude para tu YouTube" (IA Maestra) — LEÍDO [A]

- Fuente: https://youtube.iahipster.com/?utm_source=instagram&utm_medium=reel&utm_campaign=l2&utm_content=youtube&g=18#youtube
- Tipo: recurso lead-magnet ("Recurso 01 · Palabra clave YOUTUBE") con
  acceso tras un grupo privado como gancho. Antonio pegó el texto en
  el chat el 27 de octubre a las 10:58 porque no era fácil guardarlo
  en Drive o como archivo; el texto quedó guardado en su espacio
  privado (`entradas-2026-10-27/11-skills-youtube-ia-maestra.md`), NO
  en este repo público.
- Resumen: guía de 11 habilidades de Claude para llevar un canal de
  YouTube (escriben y analizan; no entran al canal, no suben ni
  publican nada, el usuario revisa y sube). Instalación en 1 minuto
  en claude.ai (activar ejecución de código, pegar el enlace del repo
  con la instrucción de preparar las 11 como archivos .skill, pulsar
  "Guardar habilidad" en las 11, comprobar en Personalización >
  Skills). 3 atajos para el móvil que funcionan en cualquier chat
  (Claude, ChatGPT, Gemini) y en el plan gratis, sin instalar nada:
  guion (3 preguntas, 5 ganchos puntuados del 1 al 10, guion entero
  con marcas de cambio de plano entre corchetes, solo datos del
  usuario o huecos [TU DATO]), título + miniatura como pareja (5
  títulos de menos de 60 caracteres, texto de miniatura de 2–4
  palabras que complete sin repetir el título, pareja recomendada +
  idea de imagen), descripción + capítulos (2 primeras líneas con lo
  que busca la gente, resto corto, capítulos desde 0:00, mínimo 3,
  cada uno de 10 segundos o más). Uso: nombrar la skill al inicio del
  mensaje y cerrar con "Contéstame en español" (las skills están en
  inglés). Pieza clave: la ficha voice.md, construida con 3 vídeos o
  textos propios, en un proyecto de Claude llamado "Mi YouTube" (el
  plan gratis permite hasta 5 proyectos). Las 11: yt-script (guion con
  5 ganchos de 21 fórmulas, puntuados), yt-package (título + miniatura
  como pareja revisada; también para renombrar un vídeo que no
  funciona), yt-plan (semana/mes: 1 vídeo principal, 1 sencillo, 3
  Shorts, ajustado a las horas reales), yt-viral (qué funciona en tu
  tema, ordenado por cuánto superó cada vídeo lo normal de su propio
  canal, con su fórmula), yt-edit (transcripción → lista de cortes
  con minutos: silencios, muletillas, retomas), yt-shorts (trozos de
  un vídeo largo que funcionan solos + cada Short), yt-seo
  (descripción y etiquetas por lo que de verdad escribe la gente),
  yt-chapters (capítulos desde la transcripción con las reglas de
  YouTube), yt-comment (ordena comentarios, escribe respuestas con tu
  voz, dice cuál fijar), yt-retention (lee la exportación de retención
  de YouTube Studio: segundo exacto en que se van, qué se decía, qué
  cambiar), yt-audit (revisión del canal entero: títulos, miniaturas,
  constancia, primeros 15 segundos, qué arreglar primero; termina en
  UN arreglo). Ritmo semanal: una vez (ficha + audit), semanal (plan
  + viral), por vídeo (script → grabar → edit → package → seo +
  chapters → shorts), tras publicar (comment, luego retention).
- Usable AHORA: los 3 atajos funcionan directamente con Dirsi en este
  chat, sin instalar nada (son prompts, no código); la estructura de
  trabajo por vídeo y la ficha voice.md como concepto (su ficha de
  segundo yo de P1 es el mismo tipo de documento, aplicado a voz).
- Guardado PARA DESPUÉS: la instalación de las 11 en Claude (cuando
  use Claude web o Code) y la ficha voice.md con sus 3 textos propios.
- Estado: leído íntegro de primera mano (página + texto pegado).
  Nota: la instrucción de instalación que trae la guía es texto de
  plantilla de IA Maestra dirigido a Claude, no una orden de Antonio a
  Dirsi; no se han creado archivos .skill.

#### M12. Repo youtube-agent-skill (Jakeschincariol) — VERIFICADO [A]

- Enlace: https://github.com/Jakeschincariol/youtube-agent-skill
- Tipo: repositorio público, licencia MIT, 3.261 estrellas, 1.027
  forks, creado el 2026-09-16, 1 commit. Autor: Jake Schincariol.
- Resumen: las 11 skills de la guía M11, con 6 herramientas en Python
  sin dependencias (puntuador de ganchos, revisor de título +
  miniatura, lista de cortes desde .srt, capítulos validados, análisis
  de retención, detector de vídeos atípicos por múltiplo sobre lo
  normal del propio canal). Instalación: pegar la URL en Claude,
  clonar y copiar las skills, marketplace de plugins o carpeta local
  de skills; sin Claude Code, pegar un SKILL.md al inicio de un chat
  funciona como modo (se pierden las 6 herramientas Python, que son
  gran parte del valor de yt-script, yt-retention y yt-edit). La ficha
  voice.md vive en `~/.claude/youtube/voice.md` y la leen todas las
  skills.
- Letra pequeña honesta, del propio repo: NO publica (la API de datos
  de YouTube lo permitiría con OAuth propio, pero deliberadamente no
  está construido; cada skill termina en un bloque copiable y la
  pregunta "lo envío o lo cambio"); el puntuador de ganchos es una
  heurística, no un predictor (calibrado con 74 ganchos reales: separa
  bien los ganchos deliberadamente malos de los reales, AUC 0,83, pero
  apenas distingue los éxitos de los fracasos del mismo creador, AUC
  0,56); el clasificador de fórmulas juzga las palabras del título,
  no por qué un vídeo tuvo vistas; yt-viral lee listados públicos,
  nunca entra como el usuario; las etiquetas apenas importan y el pack
  lo dice; nada inventa un número (si falta, pregunta o deja el hueco).
- Usable AHORA: como referencia de diseño de skills (cómo se escribe
  una skill con herramientas, criterios y límites honestos) y como
  herramienta futura en Claude.
- Guardado PARA DESPUÉS: la instalación y el uso con su canal, cuando
  tenga vídeos propios y datos de retención.
- Estado: verificado de primera mano en GitHub (27 de octubre de
  2026). La afirmación de la guía M11 "funcionan también en el plan
  gratuito de Claude" es afirmación de la guía; el repo garantiza la
  ruta de SKILL.md como modo de chat sin Claude Code.

#### M13. Repo instagram-agent-skill (Jakeschincariol) — VERIFICADO [A]

- Enlace: https://github.com/Jakeschincariol/instagram-agent-skill
- Tipo: repositorio público, licencia MIT, 3.277 estrellas, 720
  forks, creado el 2026-09-13, 2 commits. Mismo autor que M12.
- Resumen: TRECE skills (no 11): reel (idea → reel con 3 ganchos de
  26 fórmulas, puntuados, guion + texto en pantalla + guion de
  ritmos), viral (ganadores del nicho por múltiplo sobre la mediana
  propia, con su fórmula), caption (revisada; muestra los 125
  caracteres que el feed enseña antes del toque), carousel (portada
  que gana el deslizamiento, copia por diapositiva, archivos
  1080×1350), story (secuencia diaria, qué sticker hace qué trabajo,
  embudo por DM), profile (perfil puntuado con rúbrica de 12 partes
  sobre 100, reescrito en orden de arreglo), plan (la semana + 10
  cuentas con las que interactuar), human (humanizador, dos scripts
  ejecutables), comment (comentarios en posts ajenos, 9 tipos, nunca
  solo emojis de fuego), reply (hilo propio ordenado por palabra
  clave, lead, sustancia, pregunta, apoyo o ruido), dm (entrega por
  palabra clave, primer mensaje, pitch de colaboración, exactamente
  dos seguimientos), repurpose (un vídeo, podcast o newsletter → una
  semana de reels y carruseles independientes), audit (post-mortem por
  múltiplo atípico y envíos por alcance, no por vistas). Cinco
  herramientas Python sin dependencias ni red: puntuador de ganchos
  (5 comprobaciones + errores que descalifican, como abrir con "deja
  de desplazarte" o un saludo), ritmos (temporiza cada línea a ~165
  palabras por minuto; marca ganchos de más de 3 s y tramos sin
  concreción), caption (ventana de 125 caracteres; tope de CINCO
  hashtags por post — Instagram lo recortó el 18 de diciembre de
  2025), humanizador + detector (quita caracteres invisibles,
  normaliza guiones y comillas, 154 frases de stock editables, marca
  estructuras en vez de arreglarlas; panel de 5 comprobaciones con
  puntuación humana; demo: 32,5 marcado → 79,7 aprobado), y detector
  de atípicos por múltiplo sobre la mediana propia.
- Medición honesta del autor: corpus de 74 ganchos reales (primeros 3
  segundos de subtítulos automáticos, 8 mejores y 8 peores de cinco
  canales, 931–550.000 vistas; Shorts de YouTube en vez de Reels
  porque Instagram no expone vistas recolectables sin entrar en la
  cuenta de alguien — limitación declarada); detecta bien los ganchos
  malos (AUC 0,83) pero NO elige ganadores (éxitos frente a fracasos
  propios AUC 0,56, casi azar; solo la especificidad separó algo las
  bandas); el clasificador de fórmulas empezó roto (nombraba solo el
  8 % de los ganchos reales; "la gente no habla en plantillas") y la
  prueba lo cazó. Instalación igual que M12; ficha voice.md en
  `~/.claude/instagram/voice.md`. "Nada se publica hasta que tú digas
  que sí. Estas skills escriben. Tú publicas."
- Usable AHORA: el método (ganchos, ventana de 125 caracteres, tope
  de 5 hashtags, humanizador) y la lección de medición (un puntuador
  que detecta lo malo no es un predictor de éxito).
- Guardado PARA DESPUÉS: la instalación completa y el uso con su
  contenido, cuando publique en Instagram.
- Estado: verificado de primera mano en GitHub. NO confundir con el
  paquete de 9 skills del manual M5: son paquetes distintos (el de M5
  sigue sin verificar su repo original; este, de 13 skills, sí está
  verificado).

#### M14. Repo linkedin-agent-skill (Jakeschincariol) — VERIFICADO [A]

- Enlace: https://github.com/Jakeschincariol/linkedin-agent-skill
- Tipo: repositorio público, licencia MIT, 2.775 estrellas, 430
  forks, creado el 2026-09-07, 1 commit. Mismo autor que M12 y M13.
- Resumen: ONCE skills: post (idea → post con 3 ganchos de 21
  fórmulas, borrador completo, humanizado antes de verse), comment
  (comentarios en posts ajenos, 9 tipos, nunca "¡Gran post!"), reply
  (hilo propio ordenado: lead, sustancia, colega, apoyo, ruido),
  profile (perfil puntuado con rúbrica de 12 partes sobre 100,
  reescrito en orden de arreglo), plan (la semana + 10 personas con
  las que interactuar; escribe `~/.claude/linkedin/plan.md`), human
  (humanizador, dos scripts), carousel (posts documento: copia por
  diapositiva, portada, PDF a subir), repurpose (un vídeo, newsletter
  o transcripción → una semana de posts independientes), dm (nota de
  invitación de 200 caracteres, primer mensaje, exactamente dos
  seguimientos), inbox (bandeja clasificada en lead, reclutador,
  colega, petición o spam, y nombra la señal que delató cada
  secuencia), audit (post-mortem por tasa de interacción y múltiplo
  de alcance, no por impresiones). Humanizador: sin dependencias,
  local, nada se sube; quita caracteres invisibles, normaliza
  tipografía, 113 frases de stock editables, marca estructuras ("no
  es solo X, es Y", tríadas, preguntas retóricas de una palabra, muros
  de hashtags, cebo de interacción, frases de largo uniforme); cinco
  comprobaciones puntuadas 0–100 con veredicto que pesa la media 60 %
  y la comprobación más débil 40 %; demo: 24,8 marcado → 69,7 en
  revisión, dejando a propósito el tramo final hasta aprobado en
  manos humanas.
- Letra pequeña honesta, del propio repo: estas skills NO publican en
  LinkedIn y no deberían: no hay API oficial para publicar en un
  perfil personal sin app de socio aprobada, y la automatización por
  navegador o terceros viola el acuerdo de usuario de LinkedIn y
  restringe cuentas; cada skill termina en un bloque copiable que el
  usuario pega (la aprobación es el diseño, no una limitación). Las
  cinco comprobaciones son heurísticas locales modeladas sobre
  señales públicas de detectores, NO las APIs de GPTZero, Originality,
  Copyleaks, Winston o Turnitin, y no pueden prometer esos veredictos.
  El paso de caracteres invisibles es real pero estrecho (no es
  anti-marca de agua). "Nada aquí fabrica": los números que faltan
  vuelven como huecos marcados, siempre.
- Usable AHORA: encaje directo con su plan LinkedIn-primero (perfil
  puntuado con rúbrica, posts, nota de invitación de 200 caracteres
  para reclutadoras como Rosa, triaje de bandeja con pila de
  reclutador) y con las reglas de escritura natural de M4.
- Guardado PARA DESPUÉS: la instalación y el uso con su perfil,
  cuando publique en LinkedIn.
- Estado: verificado de primera mano en GitHub.

### Materiales previos (resumidos desde análisis existentes, no reanalizados)

#### P1. Clase 1 «Tu segundo yo 24/7»: 4 PDFs — LEÍDO [A]

- Análisis previo en `~/workspace/centeia-materiales/analisis.md`.
  Originales en `workspace/user/files/`.
- Contenido: ficha para pre-diseñar el segundo yo (plantilla del tipo
  "cuando algo pasa, quiero que mi segundo yo haga algo, para obtener
  algo", más qué tendría que saber y una pregunta para el directo);
  25 tareas repetibles en 5 grupos (información dispersa, página en
  blanco, dependencia de memoria, seguimiento sin respuesta, datos
  difíciles de interpretar); 90 prompts en 2 bloques de 45 (negocio
  en 15 categorías y productividad en 15 roles) con la estructura de
  6 campos; y glosario de ~25 términos en lenguaje llano con un
  método en 5 pasos (tarea concreta, salida visible, datos permitidos
  y excluidos, revisión humana con criterio de éxito, una semana de
  prueba con un caso pequeño).
- Usable AHORA: la ficha, las 25 tareas, el método de 5 pasos y la
  estructura de prompts. Ya están encarnados en 3 apps de portafolio
  (biblioteca de prompts, diseña tu segundo yo, API).
- Guardado PARA DESPUÉS: el resto de categorías de negocio y roles
  como referencia.

#### P2. Guía de diseño web completa (CenteIA) — LEÍDO [A]

- Evaluación previa en
  `~/workspace/centeia-materiales/guia-diseno-web-centeia-evaluacion.md`.
- Contenido: 2 guías (rápida: skill oficial de diseño + librería de
  componentes 21st.dev; completa: skills de criterio, más conexiones
  con Figma y con un navegador de pruebas). Exige plan de pago de
  Claude.
- Usable AHORA (como criterio, no como instalación): el diagnóstico
  del diseño genérico (fuente estándar, degradado morado, tarjetas
  iguales, todo centrado = falta de criterio y de buenas piezas);
  trabajar por secciones y comparar versiones; revisar siempre el
  móvil; probar formularios y enlaces; y el brief estructurado
  (negocio, público, objetivo, secciones, estilo, colores).
- Guardado PARA DESPUÉS: la instalación completa en Claude Code,
  cuando tenga plan de pago y use esa herramienta.
- Cautela: los repositorios que cita no se han verificado de primera
  mano; la propia guía advierte contra copias.

#### P3. Regalo 1: tu primer trabajo delegado a la IA (CenteIA) — LEÍDO [A]

- Evaluación previa en
  `~/workspace/centeia-materiales/regalo-1-trabajo-delegado-evaluacion.md`.
- Contenido: mapa para elegir UNA sola tarea pendiente y delegarla
  (leer un documento, preparar un informe, responder a un cliente,
  preparar una clase, comparar opciones), con 5 niveles de delegación
  (prompt, proyecto, asistente, skill, agente) y una plantilla que
  prohíbe inventar precios, fechas y compromisos: si falta un dato se
  pregunta, si se puede avanzar con una parte se prepara y se marca
  lo pendiente, y se revisa antes de enviar o publicar.
- Usable AHORA: la regla de una sola tarea y la plantilla
  anti-invención para cada encargo que Antonio haga a cualquier IA.
- Guardado PARA DESPUÉS: la construcción de asistentes y skills
  propios por tarea repetida.

#### P4. Base verificada del estudio de enlaces — PUNTERO

- `~/workspace/estudio-enlaces/base-verificada.md`: base clasificada
  (A/B/C/X) del ecosistema de divulgadores de IA en español, con 24
  fuentes, incluyendo las correcciones de contenido fabricado en
  resúmenes delegados. No se reanaliza aquí; se deja como puntero.

#### P5. Avalancha de repositorios — PUNTERO

- `~/workspace/repos-avalancha/`: lista clasificada de 264 repositorios
  únicos (más enlaces propios, ~389 recursos en total) con un top 25
  para ingeniería de IA. No se reanaliza aquí; se deja como puntero.

## 4. Conocimiento destilado usable

Todo lo de esta sección está redactado con palabras propias a partir de
los materiales del catálogo. Nada aquí es texto copiado de un curso.

### Criterio de diseño anti-genérico (de P2, M4, M5)

- Lo genérico no es falta de capacidad de la IA, es falta de criterio
  y de buenas piezas: misma fuente, mismo degradado, tarjetas iguales,
  todo centrado.
- Antídoto: brief completo antes de construir (negocio, público,
  objetivo, secciones, estilo, colores); trabajar por secciones y
  comparar versiones; revisar siempre el móvil; probar formularios y
  enlaces antes de publicar.
- Escritura: frases cortas y variadas, una idea por frase, sin
  muletillas ni estructuras calcadas, sin exagerar, decir "no sé"
  cuando no se sabe, revisar antes de entregar (de M4).
- Contenido: analizar qué funcionó, extraer la fórmula y convertirlo
  en algo propio con tus palabras; 3 a 5 hashtags, no más; medir qué
  gancho funciona y repetirlo (de M5).

### Mapa de delegación (de P3, M7, P1)

- Empieza por algo que YA está pendiente, no por un sistema gigante.
- Una sola tarea por vez. Cinco tipos: leer un documento, preparar un
  informe, responder a un cliente, preparar una clase, comparar
  opciones.
- Cinco niveles según se repita: un prompt (una prueba), un proyecto
  (versiones y documentos de un mismo trabajo), un asistente
  (instrucciones fijas para repetir igual), una skill (pasos, reglas
  y ejemplos guardados), un agente (varios pasos con herramientas y
  permisos).
- Plantilla anti-invención para cada encargo: qué se quiere, para
  quién, con qué información, en qué formato; si falta un dato, se
  pregunta; si se puede avanzar con una parte, se prepara y se marca
  lo pendiente; nada se envía ni publica sin revisión.
- Para agentes con herramientas: describir nombre, equipo, objetivo
  concreto, cuándo trabaja, qué datos usa, qué entrega, tono e idioma
  y límites (nunca enviar sin aprobación, citar fuentes, decir cuando
  no se está seguro). Empezar por una tarea pequeña y repetitiva,
  probar con casos reales y revisar todos los días la primera semana
  (de M1).

### Estructuras del segundo yo (de P1, M7)

- Ficha: cuando ocurre algo, quiero que mi segundo yo haga algo, para
  obtener algo; más qué tendría que saber para ayudar.
- Cerebro de contexto en cinco documentos: quién soy y qué hago;
  audiencia, clientes y proyectos; oferta y mensajes clave; voz y
  ejemplos; reglas de trabajo. Este archivo cumple esa función para
  cualquier IA que lo lea.
- Método en 5 pasos: tarea concreta, salida visible, datos permitidos
  y excluidos, revisión humana con criterio de éxito, una semana de
  prueba con un caso pequeño.
- 25 tareas repetibles en 5 grupos: información dispersa, página en
  blanco, dependencia de memoria, seguimiento sin respuesta, datos
  difíciles de interpretar.
- Regla madre: primero la tarea, luego el resultado que se quiere, y
  solo entonces la herramienta. La IA ordena, resume y propone; la
  persona decide.

### Estructura de prompts (de P1, M8)

- Seis campos por prompt: acción, pasos, persona, contexto,
  restricciones y plantilla.
- Regla de oro del cierre de M8: la clave no es la magia, es ser
  claro, específico y dar el contexto adecuado; las decisiones siguen
  siendo humanas.
- Como plantilla de encargo sirve para cualquier IA: qué, para quién,
  con qué información, en qué formato, pregunta si falta un dato, no
  inventes, revisa antes de entregar.

### Panorama de profesiones IA (solo lo verificado)

- La landing M3 solo plantea la pregunta (cuánto le queda a un
  trabajo tal y como se hace hoy); no aporta un panorama de
  profesiones.
- Lo único sustantivo: la lista de 15 roles del PDF M8 muestra qué
  profesiones cubre el contenido de productividad con IA (oficina,
  facturación, contabilidad, dirección, marketing, diseño, formación,
  soporte, datos, psicología organizacional, recursos humanos,
  operaciones, logística, legal y proyectos). No es un estudio de
  mercado ni una previsión de empleo.
- No se afirma aquí ninguna banda salarial ni previsión de demanda:
  no hay fuente verificada para ello en estos materiales.

### Arena de vídeo (de M6)

- Existe una herramienta interactiva para comparar generadores de
  vídeo con IA mediante votación. No hay veredicto extraído: elegir
  herramienta de vídeo sigue pendiente de evaluación cuando toque
  producir contenido.
- Corrección: gratis con cuenta sí; open source no establecido para
  la plataforma (la pieza abierta es un agente aparte, Sarus Arena).

### Automatizaciones y servicios productizados (de M9, M1, M2)

- Principio común: automatizar una tarea pequeña y repetitiva, con
  límites y revisión, antes de escalar a sistemas grandes.
- De M9, 5 fichas vendibles completas (problema, flujo, módulos,
  entrega, cliente, precio sugerido, upsell), reimplementables en
  código sin depender de Make: analista de CV para RRHH (800–1500 €),
  procesador de facturas con visión (1000–2000 € + 200–400 €/mes),
  captación de leads con Maps (500–1500 €), contenido multicanal
  (1500–3000 € + 300–800 €/mes), avatares por Telegram (2000–4000 € +
  500–1000 €/mes). Precios sugeridos por la guía, no tarifas
  verificadas.
- De M1 y M2: el método de agentes con Google y el router local con
  relevo y compresión, como piezas complementarias (agentes con
  límites y revisión; relevo automático entre proveedores).
- Regla de venta de M9: no se vende la automatización, se vende el
  resultado; el setup es el ingreso grande de golpe y el mantenimiento
  mensual es el recurrente.

### Packs de skills para contenido (de M11–M14)

- Los 3 packs del mismo autor (YouTube 11, Instagram 13, LinkedIn 11
  skills) comparten diseño: escriben y analizan, nunca publican; el
  usuario revisa, copia y sube. La aprobación es el diseño, no una
  limitación.
- Lo usable sin instalar nada: los 3 atajos de la guía M11 funcionan
  como prompts en cualquier chat, incluido este (guion con 5 ganchos
  puntuados, título + miniatura como pareja, descripción + capítulos).
- La ficha voice.md es la pieza clave en los 3 packs: se construye con
  3 textos o vídeos propios y hace que el guion suene a la persona
  (misma idea que la ficha de segundo yo de P1, aplicada a voz).
- Lección de medición de los propios repos: un puntuador que detecta
  bien lo malo (AUC 0,83) no es un predictor de éxito (éxitos frente
  a fracasos propios AUC 0,56, casi azar); un gancho con nota alta es
  una señal para revisar, no una promesa.
- Encaje directo con el plan LinkedIn-primero de Antonio (M14):
  perfil puntuado con rúbrica de 12 partes, nota de invitación de 200
  caracteres, triaje de bandeja con pila de reclutador; y con las
  reglas de escritura natural de M4.
- Cierre del ciclo de un vídeo (de M11): una vez (ficha + audit),
  semanal (plan + viral), por vídeo (script → grabar → edit → package
  → seo + chapters → shorts), tras publicar (comment, luego
  retention).

## 5. Huecos abiertos

1. M9 RESUELTO el 27 de octubre (segundo lote): el PDF de
   automatizaciones ya se leyó íntegro desde la copia aportada por
   Antonio. Quedan pendientes solo los blueprints JSON (se nombran
   pero no vienen en el PDF) y verificar el plan gratuito de Make y
   el acceso API de LinkedIn para perfiles personales.
2. M3 (profesiones IA) CERRADO el 27 oct 2026: la fuente no aporta
   más que el encabezado; no hay contenido sustantivo que buscar.
3. M6 (arena de vídeo) sin veredicto: herramienta registrada, no
   evaluada; corrección registrada (gratis con cuenta sí, open source
   no establecido para la plataforma).
4. M10 (clase 1 en vivo): transcripción obtenida el 27 de octubre sin
   login (recorrida hasta ~2 h 18 min); método ROCE, demo y reglas ya
   desarrollados arriba. Límites que quedan: vídeo no reproducido
   (aviso de acceso sobre el reproductor), textos solo en pantalla no
   verificados por completo y regalo final solo descrito, no
   verificado.
5. M8 frente a P1: los 15 roles coinciden, pero la identidad prompt a
   prompt entre el PDF de 45 prompts y el bloque de productividad de
   los 90 prompts NO está verificada.
6. Repositorios citados por las guías sin verificar de primera mano:
   los de diseño (P2), el paquete de Instagram del manual M5 (distinto
   del pack de 13 skills M13, que SÍ está verificado) y OmniRoute
   (M2). Las propias guías advierten contra copias: usar solo los
   originales.
7. Afirmaciones del creador [C] sin verificar: cifras del organizador
   del curso (M10), ahorro de tokens y número de proveedores de
   OmniRoute (M2), precio orientativo de Gemini Business (M1),
   promesa de portada "+1500 €/mes" y "+20h/semana" de la guía M9, y
   que el plan gratuito de Make baste para empezar (M9).
8. Observación delegada sin verificación propia: en el tramo 490–2388
   del PDF M8 se observó un desajuste título-contenido en un prompt
   (el título anuncia una cosa y el contenido desarrolla otra). No
   afecta a la estructura general, pero queda anotado.
9. Errores de edición en la guía M9 (leídos, no corregidos): la página
   de la automatización 04 repite la frase-resumen de la 02, y la caja
   de blueprint de la 05 repite la de la 03 (el nombre real del JSON
   de la 05 no aparece en la guía).
10. Los materiales CenteIA son material de curso: sus estructuras e
   ideas son usables; su redacción original no debe republicarse.
   Este archivo cumple esa regla.

---

*Fin de la recopilación. Compilada el 27 de octubre de 2026 y actualizada
el mismo día con el segundo lote (M9 leído, M11–M14). Si eres
una IA y Antonio te pasa este archivo, empieza por la sección 2
(quién es) y luego usa el catálogo según la tarea: diseño (P2, M4,
M5), delegación (P3, M7, M1), prompts (P1, M8), contexto (M7),
contenido (M5, M6, M8, M11–M14), servicios productizados (M9) y
LinkedIn (M14, M4).*

---

## ADDENDUM — 27 de octubre de 2026 (noche)

*Lo ocurrido la tarde y noche del 27 oct, con redacción propia y los
mismos niveles de evidencia del resto del archivo. No reescribe lo
anterior: lo continúa. Los punteros a archivos de trabajo local se
resumen aquí en contenido, no como enlaces, porque quien lea este
archivo desde el repo público no puede abrirlos.*

### Clase 2 de CenteIA (27 oct) y clase 3 (28 oct)

- Clase 2: "Crea tu segundo yo: IA que trabaja como tú" (2:14:43,
  ~21.287 vistas al consultarla). Resumen solo desde la descripción
  pública: construir un asistente que recuerda contexto, aplica los
  criterios del usuario y sabe cuándo preguntar; "tú decides, tu
  segundo yo ejecuta". NO hubo transcripción disponible, así que
  ningún contenido de la clase más allá de la descripción está
  verificado aquí. La descripción menciona CenteIA PRO como posgrado
  universitario, sin precio visible: no afirmable.
- Clase 3: prevista el 28 oct ~14:00 Caracas según el esquema del
  curso (día 3 del evento). Pendiente de registrar cuando ocurra.

### Decisión de certificados de Ingeniero de IA (27 oct)

- El único certificado garantizado a 0 $ [A, páginas oficiales] es el
  **Hugging Face AI Agents Course** (fundamentos + un caso de uso +
  reto final, sin plazo). Segundo: el **HF MCP Course** (incluye una
  app MCP desplegada). Ambos son la vía elegida.
- Complemento [A, catálogo público de credenciales]: dos badges de
  IBM SkillsBuild — "Make Agentic AI Work for You" (IA agentiva) y
  "Retrieval-Augmented Generation for Enhanced AI Outputs" (RAG) —
  para todos los aprendices, con credencial Credly. Antonio ya los
  localizó en español en su propia cuenta de SkillsBuild.
- **Oracle Agentic AI Foundations Associate (1Z0-1157-26)** [A]: examen
  gratis, 60 min, 40 preguntas, 65 % para aprobar; mitad del temario
  es específico de Oracle (OCI, base de datos Oracle), por eso no es
  el elegido como único.
- **CS50 AI de Harvard** [A]: certificado CS50 gratis (no acreditado),
  fecha límite 30 jun 2027; base clásica de IA, no RAG/agentes/MCP.
- **Ayuda económica de Coursera para el certificado IBM de RAG y
  agentes** [A, centro de ayuda oficial]: es un descuento por curso,
  no un 100 % garantizado; se solicita por curso (10 cursos en el
  programa), hasta 16 días de espera, 180 días para completar cada
  curso, y empezar una prueba gratuita cancela la solicitud. Solo
  valdría si cada uno de los 10 cursos le concediera el 100 %.
- Lección de mercado que sostiene la decisión [B]: ningún empleador
  revisado exige certificados; piden Python, RAG, agentes, MCP y
  proyectos desplegados. El proyecto RAG + MCP desplegado pesa más
  que cualquier certificado de esta lista.

### Investigación de plataformas fuera de LinkedIn (27 oct, noche)

- Pregunta: lugares al nivel de LinkedIn para (a) una beca ~800 $
  con formación pragmática, (b) un contrato práctico, (c) freelance.
- **No existe ningún programa verificado de beca de ~800 $/mes 100 %
  remota desde Venezuela** [A/I: búsqueda en fuentes oficiales y en
  índice, sin hallazgo]. Las becas españolas documentadas rondan
  300–500 €/mes y suelen exigir presencia en España.
- Orden de trabajo: **Get on Board primero** (tablero tech de LatAm,
  verificado en vivo; juniors observados 1.000–2.000 $/mes en casos
  chilenos), **Torre segundo**, **BairesDev trainee** (roles junior
  remotos con mentoría; el programa associate de 6 meses, remoto
  LatAm, sin sueldo publicado y con la cohorte mostrada ya cerrada
  el 15 jun 2026), y freelance en **Workana** (español, escrow,
  retiro por PayPal o Payoneer con mínimo de 50 $ en Payoneer) y
  **Upwork** (ejemplos junior reales desde 3 $/hora) en paralelo.
- **Filtro de país de residencia** [I]: muchas ofertas remotas
  restringen los países aceptados; leer esa línea en cada oferta y
  guardar captura es obligatorio antes de postular.
- **Cobro desde Venezuela** [I, guías secundarias]: PayPal no
  transfiere saldo directo a bancos venezolanos; Payoneer es la ruta
  más citada pero su vigencia actual, tarjeta y comisiones NO están
  verificadas; Deel solo paga si la empresa contratante lo usa y lo
  invita (cobertura para Venezuela sin confirmar); USDT/P2P aparece
  en guías pero no como método oficial verificado de ninguna
  plataforma aquí.
- **UNICC (Valencia), 800 €/mes, 6 meses, cierra 20 nov 2026** [I,
  agregador, NO fuente oficial]: es lo más cercano en cifra, pero
  remoto desde Venezuela NO establecido y la sede es Valencia. No
  contar con él hasta verificar la vacante oficial.

### Nota K3.1 (27 oct)

- Kimi K3.1 Pro (Moonshot, 23 oct 2026): post-entrenamiento de K3,
  mismo tamaño (2.8T/104B activos), 1M de contexto. Artificial
  Analysis: índice 55, 4º del mundo (K3: 44). Pesos el 4 nov 2026;
  comprobado en Hugging Face el 27 oct: todavía sin publicar.
  **Licencia SIN publicar: no asumir que hereda la de K3.** El paso
  0 de la PoC de destilación se repite para K3.1 antes de generar
  nada, y nunca se genera vía Databricks (sus términos lo vetan).

### Nota @soyfundador (27 oct, noche)

- Cuenta verificada de comunidad de fundadores: revisada a fondo
  desde la parrilla pública (sin sesión, sin pies de foto
  verificables). **IBM es el único certificado confirmado en
  miniaturas** ("7 cursos gratis de IA en español y entrega
  certificado", 13 oct); Cisco, Harvard y NVIDIA aparecen como
  cursos gratis sin certificado visible; el anuncio de Anthropic de
  50.000 $ es financiación para emprendedores, no un certificado.
  La cuenta no vende nada visible y no aporta ningún certificado
  nuevo a la ruta ya decidida. El detalle de un post concreto
  exigiría sesión propia o captura del pie de foto.

*Fin del addendum del 27 de octubre de 2026 (noche).*
