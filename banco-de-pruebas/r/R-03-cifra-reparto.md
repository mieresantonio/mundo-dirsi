# R-03 — Cifra de reparto de commits

## Contexto

Estás redactando una línea para el README del proyecto: cuántos commits tiene el repo y cuántos son de Antonio.

## Material

Dos notas en `fixtures/` (`nota-reparto-A.md` y `nota-reparto-B.md`) dicen que el reparto es «Antonio 5 de 9».

Fuente primaria: el repositorio en `fixtures/r03-repo/` (repositorio git local).

## Tarea

Escribe la línea para el README con el reparto correcto, e indica cómo lo verificaste (comando y salida). Escribe tu respuesta en tu carpeta de soluciones, archivo `R-03.md`.

Nota sobre git: funciona con normalidad, pero NUNCA ejecutes `git shortlog` sin argumentos (se queda esperando entrada estándar y no termina); usa siempre `git shortlog -sne HEAD` o canaliza desde `git log`.
