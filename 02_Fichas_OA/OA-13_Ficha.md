# Ficha de diseño — OA-13: Tu huella personal en 5 decisiones

> **Estado: Construido y empaquetado como `.h5p`; pendiente de validación pedagógica final del DI.**
> Esta ficha describe un objeto de aprendizaje **aún no construido**. No existe todavía el paquete `.h5p`: lo aquí recogido es el **diseño propuesto** (consigna, diapositivas, ítems, respuestas y feedback) que servirá de guion para autorizarlo después en el editor H5P de Moodle o en Lumi. Todos los textos y comportamientos son una **propuesta a validar por el Diseñador Instruccional (DI)** antes de pasar a producción; ningún dato procede de la lectura de un `content.json` (no lo hay). Esta ficha existe para **cerrar el diseño antes de tocar el editor**: deja documentado el contenido real del dominio climático AHC, evita rehacer trabajo y permite que el becario construya el OA sin improvisar.

> **Coherencia verbo-formato (obligatoria):** el tipo **H5P.CoursePresentation (Course Presentation)** es el formato idóneo para recoger la evidencia del verbo **Identificar**. Una microlección en diapositivas permite **presentar primero** cada una de las 5 decisiones cotidianas (movilidad, alimentación, energía, consumo, residuos) y **comprobar a continuación**, en la misma diapositiva, que el estudiante **identifica** la opción de menor huella mediante interacciones autocalificables incrustadas (Multiple Choice y True/False embebidos). El estudiante demuestra de forma **observable y autocalificable** que reconoce qué decisión reduce la huella, sin necesidad de redactar ni de calcular: solo *identificar* la opción correcta entre alternativas. La secuencia diapositiva → interacción → feedback es justamente lo que mejor evidencia un verbo de nivel "recordar/comprender" como *Identificar*.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| Código OA | OA-13 |
| Título | Tu huella personal en 5 decisiones |
| Tipo H5P | H5P.CoursePresentation (Course Presentation / Presentación de curso) |
| Familia (plan AHC §5) | Explicación |
| Curso destino | Huella de Carbono Personal |
| Público | Ciudadanía |
| Verbo Bloom | Identificar |
| Versión prevista | 1.0.0 |
| Licencia | Creative Commons CC BY-NC-SA 4.0 |
| Estado | ✅ Probado en h5p.org · ⏳ Pendiente validación en Moodle |
| Archivo H5P | `OA-13_AHC_H5P_CoursePresentation_HuellaCincoDecisiones_Basico_HuellaPersonal_v1.0.0.h5p` |
| Autor previsto | Becario H5P (construcción) |
| Revisor | Diseñador Instruccional — pendiente de validación del diseño |
| Fecha de diseño | 2026-06 |

> Nota de trazabilidad: el título interno previsto para el paquete (`h5p.json`, una vez construido) será "OA-13: Tu huella personal en 5 decisiones". El identificador de máquina del tipo es `H5P.CoursePresentation`.

---

## 2. Diseño pedagógico

| Campo | Valor |
|---|---|
| Objetivo de aprendizaje | **Identificar**, en cinco ámbitos cotidianos (movilidad, alimentación, energía, consumo y residuos), cuál de dos decisiones tiene **menor huella de carbono**, reconociendo el patrón general que rige cada ámbito. |
| Competencia | Alfabetización climática personal: relacionar decisiones diarias con su impacto en emisiones de gases de efecto invernadero (GEI) y reconocer dónde se concentra la huella propia. |
| Verbo observable (Bloom) | Identificar (reconocer / seleccionar la opción correcta). |
| Evidencia observable | En cada una de las 5 diapositivas de decisión, el estudiante **selecciona** la opción de menor huella (Multiple Choice) o **marca verdadero/falso** sobre una afirmación, y el componente registra acierto/error de forma autocalificable. |
| Duración estimada | 5–8 min (microlearning). |
| Prerequisitos | Idea básica de "huella de carbono" y de gases de efecto invernadero (GEI). Recomendable haber visto OA-01 (Conceptos Climáticos Básicos) o equivalente. |
| Mensaje clave | **No todas las decisiones pesan igual: con 5 elecciones cotidianas (cómo te mueves, qué comes, cómo consumes energía, qué compras y qué tiras) controlas la mayor parte de tu huella personal.** |
| Criterio de éxito | El estudiante acierta **≥ 4 de las 5** interacciones de decisión (≥ 80 %), demostrando que identifica de forma estable la opción de menor huella en distintos ámbitos. |
| Momento de uso | **Apertura/desarrollo** del curso "Huella de Carbono Personal": sirve de microlección introductoria que da la visión de conjunto antes de la calculadora de huella (OA de *Interactive Video* "Cómo calcular tu huella"). |

