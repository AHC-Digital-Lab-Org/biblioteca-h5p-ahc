# Ficha de diseño — OA-14: Cómo calcular tu huella de carbono

> **Estado: Construido y empaquetado como `.h5p`.** Incluye vídeo narrado, subtítulos en español, cinco paradas evaluables y un cierre de acción. Queda pendiente la validación pedagógica final del DI.
>
> **Estado técnico: paquete validado en reproductor H5P.**

> **Coherencia verbo-formato (obligatoria):** el tipo **H5P.InteractiveVideo (Interactive Video)** es el formato idóneo para recoger la evidencia del verbo **Aplicar**. *Aplicar* exige que el estudiante ejecute un procedimiento (usar la calculadora de huella) en un contexto real y paso a paso, no que solo lo recuerde. El vídeo interactivo permite **mostrar el procedimiento mientras se hace** y **detenerlo en cada paso** con paradas interactivas (preguntas de opción única/múltiple, arrastre y huecos) que obligan al estudiante a **tomar la decisión correcta antes de continuar**: qué dato introducir, qué unidad usar, cómo interpretar el resultado. Así la evidencia es **observable y autocalificable** —responde dentro del propio vídeo— y queda demostrado que **aplica** el cálculo, no solo que lo ha visto.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| Código OA | OA-14 |
| Título | Cómo calcular tu huella de carbono |
| Tipo H5P | H5P.InteractiveVideo (Interactive Video / Vídeo interactivo) |
| Familia (plan AHC §5) | Práctica |
| Curso destino | Huella de Carbono Personal |
| Público objetivo | Ciudadanía (nivel inicial) |
| Verbo Bloom | Aplicar |
| Versión prevista | 1.0.0 |
| Licencia | Creative Commons CC BY-NC-SA 4.0 |
| Estado | ✅ Probado en h5p.org · ⏳ Pendiente validación en Moodle |
| Archivo H5P | `OA-14_AHC_H5P_InteractiveVideo_CalcularHuella_Intermedio_HuellaPersonal_v1.0.0.h5p` |

> Nota de trazabilidad: el título interno previsto del paquete (`h5p.json`) será "OA-14: Como calcular tu huella de carbono" (sin tildes en metadatos por compatibilidad, como en OA-08). La licencia debe fijarse explícitamente a **CC BY-NC-SA 4.0** en los metadatos al construir (no dejar "U").

---

## 2. Diseño pedagógico

| Campo | Valor |
|---|---|
| Objetivo de aprendizaje | **Aplicar** la calculadora de huella de carbono personal de la AHC, recorriendo paso a paso las categorías (transporte, energía del hogar, alimentación y consumo) hasta obtener e interpretar un resultado anual en toneladas de CO₂ equivalente (t CO₂e). |
| Competencia | Alfabetización climática práctica: medir el propio impacto y traducir hábitos cotidianos en una cifra de emisiones comparable. |
| Verbo observable (Bloom) | Aplicar |
| Evidencia observable | El estudiante completa correctamente, dentro del vídeo, las paradas interactivas que reproducen cada paso del cálculo (introducir un dato, elegir la unidad correcta, clasificar una emisión y leer el resultado), demostrando que sabe usar la calculadora. |
| Duración estimada | 6–8 min (vídeo de ~5 min + paradas interactivas) |
| Prerequisitos | Concepto básico de huella de carbono y de CO₂ equivalente (recomendado haber visto OA-01 *Conceptos Climáticos Básicos*). |
| Mensaje clave | Calcular tu huella es sencillo si sigues el orden: **reúne tus datos → elige la categoría → introduce el consumo con su unidad → suma todas las categorías → interpreta el total y fija una acción de reducción**. |
| Criterio de éxito | Responder correctamente al menos **4 de las 5 paradas evaluables** (≥ 80 %) y llegar al final del vídeo. |
| Momento de uso | Desarrollo del curso (sesión práctica "Mide tu huella"), justo antes de que el estudiante use la calculadora real por su cuenta. |

---

## 3. Contenido propuesto

