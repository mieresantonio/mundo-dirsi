# Glosario del sistema

Los términos del sistema, definidos una sola vez. Cada término tiene
aquí un solo significado escrito; si un documento lo usa de otra
manera, manda esta definición o se corrige el documento. Nació de una
confusión real: el 3 nov 2026 el sistema perdió una tarde entera en
«sin sistema» contra «con sistema» hasta que Antonio corrigió los
términos; este glosario es la vacuna contra la próxima confusión de
ese tipo.

Regla de mantenimiento: cuando nazca un término nuevo o cambie uno,
se añade o se corrige aquí, con su fuente. Cada entrada cita el
documento donde nació o donde está definido; cuando la fuente vive
fuera de este repo, se dice tal cual.

**Primera versión: 16 de noviembre de 2026 (34 entradas definidas).**

## Términos del sistema

- **artefacto** — el resultado visible del trabajo de un agente:
  documento, página, informe, aplicación. *MANUAL-AGENTES.md §1.*
- **bandeja de decisiones** — ventana fija (semanal) en la que se
  agrupan las decisiones pendientes de Antonio para que las resuelva
  de una vez, en vez de interrumpirlo una a una.
  *INVENTARIO-CAPACIDADES.md §4; METODO-CLAUDE.md §7C.*
- **banco de pruebas** — conjunto fijo de tareas reales de Antonio
  con criterios de aprobado escritos de antemano, que se corren
  periódicamente para medir cómo rinde Dirsi como sistema y detectar
  deriva entre corridas. *BANCO-DE-PRUEBAS.md.*
- **capa de medición** — las tres piezas creadas el 3 nov 2026:
  registro de calibración, banco de pruebas y protocolo de
  refutación. No es el sistema entero: es la capa que lo mide.
  *BANCO-DE-PRUEBAS.md § Evaluación con/sin sistema;
  PROTOCOLO-REFUTACION.md.*
- **censo** — foto con fecha de todo lo que Dirsi tiene a mano:
  máquina, herramientas, accesos y automatismos. Manda sobre
  cualquier nota vieja de límites; se refresca antes de afirmar un
  límite, junto a cada corrida mensual del banco y tras cambios
  grandes del entorno. *INVENTARIO-CAPACIDADES.md.*
- **director / ejecutor / crítico** — los tres roles de la
  arquitectura de trabajo serio: el director piensa y estructura
  (criterios de aceptación escritos antes de ejecutar, revisión
  final); el ejecutor toca archivos y construye dentro del alcance
  recibido; el crítico — idealmente otro motor distinto — intenta
  romper lo construido. *MANUAL-AGENTES.md §5.*
- **diseno-vitrina** — sistema de diseño para interfaces web de
  Antonio, destilado de Grok Build: tokens primero, disciplina de
  color, radios concéntricos, recetas de movimiento y checklist
  anti-slop. Su primera aplicación (rediseño del portafolio, 7 nov
  2026) quedó confirmada en el registro. *Skill `diseno_vitrina`;
  CALIBRACION.md C-006.*
- **encargo / plan / parte** — los tres textos de todo encargo, que
  no se mezclan: el encargo es lo que debe ser verdad (se escribe
  antes y no se reescribe en silencio); el plan es lo que se va a
  hacer (no es evidencia de nada); el parte es lo que se afirma
  haber hecho (tampoco es evidencia: evidencia es el artefacto
  sometido a la prueba de cierre). Cuando parte y encargo no
  coinciden, manda el encargo. *METODO-GROK.md §8.*
- **ficha de sesión** — registro mínimo de una sesión: al encargar,
  encargo, invariante, fuera, prueba de cierre y disparo de parada;
  al cerrar, veredicto, afirmación verificada, resultado, hallazgos
  con clase, quedó fuera y no volví a probar. *METODO-GROK.md §8.*
- **lección** — aprendizaje registrado con procedencia (observado,
  documentado o inferido) que nace candidata, se confirma
  (reproducida o útil en al menos 2 tareas), se promueve a regla
  (útil en al menos 3 tareas distintas sin contraejemplos; la
  promoción la aprueba un humano) o se retira (contradicha,
  obsoleta o sin uso en 90 días; se marca, no se borra).
  *METODO-CLAUDE-PLAYBOOK.md §2.3.*
