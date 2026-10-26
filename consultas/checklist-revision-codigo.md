# Checklist: revisión de código

Pasar por cada punto antes de dar un trabajo por terminado.

## Correctitud
- [ ] El flujo principal funciona de principio a fin, no solo la pantalla.
- [ ] Los casos borde están cubiertos (solapes, días cerrados, entradas vacías, IDs inexistentes).
- [ ] Los errores devuelven códigos y mensajes útiles (400, 404, 409), no trazas al usuario.

## Seguridad
- [ ] Ningún secreto en el código ni en los logs (claves, tokens, contraseñas).
- [ ] Entradas validadas; nada de concatenar SQL ni comandos con input del usuario.
- [ ] Los escaneos de secretos reportan ubicación y tipo, nunca el valor.

## Verificación
- [ ] El build pasa sin errores (`npm run build`, `py_compile`, o equivalente).
- [ ] El flujo se probó contra el servidor real, no solo leyendo el código.
- [ ] No queda ningún servidor de pruebas en marcha al terminar.
- [ ] La base de datos de prueba quedó limpia (solo seed).

## Alcance y documentación
- [ ] Nada fuera de lo pedido (sin pagos, sin paneles, sin despliegues no pedidos).
- [ ] README preciso: cómo correrlo, endpoints o rutas, y qué quedó fuera.
- [ ] Los datos de ejemplo están etiquetados como tales en la interfaz.
- [ ] Lo recortado o fallido se reporta en claro, no se esconde.
