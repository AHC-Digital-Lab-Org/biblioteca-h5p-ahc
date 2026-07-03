# Ficha documental — OA-02: Alcances de Emisiones (Alcance 1, 2 y 3)

> **Coherencia verbo-formato (obligatoria):** El tipo H5P **Drag and Drop (H5P.DragQuestion)** permite recoger la evidencia del verbo **Clasificar**, porque el estudiante debe arrastrar cada fuente de emisión a la zona del alcance que le corresponde, acción que es una clasificación observable y puntuable.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| Código OA | OA-02 |
| Título | Alcances de Emisiones (Alcance 1, 2 y 3) |
| Tipo H5P | Drag and Drop — H5P.DragQuestion (v1.14) |
| Curso destino | Huella de Carbono Organización |
| Versión | 1.0.0 |
| Autor | Jaber Al Abbadi — Becario H5P |
| Revisor | Diseñador Instruccional — pendiente de validación |
| Fecha | 2026-06 |
| Estado | ✅ Probado en h5p.org · ⏳ Pendiente validación en Moodle |
| Archivo H5P | `OA-02_AHC_H5P_DragDrop_AlcancesEmisiones_Intermedio_MedicionEmisiones_v1.0.0.h5p` |

---

## 2. Diseño pedagógico

| Campo | Valor |
|---|---|
| Público objetivo | Empresas y voluntariado |
| Objetivo de aprendizaje | Clasificar las fuentes de emisión de gases de efecto invernadero (GEI) de una organización en su alcance correspondiente (1, 2 o 3). |
| Competencia | Distinguir entre emisiones directas (Alcance 1), indirectas por energía comprada (Alcance 2) e indirectas de la cadena de valor (Alcance 3) según el marco del GHG Protocol. |
| Verbo observable (Bloom) | Clasificar (nivel: Comprender/Aplicar) |
| Evidencia observable | Clasifica correctamente cada una de las 6 fuentes de emisión en su alcance (1, 2 o 3) arrastrándola a la zona correcta. |
| Duración estimada | 5–7 minutos (rango 3–10 min) |
| Prerequisitos | Conocer el concepto de huella de carbono de organización y la definición básica de Alcance 1, 2 y 3 (GHG Protocol). |
| Momento de uso | Desarrollo (práctica/refuerzo) o cierre (evaluación formativa). |

---

## 3. Contenido

| Campo | Valor |
|---|---|
| Tema | Medición y reducción de emisiones |
| Mensaje clave | Cada fuente de emisión pertenece a un único alcance (1 = directas; 2 = energía comprada; 3 = indirectas de la cadena de valor); clasificarlas correctamente es la base de todo inventario de huella de carbono. |
| Pantallas/Preguntas | **1 actividad de arrastrar y soltar** (una sola pantalla) sobre una imagen de fondo. Contiene **6 tarjetas arrastrables** (fuentes de emisión) y **3 zonas de destino** (Alcance 1, Alcance 2, Alcance 3). El alumno arrastra cada tarjeta a la zona del alcance correcto. |
| Respuestas correctas | **Alcance 1 (directas):** "Vehículos de la empresa (combustión)" y "Gas natural para la calefacción del edificio". · **Alcance 2 (energía comprada):** "Factura de electricidad de la sede central". · **Alcance 3 (cadena de valor):** "Vuelos de negocios de empleados", "Residuos de papel y plástico de la oficina" y "Compra de ordenadores nuevos para el personal". |
| Feedback | Marcado automático correcto/incorrecto por elemento, con puntos visibles (+1 / −1) y explicación de puntuación: *"Correct answers give +1 point. Incorrect answers give −1 point. The lowest possible score is 0."* No hay feedback textual personalizado ni pistas (tips) por zona. |
| Fuentes | El paquete no cita fuentes explícitas; el marco de referencia implícito es el **GHG Protocol Corporate Standard** (definición de Alcances 1, 2 y 3). |
| Licencia | Creative Commons CC BY-NC-SA 4.0 (asignada por AHC). *Nota: el metadato de licencia del paquete está como "U" / sin definir; debe alinearse — ver Incidencias.* |

---

## 4. Configuración H5P

| Campo | Valor |
|---|---|
| Ajustes de comportamiento | `dropZoneHighlighting: "dragging"` (resalta zonas al arrastrar), `showScorePoints: true`, `showTitle: true`, `enableScoreExplanation: true`, `enableCheckButton: true`, `enableFullScreen: false`, `autoAlignSpacing: 2`. |
| Reintentos | Sí (`enableRetry: true`) — botón "Retry" disponible. |
| Puntuación | Por elemento (`singlePoint: false`); penaliza errores (`applyPenalties: true`, −1 por fallo); puntuación máxima = 6 puntos; mínima posible = 0. |
| Aleatorización | No. H5P.DragQuestion no aleatoriza el orden de tarjetas/zonas y no hay parámetro de randomización en el contenido. |
| Condiciones de finalización | Se completa al pulsar "Check" (comprobar) y registrar la puntuación del intento. |
| Compatibilidad móvil | Sí (H5P responsivo, soporte táctil para arrastrar). |

