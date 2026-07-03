# Ficha documental — OA-04: Emisiones ocultas en el hogar

> **Coherencia verbo-formato (obligatoria):** El tipo H5P.ImageHotspots es un formato exploratorio que muestra puntos interactivos sobre una imagen; el alumno debe abrir cada hotspot para revelar la información, de modo que la acción de explorar e identificar los focos de emisión es exactamente lo que el formato permite recoger como evidencia observable del verbo "Explorar / Identificar". (Nota: ImageHotspots no genera puntuación, la evidencia es de interacción/exploración, no calificable.)

---

## 1. Identificación

| Campo | Valor |
|---|---|
| Código OA | OA-04 |
| Título | Emisiones ocultas en el hogar |
| Tipo H5P | H5P.ImageHotspots (Image Hotspots) v1.10 |
| Curso destino | Huella de Carbono Personal |
| Versión | 1.0.0 |
| Autor | Jaber Al Abbadi — Becario H5P |
| Revisor | Diseñador Instruccional — pendiente de validación |
| Fecha | 2026-06 |
| Estado | ✅ Probado en h5p.org · ⏳ Pendiente validación en Moodle |
| Archivo H5P | `OA-04_AHC_H5P_ImageHotspots_EmisionesHogar_Intermedio_HuellaPersonal_v1.0.0.h5p` |

---

## 2. Diseño pedagógico

| Campo | Valor |
|---|---|
| Público objetivo | Ciudadanía (general, sin conocimientos técnicos previos) |
| Objetivo de aprendizaje | Explorar e identificar los principales puntos de consumo energético y emisión de CO2 dentro de una vivienda. |
| Competencia | Conciencia y acción frente al cambio climático en el ámbito doméstico. |
| Verbo observable (Bloom) | Explorar / Identificar (nivel: Recordar–Comprender). |
| Evidencia observable | Explora todos los puntos de emisión de CO2 de la vivienda (abre los 5 hotspots del plano del hogar). |
| Duración estimada | 3–5 min (rango 3–10 min). |
| Prerequisitos | Ninguno. Conviene haber visto la introducción al concepto de huella de carbono personal. |
| Momento de uso | Inicio / desarrollo: activación y sensibilización antes de profundizar en cálculo de huella. |

---

## 3. Contenido

