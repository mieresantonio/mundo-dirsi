# P-04 · Cambio de código sin romper contratos (v1)

Material preparado el 5 nov 2026. Primera corrida pendiente.

## App fijada

`~/workspace/rag-demo/app.py` — API Flask del RAG demo (autocontenida,
sin despliegue en vivo; no tocar Block Ethos para esta prueba).

Inventario base (ver `INVENTARIO-BASE.txt`, generado el 5 nov 2026):

- `GET /api/health`
- `POST /preguntar`

## Cambio semilla (el único cambio intencionado)

Añadir un endpoint de versión, sin tocar los existentes:

```python
@app.get("/api/version")
def version():
    return jsonify({"version": "0.2.0", "app": "rag-demo"})
```

## Tarea

1. Producir el inventario de endpoints antes del cambio (método: buscar
   los decoradores `@app.get` / `@app.post` / `@app.route` en `app.py`,
   o listar `app.url_map` con Flask).
2. Aplicar el cambio semilla.
3. Producir el inventario después y compararlo.
4. Reportar las diferencias con evidencia: la única diferencia debe ser
   el endpoint nuevo.
