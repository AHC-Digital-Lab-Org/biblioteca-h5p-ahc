# Ficha — OA-16: Qué acción reduce más tu huella

> **Estado: Empaquetado.** El paquete `.h5p` de este OA está disponible en `03_H5P_exportables/`, generado a partir de esta ficha y verificado en un reproductor H5P. Esta ficha documenta su diseño (consigna, ítems, feedback y configuración); el contenido pedagógico queda a validación del Diseñador Instruccional (DI) como parte del control de calidad habitual.
>
> **Por qué existe esta ficha:** sirve como guion único y autocontenido para que el becario H5P pueda construir el OA sin ambigüedad (texto exacto, opciones, marcado de la correcta y feedback), y para que el DI pueda validar el contenido y la coherencia pedagógica **antes** de invertir tiempo en el montaje. Proviene del backlog de la biblioteca (propuesta "¿Qué acción reduce más la huella?", §17 de `backlog.md`).
>
> **Coherencia verbo-formato (obligatoria):** el verbo Bloom de este OA es **Comparar**. El tipo **H5P.MultiChoice (Multiple Choice)** es el formato idóneo para recoger esa evidencia porque presenta **varias acciones de reducción en paralelo** y obliga a la persona a **sopesar el impacto relativo de cada una** y elegir la de **mayor** reducción (no solo a reconocer una verdad aislada). La elección entre alternativas plausibles es, en sí misma, un acto de comparación; el componente la captura de forma **observable** (la opción marcada) y **autocalificable** (1 punto si acierta la de mayor impacto), y el **feedback diferenciado por opción** permite explicar *por qué* una acción reduce más que otra, que es justo el aprendizaje que persigue el verbo Comparar.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| Código OA | OA-16 |
| Título | Qué acción reduce más tu huella |
| Tipo H5P | H5P.MultiChoice (Multiple Choice / Opción múltiple) |
| Familia (plan AHC §5) | Evaluación |
| Curso destino | Huella de Carbono Personal |
| Público | Ciudadanía |
| Verbo Bloom | Comparar |
| Versión prevista | v1.0.0 |
| Licencia | Creative Commons CC BY-NC-SA 4.0 *(a fijar en los metadatos del paquete al construirlo)* |
| Estado | ✅ Probado en h5p.org · ⏳ Pendiente validación en Moodle |
| Archivo H5P | `OA-16_AHC_H5P_MultiChoice_AccionMayorImpacto_Basico_HuellaPersonal_v1.0.0.h5p` |

> Nota de trazabilidad: cuando se construya, el título interno del paquete (`h5p.json`) será "OA-16: Que accion reduce mas tu huella" (sin tildes en el identificador, como en el resto de la biblioteca).

---

## 2. Diseño pedagógico

| Campo | Valor |
|---|---|
| Objetivo de aprendizaje | **Comparar** el impacto de varias acciones cotidianas de reducción de emisiones y **seleccionar la que más reduce** la huella de carbono personal anual. |
| Competencia | Alfabetización climática aplicada: jerarquizar acciones individuales por su efecto real sobre las emisiones, evitando el "ruido" de gestos de bajo impacto. |
| Verbo observable (Bloom) | **Comparar** (sopesar alternativas y elegir la de mayor efecto). |
| Evidencia observable | La persona marca, entre 4 opciones, la acción de **mayor** reducción de huella; el componente registra la opción elegida y la puntúa (acierto/error). |
| Duración estimada | 3–5 min (microlearning: 1 idea principal, 1–3 evidencias). |
| Prerequisitos | Concepto básico de huella de carbono personal y de toneladas de CO₂ equivalente (tCO₂e). Recomendable haber visto un OA introductorio de huella personal del mismo curso. |
| Mensaje clave | **No todas las acciones reducen lo mismo.** Unas pocas decisiones de alto impacto (transporte, vuelos, dieta, energía del hogar) pesan mucho más que la suma de muchos gestos pequeños. |
| Criterio de éxito | Acertar la opción de mayor impacto (1/1 punto). Umbral de superación sugerido: 100 % del único ítem (o la media del Question Set si se inserta en uno). |
| Momento de uso | **Cierre / comprobación** de un bloque de huella personal, o **evaluación** rápida formativa dentro del curso. |

