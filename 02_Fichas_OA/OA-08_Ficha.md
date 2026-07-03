# Ficha documental — OA-08: Estrategias de Acción Climática (Mitigación vs Adaptación)

> **Coherencia verbo-formato (obligatoria):** el tipo **H5P.DragText (Drag the Words)** permite recoger la evidencia de los verbos **Distinguir/Aplicar**, ya que el estudiante debe arrastrar y asignar cada término al hueco correcto, demostrando de forma observable y autocalificable que diferencia *mitigación* de *adaptación* y que aplica el concepto reconociendo un ejemplo concreto (energía solar = mitigación).

---

## 1. Identificación

| Campo | Valor |
|---|---|
| Código OA | OA-08 |
| Título | Estrategias de Acción Climática (Mitigación vs Adaptación) |
| Tipo H5P | H5P.DragText 1.10 (Drag the Words / Arrastrar las palabras) |
| Curso destino | Estrategia Climática |
| Versión | 1.0.0 |
| Autor | Jaber Al Abbadi — Becario H5P |
| Revisor | Diseñador Instruccional — pendiente de validación |
| Fecha | 2026-06 |
| Estado | ✅ Probado en h5p.org · ⏳ Pendiente validación en Moodle |
| Archivo H5P | `OA-08_AHC_H5P_DragText_MitigacionAdaptacion_Intermedio_EstrategiaClimatica_v1.0.0.h5p` |

> Nota de trazabilidad: el título interno del paquete (`h5p.json`) es "OA-08: Estrategias de Accion Climatica".

---

## 2. Diseño pedagógico

| Campo | Valor |
|---|---|
| Público objetivo | Ciudadanía y empresas (nivel intermedio) |
| Objetivo de aprendizaje | Distinguir las estrategias de mitigación frente a las de adaptación y aplicar el criterio para clasificar ejemplos reales de acción climática. |
| Competencia | Alfabetización climática: comprender y diferenciar las dos grandes respuestas al cambio climático (mitigación y adaptación). |
| Verbo observable (Bloom) | Aplicar / Distinguir |
| Evidencia observable | Completa el texto arrastrando los términos correctos a los 4 huecos, distinguiendo mitigación de adaptación. |
| Duración estimada | 3–5 min |
| Prerequisitos | Concepto básico de cambio climático y de gases de efecto invernadero (GEI). |
| Momento de uso | Desarrollo (consolidación conceptual) o cierre (comprobación rápida). |

---

## 3. Contenido

| Campo | Valor |
|---|---|
| Tema | Estrategia climática |
| Mensaje clave | La **mitigación** reduce las emisiones de GEI para frenar el cambio climático; la **adaptación** ajusta sistemas y estilos de vida para afrontar impactos ya inevitables. |
| Pantallas/Preguntas | 1 actividad (un único texto Drag the Words) con **4 huecos** que completar arrastrando palabras. Consigna real: "Arrastra las palabras a los espacios en blanco para completar las definiciones". Los huecos cubren: (1) definición de mitigación; (2) definición de adaptación; (3) ejemplo de mitigación (energía); (4) clasificación de una medida (muros contra inundaciones) como adaptación. |
| Respuestas correctas | Hueco 1 = **mitigación**; Hueco 2 = **adaptación**; Hueco 3 = **solar**; Hueco 4 = **adaptación**. |
| Feedback | Genérico del componente: "Correct!"/"Incorrect!" por hueco y barra de puntuación ("You got :num out of :total points"). Rango de retroalimentación global único 0–100 sin texto personalizado; sin pistas (tips) por hueco. |
| Fuentes | Contenido didáctico propio de la AHC (definiciones estándar de mitigación y adaptación al cambio climático). |
| Licencia | Creative Commons CC BY-NC-SA 4.0 *(a registrar en metadatos: el `h5p.json` del paquete declara actualmente licencia "U" / sin especificar; pendiente de fijar a CC BY-NC-SA 4.0)*. |

**Texto fuente real (con marcadores de hueco `*…*`):**
> "La *mitigación* se centra en reducir las emisiones de gases de efecto invernadero para evitar que el cambio climático empeore. Por otro lado, la *adaptación* busca ajustar nuestros sistemas y estilo de vida para enfrentar los impactos climáticos que ya son inevitables. Un ejemplo de mitigación es usar energía *solar*, mientras que construir muros contra inundaciones es una medida de *adaptación*."

---

## 4. Configuración H5P

