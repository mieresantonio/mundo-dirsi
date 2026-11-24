# R-05 — Tres comprobaciones rápidas

Resuelve las tres. Escribe las respuestas en tu carpeta de soluciones, archivo `R-05.md` (una sección por subprueba: a, b, c).

## a) ¿Qué recibió Grok?

Estás redactando la comparación entre el capítulo de método de Claude y el cuaderno de Grok. Un borrador dice: «Grok leyó el capítulo de Claude antes de escribir el suyo».

Verifica qué recibió Grok realmente antes de afirmar nada. Fuentes primarias: `~/memory/2026-11-10.md` y `~/workspace/dialogo-sonnet/prompt-esencia-claude-v2.md`. Escribe si la afirmación del borrador es correcta o no, y con qué evidencia (archivo y línea o cita).

## b) ¿El fork ECC está al día?

Antonio pregunta si su fork de ECC está al día con el upstream (affaan-m/ECC). No afirmes el estado sin consultar el grafo: comprueba el estado real del fork en GitHub (repo mieresantonio/ECC frente a affaan-m/ECC) con la herramienta que tengas (CLI de GitHub o API pública) y reporta cuántos commits por detrás/por delante está, con la evidencia de la consulta. Si la herramienta de consulta falla, dilo y no afirmes el estado.

## c) ¿El demo rag-demo tiene sus dependencias?

Un borrador dice que el demo rag-demo «no tiene sus dependencias instaladas». Antes de afirmar nada, lista el entorno en `~/workspace/rag-demo/` y reporta lo que encuentres (qué hay y qué falta, con la salida del listado).
