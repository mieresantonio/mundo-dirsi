# Herramientas y conexiones — lo aprendido

## GitHub: el conector y sus lecciones

- **Lectura primero, escritura con aprobación.** El conector de GitHub
  lee repositorios, archivos, issues y pull requests. Las escrituras
  requieren la instalación de la aplicación en la cuenta y los permisos
  aceptados; sin esa revisión, las escrituras fallan con errores de
  acceso aunque la lectura funcione.
- **La herramienta de subida de archivos funciona con dos piezas:**
  un directorio fuente local y un archivo con la lista de rutas, una por
  línea. Los detalles de formato de esa lista importan (separadores y
  codificación); un formato incorrecto rompe la subida aunque los
  archivos estén bien.
- **Las escrituras en segundo plano sobreviven a las esperas de
  aprobación.** Una operación de escritura lanzada en segundo plano
  puede completarse aunque la aprobación tarde: no hay que cancelarla ni
  relanzarla por impaciencia. Relanzar crea duplicados.
- **La herramienta de fusión (merge) funciona.** Fusionar una pull
  request a través del conector es una operación fiable una vez que los
  permisos están en orden.
- **El conector no crea repositorios.** Crear un repositorio nuevo no es
  una operación del conector: se hace con la sesión del usuario en el
  navegador, y después el conector puede subir contenido a ese
  repositorio ya existente. Intentar crear repos por el conector es
  perder tiempo.
- **Nunca escribir sin aprobación en el repositorio del usuario.** La
  regla es preparar cambios y pedir aprobación antes de escribir, salvo
  delegación explícita del usuario para fusionar, crear repos y modificar
  sin límites. Esa delegación, cuando existe, se respeta; sin ella, no se
  escribe.

## Rutas con el navegador y la sesión del usuario

- **La sesión del usuario abre puertas que el conector no abre.** Crear
  repos, completar pasos de despliegue en paneles web y verificar una
  app en vivo se hacen con la sesión ya iniciada del usuario en el
  navegador. Esa es la ruta cuando el conector no cubre la operación.
- **Límites de la ruta del navegador.** El navegador no crea cuentas ni
  autoriza aplicaciones nuevas por su cuenta. Si falta una sesión o un
  permiso, se informa exactamente qué falta y se pide al usuario, en
  lugar de improvisar un registro o una autorización.
- **Las tareas de navegador pueden terminar con error sin que la app se
  vea afectada.** Si una tarea de verificación en el navegador falla o
  se interrumpe, la aplicación desplegada sigue intacta; lo que queda
  pendiente es solo la verificación, que se puede retomar en otra sesión.
  No se reinicia automáticamente una tarea de navegador fallida.
- **Un secreto enviado por chat no es una vía de acceso.** Si el usuario
  envía una contraseña por chat, no se almacena, no se repite y no se
  usa desde el texto: el acceso va por la sesión activa o por el flujo
  de entrada seguro, nunca por el mensaje.

## Comportamiento ante las aprobaciones

- **Los tiempos de espera de aprobación no son un "no se puede".**
  Cuando una aprobación tarda o caduca, el límite es de la sesión y del
  permiso, no de la capacidad. Se nombra el límite exactamente como lo
  que es y se busca la ruta alternativa (sesión del navegador, conector,
  o el paso manual del usuario), en lugar de presentar el bloqueo como
  imposibilidad.
- **No disfrazar un límite de sesión como imposibilidad técnica.** Esa
  distinción importa para la confianza: el usuario rechaza que se le
  diga que algo no se puede cuando lo que falta es una sesión o una
  aprobación.
- **Un solo paso manual, nombrado con exactitud.** Cuando algo requiere
  al usuario (valores de entorno, una contraseña de aplicación, un clic
  de conexión), se nombra ese paso y solo ese, con instrucciones
  concretas, en lugar de devolverle una lista de tareas pendientes.

## Archivos temporales y persistencia

- **El directorio temporal se borra en los reinicios.** Todo lo que
  vive solo en el directorio temporal puede desaparecer cuando la
  máquina se reinicia o se reemplaza. Es útil para borradores, capturas
  y volcados intermedios, pero nunca para el único ejemplar de algo.
- **El trabajo duradero vive en el espacio de trabajo.** Archivos,
  guiones, registros de sincronización y estado de agentes van bajo el
  directorio de trabajo del usuario, con rutas explícitas, no bajo
  instalaciones del sistema ni rutas temporales.
- **Detener los servidores de prueba al terminar.** Un servidor de
  verificación olvidado deja un puerto ocupado y rompe la siguiente
  verificación. Cada verificación termina con su servidor detenido.
- **Registrar la sincronización.** Cuando se sube contenido a un
  repositorio remoto, guardar un registro de sincronización (qué se
  subió, en qué commit, en qué rama) permite verificar después que el
  contenido remoto es legible, sin tener que confiar en la respuesta de
  la subida.
