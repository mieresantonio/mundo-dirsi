# Agentes e IA — lo aprendido

## Agentes de código: qué son en la práctica

Un agente de código no es un autocompletado con más texto: es un programa
que lee archivos, ejecuta comandos, escribe código, comprueba el resultado y
corrige sus propios errores en bucle. Su valor está en ejecutar trabajo
largo y verificable sin que el usuario tenga que vigilar cada paso. Su
límite está en lo mismo: sin verificación (compilar, correr el flujo real,
comparar contra lo esperado) produce trabajo que parece terminado y no lo
está.

## Modelos: tamaño, calidad y honestidad

- **La calidad del modelo se nota en diseño.** Comparando salidas, los
  modelos pequeños gratuitos decepcionan en trabajo visual y de diseño,
  mientras que los modelos grandes producen resultados claramente mejores.
  Para tareas de aprendizaje y texto rápido un modelo pequeño basta; para
  diseño y arquitectura, no.
- **Ningún modelo gratuito es "ilimitado".** Todo proveedor gratuito tiene
  cuotas. La promesa de "sin límites" en videos y anuncios es marketing,
  no una especificación. La economía honesta se mide en cuotas por
  proveedor, no en titulares.
- **Un modelo pequeño no supera automáticamente a otro por ser nuevo.**
  Antes de cambiar de modelo para una tarea de agente, hay que comparar
  contra lo que ya funciona (por ejemplo, un modelo de código pequeño que
  ya rinde bien en el flujo real). La novedad no es una métrica.

## FreeLLMAPI: el router local

FreeLLMAPI es un proyecto open-source (licencia MIT) que corre en la propia
máquina del usuario, no una nube con claves compartidas:

- Reúne las claves gratuitas del usuario (Groq, Cerebras, Google AI Studio,
  Mistral, OpenRouter, Cohere, Z.ai, NVIDIA, HuggingFace, OpenCode Zen,
  entre otros) detrás de un solo endpoint compatible con la API de OpenAI
  en local.
- Cuando un proveedor se queda sin cuota, el router cambia solo al
  siguiente: su valor real es amplitud de catálogo más failover automático
  a mitad de tarea, no un modelo mágico.
- Las claves quedan cifradas (AES-256-GCM) en la propia base de datos local
  del usuario. Ningún tercero las ve. El proyecto se declara para
  experimentación personal, no para producción.
- La versión gratuita usa una foto mensual del catálogo (los modelos nuevos
  llegan con retraso); la versión de pago solo adelanta ese catálogo.
- Se conecta a OpenCode de forma oficial, con un comando de configuración
  que primero muestra la diferencia y hace copia de seguridad antes de
  modificar la configuración existente, sin pisar los proveedores ya
  definidos.
- Decisión tomada: instalarlo en el portátil, no en el teléfono, cuando el
  usuario se siente frente a él.

## Destilación y Kimi K3: verificado frente a hype

- **Verificado:** los pesos de Kimi K3 pesan alrededor de 1,56 TB y están
  publicados en Hugging Face bajo la cuenta de Moonshot. Su licencia no
  restringe entrenar otros modelos con las salidas de K3, salvo un umbral
  de ingresos (por encima de cierta facturación anual se aplica una puerta
  de pago por uso del servicio).
- **Verificado:** otros proveedores sí lo prohíben. Los términos de
  Databricks, por ejemplo, vetan entrenar modelos con sus salidas: nunca
  generar datos de destilación a través de Databricks.
- **Sin confirmar:** los términos del acceso directo a la API de Moonshot
  sobre entrenar con sus salidas. Hay que comprobarlos antes de generar
  nada por esa vía.
- **La ruta viable es destilación de caja negra:** generar un conjunto de
  datos de diseño con la API de K3, y entrenar con ajuste eficiente (por
  ejemplo QLoRA sobre un modelo abierto de tamaño manejable) en recursos
  gratuitos de nube con GPU. Sin GPU local, la máquina propia solo sirve
  para orquestar, no para entrenar.
- **Material público existente no sustituye al proyecto.** Hay conjuntos
  públicos de destilación de K3, pero son mayoritariamente de otros modelos
  y de matemáticas o razonamiento formal, sin contenido de diseño o
  frontend. No reemplazan un conjunto propio orientado a diseño.
- **Hype que hay que descontar:** cualquier cifra de "rendimiento" o
  "capacidad" que venga de un video o un anuncio sin fuente primaria es
  una afirmación del creador, no un hecho. La clasificación de evidencia
  (demostrado, secundario estable, afirmación del creador, retirado) se
  aplica también aquí.

## Teléfono (Termux + OpenCode) frente a portátil

- **Teléfono:** OpenCode corre en Termux (instalado desde F-Droid, sin
  mezclar tiendas de apps) y sirve para aprender, hacer ediciones rápidas
  y tareas de texto o código ligero. Los modelos gratuitos disponibles por
  esa vía (a través de OpenRouter con clave propia) cubren bien ese uso.
  **OpenCode Zen NO está disponible en el teléfono:** la build instalada
  es la 1.17.9 y Zen exige 1.18.0 o superior, así que esa vía queda
  bloqueada en el teléfono (en el portátil, con la build oficial
  actual, sí debería funcionar). Limitaciones reales: pantalla pequeña
  para diseño visual, batería y permisos del sistema (hay que mantener
  el proceso despierto y sin restricciones de batería), y la ausencia
  de GPU.
- **Portátil:** es donde van el trabajo visual exigente, los despliegues
  con pasos manuales, la instalación de herramientas de escritorio y
  cualquier entrenamiento o proceso pesado. La regla práctica: diseño y
  demostraciones exigentes, en el agente grande o en el portátil; el
  teléfono, para aprender y para cambios rápidos.
- **Un error conocido del teléfono:** un modelo que no está en el catálogo
  del proveedor instalado produce errores persistentes de "modelo no
  encontrado" aunque se defina en la configuración y se limpie la caché.
  La solución no es insistir en la configuración, sino elegir un modelo
  que el proveedor realmente sirva.

## Addendum 27 oct 2026 — Kimi K3.1 Pro

- **Kimi K3.1 Pro** (Moonshot, lanzado el 23 oct 2026): post-entrenamiento
  de K3, mismo tamaño (2.8T de parámetros, 104B activos), 1M de contexto,
  texto e imagen. Artificial Analysis: índice 55, 4º del mundo (K3: 44).
  En diseño y frontend puro no hay medida nueva: no asumir que diseña
  mejor en proporción a su mejora en tareas agénticas.
- **Pesos el 4 nov 2026; licencia SIN publicar.** Comprobado en la
  organización de Moonshot en Hugging Face el 27 oct: todavía no hay
  K3.1 publicado. No asumir que hereda la licencia de K3: el paso 0
  de la PoC de destilación (licencia + términos de la API sobre
  entrenar con salidas) se repite para K3.1 antes de generar nada.
- **API más barata que K3:** 2 dólares de entrada y 10 de salida por
  millón de tokens (33 % menos), lo que abarataría el presupuesto de
  la PoC si se mantiene la ruta de destilación de caja negra.
