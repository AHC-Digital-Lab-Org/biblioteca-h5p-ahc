# Checklist de Accesibilidad — Biblioteca H5P AHC

> Verificación **obligatoria antes de publicar** cada OA (Guía Curricular AHC, paso 6 + Anexos, p.90).
> Objetivo: garantizar experiencias accesibles, inclusivas y usables en cualquier dispositivo.
> Marca: `[x]` cumplido · `[ ]` pendiente · `[N/A]` no aplica al tipo de contenido.

---

## Texto e imágenes
- [ ] **ALT / texto alternativo** descriptivo en todas las imágenes, mapas, iconos y gráficos.
- [ ] La información no se transmite **solo por color** (apta para daltonismo): se acompaña de texto, forma o icono.
- [ ] **Contraste** suficiente entre texto y fondo (objetivo WCAG AA: 4.5:1 en texto normal).
- [ ] **Lectura fácil**: lenguaje directo, claro y breve; una idea principal por OA.

## Vídeo y audio
- [ ] **Subtítulos en formato VTT** (`.vtt`) sincronizados en todo el vídeo.
- [ ] **Transcripción** textual disponible del contenido audiovisual.
- [ ] El audio no es el único canal de una información relevante.

## Interacción y navegación
- [ ] Contenido **operable por teclado** (tabulación lógica).
- [ ] **Foco visible** en todos los elementos interactivos.
- [ ] Zonas de interacción (botones, dropzones, hotspots) suficientemente grandes.
- [ ] **Feedback** breve, comprensible y explicativo; no se penaliza sin explicar.

## Carga cognitiva y diseño
- [ ] Pantallas limpias, sin exceso de texto.
- [ ] Carga cognitiva baja: el OA no se convierte en una mini clase teórica.
- [ ] Imágenes optimizadas/ligeras (carga rápida también en móvil).

## Dispositivos
- [ ] Probado en **escritorio**.
- [ ] Probado en **móvil** (visualización, interacción y reintentos).

---

### Notas por tipo de H5P de esta biblioteca
- **Dialog Cards / Accordion / Fill in the Blanks / Drag the Words / True-False / Question Set**: contenido principalmente textual → priorizar contraste, lectura fácil, operación por teclado y feedback. Subtítulos/transcripción **N/A** (sin vídeo).
- **Image Hotspots / Find the Hotspot**: imprescindible **ALT** de la imagen base y de cada hotspot; describir verbalmente la información que aporta la imagen; no depender solo de la posición visual.
- **Drag and Drop (DragQuestion)**: zonas de soltado amplias, instrucciones claras y alternativa comprensible para teclado; feedback por error.

> Recomendación AHC: cuando un OA incorpore vídeo en el futuro, añadir VTT + transcripción y volver a pasar este checklist antes de re-publicar (nueva versión MINOR).
