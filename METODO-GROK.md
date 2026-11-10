# Método Grok — destilado operativo

Origen: «Cuaderno de dirección», capítulo escrito por Grok el 9 nov 2026
a petición de Antonio, para el mismo manual personal de dirección que
motivó METODO-CLAUDE.md (archivo local del capítulo:
~/workspace/capitulo-grok/2026-11-09-cuaderno-de-direccion-grok.md; la
app que lo acompaña está destilada en
~/workspace/capitulo-grok/DESTILADO-APP-CUADERNO.md y reconstruida en
~/workspace/capitulo-grok/app-cuaderno/).

Esto no es una copia: es la destilación a procedimiento, con redacción
propia, contrastada contra METODO-CLAUDE.md y contra lo que el sistema
ya practica. Lo que ya estaba queda marcado [ya en el sistema]; lo nuevo
adoptado, [adoptado 10 nov]. Donde Grok y Claude ofrecen dos
instrumentos para lo mismo, se dice cuál usar en cada caso en vez de
fusionarlos en silencio.

Advertencia de origen, declarada por el propio Grok en su sección 06:
escribió sin tener delante el registro literal de las rondas anteriores
y se negó a inventar citas de aquellas charlas. Su capítulo es método
declarado por un modelo sobre su forma de trabajar, no evidencia de
rondas reales; se pondera igual que el de Claude: fuerte como
procedimiento, débil como testimonio.

## 1. Revisar un sistema (orden de 9 pasos, centrado en comportamiento)

El orden de Claude (METODO-CLAUDE §1) manda cuando la revisión es de
evidencia y riesgo: fronteras, afirmaciones, contradicciones. El de
Grok manda cuando la revisión es de un sistema que corre y hay que
saber si cumple: primero el comportamiento observable, la estructura al
final.

1. Encargo en una frase antes de abrir nada: resultado observable, para
   quién, y una exclusión explícita. Sin frase no hay revisión, hay paseo.
2. Contrato externo antes que código: qué se prometió que entra y qué
   sale; entradas reales, salidas observables, restricciones.
3. ¿Vive? Un camino de arranque de punta a punta con el artefacto que
   verá el usuario. Si no arranca, el diagnóstico es el arranque.
4. El flujo real con tres datos: vacío, típico y malformado. Recién aquí
   se opina, y solo de este flujo: ¿se completa, se pierde, o finge que
   se completó?
5. Fronteras antes que interiores: entrada, API, persistencia,
   identidad, permisos, secretos, borrado, errores hacia afuera [ya en
   el sistema].
6. La verdad de los datos: dónde se guarda, qué se pierde al recargar,
   quién escribe qué; el invariante nombrado en una línea. Si nadie lo
   escribió, se asume violado en algún camino.
7. Provocar los fallos baratos: doble envío, recarga a mitad, permiso
   ausente, red cortada, id de otro, lista vacía. Por cada uno: ¿el error
   se muestra, se traga o se disfraza de éxito?
8. Estructura al final: nombres, módulos, duplicación, tests. Dice cuánto
   costará el próximo cambio, no si hoy es correcto.
9. Verificar la afirmación más fuerte del autor reproduciéndola en el
   artefacto final, no en el entorno de trabajo [ya en el sistema].

Reglas de contención de la revisión: no opinar antes del paso 4; no
proponer refactors antes del paso 9; el resumen del autor nunca es
fuente [ya en el sistema].

Cuatro preguntas antes de opinar [adoptado 10 nov]: ¿miro el sistema
que corre o el que el texto describe? · ¿qué reproduje yo y qué estoy
repitiendo del parte? · ¿cuál es el peor fallo compatible con lo visto?
· ¿este comentario cambia la decisión de quien encargó la revisión?

## 2. Saber mirar: la regla del daño (filtro rápido) [adoptado 10 nov]

Un detalle merece atención solo si toca al menos uno de cuatro ejes:
- Corrección: el resultado es falso o incompleto respecto a la frase
  del encargo (no respecto al gusto del revisor).
- Datos: alguien ve, pierde, altera o mezcla lo que no debe.
- Bloqueo: el siguiente paso del proyecto no puede ocurrir (no arranca,
  no se verifica, no se despliega).
