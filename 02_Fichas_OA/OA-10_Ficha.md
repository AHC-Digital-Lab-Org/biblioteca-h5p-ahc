# Ficha documental — OA-10: Cuestionario de Evaluación Final

> **Coherencia verbo-formato (obligatoria):** el tipo **H5P.QuestionSet (Question Set)** —batería de preguntas autocalificable que combina **Opción múltiple** y **Verdadero/Falso**— permite recoger la evidencia del verbo **Evaluar**, ya que el cuestionario somete al participante a una evaluación final integrada en la que debe emitir un juicio sobre cada afirmación (p. ej. valorar si "plantar árboles es la *única* solución" es verdadero o falso) y seleccionar la respuesta correcta, quedando registrada de forma observable y puntuable su decisión.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| Código OA | OA-10 |
| Título | Cuestionario de Evaluación Final |
| Tipo H5P | H5P.QuestionSet 1.20 (Question Set / Batería de preguntas) — contiene H5P.MultiChoice 1.16 y H5P.TrueFalse 1.8 |
| Curso destino | Embajador Climático |
| Versión | 1.0.0 |
| Autor | Jaber Al Abbadi — Becario H5P |
| Revisor | Diseñador Instruccional — pendiente de validación |
| Fecha | 2026-06 |
| Estado | ✅ Probado en h5p.org · ⏳ Pendiente validación en Moodle |
| Archivo H5P | `OA-10_AHC_H5P_QuestionSet_EvaluacionFinal_Intermedio_EmbajadorClimatico_v1.0.0.h5p` |

> Nota de trazabilidad: el título interno del paquete (`h5p.json`) es "OA-10: Cuestionario de Evaluacion Final" (sin tildes). Biblioteca principal declarada: `H5P.QuestionSet` 1.20.

---

## 2. Diseño pedagógico

| Campo | Valor |
|---|---|
| Público objetivo | Embajadores y participantes del curso (nivel intermedio). |
| Objetivo de aprendizaje | Evaluar lo aprendido en el curso respondiendo una batería final de preguntas: identificar la principal fuente de emisiones y juzgar la validez de afirmaciones sobre soluciones climáticas. |
| Competencia | Alfabetización climática: consolidar y demostrar el dominio de los conceptos clave del cambio climático mediante una evaluación integrada. |
| Verbo observable (Bloom) | Evaluar (apoyado en Recordar/Comprender al identificar la respuesta correcta). |
| Evidencia observable | Responde la batería final de preguntas y alcanza al menos el 50 % de aciertos (1 de 2 preguntas) para superar el cuestionario. |
| Duración estimada | 3–5 min. |
| Prerequisitos | Haber completado los contenidos previos del curso Embajador Climático (conceptos de emisiones de GEI, sectores emisores y estrategias de acción climática). |
| Momento de uso | Cierre (evaluación final / comprobación integrada de aprendizajes). |

---

## 3. Contenido

| Campo | Valor |
|---|---|
| Tema | Evaluación integrada. |
| Mensaje clave | El **sector energético** es la mayor fuente de emisiones a nivel global, y **no existe una solución única** frente al cambio climático: plantar árboles, por sí solo, no basta. |
| Pantallas/Preguntas | **Question Set con 2 preguntas** (sin página de intro; progreso por puntos). **P1 – Opción múltiple** (H5P.MultiChoice): "¿Cuál de estos sectores genera más emisiones a nivel global?" con 3 opciones (Energía, Moda, Agricultura) y orden de opciones aleatorizado. **P2 – Verdadero/Falso** (H5P.TrueFalse): "Plantar árboles es la única solución para frenar el cambio climático." No hay tarjetas, hotspots ni huecos: el OA es exclusivamente un cuestionario de 2 ítems. |
| Respuestas correctas | **P1:** "Energía" (única opción correcta; "Moda" y "Agricultura" son distractores). **P2:** **Falso** (la afirmación es errónea: plantar árboles no es la única solución). |
| Feedback | Sin feedback personalizado en el contenido: las opciones no llevan texto de retroalimentación (`chosenFeedback`/`notChosenFeedback` vacíos) y los rangos de `overallFeedback` (0–100) están sin texto. Se muestran solo los mensajes genéricos del componente ("Correct answer"/"Wrong answer", barra "You got :num out of :total points") y, al final, la página de resultados con el botón "Mostrar solución". |
| Fuentes | Contenido didáctico propio de la AHC (evaluación de los conceptos tratados en el curso Embajador Climático). |
| Licencia | Creative Commons CC BY-NC-SA 4.0 *(a registrar en metadatos: el `h5p.json` del paquete declara actualmente licencia "U" / sin especificar; pendiente de fijar a CC BY-NC-SA 4.0)*. |

**Ítems reales del cuestionario:**
> **P1 (Opción múltiple):** "¿Cuál de estos sectores genera más emisiones a nivel global?" → Energía *(correcta)* · Moda · Agricultura.
>
> **P2 (Verdadero/Falso):** "Plantar árboles es la única solución para frenar el cambio climático." → **Falso** *(correcta)*.

---

## 4. Configuración H5P

