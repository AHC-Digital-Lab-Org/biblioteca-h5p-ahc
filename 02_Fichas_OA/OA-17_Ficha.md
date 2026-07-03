# Ficha de diseño — OA-17: Ordena el proceso de compostaje doméstico

> **Estado: Construido y empaquetado como `.h5p`.** Incluye las seis imágenes accesibles y la secuencia descrita en esta ficha. Queda pendiente la validación pedagógica final del DI.
>
> **Por qué existe esta ficha:** OA-17 sale del backlog de la biblioteca (`01_Catalogo_general/backlog.md`, sección de pendientes recomendados), donde se propone "Ordena el proceso de compostaje" con **Image Sequencing** como **tipo H5P nuevo** para el curso **EcoGestos**. Esta ficha deja el diseño cerrado y validable por el Diseñador Instruccional (DI) **antes** de invertir tiempo en construir el paquete, de modo que el becario reciba un guion sin ambigüedades.
>
> **Coherencia verbo-formato:** el verbo Bloom es **Ordenar** (nivel de aplicación/análisis procedimental). **H5P.ImageSequencing (Image Sequencing)** es el formato idóneo para recoger esa evidencia porque presenta un conjunto de imágenes desordenadas que el estudiante debe **reordenar arrastrándolas** hasta reconstruir la secuencia correcta. La evidencia del verbo *Ordenar* es exactamente eso: colocar pasos en el orden temporal/lógico correcto. El componente autocalifica (compara el orden del usuario con el orden de referencia) y da feedback inmediato, por lo que la secuencia ordenada **es** la evidencia observable, sin necesidad de interpretación manual.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| Código OA | OA-17 |
| Título | Ordena el proceso de compostaje doméstico |
| Tipo H5P | H5P.ImageSequencing (Image Sequencing / Secuenciación de imágenes) |
| Familia (plan AHC §5) | Práctica |
| Curso destino | EcoGestos |
| Público | Ciudadanía |
| Verbo Bloom | Ordenar |
| Versión prevista | v1.0.0 |
| Licencia | Creative Commons CC BY-NC-SA 4.0 |
| Estado | ✅ Probado en h5p.org · ⏳ Pendiente validación en Moodle |
| Archivo H5P | `OA-17_AHC_H5P_ImageSequencing_Compostaje_Basico_EcoGestos_v1.0.0.h5p` |

> Nota de trazabilidad: el título interno previsto para el paquete (`h5p.json`) será "OA-17: Ordena el proceso de compostaje domestico" (sin tildes en metadatos, por compatibilidad). La licencia debe fijarse explícitamente a **CC BY-NC-SA 4.0** al construir el paquete (no dejar "U"/sin especificar).

---

## 2. Diseño pedagógico

| Campo | Valor |
|---|---|
| Objetivo de aprendizaje | Ordenar correctamente las fases del compostaje doméstico, desde la preparación del compostador hasta la obtención del compost maduro, reconstruyendo la secuencia lógica del proceso. |
| Competencia | Acción climática práctica: reducir los residuos orgánicos del hogar gestionándolos mediante compostaje, contribuyendo a evitar emisiones de metano del vertedero. |
| Verbo observable (Bloom) | Ordenar |
| Evidencia observable | El estudiante reordena 6 imágenes desordenadas hasta dejar la secuencia del compostaje en el orden correcto (preparar → llenar → equilibrar → airear → controlar humedad → cosechar) y el componente confirma la coincidencia con el orden de referencia. |
| Duración estimada | 4–6 min |
| Prerequisitos | Saber qué residuos son orgánicos (restos vegetales, posos de café) frente a no compostables. Útil (no obligatorio) haber visto un EcoGesto previo sobre separación de residuos. |
| Mensaje clave | El compostaje doméstico transforma los restos orgánicos en abono siguiendo un orden: **mezclar verde y marrón, airear y controlar la humedad**. Hacerlo bien evita olores, atrae menos plagas y reduce las emisiones de metano que esos residuos generarían en el vertedero. |
| Criterio de éxito | Secuencia 100% correcta (las 6 imágenes en su posición) en un máximo de 2 intentos, con uso opcional del botón "Comprobar" para verificar antes de finalizar. |
| Momento de uso | Desarrollo del módulo de residuos de **EcoGestos** (práctica activa tras la explicación), o cierre como comprobación rápida del procedimiento. |