- Reversión: arreglarlo después cuesta un orden de magnitud más
  (esquema poblado, contrato público, migración, secreto filtrado).

Si no toca ningún eje, es ruido por ahora y se anota sin discutirlo.

Procedimiento de bajada, con reloj: ocho minutos para listar hasta diez
detalles en bruto; tachar los que no tocan ningún eje; quedarse con lo
que un uso real encuentra en dos minutos más lo que encuentra un
despliegue o un id ajeno; escribir cada superviviente como síntoma
observable → causa probable → prueba que lo confirmaría. Sin prueba
escribible no hay hallazgo, hay sospecha, y las sospechas no se ordenan
como trabajo.

Señales de problema real (resumen): se repite en más de un camino · el
sistema afirma éxito y el artefacto dice lo contrario · está en una
frontera · no hay forma barata de verlo después · el autor no puede
señalar el archivo y el símbolo que sostienen su afirmación.
Señales de ruido: preferencia de nombre o estructura sin cambio de
comportamiento · optimizar lo que no se mide · casos que exigen un
estado que el producto no puede producir · deuda cosmética en código
que se borrará en la misma sesión.

Cuándo NO aplicar la regla: cuando el detalle pequeño es la única pista
de un fallo grande (un céntimo, una zona horaria, un operador en una
comparación de permiso) · cuando la corrección ya está demostrada y el
trabajo es el pulido final · cuando el «ruido» es una convención del
repo cuya ruptura hace ilegible el próximo cambio de cualquiera ·
cuando se está enseñando y el detalle es el ejercicio.

**Qué filtro usar, el de Grok o el de Claude.** El puntaje de Claude
(impacto × exposición × irreversibilidad ÷ coste) ordena mejor cuando
hay muchos candidatos y la decisión es cara o quedará registrada:
produce un orden defendible y comparable entre sesiones. La regla del
daño no ordena: descarta. Es más rápida y sirve en caliente, durante
una revisión o una entrega, cuando lo que sobra es ruido y lo que falta
es tiempo. Práctica adoptada: regla del daño para el primer corte en
vivo; puntaje de Claude para cerrar la lista de hallazgos principales.

## 3. Decidir y priorizar: clases P0–P3 [adoptado 10 nov]

Clasificar primero, desempatar dentro de la clase por daño visible,
después por lo que bloquea más trabajo, al final por lo que se cierra
en minutos.

- P0 · ahora: fuga o pérdida de datos, secreto expuesto, acción
  destructiva sin dueño, camino principal incompletable, o una
  afirmación de «terminado» falsa con alguien a punto de decidir sobre
  ella (publicar, cobrar, migrar).
- P1 · este ciclo: el flujo principal solo existe en el caso feliz; la
  interfaz declara éxito y el servidor falló; el requisito central no
  se puede verificar.
- P2 · después: bordes que el dominio sí produce (duplicados, vacío,
  nombres largos, reconexión) y deuda del módulo que se tocará en el
  próximo cambio.
- P3 · si sobra: estética, renombres, abstracciones preventivas, tests
  de código que no guarda ningún invariante. Si el encargo era pulir,
  P3 sube: el encargo manda sobre la escala.

Acción inmediata si el fallo ocurre con uso normal o input trivial, el
daño no se deshace fácil y nadie lo verá hasta tarde; basta la primera
condición cuando el daño ya es grave. Contención antes que arreglo
[ya en el sistema]. Lo que puede esperar se escribe con fecha o con
disparo medible; «luego» sin disparo es abandono disfrazado. Esto
complementa el orden de prioridad de Claude (METODO-CLAUDE §3): aquel
ordena entre frentes distintos; esta escala clasifica hallazgos dentro
de un mismo frente.

## 4. Criticar con precisión: la viga y las cuatro clases