---

## 3. Contenido propuesto

**Consigna exacta (taskDescription):**

> "Una persona quiere reducir su huella de carbono personal en un año. **¿Cuál de estas acciones la reduciría MÁS?** Compara el impacto de cada opción y elige una."

**Formato:** 1 pregunta de opción múltiple, **respuesta única** (`singleAnswer`), 4 opciones. Los órdenes de magnitud son ilustrativos y coherentes con el dominio (estimaciones de reducción anual por persona); se redondean para facilitar la comparación y se validarán con la fuente de la AHC antes de construir.

| # | Opción (texto del ítem) | ¿Correcta? | Reducción anual orientativa | Feedback de la opción |
|:--:|---|:--:|---|---|
| A | **Prescindir de un vuelo transatlántico de ida y vuelta al año** (p. ej. Europa–América). | ✅ **Sí** | ~1,5–2 tCO₂e | "¡Correcto! Un único vuelo de largo radio puede emitir más de 1 tonelada de CO₂e. Evitarlo es de las decisiones individuales de **mayor** impacto." |
| B | Cambiar todas las bombillas de casa por LED. | ❌ No | ~0,03–0,05 tCO₂e | "Es útil y conviene hacerlo, pero su efecto es pequeño comparado con el transporte aéreo: ahorra decenas de kg, no toneladas." |
| C | Reciclar correctamente el vidrio y el papel durante todo el año. | ❌ No | ~0,1–0,2 tCO₂e | "Reciclar importa, pero reduce mucho menos que evitar un vuelo. Gestionar bien los residuos no compensa una emisión de transporte de más de 1 tonelada." |
| D | Usar una bolsa de tela en lugar de bolsas de plástico en la compra. | ❌ No | < 0,01 tCO₂e | "Es un buen hábito, pero su impacto en la huella anual es mínimo (kilos, no toneladas). Es el gesto de **menor** efecto de la lista." |

**Respuesta correcta:** **Opción A** (evitar un vuelo transatlántico de ida y vuelta).

**Feedback global (overallFeedback, por rangos):**

| Rango de aciertos | Texto de feedback global |
|---|---|
| 0 % (fallo) | "Casi. Recuerda: las acciones de **mayor** impacto suelen estar en el transporte de largo radio, los vuelos, la dieta y la energía del hogar; los gestos pequeños suman, pero no compensan una emisión de más de una tonelada." |
| 100 % (acierto) | "¡Muy bien! Has identificado la acción de **mayor** reducción. Priorizar pocas decisiones de alto impacto reduce tu huella más que muchos gestos pequeños." |

> **Nota de validación de datos:** las cifras de reducción son órdenes de magnitud para sostener la comparación didáctica; el DI debe confirmarlas con la fuente de referencia de la AHC (calculadora/factores de emisión vigentes) antes de construir. Lo **no negociable** del OA es el orden relativo de impacto: **A > C > B > D**.

---

## 4. Configuración H5P prevista

| Campo | Valor previsto |
|---|---|
| Comportamiento | Botón "Comprobar" activado (`enableCheckButton: true`); sin feedback instantáneo por clic (se revela al comprobar). Tipo de respuesta: **única** (`singleAnswer: true`, `singlePoint: true`). |
| Reintentos | Sí — "Reintentar" activado (`enableRetry: true`). |
| Puntuación | Automática: **1 punto** si se marca la opción correcta (A), 0 si no. "Mostrar solución" activado (`enableSolutionsButton: true`) para revelar la correcta y los feedbacks por opción. |
| Aleatorización | **Sí** — barajar el orden de las opciones (`randomAnswers: true`) para evitar el sesgo de posición. El feedback va ligado a cada opción, no a su posición, así que el barajado no lo rompe. |
| Navegación | Actividad de una sola pantalla; sin paginación. Si se inserta en un Question Set, hereda los botones de navegación del conjunto. |
| Compatibilidad móvil | Sí — `H5P.MultiChoice` es responsive y operable por toque; opciones a ancho completo para facilitar la pulsación en pantallas pequeñas. |

---

## 5. Accesibilidad prevista

