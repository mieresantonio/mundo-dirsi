# Rutas de aprendizaje — Mundo Dirsi

> Propósito: convertir lo que Dirsi ya sabe hacer (apps React + Flask,
> trabajo con datos, revisión de material) en capacidades nuevas, una a una,
> con una prueba construida en cada camino. Regla de cada paso: estudiar
> algo concreto, construir algo pequeño que lo demuestre y verificarlo con
> un criterio observable. Nada queda "aprendido" solo por haberlo leído.

> Cómo usar este archivo: elegir UNA ruta, completar sus pasos en orden y
> no saltar al proyecto final sin haber pasado las verificaciones
> intermedias. Cada ruta termina con un proyecto prueba que se puede
> enseñar, reutilizar o descartar sin romper nada de producción.

---

## Ruta 1 — Agentes avanzados y servidores MCP

### Prerrequisitos

- Saber construir una API REST pequeña (Flask o similar) y consumirla
  desde un cliente.
- Entender qué es una herramienta de agente: una función con nombre,
  descripción, entradas y salidas, que el modelo puede decidir invocar.
- Haber usado al menos un agente que llama herramientas y haber visto
  fallar una llamada (argumento mal formado, permiso denegado, respuesta
  inesperada).

### Paso 1 — El protocolo, sin magia

- **Estudiar:** qué problema resuelve un servidor MCP (Model Context
  Protocol): exponer herramientas, recursos y plantillas de prompts a un
  cliente de forma estándar, en lugar de cablear cada integración a mano.
  Leer la especificación oficial y distinguir los tres conceptos:
  herramientas (acciones), recursos (datos de solo lectura) y prompts
  (plantillas reutilizables).
- **Construir:** un esquema en papel (o en un archivo de texto) de un
  servidor MCP imaginario con exactamente 3 herramientas, cada una con
  nombre, descripción, parámetros y qué error devuelve si falta un dato.
- **Verificar:** otra persona — o una revisión propia al día siguiente —
  puede adivinar para qué sirve cada herramienta solo leyendo su
  descripción, sin explicaciones adicionales. Si hay que explicar, la
  descripción está mal escrita.

### Paso 2 — Un servidor MCP propio, mínimo y real

- **Estudiar:** el SDK oficial del lenguaje elegido y el transporte más
  simple para empezar (stdio, local, sin red). Cómo se declaran
  herramientas, cómo se validan los argumentos de entrada y cómo se
  devuelven errores legibles en lugar de trazas crípticas.
- **Construir:** un servidor MCP local con 2 herramientas reales y
  útiles: una que lee un archivo Markdown y devuelve su resumen
  estructurado (títulos y número de líneas), y otra que busca una palabra
  en un directorio y devuelve las coincidencias con su archivo y línea.
- **Verificar:** conectar el servidor a un cliente MCP (por ejemplo, la
  herramienta de inspección oficial) y ejecutar ambas herramientas con
  entradas válidas e inválidas. La verificación pasa cuando: la llamada
  válida devuelve el resultado esperado, la inválida devuelve un error
  claro y el servidor sigue vivo después de ambas.

### Paso 3 — Diseño de herramientas y permisos

- **Estudiar:** principios de diseño de herramientas para agentes:
  nombres verbales y específicos, pocos parámetros obligatorios, salidas
  pequeñas y estructuradas, y separación entre herramientas de lectura
  (seguras) y de escritura (peligrosas). Modelos de permisos: lista de
  herramientas permitidas por defecto, confirmación humana para
  escrituras y sandbox para operaciones destructivas.
- **Construir:** una segunda versión del servidor del paso 2 con una
  herramienta de escritura (crear un archivo de notas) protegida por dos
  capas: solo escribe dentro de un directorio permitido y rechaza rutas
  que intenten salir de él (por ejemplo, con `..` o rutas absolutas).
  Añadir un modo "solo lectura" activable por variable de entorno.
- **Verificar:** intentar, desde el cliente, escribir fuera del
  directorio permitido y con el modo solo lectura activado. Ambas deben
  ser rechazadas con un mensaje comprensible, sin crear ni modificar
  ningún archivo fuera del directorio. Registrar los intentos en un
  archivo de registro (log) y comprobar que el log existe.

