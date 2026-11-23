# Auditoría de coherencia de un repo de documentos — lo aprendido

Método destilado de la auditoría completa de mundo-dirsi del 23 nov
2026 (sesión de mejora «modo quemar tokens Full»). Sirve para cualquier
repo cuyo contenido son documentos que se citan entre sí: un índice que
miente, una cifra que caducó o una referencia que apunta a un archivo
que no existe son fallos de integración (FI) en potencia — el dato
correcto estaba en el sistema y la entrega no lo conectó. La auditoría
los caza antes de que alguien actúe sobre ellos.

## El principio

Un repo de documentos tiene cuatro clases de verdad, y cada una se
comprueba de una forma distinta:

1. **Estructura** — ¿el índice lista todos los archivos? ¿las
   referencias apuntan a algo que existe?
2. **Cifras** — ¿cada número que un archivo afirma coincide con su
   fuente?
3. **Vigencia** — ¿las fechas y estados describen el hoy, o un día
   viejo congelado como si fuera hoy?
4. **Historia congelada** — ¿lo que debe conservarse intacto (registro
   de calibración, antecedentes) sigue intacto, y lo que lo cita lo
   cita bien?

La auditoría del 23 nov encontró fallos en las cuatro clases (ver
«Hallazgos de la primera aplicación», abajo). Ninguno era grave por
separado; juntos hacían que el tablero del sistema (STATUS.md)
describiera el 16 nov como si fuera el 23.

## La lista de comprobación

### 1. Inventario contra índice

```
find . -path ./.git -prune -o -type f -print | sort
```

Cada archivo con contenido debe aparecer en el índice del README (o
tener una razón escrita para no aparecer: `.gitignore` no se indexa).
Recíproco: cada entrada del índice debe existir. En la auditoría del
23 nov, `CALIBRACION-ESCALA-2026-11-18.md` existía desde el 18 nov y
el índice no lo listaba.

### 2. Referencias a archivos

Los repos de documentos rara vez usan enlaces Markdown; lo habitual
son nombres de archivo entre comillas invertidas. Extraerlos todos y
comprobar que el archivo existe, en el repo o con su ruta completa
fuera de él:

```
grep -rhoE '`[A-Za-z0-9_./-]+\.md`' --include='*.md' . | sort -u
```

Clasificar cada referencia sin archivo: (a) archivo de otro repo o
del workspace local — legítima si el contexto lo dice, y mejorable
si se le añade la ruta completa; (b) nombre genérico (`SKILL.md`,
`CONNECTOR.md`, `LOG.md`) — legítima, no es una referencia a un
archivo concreto; (c) referencia rota de verdad — la única que se
corrige. En la auditoría del 23 nov, de 97 referencias solo una era
rota: `RESULTADOS.md` en `ESCALA-RAZONAMIENTO-AGENTES.md` (el archivo
real es `CALIBRACION-ESCALA-2026-11-18.md`).

### 3. Cifras contra su fuente

Todo número que un archivo afirma y otro archivo fundamenta se
verifica con un conteo directo, no leyendo el número en los dos
sitios y asintiendo. Los conteos de la auditoría del 23 nov:

```
grep -c '^## D-' aprendido/decisiones.md        # 10 fichas
grep -c '^## Ruta' por-aprender/rutas.md        # 6 rutas
grep -c '^## [0-9]' por-aprender/preguntas-abiertas.md  # 14 preguntas
grep -c '^- \*\*' GLOSARIO.md                   # 34 entradas
```

Y la aritmética de los marcadores se rehace a mano: el acierto de
calibración es (confirmadas + 0,5 × parciales) / resueltas; la línea
base de FI/semana es FI / días × 7. Un marcador que no se puede
rehacer desde sus entradas no es un marcador, es una afirmación.

### 4. Fechas contra el calendario

Buscar todas las fechas del repo y preguntar por cada una: ¿sigue
siendo verdad hoy? Los puntos calientes son los tableros de estado,
las listas de vencimientos y las frases «aún sin…» / «pendiente» /
«próximo». En la auditoría del 23 nov:

- STATUS.md decía «Tablero al 16 de noviembre» con dos vencimientos
  ya ocurridos (revisiones del 19 y 22 nov, ambas completadas) y sin
  el vencimiento nuevo más cercano (la demo de PythonAnywhere
  caduca ~26 nov si no se extiende).
- El banco decía que P-03 no había corrido; había corrido el 18 nov
  en la calibración de la escala.
- El glosario definía P-03/P-04 como «aún sin primera corrida»;
  P-03 ya la tenía.

Regla: una afirmación de estado sin fecha es una afirmación sin
vencimiento; toda sección de estado lleva su fecha, y la fecha se
actualiza cuando el estado cambia, no cuando se relee el archivo.

### 5. Historia congelada

Lo que el repo declara congelado (el registro de calibración, los
antecedentes) se verifica en dos sentidos: que nadie lo reescribió
y que lo que lo cita lo cita bien. Comprobaciones de la auditoría:

```
grep -c -i "blockali" CALIBRACION.md   # 2: las dos líneas congeladas
grep -rni "blockali" --include='*.md' . | grep -v CALIBRACION.md
# resto: solo notas históricas del renombre, ninguna como nombre vigente
```

