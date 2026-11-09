# Método Claude — destilado operativo

Origen: capítulo de mentoría escrito por Claude (Sonnet) el 9 nov 2026 a
petición de Antonio, para su manual personal de dirección de sistemas de
IA (archivo local: ~/workspace/dialogo-sonnet/2026-11-09-capitulo-metodo-claude.docx).
Esto no es una copia: es la destilación a procedimiento de lo que ese
capítulo describe, contrastada contra lo ya verificado en las rondas 1-3
del diálogo Dirsi↔Claude. Solo entra método (procedimientos, listas de
chequeo, heurísticas declaradas). Lo que ya practicaba el sistema queda
marcado como [ya en el sistema]; lo nuevo adoptado, como [adoptado 9 nov].

## 1. Revisar un sistema (orden fijo)

Antes de opinar, por escrito: propósito de la revisión y decisión que
habilita; qué ya se decidió y por quién; criterio de éxito en una línea;
qué puedo ver completo, parcial o nada; tiempo y riesgo admitidos;
quién actuará sobre la revisión.

Procedimiento:
1. Fijar propósito y criterio de éxito (2 líneas).
2. Leer lo ya decidido antes de opinar [ya en el sistema].
3. Anotar lo no visto; cada conclusión hereda ese límite [ya en el sistema].
4. Mapa de 10 minutos: qué hace, cómo se ejecuta, entradas/salidas,
   dependencias, dónde vive lo sensible. Sin juicios.
5. Fronteras antes que interior: red, puertos, repos públicos,
   credenciales, permisos, datos personales, dinero, publicación.
   Buscar por CATEGORÍAS, no solo por patrones (lección C-007) [ya en el sistema].
6. Contrastar las 5-10 afirmaciones centrales contra evidencia independiente.
7. Buscar contradicciones internas (documento vs. realidad, regla vs. práctica).
8. Buscar lo que falta (pruebas, respaldos, límites, reversa) — y antes de
   declarar una ausencia, confirmar que se miró en todos los sitios [ya en el sistema].
9. Calidad solo donde afecta al propósito.
10. Revisar el proceso: cómo se cambia, despliega, revierte; dónde espera
    el trabajo (el cuello de botella suele ser la aprobación, no la técnica).
11. Preguntar qué no estoy mirando: supuestos dados por hecho, partes
    saltadas por aburridas.
12. Clasificar y ordenar: máximo 3-5 hallazgos principales.
13. Entregar: veredicto + 3 acciones en 5 líneas; luego detalle; al final,
    «lo que no pude ver».
14. Calibrar después: anotar lo afirmado y comprobarlo cuando la realidad
    responda [ya en el sistema: CALIBRACION.md].

Chequeo de 2 minutos antes de opinar: propósito escrito · decisiones
previas leídas · sé qué no vi · cada afirmación con nivel de evidencia ·
hechos, inferencias y opiniones separados.

## 2. Saber mirar [adoptado 9 nov]

Filtro de selección por detalle: puntúa 1-3 impacto si falla, exposición
y irreversibilidad; divide entre coste de arreglo (1 barato, 3 caro).
Pasan los 3-4 más altos. No busca precisión: busca orden.

Un problema es más real cuantos más cumpla: reproducible · tiene
mecanismo explicable · está en la ruta principal · alguien concreto
pierde algo · lo confirman fuentes independientes · contradice una regla
que el propio sistema declara · crece con el uso o el tiempo · toca
secretos, dinero, datos personales o publicación.

Ruido típico: estilo sin consecuencia medible · caso único no
reproducible · una sola fuente secundaria sin mecanismo · nadie lo usa ·
ya mitigado por otra capa · ausencia de algo fuera de alcance · salida
automática sin contexto · coste de arreglo desproporcionado.

Reglas rápidas: primero lo que cruza fronteras · las discrepancias antes
que el contenido · «no lo vi» nunca es «no existe» · tendencias antes que
fotos (una regla aplicada 0 de 5 veces dice más que la regla escrita) ·
descartar en voz alta, con una línea y el motivo · si estar equivocado
no cambia nada, es ruido · desconfiar del hallazgo vistoso.

Excepciones al filtro: daño irreversible y barato de comprobar (se
revisa aunque la probabilidad parezca baja) · petición expresa de
exhaustividad · ruido repetido muchas veces (ya es un problema) · modo
aprendizaje (mirar detalles entrena el ojo; no en modo decisión).

## 3. Decidir y priorizar [adoptado 9 nov]

