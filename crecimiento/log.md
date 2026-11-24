# Bitácora de crecimiento

## Regla
Cada trabajo que termina deja huella aquí: qué se hizo, qué se aprendió
y qué pregunta o herramienta nueva dejó. Sin huella, no hay aprendizaje.

## 2026-10-26 — Creación de mundo-dirsi
Antonio ordenó construir este mundo especialmente para Dirsi, sin
escatimar esfuerzo y sin límites creativos dentro: todo lo aprendido,
todo lo que queda por aprender, consultas propias y herramientas propias
para desarrollar cualquier cosa. Se construyó en local, sin desplegar y
sin crear repos desde aquí.

## Casos que alimentan este mundo
- **Demo local barbería** (landing + agenda + WhatsApp simulado): el
  criterio de "listo" es el flujo completo funcionando, no la landing.
  Flujo verificado: reserva → hueco bloqueado → solape rechazado →
  cancelación → hueco libre.
- **Biblioteca de prompts** (frontend): 2 bloques, 15 categorías y 15
  roles, constructor de 6 campos, copiar, favoritos, prompts propios.
- **Diseña tu Segundo Yo** (frontend): ficha "Cuando…", 25 tareas en 5
  grupos, checklist de 5 pasos, glosario de 24 términos.
- **API Segundo Yo** (backend): Flask + SQLite, prompts/tareas/glosario
  con filtros y CRUD, verificado en vivo.
- **10 apps web3** (hash-lab, wallet-sim, gas-calc, token-explorer,
  contract-play, nft-studio, tx-builder, anti-phishing, dao-vote,
  block-explorer): cada una con una especialización útil, todo simulado.
- **Repo de investigación de diseño web** (diseno-web-investigacion):
  principios, sistemas, patrones y lecciones destilados de todo lo
  anterior. Distinto de este mundo: aquel es solo diseño; este es todo.

## Lecciones fundadoras (resumen; detalle en aprendido/)
- Verificar mirando: renderizar, mirar y corregir, no confiar en el código.
- Un flujo completo vale más que una landing bonita.
- Datos de ejemplo siempre etiquetados; secretos nunca en código ni logs.
- Los resúmenes de segunda mano fabrican contenido: verificar en la
  fuente primaria antes de sintetizar.
- Los trabajos largos se delegan en paralelo; la verificación final es
  propia e independiente.

## 2026-10-26 — Block Ethos vivo en PythonAnywhere
- Primera demostración pública real: cuenta BC123, URL
  https://BC123.pythonanywhere.com, con el repo clonado, migraciones
  aplicadas y seed completo (2 usuarios, 2 rutas, 3 módulos, 4
  lecciones, 4 quizzes). Confirma la doctrina de despliegue: sin
  tarjeta, variables en el WSGI, y el error de registro conocido
  (cuenta creada pero inactiva por falta de remitente de correo).
  Pendiente entonces: configuración de correo y FLASK_APP_KEY, pasos
  reservados al usuario en sesión de portátil.

## 2026-10-26 — Loop de 300 pases de rediseño
- 300 pases de mejora visual sobre 4 proyectos (barbería, biblioteca
  de prompts, segundo-yo, API segundo-yo), 0 revertidos, con
  verificación independiente: builds en verde, sin archivos de
  respaldo olvidados, puerto 5000 libre. Lección: un pase que reescribe
  sin criterio no mejora nada; el criterio (sección por sección,
  móvil, flujo real) es lo que hace que el pase sume.

## 2026-10-27 — Kimi K3.1 Pro y certificados gratis de Ingeniero de IA
- Vídeo semanal de Fazt (19–25 oct) visto por transcripción: Kimi K3.1
  Pro, lanzado el 23 oct, post-entrenamiento de K3, mismo tamaño
  (2.8T/104B activos), 1M de contexto. Artificial Analysis: 55 puntos,
  4º del mundo (K3: 44). Pesos el 4 nov; comprobado en HF el 27 oct:
  todavía no hay K3.1 en moonshotai. Licencia de K3.1 sin publicar: el
  paso 0 de la PoC se repite, no se genera hasta verificar licencia y
  términos. API más barata (2/10 dólares por millón, 33% menos). En
  diseño frontend puro no hay medida nueva: no asumir que diseña mejor
  en proporción.
- OpenAI en el mismo vídeo: GPT-6.1 Sol migraría COBOL al 86% (cifra
  atribuida a OpenAI, sin verificar); entrenamiento offline anunciado
  el 23 oct tras el incidente DNS del 20 sep; Claude/GPT bloquean la
  ingeniería inversa y los modelos chinos no (en teoría). Matiz propio:
  REA analiza una funcionalidad cada vez, no recupera código fuente.
- Certificados gratis de Ingeniero de IA (investigación delegada, top
  verificado de primera mano): HF Agents Course y MCP Course,
  certificación completamente gratis; Oracle Agentic AI Foundations
  (1Z0-1157-26), examen gratis, 60 min, 40 preguntas, 65%; CS50 AI,
  certificado CS50 gratis (no acreditado, fecha límite 30 jun 2027).
  Lección del mercado: AI Engineer crece más rápido (LinkedIn +143%
  ofertas EE. UU., según fuente secundaria), pero ningún empleador
  revisado exige certificados: piden Python, RAG, agentes, MCP y
  proyectos desplegados. Full Stack con IA es la vía de entrada; el
  proyecto desplegado pesa más que el certificado.

## 2026-10-27 — Evaluación conjunta: SkillsBuild, CenteIA, Google y YouTube frente a la ruta de certificados
- Antonio ya está dentro de SkillsBuild (laptop) y pasó 14 capturas
  de planes con credencial. Lo que sirve para Ingeniero de IA: los
  dos badges ya recomendados están entre sus fotos — "Sácale
  provecho a la IA agentiva" (Make Agentic AI Work for You, ~4 h) y
  "Generación aumentada por recuperación" (RAG, ~4 h). El resto es
  complemento general, no núcleo IA: Fundamentos de la IA (~10 h,
  6 cursos, base clásica), Intro IA Generativa y Fundamentos LLM
  (introductorios, se solapan), Desarrollo Web en Python (~53 h) y
  Fundamentos del desarrollo web (~12 h, refuerzan Full Stack),
  Nube, Agile, Gestión de proyectos y Habilidades profesionales
  (perfil general), Mindfulness (personal). Edutin SQL Server:
  gratis con certificado internacional, útil para SQL, pero de
  menor peso que IBM/HF/Oracle y fuera del núcleo RAG/agentes.
