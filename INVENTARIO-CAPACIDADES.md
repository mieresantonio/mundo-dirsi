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

*(Reverificado el 16 nov 2026: mismos valores — 4 vCPU, 7,7 GB de RAM,
150 GB de disco con 145 libres, Node v24.22.1, Python 3.12.3.)*

## 2. Cachés que ya guardan tesoro

- **Playwright: 681 MB** — Chromium completo (1248), Chromium headless
  shell y un ffmpeg propio. Es el ojo visual de
  `~/workspace/tools-visual/shot.mjs` (páginas locales, escritorio y
  móvil). El Chromium local **no sale a internet** desde la VM; las URL
  públicas van por el navegador en vivo.
- **HuggingFace: 458 MB** — el modelo de embeddings del demo RAG
  (paraphrase-multilingual-MiniLM-L12-v2) ya está descargado: el RAG
  puede correr sin descargar nada.

*(Reverificado el 16 nov 2026: 681 MB y 458 MB, sin cambios; el
Chromium sigue siendo la build 1248.)*

## 3. Superficie Muse

- **129 CLIs en /opt/hatch/bin** *(refresco del 16 nov 2026: el censo
  decía ~120; el conteo directo de hoy da 129)*. Por familias: Google Workspace
  (gmail, calendario, drive, docs, sheets…), GitHub, redes (Facebook,
  Instagram, Threads, Messenger), Meta Ads y catálogo, comercio
  (Shopify, Stripe, Shop Pay), viajes (Expedia, Agoda, Duffel,
  OpenTable, Ticketmaster, FlightAware), trabajo (Notion, Asana,
  Linear, Todoist, **Slack**, Zoom, Calendly), medios (generación de
  imagen/vídeo/audio, TTS, Spotify, búsqueda de imágenes), sistema
  (medidor de suscripción, almacenamiento remoto, Tailscale, datos del
  dispositivo, lector de códigos QR/barras `zbar-lib`).
- **90 conectores con documentación** *(refresco del 16 nov 2026: el
  conteo directo de `/opt/hatch/connectors/` da hoy 90 carpetas, las
  90 con su `CONNECTOR.md` — 11 más que los 79 del 9 nov; el entorno
  cambió entre despliegues, como la regla de refresco prevé. El censo
  del 4 nov decía 74; la verificación de primera mano del 5 nov
  recogida en `RECOPILACION-MATERIALES.md` ya contó 79)*. Conectados y verificados en uso:
  Gmail, Google Calendar, Drive, Docs, Sheets, Dropbox, GitHub.
  **Existe conector y CLI de Slack** — la nota vieja decía que no había;
  existe, con su conexión sin verificar. Que un conector exista no
  significa que la cuenta esté conectada: eso se comprueba por servicio
  antes de prometer nada con él.
- **Skills: 57 del sistema + 9 propias** (ingeniería inversa en sala
  limpia, explicaciones claras al negarse, verificación de artefactos
  antes de publicar, notas de skills recuperadas, comprobación de
  todas las fuentes antes de concluir una ausencia, dirección de cine
  y vídeo con IA, sistema de diseño vitrina para interfaces,
  verificación de la colocación de credenciales tras una configuración
  de acceso, y verificación de una herramienta gratuita antes de
  recomendarla) *(refresco del 16 nov 2026: el conteo directo de hoy
  da 57 carpetas con su `SKILL.md` en el directorio de skills del
  sistema — sin cambios — y 9 entre las propias del workspace; la
  novena es la de verificación de herramientas gratuitas, creada el
  14 nov. El 9 nov se corrigió de 56 + 4 a 57 + 8; las cuatro propias
  de entonces se crearon entre el 5 y el 7 nov)*. Entre las del sistema
  hay varias casi sin uso (traducción, campañas, finanzas, formularios,
  comparador de hipotecas…): están para cuando una tarea las pida, no
  para memorizarlas.
- **Bóveda segura: guarda logins.** El navegador en vivo guarda además
  las sesiones que Antonio abrió en él.

## 4. Automatismos vivos (4 nov 2026)

