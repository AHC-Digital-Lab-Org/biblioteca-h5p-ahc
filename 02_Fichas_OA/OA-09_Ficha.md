# Ficha documental — OA-09: Beneficios de la Acción Climática

> **Coherencia verbo-formato (obligatoria):** el tipo **H5P.Accordion (Accordion / Acordeón)** permite recoger la evidencia de los verbos **Consultar/Comprender**, ya que el estudiante despliega y lee paneles informativos, demostrando de forma observable que consulta y revisa los distintos beneficios de la acción climática; es un componente expositivo (sin autocalificación), idóneo para verbos de consulta y comprensión, no para verbos de aplicación o evaluación.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| Código OA | OA-09 |
| Título | Beneficios de la Acción Climática |
| Tipo H5P | H5P.Accordion 1.0 (Accordion / Acordeón) |
| Curso destino | Acción Climática |
| Versión | 1.0.0 |
| Autor | Jaber Al Abbadi — Becario H5P |
| Revisor | Diseñador Instruccional — pendiente de validación |
| Fecha | 2026-06 |
| Estado | ✅ Probado en h5p.org · ⏳ Pendiente validación en Moodle |
| Archivo H5P | `OA-09_AHC_H5P_Accordion_BeneficiosClima_Basico_AccionClimatica_v1.0.0.h5p` |

> Nota de trazabilidad: el título interno del paquete (`h5p.json`) es "OA-09: Beneficios de la Accion Climatica" (sin tildes). Librería principal declarada: `H5P.Accordion 1.0`; dependencia de contenido: `H5P.AdvancedText 1.1`.

---

## 2. Diseño pedagógico

| Campo | Valor |
|---|---|
| Público objetivo | Todos los perfiles (ciudadanía, empresas y administración); nivel básico, sin requisitos previos. |
| Objetivo de aprendizaje | Consultar y comprender los principales beneficios de la acción climática, agrupados en sus dimensiones ambiental, económica y de salud. |
| Competencia | Alfabetización climática: reconocer el valor y los beneficios multidimensionales de actuar frente al cambio climático. |
| Verbo observable (Bloom) | Consultar / Comprender |
| Evidencia observable | Consulta los paneles de beneficios de la acción climática (despliega los 3 acordeones: ambientales, económicos y de salud). |
| Duración estimada | 3–5 min |
| Prerequisitos | Ninguno; idea general de qué es el cambio climático (recomendable, no obligatorio). |
| Momento de uso | Inicio (motivación/sensibilización) o cierre (síntesis de beneficios). |

---

## 3. Contenido

| Campo | Valor |
|---|---|
| Tema | Acción climática |
| Mensaje clave | Actuar frente al cambio climático aporta beneficios concretos y simultáneos en tres planos: **ambiental** (biodiversidad y menos eventos extremos), **económico** (ahorro energético y empleo verde) y de **salud** (aire más limpio y menos enfermedades respiratorias). |
| Pantallas/Preguntas | 1 actividad de tipo Acordeón con **3 paneles desplegables** (encabezados `h2`), de contenido textual informativo (sin preguntas, hotspots ni huecos): **(1) Beneficios Ambientales** — "Protegemos la biodiversidad y reducimos la frecuencia de eventos climáticos extremos."; **(2) Beneficios Económicos** — "La eficiencia energética reduce las facturas de electricidad y fomenta el empleo verde."; **(3) Beneficios para la Salud** — "Menos emisiones significan un aire más limpio, reduciendo enfermedades respiratorias." |
| Respuestas correctas | N/A — el Acordeón es un componente expositivo: no plantea preguntas ni respuestas evaluables. |
| Feedback | N/A — sin autocalificación ni retroalimentación; la "respuesta" del usuario es la propia consulta (abrir/cerrar paneles). |
| Fuentes | Contenido didáctico propio de la AHC (síntesis estándar de los cobeneficios ambientales, económicos y sanitarios de la acción climática). |
| Licencia | Creative Commons CC BY-NC-SA 4.0 *(a registrar en metadatos: el `h5p.json` y cada panel declaran actualmente licencia "U" / sin especificar; pendiente de fijar a CC BY-NC-SA 4.0)*. |

**Contenido real de los paneles (texto íntegro extraído de `content.json`):**

1. **Beneficios Ambientales** — "Protegemos la biodiversidad y reducimos la frecuencia de eventos climáticos extremos."
2. **Beneficios Económicos** — "La eficiencia energética reduce las facturas de electricidad y fomenta el empleo verde." *(el título almacenado figura como "Title: Beneficios Económicos", con el prefijo "Title:" introducido por error — ver Incidencias)*.
3. **Beneficios para la Salud** — "Menos emisiones significan un aire más limpio, reduciendo enfermedades respiratorias."

---

## 4. Configuración H5P

