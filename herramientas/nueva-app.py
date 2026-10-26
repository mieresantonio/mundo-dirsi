#!/usr/bin/env python3
"""Scaffolder de proyectos para mundo-dirsi.

Uso:
    python3 nueva-app.py <nombre> --tipo frontend|api|fullstack [--dest DIR] [--force]

Crea un esqueleto de proyecto:
  - frontend / fullstack: README.md, package.json, vite.config.js,
    index.html, src/main.jsx, src/App.jsx (pantalla de saludo)
  - api / fullstack: app.py (GET /api/health), requirements.txt
  - fullstack: si existe plantilla-app/ junto a este script, se copia
    entera y se adapta el nombre; si no, se genera el mismo esqueleto
    en línea.

Nunca sobrescribe un directorio no vacío salvo que se pase --force.
Solo biblioteca estándar de Python 3.
"""

import argparse
import json
import re
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
TEMPLATE_DIR = HERE / "plantilla-app"

FRONTEND_FILES = {
    "vite.config.js": """import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/api': 'http://localhost:5000',
    },
  },
})
""",
    "index.html": """<!doctype html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{name}</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>
""",
    "src/main.jsx": """import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
""",
    "src/App.jsx": """export default function App() {
  return (
    <main style={{ fontFamily: 'system-ui, sans-serif', maxWidth: 640, margin: '4rem auto', padding: '0 1rem' }}>
      <h1>¡Hola, {name}! 👋</h1>
      <p>Proyecto generado con nueva-app.py (mundo-dirsi).</p>
    </main>
  )
}
""",
}

BACKEND_FILES = {
    "app.py": '''"""Backend Flask de {name}.

Arrancar con:  python3 app.py
Escucha en:    http://localhost:5000
"""

from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/api/health")
def health():
    return jsonify({"status": "ok", "app": "{name}"})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
''',
    "requirements.txt": "Flask>=3.0\n",
}


def package_json(name):
    return json.dumps(
        {
            "name": name,
            "private": True,
            "version": "0.1.0",
            "type": "module",
            "scripts": {"dev": "vite", "build": "vite build", "preview": "vite preview"},
            "dependencies": {"react": "^18.3.1", "react-dom": "^18.3.1"},
            "devDependencies": {"@vitejs/plugin-react": "^4.3.1", "vite": "^5.4.0"},
        },
        indent=2,
        ensure_ascii=False,
    ) + "\n"


def readme_md(name, tipo):
    parts = {
        "frontend": "Frontend React + Vite.",
        "api": "API Flask.",
        "fullstack": "Frontend React + Vite y API Flask.",
    }
    lines = [f"# {name}", "", parts[tipo], ""]
    if tipo in ("frontend", "fullstack"):
        lines += ["```bash", "npm install", "npm run dev", "```", ""]
    if tipo in ("api", "fullstack"):
        lines += ["```bash", "pip install -r requirements.txt", "python3 app.py", "```", ""]
    if tipo in ("api", "fullstack"):
        lines += ["## Endpoints", "", "- `GET /api/health` → `{\"status\": \"ok\"}`", ""]
    return "\n".join(lines)


def write_file(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def generate_inline(target, name, tipo):
    created = []
    if tipo in ("frontend", "fullstack"):
        write_file(target / "package.json", package_json(name))
        created.append("package.json")
        for rel, template in FRONTEND_FILES.items():
            # .replace, no .format: las plantillas JS contienen llaves propias.
            write_file(target / rel, template.replace("{name}", name))
            created.append(rel)
    if tipo in ("api", "fullstack"):
        for rel, template in BACKEND_FILES.items():
            write_file(target / rel, template.replace("{name}", name))
            created.append(rel)
    write_file(target / "README.md", readme_md(name, tipo))
    created.append("README.md")
    return created


def copy_template(target, name):
    shutil.copytree(TEMPLATE_DIR, target, dirs_exist_ok=True)
    # Adaptar el nombre en los archivos que lo mencionan.
    pkg_path = target / "package.json"
    try:
        pkg = json.loads(pkg_path.read_text(encoding="utf-8"))
        pkg["name"] = name
        pkg_path.write_text(json.dumps(pkg, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    except (ValueError, OSError):
        pass
    for rel in ("index.html", "src/App.jsx", "app.py", "README.md"):
        p = target / rel
        if p.exists():
            text = p.read_text(encoding="utf-8").replace("plantilla-app", name)
            p.write_text(text, encoding="utf-8")
    # La plantilla saluda como "mundo-dirsi": adaptar el saludo al proyecto.
    appjsx = target / "src" / "App.jsx"
    if appjsx.exists():
        text = appjsx.read_text(encoding="utf-8").replace(
            "¡Hola, mundo-dirsi!", f"¡Hola, {name}!")
        appjsx.write_text(text, encoding="utf-8")
    return sorted(str(p.relative_to(target)) for p in target.rglob("*") if p.is_file())


def valid_name(name):
    return bool(re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]*", name))


def main(argv=None):
    parser = argparse.ArgumentParser(description="Crea un esqueleto de proyecto (mundo-dirsi).")
    parser.add_argument("nombre", help="Nombre del proyecto (también nombre del directorio).")
    parser.add_argument("--tipo", required=True, choices=["frontend", "api", "fullstack"],
                        help="Tipo de proyecto.")
    parser.add_argument("--dest", default=".", help="Directorio padre (por defecto: actual).")
    parser.add_argument("--force", action="store_true",
                        help="Permitir escribir sobre un directorio no vacío.")
    args = parser.parse_args(argv)

    if not valid_name(args.nombre):
        print(f"error: nombre inválido {args.nombre!r} "
              "(usa letras, números, '.', '_' o '-', sin empezar por punto/guion)", file=sys.stderr)
        return 2

    target = (Path(args.dest).expanduser() / args.nombre).resolve()
    if target.exists() and any(target.iterdir()) and not args.force:
        print(f"error: {target} ya existe y no está vacío; usa --force para sobrescribirlo",
              file=sys.stderr)
        return 1
    target.mkdir(parents=True, exist_ok=True)

    if args.tipo == "fullstack" and TEMPLATE_DIR.is_dir():
        created = copy_template(target, args.nombre)
        print(f"fullstack: plantilla copiada desde {TEMPLATE_DIR}")
    else:
        created = generate_inline(target, args.nombre, args.tipo)

    print(f"creado: {target}")
    for rel in created:
        print(f"  {rel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