**Vídeo base (propuesto, a grabar/locutar por la AHC):** captura de pantalla narrada de la calculadora de huella personal de la AHC (~5 min), con voz en off que guía paso a paso. Locución y subtítulos en español. Sobre esa línea de tiempo se insertan **6 paradas interactivas** (5 evaluables + 1 panel de resumen no evaluable).

**Consigna general (texto de portada/Bookmark inicial del vídeo):**
> "En este vídeo vas a calcular tu huella de carbono paso a paso. El vídeo se detendrá en cada paso: responde antes de continuar. Necesitarás datos aproximados de tu transporte, tu energía en casa y tu alimentación del último año. ¡Empezamos!"

### Paradas interactivas propuestas (línea de tiempo)

| # | Tiempo aprox. | Paso del cálculo | Tipo de interacción (H5P) | Consigna exacta |
|---|---|---|---|---|
| 1 | 00:45 | Reunir datos | Single Choice / Multiple Choice | "Antes de empezar, ¿qué dato NO necesitas para esta calculadora?" |
| 2 | 01:40 | Transporte | Drag and Drop (clasificar) | "Arrastra cada medio de transporte a su nivel de emisiones por kilómetro." |
| 3 | 02:35 | Energía del hogar | Multiple Choice (unidad correcta) | "Tu factura de luz viene en kWh. ¿Qué casilla de la calculadora debes rellenar con ese dato?" |
| 4 | 03:30 | Alimentación | Single Choice | "Si quieres reducir la parte de tu huella que más pesa en alimentación, ¿qué cambio tiene MÁS impacto?" |
| 5 | 04:20 | Interpretar el resultado | Fill in the Blanks (hueco numérico/unidad) | "La calculadora muestra tu resultado anual. Completa: 'Mi huella es de 6,4 ____ al año'." |
| 6 | 04:55 | Resumen y acción | Summary / panel de texto (no evaluable) | "Resume lo aprendido y elige una acción de reducción para esta semana." |

### Detalle de cada ítem (respuesta correcta + feedback)

**Parada 1 — "¿Qué dato NO necesitas?" (Single Choice, evaluable)**
- A) Los kilómetros que recorres en coche al año.
- B) Los kWh de electricidad de tu hogar.
- C) **El número de tu DNI.** ✅ *(correcta: es un dato personal irrelevante para el cálculo)*
- D) Cuántas veces a la semana comes carne.
- Feedback acierto: "¡Correcto! La calculadora solo te pide datos de consumo (energía, transporte, alimentación). Tus datos personales no influyen en las emisiones."
- Feedback error: "No exactamente. La huella se calcula con tus consumos —transporte, energía y alimentación—, no con datos personales como el DNI."

**Parada 2 — "Clasifica el transporte" (Drag and Drop, evaluable)**
- Zonas de destino: **Emisiones bajas**, **Emisiones medias**, **Emisiones altas** (por km y pasajero).
- Cartas a arrastrar y clasificación correcta:
  - Ir andando o en bicicleta → **Emisiones bajas** ✅
  - Tren de cercanías / metro → **Emisiones bajas** ✅
  - Coche de gasolina (1 ocupante) → **Emisiones medias** ✅
  - Avión (vuelo de corto alcance) → **Emisiones altas** ✅
- Feedback acierto: "¡Bien! En general: andar, bici y tren emiten poco por kilómetro; el coche en solitario, más; y el avión es de lo que más emite."
- Feedback error: "Revisa la clasificación: el avión y el coche en solitario emiten mucho más por kilómetro que la bici o el tren."

**Parada 3 — "Unidad correcta de energía" (Multiple Choice, evaluable; admite 1 correcta)**
- A) **La casilla 'Electricidad (kWh/año)'.** ✅
- B) La casilla 'Agua (litros)'.
- C) La casilla 'Kilómetros en coche'.
- D) La casilla 'Residuos (kg)'.
- Feedback acierto: "¡Correcto! Los kWh de tu factura van en la casilla de electricidad. Usar la unidad y la casilla correctas es clave para no falsear el resultado."
- Feedback error: "Cuidado con la unidad: los kWh son energía eléctrica y van en la casilla 'Electricidad (kWh/año)', no en agua, transporte ni residuos."