La segunda comprobación importa tanto como la primera: el nombre
viejo puede reaparecer por la puerta de atrás (un fixture de prueba,
una cita) y cada reaparición necesita su nota de «congelado» o su
corrección. El material P-03 publicado en esta sesión conserva
«Blockali-lite» porque es un fixture congelado del 5 nov, anterior
al renombre, y así se documenta en `BANCO-DE-PRUEBAS.md`: cambiar
el fixture lo versionaría a v2 y rompería la comparación con la
corrida del 18 nov.

### 6. Contradicciones entre archivos

Buscar la misma afirmación en dos archivos y comparar la letra, no
el sentido. La auditoría del 23 nov encontró una contradicción viva:

- `aprendido/herramientas-y-conexiones.md` decía que con el permiso
  permanente de GitHub «ya no hace falta pedir aprobación por cada
  cambio».
- La memoria del sistema (corrección del 17 nov, incidente I2)
  establece que el permiso cambió la DECISIÓN, no la presentación:
  las tarjetas de aprobación SIGUEN apareciendo y se aprueban en
  segundos; afirmar que no salen es falso.

La corrección se escribe en el mismo archivo que afirma lo falso
(R3 del consejo asesor): una adenda que solo vive en el chat no
existe. Las contradicciones entre archivos son las que más duelen,
porque cada archivo por separado parece verdad.

### 7. Censo: recontar, no releer

Cuando el repo afirma cifras del entorno (conectores, CLIs, skills,
recursos de la máquina), la auditoría las reconta con los comandos
del propio inventario, no las da por buenas porque el archivo las
diga. El refresco del 23 nov encontró que el entorno había cambiado
mucho entre despliegues: 90 → 144 conectores, 129 → 186 CLIs,
57 → 58 skills del sistema, 910 → 911 binarios en `/usr/bin`; el
resto (máquina, cachés, versiones) sin cambios. La regla de refresco
del inventario existe justo para esto: una foto vieja no describe
la máquina de hoy.

### 8. Material que el repo promete y no contiene

Revisar las frases «aún sin publicar», «material preparado en…» y
las excepciones de `.gitignore` que apuntan a rutas inexistentes.
La auditoría del 23 nov encontró que `.gitignore` ya tenía una
excepción para `banco-de-pruebas/p-03/dist/` (añadida el 16 nov)
pero el material no estaba en el repo: vivía solo en la copia local
de trabajo. Se propuso su publicación con la semilla P-04 congelada
(MD5 verificado), porque la app fijada por P-04 ya divergió en su
repo publicado y sin la semilla congelada la prueba no sería
reproducible. La misma auditoría dejó una pregunta abierta (Q15):
la copia local de la app fijada (`~/workspace/rag-demo/app.py`,
MD5 `d976b50e…`) no está sincronizada con GitHub (HEAD
`7423c8c3…`, 3 rutas). La decisión —semilla canónica v1 congelada
o v2 sobre el HEAD, y sincronización del workspace— es de
Antonio/Dirsi y no se resuelve en la auditoría: se registra como
pregunta abierta.

## Hallazgos de la primera aplicación (23 nov 2026)

| Clase | Hallazgo | Gravedad |
|---|---|---|
| Estructura | `CALIBRACION-ESCALA-2026-11-18.md` fuera del índice del README | Media |
| Estructura | Referencia rota: `RESULTADOS.md` en la escala (no existe) | Media |
| Cifras | Censo desfasado: 90→144, 129→186, 57→58, 910→911 | Alta |
| Cifras | Conteos del README verificados (10 fichas, 6 rutas, 14 preguntas, 34 entradas) | — (bien) |
| Vigencia | STATUS.md a 16 nov; 2 vencimientos cumplidos sin marcar; falta la caducidad de PythonAnywhere (~26 nov) | Alta |
| Vigencia | P-03 figuraba sin correr; corrió el 18 nov (banco y glosario) | Media |
| Vigencia | El glosario no definía 26 términos usados en los documentos (FI, Fase 0, hilo abierto, corrida ciega, consejo asesor, escala, clon fresco…) | Media |
| Historia | «Blockali» solo donde debe: 2 líneas congeladas en CALIBRACION.md + notas del renombre | — (bien) |
| Contradicción | El permiso permanente de GitHub redactado como «ya no hace falta pedir aprobación» (falso: las tarjetas siguen apareciendo) | Alta |
| Material | Material P-03/P-04 sin publicar; semilla P-04 solo en local; app fijada divergida en su repo (pregunta abierta Q15: semilla canónica y sincronización del workspace) | Media |

## Cuándo correrla

- Al cierre de cada sesión de mejora de repos (como esta): la
  auditoría es la verificación final del repo antes de publicar.
- Cuando un tablero de estado (STATUS.md) cumpla una semana sin
  actualizarse: una semana es suficiente para que dos vencimientos
  se cumplan y uno nuevo aparezca.
- Después de cualquier renombre, migración o cambio de estructura:
  es cuando las referencias y los índices se rompen en silencio.

## Límites

- La auditoría caza incoherencias, no errores de fondo: una cifra
  puede ser coherente entre archivos y falsa en los dos. Para eso
  están el registro de calibración y el protocolo de refutación.
- No sustituye a la lectura: los greps encuentran las referencias
  y los conteos, pero la contradicción del permiso de GitHub solo
  se caza leyendo los dos textos y comparando la letra.