### Paso 4 — Evaluar corridas de agente, no solo respuestas

- **Estudiar:** qué significa evaluar un agente: no basta con que la
  respuesta final suene bien; hay que medir si usó las herramientas
  correctas, en el orden correcto, cuántos pasos dio, cuántas veces
  reintentó y si pidió confirmación cuando debía. Conceptos: casos de
  prueba con resultado esperado, trazas (logs de cada llamada) y
  puntuación por criterios, no por impresión general.
- **Construir:** un mini arnés de evaluación: 5 tareas escritas (por
  ejemplo, "encuentra en qué archivo aparece esta frase y resume ese
  archivo"), un script que ejecuta un agente contra el servidor MCP de
  los pasos anteriores, guarda la traza completa y puntúa cada tarea
  como éxito, éxito parcial o fallo según criterios escritos de antemano.
- **Verificar:** ejecutar el arnés dos veces con la misma entrada y
  comparar: las puntuaciones deben ser reproducibles o, si el modelo
  varía, la variación debe quedar documentada en la traza. El arnés pasa
  cuando detecta al menos un fallo real introducido a propósito (por
  ejemplo, una herramienta con una descripción engañosa) en lugar de
  aprobarlo todo.

### Proyecto prueba de la ruta

Un servidor MCP local de "memoria de proyecto": herramientas para listar
notas, buscar en ellas y añadir una nota, con permisos por capas y un
arnés de evaluación de 5 tareas con trazas guardadas. Criterio de éxito:
un agente externo puede usarlo sin instrucciones adicionales, no puede
escribir fuera de su directorio y el arnés detecta un fallo provocado.

---

## Ruta 2 — Computación cuántica básica para desarrolladores

### Prerrequisitos

- Álgebra lineal mínima: qué es un vector, qué hace una matriz al
  multiplicarlo y qué significa probabilidad (números entre 0 y 1 que
  suman 1).
- Python básico y costumbre de ejecutar código en un cuaderno
  (notebook) o script.
- Escepticismo sano: distinguir "esto ya funciona en laboratorio" de
  "esto cambiará el mundo mañana".

### Paso 1 — Qubits, superposición y entrelazamiento en lenguaje llano

- **Estudiar:** un qubit como una moneda que, antes de mirarla, puede
  describirse como combinación de cara y cruz con ciertos pesos, no
  como "cara y cruz a la vez" en sentido literal. Superposición como esa
  combinación de pesos. Entrelazamiento como correlación fuerte entre
  dos qubits: medir uno da información sobre el otro, sin que eso
  permita enviar mensajes más rápido que la luz. Interferencia: los
  pesos pueden cancelarse o reforzarse, y ahí está la potencia real.
- **Construir:** una explicación propia de una página, con un ejemplo
  cotidiano (monedas, dados o luces) y una lista explícita de tres
  afirmaciones populares FALSAS sobre lo cuántico (por ejemplo, que un
  ordenador cuántico prueba todas las respuestas a la vez y elige la
  buena).
- **Verificar:** una persona sin formación técnica lee la explicación y
  puede decir con sus palabras qué es un qubit y por qué el
  entrelazamiento no sirve para comunicarse instantáneamente. Si repite
  un mito de la lista de falsedades, la explicación debe reescribirse.

### Paso 2 — Primer programa cuántico en un simulador

- **Estudiar:** Qiskit (el kit de desarrollo cuántico de IBM) a nivel
  de uso: cómo se crea un circuito, qué es una puerta (Hadamard,
  NOT cuántica, CNOT) y qué significa ejecutar el circuito muchas veces
  (shots) para obtener una distribución de resultados.
- **Construir:** tres circuitos pequeños y ejecutables en simulador
  local, sin hardware real: (a) un qubit en superposición medida 1.000
  veces, (b) dos qubits entrelazados (par de Bell) medidos 1.000 veces,
  (c) el mismo circuito (b) con una puerta extra que rompe el
  entrelazamiento, para comparar.
- **Verificar:** los resultados numéricos coinciden con lo esperado
  dentro de un margen razonable: (a) cerca de 50/50 entre 0 y 1, (b)
  casi solo 00 y 11 en proporciones parecidas, (c) aparecen los cuatro
  resultados. Guardar las salidas en un archivo para poder compararlas
  después.

### Paso 3 — Hype frente a realidad, con fechas y límites

- **Estudiar:** el estado real del campo: número de qubits actuales,
  tasas de error, qué es la corrección de errores y por qué es el cuello
  de botella, y qué familias de problemas tienen ventaja cuántica
  demostrada o plausible (simulación de moléculas, ciertos problemas de
  optimización) frente a las que no (navegar por internet más rápido,
  romper todo el cifrado actual mañana).
- **Construir:** una tabla propia de dos columnas — "demostrado o en
  laboratorio" frente a "promesa sin fecha" — con al menos 6 filas y la
  fuente de cada afirmación (documentación oficial, artículo revisado
  o nota de prensa, etiquetada como tal).
- **Verificar:** cada fila de la columna de promesas lleva una nota de
  qué tendría que ocurrir para que dejara de ser promesa (por ejemplo,
  "qubits lógicos con tasa de error por debajo de X"). Una tabla sin
  esas condiciones es solo una lista de deseos y no pasa.

### Paso 4 — Un algoritmo pequeño, entendido de verdad

- **Estudiar:** un algoritmo cuántico introductorio completo, por
  ejemplo el de Deutsch-Jozsa o la búsqueda de Grover en su versión
  mínima: qué problema resuelve, por qué la versión clásica necesita
  más pasos y dónde entra la interferencia.
- **Construir:** la implementación en simulador para el caso más
  pequeño posible (2-3 qubits), con comentarios propios en cada puerta
  explicando qué hace y por qué está ahí, más una comparación con la
  solución clásica equivalente escrita en Python normal.
- **Verificar:** el programa cuántico da la respuesta correcta en al
  menos el 90% de las ejecuciones simuladas y la explicación escrita
  permite a otra persona señalar en qué paso la interferencia hace el
  trabajo. Si la explicación solo dice "es cuántico y por eso es más
  rápido", no pasa.

### Proyecto prueba de la ruta

Un cuaderno (notebook) único y ejecutable de principio a fin: explicación
llana con mitos desmentidos, los tres circuitos del paso 2 con sus
salidas guardadas, la tabla hype/realidad con fuentes y el algoritmo
mínimo comentado. Criterio de éxito: otra persona puede ejecutarlo en un
entorno limpio y obtener los mismos resultados aproximados, y puede
explicar después qué parte es real hoy y qué parte es promesa.

---

## Ruta 3 — Rust o Go para herramientas (tooling)

### Prerrequisitos

- Haber escrito al menos una herramienta de línea de comandos (CLI) en
  Python o JavaScript, aunque sea pequeña, y haber sufrido sus límites:
  arranque lento, dependencia del intérprete o empaquetado incómodo.
- Nociones de compilación frente a interpretación y de qué significa
  distribuir un binario único.
- Un proyecto real pendiente de herramienta (por ejemplo, un generador
  de informes, un buscador de archivos o un conversor de formatos).

### Paso 1 — Decidir cuál primero, con criterios y no por moda

- **Estudiar:** los perfiles reales de cada lenguaje. Rust: control
  fino de memoria sin recolector de basura, sistema de ownership que el
  compilador verifica, rendimiento máximo y curva de aprendizaje
  pronunciada; ideal cuando el rendimiento y la corrección importan más
  que la velocidad de escritura. Go: sintaxis pequeña, compilación
  rápida, concurrencia sencilla con goroutines, binarios estáticos
  fáciles de distribuir; ideal para CLIs, servidores y herramientas de
  red que deben escribirse rápido y mantenerse fácil.
- **Construir:** una tabla de decisión propia con 5 criterios (tiempo
  de aprendizaje, velocidad de desarrollo, rendimiento, ecosistema de
  CLIs, facilidad de distribución) puntuados para ambos lenguajes, y
  una recomendación escrita para el caso concreto de Dirsi: empezar por
  **Go** para herramientas de uso diario, porque su curva es corta, sus
  binarios se distribuyen sin fricción y cubre el 90% de las CLIs que
  hacen falta; dejar **Rust** para la segunda fase, cuando una
  herramienta concreta exija rendimiento o garantías que Go no da.
- **Verificar:** la recomendación sobrevive a una prueba: si dentro de
  seis meses ninguna herramienta construida en Go se ha quedado corta
  de rendimiento, la elección fue correcta; si alguna sí, esa
  herramienta concreta es la candidata a reescribir en Rust, no todo el
  catálogo. La decisión queda escrita, no es una preferencia vaga.

### Paso 2 — Primera CLI en Go: útil desde el día uno

- **Estudiar:** la estructura de un programa Go (módulos, paquetes,
  `main`), manejo de argumentos y flags de la biblioteca estándar,
  lectura de archivos y salida con códigos de error adecuados (0 éxito,
  distinto de 0 fallo).
- **Construir:** una CLI que haga algo que hoy se hace a mano: por
  ejemplo, contar líneas, palabras y archivos Markdown en un directorio
  y emitir un resumen, con flags para filtrar por extensión y para
  salida en formato legible o JSON.
- **Verificar:** compilar el binario, ejecutarlo en tres directorios
  distintos (vacío, pequeño, con subdirectorios) y comparar su salida
  con el resultado de herramientas conocidas del sistema (`wc`, `find`).
  Los números deben coincidir; cualquier discrepancia es un bug, no un
  redondeo.

### Paso 3 — Concurrencia y red en Go, donde brilla

- **Estudiar:** goroutines y canales a nivel práctico: lanzar trabajo
  en paralelo, recoger resultados sin carreras de datos y limitar la
  concurrencia (por ejemplo, con un semáforo basado en canales).
- **Construir:** una segunda CLI que comprueba el estado de una lista
  de URLs (código de respuesta y tiempo) en paralelo, con límite de
  peticiones simultáneas y un resumen final de éxitos, fallos y
  tiempos.
- **Verificar:** ejecutarla contra 20 URLs de prueba (algunas lentas,
  alguna que falla) y comprobar que termina más rápido que la versión
  secuencial equivalente, que no pierde ninguna URL del informe y que
  ninguna petición lenta bloquea a las demás indefinidamente (hay un
  tiempo máximo por petición).

### Paso 4 — Primera incursión en Rust, con un problema acotado

- **Estudiar:** ownership, borrowing y el compilador como ayudante
  exigente: por qué rechaza programas que en otros lenguajes compilan y
  fallan en ejecución, y cómo leer sus mensajes de error como
  instrucciones en lugar de obstáculos.
- **Construir:** reescribir en Rust la CLI del paso 2 (la más simple),
  sin añadir funciones nuevas. El objetivo no es mejorarla, sino
  aprender el modelo de memoria con un problema ya resuelto.
- **Verificar:** la versión Rust produce exactamente la misma salida
  que la versión Go ante las mismas entradas (prueba de paridad), y el
  binario resultante funciona sin instalar nada más en otra máquina.
  Anotar en un párrafo qué parte costó más (normalmente, el préstamo
  de datos entre funciones) y qué se aprendió de ello.

### Proyecto prueba de la ruta

Dos binarios distribuibles desde el mismo catálogo de ideas: la CLI de
estadísticas de Markdown en Go (uso diario) y su gemela en Rust (prueba
de paridad). Criterio de éxito: ambos se ejecutan en una máquina limpia
sin intérprete instalado, sus salidas coinciden ante las mismas
entradas y la CLI de URLs en Go demuestra una ganancia real de tiempo
frente a la versión secuencial.

---

## Ruta 4 — Patrones avanzados de React

### Prerrequisitos

- React funcional con hooks básicos (`useState`, `useEffect`) usado en
  al menos dos proyectos reales, no solo tutoriales.
- JavaScript/TypeScript cómodo con funciones, desestructuración y
  módulos.
- Haber sufrido un componente gigante que hace demasiadas cosas, un
  estado que se desincroniza entre componentes o un renderizado lento
  sin saber por qué.

### Paso 1 — Composición en lugar de configuración infinita

- **Estudiar:** el patrón de composición: componentes pequeños que se
  combinan como piezas (`children`, componentes compuestos) en lugar de
  un componente con veinte props booleanas. Cuándo una prop es
  suficiente y cuándo es señal de que hay que dividir el componente.
- **Construir:** refactorizar un componente real existente (por
  ejemplo, una tarjeta o un panel) que tenga más de 8 props, para que
  su uso quede como piezas componibles, sin cambiar lo que ve el usuario.
- **Verificar:** la interfaz visible no cambia (comparación visual
  antes/después), el componente padre queda más corto y legible, y se
  puede añadir una variante nueva (por ejemplo, una tarjeta sin imagen)
  sin tocar el componente original, solo combinando piezas.

### Paso 2 — Hooks personalizados que encapsulan lógica, no JSX

- **Estudiar:** qué merece ser un hook propio: lógica con estado y
  efectos que se repite en dos o más sitios (carga de datos, formularios,
  temporizadores, atajos de teclado), y qué NO merece serlo (una función
  pura sin estado, o un componente disfrazado).
- **Construir:** tres hooks propios y reutilizables: uno para cargar
  datos de una API con estados de carga/error, uno para formularios con
  validación simple y uno para detectar clics fuera de un elemento
  (útil para menús y modales). Cada uno con su documentación de uso en
  un comentario.
- **Verificar:** usar cada hook en al menos dos componentes distintos
  sin duplicar su lógica interna, y escribir una prueba que demuestre
  que el hook de carga de datos pasa por los estados carga → éxito y
  carga → error ante respuestas simuladas.

### Paso 3 — Máquinas de estado para flujos con muchos estados

- **Estudiar:** por qué los booleanos sueltos (`cargando`, `error`,
  `enviado`, combinados) producen estados imposibles (cargando y error
  a la vez) y cómo una máquina de estados finitos los evita: un estado
  a la vez, transiciones explícitas y estados imposibles que ni siquiera
  se pueden representar.
- **Construir:** modelar un flujo real (por ejemplo, un asistente de
  varios pasos, un proceso de subida de archivo o un reproductor) como
  máquina de estados, con su diagrama dibujado antes de escribir código,
  e implementarlo con una biblioteca pequeña o a mano con un reducer.
- **Verificar:** enumerar todas las transiciones posibles y probar que
  las imposibles no ocurren: por ejemplo, no se puede "enviar" dos
  veces seguidas sin pasar por el estado correspondiente, y el botón de
  retroceso no aparece en el primer paso. Una prueba automatizada cubre
  al menos 3 transiciones inválidas rechazadas.

### Paso 4 — Rendimiento: medir antes de optimizar

- **Estudiar:** las herramientas de medición (React DevTools Profiler),
  qué hace re-renderizar un componente, y las herramientas de
  optimización con su coste: memorización de componentes, de valores y
  de funciones, y cuándo cada una empeora el código sin mejorar nada.
- **Construir:** una lista larga (cientos de filas) con un filtro en
  vivo que, en su primera versión, se note lenta; medirla con el
  Profiler, identificar el cuello de botella real y aplicar solo la
  optimización que lo resuelve.
- **Verificar:** antes/después con números del Profiler (tiempo de
  renderizado y número de componentes re-renderizados al escribir una
  letra en el filtro). La optimización pasa solo si mejora una métrica
  medida, no por intuición; y se documenta qué se probó y se descartó.

### Paso 5 — Testing con Jest y Testing Library, desde el usuario

- **Estudiar:** la filosofía de Testing Library: probar lo que ve y
  hace el usuario (textos, botones, flujos) en lugar de detalles
  internos (nombres de variables de estado). Qué probar (flujos
  críticos y lógica de negocio) y qué no (cada detalle visual).
- **Construir:** una suite de pruebas para una aplicación pequeña
  existente: renderizado de los componentes clave, interacción completa
  de un flujo (rellenar, enviar, ver el resultado) y al menos un caso
  de error visible para el usuario.
- **Verificar:** la suite pasa en un entorno limpio (`npm test` sin
  intervención), cubre el flujo crítico de principio a fin y falla a
  propósito cuando se rompe el componente (prueba de mutación manual:
  cambiar un texto o un comportamiento y comprobar que al menos una
  prueba se pone roja).

### Proyecto prueba de la ruta

Una mini aplicación (por ejemplo, un gestor de notas con editor, filtros
y estados de guardado) construida con composición, dos hooks propios,
una máquina de estados para el flujo de guardado, una lista optimizada
con medición antes/después y una suite de pruebas que cubre el flujo
crítico. Criterio de éxito: añadir una variante de interfaz nueva no
exige tocar los componentes base, la máquina rechaza transiciones
inválidas y la suite falla si se rompe el flujo.

---

## Ruta 5 — Escalado de backend

### Prerrequisitos

- Una API en producción real o simulada con base de datos, aunque sea
  pequeña, y experiencia con sus fallos: lentitud bajo carga, tareas
  que bloquean respuestas o datos que crecen sin control.
- SQL básico y nociones de índices.
- Haber medido al menos una vez un tiempo de respuesta, no solo haberlo
  intuido.

### Paso 1 — Caché: qué guardar, dónde y cuándo invalidar

- **Estudiar:** niveles de caché (en memoria del proceso, caché
  compartida tipo Redis, caché HTTP), qué datos conviene cachear
  (lecturas frecuentes, datos que cambian poco) y el problema clásico:
  la invalidación. Estrategias: tiempo de vida (TTL), invalidación al
  escribir y claves versionadas.
- **Construir:** añadir caché a un endpoint de lectura frecuente de una
  API existente, con TTL configurable, y un endpoint o mecanismo que
  invalide la entrada correspondiente cuando el dato cambia.
- **Verificar:** medir el tiempo de respuesta del endpoint antes y
  después con 100 peticiones repetidas; la segunda medición debe ser
  claramente más rápida. Después, modificar el dato y comprobar que la
  siguiente lectura devuelve el valor nuevo, no el cacheado viejo.
  Ambas comprobaciones deben pasar: velocidad sin frescura es un bug.

### Paso 2 — Colas y trabajos en segundo plano

- **Estudiar:** por qué una petición HTTP no debe hacer trabajo lento
  (enviar correos, generar informes, procesar archivos): el usuario
  espera, la conexión puede cortarse y el trabajo se pierde. Patrón:
  la petición encola un trabajo y responde de inmediato; un trabajador
  aparte lo procesa, con reintentos y registro de fallos.
- **Construir:** un sistema mínimo de cola (puede empezar con una tabla
  en base de datos o Redis) con un trabajador que procesa un trabajo
  concreto — por ejemplo, generar un resumen o enviar una notificación
  simulada —, con reintento ante fallo y un estado visible (pendiente,
  procesando, hecho, fallido).
- **Verificar:** enviar 10 trabajos, detener el trabajador a mitad,
  reanudarlo y comprobar que ningún trabajo se pierde ni se procesa dos
  veces de forma dañina (idempotencia: procesar dos veces el mismo
  trabajo da el mismo resultado final). El panel de estados refleja la
  realidad en cada momento.

### Paso 3 — Rate limiting y protección contra abuso

- **Estudiar:** algoritmos básicos (ventana fija, cubo de tokens,
  ventana deslizante), qué limitar (por IP, por usuario, por endpoint),
  qué devolver cuando se supera el límite (código 429 y cabeceras que
  indican cuándo reintentar) y qué NO limitar (nunca bloquear al propio
  sistema ni a los endpoints de salud).
- **Construir:** un limitador en una API existente: un endpoint público
  sensible (por ejemplo, login o registro) limitado a un número
  razonable de intentos por minuto, con respuesta 429 y mensaje claro
  al superarlo, y un endpoint interno exento.
- **Verificar:** lanzar ráfagas controladas de peticiones (por ejemplo,
  50 en pocos segundos) y comprobar que las primeras pasan, las
  siguientes reciben 429, y que tras esperar el tiempo indicado el
  acceso se recupera solo. Comprobar también que un usuario distinto no
  resulta afectado por el límite de otro.

### Paso 4 — Postgres frente a SQLite: puntos de decisión

- **Estudiar:** las diferencias que de verdad importan: SQLite es un
  archivo, sin servidor, perfecto para un solo proceso y prototipos;
  Postgres es un servidor con usuarios, permisos, tipos avanzados,
  índices concurrentes y escritura concurrente real. Señales de que
  hay que migrar: varios procesos escribiendo a la vez, necesidad de
  tipos o búsquedas avanzadas, o un despliegue con más de una instancia
  de la aplicación.
- **Construir:** una lista de decisión escrita con 6 criterios y el
  umbral de cada uno (por ejemplo, "más de un proceso escritor" o
  "más de X escrituras por segundo sostenidas"), y una migración de
  práctica: la misma aplicación pequeña funcionando con SQLite y luego
  con Postgres, con el cambio aislado en la capa de conexión.
- **Verificar:** la aplicación pasa la misma suite de pruebas contra
  ambas bases de datos sin cambiar la lógica de negocio, y la lista de
  decisión permite clasificar tres proyectos reales (uno debe quedarse
  en SQLite, otro debe estar en Postgres y el tercero debe quedar en
  zona gris con su motivo escrito).

### Proyecto prueba de la ruta

Una API de ejemplo con: un endpoint cacheado con invalidación correcta,
una cola con trabajador y reintentos que procesa informes simulados sin
pérdidas, rate limiting en el endpoint de login con 429 documentado y
la misma aplicación corriendo contra SQLite y contra Postgres con la
decisión documentada. Criterio de éxito: bajo una ráfaga de prueba la
API responde rápido en lecturas, no pierde trabajos, limita el abuso y
la elección de base de datos está justificada por escrito, no por
costumbre.

---

## Ruta 6 — Seguridad de IA y evaluación

### Prerrequisitos

- Haber construido al menos un flujo donde un modelo recibe texto de
  un usuario o de un documento externo y actúa en consecuencia.
- Conocer los conceptos de alucinación (afirmar algo falso con
  seguridad) y de inyección de prompt (instrucciones escondidas en
  datos que el modelo obedece por error).
- Aceptar una regla incómoda: ningún filtro es perfecto; la seguridad
  se construye en capas, no con una sola barrera.

### Paso 1 — Defensas contra inyección de prompt, en capas

- **Estudiar:** cómo llega una inyección: texto pegado por el usuario,
  contenido de una página, un documento o un correo que el agente lee
  y trata como orden. Defensas en capas: separar instrucciones del
  sistema de datos del usuario (delimitadores y roles claros), no
  ejecutar acciones sensibles a partir de texto no confiable sin
  confirmación, listas de acciones permitidas y revisión de la acción
  propuesta antes de ejecutarla.
- **Construir:** un pequeño agente de ejemplo con 3 acciones (leer,
  resumir, archivar) y un conjunto de 10 textos de ataque de prueba
  (órdenes escondidas en notas, correos simulados y páginas simuladas)
  que intentan que archive o borre algo sin permiso.
- **Verificar:** ejecutar los 10 ataques contra el agente: ninguno
  debe lograr una acción sensible sin confirmación explícita, y las
  acciones legítimas del usuario deben seguir funcionando (un filtro
  que bloquea todo también es un fallo). Registrar cuántos ataques
  detuvo cada capa por separado.

### Paso 2 — Medir alucinaciones en lugar de intuirlas

- **Estudiar:** por qué "parece correcto" no es una medida: formas de
  medir — verificación contra una fuente (¿cada afirmación aparece en
  el documento de referencia?), preguntas con respuesta conocida y
  conjuntos de prueba con respuestas verificables, y la diferencia
  entre un error factual y una invención completa.
- **Construir:** un conjunto de 20 preguntas con respuesta verificable
  sobre un dominio acotado (por ejemplo, el contenido de un documento
  propio), un script que hace las preguntas al modelo y un verificador
  que clasifica cada respuesta como correcta, parcialmente correcta o
  inventada, según reglas escritas antes de ver las respuestas.
- **Verificar:** ejecutar el conjunto dos veces y calcular la tasa de
  invención. La verificación pasa cuando la tasa es un número
  reproducible y documentado (no cuando es cero: cero en una muestra
  pequeña suele significar que la prueba es demasiado fácil), y cuando
  al menos un caso inventado queda guardado como ejemplo para mejorar
  el sistema.

### Paso 3 — Un arnés de evaluación (eval harness) reutilizable

- **Estudiar:** la anatomía de un arnés: casos de prueba versionados,
  ejecución automática, puntuación por criterios, informe comparativo
  entre versiones del sistema y la regla de oro — nunca cambiar los
  casos para que pase la versión nueva; si un caso es injusto, se
  corrige con justificación escrita y queda registrado.
- **Construir:** un arnés genérico que sirva para más de un sistema:
  lee casos de un archivo, ejecuta el sistema bajo prueba, puntúa con
  funciones de puntuación separadas del sistema y emite un informe
  legible con aciertos, fallos y ejemplos. Aplicarlo a dos versiones
  de un mismo flujo (por ejemplo, con y sin una defensa contra
  inyección) y comparar.
- **Verificar:** el informe muestra una diferencia real entre las dos
  versiones (la versión con defensa detiene más ataques sin romper
  tareas legítimas) y el arnés detecta una regresión introducida a
  propósito (por ejemplo, quitar una defensa y ver cómo cae la
  puntuación). Un arnés que siempre da la misma nota no evalúa nada.

### Paso 4 — Puertas de revisión humana (human-review gates)

- **Estudiar:** cuándo debe intervenir una persona: acciones
  irreversibles (borrar, enviar, pagar), decisiones con datos sensibles
  y cualquier salida con baja confianza o alto impacto. Diseños de
  puerta: aprobación antes de actuar, revisión de un lote de salidas y
  auditoría posterior con registro de quién aprobó qué y cuándo.
- **Construir:** en el agente del paso 1, una puerta de revisión: las
  acciones sensibles quedan en estado "pendiente de aprobación" con su
  justificación visible, y solo se ejecutan tras una confirmación
  explícita; todas las decisiones quedan en un registro con fecha,
  acción y resultado.
- **Verificar:** intentar 5 acciones sensibles sin aprobación (deben
  quedar pendientes, no ejecutarse) y 5 con aprobación (deben
  ejecutarse y quedar registradas). Revisar el registro una semana
  después simulada: debe permitir reconstruir quién aprobó cada acción
  y por qué. Si el registro no permite esa reconstrucción, la puerta
  está incompleta.

### Proyecto prueba de la ruta

Un agente de demostración con defensas en capas contra inyección, un
conjunto de 20 preguntas para medir invención, un arnés de evaluación
que compara dos versiones del sistema y una puerta de revisión humana
con registro auditable. Criterio de éxito: 10 ataques de prueba no
logran acciones sensibles sin aprobación, la tasa de invención es un
número medido y documentado, el arnés detecta una regresión provocada
y el registro permite reconstruir cada decisión sensible.

---

## Orden sugerido entre rutas

1. **React avanzado** y **seguridad/evaluación** primero: se aplican de
   inmediato a las apps y agentes que ya existen.
2. **Agentes/MCP** y **backend escalable** después: amplían lo que esos
   proyectos pueden hacer y soportar.
3. **Go/Rust** cuando haya una herramienta concreta que lo pida, no
   antes: aprender un lenguaje sin un uso inmediato se olvida.
4. **Cuántica** como ruta de fondo, sin prisa: un circuito por semana
   es mejor ritmo que un atracón de fin de semana.

## Regla de cierre de cada ruta

Una ruta se considera cerrada solo cuando su proyecto prueba existe,
funciona en un entorno limpio y su criterio de éxito está documentado
con números o capturas, no con una sensación. Las rutas cerradas se
anotan en el archivo de registro de Mundo Dirsi; las abiertas se
retoman por el paso donde quedaron, no desde cero.
