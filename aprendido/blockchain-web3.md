# Blockchain y web3 — lo aprendido

## Blockali: un producto real, no una demo

Blockali es una plataforma de aprendizaje de blockchain con cuentas
reales, construida como proyecto final de un bootcamp y luego mejorada
hasta nivel profesional. Su estructura:

- **Rutas de aprendizaje → módulos → lecciones en Markdown → quiz por
  lección**, con progreso guardado en el servidor, no en el navegador.
- **Autenticación completa:** registro con verificación por correo,
  restablecimiento de contraseña, tokens con verificación de propiedad
  sobre el progreso y roles (estudiante y administrador).
- **Stack real:** frontend en React con Vite y enrutado, backend en Flask
  con SQLAlchemy y migraciones, base de datos relacional. Contenido de
  cursos sembrado desde el backend.
- **Gamificación añadida:** puntos de experiencia por lección y por quiz,
  niveles, rachas calculadas desde la fecha de finalización del progreso,
  y certificados verificables: para reclamarlo hay que completar el 100 %
  de las lecciones y aprobar todos los quizzes con al menos 70 %, el
  certificado lleva un código único y una página pública de verificación.
- **Laboratorio interactivo:** página de laboratorio con calculadora de
  hash en vivo y una cadena de tres bloques que se puede alterar para ver
  cómo se rompe. Esta fue la pieza que convirtió la plataforma en algo
  más que lectura.

## Lecciones de la evaluación inicial

La primera evaluación encontró que la base era sólida (un producto real,
no un juguete) y que el trabajo pendiente era de capa visual y de
experiencia, no de rescate: higiene (README propio, restos de plantilla,
dependencias unificadas, idioma, metadatos), sistema de diseño propio,
landing profesional, experiencia de aprendizaje con laboratorio y
certificado, y pulido (responsive, accesibilidad básica, estados de
carga y vacíos, control de calidad visual página por página). Las fases
se ejecutaron en orden y se fusionaron con la aprobación del usuario.

## ModelBattle: qué enseñó la comparativa

Cuatro versiones de una misma plataforma, generadas por modelos
distintos con los nombres ocultos hasta votar, dejaron una combinación
ganadora clara:

- **El laboratorio es el diferenciador.** La versión con mejores
  experimentos (constructor de transacciones entre billeteras, calculadora
  de gas en vivo, código Solidity real copiable con enlace a un entorno
  de pruebas) enseñaba más que las demás, aunque no tuviera quizzes.
- **El currículo más completo gana en estructura:** cinco módulos, examen
  final de diez preguntas y certificado con identificador generado por
  hash.
- **El simulador de condiciones importa.** Entender que un contrato
  revierte cuando una condición falla, sin tocar ningún saldo, es la idea
  central de los contratos inteligentes, y se aprende mejor simulándola
  que leyéndola.
- **La identidad visual más pulida no basta.** La versión más bonita
  tenía secciones vacías y menos contenido. Belleza sin contenido es un
  folleto; contenido sin laboratorio es un libro.
- **Gamificación combinada:** rachas y metas semanales de una versión,
  puntos y logros de otra. Ninguna versión sola lo tenía todo.
- **Lo común que hay que mantener:** español, empezar con un solo
  archivo, progreso local en las demos, avisos honestos de "sin dinero
  real", y no copiar la marca de nadie (dos versiones compartían
  prácticamente el mismo nombre; la reconstrucción propia necesita
  identidad propia).
- **Nota de proceso:** una votación se registró por accidente al cambiar
  de pestaña, avanzando la batalla sin querer. Los clics en herramientas
  de votación son votos; hay que avisar antes de tocar.

## Las 10 apps web3: una especialización por app

Serie de diez aplicaciones, cada una con una sola especialización, todas
con datos simulados y de ejemplo, sin wallets reales, sin claves, sin
fondos y sin red principal:

1. **Laboratorio de hash.** Calculadora SHA-256 en vivo (implementada en
   JavaScript puro, verificada contra vectores de referencia) y mini-cadena
   de tres bloques editable que se marca como rota al alterar un bloque.
2. **Simulador de wallet.** Carteras de ejemplo, envío de ETH de prueba
   con validaciones (formato, saldo, autoenvío), recepción simulada e
   historial.
3. **Calculadora de gas.** Precio en gwei ajustable, tipos de operación
   con sus unidades típicas, cálculo en vivo con la fórmula paso a paso y
   comparación lento / estándar / rápido.
4. **Explorador de tokens.** Lista de tokens inventados con precio
   simulado, búsqueda, filtros, ordenación y detalle con gráfico generado
   localmente.
5. **Laboratorio de contratos.** Fragmentos de Solidity copiables con
   enlace a un entorno de pruebas, más simulador de require/revert que
   muestra qué regla falló y en qué orden.
6. **Estudio NFT simulado.** Galería de ejemplo con arte generado
   localmente en SVG, creación de obras de ejemplo y minteo simulado paso
   a paso.
7. **Constructor de transacciones.** Cinco pasos (remitente, destinatario,
   valor, gas, revisión) con validación en cada paso, firma simulada e
   historial local.
8. **Entrenador anti-phishing.** Juego de decidir si cada caso es
   legítimo o phishing, con puntos, rachas, repaso de fallos y un panel
   permanente de señales de alerta.
9. **Votación DAO.** Propuestas de ejemplo, poder de voto simulado,
   quórum, resultados en vivo y creación de propuestas, con regla de
   aprobación explícita (más votos a favor que en contra y quórum
   alcanzado).
10. **Explorador de bloques.** Cadena de ejemplo navegable con búsqueda
    por altura o hash, detalle de bloque y de transacción, generada de
    forma determinista.

## Principios web3 que quedan

- **Simulado, siempre, y etiquetado.** Ninguna app de la serie toca una
  red real. La etiqueta de simulación está en cabecera, en cada pantalla
  relevante y en el pie.
- **"Aquí los errores enseñan. No cuestan dinero."** Es el mejor encuadre
  de seguridad para un simulador: el error es pedagógico porque no hay
  fondos en juego.
- **Verifica, no solo confíes.** El certificado con código verificable y
  la cadena que se rompe al alterarla enseñan la misma idea: la confianza
  se comprueba, no se declara.