---

## 3. Contenido propuesto

**Consigna exacta (texto de la tarea / `taskDescription`):**

> "El compostaje doméstico tiene un orden. Arrastra y coloca las imágenes en la secuencia correcta, desde el primer paso hasta obtener el compost listo para usar."

**Imágenes a ordenar (los 6 ítems, en el ORDEN CORRECTO de referencia).** Cada ítem necesita una imagen y un texto descriptivo corto (que H5P usa como etiqueta y como ALT accesible):

| Posición correcta | Imagen prevista | Texto / etiqueta del ítem | ALT propuesto |
|---|---|---|---|
| 1 | Compostador vacío con una capa de ramas finas en el fondo | "Preparar el compostador" | "Compostador doméstico vacío con una capa de ramas finas en el fondo para drenaje y aireación" |
| 2 | Manos echando restos de fruta y verdura | "Añadir restos orgánicos (verde)" | "Manos depositando restos de fruta y verdura, material húmedo rico en nitrógeno" |
| 3 | Echando hojas secas / cartón sobre los restos | "Equilibrar con material marrón" | "Capa de hojas secas y cartón troceado cubriendo los restos húmedos para equilibrar carbono y nitrógeno" |
| 4 | Removiendo la mezcla con una horca | "Airear y mezclar" | "Persona removiendo el compost con una horca para oxigenar la pila" |
| 5 | Comprobando humedad apretando un puñado | "Controlar la humedad" | "Mano apretando un puñado de compost para comprobar que está húmedo como una esponja escurrida" |
| 6 | Compost oscuro y desmenuzado en las manos | "Cosechar el compost maduro" | "Compost maduro, oscuro y desmenuzado, listo para usar como abono" |

> En el editor, las 6 imágenes se introducen **en este orden correcto**: Image Sequencing guarda esa secuencia como referencia y **baraja automáticamente** la presentación al estudiante. No hay que desordenarlas a mano.

**Respuesta correcta:** la secuencia 1 → 2 → 3 → 4 → 5 → 6 tal como se lista arriba (Preparar → Añadir verde → Equilibrar marrón → Airear → Controlar humedad → Cosechar).

**Feedback de acierto/error:**

- **Acierto (secuencia completa correcta):** "¡Perfecto! Has reconstruido el ciclo del compostaje. Recuerda la regla de oro: alterna material **verde** (húmedo) y **marrón** (seco), airea y vigila la humedad. Así obtienes abono y evitas las emisiones de metano del vertedero."
- **Acierto parcial / error (alguna imagen mal colocada):** "Casi. Revisa el orden: primero se **prepara** el compostador, luego se **alterna verde y marrón**, después se **airea** y se **controla la humedad**, y al final se **cosecha** el compost maduro. Reordena las imágenes que estén fuera de sitio y vuelve a comprobar."
- **Pista opcional por ítem (campo de ayuda contextual, si el editor lo permite):** breve recordatorio del tipo "El material seco (marrón) va *sobre* los restos húmedos, no antes".

---

## 4. Configuración H5P prevista

| Campo | Valor previsto |
|---|---|
| Comportamiento | Mostrar botón "Comprobar" para verificar la secuencia. Tras comprobar, marcar visualmente las imágenes en posición correcta e incorrecta (no solo por color). |
| Reintentos | Sí — botón "Reintentar" activado para permitir reordenar tras un fallo (encaja con el criterio de éxito de ≤2 intentos). |
| Puntuación | Automática: 1 punto por imagen en su posición correcta (6 imágenes → **6 puntos máx.**). Barra de puntuación visible. |
| Aleatorización | Sí — la presentación inicial de las imágenes se **baraja automáticamente** en cada carga (comportamiento nativo de Image Sequencing), de modo que el orden de salida nunca coincide con el correcto. |
| Navegación | Una sola pantalla; el estudiante arrastra y suelta para reordenar. Sin paginación. "Comprobar" → feedback → "Reintentar" o finalizar. |
| Compatibilidad móvil | Sí — arrastrar y soltar táctil (responsive). Imágenes con relación de aspecto homogénea para que la rejilla se vea bien en pantallas estrechas. |

