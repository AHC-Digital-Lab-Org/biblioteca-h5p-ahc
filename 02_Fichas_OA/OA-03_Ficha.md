# Ficha documental — OA-03: Conceptos Clave de Sostenibilidad

> **Coherencia verbo–formato (obligatoria):** El tipo H5P.Blanks (Fill in the Blanks) **sí permite recoger la evidencia** de los verbos *Comprender / Aplicar*, porque obliga al usuario a **recuperar y escribir activamente** los términos clave correctos dentro de un texto con sentido, evidenciando que comprende los conceptos y los aplica en su contexto real (no solo reconocerlos en una lista).

---

## 1. Identificación

| Campo | Valor |
|---|---|
| Código OA | OA-03 |
| Título | Conceptos Clave de Sostenibilidad |
| Tipo H5P | H5P.Blanks 1.14 (Fill in the Blanks / Rellenar huecos) |
| Curso destino | Sostenibilidad |
| Versión | 1.0.0 |
| Autor | Jaber Al Abbadi — Becario H5P |
| Revisor | Diseñador Instruccional — pendiente de validación |
| Fecha | 2026-06 |
| Estado | ✅ Probado en h5p.org · ⏳ Pendiente validación en Moodle |
| Archivo H5P | `OA-03_AHC_H5P_FillBlanks_ConceptosSostenibilidad_Basico_Sostenibilidad_v1.0.0.h5p` |

---

## 2. Diseño pedagógico

| Campo | Valor |
|---|---|
| Público objetivo | Ciudadanía (público general adulto, sin conocimientos técnicos previos) |
| Objetivo de aprendizaje | Comprender y aplicar el vocabulario básico de sostenibilidad climática completando correctamente los términos clave en un texto. |
| Competencia | Alfabetización ambiental / sostenibilidad: manejo del vocabulario esencial sobre clima y huella de carbono. |
| Verbo observable (Bloom) | Comprender / Aplicar |
| Evidencia observable | Completa correctamente los 3 términos clave (carbono, invernadero, neutralidad) en el texto. |
| Duración estimada | 3-5 min |
| Prerequisitos | Ninguno. Lectura comprensiva básica en español. |
| Momento de uso | Inicio o cierre (activación de conocimientos previos o consolidación de vocabulario). |

---

## 3. Contenido

| Campo | Valor |
|---|---|
| Tema | Sostenibilidad (huella de carbono y neutralidad climática) |
| Mensaje clave | La huella de carbono mide las emisiones de gases de efecto invernadero, y la meta global es alcanzar la neutralidad climática para proteger el planeta. |
| Pantallas / Preguntas | **1 actividad** de tipo rellenar huecos con **1 párrafo** y **3 huecos** (no contiene tarjetas, hotspots ni imágenes). Instrucción mostrada: *"Rellena los espacios en blanco con la palabra correcta."* Texto real: *"La huella de \_\_\_ mide las emisiones de gases de efecto \_\_\_. El objetivo global es alcanzar la \_\_\_ climática para proteger el planeta."* |
| Respuestas correctas | Hueco 1 = **carbono** · Hueco 2 = **invernadero** · Hueco 3 = **neutralidad** |
| Feedback | Sin retroalimentación específica por hueco ni por rango definida en el paquete. Solo rango global de feedback general 0–100 (sin texto personalizado). Mensajes de sistema por defecto: *"':ans' is correct" / "':ans' is wrong"*. |
| Fuentes | Contenido conceptual propio de la AHC sobre vocabulario climático básico. Sin citas externas en el paquete. |
| Licencia | Creative Commons CC BY-NC-SA 4.0 *(licencia institucional asignada; nota: el metadato `license` del paquete H5P figura actualmente como `"U"` / sin declarar y debe actualizarse a CC BY-NC-SA 4.0 en una próxima edición).* |

---

## 4. Configuración H5P

| Campo | Valor |
|---|---|
| Ajustes de comportamiento | Botón "Comprobar" activo (`enableCheckButton: true`); botón "Mostrar solución" activo (`enableSolutionsButton: true`); autocomprobación desactivada (`autoCheck: false`); distingue mayúsculas/minúsculas (`caseSensitive: true`); no acepta errores ortográficos (`acceptSpellingErrors: false`); ver solución requiere haber rellenado los huecos (`showSolutionsRequiresInput: true`); huecos en línea, no en líneas separadas (`separateLines: false`); sin diálogos de confirmación (`confirmCheck`/`confirmRetry: false`). |
| Reintentos | Permitidos (`enableRetry: true`). |
| Puntuación | 1 punto por hueco → **máximo 3 puntos**. Barra de puntuación: "You got :num out of :total points". |
| Aleatorización | No (orden fijo; un único párrafo). |
| Condiciones de finalización | Se considera completado al pulsar "Comprobar" y enviar las respuestas. |
| Compatibilidad móvil | Sí (responsive, embebido vía iframe). |

