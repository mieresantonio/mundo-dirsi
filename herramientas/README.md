# herramientas/ — mundo-dirsi

Herramientas propias de Dirsi para crear y revisar proyectos.
Python 3, solo biblioteca estándar, sin dependencias externas.
No se crea ningún repositorio git ni se despliega nada desde aquí.

## 1. nueva-app.py — scaffolder de proyectos

```bash
python3 nueva-app.py <nombre> --tipo frontend|api|fullstack [--dest DIR] [--force]
```

Crea un esqueleto de proyecto:

| Tipo | Archivos |
|---|---|
| `frontend` | `README.md`, `package.json`, `vite.config.js`, `index.html`, `src/main.jsx`, `src/App.jsx` (pantalla de saludo) |
| `api` | `README.md`, `app.py` (`GET /api/health` → JSON), `requirements.txt` |
| `fullstack` | Todos los anteriores. Si existe `plantilla-app/` junto al script, se copia entera y se adapta el nombre; si no, se genera el mismo esqueleto en línea. |

Reglas:

- Se niega a escribir sobre un directorio no vacío (salida 1) salvo que se pase `--force`.
- El nombre solo admite letras, números, `.`, `_` y `-` (no puede empezar por punto o guion).

Ejemplos:

```bash
python3 nueva-app.py mi-web --tipo frontend --dest /tmp
python3 nueva-app.py mi-api --tipo api
python3 nueva-app.py mi-app --tipo fullstack --dest ~/workspace
```

## 2. chequeo-app.py — comprobador de proyectos (solo lectura)

```bash
python3 chequeo-app.py <directorio> [--build]
```

Informa:

- Presencia de README (`README.md`, `README` o `readme.md`).
- Archivos de build presentes (`package.json`, `requirements.txt`, `vite.config.js`, `pyproject.toml`, etc.).
- Recuento de archivos fuente por extensión.
- Escaneo de secretos: patrones de clave AWS (`AKIA…`), token de GitHub (`ghp_…`),
  asignaciones de `api_key`/`secret`, tokens `Bearer` y cabeceras de clave privada.
  Reporta **solo archivo, línea y tipo de patrón: NUNCA imprime el valor coincidente**.
  Se omiten `node_modules`, `dist`, `venv`, `.git`, `__pycache__` y similares.

Con `--build`, si existe `package.json`, intenta `npm run build` e informa
éxito/fracaso; un fallo de build **no** hace fallar la comprobación.

Código de salida: `0` sin secretos, `1` si se halló al menos uno,
`2` si el directorio no existe. El resultado del build nunca cambia el código.

Ejemplo:

```bash
python3 chequeo-app.py ./mi-app --build
```

## 3. plantilla-app/ — plantilla fullstack mínima

React + Vite (frontend) + Flask (backend), solo código fuente
(sin `node_modules`, `venv`, `dist` ni artefactos generados):

- `package.json`, `vite.config.js`, `index.html`, `src/main.jsx`,
  `src/App.jsx` (saluda y consulta `/api/health`)
- `app.py` (`GET /api/health` → `{"status": "ok"}`), `requirements.txt`
- `README.md`

```bash
pip install -r plantilla-app/requirements.txt
python3 plantilla-app/app.py   # backend en http://localhost:5000
npm install && npm run dev    # frontend (proxy /api → :5000)
```

## Probado (2026-10-26, real, en /tmp; todo borrado tras las pruebas)

- `nueva-app.py` para los 3 tipos (`frontend`, `api`, `fullstack`): **OK** —
  6, 3 y 8 archivos creados respectivamente, listados y verificados.
- `fullstack` sin plantilla (script copiado solo a /tmp): **OK** — genera el
  esqueleto en línea (8 archivos, `app.py` compila).
- `python3 -m py_compile` de los `app.py` generados y de la plantilla: **OK**.
- `package.json` generados y de la plantilla como JSON válido: **OK (3/3)**.
- Rechazo de sobrescritura sin `--force`: **OK** (salida 1, mensaje claro);
  con `--force`: **OK** (salida 0).
- `chequeo-app.py` sobre un proyecto generado: **OK** (README sí, 3 archivos
  de build, 7 fuentes, 0 secretos, salida 0).
- `chequeo-app.py` sobre `~/workspace/mundo-dirsi` (solo lectura): **OK**
  (14 fuentes en ese momento, 0 secretos; el README del repo ya
  existe desde el 26 oct 2026 y el repo tiene hoy 27 archivos).
- Escaneo de secretos con archivo falso (`ghp_FAKE…`, `AKIA…`, `api_key`,
  `Bearer`, cabecera de clave privada): **OK** — 5 hallazgos con archivo,
  línea y tipo; **ningún valor apareció en la salida** (verificado con grep).
- `--build` con dependencias instaladas: **ÉXITO** (build de Vite real);
  sin `node_modules`: **FALLO reportado, chequeo sigue con salida 0**.
- Bug hallado y corregido durante las pruebas: `.format()` rompía con las
  llaves del JS de las plantillas (se cambió a `.replace("{name}", …)`),
  y el saludo de la plantilla copiada no adaptaba el nombre (corregido).
