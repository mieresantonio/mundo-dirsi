# Inventario de capacidades de Dirsi

Foto con fecha de todo lo que Dirsi tiene a mano: su máquina, sus
herramientas, sus accesos y sus automatismos. Nació el 4 de noviembre de
2026, el día después de descubrir que el «ojo visual» llevaba declarado
imposible dos días mientras el navegador de capturas dormía en la caché
de la propia máquina. La lección que lo funda: **Dirsi no percibe su
entorno de fondo; solo sabe de él lo que comprueba y lo que deja
escrito.** Este inventario es la comprobación escrita, y manda sobre
cualquier nota vieja.

**Regla de mantenimiento:** se refresca (a) antes de afirmar cualquier
límite de herramienta, (b) junto a cada corrida mensual del banco de
pruebas, y (c) tras cambios grandes del entorno. Una foto vieja no
describe la máquina de hoy: la máquina virtual se reemplaza en los
despliegues y sus cifras cambian con ella.

## 1. La máquina (censo del 4 nov 2026, comprobación directa)

- Linux 7.0 · **4 vCPU** · **7,7 GB de RAM** (al censar: 601 MB
  disponibles — la RAM va justa; una carga pesada puede fallar por
  memoria, no por «no poder») · sin GPU.
- Disco del home: **150 GB, 145 libres**. `/tmp` es un tmpfs de 512 MB
  (descargas e instalaciones grandes van al home, nunca a /tmp).
- Runtimes: **Node v24.22.1**, **Python 3.12.3**, **Bun** (instalado en
  la imagen). Sin Java, Go, Rust, Ruby ni PHP.
- Binarios presentes de los que importa acordarse: **ffmpeg**,
  **LibreOffice** (`soffice`: conversión de documentos sin cuentas
  externas), git + **gh**, **jq**, **sqlite3**, curl/wget, rsync, ssh,
  zip/unzip. 910 binarios en /usr/bin.
- Ausentes comprobados (no afirmar que «no se puede»: varios se instalan
  por red): Docker, ImageMagick, pandoc, yt-dlp, Ollama, Whisper.

## 2. Cachés que ya guardan tesoro

- **Playwright: 681 MB** — Chromium completo (1248), Chromium headless
  shell y un ffmpeg propio. Es el ojo visual de
  `~/workspace/tools-visual/shot.mjs` (páginas locales, escritorio y
  móvil). El Chromium local **no sale a internet** desde la VM; las URL
  públicas van por el navegador en vivo.
- **HuggingFace: 458 MB** — el modelo de embeddings del demo RAG
  (paraphrase-multilingual-MiniLM-L12-v2) ya está descargado: el RAG
  puede correr sin descargar nada.

## 3. Superficie Muse

- **~120 CLIs en /opt/hatch/bin.** Por familias: Google Workspace
  (gmail, calendario, drive, docs, sheets…), GitHub, redes (Facebook,
  Instagram, Threads, Messenger), Meta Ads y catálogo, comercio
  (Shopify, Stripe, Shop Pay), viajes (Expedia, Agoda, Duffel,
  OpenTable, Ticketmaster, FlightAware), trabajo (Notion, Asana,
  Linear, Todoist, **Slack**, Zoom, Calendly), medios (generación de
  imagen/vídeo/audio, TTS, Spotify, búsqueda de imágenes), sistema
  (medidor de suscripción, almacenamiento remoto, Tailscale, datos del
  dispositivo, lector de códigos QR/barras `zbar-lib`).
- **74 conectores con documentación.** Conectados y verificados en uso:
  Gmail, Google Calendar, Drive, Docs, Sheets, Dropbox, GitHub.
  **Existe conector y CLI de Slack** — la nota vieja decía que no había;
  existe, con su conexión sin verificar. Que un conector exista no
  significa que la cuenta esté conectada: eso se comprueba por servicio
  antes de prometer nada con él.
- **Skills: 56 del sistema + 4 propias** (ingeniería inversa en sala
  limpia, explicaciones claras al negarse, verificación de artefactos
  antes de publicar, notas de skills recuperadas). Entre las del sistema
  hay varias casi sin uso (traducción, campañas, finanzas, formularios,
  comparador de hipotecas…): están para cuando una tarea las pida, no
  para memorizarlas.
- **Bóveda segura: guarda logins.** El navegador en vivo guarda además
  las sesiones que Antonio abrió en él.

## 4. Automatismos vivos (4 nov 2026)

- De Antonio, dos: la **revisión quincenal de un fork** y una
  **verificación única de pesos de un modelo**. El resto de trabajos en
  la lista son del sistema (Feed, doctor horario, heartbeat).
- El teléfono emparejado expone **41 comandos y 10 fuentes de datos**,
  sin comando de galería ni de archivos: verificado dos veces.

## 5. Herramientas construidas por el propio sistema

- `~/workspace/tools-visual/` — el ojo: capturas locales en escritorio y
  móvil (`shot.mjs`) y de URL vía navegador en vivo cuando aplica.
- Runbook de despliegue de Blockali, kit de prueba de concepto de
  destilación Kimi K3, scripts de audio (8D, mezclas) en el workspace.
- La capa de medición: `CALIBRACION.md`, `BANCO-DE-PRUEBAS.md`,
  `PROTOCOLO-REFUTACION.md`.

## 6. Lo que este censo no puede ver

- El estado real de conexión de cada servicio: se comprueba por tarea,
  no por censo.
- Capacidades tras permisos que Antonio aún no ha otorgado.
- Lo que cambie entre despliegues de la VM: por eso la foto lleva fecha
  y la regla de refresco existe.

*Censo v1 — 4 de noviembre de 2026.*
