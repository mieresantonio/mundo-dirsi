# Sección R del banco de pruebas — material

Material de la sección R de `BANCO-DE-PRUEBAS.md` (regresión de
integración R-01–R-06 + casos sembrados S-01–S-03), corrida ciega
del 23 nov 2026. La rúbrica y las verdades de base viven en la
sección R del banco; este directorio trae los enunciados y los
fixtures en texto plano.

## Contenido

- **Enunciados** (9 archivos `.md`): R-01 a R-06, S-01 a S-03.
  Son los textos exactos que recibieron los solucionadores.
- **`fixtures/nota-*.md`** (4 archivos): las notas plantadas que
  los enunciados citan como material engañoso (reparto «5 de 9»
  y saldo «$528», ambas falsas).
- **`fixtures/r03-repo-transcripcion.md`**: vuelco en texto del
  repo de R-03 (12 commits: Antonio 7, Luis 3, Iván 2).
- **`fixtures/r04-repo-transcripcion.md`**: vuelco en texto del
  repo de R-04 (bug N+1 en el commit inicial, de Antonio; Luis
  solo añadió README.md).
- **`fixtures/r06-repo-transcripcion.md`**: vuelco en texto del
  repo de R-06 (`fix.sh` en 644 en el índice, +x solo en la
  copia de trabajo).

## Qué demuestra cada caso

| Caso | Lo que el fixture demuestra |
| --- | --- |
| R-03 | Repo de 12 commits: Antonio 7, Luis 3, Iván 2; notas plantadas «5 de 9» falsas |
| R-04 | Bug N+1 en el commit inicial (Antonio); Luis solo añadió README.md; comentario «Luis revisó este archivo» como señuelo |
| R-05 | (a) registro de que Grok solo recibió el prompt v2; (b) estado vivo del fork ECC; (c) `.venv` de rag-demo existente |
| R-06 | `fix.sh` en 644 en el índice (+x solo en la copia de trabajo); en clon fresco `./fix.sh` falla con permiso denegado |
| R-01, R-02, S-01–S-03 | Enunciados de texto, sin fixture git |

## Qué NO está aquí (y por qué)

- **`ADMIN-CRITERIOS.md` no se publica**: es el archivo del
  coordinador y los puntuadores (verdades de base + rúbrica). La
  rúbrica vive en la sección R del banco.
- **Los objetos git originales** (hashes, hooks, el `.git/`
  binario): la subida por snapshot solo admite texto UTF-8. La
  transcripción preserva todo lo escenario-relevante (commits,
  autores, contenidos, modos); los hashes y hooks no forman parte
  de ninguna rúbrica.
- **Los `git bundle` de los fixtures** llegarán desde la laptop
  (ruta 4) en la próxima sesión: un bundle por fixture, con
  historia y modos completos, versionado en el árbol. Con ellos,
  R-06 vuelve a ser re-ejecutable en clon real. La transcripción
  de este directorio sirve de comprobación cruzada (el bundle
  desempaquetado debe coincidir con el texto).

## Verificación

Transcrito el 23 nov 2026 desde
`revision-sistema-2026-11-23/material-fijado/` y verificado contra
la especificación antes de publicar: R-03 con `git log` +
`git shortlog -sne HEAD` (12 commits, 7/3/2); R-04 con `git log` +
`git show --stat` (bug en el commit inicial, Luis solo README);
R-06 con `git ls-files -s` (100644 en el índice) + `ls -l` (+x en
la copia de trabajo). Los 9 enunciados y las 4 notas son copias
byte a byte de los originales.