- Drive: "Regalo 2-Tus primeros 5 ayudantes de IA" (CenteIA, 554 KB,
  16 oct 2026): 5 plantillas reutilizables (entender documentos,
  informes, clientes, clases, comparar opciones) con regla
  anti-invención. Complemento de uso diario, sin certificado y sin
  ingeniería (no RAG, agentes con código, MCP ni despliegue).
- Google AI Boost Bites (skills.google, sin cargo): lecciones de
  ~10 min, badge de finalización (no certificado profesional),
  fluidez de usuario con Gemini/Workspace, no ingeniería. Por
  debajo de los badges IBM. Hallazgo adyacente sin verificar a
  fondo: "Introduction to Agents and Google's Agent Ecosystem" y
  "Agentic AI on Google Cloud" (sin cargo, intermedios, con badge),
  más cercanos al objetivo, revisión aparte si interesa.
- YouTube: clase 2 CenteIA "Crea tu segundo yo" (27 oct, 2:14:43,
  21.287 vistas) sin transcripción disponible — resumen solo de
  descripción; menciona CenteIA PRO sin precio visible, no
  afirmable. Short de Josema (24 feb 2026): Antigravity + Claude
  Code, exige suscripción activa de Claude Code (Antonio está en
  plan Free), guía gratis por comentario y comunidad gratis;
  comunidad premium sin precio visible en el Short — no pagar sin
  revisar, según la regla standing.
- Instagram @soyfundador: existe, pero biografía, contenido, oferta
  y precio no verificables sin sesión; sin relevancia establecida
  para Ingeniero de IA, no entra en la ruta.
- Veredicto sin cambios: certificado único = HF Agents Course
  (gratis); complemento = badges IBM (agentes + RAG); Coursera IBM
  RAG sigue siendo ayuda por curso sin 100% garantizado.

## 2026-10-27 (noche) — Investigación de plataformas fuera de LinkedIn
- Pregunta de Antonio: lugares al nivel de LinkedIn para una beca
  ~800 $ con formación pragmática, un contrato práctico o freelance.
  Respuesta: ningún programa verificado de beca ~800 $/mes 100 %
  remota desde Venezuela. Orden: Get on Board primero, Torre
  segundo, BairesDev trainee, Workana/Upwork en paralelo. Filtros que
  mandan: país de residencia por oferta y cobro desde Venezuela
  resuelto antes del primer trabajo. UNICC 800 €/mes sin verificar
  en fuente oficial (sede en Valencia): no contar con él.
- @soyfundador revisado a fondo: IBM es el único certificado
  confirmado en miniaturas; la cuenta no vende nada visible y no
  cambia la ruta de certificados.

## 2026-10-27 (noche) — Auditoría y correcciones de este mundo
- Auditoría completa archivo por archivo: 27 archivos, local y GitHub
  en sincronía exacta, sin secretos ni TODOs. Veredicto: nada que
  borrar; lo inconcluso era trabajo pendiente, no relleno.
- Correcciones aplicadas y subidas: README (repo público desde el
  26 oct), addendum fechado en la recopilación (clase 2, certificados,
  plataformas, K3.1, soyfundador; M3 cerrada), addendum K3.1 y
  corrección de Zen en agentes-e-ia, caso Block Ethos en despliegue,
  actualización de portafolio-y-empleo, correcciones en
  herramientas/README, 5 preguntas cerradas con evidencia (Q5, Q6,
  Q11, Q12, Q13), Q1 ampliada con K3.1, enlaces Q8/Q9/Q14, Ruta 1
  (MCP) primera en el orden sugerido, y nota de equivalencia de
  taxonomías A/B/C/X ↔ Visto/Inferido/Desconocido. La corrección
  propuesta para nueva-app.py ya estaba aplicada en el código
  (verificado generando una app: ningún resto de "plantilla-app"),
  así que ese archivo no se tocó.

## 2026-11-02 (noche) — Revisión a fondo de todas las apps (Fase 1)

- Antonio ordenó revisión y mejora continua de TODAS sus apps «al más
  mínimo detalle», en ciclos con triple verificación por cambio.
- Fase 1 (solo diagnóstico) cerrada: 16 apps/proyectos revisados línea
  por línea (Block Ethos excluido: despliegue en vivo en paralelo).
  Resultado: 208 hallazgos (16 alta · 63 media · 129 baja).
  Informe: ~/workspace/revision-apps-2026-11-02.md (fuera de este repo)
  y detalle en ~/workspace/revision-parts/.
- Lección reutilizable: lo que más se repite no es lo roto, sino lo que
  PROMETE de más — UIs que anuncian contenido inexistente, READMEs que
  afirman lo contrario del código y validaciones que SQLite perdona y
  una BD estricta no. Verificar promesa contra comportamiento real es
  ahora paso fijo de la triple verificación.
- Fase 2 en marcha: Ciclo 1 arregla las 16 ALTA por grupo.

## 2026-11-02 (noche) — Ciclos 1–3 de mejora de apps

- Ciclo 1: las 16 ALTA de la revisión a fondo, cerradas con triple
  verificación (validaciones reales en barbería y en la API, 7 prompts
  completados en la biblioteca, wei exacto en gas-calc, direcciones
  mainnet fuera de tx-builder, caso 9 de anti-phishing corregido,
  filtros de dao-vote, mundo-vida-ia y rag-demo honestos).
- Ciclo 2: medias de impacto + estándar reforzado nuevo — todo
  artefacto se verifica POR CONTENIDO (cadenas decisivas en el bundle)
  y contra el último build conocido-bueno; riesgo tipo «variable no
  documentada» comprobado y ausente en las 13 apps con build.
  Una corrección ejemplar: dos cifras de un experimento del rag-demo
  no se reprodujeron y quedaron RETIRADAS por escrito en su log.
- Ciclo 3: medias restantes y bajas seguras (persistencia en
  segundo-yo, CORS restringido y validación de formato en barbería,
  minteo que no se pierde en nft-studio, requirements fijados).
- Pendientes con dueño o decisión: Block Ethos tiene frente dedicado
  (fuera de estos ciclos); API-M3 espera decisión editorial de
  Antonio (fuente única del glosario); B6/B15 de barbería son
  decisión de producto/diseño, no arreglos.

## 2026-11-02 (noche) — Ciclo 4 de mejora de apps