---

## 5. Accesibilidad

| Campo | Valor |
|---|---|
| ALT en imágenes | N/A — el OA no contiene imágenes. |
| Subtítulos (VTT) | N/A — no contiene vídeo. |
| Transcripción | N/A — no contiene audio/vídeo. |
| Contraste alto | Sí — usa el tema visual estándar de H5P (texto oscuro sobre fondo claro). |
| No depender solo del color | Sí — la corrección se indica con iconos y etiquetas de texto ("correct"/"wrong"), no solo con color. |
| Lectura fácil | Frases cortas, vocabulario básico y directo, adecuado a público de Ciudadanía. |
| Operable por teclado | Sí — campos de entrada y botones navegables y activables por teclado; etiquetas a11y definidas (`inputLabel`, `a11yCheck`, `a11yShowSolution`, `a11yRetry`). |
| Carga cognitiva baja | Sí — una sola pantalla, 3 huecos, sin distractores ni temporizador. |

---

## 6. Moodle

| Campo | Valor |
|---|---|
| Curso | Sostenibilidad |
| Sección | Conceptos clave / vocabulario básico |
| Enlace | Pendiente de publicación |
| Visibilidad | Visible para estudiantes una vez publicado |
| Calificación | Sí — actividad calificable (máx. 3 puntos); puede registrarse en el libro de calificaciones vía xAPI/grade passback. |
| Finalización | Condición: ver/intentar la actividad y enviar respuestas. |
| Banco de contenido | Almacenar el `.h5p` en el Banco de contenido del curso para reutilización. |
| Etiquetas / Tags | sostenibilidad, básico, huella-de-carbono, vocabulario, fill-in-the-blanks, ciudadanía, OA-03 |

---

## 7. Reutilización

| Campo | Valor |
|---|---|
| Qué se puede adaptar | Texto de la instrucción, redacción del párrafo, idioma de la interfaz, mensajes de feedback (añadir rangos), tips por hueco, etiquetas de Moodle. |
| Qué NO debe cambiarse | Los 3 términos clave evaluados (**carbono, invernadero, neutralidad**) ni la relación verbo–formato (Comprender/Aplicar con rellenar huecos), para no romper la evidencia del OA. |
| Variables / parámetros del OA | N.º de huecos = 3; puntuación máx. = 3; `caseSensitive = true`; `acceptSpellingErrors = false`; reintentos = sí. |
| Cursos compatibles | Cualquier curso introductorio de Sostenibilidad, Medio Ambiente o Cambio Climático dirigido a público general. |

---

## 8. QA y mejora

**Checklist (verificados):**
- [x] Contenido real extraído de `content.json` (1 párrafo, 3 huecos).
- [x] Respuestas correctas confirmadas: carbono / invernadero / neutralidad.
- [x] Coherencia verbo–formato verificada (Comprender/Aplicar ↔ Fill in the Blanks).
- [x] Reintentos y botón solución activos.
- [x] Compatibilidad móvil (iframe responsive).
- [x] Operable por teclado y etiquetas a11y presentes.
- [ ] Licencia del paquete actualizada a CC BY-NC-SA 4.0 (actualmente `"U"` en el metadato — **incidencia abierta**).
- [ ] Validación final del Diseñador Instruccional.
- [ ] Feedback por rango con texto personalizado (mejora opcional).

**Incidencias:**
- El metadato `license` del `h5p.json` figura como `"U"` (sin declarar); debe fijarse a CC BY-NC-SA 4.0.
- `caseSensitive: true` + `acceptSpellingErrors: false` pueden penalizar mayúsculas/tildes; revisar si conviene relajarlo para público de Ciudadanía.
- No hay feedback formativo personalizado por rango ni tips por hueco (oportunidad de mejora).

**Métricas posteriores (pendientes de uso real en Moodle):** tasa de finalización, puntuación media, n.º medio de reintentos, % de aciertos por hueco.

**Decisiones de versión:**
- **v1.0.0** — versión inicial del OA, validada para Moodle.
- Criterio de versionado (SemVer): **MAJOR** = cambio que altera la evidencia o los términos evaluados; **MINOR** = añadir feedback/tips o nuevos huecos sin romper la evidencia; **PATCH** = correcciones menores (ortografía, metadato de licencia, etiquetas).
