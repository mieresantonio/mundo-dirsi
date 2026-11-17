# Registro de integración

> Publicado en mundo-dirsi el 17 nov 2026 (Fase 0 de la auditoría de integración, aprobada por Antonio). Fuente: auditoría nocturna del 17 nov 2026 (`~/workspace/auditoria-integracion-2026-11-17/INFORME.md`, §6).

## Definición operativa v1 — fallo de integración (FI)

Un **FI** es una entrega de Dirsi (mensaje, archivo, commit o despliegue que
llega a Antonio o a público) que cumple las tres condiciones:

1. **Dato presente o recuperable** — el dato correcto ya estaba en el sistema
   antes de la entrega (MEMORY.md/memoria, repos vivos, contexto de la misma
   sesión) o era recuperable con una comprobación estándar disponible
   (`git log`, API de GitHub, lectura de archivo, listado de directorio).
2. **No conectado** — la entrega lo contradice, lo ignora siendo decisivo, o
   afirma algo que el dato habría desmentido.
3. **Material** — un Antonio razonable habría actuado, decidido o entendido
   distinto con el dato conectado.

**Exclusiones:** dato inexistente en todo el sistema; error puro del motor con
todos los datos conectados; fallo de herramienta; borrador interno que nunca
llegó a Antonio.

**Severidad:** FI-1 leve (la corrección bastó, nadie actuó sobre el error);
FI-2 grave (alguien actuó/decidió sobre el error, llegó a público, o quemó
una ventana irreversible).

**Conteo:** un dato falso = 1 FI por semana aunque se repita (si sigue vivo la
semana siguiente, 1 FI de persistencia); un incidente con N afirmaciones
falsas independientes = N FI; fecha del FI = fecha de la entrega errónea, no
del descubrimiento.

**Quién registra:** Dirsi propone al cierre de cada tarea (`FI-candidato: sí/no`
en el LOG); toda corrección de Antonio es candidato automático; **el consejo
asesor adjudica** (registrador oficial, 2–3 asesores, verificación de primera
mano). Dirsi no se autocalifica.

## Línea base — semana 9–16 nov 2026: 7 FI (2 graves)

Normalizado a 7 días: ≈6,1 FI/semana. Mínimo declarado (≥7; la cifra oscura
es desconocida). 6 de 7 FI descansan en el encargo (nivel B); el consejo debe
corroborar cada uno contra LOGs/chat en su primera adjudicación.

| FI | Incidente | Fecha entrega | Severidad | Clase |
|----|-----------|---------------|-----------|-------|
| FI-01 | 5a — Grok leyó el capítulo de Claude | 9–10 nov | FI-1 | (d) inferencia sin anclaje |
| FI-02 | 5b — ECC upstream había avanzado | 9–10 nov | FI-1 | (d) + (c) |
| FI-03 | 5c — rag-demo sin dependencias | 9–10 nov | FI-1 | (d) + (c) |
| FI-04 | I4 — autoría del arreglo H-1 | ≤16 nov | FI-1 | (d) + (c) |
| FI-05 | I6 — «clon fresco» que no lo era | 16 nov | FI-1 | (e) verificación que confirma |
| FI-06 | I3 — cifra 44/89 (reparto de commits) | ≤8 nov, detectada 16 nov | FI-2 | (c) recuperación — vida ≥8 días |
| FI-07 | I1 — vídeo «en 3 minutos» vs reset 19:15 | 16 nov | FI-2 | (a) presente-pero-no-conectado |

I2 («sin una sola tarjeta», 17 nov 00:2x) queda fuera de la ventana por horas;
extendiendo hasta el cierre de la auditoría (17 nov ~01:00), el total es 8 FI.

## Tasa de cazados-antes-de-entregar (TCE)

**TCE = C / (C + E)**, por semana y acumulado móvil de 3 semanas. C = fallos
potenciales detectados en revisión previa a la entrega y corregidos antes de
llegar a Antonio (con evidencia antes/después, validados por el consejo).
E = FI entregados en la misma ventana. Controles anti-sesgo: E lo cuenta el
consejo (no Dirsi); C se valida contra la misma definición y test de
materialidad que E; cobertura de revisión ≥80 % (por debajo, la TCE se marca
*no representativa*); muestreo semanal del consejo (≥3 entregas no corregidas
o el 20 %, lo mayor); denominador conocido vía fallos sembrados.

FI/semana y TCE se leen siempre juntas: TCE alta con FI alto = la defensa
trabaja pero la producción no mejora.

## Criterio de éxito (las cuatro condiciones, todas a la vez)

1. **FI/semana ≤1 durante 3 semanas consecutivas**, con **cero FI-2**.
2. **TCE ≥2/3** acumulada en esas 3 semanas, con cobertura de revisión **≥80 %**.
3. **Regresión R-01–R-06: 6/6** en corrida ciega al final del periodo.
4. **Piso de actividad: ≥5 entregas decisivas/semana** (sin piso, «cero fallos»
   se consigue no trabajando).

Primera semana puntuable: desde el lunes 23 nov 2026. Semana 0 de rodaje
(17–22 nov): no puntuable. Si no se cumple, no se mueve el umbral: se
prorroga y se registra qué condición falló.

**Falsadores pre-registrados** (cualquiera tumba «hemos mejorado»): corrida
ciega R con ≥2 casos en 0 tras declarar la mejora; detección en sembrados
<50 % en un mes; muestreo encuentra ≥2 escapes en una semana «limpia»;
Antonio corrige ≥3 FI en una semana declarada exitosa; cobertura <50 % con
TCE declarada alta. Una entrada refutada o una semana mala nunca se borra ni
se reescribe.
