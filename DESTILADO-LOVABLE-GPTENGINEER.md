# Destilado: Lovable y su ancestro abierto, gpt-engineer

Investigación y destilación de Dirsi, 9 nov 2026, a petición de Antonio
(eligió solo el documento, sin fork). Todo lo afirmado sobre el repo se
leyó de primera mano (API de GitHub + clon completo leído en local);
lo de la plataforma, de su documentación oficial pública. Redacción
propia; el repo es MIT (© sus autores), y aquí se destila su método,
no se republica su código.

## 1. Las dos cosas que hay que no confundir

- **gpt-engineer** (github.com/AntonOsika/gpt-engineer): CLI de código
  abierto, MIT, 54.965 estrellas, 7.265 forks. La propia descripción del
  repo lo declara «precursor de lovable.dev». Está ARCHIVADO (solo
  lectura; último push 14 may 2025) y su README redirige: quien busque
  el servicio gestionado, a Lovable; quien busque un CLI mantenido, a
  aider. Tamaño real: 182 archivos, 11.452 líneas de Python.
- **Lovable** (lovable.dev): la plataforma comercial actual. Código
  CERRADO: no hay repo público de la plataforma, ni de sus prompts
  internos, ni de su orquestación de agentes. Lo público es su
  documentación (docs.lovable.dev), su biblioteca de prompts y el
  comportamiento observable del producto.

Conclusión de alcance: el ancestro se destila COMPLETO (es finito y
está abierto); de la plataforma solo se destila su capa pública. Quien
prometa «el sistema interno de Lovable» está vendiendo humo.

## 2. El pipeline de gpt-engineer (cómo trabaja, paso a paso)

El agente (`SimpleAgent`) tiene cuatro piezas: el modelo, una memoria
en disco (todo queda registrado en archivos de log), un entorno de
ejecución en disco, y el portador de «preprompts» — textos fijos que se
anteponen a cada tarea. El flujo de generación (`steps.py`):

1. **Aclarar antes de generar.** Un primer paso examina las
   instrucciones y decide si algo necesita aclaración; puede asumir lo
   razonable, pero si duda, formula UNA sola pregunta. Si no, declara
   que no hay nada que aclarar y sigue.
2. **Generar con contrato de formato.** El prompt de sistema combina la
   filosofía (§3) con un formato de salida estricto (§4). El modelo
   primero enumera las clases/funciones núcleo con su propósito, y
   después emite los archivos empezando por el punto de entrada y
   siguiendo por lo que este importa.
3. **Convertir la conversación en archivos.** Un parser
   (`chat_to_files.py`) extrae de la respuesta los bloques
   «nombre-de-archivo + código» y los materializa en disco. Nada de
   código «en el aire»: todo lo generado aterriza en archivos.
4. **Generar el punto de entrada y ejecutarlo.** Otro paso produce el
   script que corre el proyecto (comandos de terminal, sin instalaciones
   globales ni sudo, sin placeholders) y el entorno lo ejecuta: el
   resultado no es «código que parece funcionar», es código corrido.
5. **Mejorar con diffs y rescate de fragmentos.** El modo mejora trabaja
   en formato diff unificado. Cada diff se valida contra el código real:
   los fragmentos correctos se aplican («salvage»), los erróneos se
   devuelven al modelo con el detalle del error, solo para reescribir
   los problemáticos, con un máximo de reintentos. El error alimenta la
   siguiente pasada; no se regenera todo.

Memoria: cada paso deja log en disco (generación, diffs, errores), de
modo que la sesión es auditable después — el mismo principio que el
sistema de Dirsi aplica con sus archivos.

## 3. La «mente»: los 9 preprompts (136 líneas en total)

Destilados, uno por uno:

- **philosophy** — las reglas de casa del código: una clase por archivo;
  el lenguaje que pidió el usuario; siempre el manifiesto de
  dependencias del ecosistema (requirements.txt, package.json);
  comentario breve de propósito en cada función; comentarios en la
  lógica compleja; estructura de carpetas según las buenas prácticas
  del lenguaje. Preferencias declaradas en Python: pytest y dataclasses.
- **clarify** — el paso 1 del pipeline: no ejecutar, solo juzgar si
  falta algo; asumir lo razonable; como máximo una pregunta.
- **generate** — razonar paso a paso; esqueleto primero (nombres y
  propósito de cada pieza), código después; orden de emisión desde el
  punto de entrada; código COMPLETO y funcional, sin placeholders; si
  se duda en una pieza, escribir una implementación plausible antes que
  dejar un hueco; antes de terminar, comprobar que toda la arquitectura
  está presente en los archivos; cerrar con una frase fija de fin
  («esto concluye una implementación totalmente funcional») que actúa
  como señal de completitud verificable.
- **file_format** — el contrato de salida: cada archivo como
  ruta-en-minúsculas + bloque de código, sin comentar qué hace cada
  archivo. Es lo que permite que el parser del paso 3 sea simple y
  fiable: el formato es parte del diseño, no un adorno.
- **file_format_diff / file_format_fix** — la variante para cambios:
  diff unificado estándar de git, con ejemplos de modificar y de crear
  archivos; y las reglas para corregir diffs que no aplicaron.
- **entrypoint** — el paso 4: responder solo con los comandos, sin
  explicar el código, sin sudo, sin instalaciones globales, con valores
  de ejemplo reales en vez de marcadores.
