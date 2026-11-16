# Método Claude — Playbook del ingeniero senior (destilado operativo)

> Origen: documento «Playbook del Ingeniero Senior» v1.0.0, producido por Claude el 12 de noviembre de 2026 a petición de Antonio, en 3–4 sesiones de cuota. 982 líneas. El archivo original está archivado en privado (`~/workspace/dialogo-sonnet/2026-11-12-playbook-ingeniero-senior-claude.md`); este archivo es destilación con redacción propia: solo método, sin datos personales.
>
> La evaluación se hizo con el protocolo que el propio playbook exige al agente que lo recibe: adopto / ajusto / rechazo / falta. Veredicto en §1. Las afirmaciones de «nuevo» se comprobaron por búsqueda directa en METODO-CLAUDE.md, METODO-GROK.md, AGENTS.md y BANCO-DE-PRUEBAS.md (13 nov 2026).

## 1. Evaluación: adopto, ajusto, rechazo, falta

**Adopto** (detalle en §2): la regla de tres; las siete lentes; el ciclo de vida de lecciones con procedencia y confianza; las tareas de oro con métricas; el aviso de slopsquatting; la kata de práctica deliberada; el brief de delegación con supervisión escéptica y máximo 2 reintentos; las checklists de endpoint y despliegue; el esqueleto andante y los tests de caracterización; la carga modular (núcleo siempre + módulos por tipo de tarea).

**Ajusto**:
- El bloque de contexto del humano del playbook (§2): el stack por defecto que supone (Tailwind + shadcn) no es el de los proyectos reales (Block Ethos usa Bootstrap); la capa de IA real es FreeLLMAPI/Zen/OpenRouter, no solo la API de Claude/OpenAI. El bloque se reescribe con el stack real antes de instalarse en ningún agente.
- Las afirmaciones que dependen de versión (Express 4/5, WCAG 2.2, Core Web Vitals): se verifican contra la documentación de la versión instalada en el momento de usarlas, no se adoptan como hechos fijos. Es la propia regla del playbook.

**Rechazo**:
- Instalar el archivo completo tal cual en las instrucciones de Dirsi: el sistema ya tiene sus capas (memoria, AGENTS.md, skills, los dos métodos destilados) y una instalación íntegra duplicaría y chocaría. Se adopta esta destilación más la referencia por módulos, no el texto íntegro.

**Falta** (lo que el playbook no trae y el sistema ya tiene o debe añadir por su lado):
- Niveles de evidencia A/B/C/X (el sistema los tiene; el playbook solo trae etiquetas de confianza de tres niveles, útiles para el trabajo en curso).
- La economía de modelos por asiento (qué modelo para qué silla: rigor, arte, investigación) — el sistema la tiene.
- Las restricciones operativas propias (copia en el teléfono, caducidad de las tarjetas de aprobación) — viven en los archivos del sistema, no en el playbook.

## 2. Lo nuevo que se adopta (12 nov)

### 2.1 Regla de tres [adoptado 12 nov]
Si el mismo enfoque falla tres veces, parar: escribir qué se sabe, qué se descartó y qué no se entiende; cambiar de estrategia o preguntar. Insistir con variaciones al azar es señal de una suposición falsa. Al depurar, un cambio a la vez y comprobar el efecto tras cada cambio.

### 2.2 Siete lentes [adoptado 12 nov]
Mirar cada problema por siete lados: usuario (qué intenta lograr y qué le estorba), datos (dónde vive la verdad de cada dato; un solo dueño por dato), fallos (cómo se rompe), tiempo (qué pasa con 10× datos o usuarios, y dentro de seis meses), adversario (cómo lo abusaría alguien), operación (cómo se despliega, se observa y se revierte) y coste (tiempo, dinero y complejidad: ¿compensa?).

### 2.3 Ciclo de vida de lecciones [adoptado 12 nov]
Toda lección nace candidata (vista una vez; se aplica con cautela), se confirma (reproducida o respaldada por documentación oficial, o útil en al menos 2 tareas), se promueve (útil en al menos 3 tareas distintas sin contraejemplos; la promoción a regla se propone como diff y la aprueba un humano) o se retira (contradicha por evidencia nueva, obsoleta por un cambio de versión, o sin uso en 90 días; se marca obsoleta con el motivo, no se borra en silencio). Cada lección lleva procedencia: observado, documentado o inferido; las inferidas no se promueven sin verificar. Si el archivo de lecciones pasa de unas 150 líneas, consolidar (agrupar por tema, resumir, archivar lo antiguo).

### 2.4 Tareas de oro con métricas [adoptado 12 nov]
Conjunto pequeño (5–15) de tareas representativas con un criterio de éxito objetivo; se ejecutan antes y después de cambiar el método, el modelo o las lecciones promovidas. Métricas: porcentaje completadas con tests en verde a la primera, iteraciones hasta el verde, defectos que se escapan, comentarios de revisión por PR, y tiempo y coste por tarea. Si un cambio empeora algo, se revierte. El banco de pruebas existente es pariente de esto (pruebas fijas con corridas registradas); lo nuevo es el bucle antes/después con métricas por cada cambio.

### 2.5 Slopsquatting [adoptado 12 nov]
Antes de instalar un paquete: verificar que existe, que es el correcto (nombre exacto, mantenimiento, descargas) y que la versión es compatible. Los modelos inventan nombres de paquetes y los atacantes registran esos nombres.

### 2.6 Kata de práctica deliberada [adoptado 12 nov]
Una vez por semana, o cuando no haya tareas: tomar la debilidad más repetida en el registro de errores, diseñar un ejercicio pequeño que la ataque (30–60 min en un repo de práctica), resolverlo, verificarlo contra la documentación o una solución de referencia, y registrar lo aprendido.

