# Ficha documental — OA-05: Mitos y realidades del clima

> Ficha basada en el contenido REAL del paquete `AHC_H5P_TrueFalse_MitosClima_Basico_EducacionClimatica_v1.0.0.h5p` (lectura directa de `content/content.json` y `h5p.json`). El objeto es un **único enunciado Verdadero/Falso** (H5P.TrueFalse 1.8), no un conjunto de preguntas.

**Coherencia verbo–formato (obligatoria):** el tipo H5P.TrueFalse permite recoger la evidencia del verbo *Discriminar / Juzgar*, porque obliga a la persona a emitir un juicio binario (verdadero o falso) sobre una afirmación concreta del clima, que es exactamente la conducta observable que se quiere medir.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| Código OA | OA-05 |
| Título | Mitos y realidades del clima |
| Tipo H5P | H5P.TrueFalse (Verdadero/Falso) — librería 1.8 |
| Curso destino | Educación Climática |
| Versión | 1.0.0 |
| Autor | Jaber Al Abbadi — Becario H5P |
| Revisor | Diseñador Instruccional — pendiente de validación |
| Fecha | 2026-06 |
| Estado | ✅ Probado en h5p.org · ⏳ Pendiente validación en Moodle |
| Archivo H5P | `OA-05_AHC_H5P_TrueFalse_MitosClima_Basico_EducacionClimatica_v1.0.0.h5p` |

---

## 2. Diseño pedagógico

| Campo | Valor |
|---|---|
| Público objetivo | Ciudadanía (público general, sin conocimientos técnicos previos) |
| Objetivo de aprendizaje | Distinguir un mito habitual sobre el cambio climático de la realidad científica, reconociendo que el calentamiento actual está acelerado por las emisiones humanas. |
| Competencia | Alfabetización climática / pensamiento crítico ante la desinformación ambiental. |
| Verbo observable (Bloom) | Discriminar / Juzgar (nivel Analizar–Evaluar). |
| Evidencia observable | Juzga si una afirmación sobre el cambio climático es verdadera o falsa, emitiendo un juicio binario sobre un mito climático. |
| Duración estimada | 1–3 min (un único enunciado V/F). |
| Prerequisitos | Ninguno; noción básica de qué es el cambio climático. |
| Momento de uso | Inicio (activación/diagnóstico) o cierre (comprobación rápida) de una unidad de educación climática. |

---

## 3. Contenido

| Campo | Valor |
|---|---|
| Tema | Educación climática (mitos y realidades del clima). |
| Mensaje clave | El cambio climático actual no es un simple ciclo natural de la Tierra: existe consenso científico de que el calentamiento global se acelera directamente por las emisiones humanas. |
| Pantallas/Preguntas | **1 afirmación** de tipo Verdadero/Falso. Enunciado real: «El cambio climático es un ciclo natural de la Tierra y las emisiones humanas no tienen un impacto significativo en él.» |
| Respuestas correctas | **Falso** (`correct: "false"`). La afirmación es un mito; la respuesta válida es marcarla como falsa. |
| Feedback | Acierto (responder *Falso*): «¡Exacto! El ritmo actual de calentamiento es causado directamente por la actividad humana.» / Error (responder *Verdadero*): «Cuidado. Existe un consenso científico absoluto de que el calentamiento global actual es acelerado por nuestras emisiones.» |
| Fuentes | Consenso científico sobre el origen antropogénico del calentamiento global (p. ej. IPCC). No se declaran fuentes embebidas dentro del paquete; añadir cita formal en futura revisión. |
| Licencia | Creative Commons CC BY-NC-SA 4.0 (licencia AHC asignada). Nota: el paquete declara internamente `license: "U"` (sin definir); corregir metadato a CC BY-NC-SA 4.0 (ver §8). |

---

## 4. Configuración H5P

| Campo | Valor |
|---|---|
| Ajustes de comportamiento | `enableCheckButton: true`, `enableSolutionsButton: true` (mostrar solución), `autoCheck: false` (comprobación manual con botón), sin diálogos de confirmación (`confirmCheckDialog: false`, `confirmRetryDialog: false`). |
| Reintentos | Habilitados (`enableRetry: true`). |
| Puntuación | 1 punto sobre 1 (ítem único). Marca correcto/incorrecto/sin responder. |
| Aleatorización | No aplica (un solo enunciado, sin orden de opciones aleatorio). |
| Condiciones de finalización | Se completa al pulsar «Check» y registrar respuesta; admite reintento. |
| Compatibilidad móvil | Sí (responsive, interacción táctil de dos botones V/F). |

---

## 5. Accesibilidad