- **memoria de traspaso** — relevo escrito al cerrar un trabajo:
  propósito y estado, jerarquía de fuentes, archivos clave, comandos
  ejecutados y estado de verificación punto por punto.
  *MANUAL-AGENTES.md §10.*
- **niveles de evidencia (A / B / C / X)** — A demostrado (leído de
  primera mano o en fuente primaria); B secundario estable (método
  declarado, sin contradicciones); C afirmación del creador
  (marketing, nunca hecho); X retirado (no vuelve a usarse).
  *MANUAL-AGENTES.md §8.*
- **ojo visual** — la capacidad de Dirsi de capturar páginas locales
  (escritorio y móvil) con el Chromium headless de Playwright y
  verlas ella misma; las URL públicas van por el navegador en vivo.
  *INVENTARIO-CAPACIDADES.md §2; BANCO-DE-PRUEBAS.md § Evaluación
  (actualización del 3 nov 2026, 19:00).*
- **pasada de refutación** — revisión adversarial obligatoria antes
  de entregar algo decisivo: un agente que no produjo el trabajo
  intenta refutarlo; cada afirmación atacada se clasifica refutada
  (se corrige o retira), debilitada (la salvedad entra visible en la
  entrega) o resiste (su confianza sube con motivo registrado).
  *PROTOCOLO-REFUTACION.md.*
- **registro de calibración** — anotación de las afirmaciones
  decisivas y comprobables de Dirsi con su nivel de evidencia,
  marcadas confirmada / parcial / refutada cuando la realidad
  responde; una refutada nunca se borra ni se reescribe.
  *CALIBRACION.md.*
- **ROCE** — forma de escribir una instrucción seria: Rol, Objetivo,
  Contexto, Estructura. *MANUAL-AGENTES.md §3.*
- **segundo yo** — agente de IA configurado para actuar por una
  persona de forma continua (24/7), con su contexto y sus reglas;
  el término viene de la serie «Tu segundo yo 24/7» de CenteIA y en
  este sistema nombra el papel de Dirsi para Antonio.
  *RECOPILACION-MATERIALES.md §M10 y §P1; el uso para Dirsi, en la
  memoria del sistema (MEMORY.md, fuera de este repo).*
- **sistema** — todo lo que rodea al motor y persiste: memoria,
  archivos, procedimientos, skills, repos vivos y conexiones;
  existe desde oct 2026. No confundir con la capa de medición, que
  es solo su parte que mide (desde el 3 nov 2026).
  *BANCO-DE-PRUEBAS.md § Evaluación con/sin sistema (corrección de
  términos del 3 nov 2026).*
- **skill** — el cómo encapsulado: un método empaquetado que se
  ejecuta siempre igual; carpeta con un `SKILL.md` obligatorio y,
  opcionalmente, scripts, referencias y salidas.
  *MANUAL-AGENTES.md §1 y §4.*
- **tarea de oro** — tarea representativa con un criterio de éxito
  objetivo, de un conjunto pequeño (5–15) que se ejecuta antes y
  después de cambiar el método, el modelo o las lecciones; si un
  cambio empeora algo, se revierte.
  *METODO-CLAUDE-PLAYBOOK.md §2.4.*
- **terminado de verdad** — estado que cumple la prueba de 9 puntos
  de Claude (criterio cumplido, verificado por otro método, probado
  en real, fallos probados, reversible, operable por otro, sin
  sorpresas, lo no comprobado listado, explicable por el dueño) o su
  versión rápida de 7 casillas de Grok. Presentable no es
  terminado: presentable es que se ve bien en el caso que el autor
  eligió mostrar. *METODO-CLAUDE.md §4; METODO-GROK.md §5.*

## Método adoptado (de Claude, Grok y el playbook)

- **clases P0–P3** — clasificación de hallazgos dentro de un mismo
  frente: P0 ahora, P1 este ciclo, P2 después (con fecha o disparo),
  P3 si sobra. *METODO-GROK.md §3.*