- **improve** — generate, pero sobre código existente y en diffs:
  mismas exigencias de completitud y compatibilidad entre archivos.
- **roadmap** — la variante de respuesta larga: asegurar que cada
  detalle de la arquitectura termine implementado como código.

Lo notable: no hay «magia». La ventaja del sistema no es un prompt
secreto brillante, es la DISCIPLINA del bucle: aclarar → contrato de
formato → aterrizar en archivos → ejecutar → mejorar con errores reales.

## 4. La capa pública de Lovable hoy (documentación oficial)

Leído en docs.lovable.dev (página de buenas prácticas de prompting,
actualizada el 28 oct 2026). Su método público, en 4 fases:

1. **Cimientos.** Planificar antes de promptar (qué es, para quién, por
   qué, la acción clave); mapear el viaje del usuario entre pantallas,
   no pantallas sueltas; fijar el lenguaje visual al principio, con
   palabras de estilo que el modelo entiende («minimal», «cinematic»,
   «premium»…) porque mueven tipografía, espaciado y color.
   Y su consejo estrella: terminar el prompt pidiendo que el propio
   Lovable haga las preguntas aclaratorias antes de codificar — el
   paso «clarify» del ancestro, convertido en función del producto
   (Plan Mode).
2. **Pensar en sistemas.** Promptar por COMPONENTE, no por página
   (construir, revisar, refinar, seguir); contenido real, nunca
   «lorem ipsum» (el contenido real revela decisiones de diseño que el
   placeholder esconde); vocabulario atómico (botón, tarjeta, modal,
   toast) en vez de «una interfaz».
3. **Precisión.** Patrones de prompt reutilizables por tipo de sección
   (una biblioteca personal de recetas); y la regla de oro de los
   cambios: decir qué se construye, dónde va, y QUÉ NO SE TOCA — sin
   límites explícitos, un cambio pequeño se propaga a lo que ya
   funcionaba.
4. **Iterar y entregar.** Diseñar con el backend en mente (estados:
   con/sin sesión, datos vacíos, cargando, error); un cambio
   significativo por vez; MARCAR las versiones buenas en el historial
   para poder volver a un estado conocido; antes de un cambio riesgoso,
   abrir la versión actual para saber a qué se vuelve si sale mal.

También público: biblioteca de prompts por caso de uso y la práctica de
mantener un archivo de instrucciones/conocimiento del proyecto que el
agente lee como contexto persistente.

## 5. El linaje, en una mirada

Lo que Lovable heredó de gpt-engineer (verificable comparando ambos):
la aclaración antes de generar (clarify → Plan Mode y «haz que
pregunte»), la generación por piezas con orden, el bucle de mejora
sobre lo ya construido, y la memoria del proyecto en archivos.

Lo que la plataforma añadió y NO está en el repo (documentado u
observable, nivel B): stack fijo y opinado (React + TypeScript +
Tailwind + backend integrado tipo Supabase), edición visual por
selección de elementos, historial de versiones con marcadores,
despliegue y hosting gestionados, y un agente con herramientas
(búsqueda en el código, subagentes de investigación) tras el Plan Mode.
Sus prompts internos y su orquestación exacta no son públicos: eso no
se destila, se observa como caja negra o no se afirma.

Advertencia de época: el ancestro es de la era GPT-4 (2023). Sus
preprompts asumen un modelo que había que obligar a completar y a
respetar formatos; los modelos actuales necesitan menos corsé. Lo que
envejece es la letra; lo que no envejece es el bucle.

## 6. Qué adopta la fábrica de Antonio de este destilado

1. **Puerta de aclaración formal en cada encargo:** antes de construir,
   el ejecutor juzga si falta algo; asume lo razonable y formula como
   máximo UNA pregunta. (Refuerza la plantilla de encargo del
   METODO-CLAUDE §7A con un paso explícito previo.)
2. **Contrato de formato de entrega:** cada entrega llega en un formato
   fijo y parseable por la verificación (archivos, rutas, frase de
   cierre de completitud). El formato es parte del diseño del encargo.
3. **Nada «terminado» sin ejecución:** el punto de entrada se corre; el
   «funciona» se demuestra ejecutando, no afirmando. (Conecta con la
   prueba de 9 puntos de «terminado» del METODO-CLAUDE §4.)
4. **Bucle de mejora con rescate:** al corregir, se aplica lo que está
   bien, se devuelve solo lo erróneo con el detalle del error, y hay
   tope de reintentos. Nunca regenerar todo por un fragmento malo.
5. **«Qué no se toca» en todo encargo de cambio:** construir qué, dónde,
   y los límites explícitos de lo intocable. Regla tomada literal del
   playbook oficial de Lovable (fase 3).
6. **Marcar los estados buenos:** commit/hito verificable tras cada
   estado que funciona, antes de experimentar. (En la fábrica: git ya
   es la mesa; esto lo convierte en hábito con nombre.)

## 7. Veredicto

¿Se puede destilar «Lovable» por completo? Del ancestro abierto, sí:
está hecho arriba, desde la fuente, y su lección central es que el
producto no nació de un prompt genial sino de un bucle disciplinado.
De la plataforma actual, solo su método público — que es, curiosamente,
el mismo bucle vestido de producto. Lo demás es caja cerrada, y
decirlo así también es parte de la destilación.
