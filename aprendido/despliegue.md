# Despliegue — lo aprendido

## Render: lo que hay que saber antes de prometer nada

- **Verificación con tarjeta.** Render pide una tarjeta para verificar la
  cuenta, con un cargo pequeño de verificación. Una tarjeta de débito en
  moneda local puede no funcionar o no registrar nada: un intento fallido
  puede dejar la cuenta sin tarjeta registrada, sin servicios y sin cargos,
  como si el intento no hubiera ocurrido. No insistir en reintentos con la
  misma tarjeta que ya falló.
- **Tarjeta prepago internacional como opción futura.** Una billetera
  digital en dólares con tarjeta virtual Visa prepago internacional, apta
  para comercio electrónico, encaja en principio con la verificación de
  Render. Queda una incertidumbre sin resolver: si el procesador de
  Render rechaza específicamente las tarjetas prepago. Solo probarlo lo
  resuelve, y un rechazo no cuesta nada.
- **Límites del nivel gratuito.** El nivel gratis duerme los servicios sin
  actividad, las bases de datos gratuitas caducan, y no hay copias de
  seguridad serias. Para una demo personal sirve; para un cliente, no.
- **Piso de producción realista.** Para una app de cliente que debe
  funcionar siempre, el piso ronda los 13 dólares al mes: servicio web de
  pago sin suspensión por inactividad más base de datos de pago con
  copias de seguridad. A eso se suma el dominio (alrededor de 10–15
  dólares al año). El coste de hosting se traslada al cliente (hosting
  más una cuota mensual de mantenimiento), no lo absorbe quien desarrolla.
- **"Siempre funciona" no es 100 %.** Lo honesto es 99 % o más con niveles
  de pago, monitorización y alguien de guardia. Prometer un 100 % literal
  es mentir.
- **El archivo de despliegue debe estar limpio.** Un manifiesto de
  despliegue que todavía lleva el nombre de ejemplo de la plantilla
  ("sample-service-name") delata que nadie revisó la configuración antes
  de desplegar.

## PythonAnywhere: el camino sin tarjeta

- **Sin tarjeta y con límites propios.** La cuenta gratuita no pide
  tarjeta y sirve para una primera demostración pública real. Sus límites:
  las consolas gratuitas no tienen Node ni npm (no se puede construir un
  frontend desde la consola gratuita), y el despliegue de un frontend ya
  construido exige otros medios.
- **Variables de entorno en el archivo WSGI.** La configuración del
  entorno (claves, remitente de correo, URL pública del frontend) se pone
  en el archivo WSGI, no en el código. Si falta una variable, el fallo
  aparece en tiempo de ejecución, no en el despliegue.
- **El error de registro que hay que conocer.** Si el registro de usuario
  guarda la cuenta y después intenta enviar el correo de verificación, y
  el envío falla (por ejemplo, por falta de remitente configurado), el
  resultado es una cuenta creada pero inactiva y un error 500 visible. El
  usuario existe, pero no puede entrar. La recuperación sin borrar nada:
  una vez configurado el correo, volver a registrar el mismo correo
  actualiza la cuenta inactiva y reenvía el enlace.
- **La URL pública del frontend no es localhost.** Si la URL del frontend
  queda con su valor por defecto local, los enlaces enviados por correo
  apuntan a localhost y no sirven a nadie. Hay que fijarla a la URL pública
  real de la app.
- **Correo con contraseña de aplicación.** El envío de correo se configura
  con una contraseña de aplicación de la cuenta de correo, no con la
  contraseña normal, y esa contraseña la introduce el usuario por el
  canal seguro, nunca por chat. El agente no la almacena, no la repite y
  no la pasa a ningún otro sitio.
- **FLASK_APP_KEY (clave secreta de la app).** Sin una clave secreta real,
  la app corre con un valor de respaldo inseguro. Hay que fijar una clave
  real antes de cualquier uso con usuarios reales, y ese paso queda
  reservado al usuario al final.
- **Cuenta de demostración como atajo.** Sembrar una cuenta de estudiante
  activa sirve como solución inmediata mientras se resuelve la
  configuración de correo, pero es un atajo, no la resolución.
- **Caso real que confirma la doctrina (26 oct 2026).** Blockali ya
  está vivo en PythonAnywhere: cuenta BC123, URL pública
  https://BC123.pythonanywhere.com. Es la primera demostración
  pública real del trabajo, y confirma en la práctica lo anterior:
  despliegue sin tarjeta, variables en el WSGI, y el error de
  registro (cuenta creada pero inactiva por falta de remitente de
  correo) que aquí se documenta.

## Runbook de despliegue (lecciones)

1. **Una sola fuente de dependencias.** Un manifiesto viejo junto a uno
   moderno rompe despliegues. Eliminar el viejo.
2. **Variables antes que código.** Revisar la lista completa de variables
   de entorno antes de desplegar, no después del primer error 500.
3. **Probar el flujo completo en la URL pública.** Registro, verificación
   por correo, inicio de sesión, flujo principal. Probar en local no
   prueba el despliegue.
4. **Verificar que no quedó ningún servidor de pruebas corriendo.** Los
   servidores de verificación local se detienen al terminar; un puerto
   ocupado por una verificación olvidada rompe la siguiente.
5. **Nunca prometer despliegue sin comprobar la sesión.** Si el despliegue
   necesita una cuenta o una sesión y no está disponible, se informa
   exactamente qué falta, no se improvisa una cuenta ni una autorización.
6. **Documentar el despliegue repetible.** Facturación, variables,
   migraciones, dominio, copias de seguridad y monitorización, por
   escrito, para poder repetirlo con un cliente y citarlo en una
   entrevista sin inventar experiencia.

## Manejo de archivos .env y secretos

- **Los secretos no van al chat, ni a archivos del proyecto, ni a
  informes.** Ni valores, ni fragmentos, ni versiones codificadas para
  disimularlos.
- **El usuario introduce sus propios valores al final,** con una guía
  paso a paso, por el canal seguro previsto para ello.
- **Un archivo .env de ejemplo** (con nombres de variables y valores
  falsos) sí pertenece al repositorio; el .env real, nunca.
- **Si un secreto aparece en un mensaje,** no se almacena, no se repite y
  no se reenvía. El trabajo continúa desde la sesión activa, no desde el
  texto del mensaje.