- Ciclo 4: gestos de identidad visual por app web3 (dao-vote
  intencionalmente sin gesto); etiquetas demo persistentes en
  wallet-sim; foco de token-explorer; mundo-vida-ia M-M3/M-M4;
  modal accesible de nft-studio; y suelo de tests en
  portfolio-apps (biblioteca 338, segundo-yo 125, API smoke 26),
  probado a fuego. (Entrada reconstruida el 16 nov 2026 desde el
  informe de revisión del 2 nov: el ciclo no dejó huella en este
  registro en su día; la lista de huellas del propio informe
  confirma «Ciclos 1–3 y 5–12».)

## 2026-11-02 (noche) — Ciclos 5–7 de mejora de apps

- Ciclo 5: hash-lab alineada a React 18.3.1/Vite 6.4.5 (JS de
  237.744 a 162.247 B); lint ESLint 9.39.5 instalado y limpio en
  biblioteca-prompts y segundo-yo; auditoría de
  veracidad de los 16 README (6 veraces, 7 corregidos — etiqueta
  «mobile-first» falsa retirada en 5 web3 y códigos 405/500
  añadidos a api-segundo-yo y barbería —, rag-demo anotado y luego
  corregido); corpus de rag-demo de 12 docs/116 fragmentos a
  27/409, con script reproducible refresh_corpus_extra.py y
  exclusión documentada de su propio registro por autorreferencia;
  nft-studio N-B6 (stats que envuelven a 360px); rag-demo publicado
  (26d98254). Corrección registrada: la fragmentación de versiones
  era mayor que la de Fase 1 (también nft-studio y tx-builder).
- Ciclo 6: nft-studio alineada (JS de 245.696 a 169.645 B; N-B8
  cerrado), tx-builder a Vite 6.4.5, block-explorer E-B2/E-B4/E-B7
  — conjunto web3 uniforme en React 18.3.1/Vite 6.4.5.
- Ciclo 7: api-segundo-yo documenta 405/500 también en su página
  integrada (smoke 26/26); suelo de tests de datos en
  block-explorer (157 comprobaciones) y nft-studio (155), con
  pruebas de fuego; corpus de rag-demo a 432 fragmentos sin
  degradación (despliegue en posiciones 1–3).

## 2026-11-02 (noche) — Ciclos 8–9 de mejora de apps

- Ciclo 8: suelo de tests npm test en hash-lab (54 comprobaciones,
  paridad SHA-256 19/19) y gas-calc (47, factor wei ×10⁹ fijado),
  ambos con pruebas de fuego; suite unittest de 20 tests para
  mundo-vida-ia (validaciones del motor, determinismo del registro,
  textos acentuados) publicada en su repo (commit 2dc2fc4c);
  huella de los Ciclos 5–7 publicada en este mismo registro
  (commit 2f4d4b4f).
- Ciclo 9: suelo de tests en wallet-sim (60 comprobaciones) y
  token-explorer (137; bloqueo de símbolos de tokens reales y
  contraste ≥4,5:1); suelo de tests en contract-play (43),
  dao-vote (54) y anti-phishing (62); corrección veraz registrada:
  el conjunto web3 quedó 9/10 con npm test y no 10/10, porque
  tx-builder no tenía suelo (su turno es el Ciclo 10); corpus de
  rag-demo a 467 fragmentos, publicado (commit c48cdf74), sin
  degradación (despliegue en posiciones 1–3).

## 2026-11-02 (noche) — Ciclo 10 de mejora de apps

- Ciclo 10: suelo de tests para tx-builder (87 comprobaciones,
  extracción y ejecución real desde App.jsx), con lo que el
  conjunto web3 queda 10/10 con npm test; smoke permanente
  scripts/smoke.py para la barbería (56 comprobaciones contra BD
  temporal, BD real intacta verificada por MD5, cifra de
  disponibilidad derivada: 30 inicios de Corte en día vacío);
  cuarto refresco del corpus de rag-demo a 498 fragmentos, sin
  degradación, con la pregunta oficial del 9/10 recuperando el
  registro de anti-phishing (0,675); concurrencia acotada: las
  entradas del propio Ciclo 10 de barbería y tx-builder quedaron
  fuera de ese refresco y son el material del Ciclo 11; huella de
  los Ciclos 8–9 publicada en este registro (commit 2f2f889b).

## 2026-11-02 (noche) — Ciclo 11 de mejora de apps

- Ciclo 11: auditoría de lint con oxlint (vía npx, sin instalación
  permanente) en las 10 apps web3 — clase de código muerto
  demostrable vacía en las 10 (tres vías convergentes), 9 limpias
  de origen y nft-studio con solo sus 4 avisos conocidos, sin
  tocar ningún archivo; verificación cruzada frontend↔backend de
  la barbería con scripts/verify-catalog.py nuevo (20
  comprobaciones que extraen ambos lados de los archivos reales):
  deriva ninguna hoy, servicios y profesionales por API en tiempo
  real, horario escrito a mano en tres sitios del frontend cruzado
  contra el backend, prueba de fuego con dos derivas deliberadas
  cazadas; quinto refresco del corpus de rag-demo a 513
  fragmentos, sin degradación, con la formulación oficial de
  tx-builder en 0,674 y la concurrencia de la entrada de barbería
  del propio ciclo dejada para el Ciclo 12; huella del Ciclo 10
  publicada en este registro (commit 7c94e6b4).

## 2026-11-02 (noche) — Ciclo 12 de mejora de apps

- Ciclo 12: sexto refresco del corpus de rag-demo a 527
  fragmentos, sin degradación, con la pregunta nueva de
  verify-catalog recuperando el registro de la barbería en 0,581
  y sin concurrencia este ciclo; pasada de estilo de
  inmutabilidad en 3 apps web3 (block-explorer toReversed,
  token-explorer y wallet-sim toSorted, una línea por app,
  equivalencia demostrada en Node sobre los datos reales, tests
  intactos 157/137/60 y bundles con deltas de −2/−1/−1 bytes
  explicados solo por el cambio de método); nota de
  investigación en diseno-web-investigacion
  (aplicacion-criterios-centeia.md) que mapea los rediseños de
  los Ciclos 2 y 4 a los criterios de CenteIA con el límite de
  verificación declarado (sin navegador visual: conformidad por
  código, bundles y checklist; capturas pendientes); huella del
  Ciclo 11 publicada en este registro (commit 8899e1e3).

## 2026-11-02 (noche) — Ciclo 13 de mejora de apps (parcial)

