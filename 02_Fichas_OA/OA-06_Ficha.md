# Ficha documental — OA-06: Glosario Climático

> **Coherencia verbo-formato (obligatoria):** El tipo H5P *Dialog Cards* (tarjetas de anverso/reverso que el alumno gira) es idóneo para el verbo Bloom **"Recordar"**, porque permite recoger la evidencia de repaso y memorización: el alumno gira cada tarjeta para recuperar la definición del término, evidenciando que reconoce y recuerda el vocabulario climático básico.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| Código OA | OA-06 |
| Título | Glosario Climático |
| Tipo H5P | H5P.Dialogcards 1.9 (Dialog Cards / Tarjetas de diálogo) — modo `normal` |
| Curso destino | Huella de Carbono Personal |
| Versión | 1.0.0 |
| Autor | Jaber Al Abbadi — Becario H5P |
| Revisor | Diseñador Instruccional — pendiente de validación |
| Fecha | 2026-06 |
| Estado | ✅ Probado en h5p.org · ⏳ Pendiente validación en Moodle |
| Archivo H5P | `OA-06_AHC_H5P_DialogCards_GlosarioClimatico_Basico_HuellaCarbono_v1.0.0.h5p` |

---

## 2. Diseño pedagógico

| Campo | Valor |
|---|---|
| Público objetivo | Todos los perfiles |
| Objetivo de aprendizaje | Recordar las definiciones de los términos básicos del glosario climático (huella de carbono, GEI y neutralidad de carbono) asociados a la huella de carbono personal. |
| Competencia | Alfabetización climática básica: comprensión del vocabulario fundamental de sostenibilidad y emisiones. |
| Verbo observable (Bloom) | Recordar |
| Evidencia observable | Repasa las definiciones del glosario climático girando las 3 tarjetas (Huella de Carbono, GEI y Neutralidad de Carbono) y reconoce su significado. |
| Duración estimada | 3-5 min (dentro del rango 3-10 min) |
| Prerequisitos | Ninguno. Actividad introductoria de nivel básico. |
| Momento de uso | Inicio del curso (activación de vocabulario) o cierre como repaso de términos. |

---

## 3. Contenido

| Campo | Valor |
|---|---|
| Tema | Vocabulario climático |
| Mensaje clave | Tres términos básicos permiten entender la huella de carbono personal: qué es la huella de carbono, qué son los gases de efecto invernadero (GEI) y qué significa la neutralidad de carbono (Net Zero). |
| Pantallas/Preguntas | **3 tarjetas de diálogo** (flashcards), sin imágenes, audio ni vídeo, sin pistas (`tips` vacías). Cada tarjeta presenta un término en el anverso y su definición en el reverso. Descripción de la actividad: "Gira las tarjetas para aprender los términos clave." |
| Respuestas correctas (contenido real) | **T1 — Huella de Carbono:** "La cantidad total de gases de efecto invernadero emitidos directa o indirectamente por un individuo, organización o producto." · **T2 — Gases de Efecto Invernadero (GEI):** "Gases como el CO2 y el metano que atrapan el calor en la atmósfera, causando el calentamiento global." · **T3 — Neutralidad de Carbono (Net Zero):** "Estado en el que las emisiones de carbono liberadas a la atmósfera se equilibran con una cantidad equivalente retirada." |
| Feedback | No hay feedback por respuesta (modo `normal`): la actividad es autoformativa de repaso; el alumno autoevalúa su recuerdo al girar la tarjeta. No incluye pistas (`tips`). |
| Fuentes | Glosario interno AHC de vocabulario climático (definiciones divulgativas elaboradas por el equipo del curso Huella de Carbono Personal). |
| Licencia | Creative Commons CC BY-NC-SA 4.0 *(documentación AHC)*. **Aviso:** el campo `license` del paquete H5P está como `U` (Undisclosed/sin declarar) — corregir a CC BY-NC-SA 4.0 en metadatos antes de publicar. |

---

## 4. Configuración H5P

| Campo | Valor |
|---|---|
| Ajustes de comportamiento | Modo `normal`. Navegación hacia atrás habilitada (`disableBackwardsNavigation: false`). Texto NO escalado en lugar de la tarjeta (`scaleTextNotCard: false`). Progresión rápida desactivada (`quickProgression: false`). Dominio máximo (`maxProficiency: 5`, relevante solo en modo repetición). |
| Reintentos | Sí — botón "Retry" activado (`enableRetry: true`). El alumno puede reiniciar y volver a repasar las tarjetas. |
| Puntuación | No genera calificación numérica. En modo `normal`, Dialog Cards es una actividad de repaso no evaluable (no envía nota al libro de calificaciones; solo eventos xAPI de intento/finalización). |
| Aleatorización | No — orden fijo de tarjetas (`randomCards: false`). |
| Condiciones de finalización | Finaliza al haber visualizado/girado las 3 tarjetas. No hay umbral de aprobado (actividad formativa). |
| Compatibilidad móvil | Sí — diseño responsive; las tarjetas se giran por toque/clic. |