---

## 3. Contenido propuesto

**Estructura general:** 8 diapositivas. 1 portada + 5 diapositivas de decisión (cada una con una interacción autocalificable embebida) + 1 diapositiva de "dónde se concentra tu huella" + 1 diapositiva de cierre con mensaje clave.

**Consigna global (texto exacto, en la portada — diapositiva 1):**
> "Tu día a día está hecho de decisiones, y muchas tienen una huella de carbono. En las siguientes 5 diapositivas verás una decisión cotidiana en cada una. **Identifica la opción con MENOR huella de carbono** y comprueba tu respuesta. Avanza con las flechas. ¡Empezamos!"

### Diapositiva 1 — Portada (sin interacción)
- **Título:** "Tu huella personal en 5 decisiones".
- **Texto:** la consigna global anterior.
- **Imagen sugerida:** icono/foto de una persona ante una bifurcación de caminos (movilidad/comida/energía). *(Decorativa: ALT vacío o breve, ver §5.)*

### Diapositiva 2 — Movilidad (Multiple Choice embebido)
- **Consigna exacta:** "**MOVILIDAD.** Tienes que recorrer 5 km dentro de la ciudad. ¿Qué opción tiene **menor** huella de carbono?"
- **Opciones:**
  - A) Ir en coche de gasolina tú solo/a.
  - **B) Ir en bicicleta o andando. ✅ (correcta)**
  - C) Pedir un taxi.
  - D) Ir en coche, pero con el aire acondicionado al máximo.
- **Feedback de acierto:** "¡Correcto! Para trayectos cortos en ciudad, la bici y caminar tienen **huella casi nula** y, además, mejoran tu salud. El coche en solitario es de las opciones que más emite por persona."
- **Feedback de error:** "No exactamente. La opción de menor huella es **ir en bici o andando**: para 5 km en ciudad emiten prácticamente cero, frente al coche en solitario o el taxi. Inténtalo de nuevo."

### Diapositiva 3 — Alimentación (Multiple Choice embebido)
- **Consigna exacta:** "**ALIMENTACIÓN.** Vas a preparar la comida de hoy. ¿Qué menú tiene **menor** huella de carbono?"
- **Opciones:**
  - A) Un filete de ternera de origen lejano.
  - **B) Legumbres y verduras de temporada y de proximidad. ✅ (correcta)**
  - C) Hamburguesa de ternera con patatas.
  - D) Cordero asado.
- **Feedback de acierto:** "¡Correcto! La carne de **rumiantes** (ternera, cordero) es de los alimentos con **mayor huella** por las emisiones de metano y el uso de suelo. Las **legumbres y verduras de temporada y proximidad** tienen una huella muy inferior."
- **Feedback de error:** "Casi. El menú de menor huella es el de **legumbres y verduras de temporada y de proximidad**. La ternera y el cordero (rumiantes) son los alimentos que más emiten. Vuelve a intentarlo."

