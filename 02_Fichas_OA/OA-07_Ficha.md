# Ficha documental — OA-07: Identificación de energías renovables

> **Coherencia verbo–formato (obligatoria):** El tipo *Find the Hotspot* (`H5P.ImageHotspotQuestion`) **sí permite recoger la evidencia del verbo "Identificar"**, porque exige al usuario localizar y señalar mediante clic las zonas correctas de la imagen, acción observable y evaluable que constituye en sí misma una identificación.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| Código OA | OA-07 |
| Título | Identificación de energías renovables |
| Tipo H5P | Find the Hotspot (`H5P.ImageHotspotQuestion` v1.8) |
| Curso destino | Energía Sostenible |
| Versión | 1.0.0 |
| Autor | Jaber Al Abbadi — Becario H5P |
| Revisor | Diseñador Instruccional — pendiente de validación |
| Fecha | 2026-06 |
| Estado | ✅ Probado en h5p.org · ⏳ Pendiente validación en Moodle |
| Archivo H5P | `OA-07_AHC_H5P_FindHotspot_EnergiasRenovables_Intermedio_EnergiaSostenible_v1.0.0.h5p` |

---

## 2. Diseño pedagógico

| Campo | Valor |
|---|---|
| Público objetivo | Ciudadanía |
| Objetivo de aprendizaje | Identificar las fuentes de energía renovable representadas en una imagen, distinguiéndolas de las fuentes no renovables. |
| Competencia | Competencia ciudadana en sostenibilidad ambiental (transición energética y reducción de la huella de carbono). |
| Verbo observable (Bloom) | Identificar (nivel: Recordar/Comprender). |
| Evidencia observable | Localiza y hace clic sobre las fuentes de energía renovable correctas en la imagen. |
| Duración estimada | 3–5 min |
| Prerequisitos | Noción básica de qué es una fuente de energía; lectura del concepto "renovable vs. no renovable". |
| Momento de uso | Inicio / desarrollo (activación o comprobación de conocimientos previos). |

---

## 3. Contenido

| Campo | Valor |
|---|---|
| Tema | Energía sostenible |
| Mensaje clave | Las fuentes de energía renovable son clave para reducir nuestra huella de carbono; saber identificarlas es el primer paso hacia un consumo sostenible. |
| Pantallas/Preguntas | **1 pantalla / 1 pregunta** con imagen de fondo (`images/image-d4h68Cxv.png`, PNG, 1536×1024 px) y **5 zonas interactivas (hotspots) circulares**. Consigna real: *"Encuentra y haz clic en la fuente de energía renovable en esta imagen."* De las 5 zonas, **4 están marcadas como correctas** (fuentes renovables) y **1 como incorrecta** (distractor). |
| Respuestas correctas | Las **4 zonas circulares marcadas `correct=true`** sobre la imagen (las fuentes de energía renovable). La zona restante (`correct=false`) es el distractor que debe evitarse. |
| Feedback | Mostrado como **popup** (`showFeedbackAsPopup: true`). Texto de acierto: *"¡Excelente! Esta energía es clave para reducir nuestra huella de carbono."*, presente en 3 de las 4 zonas correctas. Incidencias detectadas: una zona correcta no tiene texto de feedback (vacío) y el distractor incorrecto reutiliza por error el mismo texto positivo (ver §8). |
| Fuentes | Imagen de fondo propia del paquete (`content/images/image-d4h68Cxv.png`). Sin fuentes externas citadas en el contenido. |
| Licencia | **Documental/intencional del OA: Creative Commons CC BY-NC-SA 4.0.** Atención: en los metadatos del paquete la licencia (`h5p.json`) y la de la imagen de fondo figuran como **"U" (Undisclosed/sin declarar)** — pendiente de asignar la licencia CC en H5P antes de publicar. |

---

## 4. Configuración H5P

| Campo | Valor |
|---|---|
| Ajustes de comportamiento | Feedback mostrado como ventana emergente (`showFeedbackAsPopup: true`); figuras de hotspot circulares. |
| Reintentos | Botón "Retry" disponible (cadena `l10n.retryText = "Retry"`); permite reintentar la tarea (reinicia respuestas). |
| Puntuación | Por zonas acertadas; barra de puntuación activa (`scoreBarLabel = "You got :num out of :total points"`). |
| Aleatorización | No aplica / no configurada (una sola imagen y conjunto fijo de hotspots). |
| Condiciones de finalización | Interacción completada al pulsar sobre una zona y recibir feedback; sin umbral de aprobado definido en el contenido. |
| Compatibilidad móvil | Sí (responsive; interacción por toque sobre la imagen). |

---

## 5. Accesibilidad

