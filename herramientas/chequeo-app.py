#!/usr/bin/env python3
"""Comprobador de proyectos para mundo-dirsi (solo lectura, salvo --build).

Uso:
    python3 chequeo-app.py <directorio> [--build]

Informa:
  - presencia de README
  - archivos de build presentes (package.json, requirements.txt,
    vite.config.js, pyproject.toml, etc.)
  - recuento de archivos fuente por extensión
  - escaneo de secretos: busca patrones de secretos en el código y
    reporta SOLO archivo, número de línea y tipo de patrón.
    NUNCA imprime el valor coincidente.

Con --build, si existe package.json, intenta `npm run build` e informa
éxito/fracaso; un fallo de build NO hace fallar la comprobación entera.

Código de salida: 0 si no se hallaron secretos, 1 si se halló al menos
uno, 2 ante error de uso (directorio inexistente, etc.). El resultado
del build nunca cambia el código de salida.

Solo biblioteca estándar de Python 3.
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path

# Directorios que nunca se escanean ni se cuentan (artefactos, dependencias, VCS).
SKIP_DIRS = {
    ".git", ".hg", ".svn", "node_modules", "dist", "build", ".venv", "venv",
    "__pycache__", ".tox", ".pytest_cache", "coverage", ".next",
}

BUILD_FILES = [
    "package.json", "package-lock.json", "requirements.txt", "pyproject.toml",
    "vite.config.js", "vite.config.ts", "tsconfig.json", "Dockerfile",
    "Makefile", "Pipfile", "Gemfile", "composer.json", "go.mod",
]

# Solo se reporta el TIPO. El texto coincidente nunca se imprime ni se guarda.
SECRET_PATTERNS = [
    ("aws-access-key", re.compile(r"AKIA[0-9A-Z]{16}")),
    # Umbral bajo (12) a propósito: es un escáner heurístico y un token
    # real de GitHub tiene 36+ caracteres; mejor un falso positivo que
    # dejar pasar un token corto de ejemplo.
    ("github-token", re.compile(r"gh[pousr]_[A-Za-z0-9_]{12,}")),
    ("generic-api-key-assignment",
     re.compile(r"(?i)\b(api[_-]?key|apikey|secret[_-]?key|access[_-]?token)\b\s*[:=]\s*['\"][^'\"]+['\"]")),
    ("bearer-token", re.compile(r"Bearer\s+[A-Za-z0-9\-._~+/=]{20,}")),
    ("private-key-header", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),
    ("aws-secret-assignment",
     re.compile(r"(?i)\baws[_-]?secret[_-]?access[_-]?key\b\s*[:=]\s*['\"][^'\"]+['\"]")),
]

# Extensiones que cuentan como código/fuente para el recuento.
SOURCE_EXTS = {
    ".py", ".js", ".jsx", ".ts", ".tsx", ".html", ".css", ".scss",
    ".json", ".md", ".toml", ".yaml", ".yml", ".sh", ".sql",
}


def iter_files(root):
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.relative_to(root).parts):
            continue
        yield path


def scan_secrets(root):
    """Devuelve [(ruta_relativa, línea, tipo)] — jamás el valor."""
    findings = []
    for path in iter_files(root):
        try:
            text = path.read_text(encoding="utf-8", errors="strict")
        except (UnicodeDecodeError, OSError):
            continue  # binario o ilegible: se omite, no se vuelca
        rel = str(path.relative_to(root))
        for lineno, line in enumerate(text.splitlines(), start=1):
            for ptype, pattern in SECRET_PATTERNS:
                if pattern.search(line):
                    findings.append((rel, lineno, ptype))
    return findings


def main(argv=None):
    parser = argparse.ArgumentParser(description="Comprueba un proyecto (mundo-dirsi).")
    parser.add_argument("directorio", help="Directorio del proyecto a comprobar.")
    parser.add_argument("--build", action="store_true",
                        help="Intentar 'npm run build' si existe package.json.")
    args = parser.parse_args(argv)

    root = Path(args.directorio).expanduser().resolve()
    if not root.is_dir():
        print(f"error: {root} no existe o no es un directorio", file=sys.stderr)
        return 2

    print(f"proyecto: {root}")
    print()

    # README
    readme = next((p for p in ("README.md", "README", "readme.md") if (root / p).is_file()), None)
    print(f"README: {'sí (' + readme + ')' if readme else 'NO'}")

    # Archivos de build
    print("archivos de build:")
    for name in BUILD_FILES:
        if (root / name).is_file():
            print(f"  presente: {name}")
    print()

    # Recuento de fuentes
    counts = {}
    total = 0
    for path in iter_files(root):
        if path.suffix in SOURCE_EXTS:
            counts[path.suffix] = counts.get(path.suffix, 0) + 1
            total += 1
    print(f"archivos fuente: {total}")
    for ext in sorted(counts):
        print(f"  {ext}: {counts[ext]}")
    print()

    # Escaneo de secretos (solo ubicación + tipo, nunca valores)
    findings = scan_secrets(root)
    if findings:
        print(f"SECRETOS POSIBLES: {len(findings)} hallazgo(s) — revisa estos archivos:")
        for rel, lineno, ptype in findings:
            print(f"  {rel}:{lineno} [{ptype}]")
    else:
        print("secretos: ninguno detectado")
    print()

    # Build opcional
    if args.build:
        if (root / "package.json").is_file():
            print("build: ejecutando 'npm run build'…")
            try:
                result = subprocess.run(
                    ["npm", "run", "build"], cwd=root, capture_output=True,
                    text=True, timeout=300,
                )
                if result.returncode == 0:
                    print("build: ÉXITO")
                else:
                    print("build: FALLO (no hace fallar la comprobación)")
                    tail = (result.stderr or result.stdout or "").strip().splitlines()[-5:]
                    for line in tail:
                        print(f"    {line}")
            except FileNotFoundError:
                print("build: FALLO — 'npm' no está instalado")
            except subprocess.TimeoutExpired:
                print("build: FALLO — tiempo agotado (300 s)")
        else:
            print("build: omitido (no hay package.json)")
    print()
    print(f"resumen: secretos={len(findings)}")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
