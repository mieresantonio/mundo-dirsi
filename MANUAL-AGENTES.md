# Manual de agentes

*Cómo se monta un agente o subagente con el método de Antonio — para
los agentes futuros (principales y ejecutores) que trabajen con él.*

## Para qué es este manual

Este manual destila, en un solo documento, todo lo verificado sobre
cómo construir y dirigir agentes de IA dentro del sistema de Antonio:
lo enseñado en los videos revisados el 4 nov 2026 (Claude con skills,
Cowork, Codex, Claude Code, ChatGPT Work), lo ya recopilado antes
(guía de agentes de Google, packs de skills) y lo que su propio
sistema ya practica (memoria en archivos, skills propias, capa de
medición).

Un agente nuevo — en Claude, ChatGPT, Gemini, Grok o en una terminal —
que lea este manual y la `RECOPILACION-MATERIALES.md` de este repo
puede empezar a trabajar a su manera sin que Antonio tenga que
explicarlo todo otra vez.

**Qué no es**: no contiene la memoria personal completa de Antonio.
Esa memoria es privada y vivirá aparte; este manual es solo el
*método*, que sí es portable y público.

## 1. El mapa de piezas

Cinco piezas que se apilan, no se eligen (Clase 2 y video de skills,
CenteIA, oct 2026):

- **Prompt**: un encargo puntual, de una sola vez.
- **Proyecto**: un espacio con contexto — documentos y reglas que
  todas las conversaciones heredan sin repetirlos.
- **Skill**: el cómo encapsulado — un método empaquetado que se
  ejecuta siempre igual.
- **Plugin / conector**: la conexión con una herramienta o servicio
  externo.
- **Agente**: la suma de todo lo anterior, orientada a entregar
  trabajo terminado, no respuestas sueltas. El resultado visible de
  ese trabajo es el **artefacto** (documento, página, informe,
  aplicación).

Mapa de decisión antes de crear nada:

1. ¿Se usa una sola vez? → prompt.
2. ¿Se repite y necesita contexto? → proyecto.
3. ¿Se repite y debe seguir pasos y formato fijos? → skill.
4. ¿Debe verse o entregarse? → artefacto.

## 2. Contexto persistente: la memoria vive en archivos

Regla madre del sistema: **el agente no «aprende» en su modelo; lo que
persiste son los archivos**. Por eso todo agente de Antonio trabaja
sobre una base escrita:

- **Carpeta de contexto**: una carpeta única por proyecto o negocio
  con los documentos que mandan (identidad, catálogo, reglas,
  ejemplos). El agente lee de ahí en vez de pedir que le suban los
  archivos cada vez (patrón Cowork y ChatGPT Work).
- **Archivo de identidad** (`quién-soy`, `CLAUDE.md`, `agents.md`
  según la plataforma): quién es el usuario, cómo trabaja, sus reglas
  y qué no debe inventarse. Corto y vigente manda más que largo y
  viejo.
- **Carpeta de salidas**: todo lo que el agente produce se guarda en
  una carpeta conocida, no se queda flotando en el chat.
- **Jerarquía de fuentes**: cuando dos documentos discrepan, debe
  estar escrito cuál manda. Si no está escrito, el agente pregunta —
  no decide en silencio.

## 3. Cómo se instruye: ROCE y reglas duras

Toda instrucción seria se escribe con **ROCE**: **Rol** (en quién se
convierte el agente), **Objetivo** (qué debe lograr), **Contexto**
(qué material tiene y cuál manda) y **Estructura** (en qué forma
devuelve el resultado).

Reglas duras que acompañan a cualquier encargo importante:

- **Anti-invención**: «si no encuentras el caso, indícalo y detente;
  no sustituyas los datos por suposiciones» (Clase 2, [00:27:31]).
- **Sección de «lo no confirmado»**: toda entrega analítica cierra
  separando lo verificado de lo que no se pudo confirmar (guía de
  Codex).
- **Criterio antes que ejecución**: en tareas con dinero, precios o
  decisiones, primero se documenta el criterio en comprobaciones
  concretas y después se automatiza (Clase 2: el criterio del experto
  en 4 comprobaciones antes de dar un paso).

## 4. Skills: el método empaquetado

**Anatomía** (video «Claude con skills», verificada contra las skills
reales de este sistema, que usan la misma estructura):

- Carpeta con un **`SKILL.md` obligatorio**: cuándo se usa la skill y
  cómo debe trabajar.
- Opcionales: **`scripts/`** (código), **`referencias/`**
  (documentación y criterios), **`outputs/`** (activos: plantillas,
  logos, formatos).

**Cómo se crea una skill** (dos rutas que se complementan):

1. *Método en 3 pasos* (Repaso): primero un prompt ROCE que resuelve
   el caso → se itera el resultado hasta que es bueno → **recién
   entonces** se encapsula en una skill. No se empaqueta lo que aún
   no funciona suelto.
