# Plantilla: especificación de una app

Rellena antes de construir. Si un campo no se sabe, se escribe "pendiente
de decisión" y no se inventa.

## Problema y usuario
- ¿Qué problema resuelve y para quién?
- ¿Qué hace el usuario en una frase?

## Flujo principal (el único que decide si está lista)
1. <!-- Paso 1 -->
2. <!-- Paso 2 -->
3. <!-- Resultado visible -->

## Funcionalidades
- Incluye: <!-- lista corta -->
- NO incluye: <!-- pagos, panel admin, API oficial, datos reales, etc. -->

## Datos
- Modelo mínimo (entidades y campos).
- Reglas de negocio (horarios, bloqueos, límites, validaciones).
- Todo dato ficticio lleva la etiqueta "datos de ejemplo".

## Stack
- Frontend, backend, base de datos. Justificar en una línea cada elección.
- Servicios de pago: ninguno salvo que se pida explícitamente.

## Criterio de "listo"
- Un visitante puede completar el flujo sin ayuda y verificar el resultado.
- Si eso no funciona, la app no está lista aunque se vea bien.

## Verificación obligatoria
- Build sin errores, flujo real contra el servidor, casos borde probados.
- Servidores de prueba detenidos y base limpia al terminar.
