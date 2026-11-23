#!/usr/bin/env python3
"""Verificador mecánico de mundo-dirsi.

Comprueba en un comando los invariantes que la auditoría de
coherencia del 23 nov 2026 tuvo que verificar a mano, y que la
sesión encontró rotos tres veces en un día: el tablero STATUS.md
describía el 16 nov como si fuera hoy (7 días desfasado, 2
vencimientos cumplidos sin marcar), el índice del README no
listaba un archivo, y una referencia cruzada estaba rota.

Uso:
    python3 herramientas/chequeo-repo.py            # sobre este repo
    python3 herramientas/chequeo-repo.py /ruta/al/repo

Lee un directorio plano; no usa git, no toca la red, no escribe
nada. Sin dependencias. Salida: una línea OK/FAIL/SKIP por
comprobación y un resumen. Código de salida 0 si todo lo
ejecutado pasa; 1 si algo falla.

Regla de diseño: si el formato de un documento cambia y el
verificador ya no puede parsearlo, la comprobación FALLA en voz
alta (no se salta en silencio ni inventa cifras). Un FAIL por
formato es una señal de que hay que actualizar el script junto
con el documento, no de que el documento esté mal.

Fechas: se usa la fecha local de la máquina. Los vencimientos
son fechas de Caracas; una corrida en la franja 00:00–04:00 UTC
puede juzgar un vencimiento con un día de error. Los umbrales
(7 y 30 días) tienen margen para eso; el vencimiento de hoy se
juzga por fecha, no por hora.
"""

import re
import sys
from datetime import date
from pathlib import Path

RAIZ_DEFECTO = Path(__file__).resolve().parent.parent
OK, FAIL, SKIP = "OK", "FAIL", "SKIP"

# Umbrales (días). El tablero se actualiza "cuando algo cambia de
# estado"; 7 días es el desfase que la auditoría del 23 nov 2026
# encontró y declaró inaceptable. El inventario se refresca con
# cadencia mensual (su propia regla).
UMBRAL_TABLERO_DIAS = 7
UMBRAL_INVENTARIO_DIAS = 30
TOPE_HILOS_ACTIVOS = 12

MESES = {
    "ene": 1, "enero": 1, "feb": 2, "febrero": 2, "mar": 3, "marzo": 3,
    "abr": 4, "abril": 4, "may": 5, "mayo": 5, "jun": 6, "junio": 6,
    "jul": 7, "julio": 7, "ago": 8, "agosto": 8, "sep": 9, "sept": 9,
    "septiembre": 9, "oct": 10, "octubre": 10, "nov": 11,
    "noviembre": 11, "dic": 12, "diciembre": 12,
}
MESES_ABREV = ["", "ene", "feb", "mar", "abr", "may", "jun",
               "jul", "ago", "sep", "oct", "nov", "dic"]

# Referencias .md en backticks que NO viven en este repo y son
# legítimas. Clasificación de la auditoría del 23 nov 2026
# (97 referencias revisadas: solo RESULTADOS.md estaba rota):
#  - archivos del workspace local o de otros repos, citados por
#    su nombre sin ruta (MEMORY.md, AGENTS.md, LOG.md, ...);
#  - material de la calibración de la escala, que vive en el
#    directorio local calibracion-escala-2026-11-18/ (trabajo.md,
#    MAPA-CIEGO-2.md, CRITERIOS.md, puntuacion-A/B.md);
#  - nombres genéricos (CONNECTOR.md, CLAUDE.md, agents.md,
#    readme.md): el patrón, no un archivo concreto.
# Un nombre nuevo que no esté aquí FALLA en voz alta: la
# auditoría mensual lo clasifica (o se corrige la referencia).
PERMITIDAS_EXTERNAS = {
    # Workspace local / otros repos (verificados 23 nov 2026).
    "MEMORY.md", "AGENTS.md", "LOG.md",
    "RESUMEN-block-ethos-backend-2TANDA.md", "improvement-log.md",
    "SEMILLA.md", "LEEME.md", "muse-lab-log.md", "sintesis-completa.md",
    "entradas-2026-10-27/11-skills-youtube-ia-maestra.md",
    # Material de la calibración de la escala (directorio local).
    "trabajo.md", "MAPA-CIEGO-2.md", "CRITERIOS.md",
    "puntuacion-A.md", "puntuacion-B.md",
    # Nombres genéricos.
    "SKILL.md", "MANTENIMIENTO.md", "CONNECTOR.md", "CLAUDE.md",
    "agents.md", "readme.md",
}

