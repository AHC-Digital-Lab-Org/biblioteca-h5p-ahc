# Checklist de Calidad y QA — Biblioteca H5P AHC

> Instrumento de validación obligatorio. Cada Objeto de Aprendizaje (OA) debe superar **todas** las
> dimensiones antes de marcarse como *Publicado* en Moodle (plan AHC §9, Guía Curricular p.90).
> Marca cada punto: `[x]` cumplido · `[ ]` pendiente · `[N/A]` no aplica.

Cómo usarlo: duplica este checklist por cada OA (o usa la tabla resumen del final), márcalo en la revisión
del Diseñador Instruccional (DI) y archiva el resultado en `06_Revisiones_DI/`.

---

## 1. Diseño pedagógico
- [ ] Objetivo de aprendizaje claro y redactado con verbo observable (Bloom).
- [ ] Evidencia observable concreta: el OA obliga a una acción que demuestra el aprendizaje.
- [ ] **Coherencia verbo-formato**: el tipo H5P elegido permite recoger esa evidencia (no se elige por estética). Si no coincide, se rediseña **antes** de publicar.
- [ ] Microlearning real: una idea principal, duración **3–10 min**, entre 1 y 3 evidencias.
- [ ] Coherente con el curso y el momento de uso (inicio / desarrollo / cierre).

## 2. Contenido
- [ ] Mensaje clave identificable.
- [ ] Exactitud técnica del contenido climático (datos y conceptos correctos).
- [ ] Fuentes citadas cuando procede.
- [ ] Sin exceso de texto; lenguaje claro y directo.

## 3. Configuración H5P
- [ ] Solución correcta marcada y validada.
- [ ] Reintentos configurados según el propósito (práctica vs evaluación).
- [ ] Feedback presente, breve y explicativo (no penaliza sin explicar).
- [ ] Puntuación y condiciones de finalización configuradas.
- [ ] Metadatos y autoría completados dentro del propio H5P.

## 4. Accesibilidad
> Ver el detalle ampliado en [`Checklist_Accesibilidad.md`](./Checklist_Accesibilidad.md).
- [ ] Texto alternativo (ALT) en todas las imágenes, mapas, iconos y gráficos.
- [ ] Subtítulos **VTT** y transcripción en todo contenido de vídeo/audio.
- [ ] Contraste de color suficiente; no se depende solo del color para transmitir información.
- [ ] Operable por teclado, con foco visible.
- [ ] Lectura fácil y carga cognitiva baja (pantallas limpias).

## 5. Moodle
- [ ] Se visualiza correctamente dentro del curso.
- [ ] Funciona en móvil además de escritorio.
- [ ] Guarda calificación si procede; finalización de actividad correcta.
- [ ] Permisos y visibilidad correctos.

## 6. Licencias y publicación
- [ ] Verificadas las **licencias** de todos los recursos (imágenes, audio, vídeo).
- [ ] Licencia del OA declarada: **Creative Commons CC BY-NC-SA 4.0** (estándar AHC).
- [ ] Atribución/autoría registrada.

## 7. Reutilización y versionado
- [ ] Archivo `.h5p` exportado a `03_H5P_exportables/` con la nomenclatura oficial.
- [ ] Ficha documental completa (8 bloques) en `02_Fichas_OA/`.
- [ ] Assets originales guardados en `04_Assets_imagen_audio_video/`.
- [ ] Variables de adaptación documentadas en el bloque *Reutilización* de la ficha.
- [ ] Versión semántica `vX.Y.Z` registrada; cambios anotados (MAJOR/MINOR/PATCH).

## 8. Piloto y mejora (Guía Curricular)
- [ ] Probado como **estudiante** y como **profesor** en un curso piloto.
- [ ] Validado: finalización, calificación, reintentos, navegación y trazabilidad.
- [ ] Revisión del **Diseñador Instruccional** registrada.
- [ ] Plan de mejora continua tras uso real (ítems fallados, tiempo medio, tasa de finalización).

---

## Tabla resumen de control (10 OA terminados)

| OA | Pedagógico | Contenido | Config H5P | Accesib. | Moodle | Licencia | Reutiliz. | Piloto | Estado |
|----|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--|
| OA-01 | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | Pendiente piloto Moodle |
| OA-02 | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | Pendiente piloto Moodle |
| OA-03 | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | Pendiente piloto Moodle |
| OA-04 | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | Pendiente piloto Moodle |
| OA-05 | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | Pendiente piloto Moodle |
| OA-06 | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | Pendiente piloto Moodle |
| OA-07 | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | Pendiente piloto Moodle |
| OA-08 | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | Pendiente piloto Moodle |
| OA-09 | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | Pendiente piloto Moodle |
| OA-10 | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | Pendiente piloto Moodle |

> Los paquetes `.h5p` están construidos, validados técnicamente y empaquetados con nomenclatura oficial.
> Las columnas *Moodle* y *Piloto* quedan pendientes porque requieren un entorno Moodle real (credenciales
> y curso destino) que está fuera del alcance de la producción local.