| Campo | Valor |
|---|---|
| ALT en imágenes | **Ausente** — la imagen de fondo no tiene texto alternativo en `content.json`. Pendiente de añadir ALT descriptivo (incidencia §8). |
| Subtítulos (VTT) | N/A — el OA no contiene vídeo. |
| Transcripción | N/A — el OA no contiene audio ni vídeo. |
| Contraste alto | Revisar contraste de los marcadores/hotspots sobre la imagen; recomendable verificar en validación DI. |
| No depender solo del color | Parcial — la identificación se basa en posición sobre la imagen; conviene reforzar con la consigna textual (ya presente). |
| Lectura fácil | Consigna breve y clara en español ("Encuentra y haz clic…"). Adecuada para Ciudadanía. |
| Operable por teclado | Limitado — `ImageHotspotQuestion` se opera principalmente con ratón/táctil; verificar navegación por teclado en validación. |
| Carga cognitiva baja | Sí — una sola pantalla, una tarea, instrucción única y directa. |

---

## 6. Moodle

| Campo | Valor |
|---|---|
| Curso | Energía Sostenible |
| Sección | Módulo de energías renovables (sección de identificación/diagnóstico inicial). |
| Enlace | Pendiente de publicación. |
| Visibilidad | Visible para estudiantes una vez publicado (oculto hasta validación DI). |
| Calificación | Sí — la actividad genera puntuación (por zonas correctas); configurable como formativa. |
| Finalización | Condición: el estudiante interactúa con la actividad y recibe feedback (ver/recibir intento). |
| Banco de contenido | Almacenar el `.h5p` en el Banco de contenido del curso para reutilización. |
| Etiquetas/Tags | energía renovable; sostenibilidad; huella de carbono; find-the-hotspot; OA-07; ciudadanía; intermedio. |

---

## 7. Reutilización

| Campo | Valor |
|---|---|
| Qué se puede adaptar | Imagen de fondo, posición/tamaño de los hotspots, textos de feedback, consigna (`taskDescription`) y traducción de cadenas de UI. |
| Qué NO debe cambiarse | El verbo/objetivo (Identificar fuentes renovables) ni el formato Find the Hotspot, para mantener la coherencia verbo–formato y la evidencia. |
| Variables/parámetros del OA | Nº de hotspots correctos/incorrectos, figura (círculo), `showFeedbackAsPopup`, texto de cada feedback, ALT de la imagen, licencia. |
| Cursos compatibles | Cualquier curso de sostenibilidad/medio ambiente que requiera reconocer visualmente fuentes de energía (Energía Sostenible y afines). |

---

## 8. QA y mejora

**Checklist de verificación**

- [x] Tipo H5P confirmado: `H5P.ImageHotspotQuestion` v1.8 (Find the Hotspot).
- [x] Coherencia verbo–formato (Identificar ↔ localizar/clic en imagen) verificada.
- [x] Consigna en español, clara y breve.
- [x] Contenido real extraído de `content.json` (1 imagen, 5 hotspots: 4 correctos + 1 distractor).
- [x] Compatibilidad móvil.
- [ ] ALT de imagen de fondo presente. **(Falta)**
- [ ] Licencia CC BY-NC-SA 4.0 declarada en metadatos H5P (actualmente "U"). **(Falta)**
- [ ] Feedback coherente en todas las zonas (1 zona correcta sin feedback; distractor con feedback positivo erróneo). **(Falta)**
- [ ] Cadenas de interfaz traducidas al español ("Retry", "Close", barra de puntuación en inglés). **(Falta)**
- [ ] Operabilidad por teclado y contraste verificados por DI. **(Pendiente)**

**Incidencias**

1. La imagen de fondo carece de texto alternativo (ALT) — barrera de accesibilidad.
2. Licencia del paquete y de la imagen sin declarar ("U") pese a que la licencia documental es CC BY-NC-SA 4.0.
3. La zona `correct=true` nº 3 tiene el campo de feedback vacío.
4. El distractor (`correct=false`) muestra el mismo feedback positivo ("¡Excelente!…") que las zonas correctas: confunde la corrección.
5. Cadenas de UI en inglés ("Retry", "Close", "You got :num out of :total points") sin localizar al español.

**Métricas posteriores:** pendientes de uso real en Moodle (nº de intentos, % de aciertos, tasa de clic en el distractor, tiempo medio).

**Decisiones de versión:** v1.0.0 inicial. Criterio SemVer — **MAJOR:** cambio de tipo H5P, objetivo o evidencia; **MINOR:** añadir/quitar hotspots o nueva imagen manteniendo el objetivo; **PATCH:** correcciones sin cambio funcional (ALT, licencia, feedback faltante, traducción de UI → previsto **v1.0.1** al resolver las incidencias 1–5).
