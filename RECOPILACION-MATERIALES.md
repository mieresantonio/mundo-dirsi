# Recopilación de materiales — Antonio

Compilado el 27 de octubre de 2026 a partir de 10 enlaces enviados por Antonio
el 27 de octubre de 2026 a las 02:49 (hora de Caracas), más los materiales
previos que ya estaban analizados. Redactado con palabras propias: este
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

### Hoy, 27 de octubre de 2026 (10 fuentes)

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

#### M3. Página CenteIA de profesiones IA — PARCIAL

- Enlace: https://training.centeia.com/profesiones-ia/?utm_term=01a179c7-8b7a-74ee-b1f7-8fd539b204f1&fbclid=PAT01DUAVM9RpleHRuA2FlbQIxMABwZG9mAnNydGMGYXBwX2lkDzU2NzA2NzM0MzM1MjQyNwABp2YzBl_wSWIin9p_BON5syvcNHQVvAH_TdR_XBcZCrqw80j5MJziZ1Cq7zHP_aem_MgJtZOYozHMnj_sRVJCD9w
- Tipo: página web (landing) de CenteIA.
- Resumen: solo se extrajo el encabezado. Es una landing de captación
  para un "Diagnóstico ocupacional" que plantea una pregunta: cuánto
  le queda a un trabajo tal y como se hace hoy. Muestra horarios por
  zona. No se extrajo contenido sustantivo.
- Usable AHORA: casi nada, salvo la pregunta que plantea, útil como
  reflexión para posicionamiento (qué partes de un trabajo resisten
  frente a la IA y cuáles no).
- Guardado PARA DESPUÉS: revisitar si el contenido completo se hace
  accesible; al ser una landing de captación, probablemente pida
  registro.
- Estado: parcial, solo encabezado. No se inventa contenido.

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

#### M6. Arena de vídeo (arena.ai) — PARCIAL

- Enlace: https://arena.ai/video?utm_term=01a179c7-8b7a-74ee-b1f7-8fd539b204f1
- Tipo: herramienta web interactiva ("Video Arena: compara los mejores
  generadores de vídeo con IA"), de votación y comparación.
- Resumen: es una herramienta, no un artículo. Permite comparar
  generadores de vídeo con IA mediante votación. No se extrajo un
  veredicto ni un ranking aprovechable.
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

#### M9. 5 Automatizaciones y Agentes de IA (CenteIA) — NO LEGIBLE

- Enlace: https://training.centeia.com/wp-content/uploads/2026/07/5-Automatizaciones-y-Agentes-de-IA_compressed.pdf
- Tipo: PDF de CenteIA, julio de 2026 (según la ruta del enlace).
- Resumen: ninguno. El enlace redirige a una zona de miembros
  ("Accede a Círculo CenteIA aquí") con 0 líneas de contenido.
- Usable AHORA: nada.
- Guardado PARA DESPUÉS: todo, si Antonio aporta el archivo desde su
  acceso de miembro y se analiza entonces.
- Estado: no legible, tras muro de miembros del Círculo CenteIA. No
  se intentaron más vías. No confundir con M1 (la guía de agentes con
  Google), que sí es legible: son archivos distintos.

#### M10. Clase 1 en vivo "Tu segundo yo 24/7" (YouTube) — PARCIAL

- Enlace: https://www.youtube.com/live/we3gUsC7_80?si=Fk2kmbZAn_ePv48-
- Tipo: vídeo en directo de YouTube, primera clase del curso CenteIA.
- Resumen: descripción verificada: presenta el método ROCE, con Jordi
  Segura y Armand Pujadó, y cifras del organizador (más de un millón
  de personas aprendiendo y más de 5.000 en su programa PRO, ambas
  [C]). No hay transcripción extraíble por texto.
- Usable AHORA: el nombre del método (ROCE) como referencia; su
  contenido concreto NO está verificado más allá de la descripción,
  así que no se desarrolla aquí.
- Guardado PARA DESPUÉS: revisión cuando lleguen las clases 2 y 3.
- Estado: parcial (descripción verificada, sin transcripción).
  Antonio ya vio la clase; su contenido está cubierto por los PDFs de
  la clase 1 (ver P1).

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

### Automatizaciones (solo lo verificado)

- Verificado y legible: el método de agentes con Google (M1) y el
  router local con relevo y compresión (M2).
- NO verificado: el contenido del PDF M9 (tras muro de miembros).
- Principio común de ambos materiales legibles: automatizar una tarea
  pequeña y repetitiva, con límites y revisión, antes de escalar a
  sistemas grandes.

## 5. Huecos abiertos

1. M9 (5 automatizaciones y agentes) no legible: tras muro de
   miembros del Círculo CenteIA. Solo se podrá analizar si Antonio
   aporta el archivo desde su acceso.
2. M3 (profesiones IA) solo encabezado: sin contenido sustantivo.
3. M6 (arena de vídeo) sin veredicto: herramienta registrada, no
   evaluada.
4. M10 (clase 1 en vivo) sin transcripción: el método ROCE solo está
   nombrado, no desarrollado ni verificado.
5. M8 frente a P1: los 15 roles coinciden, pero la identidad prompt a
   prompt entre el PDF de 45 prompts y el bloque de productividad de
   los 90 prompts NO está verificada.
6. Repositorios citados por las guías sin verificar de primera mano:
   los de diseño (P2), el paquete de Instagram (M5) y OmniRoute (M2).
   Las propias guías advierten contra copias: usar solo los
   originales.
7. Afirmaciones del creador [C] sin verificar: cifras del organizador
   del curso (M10), ahorro de tokens y número de proveedores de
   OmniRoute (M2), precio orientativo de Gemini Business (M1).
8. Observación delegada sin verificación propia: en el tramo 490–2388
   del PDF M8 se observó un desajuste título-contenido en un prompt
   (el título anuncia una cosa y el contenido desarrolla otra). No
   afecta a la estructura general, pero queda anotado.
9. Los materiales CenteIA son material de curso: sus estructuras e
   ideas son usables; su redacción original no debe republicarse.
   Este archivo cumple esa regla.

---

*Fin de la recopilación. Compilada el 27 de octubre de 2026. Si eres
una IA y Antonio te pasa este archivo, empieza por la sección 2
(quién es) y luego usa el catálogo según la tarea: diseño (P2, M4,
M5), delegación (P3, M7, M1), prompts (P1, M8), contexto (M7) y
contenido (M5, M6, M8).*