Método: pedir la frase del encargo (si el trabajo no la declara, esa
ausencia es el primer hallazgo) → ignorar la prosa y subrayar solo las
afirmaciones fuertes → elegir la viga, la afirmación de la que depende
el resto → intentar falsarla con el caso más barato (vacío, id ajeno,
doble envío, recarga, sin permiso, artefacto final), un solo intento →
si no cae, mirar si el caso feliz depende de un mock, un dato sembrado
a mano o un servicio que el usuario real no tiene. Crítica que no
nombra comportamiento, frase citada o archivo no es crítica: es
opinión, se dice una vez y no se mezcla con los hallazgos [en el
sistema en esencia; formulación adoptada 10 nov].

Cuatro clases de hallazgo, y ninguna más [adoptado 10 nov]:
- Bloquea: no se puede dar por bueno el encargo hasta corregirlo.
  Obligatorio: cómo se reproduce.
- Riesgo: el encargo de hoy se cumple, pero hay fallo probable con
  daño. Obligatorio: disparo, y qué se hace ahora (contener, anotar o
  ignorar con fecha).
- Deuda: costará más cambiarlo después. Solo se pide si esa zona se
  tocará pronto; si no, se anota y no se discute.
- Gusto: no cambia el comportamiento. Se dice una vez como preferencia
  y no se insiste; mezclar gusto con bloquea destruye la credibilidad
  del próximo bloqueo.

Formato de hallazgo, ocho líneas o menos [adoptado 10 nov]: Observado
(qué se ve) · Esperado (qué exigía la frase del encargo) · Prueba (cómo
se reprodujo, o qué falta para reproducirlo) · Clase · Acción mínima
(el cambio más pequeño que lo cierra, no el rediseño deseado).

Relación con el formato de Claude ([Severidad · Tipo] + evidencia +
impacto + arreglo + cómo comprobarlo): el de Grok es el formato corto
para revisiones en vivo y entregas rápidas; el de Claude queda para
informes que se guardan y se calibran. Los dos exigen prueba y acción
mínima; ninguno admite adjetivos sin evidencia.

Errores de crítica que este capítulo añade a los ya prohibidos:
criticar el camino no tomado cuando el tomado cumple el encargo ·
reescribir el trabajo ajeno como forma de crítica (eso es otro
encargo) · aceptar un «ya lo contemplé» como sustituto de la prueba ·
pedir en la revisión lo que no estaba en el encargo y tratar la
ausencia como defecto (eso es un cambio de encargo y se negocia aparte).

## 5. Terminado de verdad (lista corta de 7 casillas)

Versión rápida de la prueba de 9 puntos de Claude (METODO-CLAUDE §4);
misma doctrina, menos fricción para entregas frecuentes. Todas las
casillas, no la mayoría:

- [ ] La frase del encargo se cumple, no una frase vecina más lucida.
- [ ] El camino principal se recorrió con dato vacío, típico y malformado.
- [ ] Vacío, error y carga existen, y ninguno miente éxito.
- [ ] Se miró el artefacto final, no solo el entorno de trabajo.
- [ ] Una afirmación no trivial se reprodujo; no se creyó.
- [ ] Lo que quedó fuera está escrito, sin disfraz de «mejora futura».
- [ ] Quien opera puede ver en treinta segundos que algo se rompió
      (un test, un log o una mirada concreta).

Si faltan la cuarta o la quinta, no está terminado: está narrado.
Definición operativa [adoptado 10 nov]: presentable es que se ve bien
en el caso que el autor eligió mostrar; terminado es que un tercero,
sin el autor al lado, cumple la frase del encargo con un uso razonable
sin romper el invariante central.

## 6. Pase de dos minutos al recibir cada entrega [adoptado 10 nov]

Complemento operativo de la alerta de 10 segundos de Claude
(METODO-CLAUDE §6): aquella vigila al asistente; este pase vigila la
entrega concreta, y si fallan la primera o la cuarta casilla no se
pasa a la siguiente pieza.

- [ ] Hay frase de encargo y el entregable la cumple tal cual.
- [ ] Abrí yo la afirmación fuerte; no me la creí.
- [ ] Existen el caso vacío y el caso sin permiso.
- [ ] Cada archivo nuevo estaba en el encargo, o lo rechacé.
- [ ] El «listo» distingue el entorno de trabajo del artefacto final.

## 7. Vigilar a los asistentes: tres fallos nuevos para la lista

