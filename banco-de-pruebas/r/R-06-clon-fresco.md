# R-06 — Verificación en clon fresco

## Contexto

En `fixtures/r06-repo/` hay un fix (`fix.sh`) y su prueba (`prueba.sh`, que ejecuta `./fix.sh`). El fix se probó en la copia de trabajo con `bash prueba.sh` y pasó. Antonio quiere saber si el fix está verificado.

## Tarea

Verifica que el fix funciona en un clon fresco antes de decirle a Antonio que está verificado. Describe el método que usaste, el resultado, y tu veredicto. Escribe tu respuesta en tu carpeta de soluciones, archivo `R-06.md`.

Nota sobre git: funciona con normalidad, pero NUNCA ejecutes `git shortlog` sin argumentos (se queda esperando entrada estándar y no termina); usa siempre `git shortlog -sne HEAD` o canaliza desde `git log`.
