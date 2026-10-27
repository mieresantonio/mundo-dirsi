# Ingeniería inversa — lo aprendido

## Qué es REA

REA (ingeniería inversa asistida, en el sentido de "reverse engineering
assisted") es la práctica de estudiar una web o una app existente para
entender su interfaz y su comportamiento observable, y luego reconstruir
algo equivalente con código propio. No es copiar código ajeno: es observar
qué hace un producto desde fuera y volver a construirlo desde dentro.

## El método de sala limpia

El procedimiento tiene cuatro fases, en orden, sin saltarse ninguna:

1. **Observar.** Recorrer la app original y anotar lo que se ve y lo que
   hace: pantallas, flujos, textos visibles, estados, errores, tiempos de
   respuesta. Solo comportamiento observable; nada de mirar su código
   fuente si el objetivo es una reconstrucción limpia.
2. **Especificar.** Convertir las observaciones en una especificación
   escrita en sala limpia: qué debe hacer la reconstrucción, pantalla por
   pantalla, sin referencia al código original. Esta especificación es el
   único documento que la fase de construcción puede consultar.
3. **Reconstruir.** Escribir código propio a partir de la especificación,
   con las propias decisiones de arquitectura, nombres y estructura.
4. **Comparar paridad.** Poner la reconstrucción junto a la original y
   comprobar, flujo por flujo, que se comporta igual desde fuera. Lo que
   no coincide vuelve a la especificación, no a copiar la original.

Saltarse la especificación y construir mirando la app original convierte
la reconstrucción en copia. Saltarse la comparación deja diferencias sin
detectar.

## Clasificación de evidencia

Toda afirmación sobre lo observado se etiqueta, sin mezclar niveles:

- **Visto.** Leído o comprobado de primera mano: una pantalla, un archivo,
  un flujo ejecutado. Es el único nivel que sostiene una afirmación fuerte.
- **Inferido.** Deducido a partir de lo visto, con el razonamiento
  explícito. Útil, pero se presenta como inferencia, no como hecho.
- **Desconocido.** Lo que no se pudo comprobar. Se dice así, sin rellenar
  el hueco con una suposición plausible. Un hueco declarado es mejor que
  un dato inventado.
- **Afirmación del creador.** Lo que dice quien hizo el producto (videos,
  anuncios, documentación de marketing). Se registra como marketing, no
  como hecho, hasta que se comprueba.
- **Retirado.** Una afirmación que se sostuvo y luego se corrigió con
  buena evidencia. Queda registrada como retirada, no borrada en silencio.

Regla de trabajo: nunca sintetizar a partir de resúmenes de segunda mano
sin cruzar las afirmaciones decisivas contra la fuente primaria. Los
resúmenes intermedios, por verosímiles que suenen, han fabricado contenido
antes; lo leído de primera mano no ha fallado.

> Equivalencia con la taxonomía de `consultas/plantilla-investigacion.md`:
> Visto corresponde a A (Demostrado), Inferido a B (Secundario estable,
> con el razonamiento explícito), Afirmación del creador a C, y Retirado
> a X. Desconocido no tiene letra propia en aquella plantilla: se marca
> como hueco declarado dentro del informe. Son dos formas de decir lo
> mismo, no dos sistemas distintos.

## El experimento con y sin control

La prueba de referencia para la ingeniería inversa asistida es un
experimento con control: la misma reconstrucción intentada con y sin la
ayuda de la herramienta, midiendo la diferencia real de resultado. Sin
grupo de control, cualquier "mejora" atribuida a la herramienta es una
opinión, no una medición. Este criterio se aplica a cualquier afirmación
de productividad de una herramienta de IA: sin comparación, no hay
conclusión.

## Advertencia: repositorios falsos

En torno a REA circuló un repositorio falso que contenía un troyano. Las
fuentes oficiales son únicamente el repositorio del autor (morluto/rea),
su sitio y su paquete publicado. Reglas:

- Descargar o clonar solo desde la fuente oficial verificada.
- Desconfiar de repositorios con nombres parecidos, de enlaces en videos
  sin verificar y de cualquier "versión mejorada" de origen desconocido.
- Antes de ejecutar código de terceros, revisar qué hace. Un troyano no
  avisa; la verificación previa es la única defensa barata.

## Límites

- La ingeniería inversa reconstruye comportamiento observable, no
  propiedad intelectual ajena: textos, marcas, diseños distintivos y
  código original no se copian. La reconstrucción tiene identidad propia.
- Si la app original exige cuentas, pagos o acceso a datos de terceros,
  la reconstrucción usa datos de ejemplo y simulación, nunca credenciales
  ni datos reales de nadie.