---

## 5. Accesibilidad prevista

| Campo | Valor previsto |
|---|---|
| ALT en imágenes | **Obligatorio** en las 6 imágenes (textos alternativos propuestos en la tabla del §3). Image Sequencing usa el texto descriptivo del ítem como etiqueta accesible. |
| Contraste | Etiquetas de texto con contraste suficiente sobre la imagen (banda/fondo si hace falta). Marcas de correcto/incorrecto con icono + texto, no solo color. |
| Navegación por teclado | Verificar la operabilidad por teclado del arrastrar-y-soltar; ofrecer textos ARIA de las zonas y de los elementos. Si el componente no garantiza reordenación completa por teclado, documentarlo como limitación conocida. |
| Subtítulos / transcripción | N/A — el OA no incluye vídeo ni audio. |
| Lenguaje claro | Etiquetas cortas e imperativas ("Airear y mezclar", "Controlar la humedad"); consigna directa; sin tecnicismos innecesarios. |
| Carga cognitiva | Baja: una sola tarea, 6 pasos, una instrucción. |

---

## 6. Reutilización

| Campo | Valor |
|---|---|
| Cursos AHC donde insertarlo | **EcoGestos** (curso destino). Reutilizable en cualquier curso de sensibilización/educación ambiental para ciudadanía donde se trate gestión de residuos orgánicos en el hogar. |
| Parámetros a variar | `taskDescription` (consigna); el conjunto y orden de las **imágenes** (p. ej. versión "compostaje en vermicompostera" o "compostaje comunitario" cambiando las fotos y sus etiquetas); número de pasos (5–7); textos de feedback y pistas; etiquetas de los ítems. |
| Qué NO debe cambiarse | La **lógica del orden** (preparar antes de llenar; equilibrar verde/marrón antes de airear; cosechar al final): es el núcleo evaluativo del verbo *Ordenar*. |

---

## 7. Pasos para construirlo (checklist para el becario)

- [ ] Reunir/crear las **6 imágenes** del §3 (propias o de banco con licencia compatible; documentar la fuente). Recortarlas a una relación de aspecto homogénea (p. ej. 4:3).
- [ ] En el editor H5P (Lumi en local o el plugin H5P de Moodle), crear un contenido nuevo de tipo **Image Sequencing**.
- [ ] Pegar la **consigna exacta** del §3 en el campo de descripción de la tarea (`taskDescription`).
- [ ] Añadir las 6 imágenes **en el orden correcto** (posición 1 → 6); rellenar el texto/etiqueta y el **ALT** de cada una según la tabla.
- [ ] Configurar comportamiento del §4: "Comprobar" y "Reintentar" activados; barajado automático (por defecto); puntuación 1 punto/imagen.
- [ ] Redactar los **feedback de acierto y error** del §3 en los campos correspondientes.
- [ ] Fijar la **licencia a CC BY-NC-SA 4.0** y los metadatos (título "OA-17: Ordena el proceso de compostaje domestico", autoría AHC).
- [ ] Previsualizar: comprobar que las imágenes salen **desordenadas**, que "Comprobar" detecta el orden correcto y que el feedback aparece. Probar en móvil.
- [ ] Exportar el paquete `.h5p` y guardarlo en la carpeta de entregables; actualizar el backlog y pasar la ficha a validación del **DI**.
- [ ] Validación final del Diseñador Instruccional → cambiar Estado a "Validado" y publicar en Moodle (Banco de contenido del curso EcoGestos).

---

> **Estado de entrega:** paquete construido y validado técnicamente; queda la validación pedagógica final del DI.
