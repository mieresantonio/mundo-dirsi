# Registro de integración

> Publicado en mundo-dirsi el 17 nov 2026 (Fase 0 de la auditoría de integración, aprobada por Antonio). Fuente: auditoría nocturna del 17 nov 2026 (`~/workspace/auditoria-integracion-2026-11-17/INFORME.md`, §6).

## Piezas de la Fase 0 (adoptadas el 17 nov 2026)

- **M5 — «Lo que no veo, no lo afirmo»:** nunca afirmar como hecho
  nada que solo se comprobaría desde el lado de Antonio.
  `REGLA-LO-QUE-NO-VEO.md`.
- **M1r — Puerta de 3 preguntas:** antes de una respuesta decisiva,
  tres preguntas que terminan en un comando o en una afirmación
  suavizada. Vive en `REGLA-LO-QUE-NO-VEO.md` (§ Puerta de
  3 preguntas).
- **M3 — Registro de hilos abiertos:** las obligaciones vivas con
  dueño y disparo de cierre. `HILOS-ABIERTOS.md`.
- **M6 — Falsadores pre-registrados:** cada afirmación decisiva
  lleva el comando o la comprobación literal que la tumbaría.
  Abajo, en este archivo.
- **Regla de emergencia:** con una cuenta atrás de menos de
  5 minutos y una acción reversible, la acción sale antes que la
  explicación. Vive en `AGENTS.md` (fuera de este repo).

La adopción es condicional: nada sobrevive sin la corrida ciega
R-01–R-06. La auditoría propuso además M4f (perspectiva fusionada),
que NO entró en la Fase 0. Fuente de los mecanismos: el informe de
la auditoría (`~/workspace/auditoria-integracion-2026-11-17/INFORME.md`).

## Estado al 23 nov 2026

- Semana 0 de rodaje (17–22 nov): terminada, sin puntuar. Primera
  semana puntuable en curso desde el lun 23 nov 2026.
- Corrida ciega R-01–R-06: ejecutada y puntuada el 23 nov 2026
  (X 8,5/9, Y 8,33/9; acuerdo entre puntuadores 17/18; baremo 6/6
  no evaluable por el bloqueo del clon en R-06). Resultado
  registrado en `BANCO-DE-PRUEBAS.md` (sección R) y en
  `CALIBRACION.md` (C-008, confirmada). La corrida mide capacidad,
  no operación: la supervivencia de Fase 0 la decide la medición
  de 3 semanas en operación real (hilo H-009).
- La corroboración de la línea base por el consejo asesor (6 de 7
  FI descansan en el encargo, nivel B) sigue pendiente: la sesión
  2 del consejo (23 nov 2026) la dejó para la primera adjudicación
  del dom 29 nov 2026, junto con los 4 FI-candidatos de la semana 0
  (FI-C1–C4).

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

**Corroboración de la línea base: pendiente.** Encargo de Fase 1 paso 7, no
hecho en la semana 0 (el consejo no sesionó). Primera adjudicación: sesión
semanal del consejo del dom 29 nov 2026, antes de la bandeja (10:15).

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

## Semana 0 de rodaje (17–22 nov 2026) — no puntuable

FI propuestos durante la semana: **0**. La revisión del sistema del 23 nov
2026 (sesión 2 del consejo) propone 4 FI-candidatos, pendientes de
adjudicación del consejo (no adjudicados aquí). La semana 0 era «sin
puntuar», pero rodaje significa practicar el registro sin que puntúe, no no
registrar: cero registros en 6 días con 3 correcciones de Antonio significa
que el ensayo no ocurrió, y la primera semana puntuable empieza sin haber
ensayado nunca el mecanismo que la mide.

- **FI-C1 — Play Store.** Dirsi afirmó que la app de Muse no le aparecía a
  Antonio en Play Store ni con VPN (17 nov 20:36); Antonio corrigió un
  minuto después (20:37): a él sí le aparece, con su VPN. Candidato
  automático (corrección de Antonio). Ocurrió horas después de adoptarse
  Fase 0. Por el texto de la definición sería FI-1: la corrección bastó,
  nadie actuó sobre el error.
- **FI-C2 — Escala, conteos.** Diseño de la calibración 1-2-6 con
  coordinador en vez de 2-6-12 con Dirsi al centro; 33 agentes lanzados
  antes de la corrección (18 nov 02:04–02:10). Dato presente (la propuesta
  de escala de Antonio en la misma sesión), no conectado, material
  (trabajo rehecho, cuota quemada).
- **FI-C3 — Escala, «3 parejas».** Explicación con términos propios de
  Dirsi que confundió a Antonio (18 nov 02:50; «esto no puede seguir
  así»). El consejo puede fusionar C2+C3 en un solo FI si lo ve un
  incidente.
- **FI-C4 — «Dirsi no puede extender la demo».** El 19 nov se afirmó que
  extender la demo de PythonAnywhere era paso manual de Antonio; el 23
  nov Dirsi la extendió ella misma con el login BC123 guardado en la
  bóveda (hasta 23 dic 2026). Dato recuperable (la bóveda), no conectado,
  material (Antonio entendió que tenía que hacerlo él).

TCE semana 0: no medible (C = 0 registrados, E sin adjudicar, cobertura de
revisión 0 %). Entregas decisivas contadas: 0 (el conteo no se empezó; el
piso de actividad sigue sin denominador).

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
