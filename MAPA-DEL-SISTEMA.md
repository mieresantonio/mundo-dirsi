# Mapa del sistema en una página

De un vistazo: qué es el sistema, cómo encajan sus piezas y dónde
vive cada cosa. Verificado contra el contenido real del repo
(58 archivos en HEAD `f35bfcc`, 63 con esta publicación;
auditoría de coherencia del 23 nov 2026) y contra los archivos
del sistema que viven fuera de este repo (ver
`QUE-NO-ESTA-EN-ESTE-REPO.md`).

Regla de mantenimiento: este mapa se actualiza cuando nace o muere
una pieza del sistema (un documento nuevo en la raíz, un repo vivo
nuevo, un mecanismo de la capa de medición). La auditoría mensual
del repo comprueba que el mapa sigue diciendo la verdad. Un mapa
desactualizado es peor que no tener mapa: si una pieza cambió y el
mapa no, se corrige el mapa en la misma sesión, no «después».

## El dibujo

```
                    ┌──────────────────────────────┐
                    │      CAPA DE MEDICIÓN        │
                    │  registro · banco · refuta-  │
                    │  ción (desde el 3 nov 2026)  │
                    └──────┬───────────────┬───────┘
                           │ mide          │ mide
              ┌────────────▼───────┐  ┌────▼────────────┐
              │  LO QUE DIRSI      │  │  LO QUE DIRSI   │
              │  AFIRMA            │  │  HACE           │
              │  CALIBRACION.md    │  │  BANCO-DE-      │
              │  (11 entradas;     │  │  PRUEBAS.md     │
              │  9 resueltas,      │  │  (10 pruebas;   │
              │  77,8 % de acierto)│  │  6/6 línea base │
              └────────────┬───────┘  └────┬────────────┘
                           │               │
              ┌────────────▼───────────────▼────────────┐
              │              EL SISTEMA                  │
              │  todo lo que rodea al motor y persiste   │
              │                                          │
              │   ┌──────────────────────────────────┐   │
              │   │  MOTOR (Muse Spark 1.3)          │   │
              │   │  la primera inferencia; no vive  │   │
              │   │  en ningún repo                  │   │
              │   └──────────────┬───────────────────┘   │
              │                  │ lee y escribe         │
              │   ┌──────────────▼───────────────────┐   │
              │   │  MEMORIA  ·  ARCHIVOS  ·  REGLAS │   │
              │   │  MEMORY.md, ~/memory/  ·  este   │   │
              │   │  repo (mundo-dirsi)  ·  AGENTS.md│   │
              │   └──────────────┬───────────────────┘   │
              │                  │                       │
              │   ┌──────────────▼───────────────────┐   │
              │   │  PROCEDIMIENTOS  ·  SKILLS       │   │
              │   │  MANUAL-AGENTES, métodos desti-  │   │
              │   │  lados  ·  58+8 skills           │   │
              │   └──────────────┬───────────────────┘   │
              │                  │                       │
              │   ┌──────────────▼───────────────────┐   │
              │   │  REPOS VIVOS  ·  CONEXIONES      │   │
              │   │  8 repos (ver abajo)  ·  144     │   │
              │   │  conectores, 186 CLIs            │   │
              │   └──────────────┬───────────────────┘   │
              │                  │                       │
              │   ┌──────────────▼───────────────────┐   │
              │   │  AGENDA  ·  VIGILANCIA           │   │
              │   │  crons quincenales, vencimien-   │   │
              │   │  tos  ·  Fase 0 + consejo asesor │   │
              │   └──────────────────────────────────┘   │
              └──────────────────────────────────────────┘
```

Lectura del dibujo: el motor piensa; el sistema recuerda, ordena
y verifica. La capa de medición no es el sistema entero: es la
capa que lo mide (corrección de términos de Antonio, 3 nov 2026 —
«el sistema» existe desde oct 2026; lo creado el 3 nov es solo su
capa de medición). La vigilancia (Fase 0 + consejo asesor) no es
una capa más: es la revisión continua sobre todo lo demás.

## Las piezas y dónde viven