| Campo | Valor |
|---|---|
| Ajustes de comportamiento | Sin página de introducción (`showIntroPage: false`); indicador de progreso por puntos (`progressType: "dots"`); navegación hacia atrás permitida (`disableBackwardsNavigation: false`); botón "Comprobar" forzado (`override.checkButton: true`). Cada pregunta tiene "Comprobar", "Mostrar solución" y "Reintentar" activados. |
| Reintentos | Sí — botón "Retry" en la página de resultados (`showRetryButton: true`) y `enableRetry: true` en cada pregunta. |
| Puntuación | Sí, automática: 1 punto por pregunta correcta (2 puntos máx.). Umbral de aprobado **50 %** (`passPercentage: 50`) → basta acertar 1 de 2. La P1 muestra puntos por opción (`showScorePoints: true`). |
| Aleatorización | Orden de preguntas **fijo** (`randomQuestions: false`); en la P1 de opción múltiple **se barajan las opciones** (`randomAnswers: true`). |
| Condiciones de finalización | Responder ambas preguntas y llegar a la página de resultados (`showResultPage: true`), que muestra la puntuación final y permite "Mostrar solución"/"Reintentar". |
| Compatibilidad móvil | Sí (responsive; selección táctil de opciones y de Verdadero/Falso). |

---

## 5. Accesibilidad

| Campo | Valor |
|---|---|
| ALT en imágenes | N/A — el cuestionario no incluye imágenes ni medios (`media` sin recurso). |
| Subtítulos (VTT) | N/A — sin vídeo (la librería H5P.Video figura como dependencia pero no se usa en el contenido). |
| Transcripción | N/A — sin audio/vídeo. |
| Contraste alto | Sí — usa los estilos por defecto de H5P, con contraste adecuado texto/fondo. |
| No depender solo del color | Sí — la corrección se indica además con iconos y etiquetas ("Correct answer"/"Wrong answer"), no solo con color. |
| Lectura fácil | Preguntas cortas y vocabulario claro; un solo enunciado por pantalla. |
| Operable por teclado | Sí — opción múltiple y Verdadero/Falso son navegables y seleccionables por teclado, con textos ARIA de comprobar/solución/reintentar. |
| Carga cognitiva baja | Sí — solo 2 preguntas, una por pantalla, con progreso por puntos visible. |

---

## 6. Moodle

| Campo | Valor |
|---|---|
| Curso | Embajador Climático. |
| Sección | Evaluación final del curso. |
| Enlace | Pendiente de publicación. |
| Visibilidad | Visible para estudiantes una vez publicado. |
| Calificación | Sí — el Question Set registra puntuación (2 puntos máx., aprobado al 50 %); califica vía xAPI/Banco de contenido. |
| Finalización | Condición: actividad enviada/completada (opcionalmente, calificación mínima ≥ 50 %). |
| Banco de contenido | Almacenar el `.h5p` en el Banco de contenido del curso y enlazar la actividad. |
| Etiquetas/Tags | `evaluación-final`, `cuestionario`, `emisiones`, `cambio-climático`, `embajador-climático`, `OA-10`, `QuestionSet`, `intermedio` |

---

## 7. Reutilización

| Campo | Valor |
|---|---|
| Qué se puede adaptar | Número y redacción de las preguntas (ampliar la batería), distractores de la P1, umbral de aprobado (`passPercentage`), activar página de intro, añadir feedback por opción y por rango, e incluir más tipos de pregunta dentro del set. |
| Qué NO debe cambiarse | Las respuestas correctas validadas (P1 = Energía; P2 = Falso) y el carácter de **evaluación final integrada** del OA (núcleo evaluativo). |
| Variables/parámetros del OA | `passPercentage`, `progressType`, `randomQuestions`, `disableBackwardsNavigation`, `introPage`, `endGame` (página de resultados, botones), y por pregunta: `answers/correct`, `behaviour` (reintento, solución, comprobar), `randomAnswers`, `overallFeedback`. |
| Cursos compatibles | Embajador Climático; cualquier curso de sensibilización ambiental/sostenibilidad que requiera una evaluación final autocalificable de conceptos básicos. |

---

## 8. QA y mejora

**Checklist de verificación**

- [x] El paquete abre y el Question Set carga las 2 preguntas (MultiChoice + TrueFalse).
- [x] Respuestas correctas confirmadas: P1 = "Energía"; P2 = "Falso".
- [x] Umbral de aprobado configurado (50 %) y puntuación automática operativa (2 puntos máx.).
- [x] Reintentos, "Mostrar solución" y página de resultados activados.
- [x] Aleatorización de opciones en la P1 (`randomAnswers: true`).
- [x] Sin dependencia exclusiva del color para el feedback.
- [x] Operable por teclado y compatible con móvil.
- [ ] Metadatos de licencia fijados a CC BY-NC-SA 4.0 en el paquete (actualmente "U").
- [ ] Idioma del paquete a `es` (actualmente `en`) y traducción de las etiquetas de UI ("Check", "Retry", "Show solution", "True/False").
- [ ] Validación final del Diseñador Instruccional.
- [ ] Publicación y enlace en Moodle.

| Campo | Valor |
|---|---|
| Incidencias | (1) La licencia en `h5p.json` figura como "U" (sin especificar); actualizar a CC BY-NC-SA 4.0. (2) Idioma del paquete en `en` y botones de UI en inglés ("Start Quiz", "Check", "Retry"…); localizar a español. (3) La batería tiene **solo 2 preguntas**, escasa para una "evaluación final"; se recomienda ampliarla. (4) Sin feedback personalizado por opción ni por rango (mejora opcional). |
| Métricas posteriores | Pendientes de uso real en Moodle: % de aprobados, aciertos por pregunta, intentos medios, tiempo de resolución y % de finalización. |
| Decisiones de versión | v1.0.0 inicial (publicación base). Criterio SemVer: **MAJOR** = cambio del objetivo/evidencia o reestructuración del cuestionario; **MINOR** = añadir preguntas o feedback sin alterar el objetivo; **PATCH** = correcciones menores de texto, tildes, idioma, licencia o ajustes de comportamiento. |