- De Antonio, tres: **dos revisiones quincenales de forks** y la
  **bandeja semanal de decisiones**. El resto de trabajos en
  la lista son del sistema (Feed, doctor horario, heartbeat)
  *(corregido el 9 nov 2026 en la operación de mejora: antes decía
  dos —la revisión quincenal de un fork y una verificación única de
  pesos de un modelo—; la lista de trabajos de hoy muestra tres de
  Antonio y ya no muestra aquella verificación única)*.
- El teléfono emparejado expone **43 comandos y 10 fuentes de datos**,
  sin comando de galería ni de archivos *(corregido el 9 nov 2026 en
  la operación de mejora: antes decía 41 comandos; hoy la lista del
  dispositivo declara 43 y su descripción completa permite
  enumerarlos uno a uno —43, sin ninguno de galería ni de archivos—,
  y las fuentes de datos siguen siendo 10)*.

## 5. Herramientas construidas por el propio sistema

- `~/workspace/tools-visual/` — el ojo: capturas locales en escritorio y
  móvil (`shot.mjs`) y de URL vía navegador en vivo cuando aplica.
- Runbook de despliegue de Block Ethos, kit de prueba de concepto de
  destilación Kimi K3, scripts de audio (8D, mezclas) en el workspace.
- La capa de medición: `CALIBRACION.md`, `BANCO-DE-PRUEBAS.md`,
  `PROTOCOLO-REFUTACION.md`.

## 6. Lo que este censo no puede ver

- El estado real de conexión de cada servicio: se comprueba por tarea,
  no por censo.
- Capacidades tras permisos que Antonio aún no ha otorgado.
- Lo que cambie entre despliegues de la VM: por eso la foto lleva fecha
  y la regla de refresco existe.

*Censo v1 — 4 de noviembre de 2026. Refresco 16 nov 2026: §1 y §2
reverificados sin cambios; §3 actualizado (90 conectores, 129 CLIs,
57 + 9 skills). Apéndice de refresco reproducible añadido el 16 nov
2026.*

## Apéndice: refresco reproducible (16 nov 2026)

El próximo refresco no debe deducir el método: es ejecutar esta lista
y anotar. Cada comando reproduce una cifra del censo; la salida
esperada es la del refresco del 16 nov 2026. Mismo comando, mismo
significado: así las cifras son comparables entre refrescos. Si un
comando no reproduce su cifra, se corrige el comando, no la cifra —
y si la cifra cambió de verdad (la VM se reemplaza entre despliegues),
se anota el cambio con su fecha, como hizo el refresco del 16 nov
con los conectores (79 → 90).

### §1 · La máquina

```
nproc                                    # → 4 (vCPU)
free -m                                  # → total 7934 MB (≈ 7,7 GB de RAM)
df -h ~                                  # → 150G total, 145G libres
node --version                           # → v24.22.1
python3 --version                        # → Python 3.12.3
command -v bun                           # → presente
ls /usr/bin | wc -l                      # → 910 binarios
uname -r                                 # → 7.0.0-44-generic (Linux 7.0)
```

Presentes (todos deben responder con una ruta):

```
for b in ffmpeg soffice gh jq sqlite3 curl wget rsync ssh zip unzip; do command -v $b; done
```

Ausentes (ninguno debe responder):

```
for b in docker magick convert pandoc yt-dlp ollama whisper java go rustc ruby php; do command -v $b; done
```

### §2 · Cachés

```
du -sh ~/.cache/ms-playwright           # → 681M
du -sh ~/.cache/huggingface             # → 458M
ls ~/.cache/ms-playwright/              # → chromium-1248, chromium_headless_shell-1248, ffmpeg-1013
```

### §3 · Superficie Muse

```
ls /opt/hatch/connectors/*/CONNECTOR.md | wc -l   # → 90 conectores con documentación
ls /opt/hatch/bin | wc -l                         # → 129 CLIs
ls /opt/muse/skills/*/SKILL.md | wc -l            # → 57 skills del sistema
ls ~/workspace/custom-skills/*/SKILL.md | wc -l   # → 9 skills propias
```

Verificación del apéndice (16 nov 2026): cada comando de esta lista
se ejecutó en esta máquina y su salida coincidió exactamente con la
cifra que el inventario declara.

