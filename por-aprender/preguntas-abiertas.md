# Preguntas abiertas — Mundo Dirsi

> Preguntas que Dirsi todavía no puede responder con evidencia suficiente.
> Cada una lleva: la pregunta, por qué importa y cómo se resolverá
> (experimento, lectura de fuente oficial o pregunta directa al usuario).
> Regla: una pregunta se cierra solo con evidencia — un documento, una
> prueba ejecutada o una respuesta explícita del usuario —, nunca con una
> suposición que suene convincente. Las preguntas cerradas se mueven al
> registro con su evidencia, no se borran sin dejar rastro.

---

## 1. ¿Permiten las condiciones de la API directa de Moonshot entrenar otros modelos con las salidas de Kimi K3?

- **Por qué importa:** la ruta de destilación de diseño depende de
  generar un conjunto de datos con K3. Si sus términos lo prohíben,
  todo el plan cambia de proveedor o de enfoque antes de gastar nada.
- **Cómo resolverla:** lectura directa de los términos vigentes de la
  API de Moonshot (plataforma oficial, no resúmenes de terceros) y, si
  el texto es ambiguo, consulta escrita al soporte o revisión del
  apartado de uso de salidas con fecha de consulta anotada.

## 2. ¿Rechaza Render las tarjetas prepagas, como la virtual de Zinli, en su verificación?

- **Por qué importa:** si Zinli funciona, Render vuelve a ser viable
  para despliegues con base de datos permanente; si el procesador la
  rechaza por ser prepaga, hay que dejar de considerarlo y no hacer
  perder tiempo al usuario con intentos.
- **Cómo resolverla:** experimento controlado y barato: un solo intento
  de verificación con la tarjeta prepaga cuando el usuario lo autorice
  expresamente, anotando el resultado exacto (aceptada, rechazada con
  qué mensaje, o sin reacción). Un rechazo no cuesta nada más que ese
  intento; repetirlo sin cambiar nada no aporta información.

## 3. ¿Cuál es el mejor modelo gratuito para trabajo agéntico de código en el teléfono frente al portátil?

- **Por qué importa:** el teléfono es el entorno diario del usuario y
  el portátil el de calidad visual; usar el modelo equivocado en cada
  uno desperdicia el presupuesto semanal o entrega trabajo por debajo
  del estándar que él exige.
- **Cómo resolverla:** experimento comparativo con la misma tarea de
  código en ambos entornos (por ejemplo, construir una CLI pequeña y
  corregir un bug provocado), midiendo tiempo, número de intentos,
  calidad del resultado y consumo. La respuesta puede ser distinta por
  entorno y debe quedar escrita así, no como un único ganador.

## 4. ¿Existe un repositorio compartido entre Muse y Muse Code, o son productos separados sin código común público?

- **Por qué importa:** si existiera un repo compartido, seguir su
  desarrollo daría pistas directas sobre la dirección de ambas
  herramientas; si no existe, hay que dejar de buscarlo y tratar cada
  producto por sus canales oficiales.
- **Cómo resolverla:** búsqueda en las organizaciones oficiales de
  GitHub y en la documentación de ambos productos, anotando qué se
  encontró y qué no. Un resultado negativo documentado (dónde se buscó
  y cuándo) también cierra la pregunta.

## 5. ¿Cómo se verifica que una URL de demo en vivo pertenece realmente a un repositorio concreto?

- **Por qué importa:** presentar una demo como prueba de trabajo exige
  poder demostrar la cadena repo → despliegue → URL; sin esa cadena,
  una demo puede ser cualquier cosa y no sirve como prueba en una
  entrevista ni ante un cliente.
- **Cómo resolverla:** experimento con un despliegue propio: conectar
  un repo a un host, desplegar, cambiar una cadena visible en el repo,
  redesplegar y comprobar que el cambio aparece en la URL. Documentar
  además los indicios que NO prueban nada por sí solos (que la página
  exista, que el nombre coincida).

## 6. ¿Cuál es el alojamiento más barato y fiable para un cliente que necesita su app siempre funcionando?

- **Por qué importa:** el usuario teme que le pregunten por producción
  real y no quiere prometer un 100% imposible ni absorber un coste que
  debe pagar el cliente; necesita una cifra defendible con respaldo,
  copias de seguridad y monitorización.
- **Cómo resolverla:** lectura de precios y condiciones vigentes de
  los candidatos (nivel pago sin suspensión, base de datos con respaldo
  y dominio) y cálculo del coste mensual total para una app pequeña,
  comparado con lo que ya se sabe de los niveles gratuitos (suspensión,
  caducidad de la base de datos, falta de respaldos). La respuesta debe
  incluir qué se le cobra al cliente y qué cubre ese pago.

## 7. ¿Qué parte del trabajo de agente puede hacerse sin conexión y qué parte exige siempre un modelo en la nube?

- **Por qué importa:** define qué herramientas de Dirsi pueden
  funcionar en el teléfono sin internet o con un modelo local, y qué
  promesas no se pueden hacer sobre trabajo offline.
- **Cómo resolverla:** experimento: ejecutar las mismas tareas
  pequeñas (resumir un archivo local, buscar en notas, generar una
  plantilla) con un modelo local disponible y con un modelo en la nube,
  comparando calidad, velocidad y qué tareas fallan sin conexión.