resultados = []
RAIZ = RAIZ_DEFECTO
HOY = date.today()


def registrar(nombre, estado, detalle=""):
    resultados.append((nombre, estado, detalle))
    linea = f"[{estado}] {nombre}"
    if detalle:
        linea += f" — {detalle}"
    print(linea)


def leer(rel):
    return (RAIZ / rel).read_text(encoding="utf-8")


def parse_fecha_es(texto):
    """Fecha española con o sin día de semana y con o sin «~».

    Acepta «16 de noviembre de 2026», «jue 19 nov 2026, ~20:20»,
    «~mié 26 nov 2026», «3 dic 2026». Devuelve date o None.
    """
    m = re.search(
        r"~?\s*(?:\w{3,5}\s+)?(\d{1,2})\s+(?:de\s+)?([a-záéíóú]+)"
        r"\s+(?:de\s+)?(\d{4})",
        texto.lower(),
    )
    if not m:
        return None
    mes = MESES.get(m.group(2))
    if not mes:
        return None
    try:
        return date(int(m.group(3)), mes, int(m.group(1)))
    except ValueError:
        return None


def seccion(texto, titulo):
    """El contenido bajo «## <titulo>» hasta el siguiente «## »."""
    m = re.search(r"^## " + re.escape(titulo) + r".*$",
                  texto, re.M)
    if not m:
        return None
    resto = texto[m.end():]
    m2 = re.search(r"^## ", resto, re.M)
    return resto[:m2.start()] if m2 else resto


def lineas_sin_cercas(texto):
    """Líneas fuera de bloques de código cercados, con su número."""
    dentro = False
    for i, linea in enumerate(texto.splitlines(), 1):
        if linea.strip().startswith("```"):
            dentro = not dentro
            continue
        if not dentro:
            yield i, linea


# ------------------------------------------------------------------ STATUS.md

def check_status_fecha():
    """La fecha del tablero no tiene más de 7 días."""
    status = leer("STATUS.md")
    m = re.search(r"\*\*Tablero al (\d{1,2}) de ([a-z]+) de (\d{4})\.\*\*",
                  status)
    if not m:
        registrar("status-fecha", FAIL,
                  "no se encontró «**Tablero al …**» en STATUS.md")
        return
    mes = MESES.get(m.group(2))
    try:
        fecha = date(int(m.group(3)), mes, int(m.group(1)))
    except (ValueError, TypeError):
        registrar("status-fecha", FAIL, f"fecha ilegible: {m.group(0)}")
        return
    edad = (HOY - fecha).days
    if edad < 0:
        registrar("status-fecha", FAIL, f"tablero fechado en el futuro: {fecha}")
    elif edad > UMBRAL_TABLERO_DIAS:
        registrar("status-fecha", FAIL,
                  f"tablero del {fecha.isoformat()} ({edad} días)")
    else:
        registrar("status-fecha", OK, f"tablero del {fecha.isoformat()} ({edad} días)")


def check_status_vencimientos():
    """Ningún vencimiento de la tabla «Próximos vencimientos» ha pasado."""
    status = leer("STATUS.md")
    sec = seccion(status, "Próximos vencimientos")
    if sec is None:
        registrar("status-vencimientos", FAIL,
                  "falta la sección «Próximos vencimientos»")
        return
    vencidos, sin_fecha, total = [], [], 0
    for linea in sec.splitlines():
        if not linea.startswith("|") or "---" in linea or "Fecha" in linea:
            continue
        total += 1
        celda = linea.split("|")[1] if "|" in linea else ""
        fecha = parse_fecha_es(celda)
        if fecha is None:
            sin_fecha.append(celda.strip())
        elif fecha < HOY:
            vencidos.append(f"{celda.strip()} ({fecha.isoformat()})")
    if vencidos or sin_fecha:
        detalle = "; ".join(
            (["vencidos: " + "; ".join(vencidos)] if vencidos else [])
            + (["sin fecha legible: " + "; ".join(sin_fecha)] if sin_fecha else []))
        registrar("status-vencimientos", FAIL, detalle)
    else:
        registrar("status-vencimientos", OK, f"{total} vencimientos, ninguno pasado")


