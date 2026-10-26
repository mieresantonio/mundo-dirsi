# Checklist: verificación antes de entregar

No se entrega nada sin pasar por aquí.

1. **Archivos en su sitio:** el código está en el directorio prometido y el
   README existe y describe cómo correrlo.
2. **Build:** `npm run build` (frontend) o `py_compile` (Python) sin errores.
3. **Flujo real:** arrancar el servidor y ejercer el flujo principal con
   peticiones reales: crear → comprobar el efecto → caso borde (solape,
   dato inválido, inexistente) → cancelar o borrar → comprobar que el
   estado volvió a quedar limpio.
4. **Contenido:** sin textos copiados de material de curso; redacción propia.
   Sin secretos en código, logs ni informes.
5. **Limpieza:** ningún servidor en marcha, ningún puerto ocupado por
   pruebas, base de datos solo con seed.
6. **Informe:** qué se entregó, evidencia de cada paso (códigos y
   resultados), y lo recortado o fallido dicho en claro.
7. **Límites:** nada desplegado, ningún repo creado, ningún otro proyecto
   tocado, salvo que el encargo lo pidiera explícitamente.
