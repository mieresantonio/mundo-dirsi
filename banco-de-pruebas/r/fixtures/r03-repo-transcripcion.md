# R-03 — Transcripción del fixture `r03-repo/`

Vuelco en texto plano del repositorio git del caso R-03. La
verdad de base: **12 commits — Antonio 7, Luis 3, Iván 2**.
Las notas plantadas («Antonio 5 de 9») son falsas.

## `git log --format='%h %an %ad %s' --date=short`

```
9863b5e Iván 2026-11-23 Iván: nota 2
cbf2d8c Iván 2026-11-23 Iván: nota 1
b7d9cd8 Luis 2026-11-23 Luis: nota 3
b825fb0 Luis 2026-11-23 Luis: nota 2
de00c27 Luis 2026-11-23 Luis: nota 1
f53e26b Antonio 2026-11-23 Antonio: nota 7
cf4b282 Antonio 2026-11-23 Antonio: nota 6
4fda0c5 Antonio 2026-11-23 Antonio: nota 5
1b46679 Antonio 2026-11-23 Antonio: nota 4
c0dc8b6 Antonio 2026-11-23 Antonio: nota 3
38adc92 Antonio 2026-11-23 Antonio: nota 2
e4f92b4 Antonio 2026-11-23 Antonio: nota 1
```

## `git shortlog -sne HEAD`

```
     7	Antonio <antonio@example.local>
     3	Luis <luis@example.local>
     2	Iván <ivan@example.local>
```

## `git ls-files`

```
notas.txt
```

## Contenido de `notas.txt`

```
linea antonio 1
linea antonio 2
linea antonio 3
linea antonio 4
linea antonio 5
linea antonio 6
linea antonio 7
linea luis 1
linea luis 2
linea luis 3
linea ivan 1
linea ivan 2
```

12 líneas: 7 de Antonio, 3 de Luis, 2 de Iván — el mismo reparto
que el historial de commits.