| Pieza | Qué es | Dónde vive |
|---|---|---|
| Motor | La primera inferencia; razona y escribe | No vive en ningún repo (cuenta de Muse) |
| Memoria | Lo que Dirsi sabe de Antonio y del trabajo: hechos, decisiones, personas | `MEMORY.md`, `~/memory/` (fuera de este repo) |
| Archivos del sistema | Este repo: lo aprendido, lo pendiente, los métodos, los registros | `mundo-dirsi` (este repo, público en GitHub) |
| Reglas de operación | Cómo trabaja Dirsi cada día: convenciones, lecciones, límites | `AGENTS.md` (fuera de este repo) |
| Procedimientos | Manual de agentes, métodos destilados (Claude, Grok, playbook, gpt-engineer) | `MANUAL-AGENTES.md`, `METODO-*.md`, `DESTILADO-LOVABLE-GPTENGINEER.md` |
| Skills | Métodos empaquetados reutilizables (58 de sistema + 8 propias) | `/opt/muse/skills/`, `~/workspace/custom-skills/` |
| Repos vivos | Los 8 proyectos activos de Antonio | GitHub `mieresantonio`: block-ethos, portfolio, mundo-vida-ia, rag-demo-asistente-documentos, fabrica-de-software, diseno-web-investigacion, mundo-dirsi, mieresantonio (perfil) |
| Conexiones | Accesos a cuentas y servicios (144 conectores, 186 CLIs) | `/opt/hatch/connectors/`, `/opt/hatch/bin/`; el censo vive en `INVENTARIO-CAPACIDADES.md` |
| Agenda | Revisiones quincenales, vencimientos, la bandeja semanal de decisiones | Programador de tareas (crons); los vencimientos, en `STATUS.md` |
| Capa de medición | Registro de calibración, banco de pruebas, protocolo de refutación | `CALIBRACION.md`, `BANCO-DE-PRUEBAS.md`, `PROTOCOLO-REFUTACION.md`; material reproducible en `banco-de-pruebas/p-03/` y `p-04/` |
| Vigilancia | Fase 0 (M5, M1r, M3, M6, regla de emergencia) + consejo asesor permanente | `REGISTRO-INTEGRACION.md`, `REGLA-LO-QUE-NO-VEO.md`, `HILOS-ABIERTOS.md`, `CONSEJO-ASESOR.md` |
| Auditoría de coherencia | Método para auditar un repo de documentos: índice contra archivos, cifras contra fuentes | `aprendido/auditoria-de-coherencia.md` |
| Escala de razonamiento | Niveles por número de agentes (bajo/medio/alto/extra/Max), en calibración | `ESCALA-RAZONAMIENTO-AGENTES.md`, `CALIBRACION-ESCALA-2026-11-18.md` |
| Tablero y glosario | El estado de hoy en una página; los términos definidos una sola vez | `STATUS.md`, `GLOSARIO.md` |
| Primera lectura | La página de entrada para un agente nuevo que va a trabajar en el sistema | `ONBOARDING.md` |

Cifras del censo (144/186/58+8): refresco del 23 nov 2026, 1ª
tanda de esta sesión; el inventario manda sobre cualquier nota
vieja. El marcador de calibración (9 resueltas, 77,8 %) es el de
`CALIBRACION.md` al 23 nov (C-008–C-011 publicadas); la línea base
del banco (6/6) es la de `STATUS.md` al 16 nov, sin cambios de
estado desde entonces (verificado en la auditoría del 23 nov).

## Cómo se conectan (los flujos que importan)

1. **Trabajo → aprendizaje.** Cada trabajo que termina deja huella
   en este repo (regla de crecimiento del README): una entrada en
   `crecimiento/log.md`, un patrón en `aprendido/` o una pregunta
   en `por-aprender/`. Si no dejó huella, es como si no se hubiera
   aprendido.
2. **Fallo → registro → mecanismo.** Un fallo demostrado se registra
   (FI en `REGISTRO-INTEGRACION.md`, lección en `aprendido/` o
   regla en `AGENTS.md`) y, si la clase de fallo se repite, nace
   un mecanismo (la Fase 0 nació así de la auditoría del 17 nov:
   0 de 28 fallos por dato ausente, todo integración). Ver
   `CICLO-DE-VIDA-DE-LECCIONES.md`.
3. **Afirmación decisiva → calibración.** Lo decisivo y comprobable
   a futuro se anota en `CALIBRACION.md` con su nivel de evidencia
   y se marca confirmada/parcial/refutada cuando la realidad
   responde. Las refutadas nunca se borran.
4. **Tarea recurrente → banco.** Lo que Antonio pide una y otra vez
   se convierte en prueba fija del banco, con criterios escritos
   antes de correr, para detectar deriva entre corridas.
5. **Entrega decisiva → refutación.** Antes de entregar algo
   decisivo (investigación con consecuencias, dinero, publicación,
   despliegue), una pasada adversarial intenta refutarlo; cada
   afirmación atacada se clasifica refutada/debilitada/resiste.
6. **Obligación viva → hilo.** Lo que queda pendiente con dueño y
   disparo de cierre vive en `HILOS-ABIERTOS.md`, no en la cabeza
   de nadie. Los hilos se leen cada sesión.
7. **Duda sin respuesta → pregunta abierta.** Lo que no se sabe vive
   en `por-aprender/preguntas-abiertas.md` con por qué importa y
   cómo resolverlo (15 preguntas; la Q15 pregunta cuál es la semilla canónica
   de P-04).

## Lo que este mapa NO es

- No es el índice del repo: eso es el README (qué archivo hay y
  para qué sirve). El mapa dice cómo encajan las piezas, no en
  qué orden leerlas.
- No es el tablero: eso es `STATUS.md` (cómo va el sistema hoy,
  con fecha). El mapa es estructura; el tablero es estado.
- No incluye lo que vive fuera del sistema de Dirsi: las cuentas
  de Antonio, su teléfono, su portátil (salvo el puente Tailscale
  + OpenCode, que es una conexión del sistema) y sus archivos
  personales. Ver `QUE-NO-ESTA-EN-ESTE-REPO.md`.