**Parada 4 — "Cambio de mayor impacto en alimentación" (Single Choice, evaluable)**
- A) Usar bolsas reutilizables en la compra.
- B) **Reducir el consumo de carne de vacuno.** ✅
- C) Comprar fruta en envases más pequeños.
- D) Cambiar de marca de café.
- Feedback acierto: "¡Eso es! La carne de vacuno tiene una huella muy alta; reducir su consumo es de los cambios alimentarios que más bajan tu huella."
- Feedback error: "Las bolsas o los envases ayudan, pero su efecto es pequeño. En alimentación, reducir la carne de vacuno es lo que más reduce la huella."

**Parada 5 — "Interpreta tu resultado" (Fill in the Blanks, evaluable)**
- Texto con hueco: "La calculadora muestra mi resultado anual. Mi huella es de 6,4 *toneladas de CO₂ equivalente* al año."
- Respuesta correcta del hueco: **toneladas de CO₂ equivalente** (se aceptan variantes: "t CO₂e", "toneladas de CO2 equivalente", "toneladas de CO2e").
- Feedback acierto: "¡Correcto! El resultado se expresa en toneladas de CO₂ equivalente al año (t CO₂e). Así puedes compararlo con la media nacional."
- Feedback error: "Casi: la huella personal se mide en *toneladas de CO₂ equivalente al año* (t CO₂e), no en otra unidad."

**Parada 6 — "Resumen y acción" (Summary / panel, NO evaluable)**
- Panel de cierre con los 5 pasos resumidos y la frase del mensaje clave.
- Llamada a la acción: "Elige UNA acción para esta semana: ☐ ir en bici un día, ☐ bajar 1 grado la calefacción, ☐ una comida sin carne, ☐ apagar lo que no uses." *(selección reflexiva, sin puntuación)*

**Fuente del contenido:** material didáctico propio de la AHC (calculadora de huella de carbono personal y guía de uso). Ítems redactados para este OA; cifras de ejemplo (6,4 t CO₂e) ilustrativas, ajustables a la media de referencia que use la AHC.

---

## 4. Configuración H5P prevista

| Campo | Valor |
|---|---|
| Comportamiento general | Vídeo con paradas que **pausan automáticamente** (`pause: true` en cada interacción); el estudiante debe responder para reanudar. Botón de la barra de progreso visible. |
| Reintentos | Sí: "Reintentar" activado por interacción (`enableRetry: true`) para que el estudiante corrija antes de seguir. |
| Puntuación | Automática y agregada: 1 punto por cada parada evaluable correcta (5 evaluables → **5 puntos máx.**). Mostrar barra de puntuación y, al final, **Summary screen** del Interactive Video con el total. |
| Mostrar solución | Activado por interacción (`enableSolutionsButton: true`) para reforzar el aprendizaje tras el error. |
| Aleatorización | No procede para el orden de las paradas (debe seguir la secuencia del procedimiento). En la parada 1/3/4 (opción) se puede **barajar el orden de las opciones**; en la 2 (arrastre) se barajan las cartas. |
| Navegación | Permitir **retroceder** y volver a ver un tramo; **no** permitir saltar paradas sin responder (las pausas son obligatorias). Marcadores (bookmarks) por paso para facilitar el repaso. |
| Condiciones de finalización | Llegar al final del vídeo habiendo respondido las 5 paradas evaluables; reporte de calificación vía xAPI. |
| Compatibilidad móvil | Sí: reproductor responsive; controles táctiles; el arrastre de la parada 2 funciona en táctil. Vídeo en formato ligero (MP4 H.264) y subtítulos VTT. |

---

## 5. Accesibilidad prevista