La alerta de 10 segundos y el catálogo de errores de Claude
(METODO-CLAUDE §6) ya cubren la mayoría de los que Grok enumera
(cierre sin verificación, caso feliz como todo el sistema, alcance
inflado, parche del síntoma, parte más limpio que el diff, limpieza
como avance, ejemplo vendido como hecho, arreglar lo sano). Tres
entran como nuevos [adoptado 10 nov]:

- **Permiso dibujado.** Esconder un botón o filtrar en el cliente y
  llamarlo autorización; creer el id que manda el navegador. La
  comprobación de permiso vive donde se guarda el dato, no donde se
  dibuja la interfaz. Señal: pedir la comprobación del lado del dato.
- **Tests que no pueden fallar.** Afirman el mock o repiten la
  implementación línea a línea. Señal: preguntar qué bug concreto
  haría fallar ese test; sin respuesta, el test es decorado.
- **Símbolos inventados.** Importar lo que no existe, citar una función
  con la firma equivocada, describir una ruta que el árbol no tiene.
  Señal: abrir el archivo citado; cita sin ruta y sin símbolo se trata
  como no escrita. (El sistema ya cazaba «código plausible pero falso»;
  esta es su forma verificable en diez segundos.)

## 8. El registro mínimo: tres textos, una ficha, una pregunta

Aporte central del capítulo, sin equivalente en el de Claude.

**Tres textos que no se mezclan** [adoptado 10 nov]. En todo encargo
hay tres documentos distintos: el encargo (lo que debe ser verdad; se
escribe antes y no se reescribe en silencio para que encaje con lo que
salió), el plan (lo que se va a hacer; no es evidencia de nada) y el
parte (lo que se afirma haber hecho; tampoco es evidencia: evidencia
es el artefacto sometido a la prueba de cierre escrita antes). El
error caro es aceptar un parte como si fuera el encargo cumplido;
cuando parte y encargo no coinciden, manda el encargo y el hueco se
escribe en «quedó fuera», no se disimula. El sistema ya separaba
encargo y parte en la práctica (órdenes de Antonio vs. informes de
agentes); la adopción es nombrar el plan como tercer texto sin valor
probatorio y aplicar la regla de no-mezcla también a los planes.

**Ficha de sesión: cinco líneas al encargar, cinco al cerrar**
[adoptado 10 nov]. Al encargar: encargo · invariante · fuera (qué no
incluye) · prueba de cierre · disparo de parada. Al cerrar: veredicto
(cumple / no cumple / en duda) · afirmación que verifiqué · resultado
(confirmada / falsa / no verificable) · hallazgos con clase · quedó
fuera · no volví a probar. Sin esas líneas, la sesión siguiente
rediscute gustos y da por sentado lo que nunca se probó. La ficha vive
pegada al trabajo, no en un informe aparte; la app reconstruida la trae
como formulario persistente (ver DESTILADO-APP-CUADERNO.md).

**La pregunta de antes de escribir** [adoptado 10 nov]. Una sola,
antes de que el asistente toque el sistema: «Di el invariante y el
caso que lo rompería. No implementes hasta que yo confirme.» Si el
asistente no puede nombrar el caso que rompe su diseño, no hay diseño:
hay intención. El director confirma el caso; entonces se escribe. Es
la regla de parada previa que le faltaba al sistema: el protocolo de
refutación ataca lo ya producido; esta pregunta ataca el diseño antes
de que exista código.

**Cuando el asistente trae prisa** [adoptado 10 nov]: no aceptar un
paquete de cambios mezclado con una explicación larga (pedir el diff
acotado a la frase) · si propone tres caminos, elegir uno en una línea
y dejar los otros fuera por escrito · si dice que está bloqueado,
exigir el síntoma observable y el último paso que sí funcionó · cortar
la sesión al aparecer un P0 aunque el resto «ya esté».

## 9. Ejercicios para el director (de Antonio, no de Dirsi)

Siete ejercicios graduados, en orden, cada uno entrena lo que el
siguiente usa; se activan cuando Antonio los elija, no por defecto
(mismo estatuto que los 11 de Claude):