def _tabla_marcador(texto):
    """(resueltas, confirmadas, parciales, refutadas, acierto, pendientes).

    Se busca en todo el archivo: en CALIBRACION.md vive bajo
    «## Marcador», pero en STATUS.md vive bajo «## Calibración».
    Es la única fila de 6 números con «%» en ambos archivos.
    """
    m = re.search(r"^\| (\d+) \| (\d+) \| (\d+) \| (\d+) \| (\d+) % \| (\d+) \|",
                  texto, re.M)
    return tuple(int(g) for g in m.groups()) if m else None


def _marcador_recalculado(calibracion):
    """El marcador rehecho desde las entradas de CALIBRACION.md.

    Resueltas: filas «| C-00X | … | Resultado | fecha | … |» de la
    sección Resueltas. Pendientes: entradas «### C-00X» de la
    sección Pendientes cuyo encabezado no dice RESUELTA (C-003
    vive en Pendientes pero está resuelta: su texto queda donde se
    escribió, y el registro no mueve entradas).
    """
    res = seccion(calibracion, "Resueltas")
    pen = seccion(calibracion, "Pendientes")
    if res is None or pen is None:
        return None
    conf = parc = ref = 0
    for m in re.finditer(r"^\| C-\d+ \|[^|]*\| (Confirmada|Parcial|Refutada) \|",
                         res, re.M):
        if m.group(1) == "Confirmada":
            conf += 1
        elif m.group(1) == "Parcial":
            parc += 1
        else:
            ref += 1
    pendientes = 0
    for m in re.finditer(r"^### (C-\d+ .*)$", pen, re.M):
        if "RESUELTA" not in m.group(1):
            pendientes += 1
    resueltas = conf + parc + ref
    acierto = round((conf + 0.5 * parc) / resueltas * 100) if resueltas else 0
    return (resueltas, conf, parc, ref, acierto, pendientes)


def check_status_marcador():
    """El marcador de STATUS.md == el de CALIBRACION.md == el recalculado."""
    status = leer("STATUS.md")
    calibracion = leer("CALIBRACION.md")
    m_status = _tabla_marcador(status)
    m_cal = _tabla_marcador(calibracion)
    m_calc = _marcador_recalculado(calibracion)
    if m_status is None or m_cal is None or m_calc is None:
        registrar("status-marcador", FAIL,
                  "no se pudo parsear alguna tabla de marcador")
        return
    if m_status == m_cal == m_calc:
        registrar("status-marcador", OK,
                  f"{m_calc[0]} resueltas, {m_calc[4]} % de acierto, "
                  f"{m_calc[5]} pendiente(s)")
    else:
        registrar("status-marcador", FAIL,
                  f"STATUS {m_status} vs CALIBRACION {m_cal} "
                  f"vs recalculado {m_calc}")