---

## 5. Accesibilidad

| Campo | Valor |
|---|---|
| ALT en imágenes | N/A — el contenido no incluye imágenes. |
| Subtítulos (VTT) | N/A — no hay vídeo. |
| Transcripción | N/A — no hay audio cargado en las tarjetas (la librería H5P.Audio es dependencia, pero no se usa). |
| Contraste alto | Sí — se usa el tema por defecto de H5P con texto sobre tarjeta; contraste suficiente. Verificar en Moodle el tema institucional. |
| No depender solo del color | Sí — la información se transmite por texto (término/definición), no por color. |
| Lectura fácil | Sí — definiciones breves, lenguaje divulgativo y frases de una sola idea. |
| Operable por teclado | Sí — Dialog Cards es navegable con teclado (Tab/Enter para girar y avanzar entre tarjetas). |
| Carga cognitiva baja | Sí — solo 3 tarjetas, una idea por tarjeta, sin distractores. |

---

## 6. Moodle

| Campo | Valor |
|---|---|
| Curso | Huella de Carbono Personal |
| Sección | Módulo introductorio — Vocabulario climático |
| Enlace | Pendiente de publicación |
| Visibilidad | Visible para todos los perfiles inscritos |
| Calificación | No — actividad formativa de repaso, sin nota (modo `normal`). |
| Finalización | Condición: ver/completar la actividad (las 3 tarjetas giradas). |
| Banco de contenido | Almacenar el .h5p en el Banco de contenido del curso para reutilización. |
| Etiquetas/Tags | huella-de-carbono, glosario, vocabulario-climatico, GEI, neutralidad-carbono, basico, dialog-cards, OA-06 |

---

## 7. Reutilización

| Campo | Valor |
|---|---|
| Qué se puede adaptar | Añadir nuevas tarjetas de términos al glosario; añadir imágenes ALT o audio a las tarjetas; activar modo repetición si se quiere seguimiento de dominio; traducir/ajustar las etiquetas de interfaz (botones); reordenar tarjetas. |
| Qué NO debe cambiarse | Las definiciones reales de los 3 términos núcleo (Huella de Carbono, GEI, Neutralidad de Carbono), el código OA-06 y el alineamiento con el verbo "Recordar". |
| Variables/parámetros del OA | `mode: normal`; `dialogs` (3 tarjetas texto/respuesta); `behaviour.enableRetry: true`; `randomCards: false`; `disableBackwardsNavigation: false`; `maxProficiency: 5`; `quickProgression: false`. |
| Cursos compatibles | Cualquier curso AHC introductorio de sostenibilidad/clima que requiera repaso de vocabulario base (huella de carbono, emisiones, neutralidad). |

---

## 8. QA y mejora

**Checklist de verificación**

- [x] Tipo H5P confirmado: H5P.Dialogcards 1.9, modo `normal`.
- [x] Nº de tarjetas verificado en `content.json`: 3.
- [x] Definiciones reales transcritas literalmente desde el paquete.
- [x] Coherencia verbo-formato confirmada (Recordar ↔ Dialog Cards).
- [x] Reintentos activados (`enableRetry: true`).
- [x] Sin imágenes/audio/vídeo → criterios de ALT/subtítulos/transcripción marcados N/A correctamente.
- [x] Compatibilidad móvil y operación por teclado verificadas a nivel de librería.
- [ ] Licencia del paquete corregida de `U` a CC BY-NC-SA 4.0 (pendiente).
- [ ] Idioma de la interfaz traducido al español (botones aún en inglés: "Turn/Next/Previous/Retry").
- [ ] Validación final del Diseñador Instruccional.
- [ ] Publicación y enlace en Moodle.

**Incidencias**

1. Metadatos: `license: "U"` en `h5p.json` — no coincide con la licencia documental CC BY-NC-SA 4.0; corregir antes de publicar.
2. Interfaz: `defaultLanguage`/`language` = `en`; las etiquetas de botones aparecen en inglés mientras el contenido está en español. Recomendado localizar al español para coherencia.
3. Título en metadatos sin tilde ("Glosario Climatico"); unificar con el título de la ficha ("Glosario Climático").

**Métricas posteriores** — Pendientes de uso real en Moodle: nº de intentos, tarjetas completadas, tiempo medio de repaso, eventos xAPI de finalización.

**Decisiones de versión** — v1.0.0 inicial (primera versión validada del OA). Criterio de versionado semántico: **MAJOR** = cambio de tipo H5P o de objetivo/verbo Bloom; **MINOR** = añadir/quitar tarjetas o funcionalidad manteniendo el objetivo; **PATCH** = correcciones menores (licencia, idioma de interfaz, tildes, ajustes de comportamiento sin alterar contenido).
