# P-04 · Nota del administrador (NO entregar al solucionador)

Versión del material: v1, preparado el 5 nov 2026.

## Diferencia intencionada

Exactamente una: `GET /api/version` (nuevo). El inventario después debe
tener 3 endpoints; cualquier otra diferencia es no intencionada.

## Verificación del material (5 nov 2026)

Inventario base generado de primera mano con `rg` sobre
`~/workspace/rag-demo/app.py`: 2 endpoints (`GET /api/health`,
`POST /preguntar`). No se modificó `app.py` al preparar el material.

## Regla de versionado

Si la app o el cambio semilla cambian, se versiona (v2) y la comparación
se reinicia para P-04, según el diseño del banco.