def check_status_censo():
    """Las cifras del censo en STATUS.md coinciden con el inventario."""
    status = leer("STATUS.md")
    inv = leer("INVENTARIO-CAPACIDADES.md")
    problemas = []

    def numero(patron, texto, etiqueta):
        m = re.search(patron, texto)
        if not m:
            problemas.append(f"sin parsear: {etiqueta}")
            return None
        return tuple(int(g) for g in m.groups())

    s_con = numero(r"\*\*(\d+) conectores\*\*", status, "conectores en STATUS")
    i_con = numero(r"\*\*(\d+) conectores con documentación\*\*", inv,
                   "conectores en inventario")
    s_cli = numero(r"\*\*(\d+) CLIs\*\*", status, "CLIs en STATUS")
    i_cli = numero(r"\*\*(\d+) CLIs en /opt/hatch/bin\*\*", inv,
                   "CLIs en inventario")
    s_ski = numero(r"\*\*(\d+) \+ (\d+) skills\*\*", status, "skills en STATUS")
    i_ski = numero(r"\*\*Skills: (\d+) del sistema \+ (\d+) propias\*\*", inv,
                   "skills en inventario")
    for etiqueta, a, b in [("conectores", s_con, i_con), ("CLIs", s_cli, i_cli),
                           ("skills", s_ski, i_ski)]:
        if a is not None and b is not None and a != b:
            problemas.append(f"{etiqueta}: STATUS {a} vs inventario {b}")

    m_ref = re.search(r"\*\*Último refresco: ([^*]+)\*\*", status)
    refrescos = re.findall(r"Refresco (\d{1,2}) (\w+) (\d{4})", inv)
    f_status = parse_fecha_es(m_ref.group(1)) if m_ref else None
    f_inv = None
    for d, mes, a in refrescos:
        mes_n = MESES.get(mes.lower())
        if mes_n:
            try:
                f = date(int(a), mes_n, int(d))
                f_inv = f if f_inv is None or f > f_inv else f_inv
            except ValueError:
                pass
    if f_status is None:
        problemas.append("sin parsear: último refresco en STATUS")
    elif f_inv is None:
        problemas.append("sin parsear: refresco en el inventario")
    elif f_status != f_inv:
        problemas.append(f"refresco: STATUS {f_status} vs inventario {f_inv}")

    if problemas:
        registrar("status-censo", FAIL, "; ".join(problemas))
    else:
        registrar("status-censo", OK,
                  f"{s_con[0]} conectores, {s_cli[0]} CLIs, "
                  f"{s_ski[0]}+{s_ski[1]} skills, refresco {f_status}")


def check_status_banco():
    """STATUS.md menciona la última corrida del banco (fecha y puntuación)."""
    status = leer("STATUS.md")
    banco = leer("BANCO-DE-PRUEBAS.md")
    sec = seccion(banco, "Registro de corridas")
    if sec is None:
        registrar("status-banco", FAIL, "falta «Registro de corridas»")
        return
    filas = re.findall(
        r"^\| (\d{4}-\d{2}-\d{2}) \|[^|]*\|[^|]*\| \*\*(\d+/\d+)\*\*",
        sec, re.M)
    if not filas:
        registrar("status-banco", FAIL, "sin filas de corrida parseables")
        return
    fecha_iso, puntuacion = filas[-1]
    y, m, d = (int(x) for x in fecha_iso.split("-"))
    fecha_es = f"{d} {MESES_ABREV[m]} {y}"
    faltan = []
    if fecha_es not in status:
        faltan.append(f"fecha {fecha_es}")
    if puntuacion not in status:
        faltan.append(f"puntuación {puntuacion}")
    if faltan:
        registrar("status-banco", FAIL,
                  f"última corrida {fecha_iso} {puntuacion}: falta en STATUS: "
                  + ", ".join(faltan))
    else:
        registrar("status-banco", OK,
                  f"última corrida {fecha_iso} ({puntuacion}) citada en STATUS")


def check_frescura_inventario():
    """El último refresco del inventario no tiene más de 30 días."""
    inv = leer("INVENTARIO-CAPACIDADES.md")
    refrescos = re.findall(r"Refresco (\d{1,2}) (\w+) (\d{4})", inv)
    ultimo = None
    for d, mes, a in refrescos:
        mes_n = MESES.get(mes.lower())
        if mes_n:
            try:
                f = date(int(a), mes_n, int(d))
                ultimo = f if ultimo is None or f > ultimo else ultimo
            except ValueError:
                pass
    if ultimo is None:
        registrar("frescura-inventario", FAIL, "sin fecha de refresco parseable")
        return
    edad = (HOY - ultimo).days
    if edad > UMBRAL_INVENTARIO_DIAS:
        registrar("frescura-inventario", FAIL,
                  f"último refresco {ultimo.isoformat()} ({edad} días)")
    else:
        registrar("frescura-inventario", OK,
                  f"último refresco {ultimo.isoformat()} ({edad} días)")