| Campo | Valor |
|---|---|
| Tema | Huella de carbono personal |
| Mensaje clave | El hogar tiene varios focos de consumo energético "ocultos" que generan emisiones de CO2, y pequeños cambios de hábito reducen ese consumo de forma notable. |
| Pantallas/Preguntas | Una sola imagen interactiva: plano de una vivienda (imagen 768×768 px) con **5 hotspots** (icono "+" verde #7fd54b). No hay preguntas ni evaluación; cada punto despliega un texto informativo (H5P.Text). Los 5 puntos son: 1) Nevera y Congelador, 2) Aire Acondicionado, 3) Consumo Vampiro, 4) Iluminación LED, 5) Lavadora Eficiente. |
| Respuestas correctas | No aplica (contenido exploratorio sin respuestas evaluables). El "contenido revelado" de cada hotspot es: **Nevera y Congelador** — "Los frigoríficos antiguos consumen el doble. Usa modelos eficientes."; **Aire Acondicionado** — "Bajar la temperatura de 24°C aumenta el consumo un 8%."; **Consumo Vampiro** — "Los aparatos en modo espera consumen un 10% inútilmente."; **Iluminación LED** — "Las luces LED ahorran hasta un 80% de electricidad."; **Lavadora Eficiente** — "Lava a 30°C; calentar agua consume el 90% de la energía." |
| Feedback | No hay feedback de acierto/error (formato no evaluable). El feedback es informativo: el texto que aparece al abrir cada hotspot. |
| Fuentes | Datos de eficiencia energética doméstica de referencia general (IDAE / buenas prácticas de ahorro energético en el hogar). Pendiente de citar fuente concreta por el equipo DI. |
| Licencia | Creative Commons CC BY-NC-SA 4.0. (Nota: el paquete declara internamente license "U"; debe actualizarse a CC BY-NC-SA 4.0 antes de publicación.) |

---

## 4. Configuración H5P

| Campo | Valor |
|---|---|
| Ajustes de comportamiento | Icono de hotspot: "+" (plus), color #7fd54b. Cada punto abre una ventana emergente con texto. `alwaysFullscreen` = false en los 5 hotspots. |
| Reintentos | No aplica: el contenido es libremente reabrible; los hotspots se pueden abrir y cerrar sin límite. |
| Puntuación | No aplica (ImageHotspots no genera puntuación ni xAPI scoring). |
| Aleatorización | No (los 5 puntos están fijados por coordenadas sobre el plano). |
| Condiciones de finalización | El tipo no emite evento de finalización automático; en Moodle la finalización se basa en "ver/visualizar". |
| Compatibilidad móvil | Sí (responsive; los hotspots se adaptan a pantalla táctil). |

---

## 5. Accesibilidad

| Campo | Valor |
|---|---|
| ALT en imágenes | Sí. Texto alternativo de la imagen de fondo: "Plano del hogar". |
| Subtítulos (VTT) | N/A (no contiene vídeo). |
| Transcripción | N/A (no contiene audio ni vídeo). El contenido ya es textual y legible. |
| Contraste alto | A revisar: el icono verde #7fd54b sobre el plano debe verificarse contra fondo para contraste suficiente del marcador. |
| No depender solo del color | Cumple: los puntos usan icono "+" y numeración ("Hotspot #num"), no solo color. |
| Lectura fácil | Sí: textos breves, frases simples y dato concreto por punto. |
| Operable por teclado | Parcial: los hotspots son focusables/activables; verificar navegación completa con tabulador y cierre con teclado. |
| Carga cognitiva baja | Sí: 5 puntos, un dato por punto, sin evaluación ni presión de tiempo. |

---

## 6. Moodle

| Campo | Valor |
|---|---|
| Curso | Huella de Carbono Personal |
| Sección | Módulo de hogar / consumo energético doméstico (inicio del curso). |
| Enlace | Pendiente de publicación. |
| Visibilidad | Visible para estudiantes una vez publicado. |
| Calificación | No (actividad no calificable; formato exploratorio sin puntuación). |
| Finalización | Por visualización ("el estudiante debe ver la actividad"); no hay condición de nota. |
| Banco de contenido | Sí: alojar el .h5p en el Banco de contenido de Moodle para reutilización. |
| Etiquetas/Tags | huella-de-carbono, hogar, consumo-energético, CO2, eficiencia, ciudadanía, image-hotspots, OA-04. |

---

## 7. Reutilización

| Campo | Valor |
|---|---|
| Qué se puede adaptar | Los textos de cada hotspot, la imagen de fondo (otro plano/vivienda), el número y posición de puntos, el idioma y las etiquetas de interfaz. |
| Qué NO debe cambiarse | El código OA-04, el objetivo de exploración/identificación y la coherencia verbo-formato (debe seguir siendo un formato exploratorio). No convertir en cuestionario calificable sin reasignar verbo Bloom. |
| Variables/parámetros del OA | 5 hotspots (`position x/y`), icono "+" (#7fd54b), imagen 768×768, ALT "Plano del hogar", subcontenidos H5P.Text por punto. |
| Cursos compatibles | Huella de Carbono Personal y cualquier curso de sensibilización ambiental, eficiencia energética doméstica o consumo responsable dirigido a ciudadanía. |

---

## 8. QA y mejora

**Checklist**

- [x] Contenido real verificado contra `content.json` (5 hotspots, textos exactos).
- [x] Tipo H5P confirmado: H5P.ImageHotspots 1.10.
- [x] Coherencia verbo-formato confirmada (Explorar/Identificar ↔ exploración de hotspots).
- [x] Imagen con texto ALT ("Plano del hogar").
- [x] Compatibilidad móvil.
- [ ] Licencia interna actualizada a CC BY-NC-SA 4.0 (actualmente "U" en el paquete).
- [ ] Verificación de contraste del marcador y navegación completa por teclado.
- [ ] Cita de fuente concreta de los datos de eficiencia.
- [ ] Validación final del Diseñador Instruccional.

**Incidencias**

- La licencia declarada en `h5p.json`/`content.json` es "U" (sin especificar); debe corregirse a CC BY-NC-SA 4.0 antes de publicar.
- Falta fuente bibliográfica explícita de los porcentajes citados.

**Métricas posteriores**

- Pendientes de uso real en Moodle: nº de aperturas de la actividad, % de hotspots abiertos por sesión, tiempo medio de interacción, finalización por visualización.

**Decisiones de versión**

- v1.0.0: versión inicial publicable.
- Criterio SemVer: **MAJOR** = cambio de tipo H5P, objetivo o verbo Bloom; **MINOR** = añadir/quitar hotspots o nuevos contenidos sin romper el objetivo; **PATCH** = correcciones de texto, ALT, licencia o ajustes de accesibilidad.