## 8. ¿Cuándo conviene SQLite y cuándo Postgres en un proyecto real de cliente, en números y no por costumbre?

- **Por qué importa:** es la decisión de base de datos que más se
  repite y la que más cuesta corregir tarde; una regla escrita con
  umbrales evita migrar por pánico o quedarse corto por inercia.
- **Cómo resolverla:** experimento de carga controlado: la misma
  aplicación con escrituras concurrentes simuladas contra ambas bases,
  midiendo a partir de qué volumen aparecen errores o bloqueos en
  SQLite. El resultado alimenta la lista de decisión de la ruta de
  backend (ver `rutas.md`, Ruta 5, paso 4).

## 9. ¿Qué tan fiable es un agente que revisa su propio trabajo frente a uno revisado por un evaluador independiente?

- **Por qué importa:** si la auto-revisión bastara, los arneses de
  evaluación serían innecesarios; si no basta, todo proyecto serio
  necesita un evaluador separado, y eso cambia cómo se diseñan los
  flujos de Dirsi.
- **Cómo resolverla:** experimento: el mismo conjunto de tareas con
  errores provocados, evaluado primero por el propio agente y luego
  por un arnés con criterios escritos de antemano, comparando cuántos
  errores detecta cada uno. La diferencia medida, no opinada, responde
  la pregunta.

## 10. ¿Qué señales distinguen una ventaja cuántica real de una demostración de marketing?

- **Por qué importa:** el usuario sigue el tema cuántico y quiere
  separar hype de realidad; repetir una nota de prensa como hecho
  dañaría su credibilidad justo donde quiere construirla.
- **Cómo resolverla:** lectura de fuentes primarias (artículos
  revisados y documentación de los fabricantes) con una lista de
  verificación propia: problema definido, comparación con el mejor
  método clásico conocido, tamaño del problema y reproducibilidad.
  Cada noticia futura se pasa por esa lista antes de citarla.

## 11. ¿Qué nivel de calidad visual es alcanzable en el teléfono y a partir de qué punto hace falta el portátil?

- **Por qué importa:** el usuario trabaja casi siempre desde el
  teléfono pero exige calidad visual alta; saber dónde está el límite
  real evita prometer en el teléfono lo que solo sale bien en el
  portátil, y viceversa.
- **Cómo resolverla:** experimento: la misma pieza de diseño
  (una landing pequeña) producida con el flujo de teléfono y con el
  flujo de portátil/Dirsi, comparada por criterios escritos (jerarquía,
  espaciado, contraste, coherencia) y por tiempo invertido.

## 12. ¿Qué datos de un proyecto conviene que Dirsi recuerde entre sesiones y cuáles deben pedirse siempre de nuevo?

- **Por qué importa:** recordar demasiado genera respuestas que
  parecen personalizadas pero usan datos viejos; recordar demasiado
  poco obliga al usuario a repetir lo mismo en cada sesión, que es
  justo lo que le cuesta.
- **Cómo resolverla:** pregunta directa al usuario con ejemplos
  concretos (preferencias de diseño, decisiones de despliegue, datos
  del proyecto) más una revisión de los errores pasados causados por
  usar un dato desactualizado. La respuesta se escribe como una lista
  de qué se guarda, qué caduca y qué se confirma siempre.

## 13. ¿Cuál es el flujo más simple y seguro para que el usuario entregue sus archivos (fotos, documentos) sin el límite de 10 por mensaje?

- **Por qué importa:** hay material pendiente (por ejemplo, fotos
  personales) que no cabe en el chat y cuyo manejo debe ser cómodo y
  seguro, no un proceso que se abandona a medias.
- **Cómo resolverla:** experimento con las herramientas ya conectadas
  (carpetas compartidas en la nube) en un caso pequeño y no sensible,
  midiendo pasos, tiempo y qué permisos pide cada opción. Solo después
  se propone el flujo para material sensible.

## 14. ¿Qué métrica resume mejor "esta demo está lista para enseñar" sin depender de la opinión de quien la hizo?

- **Por qué importa:** el estándar del usuario es "lo mejor de lo
  mejor", y sin un criterio medible cada demo puede declararse lista
  por entusiasmo o retrasarse indefinidamente por perfeccionismo.
- **Cómo resolverla:** lectura y prueba: aplicar una lista de
  verificación fija (flujo principal completo sin errores, datos de
  ejemplo coherentes, rendimiento aceptable, textos sin errores,
  funcionamiento en móvil) a tres demos ya construidas y ver si la
  lista distingue la que está lista de la que no. Ajustar la lista
  hasta que lo haga.

---

## Cómo se cierra una pregunta

1. Anotar la evidencia (enlace oficial con fecha, salida de un
   experimento o respuesta literal del usuario).
2. Escribir la respuesta en una línea en el registro, con su fecha.
3. Si la evidencia contradice algo ya construido (una ruta, una demo,
   una recomendación), actualizar ese archivo también: una pregunta
   cerrada que no cambia nada es solo una nota.

## Preguntas aparcadas deliberadamente

- Cualquier pregunta sobre sistemas de trading automatizado queda
  aparcada hasta que el usuario defina la fuente de señal y el motor
  de ejecución: sin eso no hay experimento honesto que hacer.
- Cualquier pregunta que exija una cuenta nueva, un pago o un permiso
  OAuth nuevo queda aparcada hasta autorización explícita del usuario:
  se formula aquí, pero no se ejecuta sola.