### 2.7 Brief de delegación y supervisión escéptica [adoptado 12 nov]
Un brief trae: objetivo en una frase, contexto mínimo suficiente, alcance (qué se puede tocar y qué no), restricciones, criterio de aceptación verificable (comandos y salida esperada), límite de intentos y formato del informe. El director verifica por su cuenta (tests, lint, build, diff) y nunca acepta el informe del trabajador como prueba. Máximo 2 reintentos; si sigue fallando, se rehace el plan (brief ambiguo o tarea demasiado grande) o el director hace la parte difícil. Sin secretos en los briefs ni en el contexto; nada llega a `main` sin revisión humana.

### 2.8 Checklists de endpoint y despliegue [adoptado 12 nov]
Nuevo endpoint: contrato escrito, autenticación y autorización por recurso, validación de entrada y límites de tamaño, códigos de estado y formato de error uniformes, paginación en listas, idempotencia en POST sensibles, tests de éxito/validación/permisos/no-encontrado, logs sin datos sensibles y sin N+1. Antes de desplegar: CI en verde, variables y secretos configurados, migraciones probadas y copia de seguridad hecha, plan de rollback y smoke test definidos, alertas y logs listos, aprobación humana si es producción.

### 2.9 Esqueleto andante y tests de caracterización [adoptado 12 nov]
Proyecto nuevo: primero repo, CI, lint, tests, `.env.example` y un «hola mundo» de extremo a extremo incluido el despliegue, antes de construir funcionalidad. Código heredado: antes de cambiarlo, tests de caracterización que fijan lo que hace hoy; cambios en pasos pequeños; no reescribir desde cero salvo evidencia clara de que el diseño actual bloquea el negocio.

### 2.10 Carga modular [adoptado 12 nov]
Núcleo siempre cargado más módulos según el tipo de tarea (tabla de enrutado en §4). Pensado para agentes con contexto limitado (modelos pequeños, teléfono, laptop): cargar solo lo que la tarea exige, no el método entero.

## 3. Lo que ya era del sistema (solape; no se duplica)

- Orden fijo de revisión, filtro puntuado, prioridad y triaje con contención antes que arreglo, prueba de 9 puntos de «terminado de verdad», formato de crítica, alerta de 10 segundos, escalera de autonomía y regla de parada → METODO-CLAUDE.md.
- Regla del daño, clases P0–P3, cuatro clases de crítica, pase de 2 minutos, tres fallos de vigilancia, tres textos / una ficha / una pregunta → METODO-GROK.md.
- Revisión hostil del propio diff → el protocolo de refutación del sistema es más fuerte (lo corre un agente distinto, antes de lo decisivo, con clasificación refutada/debilitada/resiste).
- Pre-mortem → ya en METODO-CLAUDE.md.
- Memoria en archivos, skills, registro de calibración y banco de pruebas → ya existen; el playbook añade el ciclo de vida de lecciones y las métricas (§2.3, §2.4), no la idea.
- Verificar antes que suponer, evidencia sobre confianza, cambios pequeños, discrepar con respeto, reconocer errores rápido → práctica del sistema desde octubre; las 15 reglas de oro del playbook las formulan de forma compacta y numerada, útil como referencia rápida.

## 4. La referencia por dominios y cómo usarla

El grueso nuevo del playbook es la referencia por dominios: UI/UX, Frontend (React), Backend (Express/Flask), APIs, bases de datos, seguridad (OWASP aplicado), pruebas, depuración e incidentes, despliegue y operación, IA en productos, delegación y supervisión de agentes. Es conocimiento senior estándar, bien organizado; su valor es la organización y la completitud, no la novedad.

Uso:
- Dirsi lo consulta como referencia al trabajar en cada dominio; no se memoriza entero.
- Para agentes con contexto limitado (OpenCode en teléfono o laptop): núcleo más solo los módulos de la tarea.
- Las afirmaciones que dependen de versión se verifican contra la documentación instalada en el momento de usarlas.

Tabla de enrutado (resumida): pantalla o componente → UI/UX + Frontend + checklist de pantalla; endpoint o API → Backend + APIs + BD + seguridad + pruebas; esquema o consulta → BD + seguridad; bug → depuración + pruebas; deploy o CI/CD → despliegue + seguridad; función con IA → IA en productos + seguridad + Backend; delegar → delegación + plantilla de brief; proyecto nuevo → UI a BD + despliegue + kickoff; cerrar una tarea → aprendizaje.

## 5. Qué cambia en la práctica de Dirsi

1. Regla de tres activa en depuración y en tareas que se atascan.
2. Siete lentes como repaso rápido antes de entregar algo no trivial.
3. Las lecciones nuevas llevan procedencia y confianza, y se revisan con el ciclo de vida (§2.3).
4. Los cambios de método se miden con tareas de oro antes/después cuando el cambio lo justifica.
5. Verificación de paquetes antes de instalar (slopsquatting).
6. Briefs de delegación con criterio de aceptación verificable y máximo 2 reintentos.
7. Checklists de endpoint y despliegue en las tareas que toquen API o producción.

## Tarjeta de bolsillo

- Tres fallos iguales → para, escribe qué sabes y qué descartaste, cambia de enfoque.
- Siete lentes: usuario, datos, fallos, tiempo, adversario, operación, coste.
- Lección: procedencia + confianza + fecha; sin verificar no se promueve.
- Delegar: brief con criterio verificable; verificar tú mismo; 2 reintentos máximo.
- Paquete nuevo: verifica que existe y es el correcto antes de instalar.
- Método ≠ capacidad: el techo lo marca el modelo; el método hace que falle menos y más barato de corregir.

---
*Destilado el 13 nov 2026 por Dirsi, a partir del original archivado en privado. Redacción propia; las ideas son del playbook de Claude.*