2. *Con Skill Creator* (la skill de Anthropic para crear skills): se
   le explica el caso de uso y se le sube un **brief** con el
   problema, las entradas posibles, la salida deseada, los criterios
   de análisis, las reglas de tono y los casos que debe cubrir. El
   creador estructura, crea, **prueba con un caso realista** y
   empaqueta. La skill resultante lleva su descripción-activador
   («usa esta skill siempre que…»), sus criterios y su plantilla de
   salida. Se puede descargar (vale para otras plataformas) o guardar
   en la cuenta.

**Uso**: se instala desde el catálogo de la plataforma o desde la
carpeta, y se invoca por nombre (en Claude, «/» + nombre).

**Criterio de calidad**: la pregunta no es «¿respondió bien?» sino
**«¿siguió el método?»**. Si la salida sale genérica, no se cambia de
modelo: **se mejora la skill** (más criterios, un mejor ejemplo de
salida, un formato más estricto).

## 5. La arquitectura: uno dirige, otro ejecuta, otro rompe

El patrón central para trabajo serio, confirmado por los videos
(Co-Work → Codex) y ya esbozado por Antonio para su sistema:

- **Director**: piensa y estructura — problema, criterios de
  aceptación escritos *antes* de ejecutar, y revisión final. Su
  salida (propuesta estructurada) se convierte tal cual en la
  entrada del ejecutor.
- **Ejecutor**: toca archivos y construye, dentro del alcance y las
  restricciones que recibió. Suele ser un agente de terminal
  (Claude Code, Codex, OpenCode).
- **Crítico**: un rol — idealmente **otro motor distinto** — que
  intenta romper lo construido. La crítica entre motores distintos
  vale más que la autocrítica del mismo motor. El director controla
  el *flujo*; nunca el *veredicto* del crítico.
- **El humano**: define el problema y conserva el criterio y la
  decisión final.

Punto de encuentro: **Git**. Cada agente trabaja en su rama; el diff
y el resumen de archivos cambiados son el contrato de entrega que el
director revisa antes de aceptar.

## 6. Método de trabajo en código (los cinco verbos)

Del video «+1.000 horas en Claude Code», el método más completo
revisado:

1. **Mirar**: explorar sin tocar.
2. **Entender**: lectura con entregable cerrado — un prompt de
   análisis ROCE que *prohíbe construir* y devuelve: la pregunta
   exacta, los hechos con su fuente, las contradicciones entre
   fuentes y el plan. («No me propongas todavía ninguna solución».)
3. **Construir**: versión pequeña y acotada, con restricciones
   explícitas (qué no debe usar) y criterios de aceptación por
   bloque, no «hazlo bonito».
4. **Romper**: fase adversarial en **dos pasadas** — primero la
   lógica, después la interfaz — con salida clasificada:
   comprobado / no comprobado / revisión humana.
5. **Documentar**: cerrar escribiendo la memoria de traspaso (§9).

**Permisos como semáforo**: manual (aprobar cada paso), automático
con compuertas (aprobar en los puntos de riesgo) o libre solo en
trabajo reversible y acotado. La aprobación humana es una compuerta
del flujo, no un trámite.

## 7. Verificación: nada se entrega sin pasar por el fuego

- **Autoverificación del ejecutor**: quien construye una interfaz se
  hace capturas en móvil y escritorio, se compara contra los
  criterios y se corrige *antes* de entregar.
- **Verificar el artefacto, no el informe**: antes de publicar o
  desplegar, se comprueba el contenido real del paquete (buscar en
  el bundle las cadenas decisivas), no el nombre del archivo ni el
  log de construcción. (Lección propia del sistema, nov 2026.)
- **Red team con lentes**: para revisiones grandes, varios agentes
  en paralelo con lentes distintas (romper, generalizar, diseñar)
  supervisados por un orquestador que integra.
- **Pasada de refutación**: antes de una entrega decisiva (dinero,
  publicación, investigación con consecuencias), un agente que no
  produjo el trabajo intenta refutarlo; cada afirmación atacada se
  clasifica refutada / debilitada / resiste y el resultado se
  muestra, sin correcciones silenciosas. (Procedimiento completo en
  `PROTOCOLO-REFUTACION.md`.)

## 8. Evidencia: cómo se trata lo que se afirma

Sistema de niveles de este repo, obligatorio para cualquier agente
que trabaje con Antonio:

- **A** — demostrado: leído de primera mano o en fuente primaria.
- **B** — secundario estable: método declarado, sin contradicciones.
- **C** — afirmación del creador: marketing; se registra como tal,
  nunca como hecho.
- **X** — retirado: no vuelve a usarse.

Reglas: nunca sintetizar desde resúmenes de segunda mano sin cruzar
las afirmaciones decisivas contra la fuente primaria; nunca endurecer
las cautelas de un informe al resumirlo («no verificado» no se
convierte en «no existe»); las cifras de redes sociales obtenidas por
búsqueda pública son inestables y no se usan como dato. Las
afirmaciones decisivas y comprobables se anotan en el registro de
calibración (`CALIBRACION.md`) y se marcan cuando la realidad
responde.