- **regla de tres** — si el mismo enfoque falla tres veces, parar:
  escribir qué se sabe, qué se descartó y qué no se entiende;
  cambiar de estrategia o preguntar. *METODO-CLAUDE-PLAYBOOK.md
  §2.1.*
- **regla del daño** — filtro rápido: un detalle merece atención
  solo si toca corrección, datos, bloqueo o reversión; si no toca
  ningún eje, es ruido por ahora. *METODO-GROK.md §2.*
- **siete lentes** — mirar cada problema por siete lados: usuario,
  datos, fallos, tiempo, adversario, operación y coste.
  *METODO-CLAUDE-PLAYBOOK.md §2.2.*
- **slopsquatting** — riesgo de instalar un paquete cuyo nombre
  inventó un modelo y registró un atacante; antes de instalar se
  verifica que existe, que es el correcto y que la versión es
  compatible. *METODO-CLAUDE-PLAYBOOK.md §2.5.*

## Nombres propios que aparecen en todo el sistema

- **Block Ethos** — proyecto final de 4Geeks de Antonio:
  plataforma de aprendizaje blockchain (frontend React con Vite,
  backend Flask), eslogan «Web3 Space»; se llamó «Blockali» hasta
  el 16 nov 2026. *RECOPILACION-MATERIALES.md §2;
  aprendido/blockchain-web3.md; README.md (nota de nombre).*
- **CenteIA (CenteIA Education)** — canal de educación en IA detrás
  de la serie gratuita «Tu segundo yo 24/7» que Antonio estudió; su
  material nutre el MANUAL-AGENTES y la RECOPILACIÓN.
  *RECOPILACION-MATERIALES.md §M1–M10; MANUAL-AGENTES.md § Fuentes.*
- **ECC** — sistema de optimización de rendimiento para arneses de
  agentes (skills, instintos, memoria, seguridad y desarrollo con
  investigación primero), para Claude Code, Codex, OpenCode, Cursor
  y otros; Antonio forkeó `affaan-m/ECC` a su cuenta
  (`mieresantonio/ECC`) y lo revisa quincenalmente contra el
  upstream. *API pública de GitHub (descripción del repo,
  verificada el 16 nov 2026); CALIBRACION.md C-005; MEMORY.md
  (memoria del sistema, fuera de este repo).*
- **fábrica de software** — kit «Tu fábrica de software» de Jesús
  (AlpacaTech): método con cerebro («qué es bien» + contexto +
  lecciones), pasos de un solo puesto, quien produce no revisa,
  telemetría desde el primer paso y nada fuera sin OK humano;
  Antonio lo publicó como copia de trabajo en
  `mieresantonio/fabrica-de-software`.
  *RECOPILACION-MATERIALES.md (addendum del 5 nov 2026).*
- **GDD** — desarrollo guiado por objetivos (Goal-Driven
  Development): tema del taller Agentic Engineer 2027 del 24 nov
  2026. *RECOPILACION-MATERIALES.md (addendum del 16 nov 2026).*
- **P-03 / P-04** — pruebas del banco aún sin primera corrida: P-03
  verifica un paquete construido contra su lista de promesas antes
  de publicar; P-04 aplica un cambio pequeño a una app y demuestra
  que el inventario de endpoints solo difiere en lo intencionado.
  *BANCO-DE-PRUEBAS.md.*
- **REA** — ingeniería inversa asistida: estudiar una web o app
  existente para entender su interfaz y su comportamiento observable
  y reconstruir algo equivalente con código propio, sin copiar
  código ajeno; la herramienta de referencia es `morluto/rea` (MIT),
  de la que Antonio tiene un fork de respaldo.
  *aprendido/ingenieria-inversa.md § Qué es REA;
  RECOPILACION-MATERIALES.md (addendum del 5 nov 2026).*
- **sala limpia** — separación entre especificación y construcción
  al clonar por ingeniería inversa: la réplica nace de la
  especificación escrita a partir de lo observado, no del material
  original. *Skill `clonacion_limpia_ingenieria_inversa`.*
