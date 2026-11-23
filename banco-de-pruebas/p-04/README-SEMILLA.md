# P-04 · La semilla congelada (por qué `app-semilla.py` viaja con el material)

La prueba P-04 fija una app y un cambio semilla: el inventario de
endpoints antes y después del cambio solo debe diferir en lo
intencionado (`GET /api/version`). Para que la prueba sea reproducible
desde este repo, la app fijada viaja congelada aquí, en
`app-semilla.py`. Sin ella, la prueba dependería de un archivo local
(`~/workspace/rag-demo/app.py`) que puede moverse, cambiar o perderse.

## Qué es este archivo

Copia byte-exacta de `rag-demo/app.py` tal como estaba al preparar el
material v1 (5 nov 2026):

- **MD5:** `d976b50e1bee4b0a7efe9f0ee6ae21fc`
- **Tamaño:** 5.537 bytes, 150 líneas
- **Endpoints (2):** `GET /api/health`, `POST /preguntar`
  (ver `INVENTARIO-BASE.txt`, generado con el mismo método)

Verificación de la copia (23 nov 2026): el MD5 coincide con el de la
semilla verificada por el consejo asesor el 16 nov 2026 (sesión 1) y
con el archivo local, cuyo mtime sigue siendo 2 nov 2026, 22:08 UTC.
La copia no se editó: ni siquiera lleva una cabecera añadida, para que
el MD5 siga siendo la prueba de identidad.

## Por qué congelada: la app publicada ya divergió

La app viva de rag-demo (repo `mieresantonio/rag-demo-asistente-
documentos`) ya no es esta: en el clon del 23 nov 2026 tiene 3 rutas
(`GET /` nueva, `GET /api/health`, `POST /preguntar`), configuración
por variables de entorno y manejadores de error JSON. Si P-04 se
corriera contra la app viva, el inventario base sería otro y la
comparación v1 no valdría. Por eso la primera corrida de P-04 usa
esta semilla congelada, no la app viva.

## Reglas

- **No es código vivo.** No se ejecuta en producción, no se corrige,
  no se mejora. Si hay que cambiar la app de la prueba, se versiona
  el material (v2) según la regla de `P-04-ADMIN.md` y se congela una
  semilla nueva con su MD5.
- **La prueba corre sobre una copia de trabajo**, no sobre este
  archivo: se copia `app-semilla.py` a un directorio de trabajo, se
  aplica el cambio semilla de `SEMILLA.md` y se comparan los
  inventarios. Este archivo queda intacto como referencia.
- Para reproducir la prueba hacen falta además `rag_core.py` e
  `ingest.py` de rag-demo (la semilla los importa); el inventario de
  endpoints, que es lo que la prueba mide, se obtiene por lectura de
  los decoradores, sin ejecutar nada.

## Pregunta abierta (Q15)

La semilla congelada es la v1 tal como se preparó el 5 nov 2026 y
como la verificó el consejo asesor el 16 nov (MD5 `d976b50e…`).
Pero la copia local `~/workspace/rag-demo/app.py` NO está
sincronizada con GitHub: el HEAD publicado (MD5 `7423c8c3…`) tiene
3 rutas y endurecimiento que la copia local no tiene. Queda
pendiente decidir (Antonio/Dirsi): (a) si la semilla canónica de
P-04 es esta v1 congelada o una v2 rebasada sobre el HEAD de
GitHub; (b) si la copia del workspace se sincroniza con GitHub.
Registrado como pregunta abierta Q15 en
`por-aprender/preguntas-abiertas.md`. Confirmado en revisión
cruzada por el trabajador de rag-demo el 23 nov 2026 (14:10):
`app.py` en el clon fresco es idéntico al HEAD de GitHub; la
divergencia es anterior a la sesión, no un cambio de hoy.