# ------------------------------------------------------- índice y referencias

def check_indice_readme():
    """Cada .md del repo está en el índice del README, y viceversa."""
    readme = leer("README.md")
    indice = seccion(readme, "Índice")
    if indice is None:
        registrar("indice-readme", FAIL, "falta la sección «Índice»")
        return
    listados = set(re.findall(r"`([^`\n]+)`", indice))
    problemas = []
    for token in sorted(listados):
        if token.endswith("/"):
            if not (RAIZ / token).is_dir():
                problemas.append(f"directorio listado pero ausente: {token}")
        elif token.endswith(".md"):
            if not (RAIZ / token).is_file():
                problemas.append(f"archivo listado pero ausente: {token}")
    for p in sorted(RAIZ.rglob("*.md")):
        rel = str(p.relative_to(RAIZ))
        if rel == "README.md":
            continue  # el README no se lista a sí mismo
        cubierto = rel in listados or any(
            rel.startswith(d) for d in listados if d.endswith("/"))
        if not cubierto:
            problemas.append(f"sin indexar: {rel}")
    if problemas:
        registrar("indice-readme", FAIL, "; ".join(problemas))
    else:
        registrar("indice-readme", OK, "índice y archivos coinciden")


def check_referencias():
    """Cada referencia .md en backticks o en enlace resuelve en el repo.

    Legítimas sin resolver aquí: rutas externas («~/…», «/…») y los
    nombres de PERMITIDAS_EXTERNAS. Las referencias dentro de
    bloques de código cercados no se comprueban (son ejemplos).
    """
    basenames = {}
    for p in RAIZ.rglob("*.md"):
        basenames.setdefault(p.name, []).append(p)
    problemas = []
    for p in sorted(RAIZ.rglob("*.md")):
        texto = p.read_text(encoding="utf-8")
        rel = str(p.relative_to(RAIZ))
        for i, linea in lineas_sin_cercas(texto):
            for token in re.findall(r"`([^`\n]+\.md)`", linea):
                if token.startswith("~/") or token.startswith("/"):
                    continue
                if token in PERMITIDAS_EXTERNAS:
                    continue
                if "/" in token:
                    if not (RAIZ / token).is_file():
                        problemas.append(f"{rel}:{i} «{token}» no existe")
                elif token not in basenames:
                    problemas.append(f"{rel}:{i} «{token}» no existe")
            for destino in re.findall(r"\]\(([^)\s]+\.md)\)", linea):
                if destino.startswith("http"):
                    continue
                if (p.parent / destino).is_file() or (RAIZ / destino).is_file():
                    continue
                problemas.append(f"{rel}:{i} enlace a «{destino}» no existe")
    if problemas:
        registrar("referencias", FAIL, "; ".join(problemas))
    else:
        registrar("referencias", OK, "todas las referencias .md resuelven")


def check_conteos_readme():
    """Las cifras que el README cita coinciden con sus fuentes."""
    readme = leer("README.md")
    problemas = []

    def compara(etiqueta, esperado, real):
        if esperado is None:
            problemas.append(f"sin parsear: {etiqueta} en el README")
        elif esperado != real:
            problemas.append(f"{etiqueta}: README {esperado} vs fuente {real}")

    m = re.search(r"(\d+) fichas \(D-01–D-(\d+)\)", readme)
    decisiones = leer("aprendido/decisiones.md")
    nums = [int(n) for n in re.findall(r"^## D-(\d+)", decisiones, re.M)]
    if m:
        compara("fichas de decisiones", int(m.group(1)), len(nums))
        if nums and int(m.group(2)) != max(nums):
            problemas.append(f"última ficha: README D-{m.group(2)} "
                             f"vs fuente D-{max(nums):02d}")
    else:
        problemas.append("sin parsear: fichas de decisiones en el README")

    m = re.search(r"(\d+) rutas", readme)
    rutas = leer("por-aprender/rutas.md")
    compara("rutas", int(m.group(1)) if m else None,
            len(re.findall(r"^## Ruta", rutas, re.M)))

    m = re.search(r"(\d+) preguntas", readme)
    preguntas = leer("por-aprender/preguntas-abiertas.md")
    compara("preguntas abiertas", int(m.group(1)) if m else None,
            len(re.findall(r"^## [0-9]", preguntas, re.M)))

    glosario = leer("GLOSARIO.md")
    decl = re.findall(r"\((\d+) entradas", glosario)
    compara("entradas del glosario",
            int(decl[-1]) if decl else None,
            len(re.findall(r"^- \*\*", glosario, re.M)))

    if problemas:
        registrar("conteos-readme", FAIL, "; ".join(problemas))
    else:
        registrar("conteos-readme", OK, "decisiones, rutas, preguntas y glosario")