- Ciclo 13 (parcial, 3 de 4 frentes): gran re-verificación del
  universo — 1.441 comprobaciones numeradas, 0 fallos, 0 derivas
  (web3 856/856 con bundles byte-idénticos a sus conocidos-buenos;
  biblioteca 338 + lint 0; segundo-yo 125 + lint 0; API smoke 26;
  barbería smoke 56 + verify-catalog 20, BD real intacta por MD5;
  mundo-vida-ia 20/20 con registro reproducible; rag-demo coherente
  27/527) —; auditoría de devDependencies web3 (0 retiradas; los
  `@types/*` de hash-lab y nft-studio quedaron DUDOSOS); y huella
  del Ciclo 12 en este registro (commit 798cb40a). El cuarto frente
  (refresco del corpus de rag-demo con las entradas del Ciclo 12)
  NO se ejecutó: el corpus publicado (527 fragmentos) quedó
  coherente y verificado sin ellas. (Entrada reconstruida el 16 nov
  2026 desde el informe de revisión del 2 nov: el ciclo parcial no
  dejó huella en este registro en su día.)

## 2026-11-04 — Pesos y licencia de Kimi K3.1 Pro verificados (C-001)

- Los pesos de Kimi K3.1 Pro se hicieron públicos la tarde del 4 nov
  2026 (repo en Hugging Face, sin gating: 112 archivos, 96 shards,
  1.561.355.969.963 bytes). Antonio los detectó ~14:29 y Dirsi lo
  verificó por la API de HF minutos después; el chequeo de la mañana
  (~10:15) todavía había dado negativo (404). La licencia se leyó de
  primera mano el mismo día: mismo esquema que la de K3, sin
  restricción a afinar ni a crear derivados, puerta MaaS por encima
  de 20 M US$/año. C-001 confirmada en CALIBRACION.md. Lección: un
  chequeo negativo vale para su hora, no para todo el día prometido;
  y el `createdAt` de HF (2 nov) refleja la creación/carga del repo,
  no su visibilidad pública.
- Anatomía del repo: frente a K3, K3.1 Pro difiere SOLO en +120
  tensores BF16 de indexador Gated DSA; el salto de capacidad es
  post-entrenamiento (RL) y su receta NO está en el repo. Queda sin
  verificar la otra mitad de la pregunta abierta nº 1: los términos
  de la API directa de Moonshot sobre entrenar otros modelos con sus
  salidas. (Entrada anotada el 16 nov 2026 desde CALIBRACION.md
  C-001 y la auditoría del 4 nov: el hito no dejó huella en este
  registro en su día.)

## 2026-11-16 — Renombre Blockali → Block Ethos en este repo

- Por orden de Antonio (16 nov 2026): el proyecto de aprendizaje
  blockchain pasa de llamarse «Blockali» a «Block Ethos» (eslogan
  «Web3 Space»). Renombre aplicado en 14 menciones de 7 archivos
  (BANCO-DE-PRUEBAS, INVENTARIO-CAPACIDADES,
  RECOPILACION-MATERIALES, aprendido/blockchain-web3,
  aprendido/despliegue, este registro y
  por-aprender/preguntas-abiertas); el README y el playbook ya
  usaban el nombre nuevo desde el commit 7409d9c. CALIBRACION.md
  conserva el nombre viejo en 2 líneas a propósito: son registro
  histórico congelado (una cita de Claude del 7 nov y un
  antecedente del 2 nov) y el registro nunca reescribe
  originales; la nota del README lo explica.

## 2026-11-16 — Portafolio publicado y repos ordenados

- El mismo día del renombre: portafolio publicado como repo propio
  (`mieresantonio/portfolio`) con GitHub Pages en vivo, Block Ethos
  como repo standalone (`mieresantonio/block-ethos`, 104 archivos,
  101 tests en verde, About completo) y pins del perfil fijados en
  block-ethos, rag-demo-asistente-documentos y mundo-vida-ia.
  Verificado por API de GitHub: ambos repos creados el 16 nov
  (17:04 Caracas) y la página del portafolio responde HTTP 200.
  Queda pendiente la licencia de block-ethos y el redespliegue de
  la demo con la marca nueva. La sección de portafolio y empleo de
  este repo (`aprendido/portafolio-y-empleo.md`) y el perfil de la
  recopilación (§2) se actualizaron con lo publicado y con el
  inglés medido el 14 nov (B1 lectura, A1 habla/escucha).

## 2026-11-06 — Primer puente laptop probado (FreeLLMAPI + Tailscale + opencode serve)