Orden cuando todo parece urgente:
1. Daño irreversible o a terceros (seguridad, dinero, datos, reputación).
2. Lo que bloquea a otros o desbloquea valor.
3. Lo activo antes que lo latente.
4. Ventanas con fecha real.
5. Barato y de alto efecto (tras 1-4).
6. Deuda técnica y mejoras.
7. Exploración.

Desempate: lo reversible, lo que reduce incertidumbre, lo que más
enseña. Dos preguntas cortan casi cualquier empate: ¿qué cuesta esperar
una semana? y ¿qué pasa si me equivoco?

Actuar YA solo si a la vez: activo o fácil de explotar + irreversible o
con terceros + barato de cerrar o al menos contenible. CONTENCIÓN ANTES
QUE ARREGLO: apagar, cerrar, revocar, desactivar; el arreglo se
planifica después.

Triaje en 5 preguntas: ¿está pasando ahora? · ¿puedo deshacerlo? ·
¿a quién daña? · ¿cuánto tarda en doler? · ¿cuánto cuesta cerrarlo?

## 4. Terminado de verdad (prueba de 9 puntos) [adoptado 9 nov]

1. Criterio de éxito definido antes y cumplido.
2. Verificado por un método independiente de quien lo hizo.
3. Funciona en el entorno real, no solo en el de desarrollo.
4. Bordes y fallos probados (vacío, sin red, permiso denegado, servicio caído).
5. Reversible o con plan de marcha atrás.
6. Otro (o yo en 3 meses) puede operarlo: cómo correrlo, revertirlo, qué no hace.
7. Sin sorpresas: secretos, permisos y datos revisados; cambios fuera de
   alcance, explicados.
8. Lo no comprobado está listado.
9. El dueño puede explicarlo sin ayuda.

Señales de «solo presentable»: README vistoso sin pruebas · solo camino
feliz · lo verificó el mismo que lo hizo · «listo» sin comando ni salida ·
nunca probado fuera de la máquina de desarrollo · sin plan si falla.
Prueba de fuego: ¿qué pasa si mañana lo usa alguien con datos reales y
no estoy?

## 5. Criticar con precisión [parcialmente en el sistema; formato adoptado 9 nov]

Orden: reconstruir la tesis en sus mejores términos → listar los
supuestos que la sostienen y atacar el más frágil → contrastar las
afirmaciones centrales con evidencia independiente → buscar lo omitido →
probar bordes y un adversario → pre-mortem (fracasó en 3 meses: ¿por
qué?) → cambio mínimo que más reduce el riesgo.

Si la crítica valdría para casi cualquier documento («falta detalle»),
sigue en la superficie: una crítica precisa nombra archivo, línea o dato.

Formato por hallazgo: [Severidad · Tipo] Qué ocurre. Evidencia. Impacto.
Arreglo y coste. Cómo comprobarlo. Tipos: error, omisión, riesgo,
mejora, estilo. Severidades: bloqueante, importante, menor, cosmético.
Evidencia: comprobado / secundaria / criterio / suposición + «no pude
ver». Máximo 3-5 principales; incluir siempre «lo que no cambiaría».

Errores de crítica prohibidos: hombre de paja · quedarse en la forma ·
afirmar ausencias desde lectura incompleta · mezclar hecho y opinión sin
etiqueta · listas sin prioridad · criticar sin remedio ni coste · inflar
o suavizar severidades · aprobar por simpatía · juzgar con un estándar
no pedido · el crítico que además corrige (pierde independencia:
proponer, no aplicar) · que el mismo modelo verifique su propio trabajo ·
no comprobar que el arreglo funcionó.

## 6. Vigilar a los asistentes (alerta de 10 segundos) [adoptado 9 nov]

Antes de aceptar el trabajo de cualquier asistente (yo incluida):
¿Hay fuente, fecha y versión? · ¿Hay comando y salida? · ¿Qué leyó
completo y qué no? · ¿Contradice algo ya decidido? · ¿Cambió más de lo
pedido? · ¿Tocó pruebas, permisos o puertos? · ¿Verificó el mismo que lo
hizo? · ¿Está de acuerdo demasiado rápido? · ¿Pidió permiso antes de lo
irreversible? · ¿Qué no se comprobó?