---

## 5. Accesibilidad

| Campo | Valor |
|---|---|
| ALT en imágenes | Pendiente: la imagen de fondo (`image-PEhsrZKY.png`) no tiene texto alternativo declarado — ver Incidencias. |
| Subtítulos (VTT) | N/A (la actividad no incluye vídeo). |
| Transcripción | N/A (no incluye audio ni vídeo). |
| Contraste alto | A revisar: las tarjetas de texto se muestran sobre una imagen de fondo; verificar el contraste del texto sobre la imagen. |
| No depender solo del color | Cumple: las zonas se distinguen por etiqueta de texto ("Alcance 1", "Alcance 2", "Alcance 3"), no solo por color. |
| Lectura fácil | Cumple: enunciados de las tarjetas breves y concretos. |
| Operable por teclado | Sí: H5P.DragQuestion v1.14 admite navegación y arrastre por teclado con instrucciones a11y (grabbable/dropzone). |
| Carga cognitiva baja | Moderada-baja: 6 ítems distribuidos en 3 categorías claras. |

---

## 6. Moodle

| Campo | Valor |
|---|---|
| Curso | Huella de Carbono Organización |
| Sección | Medición y reducción de emisiones (módulo "Alcances de emisiones") |
| Enlace | Pendiente de publicación |
| Visibilidad | Visible para el alumnado tras la publicación |
| Calificación | Sí — actividad puntuable (máx. 6 puntos); reporta puntuación vía H5P/xAPI. |
| Finalización | Condición: alcanzar la puntuación de aprobación o completar el intento (comprobar respuestas). |
| Banco de contenido | Sí — alojar el archivo `.h5p` en el Banco de contenido de Moodle para su reutilización. |
| Etiquetas/Tags | huella-carbono, alcances, GEI, GHG-protocol, drag-and-drop, intermedio, OA-02 |

---

## 7. Reutilización

| Campo | Valor |
|---|---|
| Qué se puede adaptar | Los textos de las tarjetas (otras fuentes de emisión), la imagen de fondo, el número de tarjetas, los textos de feedback/pistas y el idioma de la interfaz. |
| Qué NO debe cambiarse | Las tres categorías (Alcance 1 / 2 / 3) ni el mapeo correcto tarjeta→alcance (definen la validez pedagógica); el verbo "Clasificar"; la licencia asignada. |
| Variables/parámetros del OA | 6 elementos arrastrables, 3 zonas de destino, mapeo `correctElements` por zona, penalización (`applyPenalties`), puntuación por elemento (`singlePoint`), imagen de fondo. |
| Cursos compatibles | Cualquier formación de huella de carbono organizacional, sostenibilidad empresarial o gestión ambiental que cubra el marco de alcances del GHG Protocol. |

---

## 8. QA y mejora

**Checklist (verificado contra `content.json` / `h5p.json`):**

- [x] Tipo H5P correcto: H5P.DragQuestion (Drag and Drop) — confirmado en `h5p.json`.
- [x] 6 tarjetas arrastrables y 3 zonas de destino presentes — confirmado.
- [x] Mapeo correcto definido por zona (`correctElements`) — confirmado.
- [x] Reintentos habilitados (`enableRetry: true`).
- [x] Penalización por error configurada (`applyPenalties: true`).
- [x] Las zonas se distinguen por texto, no solo por color.
- [x] Compatibilidad móvil (H5P responsivo).
- [ ] Texto alternativo (ALT) de la imagen de fondo — ausente.
- [ ] Idioma de la interfaz en español — botones en inglés (Check/Retry/Submit).
- [ ] Metadato de licencia del paquete definido — actualmente "U" (sin definir).
- [ ] Feedback textual personalizado / pistas por zona — ausente.
- [ ] Revisión por Diseñador Instruccional — pendiente.

**Incidencias:**
1. El metadato de licencia del paquete está como "U" (sin definir); debe alinearse con CC BY-NC-SA 4.0.
2. La interfaz/botones aparecen en inglés (Check, Retry, Submit) y `defaultLanguage` es "en", mientras el contenido está en español: conviene traducir la UI.
3. La imagen de fondo no tiene texto alternativo (ALT) declarado.
4. No hay feedback textual personalizado ni pistas por zona (solo marcado automático y explicación de puntuación).
5. El título visible coincide con el nombre de archivo (`OA-02_Alcances_Emisiones.h5p`); conviene un título legible para el alumnado.

**Métricas posteriores (pendientes de uso real en Moodle):** nº de intentos, % de acierto por alcance, tiempo medio de resolución y tasa de finalización.

**Decisiones de versión:**
- **v1.0.0** — versión inicial.
- Criterio semántico: **MAJOR** = cambio que rompe la equivalencia pedagógica (modificar categorías o mapeo correcto, cambiar el tipo H5P o el objetivo). **MINOR** = añadir tarjetas/zonas o feedback sin alterar el OA. **PATCH** = correcciones menores (erratas, ALT, idioma de la UI, metadato de licencia).