| Campo | Valor |
|---|---|
| Texto alternativo (ALT) | Las cartas de imagen de la parada 2 (medios de transporte) llevarán ALT descriptivo (p. ej. "Bicicleta", "Avión"). Si se usan iconos, texto equivalente. |
| Subtítulos (VTT) | **Sí, obligatorios**: pista de subtítulos en español sincronizada con la locución (`track kind="captions"`). |
| Transcripción | Sí: transcripción completa del vídeo disponible junto a la actividad (texto descargable o panel) para quien no pueda usar audio. |
| Contraste | Alto: texto de las paradas sobre fondo sólido, cumpliendo contraste AA; no usar texto sobre zonas de vídeo de bajo contraste. |
| No depender solo del color | La corrección se indica con icono + etiqueta ("Correcto"/"Incorrecto"), no solo con color. |
| Navegación por teclado | Las interacciones (opción, arrastre, huecos) deben ser operables por teclado; controles del reproductor accesibles con Tab/Enter. Verificar foco visible. |
| Lenguaje claro | Frases cortas, vocabulario cotidiano, una instrucción por parada; evitar tecnicismos sin explicar (CO₂e se introduce en la parada 5). |
| Carga cognitiva | Baja: una decisión por parada, pausas que dan tiempo a pensar, posibilidad de retroceder. |

---

## 6. Reutilización

| Campo | Valor |
|---|---|
| Cursos AHC donde insertarlo | **Huella de Carbono Personal** (uso principal). Reutilizable en *Educación ambiental* y en cualquier curso de sensibilización para ciudadanía que incluya la calculadora; adaptable a una variante "huella de una pyme" para el curso *Embajador Climático*. |
| Qué parámetros variar | El **vídeo base** (sustituir por la captura de la calculadora vigente), las **cifras de ejemplo** (parada 5), las **opciones** de cada parada, el **número de paradas** (añadir categorías como agua o residuos), los **textos de feedback** y la **acción semanal** de la parada 6. |
| Qué NO debe cambiarse | La **secuencia del procedimiento** (reunir datos → categoría → unidad correcta → suma → interpretar resultado) y la **unidad del resultado** (t CO₂e), que son el núcleo del verbo *Aplicar*. |
| Variables/parámetros del OA | `interactiveVideo.video` (fuente del vídeo y subtítulos VTT), `assets.interactions` (paradas: tipo, tiempo, `pause`, contenido), `behaviour` (reintentos, soluciones), `summary` (pantalla de resumen), metadatos de licencia. |

---

## 7. Pasos para construirlo (checklist para el becario)

> Montaje en el **editor H5P de Moodle** (Banco de contenido) o en **Lumi** (escritorio) y exportación del `.h5p`.

- [ ] **Validación previa del DI**: confirmar esta ficha (objetivo, paradas, ítems y feedback) antes de tocar el editor.
- [ ] Conseguir/grabar el **vídeo base** (captura narrada de la calculadora, ~5 min) y generar los **subtítulos VTT** en español.
- [ ] En el Banco de contenido, **crear contenido → Interactive Video**; subir el vídeo (o pegar URL) y cargar la pista de subtítulos.
- [ ] En la pestaña **Add interactions**, insertar las **6 paradas** en los tiempos indicados (00:45, 01:40, 02:35, 03:30, 04:20, 04:55), cada una con su tipo H5P, activando **"Pause video"**.
- [ ] Volcar **consignas, opciones, respuestas correctas y feedback** de la sección 3 en cada parada.
- [ ] Configurar **comportamiento** (sección 4): reintentos y soluciones por interacción, puntuación agregada (5 pts), barra de progreso, marcadores por paso y **Summary screen** final.
- [ ] Revisar **accesibilidad** (sección 5): ALT de las cartas, subtítulos activos, contraste, foco por teclado.
- [ ] Fijar **metadatos**: título "OA-14: Como calcular tu huella de carbono", autor (becario), licencia **CC BY-NC-SA 4.0**, versión **v1.0.0**.
- [ ] **Probar** en escritorio y móvil (las 5 paradas evaluables puntúan, pausas obligatorias, navegación atrás OK).
- [ ] **Exportar** el `.h5p`, guardarlo en el repositorio de la biblioteca y enlazar la actividad en el curso *Huella de Carbono Personal*.
- [ ] **Validación final del DI** y publicación en Moodle.