| Campo | Valor |
|---|---|
| Ajustes de comportamiento | Acordeón estándar: cada panel se despliega/colapsa de forma independiente; encabezados de panel con etiqueta `h2` (`hTag: "h2"`). Sin botones de comprobar/reintentar (no aplica a este tipo). |
| Reintentos | N/A — no es una actividad evaluable; el usuario puede abrir y cerrar los paneles cuantas veces quiera. |
| Puntuación | No — el Acordeón no genera puntuación ni reporta `score` por xAPI más allá de la interacción de apertura. |
| Aleatorización | No — el orden de los 3 paneles es fijo (Ambientales → Económicos → Salud). |
| Condiciones de finalización | Acceso/visualización de la actividad (no hay envío ni calificación que comprobar). |
| Compatibilidad móvil | Sí (responsive; los paneles se despliegan con toque táctil). |

---

## 5. Accesibilidad

| Campo | Valor |
|---|---|
| ALT en imágenes | N/A — la actividad es solo texto, sin imágenes ni medios. |
| Subtítulos (VTT) | N/A — sin vídeo. |
| Transcripción | N/A — sin audio/vídeo. |
| Contraste alto | Sí — usa los estilos por defecto de H5P, con contraste adecuado texto/fondo. |
| No depender solo del color | Sí — la información se transmite por texto y encabezados; el estado abierto/cerrado se indica con icono además del color. |
| Lectura fácil | Sí — tres frases cortas, una por dimensión, con vocabulario claro y directo. |
| Operable por teclado | Sí — los encabezados del acordeón son focalizables y se abren/cierran con teclado, con roles/estados ARIA (expandido/contraído). |
| Carga cognitiva baja | Sí — solo 3 paneles, una idea por panel, sin elementos interactivos complejos. |

---

## 6. Moodle

| Campo | Valor |
|---|---|
| Curso | Acción Climática |
| Sección | Beneficios de la acción climática |
| Enlace | Pendiente de publicación |
| Visibilidad | Visible para estudiantes una vez publicado |
| Calificación | No — el Acordeón es informativo y no registra puntuación; no se califica. |
| Finalización | Condición: ver/acceder a la actividad (marca por visualización; sin nota mínima). |
| Banco de contenido | Almacenar el `.h5p` en el Banco de contenido del curso y enlazar la actividad. |
| Etiquetas/Tags | `acción-climática`, `beneficios`, `cobeneficios`, `biodiversidad`, `empleo-verde`, `salud`, `OA-09`, `Accordion`, `básico` |

---

## 7. Reutilización

| Campo | Valor |
|---|---|
| Qué se puede adaptar | El texto de cada panel, añadir o quitar paneles (p. ej. un cuarto panel "Beneficios Sociales"), los títulos de los encabezados y el nivel de encabezado (`hTag`). |
| Qué NO debe cambiarse | El propósito expositivo del OA (consultar/comprender) y la cobertura de las tres dimensiones de beneficio (ambiental, económica y de salud) como núcleo del mensaje. |
| Variables/parámetros del OA | `panels[]` (lista de paneles), `panels[].title` (encabezado), `panels[].content` (texto AdvancedText), `hTag` (nivel de encabezado de los paneles). |
| Cursos compatibles | Acción Climática; cualquier curso de sensibilización ambiental, sostenibilidad o salud ambiental dirigido a público general. |

---

## 8. QA y mejora

**Checklist de verificación**

- [x] El paquete abre y la actividad carga (3 paneles detectados).
- [x] Contenido real confirmado: Ambientales / Económicos / Salud, con su texto íntegro.
- [x] Encabezados de panel con etiqueta `h2` (estructura accesible).
- [x] Operable por teclado y compatible con móvil.
- [x] Sin dependencia exclusiva del color para el estado de los paneles.
- [x] Tipo coherente con el verbo (Consultar/Comprender → componente expositivo).
- [ ] Corregir el título del panel 2: "Title: Beneficios Económicos" → "Beneficios Económicos".
- [ ] Fijar metadatos de idioma a español (`language`/`defaultLanguage` figuran como "en").
- [ ] Metadatos de licencia fijados a CC BY-NC-SA 4.0 en el paquete y paneles (actualmente "U").
- [ ] Validación final del Diseñador Instruccional.
- [ ] Publicación y enlace en Moodle.

| Campo | Valor |
|---|---|
| Incidencias | (1) El título del segundo panel almacena el prefijo literal "Title: " ("Title: Beneficios Económicos"), error de entrada de datos a corregir. (2) `language` y `defaultLanguage` del `h5p.json` son "en" pese a que el contenido es español; conviene fijarlos a "es". (3) La licencia figura como "U" (sin especificar) en `h5p.json` y en cada panel; debe actualizarse a CC BY-NC-SA 4.0. |
| Métricas posteriores | Pendientes de uso real en Moodle: nº de aperturas por panel, % de usuarios que despliegan los 3 paneles, tiempo de permanencia, % de finalización por visualización. |
| Decisiones de versión | v1.0.0 inicial (publicación base). Criterio SemVer: **MAJOR** = cambio del objetivo/evidencia o del tipo de componente; **MINOR** = añadir/quitar paneles o ampliar contenido sin alterar el objetivo; **PATCH** = correcciones menores de texto, tildes, título del panel, idioma o licencia. |