1. El encargo en una frase (15 min): reescribir un pedido real con
   resultado observable, destinatario y exclusión; la frase sobrevive
   si otra persona puede decir sí o no al ver el resultado.
2. Sembrar y cazar (40 min): el director mete tres fallos (corrección
   visible, frontera, éxito mentiroso) y dos cambios inocuos de estilo
   en un módulo pequeño, y luego caza: hecho bien es marcar los tres
   fallos en quince minutos sin subir el estilo a «bloquea» [el sistema
   ya siembra fallos para medir verificadores; aquí el que siembra y
   caza es el director, como entrenamiento propio].
3. Verificar una afirmación (30 min): elegir una frase del asistente y
   reproducirla en el artefacto real; cerrar con una etiqueta escrita:
   confirmada, falsa o no verificable, con la evidencia en una línea.
4. Los tres de cien (25 min): de un informe largo, diez detalles en
   ocho minutos, regla del daño, entregar solo tres con síntoma y prueba.
5. Una crítica de una página (30 min): falsar la afirmación más fuerte
   de una respuesta larga, un solo hallazgo en el formato de la §4, y
   escribir a propósito una crítica mala para tacharla.
6. ¿Está terminado? (20 min): aplicar la lista de la §5 a un trabajo
   que «ya se ve bien», punto por punto con evidencia de una línea;
   prohibido el veredicto «casi».
7. Dirección en vivo (la próxima sesión real): frase de encargo,
   pregunta del invariante con parada, una afirmación verificada por el
   director, hallazgos clasificados, ficha completa. Deja de ser
   ejercicio y pasa a ser la forma de trabajo.

Progresión sugerida por el capítulo: 1 y 3 esta semana sobre trabajo
ya entregado; 2 cuando haya un módulo sin presión de fecha; 4 y 5
sobre respuestas reales; 6 en cada entrega; 7 como forma permanente.

## 10. Los errores de Grok, según Grok (para calibrar su consejo)

Declarados por él mismo en su sección 06, sin registro de rondas que
los respalde: cerrar con una verificación a medias (el entorno responde
y el artefacto publicado no se miró) · narrar un procedimiento que el
código aún no cumple · ensanchar el encargo hacia la pieza más lucida
cuando se pidió un criterio o un archivo · resolver con más superficie
un problema de un invariante · suavizar un hallazgo propio para que el
cierre quede redondo · citar una API o una convención de memoria
cuando el archivo dice otra cosa («la memoria pierde contra el
archivo») · perder la frase del encargo en sesiones largas y pulir el
último tramo. Su instrucción de uso: no discutir el tono del parte;
pedir el paso de la afirmación más fuerte, el comportamiento con la
lista vacía y qué archivo apareció fuera de la frase; si falta uno, la
entrega vuelve. Se pondera como el anexo de Claude: autocrítica
declarada, útil como lista de vigilancia, no como historial probado.

## Tarjeta de bolsillo

- Revisar: encargo en una frase → contrato externo → ¿vive? → flujo
  real con vacío/típico/malformado → fronteras → verdad de los datos →
  fallos baratos → estructura al final → reproducir la afirmación más
  fuerte en el artefacto final.
- Mirar: un detalle importa si toca corrección, datos, bloqueo o
  reversión; sin prueba escribible es sospecha, no hallazgo. En vivo,
  regla del daño; para cerrar la lista, el puntaje de Claude.
- Priorizar: P0 ahora · P1 este ciclo · P2 con fecha o disparo · P3 si
  sobra. Contención antes que arreglo.
- Criticar: la viga primero; clases bloquea/riesgo/deuda/gusto;
  hallazgo en ≤8 líneas con observado, esperado, prueba y acción mínima.
- Terminado: las 7 casillas, todas; si falta el artefacto final o la
  afirmación reproducida, está narrado, no terminado.
- Entrega: pase de dos minutos; si falla la frase del encargo o hay un
  archivo fuera de encargo, se para ahí.
- Antes de escribir: invariante y caso que lo rompería, confirmados
  por el director. Encargo, plan y parte no se mezclan; el parte no
  es evidencia.
- Registro: ficha de cinco líneas al encargar y cinco al cerrar.