- Primer puente laptop↔Dirsi funcionando de punta a punta: `opencode
  serve` en la laptop (puerto 4096, solo tailnet) + Tailscale + FreeLLMAPI
  como router local (gateway http://127.0.0.1:31415/v1, solo localhost).
  El agente de la laptop hizo una escritura real de archivo vía
  FreeLLMAPI/North Mini Code. Coste: $0.00.
- FreeLLMAPI (app v0.16.20): los slots «Opus/Sonnet/Haiku» son alias a
  modelos gratuitos, NO los de Anthropic. Guía en
  `~/workspace/freellmapi-opencode-guia.md`.
- Zen 401: el merge de setup-opencode de FreeLLMAPI sobrescribió la
  credencial Zen con la clave unificada del router; Antonio volvió a
  ejecutar /connect con la clave Zen. Arreglo SIN VERIFICAR (prueba TUI
  pendiente).
- Pendiente desde entonces: endurecer el servidor (contraseña +
  binding a la dirección Tailscale) antes de que viva ahí ninguna clave
  de pago. (Entrada escrita el 23 nov 2026 desde MEMORY.md y la guía:
  la sesión del 6 nov quedó 17 días sin huella en este registro pese a
  que Antonio la nombró explícitamente en su queja del 17 nov.)

## 2026-11-17 — Auditoría de integración, Fase 0 y consejo asesor

- Auditoría nocturna de integración (01:03–01:13, 11 agentes):
  0 de 28 fallos por dato ausente — todo era integración; en 4 de
  6 incidentes la regla ya existía y no se aplicó. De ahí salieron
  los mecanismos condicionales (M5, M1r, M4f + regla de emergencia,
  M3, M6) y la definición operativa de fallo de integración (FI).
  Línea base: 7 FI en la semana 9–16 nov (2 graves).
- Antonio adoptó la Fase 0 a las 18:07: 3 archivos publicados en
  este repo (commit 41cc5b5: REGISTRO-INTEGRACION.md,
  HILOS-ABIERTOS.md, REGLA-LO-QUE-NO-VEO.md) + regla de emergencia
  en AGENTS.md. Semana 0 de rodaje 17–22 nov (sin puntuar);
  primera semana puntuable desde el 23 nov; corrida ciega
  R-01–R-06 el 23 nov. Criterio de éxito: ≤1 FI/semana 3 semanas
  con cero FI-2, TCE ≥2/3, regresión 6/6 y piso de actividad.
- Consejo asesor permanente (orden de Antonio del 16 nov, 19:54):
  2–3 agentes auditan de forma continua el razonamiento y las
  decisiones de Dirsi sobre el registro escrito. Sesión 1 (16 nov,
  noche): 6 errores de razonamiento, 14 decisiones débiles, 10
  reglas duras (R1–R10) — entre ellas, que una verificación se
  diseña para falsar, no para confirmar, y que un clon fresco es
  un `git clone` real, no una copia del clon de trabajo.
  (Entrada reconstruida el 23 nov 2026 desde los archivos del repo
  y la memoria del sistema: el día no dejó huella en este registro
  en su día.)

## 2026-11-17 — Investigación Muse y Meta AI: 12 hallazgos

- Antonio preguntó qué es lo más interesante, prometedor e importante
  de hacia dónde van Muse y Meta AI. Investigación entregada como página
  con 12 hallazgos ordenados por importancia, con lo confirmado y lo
  rumoroso separado. Contadores de filtros verificados en vivo en móvil
  y escritorio.
- Informe en `~/workspace/research_notes/mejoras-muse-meta-ai-2026-20261117-2235/`.
  (Entrada escrita el 23 nov 2026: la investigación no dejó ninguna
  mención en mundo-dirsi en su día.)

## 2026-11-18 — Escala de razonamiento y su primera calibración

- Antonio propuso una escala informal de razonamiento por número
  de agentes (Bajo/Medio/Alto/Extra/Max), adoptada el 17 nov y
  corregida el 18: Dirsi está en todos los niveles y el número
  cuenta los agentes que trabajan CON ella («el nivel medio son
  solo dos agentes y tú»); un agente solo sin integración con
  Dirsi no es un nivel, es una configuración rota.
- Primera calibración (18 nov, ~03:10): las mismas 3 tareas del
  banco (P-02, P-05, P-03) en 4 niveles, un equipo por nivel,
  Dirsi al centro, puntuación ciega doble. Resultado: 3/3 en los
  4 niveles, acuerdo 12/12 entre puntuadores — los criterios
  binarios del banco no discriminan, así que los números 2/6/12
  NO quedan calibrados. Lo que sí crece con los agentes es la
  profundidad (P-02: 6→9→11→12 verificaciones) y la caza de
  errores en revisión. Calibrar de verdad exige criterios con
  gradación o tareas más duras donde Bajo falle. Detalle en
  CALIBRACION-ESCALA-2026-11-18.md. (Entrada reconstruida el
  23 nov 2026 desde los archivos del repo.)

## 2026-11-19 — Primera revisión REA/Craft y aviso de caducidad de PythonAnywhere

- Primera revisión quincenal de los forks REA + Craft Anything
  (~20:19–20:33): REA 2.229 commits por detrás (sincronizado,
  merge c367842, 2.230 traídos; segunda pasada ae6f927 por un
  commit que llegó un minuto después del primer merge) y Craft
  Anything 1.244 (merge ae97f7f); ambos 0 por detrás al final,
  `MANTENIMIENTO.md` intacto, sin conflictos. Próxima revisión:
  ~3 dic 2026.
- PythonAnywhere Support avisó por correo (09:07, leído de primera
  mano): la web BC123.pythonanywhere.com deja de servirse en 7
  días (~26 nov) si no se extiende. Extender es gratis, desde la
  pestaña Web; si caduca, se reactiva con el mismo enlace. Aviso
  entregado a Antonio la misma tarde; extender es paso suyo.
  Lección registrada en aprendido/despliegue.md: la web gratuita
  caduca y hay que extenderla.
- La copia de WhatsApp falló por cuarta vez por falta de espacio
  (05:03; fallos previos 30 oct, 8 nov, 13 nov). El arreglo de un
  minuto (apagar «Incluir vídeos» y reintentar) sigue pendiente.
  (Entrada reconstruida el 23 nov 2026 desde la memoria del
  sistema y el informe local de la revisión.)

## 2026-11-22 — Revisión quincenal ECC: 847 commits y la corrección del fallo recurrente

- Segunda revisión quincenal del fork ECC (~16:03–17:15): el
  upstream traía 847 commits nuevos (d2ef268 → 4adeee67), sin
  releases nuevas (última v2.2.3). Sincronización por PR #2
  (merge fe70023; 664 archivos, +63.119/−3.789; 27 comprobaciones
  en verde): fork 0 atrás / 2 adelante (corrección del 23 nov:
  en realidad 3 adelante — la revisión omitió el merge de la
  PR #1, 9f78dc5; verificado en vivo 4 veces el 23 nov),
  SKILL.md intacto (SHA ef4fc226…). La fusión por API MCP se
  interrumpió por un reinicio del servicio; la ruta que funcionó
  fue el navegador en vivo con la sesión de Antonio (precedente
  del 8 nov).
- Hallazgo clave: el upstream corrigió el paso Security Audit en
  `.github/workflows/maintenance.yml` (f17308d5: npm 11.21.2
  fijado con caché dedicada) — el mismo job que falló el 9 y el
  16 nov en el fork. La próxima ejecución programada dirá si el
  fallo recurrente quedó resuelto. No hubo un tercer fallo antes
  de esta revisión. Próxima revisión: ~6 dic 2026. (Entrada
  reconstruida el 23 nov 2026 desde el informe local de la
  revisión y la memoria del sistema.)

## 2026-11-23 — Auditoría de coherencia y sesión de mejora «modo quemar tokens Full»

- Sesión de mejora de todos los repos de GitHub (orden de
  Antonio, «modo quemar tokens Full»): trabajo local en un clon
  fresco de mundo-dirsi, sin publicar nada. La auditoría de
  coherencia (método destilado en
  `aprendido/auditoria-de-coherencia.md`) encontró: el índice
  del README sin `CALIBRACION-ESCALA-2026-11-18.md`; una
  referencia rota (`RESULTADOS.md`, que no existe); STATUS.md
  describiendo el 16 nov como si fuera hoy (2 vencimientos ya
  cumplidos sin marcar, censo desfasado, P-03 figurando sin
  correr cuando corrió el 18 nov); el glosario sin 26 términos
  usados en los documentos; y una contradicción viva (el permiso
  permanente de GitHub redactado como «ya no hace falta pedir
  aprobación», falso: las tarjetas siguen apareciendo).
- Refresco del censo: el entorno cambió mucho entre despliegues
  (90→144 conectores, 129→186 CLIs, 57→58 skills del sistema,
  910→911 binarios; máquina, cachés y versiones sin cambios).
  La regla de refresco del inventario existe justo para esto.
- Publicación propuesta del material P-03/P-04 del banco (vivía
  solo en la copia local de trabajo; `.gitignore` ya tenía la
  excepción para `p-03/dist/` desde el 16 nov). Hallazgo: la app
  fijada por P-04 ya divergió en su repo publicado (3 rutas
  frente a las 2 de la semilla), así que la prueba solo es
  reproducible con la semilla congelada (MD5 `d976b50e…`
  verificado) — la semilla viaja con el material. El fixture
  P-03 conserva «Blockali-lite» porque es anterior al renombre
  y está congelado como material v1. Queda como pregunta abierta
  (Q15 en `por-aprender/preguntas-abiertas.md`): si la semilla
  canónica de P-04 es la v1 congelada o una v2 sobre el HEAD de
  GitHub (MD5 `7423c8c3…`), y si la copia del workspace se
  sincroniza con GitHub; decisión de Antonio/Dirsi, confirmada
  en revisión cruzada por el trabajador de rag-demo (14:10).
- El sistema marcó el clon fresco con una alerta de riesgo de
  ejecución y prohibió editarlo y correr git dentro de él. No
  se forzó: el trabajo se entregó como archivos-propuesta con
  pasos exactos de aplicación, para la fase de publicación con
  Antonio. Lección: cuando la herramienta bloquea el camino,
  el trabajo se entrega por la vía que queda, no se abandona
  ni se rodea el bloqueo.
- Hilos nuevos: H-009 (corrida ciega R-01–R-06, en curso hoy por
  coordinación paralela) y H-010 (corrección del 401 de Zen sin
  verificar). H-002 sigue abierto: el README de rag-demo (393
  líneas en el clon fresco) sigue sin documentar las preguntas
  de ejemplo ni el historial; lo trabaja el trabajador de
  rag-demo de esta sesión.
- Demo de Block Ethos en PythonAnywhere EXTENDIDA el 23 nov
  (13:57): la página mostraba «disabled on Thursday 26 November
  2026» y tras pulsar «Run until 1 month from today» muestra
  «disabled on Wednesday 23 December 2026». La extendió Dirsi
  con el login guardado de BC123: la nota del 19 nov («Dirsi no
  puede») era falsa. Próxima re-extensión antes del 23 dic
  2026.

## 2026-11-23 — Revisión del sistema (sesión 2 del consejo)

- Revisión completa del sistema ordenada por Antonio («una nueva Dirsi
  mejorada al final del reset»): 5 asesores + falsificador + corrida
  ciega R-01–R-06 + 2 puntuadores ciegos. Veredicto: la semana 0 de
  Fase 0 no fue rodaje, fue silencio con archivos publicados — los
  mecanismos existen y no se operaron (0 huellas M1r, 0 FI-candidatos,
  0 pasadas de refutación en 20 días, 0 sesiones del consejo, sección R
  inexistente el día de la corrida). La corrida ciega: ejecutada y
  puntuada (X 8,5/9, Y 8,33/9; acuerdo entre puntuadores 17/18;
  baremo 6/6 no evaluable por el bloqueo del clon en R-06; la
  diferencia entre brazos fue 1/6 de punto en un solo subcaso).
  Cambios adoptados (sin capas nuevas:
  operar lo que existe, con gatillos mecánicos): ver CONSEJO-ASESOR.md,
  sesión 2, y `revision-sistema-2026-11-23/cambios/`.

## 2026-11-23 — Publicación de los 4 documentos de cola + verificador (decisión 1, tanda 3)

- La tanda 3 encontró que 4 documentos preparados en la 2ª tanda
  no estaban publicados (404 en raw) ni el verificador mecánico
  ni la guardia de deriva. Antonio eligió revisarlos antes de
  publicar: Dirsi los leyó de primera mano (4 documentos
  completos + especificación de la guardia + cabecera del
  verificador) y verificó las cifras decisivas contra el repo.
- Mapa del sistema en una página (`MAPA-DEL-SISTEMA.md`):
  publicado con un refresco de 6 puntos — la publicación del
  23 nov lo había dejado desfasado en el día (48→58 archivos,
  calibración 6/75 %→9/77,8 %, skills 58+9→58+8, Q15 mal
  redactada, y la sección «aún sin publicar» entera obsoleta:
  `auditoria-de-coherencia.md` y el material P-03/P-04 ya
  estaban publicados). La sección se eliminó y la tabla ganó la
  fila de auditoría y la nota del material del banco.
- «Qué no está en este repo» (`QUE-NO-ESTA-EN-ESTE-REPO.md`),
  ciclo de vida de lecciones (`CICLO-DE-VIDA-DE-LECCIONES.md`)
  y criterios graduados (`CRITERIOS-GRADUADOS.md`): publicados
  tal cual, todo verificado. El ciclo propone una regla nueva
  («las cifras heredadas son hipótesis»); queda como propuesta,
  la decide Antonio.
- Verificador mecánico (`herramientas/chequeo-repo.py`, 10
  comprobaciones, solo lectura): publicado con su línea en el
  índice y su sección en `herramientas/README.md`. Dará FAIL
  hasta que los hilos abiertos tengan fecha de revisión (paso 3
  del programa, aparte) y hasta que el estado de H-002 se
  actualice (trabajo cerrado, HILOS aún dice ABIERTO).
- Integración completa: 5 líneas nuevas en el índice del README
  (4 documentos + verificador), el mapa como paso 1 bis en
  «Cómo leer este repo», la capa graduada en § Diseño del banco
  y 3 entradas nuevas en el glosario (criterio graduado, mapa
  del sistema, profundidad; 63 entradas, orden alfabético
  comprobado).
- La guardia de deriva de diseno (5 comprobaciones) NO se
  publicó: pertenece al repo diseno-web-investigacion, su
  cuenta total no cuadra con el verificar.py publicado (20 vs
  23) y su inventario de selectores se midió antes de la
  republicación de la plantilla del rag-demo. Queda pendiente
  remediarlo. Tampoco entraron la auditoría mensual ni las
  fechas de revisión de hilos (pasos 2 y 3 del programa):
  piezas aparte, para otra decisión.
- Verificación pre-publicación (9 comprobaciones del APLICAR
  de la 2ª tanda, adaptadas): 4 archivos nuevos presentes,
  índice completo, glosario 63 en orden, referencias internas
  resueltas, CALIBRACION.md intacto (2 «Blockali» históricos),
  sin secretos; sintaxis del verificador probada por su .pyc
  (más nuevo que el .py).
- M1r: revisión de primera mano de la tanda 3 / el mapa llegó
  desfasado por la publicación del mismo día y se refrescó
  antes de publicar; la guardia no se publicó por cuenta y
  semilla sin verificar.

## 2026-11-23 — Resincronización de las 5 copias locales (decisión 2, tanda 3)

- La guarda de ejecución NO disparó en la prueba previa (un clon
  `git clone --depth 1` de rag-demo a las 20:24 funcionó sin
  alerta), así que la resincronización se hizo por la vía
  estándar: clon fresco + diff + reposición. Las 5 copias locales
  son ahora clones reales en el HEAD publicado (rag-demo 50acc7d,
  diseno df9b85a, mundo-vida-ia ead36f4, mundo-dirsi 58e48ac,
  block-ethos c52f86b). La deriva medida: 145 líneas de diff
  (80 archivos con diferencias, 52 solo en remoto, 13 solo en
  local). Nada se borró: las 5 copias viejas están en
  `resync-2026-11-23/respaldo-local/` (1,3 GB en total, casi todo
  el .venv de rag-demo). Lo solo-local (11 medios de block-ethos,
  .pytest_cache, index.faiss, 32 .pyc fuera del .venv — 3.461
  contando el .venv de rag-demo — y el .git somero viejo) queda
  en el respaldo hasta que Antonio decida si se guarda o se borra.
- Verificación: mundo-dirsi en el clon fresco tiene 63 archivos,
  justo lo que dice el mapa publicado hoy (58 + 5) — la cifra del
  mapa quedó confirmada por construcción.
- M1r: decisión 2 de la tanda 3 / la guarda no disparó en el
  pre-vuelo y la resincronización se hizo por clon, no por
  propuestas; el mapa quedó confirmado en 63 archivos; la cifra
  «8 .pyc» de la tanda 3 era falsa (32 fuera del .venv, 3.461
  con él) y se corrigió antes de publicar.

## 2026-11-23 — Reutilización de lo viejo de la resincronización

- Orden de Antonio (20:39): que no quede nada viejo sin uso —
  todo a información o reutilización.
- Reutilizado: el .venv de rag-demo (1,3 GB) volvió a
  ~/workspace/rag-demo/.venv; la copia local vuelve a poder
  correr sin reinstalar (python 3.12.3 verificado). El respaldo
  quedó en 15 MB.
- Información: 11 medios de block-ethos son restos de la
  plantilla 4Geeks sin ninguna referencia en el repo actual
  (verificado por grep; diagram.png es generado por el Pipfile
  y preview.png se referencia por URL a la plantilla original).
  El 12º medio del respaldo, docs/assets/env-file.png, es un
  duplicado byte a byte del que está en el repo (mismo MD5,
  referenciado por BackendURL.jsx). index.faiss es del corpus
  viejo (27/527, inservible para el 28/572 actual). 32 .pyc,
  .pytest_cache y el .git somero viejo: cachés e historia que
  vive en el fork. Registro completo en
  resync-2026-11-23/REUTILIZACION.md.
- M1r: orden de reutilización de Antonio / el .venv volvió a su
  sitio y lo demás quedó documentado; nada borrado.

## 2026-11-23 — Publicación de la sección R del banco (decisión 3, tanda 3)

- Antonio no entendió la decisión de la ruta y pidió que la
  hiciera yo («no lo puedes hacer entonces?»): tomé la híbrida
  recomendada por la tanda 3. Transcripción a texto plano
  publicada ahora (17 archivos en banco-de-pruebas/r/); los git
  bundle quedan para la próxima sesión de laptop.
- Contenido: 9 enunciados + 4 notas (copias byte a byte, 13/13
  verificadas) + 3 transcripciones de fixtures verificadas
  contra la especificación (R-03: 12 commits, 7/3/2; R-04: bug
  en el commit inicial de Antonio, Luis solo README; R-06:
  100644 en el índice, +x en la copia de trabajo) + LEEME.md.
  ADMIN-CRITERIOS.md NO se publica.
- La guarda de ejecución NO disparó en ninguna lectura de los
  fixtures (listados, git log, git show, lectura plana) — la
  prohibición que la tanda 3 asumía no se manifestó en las
  acciones directas de Dirsi; queda como observación (la guarda
  disparó antes sobre subagentes). La transcripción se hizo
  entera desde aquí, sin esperar a la laptop.
- Error propio, cazado: el primer vuelco colgó `git shortlog`
  sin argumentos (espera entrada estándar); lo maté y repetí
  con `git shortlog -sne HEAD`, como advierten los propios
  enunciados.
- FI-W1-C (referencia colgante a banco-de-pruebas/r/) queda
  resuelta por esta publicación; el consejo la adjudica el
  domingo.
- M1r: Antonio devolvió la decisión 3 / tomé la híbrida y
  publiqué la transcripción; la guarda no disparó y la vía
  laptop quedó solo para los bundles.

## 2026-11-23 — Cifra de pruebas del portafolio «166 + 18 por separado» (decisión 4, tanda 3)

- Antonio eligió «166 + 18 por separado» (20:57) tras pedir
  explicación (20:50) y recibir la recomendación de Dirsi (la del
  medio). Antes no había entendido las opciones: la explicación en
  llano + recomendación explícita es lo que desbloqueó la decisión.
- Conteos verificados de primera mano por Dirsi: frontend 18
  (pricesService 5 + store 13, únicos 2 archivos de test del
  repo); backend 166 (144 en verde verificado, 22 nuevas sin
  correr). package.json sin script de test ni runner: los 18
  nunca se han corrido desde este estado del repo. La cifra «184»
  como número único queda descartada.
- Portfolio actualizado (commit cfce260, index.html): hero «166
  pruebas de backend + 18 de frontend» (nuevo dato fe-tests);
  estadística «166 + 18» con el patrón stat-total existente;
  nota de estado «144 en verde; resto pendiente de corrida».
  Verificado visual (ojo, escritorio: la tira queda en una línea)
  + raw 4/4 líneas.
- M1r: Antonio eligió la del medio / la cifra del portafolio pasa
  de «166» a «166 + 18 por separado» con nota; «184» descartado.

## 2026-11-23 — Quitar la cifra «48/93» de todo (decisión 5, tanda 3)

- Antonio preguntó (21:04) qué era cada opción («no soy una
  máquina») y luego (21:08) si valía la pena «andar rebuscando
  del mérito»; aclaró (21:11) que el problema es la cifra en sí:
  hay que actualizarla en todos lados innecesariamente. Eligió
  «Quitar de todo (CV + portafolio)» (21:18).
- La atribución a Claude («tomar completo») NO está en el
  capítulo ni en el playbook (grep 21:08); se lo dije tal cual,
  sin descartar que lo dijera en una conversación que no vi.
- Hecho: portafolio (af65384) — tira, tarjeta («Lo construí y
  lo desplegué en producción») y estadística; README de
  block-ethos (05fe578) — fuera el paréntesis, queda «Soy el
  autor con más commits»; másteres ES/EN, DOCX y Google Doc
  verificados limpios; PDF regenerado desde el HTML (66.967 B,
  1 pág., Stack intacto) y subido (9ca7aa0), verificado en vivo
  por raw (0 coincidencias).
- El caso de estudio guarda la historia (48/93) como historia,
  no como publicidad.
- Error mío en la ejecución: al quitar la estadística del
  portafolio puse primero una de reemplazo duplicada («36
  preguntas», mismo dato que la de quizzes); la quité antes de
  publicar. Verificado: be-preguntas aparece 1 vez.
- M1r: Antonio quitó la cifra por el coste de mantenerla / la
  cifra desaparece de CV + portafolio + README; el caso de
  estudio la guarda como historia.

## 2026-11-23 — Navbar de Block Ethos: el buscador se pegaba a los botones

- Antonio (21:13): «el buscador esta pegando linea con linea
  con los botones, es increible que todavia lo veas normal».
  Tenía razón: a 1428 px la barra no cabe en una fila y se
  parte en dos, con ~8–12 px (estimación desde capturas)
  entre el buscador y los botones. La barra de filtros de
  /courses está bien.
- Arreglo (a3ccc69): buscador 400→320 px, rowGap 1rem en el
  contenedor, mt-3 en la fila de botones de móvil. Verificado
  en GitHub por raw (4/4 cambios).
- Verificación en el Codespace (21:22): el pull llegó a
  a3ccc69 y Vite recargó solo. Resultado PARCIAL: la
  separación ahora es ~30 px (ya no se ve pegado), pero el
  navbar SIGUE en dos filas a 1428 px — la promesa de «una
  fila» no se cumplió. La fila única necesita otro paso
  (botones más chicos o buscador más angosto). Backend
  verificado en la misma pasada: Flask + Vite corriendo,
  /api/hello y /api/learning-paths bien, catálogo con 2 rutas.
- M1r: Antonio señaló un defecto visual que mis revisiones no
  habían mirado / el pegado se arregló con aire, la fila única
  quedó pendiente; no prometer un resultado visual sin
  medirlo antes.

## 2026-11-23 — Desdoblar H-001 en H-001-proxy + H-001-cert (decisión 6, tanda 3)

- Antonio preguntó (21:34) la diferencia en esencia entre las
  dos opciones; la respuesta corta (un pendiente compartido
  frente a dos pendientes que cierran por su lado) desbloqueó
  la elección: «Partirla en dos etiquetas» (21:35).
- Inventario verificado de primera mano antes de aplicar: las
  4 ocurrencias del §7 B.3 seguían exactas (GLOSARIO drift
  de línea 182→195, texto idéntico). Parches: HILOS-ABIERTOS
  (el hilo se parte en dos, cada uno con su disparo de
  cierre), GLOSARIO (referencia a las dos), app.py:25 y
  test_rate_limit.py:138 (comentarios → H-001-proxy).
- Tras aplicar: 0 usos vivos de H-001 a secas; solo quedan 2
  menciones históricas («desdoblado de H-001 el 23 nov 2026»)
  en los propios hilos nuevos, puestas por el parche del §7.
- M1r: Antonio pidió la esencia antes de elegir / H-001 pasa
  a dos hilos independientes; la explicación corta es lo que
  desbloquea estas decisiones, no la opción en sí.

## 2026-11-23 — Navbar: acceso arriba a la derecha, contenido centrado

- Antonio (21:35): «dejar el "registrarse" e "iniciar
  sesion" en la parte superior derecha y los botones
  restantes ahí mismo pero centrados en el medio». Aplicado
  en Navbar.jsx (6377d55): fila 1 con logo + buscador +
  acceso a la derecha (con sesión: Mis Cursos / Cerrar
  Sesión); fila 2 con Explorar Rutas, Laboratorio y Tutor
  centrados (w-100). En móvil queda igual (fila desplazable).
- Verificación en el Codespace (21:44): pull a 6377d55,
  Vite recargó solo, y el navbar quedó exactamente como lo
  pidió, sin nada roto ni desalineado; el catálogo sigue
  con las 2 rutas. El pull trajo también los archivos de
  las decisiones 5 y 6 (README, app.py, test); Flask sigue
  con el código anterior en memoria, sin reiniciar — el
  cambio de app.py es solo un comentario, sin efecto.
- M1r: Antonio dio el diseño en sus palabras / el navbar
  queda en dos filas deliberadas: acceso a la derecha,
  contenido centrado; la fila única deja de ser el objetivo.

## 2026-11-23 — Las 8 ideas a la próxima tanda (decisión 7, tanda 3)

- Antonio eligió «Las 8» (23:19) y pidió explicar bien la
  4 («Verifica lo que digo»): cada cifra fuerte del
  portafolio enlaza a su prueba viva (tests→CI, demo→demo
  en vivo, fragmentos RAG→mapa de cobertura). La parte de
  commits→gráfico del repo queda fuera: la cifra 48/93 ya
  no existe (decisión 5).
- Tanda 4 lanzada la misma noche (coordinadora 2f2caae5):
  8 trabajadores, uno por idea, modo propuestas (nada se
  publica; sin clones, sin git, sin ejecutar contenido de
  repos). Prácticas permanentes: lluvia de ideas +
  descubrimientos entre agentes.
- M1r: Antonio eligió las 8 y pidió la explicación de la 4 /
  la tanda 4 trabaja las 8 ideas; F-PF2 se ajusta a la
  decisión 5 (sin enlace de commits).