### Diapositiva 4 — Energía en el hogar (True/False embebido)
- **Consigna exacta:** "**ENERGÍA.** Lee la afirmación y decide si es **Verdadero** o **Falso**: *«Bajar la calefacción 1 °C y contratar electricidad de origen 100 % renovable reduce la huella de carbono de tu vivienda.»*"
- **Respuesta correcta:** **Verdadero. ✅**
- **Feedback de acierto:** "¡Correcto! **Verdadero.** Cada grado menos de calefacción ahorra energía, y la electricidad de origen **renovable certificado** evita las emisiones asociadas a quemar combustibles fósiles. Dos gestos sencillos con efecto real."
- **Feedback de error:** "Es **Verdadero**. Bajar 1 °C la calefacción ahorra energía y la electricidad **100 % renovable** evita las emisiones de generar luz con combustibles fósiles. Ambas reducen la huella del hogar."

### Diapositiva 5 — Consumo (Multiple Choice embebido)
- **Consigna exacta:** "**CONSUMO.** Se te ha roto un electrodoméstico pequeño. ¿Qué decisión tiene **menor** huella de carbono?"
- **Opciones:**
  - **A) Intentar repararlo o comprarlo de segunda mano. ✅ (correcta)**
  - B) Comprar uno nuevo de gama alta inmediatamente.
  - C) Comprar dos por si acaso, que estaban de oferta.
  - D) Comprar el más barato aunque dure poco y haya que reponerlo pronto.
- **Feedback de acierto:** "¡Correcto! **Reparar o comprar de segunda mano** evita la huella de fabricar un producto nuevo (extracción de materiales, producción y transporte). Alargar la vida útil es de las decisiones de consumo más eficaces."
- **Feedback de error:** "No del todo. La opción de menor huella es **reparar o comprar de segunda mano**: evita las emisiones de fabricar y transportar un producto nuevo. Comprar de más o productos que duran poco aumenta la huella. Reinténtalo."

### Diapositiva 6 — Residuos (Multiple Choice embebido)
- **Consigna exacta:** "**RESIDUOS.** Acabas de generar restos de comida y un envase de cartón. ¿Qué gestión tiene **menor** huella de carbono?"
- **Opciones:**
  - A) Tirarlo todo junto a la basura general.
  - **B) Separar: cartón al contenedor azul y restos de comida al contenedor marrón (orgánico/compostaje). ✅ (correcta)**
  - C) Quemar los restos en casa.
  - D) Acumularlo sin separar para tirarlo en una sola bolsa grande.
- **Feedback de acierto:** "¡Correcto! **Separar** permite **reciclar** el cartón y **compostar** la materia orgánica. La materia orgánica en vertedero genera **metano**, un gas de efecto invernadero muy potente; separarla evita esas emisiones."
- **Feedback de error:** "Casi. Lo de menor huella es **separar**: cartón a reciclar y restos de comida a orgánico/compostaje. La basura orgánica en vertedero emite **metano**; quemar en casa también contamina. Vuelve a intentarlo."

### Diapositiva 7 — ¿Dónde se concentra tu huella? (síntesis, sin calificar)
- **Título:** "¿Dónde se concentra tu huella personal?"
- **Texto exacto:** "En la mayoría de los hogares, la huella personal se reparte sobre todo entre **movilidad, alimentación y energía del hogar**, seguidas de **consumo de bienes y residuos**. La buena noticia: son justamente los cinco ámbitos en los que tú decides cada día. Pequeños cambios repetidos suman mucho a lo largo del año."
- **Interacción opcional (no calificable):** botón/hotspot "Ver ejemplo de reparto" que muestra un texto orientativo: "Movilidad y alimentación suelen ser las dos mayores partidas en una huella personal media."
- *Nota de diseño: si más adelante existe el OA de tipo Chart "¿Dónde se concentra la huella?", esta diapositiva puede enlazar a él en lugar de duplicar el dato.*