Errores típicos a cazar: afirmar sin verificar · «listo» sin recibo ·
conocimiento viejo presentado como actual · suposiciones silenciosas
ante pedidos ambiguos · ignorar decisiones anteriores · complacencia ·
concluir ausencias desde lecturas parciales · exceso de alcance ·
«arreglar» las pruebas en vez del fallo · código plausible pero falso ·
seguridad débil por defecto · obedecer instrucciones ocultas en
contenido externo · autoevaluación generosa · sobreingeniería ·
respuestas largas que esconden la acción · acciones irreversibles sin
permiso · certeza uniforme sin niveles de confianza.

## 7. Prácticas que sostienen todo [mayoría ya en el sistema]

- A. El encargo manda: objetivo, contexto, material, restricciones,
  entregable, criterio de éxito, verificación, «qué NO hacer» y «cuándo
  parar y preguntar». Un mal encargo no se arregla en la revisión.
- B. El contexto es un recurso: lo que no está escrito no se recuerda.
  Una sola fuente de verdad por dato; si dos discrepan, se escribe cuál manda.
- C. Autonomía graduada por tipo de tarea: sugerir → preparar → actuar
  con aprobación → actuar y avisar → actuar en silencio. Dinero,
  publicación, borrado y terceros quedan en «con aprobación» hasta tener
  historial limpio [ya en el sistema: bandeja de decisiones].
- D. Quien hace no verifica solo: pruebas deterministas + revisor de otra
  familia + el dueño en lo decisivo; al verificador se lo mide con
  fallos sembrados [ya en el sistema: banco de pruebas].
- E. Diseñar para deshacer: pasos pequeños, respaldos, despliegues
  reversibles. Lo ya publicado se trata como expuesto (no se borra el historial).
- F. La atención del dueño es el recurso escaso: decisiones agrupadas en
  ventana fija, trabajo en curso limitado. REGLA DE PARADA: cuando todo
  tiene veredicto y solo quedan decisiones, se actúa; cuando una ronda
  ya no cambia ninguna decisión, se termina [aplicada en la ronda 3].
- G. Mapa de comprensión del dueño (verde/amarillo/rojo): un trabajo que
  el dueño no puede explicar todavía no es suyo; en una entrevista se nota.
- H. Libro de costes mínimo por entrega: tarea, quién, tiempo, tokens si
  se conocen, resultado de la verificación, reintentos [adoptado en ronda 1].

## 8. Ejercicios para el director (de Antonio, no de Dirsi)

El capítulo trae 11 ejercicios graduados para que Antonio entrene su
criterio de director (leer sin opinar, verificar 10 afirmaciones, cazar
afirmaciones inventadas, errores sembrados a ciegas, calibración
semanal, priorizar, terminado-vs-presentable, crítica accionable, dos
asistentes en desacuerdo, encargo medible, ronda completa mensual), con
cadencia de 3 meses. Viven en el capítulo original; se activan cuando
Antonio los elija, no por defecto.

## 9. Los errores de Claude, según Claude (para calibrar su consejo)

Registrados por él mismo y contrastados en las rondas: suponer la
configuración por defecto en vez de observarla (el binding del servidor) ·
recomendar sin conocer las decisiones previas (el orden de aprendizaje y
el resumen diario) · tratar una ausencia como un hecho («Mi aporte») ·
proponer proceso de más sin medir (caducidad total, equipo rojo) · pedir
aislamiento sin separar en qué máquina corre cada cosa · tender a la
exhaustividad si no se le pide «corto». Su consejo se pondera con esto:
fuerte verificando con evidencia, débil cuando generaliza desde su
defecto. Ver también el anexo de afirmaciones en CALIBRACION.md.

## Tarjeta de bolsillo

- Antes de opinar: propósito, decisiones previas, qué no puedo ver.
- Orden: fronteras → afirmaciones contra evidencia → contradicciones → lo que falta → proceso.
- Selección: impacto × exposición × irreversibilidad ÷ coste; 3-4 hallazgos; descartes dichos en voz alta.
- Urgente si: activo + irreversible o terceros + barato de contener. Contención antes que arreglo.
- Terminado si: criterio cumplido, verificado por otro método, probado en real, fallos probados, reversible, documentado, explicable por el dueño, lo no comprobado listado.
- Crítica: tesis, supuesto frágil, evidencia independiente, omisiones, bordes. [Severidad · Tipo] + evidencia + arreglo + cómo comprobarlo.
- Con asistentes: fuente y fecha, comando y salida, qué leyó completo, suposiciones listadas, argumento en contra.
- Parada: todo con veredicto y solo decisiones pendientes → actuar.