| Campo | Valor |
|---|---|
| ALT en imágenes | N/A — el objeto no incluye imágenes (no hay media embebida; `disableImageZooming: false` está por defecto pero sin imagen asociada). |
| Subtítulos (VTT) | N/A — no contiene vídeo. |
| Transcripción | N/A — no contiene audio ni vídeo. |
| Contraste alto | Sí — usa estilos por defecto de H5P.TrueFalse, con suficiente contraste texto/fondo. |
| No depender solo del color | Sí — el feedback se comunica con texto explícito (mensajes de acierto/error), no solo por color. |
| Lectura fácil | Enunciado de una sola frase, lenguaje sencillo orientado a ciudadanía. |
| Operable por teclado | Sí — H5P.TrueFalse es navegable y accionable por teclado (etiquetas a11y presentes en `l10n`). |
| Carga cognitiva baja | Sí — una única decisión binaria, sin distractores múltiples. |

---

## 6. Moodle

| Campo | Valor |
|---|---|
| Curso | Educación Climática |
| Sección | Mitos y realidades del clima (módulo de educación climática). |
| Enlace | Pendiente de publicación. |
| Visibilidad | Visible una vez publicado. |
| Calificación | Sí (ítem evaluable, 1 punto); puede configurarse como formativo si se desea no ponderar. |
| Finalización | Condición: requerir vista y/o recibir calificación al enviar respuesta. |
| Banco de contenido | Almacenar el `.h5p` en el Banco de contenido del curso para reutilización. |
| Etiquetas/Tags | clima, cambio-climatico, mito, verdadero-falso, educacion-climatica, basico, ciudadania |

---

## 7. Reutilización

| Campo | Valor |
|---|---|
| Qué se puede adaptar | Texto del enunciado, mensajes de feedback (acierto/error), traducción de la interfaz (botones, etiquetas), etiquetas/tags y sección de Moodle. |
| Qué NO debe cambiarse | La respuesta correcta (Falso) y el sentido del mensaje clave (origen antropogénico del calentamiento), para no romper el rigor científico ni la evidencia evaluada. |
| Variables/parámetros del OA | `question` (enunciado), `correct` (false), `behaviour.feedbackOnCorrect`, `behaviour.feedbackOnWrong`, `behaviour.enableRetry`, `behaviour.enableSolutionsButton`, `l10n` (idioma de interfaz). |
| Cursos compatibles | Cualquier curso de educación climática, sostenibilidad o ciudadanía ambiental de nivel básico; reutilizable como ítem dentro de un H5P.QuestionSet. |

---

## 8. QA y mejora

**Checklist de verificación**

- [x] Tipo H5P confirmado por lectura del paquete: H5P.TrueFalse 1.8.
- [x] Enunciado, respuesta correcta y feedback extraídos del `content.json` real (no inventados).
- [x] Coherencia verbo–formato verificada (Discriminar/Juzgar ↔ juicio V/F).
- [x] Reintentos y botón «Mostrar solución» habilitados.
- [x] Sin dependencia exclusiva del color para el feedback.
- [x] Operable por teclado.
- [ ] Interfaz localizada al español (pendiente: `l10n` y `language` están en inglés — «True/False», «Check», «Retry»).
- [ ] Metadato de licencia corregido en el paquete (actualmente `license: "U"`; debe ser CC BY-NC-SA 4.0).
- [ ] Cita formal de fuente científica añadida al objeto.
- [ ] Validación final del Diseñador Instruccional.

**Incidencias**

- Localización: los textos de interfaz (`trueText`, `falseText`, `Check`, `Retry`, etiquetas a11y) y `defaultLanguage`/`language` figuran en inglés, mientras el contenido didáctico está en español. Conviene traducir la UI a español.
- Licencia: el `h5p.json` declara `license: "U"` (sin definir); ajustar a la licencia AHC CC BY-NC-SA 4.0.
- Contenido único: el objeto es un solo enunciado; si se requiere mayor cobertura, considerar agruparlo en un QuestionSet con más mitos climáticos.

**Métricas posteriores** (pendientes de uso real en Moodle)

- % de aciertos (selección de «Falso»).
- Nº de reintentos por intento.
- Tasa de finalización y tiempo medio de respuesta.

**Decisiones de versión**

- v1.0.0: versión inicial publicable.
- Criterio SemVer: **MAJOR** si cambia la respuesta correcta o el constructo evaluado; **MINOR** si se añaden enunciados o se traduce/mejora la interfaz manteniendo el objetivo; **PATCH** para correcciones menores de redacción, feedback o metadatos (p. ej. corregir la licencia).