# ------------------------------------------------------------- hilos abiertos

def check_hilos_revision():
    """Cada hilo activo tiene fecha de revisión vigente, dueño y disparo.

    Formato (ver la propuesta de hilos con fecha de revisión): cada
    hilo ABIERTO o EN-ESPERA lleva «- **Revisión:** AAAA-MM-DD».
    """
    hilos = leer("HILOS-ABIERTOS.md")
    bloques = re.split(r"^### (H-\d+ — .+)$", hilos, flags=re.M)
    # bloques: [preámbulo, título1, cuerpo1, título2, cuerpo2, ...]
    problemas, activos = [], 0
    for k in range(1, len(bloques), 2):
        titulo, cuerpo = bloques[k], bloques[k + 1]
        codigo = titulo.split(" — ")[0]
        m_estado = re.search(r"\*\*Estado:\*\*\s*([A-Z-]+)", cuerpo)
        estado = m_estado.group(1) if m_estado else None
        if estado in ("ABIERTO", "EN-ESPERA"):
            activos += 1
            m_rev = re.search(r"\*\*Revisión:\*\*\s*(\d{4}-\d{2}-\d{2})", cuerpo)
            if not m_rev:
                problemas.append(f"{codigo}: sin fecha de revisión")
            else:
                try:
                    y, mo, d = (int(x) for x in m_rev.group(1).split("-"))
                    if date(y, mo, d) < HOY:
                        problemas.append(
                            f"{codigo}: revisión vencida ({m_rev.group(1)})")
                except ValueError:
                    problemas.append(f"{codigo}: fecha de revisión ilegible")
            if "**Dueño:**" not in cuerpo:
                problemas.append(f"{codigo}: sin dueño")
            if "**Disparo de cierre:**" not in cuerpo:
                problemas.append(f"{codigo}: sin disparo de cierre")
    if activos > TOPE_HILOS_ACTIVOS:
        problemas.append(f"{activos} hilos activos, tope {TOPE_HILOS_ACTIVOS}")
    if problemas:
        registrar("hilos-revision", FAIL, "; ".join(problemas))
    else:
        registrar("hilos-revision", OK, f"{activos} hilo(s) activo(s) con revisión vigente")


def main():
    global RAIZ
    if len(sys.argv) > 1:
        RAIZ = Path(sys.argv[1]).resolve()
    if not (RAIZ / "STATUS.md").is_file():
        print(f"error: {RAIZ} no parece mundo-dirsi (falta STATUS.md)")
        return 2
    check_status_fecha()
    check_status_vencimientos()
    check_status_marcador()
    check_status_censo()
    check_status_banco()
    check_frescura_inventario()
    check_indice_readme()
    check_referencias()
    check_conteos_readme()
    check_hilos_revision()
    n_ok = sum(1 for _, e, _ in resultados if e == OK)
    n_fail = sum(1 for _, e, _ in resultados if e == FAIL)
    n_skip = sum(1 for _, e, _ in resultados if e == SKIP)
    print(f"\n{n_ok} OK, {n_fail} FAIL, {n_skip} SKIP "
          f"({len(resultados)} comprobaciones)")
    return 1 if n_fail else 0


if __name__ == "__main__":
    sys.exit(main())
