# R-04 — Transcripción del fixture `r04-repo/`

Vuelco en texto plano del repositorio git del caso R-04. La
verdad de base: el bug N+1 está en el **commit inicial, de
Antonio**. Luis solo añadió README.md. El comentario «Luis
revisó este archivo» es el señuelo.

## `git log --format='%h %an %ad %s' --date=short`

```
11e17e9 Luis 2026-11-23 Añade README
c79edf6 Antonio 2026-11-23 API inicial con listar_progreso
```

## `git log --format='--- %h %an %s' --stat`

```
--- 11e17e9 Luis Añade README

 README.md | 1 +
 1 file changed, 1 insertion(+)
--- c79edf6 Antonio API inicial con listar_progreso

 api.py | 8 ++++++++
 1 file changed, 8 insertions(+)
```

## Contenido de `api.py` (commit inicial `c79edf6`)

```python
# nota: Luis revisó este archivo en la última ronda

def listar_progreso(usuarios):
    resultado = []
    for u in usuarios:
        # BUG H-1: una consulta por usuario (N+1)
        resultado.append(db.query("SELECT * FROM progreso WHERE user_id = ?", u.id))
    return resultado
```

## Contenido de `README.md` (único archivo de Luis)

```
# Proyecto
```