| Campo | Valor previsto |
|---|---|
| Texto ALT en imágenes | N/A en el diseño base (actividad solo de texto). Si se añade una imagen ilustrativa (p. ej. un avión), llevará ALT descriptivo y **no** portará información imprescindible para responder. |
| Contraste | Estilos por defecto de H5P, con contraste texto/fondo adecuado (AA). No se usará color como única señal. |
| No depender solo del color | El acierto/error se indica además con icono y texto ("Correcto"/"Incorrecto") y con el feedback por opción, no solo con color. |
| Navegación por teclado | Sí — `MultiChoice` permite seleccionar opciones y pulsar "Comprobar" con teclado (Tab/Flechas/Espacio), con etiquetas ARIA en cada opción. |
| Subtítulos / transcripción | N/A — el diseño base no incluye vídeo ni audio. Si se añadieran, se incluirá subtitulado VTT y transcripción. |
| Lenguaje claro | Frases cortas, una idea por opción, vocabulario cotidiano; las cifras se expresan con unidades comprensibles (toneladas/kg de CO₂e) y orden de magnitud. |
| Carga cognitiva | Baja: una sola pregunta, 4 opciones, una decisión. |

---

## 6. Reutilización

| Campo | Valor |
|---|---|
| Cursos AHC donde insertar | **Huella de Carbono Personal** (curso destino); también encaja en cursos de **sensibilización ciudadana / EcoGestos** y en el **Cuestionario de Evaluación Final** (como ítem de un Question Set). |
| Qué parámetros variar | `question`/`taskDescription` (la consigna), el **conjunto de opciones** y cuál es la correcta (`answers[].correct`), el **feedback por opción** (`answers[].tipsAndFeedback`), los **rangos de feedback global** (`overallFeedback`), y `behaviour` (reintentos, solución, barajado). |
| Variantes sugeridas | Cambiar el contexto manteniendo el verbo Comparar: "¿qué acción reduce más en una **pyme**?" (curso Embajador/Empresa), o "¿qué medida del **hogar** ahorra más energía?". Reutilizar la estructura A>C>B>D con datos del nuevo dominio. |
| Qué NO debe cambiarse | El núcleo evaluativo: que la opción correcta sea la de **mayor** impacto real y que el orden relativo de impacto entre opciones se sostenga con datos. Si cambia eso, cambia el objetivo (ver criterio de versión). |
| Familia y licencia | Pertenece a la familia **Evaluación** (plan §5); se mantiene la licencia **CC BY-NC-SA 4.0** en todas las variantes. |

---

## 7. Pasos para construirlo (checklist para el becario)

Construir en el editor H5P (Lumi de escritorio o el plugin H5P / Banco de contenido de Moodle):

- [ ] Crear contenido nuevo de tipo **Multiple Choice** (`H5P.MultiChoice`).
- [ ] Pegar la **consigna** del §3 en el campo *Question*.
- [ ] Crear **4 opciones** con el texto de A–D del §3; marcar **A como correcta** y B, C, D como incorrectas.
- [ ] Rellenar el **feedback por opción** (columna "Feedback de la opción") en *Tips and feedback* de cada respuesta.
- [ ] Añadir el **feedback global** por rangos (0 % y 100 %) en *Overall Feedback*.
- [ ] En *Behavioural settings*: activar **Retry**, **Show solution** y **Check**; poner **Question Type = Single answer**; activar **Randomize answers**.
- [ ] En *Metadata*: fijar **título** "OA-16: Que accion reduce mas tu huella", **autor** (becario H5P), **licencia = CC BY-NC-SA 4.0** y **versión 1.0.0**.
- [ ] Validar con el **DI** las cifras de reducción y el orden A>C>B>D antes de publicar.
- [ ] **Exportar** el paquete `.h5p` (botón *Download / Export*) y subirlo al **Banco de contenido** del curso *Huella de Carbono Personal*.
- [ ] Revisar accesibilidad rápida: navegación por teclado y que el feedback no dependa solo del color.
- [ ] Actualizar el **backlog** y el catálogo: marcar OA-16 como "prototipado / construido".

---

> **Resumen de estado:** ficha de **diseño** completa y lista para construcción. Pendiente: montaje en editor H5P, validación de cifras por el DI, fijación de licencia en metadatos y exportación/publicación en Moodle.
