# P-03 · Nota del administrador (NO entregar al solucionador)

Versión del material: v1, preparado el 5 nov 2026.

## Elemento faltante plantado

La ruta `/certificados` NO aparece en ninguna parte del paquete
(`dist/index.html` ni `dist/assets/app.js`). Todo lo demás prometido
sí está como cadena literal:

- `/inicio`, `/modulos`, `/laboratorio` — en `ROUTES` de `app.js`
- `https://BC123.pythonanywhere.com/api/progreso` — compuesto como
  `API_BASE` + `/api/progreso` en `app.js`
- `/api/tutor/preguntar` — en `askTutor()` de `app.js`

## Verificación del material (5 nov 2026)

```sh
cd banco-de-pruebas/p-03/dist
rg -o "/inicio|/modulos|/laboratorio|/certificados|api/progreso|api/tutor/preguntar" .
# Esperado: todo presente salvo /certificados (0 ocurrencias).
```

Resultado al preparar: `/inicio` 1, `/modulos` 1, `/laboratorio` 1,
`/certificados` 0, `api/progreso` 1, `api/tutor/preguntar` 1.

## Regla de versionado

Si este material cambia, se versiona (v2) y la comparación se reinicia
para P-03, según el diseño del banco.