## 9. Subagentes y delegación

- Se delega trabajo **autocontenido y verificable**: la tarea lleva
  su contexto completo, sus límites y qué cuenta como terminado. El
  delegado no recibe permisos que el encargo no tenga.
- El resultado de un subagente es un *informe*, no un hecho: lo
  decisivo se cruza contra la fuente primaria antes de usarse.
- **Triaje barato primero**: para clasificar y ordenar (correos,
  registros, documentos) basta un modelo clasificador sencillo que
  devuelva probabilidades entre opciones definidas (lección del
  clasificador Jev); el motor caro se reserva para generar y juzgar.
- **Tareas programadas**: lo recurrente (un cierre semanal, una
  revisión periódica) se convierte en tarea programada con su skill,
  no en un encargo repetido a mano.

## 10. Memoria de traspaso entre agentes

Al cerrar un trabajo, el agente deja escrito el relevo
(`CLAUDE.md` del proyecto o su equivalente):

- propósito del proyecto y estado actual;
- jerarquía de fuentes (qué documento manda);
- archivos clave y dependencias;
- comandos ejecutados y cómo se reproduce el resultado;
- estado de verificación, punto por punto (qué está comprobado y
  qué no).

El equivalente visual es el **Design System persistente**: se define
una vez (aunque sea desde capturas de la propia web) y todos los
encargos de diseño lo heredan, pidiendo dos versiones A/B cuando haya
que elegir. Los repos vivos del sistema (este incluido) son la
memoria compartida entre agentes: se consultan al empezar un trabajo
y se alimentan al terminarlo.

## 11. Arranque de un agente nuevo (checklist)

1. Leer `RECOPILACION-MATERIALES.md` y este manual completos.
2. Leer el `AGENTS.md` / archivo de identidad del proyecto donde va
   a trabajar, y respetar sus reglas por encima de cualquier
   costumbre propia.
3. Confirmar qué motor es y qué herramientas tiene *de verdad*
   (consultar el inventario de capacidades antes de afirmar un
   límite: `INVENTARIO-CAPACIDADES.md`).
4. Trabajar con la carpeta de contexto y la de salidas del proyecto;
   no pedir lo que ya está en los archivos.
5. Instruir y ser instruido en ROCE; criterios escritos antes de
   ejecutar en lo decisivo.
6. Construir acotado, verificar contra los criterios, romper en dos
   pasadas lo importante.
7. Entregar con diff/resumen de archivos y sección de «lo no
   confirmado».
8. Dejar la memoria de traspaso escrita y la huella en el repo
   correspondiente.

## 12. Límites honestos de este manual

- **El motor manda**: el mismo método rinde distinto según el modelo
  que lo ejecuta. Este manual multiplica lo que el motor ya sabe
  hacer; no lo sustituye.
- **Leer no transfiere habilidad**: un agente no se vuelve mejor en
  una destreza por leer cómo otro la ejerce; mejora su *sistema*
  (contexto, procedimientos, verificación), que es exactamente lo
  que este manual transfiere.
- **La salida es tan buena como las entradas**: con archivos malos,
  la respuesta sale igual de segura e igual de falsa (advertencia
  del propio video de Codex). La calidad del contexto es trabajo del
  humano y del director.
- Todas las cifras comerciales de los videos fuente (precios,
  alumnos, ingresos) son **nivel C** y no forman parte del método.

## Fuentes

- Videos revisados el 4 nov 2026 (transcripciones y síntesis en el
  archivo local de Antonio): «Claude con skills» (aa_lD4Lye3M),
  «Negocio de 1 persona con Claude» (vC9VHrvahJc), «Guía de Codex»
  (_1yMovPTJGM), «+1.000 horas en Claude Code» (nwfR325UyYk),
  «Co-Work vs Codex» (8L1d9bnDBf0), «App con Claude en 20 minutos»
  (LjFoELKPnXg), «Claude Design 2.0» (1xovtKZrREs), «Clonar cualquier
  app» (jQAHwKSsekY), «ChatGPT Work» (Tk8l491XiIM), Clases 2, extra
  y Repaso de «Tu segundo yo 24/7» (gheBwtDtU2o, gH1NFnWu07I,
  uAqeKFW1Ti4) — todos de CenteIA Education.
- Síntesis completa de esos videos:
  `~/workspace/centeia-materiales/sintesis-videos-2026-11-04.md`
  (archivo local) y el addendum del 4 nov en
  `RECOPILACION-MATERIALES.md`.
- Material previo: guía de agentes de Google y packs de skills
  verificados (ver M1 y entradas de repositorios en la RECOPILACIÓN).
- Sistema propio de Antonio: `CALIBRACION.md`,
  `BANCO-DE-PRUEBAS.md`, `PROTOCOLO-REFUTACION.md` e
  `INVENTARIO-CAPACIDADES.md`, en este mismo repo.

*Redactado el 4 nov 2026 con redacción original a partir de las
fuentes citadas. Se actualiza cuando una corrida del banco de
pruebas o una pasada de refutación cambie el método.*