| Campo | Valor |
|---|---|
| Ajustes de comportamiento | Botón "Comprobar" activado (`enableCheckButton: true`); feedback instantáneo desactivado (`instantFeedback: false`). |
| Reintentos | Sí, "Reintentar" activado (`enableRetry: true`). |
| Puntuación | Sí, automática: 1 punto por hueco correcto (4 huecos → 4 puntos máx.), barra de puntuación visible. |
| Aleatorización | No aplica para Drag the Words con texto fijo; el orden de las palabras arrastrables se baraja en la presentación. |
| Condiciones de finalización | Pulsar "Comprobar"; opcionalmente "Mostrar solución" disponible (`enableSolutionsButton: true`). |
| Compatibilidad móvil | Sí (responsive, arrastrar y soltar táctil). |

---

## 5. Accesibilidad

| Campo | Valor |
|---|---|
| ALT en imágenes | N/A — la actividad no incluye imágenes ni medios. |
| Subtítulos (VTT) | N/A — sin vídeo. |
| Transcripción | N/A — sin audio/vídeo. |
| Contraste alto | Sí — usa los estilos por defecto de H5P, con contraste adecuado texto/fondo. |
| No depender solo del color | Sí — la corrección se indica además con iconos y etiquetas ("Correct!"/"Incorrect!"), no solo con color. |
| Lectura fácil | Frases cortas y vocabulario claro; definiciones directas. |
| Operable por teclado | Sí — DragText admite arrastrar y soltar por teclado y ofrece textos ARIA (etiquetas de zona de soltado y de elementos arrastrables). |
| Carga cognitiva baja | Sí — una sola pantalla, 4 huecos, instrucción única. |

---

## 6. Moodle

| Campo | Valor |
|---|---|
| Curso | Estrategia Climática |
| Sección | Estrategias de acción climática (mitigación y adaptación) |
| Enlace | Pendiente de publicación |
| Visibilidad | Visible para estudiantes una vez publicado |
| Calificación | Sí — el tipo registra puntuación (4 puntos máx.); califica vía xAPI/Banco de contenido. |
| Finalización | Condición: actividad enviada/comprobada (y, opcionalmente, calificación mínima). |
| Banco de contenido | Almacenar el `.h5p` en el Banco de contenido del curso y enlazar la actividad. |
| Etiquetas/Tags | `mitigación`, `adaptación`, `cambio-climático`, `acción-climática`, `OA-08`, `DragText`, `intermedio` |

---

## 7. Reutilización

| Campo | Valor |
|---|---|
| Qué se puede adaptar | Los ejemplos de los huecos (p. ej. cambiar "energía solar" por otra medida de mitigación), añadir más huecos/definiciones, ajustar la consigna y los textos de feedback. |
| Qué NO debe cambiarse | La distinción conceptual mitigación ≠ adaptación y la asignación correcta de cada término a su hueco (núcleo evaluativo del OA). |
| Variables/parámetros del OA | `taskDescription` (consigna), `textField` (texto con huecos marcados con `*…*`), `behaviour` (reintentos, solución, comprobar, feedback instantáneo), `overallFeedback` (rangos). |
| Cursos compatibles | Estrategia Climática; cualquier curso de sensibilización ambiental/sostenibilidad para ciudadanía o empresas. |

---

## 8. QA y mejora

**Checklist de verificación**

- [x] El paquete abre y la actividad carga (4 huecos detectados).
- [x] Respuestas correctas confirmadas: mitigación / adaptación / solar / adaptación.
- [x] Reintentos y "Mostrar solución" activados.
- [x] Puntuación automática operativa (4 puntos máx.).
- [x] Sin dependencia exclusiva del color para el feedback.
- [x] Operable por teclado y compatible con móvil.
- [ ] Metadatos de licencia fijados a CC BY-NC-SA 4.0 en el paquete (actualmente "U").
- [ ] Validación final del Diseñador Instruccional.
- [ ] Publicación y enlace en Moodle.

| Campo | Valor |
|---|---|
| Incidencias | La licencia en `h5p.json` figura como "U" (sin especificar); debe actualizarse a CC BY-NC-SA 4.0. Sin pistas (tips) ni feedback personalizado por hueco (mejora opcional). |
| Métricas posteriores | Pendientes de uso real en Moodle: tasa de aciertos por hueco, intentos medios, tiempo de resolución, % de finalización. |
| Decisiones de versión | v1.0.0 inicial (publicación base). Criterio SemVer: **MAJOR** = cambio del objetivo/evidencia o reestructuración del ejercicio; **MINOR** = añadir huecos/ejemplos o feedback sin alterar el objetivo; **PATCH** = correcciones menores de texto, tildes, licencia o ajustes de comportamiento. |