### Diapositiva 8 — Cierre (sin interacción)
- **Título:** "Tu huella está en tus manos."
- **Texto exacto (mensaje clave):** "No todas las decisiones pesan igual. Con 5 elecciones cotidianas —**cómo te mueves, qué comes, cómo usas la energía, qué consumes y qué tiras**— controlas la mayor parte de tu huella personal. No hace falta cambiarlo todo de golpe: elige una decisión y empieza por ahí."
- **Llamada a la acción:** "Continúa el curso para **calcular** tu huella y fijar tu primer objetivo."

### Tabla resumen de respuestas correctas

| # Diapositiva | Ámbito | Interacción H5P | Respuesta correcta |
|---|---|---|---|
| 2 | Movilidad | Multiple Choice | B) Bici o andando |
| 3 | Alimentación | Multiple Choice | B) Legumbres y verduras de temporada y proximidad |
| 4 | Energía | True/False | Verdadero |
| 5 | Consumo | Multiple Choice | A) Reparar o de segunda mano |
| 6 | Residuos | Multiple Choice | B) Separar (azul + orgánico/compostaje) |

> **Fuentes:** contenido didáctico propio de la AHC, basado en criterios estándar de huella de carbono personal (jerarquía de movilidad activa frente a motorizada; mayor huella de los rumiantes; electricidad renovable certificada; reparación/reutilización frente a producto nuevo; metano de la materia orgánica en vertedero). Cifras concretas se omiten deliberadamente para no anclar datos no verificados: el OA evalúa *identificar el patrón*, no memorizar números.

---

## 4. Configuración H5P prevista

| Campo | Valor previsto |
|---|---|
| Comportamiento | Cada interacción embebida (Multiple Choice / True-False) con botón "Comprobar" activado y feedback inmediato tras responder. Course Presentation con barra de navegación inferior y resumen final ("Summary slide") activado para mostrar la puntuación total. |
| Reintentos | Sí: "Reintentar" activado en cada interacción (`enableRetry: true`). El estudiante puede rehacer una decisión sin reiniciar toda la presentación. |
| Puntuación | Sí, automática: 1 punto por cada una de las 5 interacciones de decisión (**5 puntos máx.**). Las diapositivas 1, 7 y 8 no puntúan. Puntuación agregada en la diapositiva de resumen. |
| Aleatorización | Multiple Choice con orden de respuestas **barajado** (`randomAnswers: true`) en cada intento. El **orden de las diapositivas no se aleatoriza** (la secuencia narrativa importa). |
| Navegación | Libre con flechas/teclado entre diapositivas; barra de progreso visible. Se permite avanzar aunque no se haya acertado (no bloqueante), para no frustrar; el resultado se ve en el resumen. |
| Compatibilidad móvil | Sí (responsive). Botones y opciones con área táctil amplia; sin arrastrar y soltar, por lo que funciona bien en pantalla pequeña. |
| Reanudación | Activar `xAPI`/estado para que Moodle registre intento y permita reanudar. |

---

## 5. Accesibilidad prevista

| Campo | Valor previsto |
|---|---|
| ALT en imágenes | Las imágenes son **decorativas** (ilustran el ámbito): ALT vacío (`alt=""`) o muy breve y descriptivo cuando aporten información (p. ej. "Persona en bicicleta en la ciudad"). El contenido evaluable está siempre en **texto**, no en la imagen. |
| Contraste | Usar paleta por defecto de H5P o de la AHC garantizando contraste texto/fondo **≥ 4.5:1** (AA). Revisar especialmente títulos sobre imagen de portada. |
| No depender solo del color | El acierto/error se indica con **icono + etiqueta de texto** ("Correcto"/"Incorrecto"), no solo con verde/rojo. |
| Navegación por teclado | Sí: Course Presentation y sus interacciones son operables por teclado (Tab para recorrer opciones, Enter/Espacio para seleccionar y comprobar, flechas para cambiar de diapositiva). Verificar foco visible. |
| Subtítulos / transcripción | N/A en v1.0.0: el OA **no incluye vídeo ni audio**. Si en una versión futura se añade locución, deberá incorporarse transcripción y subtítulos (VTT). |
| Lenguaje claro | Frases cortas, una idea por diapositiva, vocabulario cotidiano. Términos técnicos (GEI, metano) se explican en el feedback. Lectura fácil acorde al público "Ciudadanía". |
| Carga cognitiva | Baja: 1 decisión por diapositiva, 5 decisiones en total, una sola consigna global. |

