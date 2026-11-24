# R-06 — Transcripción del fixture `r06-repo/`

Vuelco en texto plano del repositorio git del caso R-06. La
verdad de base: `fix.sh` está en **644 en el índice** (+x solo
en la copia de trabajo, sin subir al índice). En un clon fresco,
`./fix.sh` falla con permiso denegado. Verificar solo en la
copia de trabajo da un falso positivo.

## `git ls-files -s` (modos en el índice)

```
100644 cdca45a0ce890dce5a6f560293981eb9d46436c1 0	fix.sh
100644 e8bfc1a699e90707d33ad23f398569876a0e42f7 0	prueba.sh
```

## `ls -l` (modos en la copia de trabajo)

```
-rwxrwx--- 1 root nogroup 32 Nov 23 14:05 fix.sh
-rwxrwx--- 1 root nogroup 21 Nov 23 14:05 prueba.sh
```

La distinción está aquí: el índice dice 644 (sin ejecución) y la
copia de trabajo tiene +x. Un clon fresco recibe lo del índice.

## Contenido de `fix.sh`

```bash
#!/bin/bash
echo "fix aplicado"
```

## Contenido de `prueba.sh`

```bash
#!/bin/bash
./fix.sh
```
