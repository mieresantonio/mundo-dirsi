# Desarrollo web — lo aprendido

## Principios que se repiten en cada proyecto

- **Una app, una especialización.** Cada proyecto rinde más cuando hace una
  sola cosa bien que cuando intenta cubrirlo todo. Una calculadora de gas, un
  laboratorio de hash o una agenda de barbería se entienden en segundos; una
  app que promete diez cosas a la vez no se entiende en ninguna.
- **Primero la tarea, luego la herramienta.** Antes de elegir un framework o
  un modelo, hay que nombrar la tarea que se repite y el resultado visible
  que se espera. Si eso no está claro, la herramienta solo esconde la duda.
- **Datos de ejemplo, etiquetados siempre.** Todo lo simulado lleva su aviso
  visible en cabecera y en cada pantalla relevante. Nunca debe parecer real
  lo que es un ejemplo: ni precios, ni saldos, ni transacciones.
- **Originalidad sobre copia.** Las estructuras y las ideas generales se
  pueden reutilizar; los textos ajenos, no. Cada app de portafolio se redacta
  con palabras propias, y el usuario puede añadir su propio contenido.

## Sistemas de diseño

- **Tokens antes que componentes.** Colores, tipografía y espaciados se
  definen una vez como variables y luego se usan en todas partes. Sobrescribir
  un framework con cientos de líneas sueltas produce un "techo de plantilla":
  se ve decente, pero nunca llega a identidad propia.
- **Un solo set de iconos.** Mezclar tres librerías de iconos a la vez
  (por ejemplo, una por CDN y dos por paquete) da inconsistencia visual y
  peso innecesario. Elegir una y usarla en todo el proyecto.
- **Modo oscuro en web3, casi obligatorio.** En el ámbito cripto el tema
  oscuro es la norma; una app clara sin alternativa oscura se siente fuera
  de lugar.
- **Imágenes propias o generadas en local.** Las imágenes de plantilla
  (la foto de ejemplo que trae un starter) delatan el origen del proyecto.
  Generar arte local (por ejemplo SVG a partir de rasgos) evita además
  enlaces externos que se pueden romper.
- **Mobile-first de verdad.** Diseñar primero para el teléfono y luego
  ampliar a escritorio, no al revés. Los estados vacíos, los errores y la
  carga son parte del diseño, no un detalle final.

## Patrones que funcionan

- **Leer → experimentar → responder.** En aprendizaje: primero una
  explicación corta, luego un laboratorio interactivo, luego una pregunta
  que compruebe lo aprendido. Leer sin practicar se olvida; practicar sin
  contexto confunde.
- **Laboratorio como diferenciador.** El contenido bonito sin interacción
  es un folleto. Un simulador que se puede romper (editar un bloque y ver
  cómo se marca la cadena como rota) enseña más que diez párrafos.
- **Validación paso a paso.** En formularios de varios pasos, cada paso
  bloquea el avance hasta que sus datos son válidos, con mensajes de error
  claros y concretos (formato esperado, rango permitido, saldo insuficiente).
- **Estados visibles.** Carga, vacío, error y éxito tienen su pantalla. Un
  "no se encontró ningún bloque" con acción para limpiar filtros vale más
  que una lista en blanco.
- **Copiar al portapapeles.** En herramientas para desarrolladores y en
  bibliotecas de prompts, el botón de copiar es una función central, no un
  adorno.

## Verificación por renderizado

- **Construir y probar el flujo real.** No basta con que el código compile:
  hay que crear un registro, comprobar que el hueco queda bloqueado,
  intentar el solapamiento y verificar que se rechaza, cancelar y comprobar
  que el hueco se libera. La verificación se hace con el servidor corriendo
  y el flujo completo, no leyendo el código y suponiendo que funciona.
- **Verificar después de cada pasada.** En un ciclo de rediseño, cada
  iteración se construye y se comprueba; si algo falla, se revierte. Nunca
  se acumulan cambios sin verificar sobre cambios sin verificar.
- **Vectores conocidos para lo crítico.** Un hash implementado a mano se
  comprueba contra valores de referencia públicos (por ejemplo, el hash de
  la cadena vacía y de "abc"), no contra la intuición del autor.

## Lo que falló y por qué

- **Restos de plantilla en un proyecto final.** Páginas de ejemplo, favicon
  del starter, idioma del documento en inglés en una app en español,
  artefactos de build versionados y un README que sigue siendo el de la
  plantilla. Todo eso es lo primero que ve un reclutador, y habla antes que
  el código.
- **Dos manifiestos de dependencias en conflicto.** Un archivo viejo con
  versiones de años atrás junto a uno moderno confunde a quien despliega y
  puede romper rutas enteras de despliegue. Una sola fuente de verdad.
- **Codificación rota visible.** Un buscador que muestra caracteres
  corruptos es un error pequeño con un coste de credibilidad enorme.
- **Belleza sin contenido.** La versión visualmente más pulida de una
  comparativa puede ser la más floja en contenido: secciones marcadas como
  "pronto", sin cuestionarios, sin profundidad. El diseño no compensa la
  falta de sustancia; la sustancia sin diseño tampoco llega.
- **Generar lento no es generar mejor.** La versión que más tardó en
  generarse no tenía ventaja clara sobre las demás. Tiempo de generación no
  es una medida de calidad.