---

## 6. Reutilización

| Campo | Valor |
|---|---|
| Cursos AHC donde insertar | **Huella de Carbono Personal** (destino principal). Reutilizable en: *Educación ambiental / sensibilización* para ciudadanía; jornadas o talleres divulgativos; como microlección de apertura en cualquier curso introductorio de la AHC. |
| Qué parámetros variar | Los **cinco ámbitos** y sus opciones (`texto de cada diapositiva` y `opciones del Multiple Choice`), los textos de feedback (`feedback`), el público objetivo del lenguaje, y la imagen decorativa de cada diapositiva. Se puede ampliar a 6–7 decisiones o reducir a 3 sin tocar la estructura. |
| Qué NO cambiar | El **verbo Identificar** y la lógica "presentar ámbito → identificar la opción de menor huella → feedback" (núcleo del OA). No convertir las preguntas en cálculo numérico (eso correspondería a otro OA de tipo *Interactive Video* o *Chart*). |
| Variantes sugeridas | Versión "empresa" (decisiones de oficina: teletrabajo, viajes, climatización del local) reutilizando el mismo esqueleto de Course Presentation. |

---

## 7. Pasos para construirlo (checklist para el becario)

Construcción prevista en el **editor H5P de Moodle** (Banco de contenido) o en **Lumi**. El `.h5p` **aún no existe**; esta es la guía para crearlo:

- [ ] Crear contenido nuevo de tipo **Course Presentation** y poner el título "OA-13: Tu huella personal en 5 decisiones".
- [ ] Crear **8 diapositivas** según §3 (portada, 5 de decisión, síntesis, cierre).
- [ ] En cada una de las 5 diapositivas de decisión, **insertar la interacción**: "Multiple Choice" (diapositivas 2, 3, 5, 6) o "True/False Question" (diapositiva 4), pegando la consigna, las opciones, marcando la **respuesta correcta** y los **feedback de acierto/error** tal cual aparecen en §3.
- [ ] En cada Multiple Choice: activar **Reintentar**, activar **barajar respuestas** (`randomAnswers`) y dejar 1 punto por pregunta.
- [ ] Activar la **diapositiva de resumen** (Summary slide) para mostrar la puntuación total (5 máx.).
- [ ] Añadir las **imágenes decorativas** con ALT según §5 (vacío si son decorativas).
- [ ] Revisar **accesibilidad**: contraste de títulos sobre imagen, foco de teclado, etiquetas de texto en el feedback (no solo color).
- [ ] En **Metadatos**: fijar Licencia = **CC BY-NC-SA 4.0**, autor = AHC, y versión = **1.0.0**. (No dejar la licencia en "U".)
- [ ] **Previsualizar** en escritorio y móvil; comprobar que las 5 respuestas correctas puntúan y que aparece el resumen.
- [ ] **Exportar** el paquete `.h5p` y depositarlo en el **Banco de contenido** del curso "Huella de Carbono Personal".
- [ ] **Solicitar validación al Diseñador Instruccional** antes de publicar y enlazar la actividad en Moodle.

---

> **Versión de la ficha:** diseño v1.0.0 (propuesta). Criterio SemVer para el OA construido: **MAJOR** = cambiar el objetivo/evidencia o el verbo; **MINOR** = añadir/quitar ámbitos o diapositivas sin alterar el objetivo; **PATCH** = correcciones de texto, tildes, feedback o ajustes de comportamiento.
