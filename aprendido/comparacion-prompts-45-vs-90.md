# Comparación prompt a prompt: los 45 de M8 frente a los 90 de P1

Fecha: 2 de noviembre de 2026. Cierra la pregunta abierta nº 5 de la
recopilación (M8 frente a P1).

## Pregunta

¿Los 45 prompts del PDF «Multiplica tu productividad…» (M8) son un
subconjunto de los 90 prompts del material de la clase 1 (P1), o son
material distinto?

## Fuentes usadas

- M8: PDF «Multiplica tu productividad y aumenta tu valor profesional
  utilizando Inteligencia Artificial» (CenteIA, junio de 2026,
  20 páginas), descargado de la URL oficial registrada en la propia
  recopilación (training.centeia.com).
- P1: PDF «90 prompts que funcionan» de la clase 1, copia en
  `workspace/user/files/`.

## Método

1. Extracción del texto completo de ambos PDF (pdftotext con
   maquetación).
2. Segmentación de cada prompt por su encabezado «PROMPT N» y por sus
   6 campos (acción, pasos, persona, contexto, restricciones,
   plantilla).
3. Comparación campo a campo con el texto normalizado (sin acentos,
   mayúsculas ni puntuación) y medida de similitud por secuencia.
4. Revisión manual de todos los casos con similitud menor que 1 para
   distinguir diferencias reales de residuos de maquetación
   (encabezados de página, pies, nombres de rol repetidos).

Nota: por la regla de no copiar textos de cursos, este documento no
reproduce los prompts; los referencia por su título corto.

## Resultado

Los 90 de P1 se dividen en dos bloques de 45:

- Bloque 01: «Aumenta la rentabilidad y disminuye los costes de tu
  negocio» — 45 prompts de negocio en 15 categorías, en primera
  persona (el dueño del negocio pide para sí).
- Bloque 02: «Multiplica tu productividad y aumenta tu valor
  profesional» — 45 prompts de productividad en 15 roles
  profesionales, 3 por rol, con la estructura de 6 campos.

Y el Bloque 02 es exactamente el contenido de M8:

- **Idénticos: 45 de 45.** Los 45 prompts de M8 coinciden con los
  prompts 1–45 del Bloque 02 de P1 en el mismo orden, con el mismo
  título (45/45) y el mismo texto en los 6 campos:
  - Acción: idéntica en 45/45 (similitud normalizada 1,000).
  - Persona, contexto y restricciones: idénticos en 45/45.
  - Pasos: idénticos; las únicas diferencias al extraer eran la
    línea con el nombre del rol que P1 repite como encabezado de
    página (11 casos), no texto del prompt.
  - Plantilla: idéntica; las diferencias al extraer eran pies de
    página y el texto de cierre de la guía, no texto del prompt.
- **Casi duplicados (misma tarea, redacción distinta): 0.** No es una
  re-redacción: es el mismo texto.
- **Únicos de M8: 0 prompts.** M8 es el Bloque 02 republicado como
  PDF independiente, con portada, introducción y cierre adaptados al
  ángulo de «valor profesional». No añade ningún prompt nuevo.
- **Únicos de P1: 45 prompts**, todo el Bloque 01. Títulos cortos:
  propósito y visión empresarial; diseño de la estrategia a 1-3-5
  años; evaluación del modelo de negocio (Canvas); buyer persona;
  validación rápida de idea de negocio; análisis competitivo con mapa
  de posicionamiento; prototipado rápido con feedback; roadmap de
  funcionalidades a 6 meses; product-market fit; posicionamiento y
  branding; embudo de captación; estrategia de contenidos con
  storytelling; campaña publicitaria en Meta/Google Ads;
  automatización de embudo con Zapier o Make; email marketing con
  secuencias; pitch de ventas persuasivo; script de llamada en frío;
  precios y packaging; sistema de soporte con IA; gestión de quejas;
  encuesta NPS; análisis financiero mensual; forecast de ingresos y
  gastos; rentabilidad por producto o servicio; organización contable
  para no financieros; impuestos trimestrales; calendario fiscal
  anual; documentación de procesos (SOP); mapa de procesos; auditoría
  operativa para escalar; selección de talento; onboarding;
  evaluación de desempeño; ponencia inspiradora; presentación
  corporativa; guión de vídeo corto o reel; pitch de colaboración;
  email de networking; nota de prensa; informe mensual de rendimiento;
  análisis post-lanzamiento; seguimiento de OKR/KPI; revisión legal
  básica; contrato de colaboración; estrategia legal para escalar.

## Dos observaciones

- **Título repetido dentro de P1:** «Diseño de pitch de ventas
  persuasivo» aparece como nº 16 en AMBOS bloques, pero son prompts
  distintos: en el Bloque 01 es un pitch comercial en primera persona
  para presentar tu producto; en el Bloque 02 (y en M8) pertenece al
  rol de diseñador gráfico/multimedia. Mismo título, contenido
  diferente.
- **Sin desfases de numeración:** ningún prompt de M8 empareja con un
  número distinto en P1. El «desajuste título-contenido» anotado en
  la pregunta abierta nº 8, si existe, es interno a un mismo prompt y
  está igual en las dos copias.

## Conclusión

Los 45 de M8 son un subconjunto exacto — en la práctica, una copia —
de los 90 de P1: son su Bloque 02 suelto. Para conservar, basta P1.
M8 solo aporta valor como versión independiente y ligera del bloque
de productividad (más cómoda de consultar que el PDF completo de 90).
