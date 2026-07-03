# Ficha — OA-18: Dónde se concentra tu huella

> **Estado: Empaquetado.** El paquete `.h5p` de este OA está disponible en `03_H5P_exportables/`, generado a partir de esta ficha y verificado en un reproductor H5P. Esta ficha documenta su diseño (consigna, ítems, feedback y configuración); el contenido pedagógico queda a validación del Diseñador Instruccional (DI) como parte del control de calidad habitual.
>
> **Por qué existe esta ficha:** OA-18 sale del backlog de la Biblioteca H5P AHC (sección «Pendientes recomendados»), donde figura como *«¿Dónde se concentra la huella?» — Chart — Interpretar — Huella Personal — Tipo nuevo (datos)*. Su función es cubrir un **tipo H5P que hoy falta en la biblioteca** (visualización de datos) y aportar al curso *Huella de Carbono Personal* una pieza de **interpretación de datos** que conecte el cálculo de la huella con la decisión de dónde actuar. Esta ficha deja fijado el contenido real (consigna, datos del gráfico, lectura esperada y feedback) para que el becario lo construya sin ambigüedad.
>
> **Coherencia verbo-formato:** el verbo Bloom de este OA es **Interpretar**, y **H5P.Chart (Chart)** es el formato idóneo para recoger su evidencia. Interpretar no es memorizar ni clasificar: es *leer un conjunto de datos y extraer su significado*. Un gráfico de barras/sectores con el reparto de la huella personal por categoría obliga al usuario a **comparar magnitudes, identificar la categoría dominante y traducir esa lectura en una conclusión de acción** ("dónde actuar primero"). El propio componente Chart muestra los datos de forma visual y autoexplicativa, y la evidencia de interpretación se recoge en la pregunta de lectura asociada (qué categoría pesa más / qué conclusión se deduce). Así el formato hace observable justo lo que el verbo pide: dar sentido a los datos, no solo verlos.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| Código OA | OA-18 |
| Título | Dónde se concentra tu huella |
| Tipo H5P | H5P.Chart (Chart / Gráfico) |
| Familia (plan AHC §5) | Práctica |
| Curso destino | Huella de Carbono Personal |
| Público | Ciudadanía |
| Verbo Bloom | Interpretar |
| Versión prevista | v1.0.0 |
| Licencia | Creative Commons CC BY-NC-SA 4.0 |
| Estado | ✅ Probado en h5p.org · ⏳ Pendiente validación en Moodle |
| Archivo H5P | `OA-18_AHC_H5P_Chart_RepartoHuella_Basico_HuellaPersonal_v1.0.0.h5p` |

> Nota: el autor (becario H5P) y el revisor (DI) se asignarán al abrir la construcción. La fecha de publicación queda pendiente.

---

## 2. Diseño pedagógico

| Campo | Valor |
|---|---|
| Objetivo de aprendizaje | Interpretar el reparto de la huella de carbono personal por categorías de consumo para identificar dónde se concentra el mayor impacto y deducir sobre qué área conviene actuar primero. |
| Competencia | Alfabetización climática aplicada: leer e interpretar datos de huella personal para tomar decisiones informadas de reducción de emisiones. |
| Verbo observable (Bloom) | Interpretar (leer datos, comparar magnitudes y extraer una conclusión). |
| Evidencia observable | A partir del gráfico de reparto de la huella, el usuario responde correctamente cuál es la categoría de mayor impacto y qué conclusión de acción se deduce (señalar la categoría dominante y la prioridad de actuación). |
| Duración estimada | 3–5 min |
| Prerequisitos | Saber qué es la huella de carbono personal y conocer las categorías básicas de consumo (transporte, hogar/energía, alimentación, consumo/bienes). Ideal tras OA-15 («Huella personal en 5 decisiones») o tras el cálculo de la propia huella. |
| Mensaje clave | No todas las categorías pesan igual: identificar **dónde se concentra** la huella (la categoría dominante) permite priorizar la acción que más reduce emisiones, en lugar de dispersar esfuerzos. |
| Criterio de éxito | El usuario lee el gráfico y acierta la pregunta de interpretación: reconoce la categoría con mayor porcentaje y elige la conclusión de acción coherente con ese dato. |
| Momento de uso | Desarrollo (interpretación de resultados, tras presentar o calcular la huella). También sirve de cierre reflexivo del bloque de huella personal. |

---

## 3. Contenido propuesto

> El componente **H5P.Chart** por sí solo muestra datos pero **no se autocalifica** (no registra respuestas). Para recoger la evidencia del verbo *Interpretar*, el diseño combina **el gráfico (Chart)** con una **pregunta de lectura asociada** que sí evalúa. En construcción esto se monta como: (a) un Chart con el reparto de la huella, y (b) una pregunta de opción múltiple de interpretación situada justo debajo (idealmente ambos dentro de un **H5P.Column**, o bien el gráfico como apoyo visual previo a un `Multiple Choice`). Aquí se especifica el contenido real de ambas partes.

### 3.1 Datos del gráfico (Chart)

- **Tipo de gráfico:** barras (recomendado por ser el más legible para comparar magnitudes; alternativa: sectores/tarta si se prefiere mostrar "reparto del 100%").
- **Título del gráfico:** «Reparto de tu huella de carbono personal (media orientativa, % anual)».
- **Datos (categoría → % de la huella anual, valores orientativos de una persona media en España):**

| Categoría | % de la huella | Color sugerido |
|---|---|---|
| Transporte (coche, avión, desplazamientos) | 30 % | Rojo/naranja |
| Hogar y energía (calefacción, electricidad) | 25 % | Azul |
| Alimentación (especialmente carne y lácteos) | 20 % | Verde |
| Consumo y bienes (ropa, electrónica, compras) | 15 % | Morado |
| Residuos y otros | 10 % | Gris |

> Los porcentajes suman 100 % y son **valores orientativos didácticos** de la AHC para que el reparto sea claro; no son una medición individual. En la consigna se aclara que son una media para ilustrar el patrón general.

### 3.2 Consigna exacta (texto a mostrar sobre el gráfico)

> «Este gráfico muestra cómo se reparte, de media, la huella de carbono de una persona. **Obsérvalo con atención**: fíjate en qué categoría ocupa la barra más alta y cuál la más baja. Después responde a la pregunta para interpretar **dónde se concentra el mayor impacto** y decidir por dónde empezar a actuar.»

### 3.3 Pregunta de interpretación (la que recoge la evidencia)

**Enunciado:** «Según el gráfico, ¿en qué categoría se concentra el mayor impacto de la huella personal y qué conviene priorizar para reducirla más?»

| # | Opción | ¿Correcta? |
|---|---|---|
| A | El **transporte** es la categoría de mayor peso (30 %); priorizar reducir desplazamientos en coche/avión es lo que más reduce la huella. | ✅ Correcta |
| B | Los **residuos** son la categoría de mayor peso; reciclar más es lo que más reduce la huella. | ❌ Incorrecta |
| C | Todas las categorías pesan igual, así que da igual por dónde empezar. | ❌ Incorrecta |
| D | La **alimentación** es la categoría de mayor peso; cambiar la dieta es lo que más reduce la huella. | ❌ Incorrecta |

> Respuesta correcta: **A**. (Diseño con respuesta única; `singleAnswer = true`.)

### 3.4 Feedback (acierto / error)

| Caso | Texto de feedback propuesto |
|---|---|
| Acierto (elige A) | «✅ ¡Bien interpretado! El **transporte** es la barra más alta (30 %): ahí se concentra tu mayor impacto. Reducir trayectos en coche y avión, compartir coche o usar transporte público es lo que más baja tu huella. Empezar por lo que más pesa multiplica el efecto de tu esfuerzo.» |
| Error — elige B (residuos) | «❌ Casi. Los residuos son la barra **más baja** (10 %): importan, pero no es donde más reduces. Vuelve a mirar qué categoría tiene la barra más alta. Pista: piensa en cómo te desplazas.» |
| Error — elige C (todas iguales) | «❌ No exactamente. El gráfico muestra que las categorías **no pesan igual**: las barras tienen alturas distintas. Interpretar el gráfico es justamente detectar cuál destaca para priorizar. Fíjate en la barra más alta.» |
| Error — elige D (alimentación) | «❌ Buena observación, la alimentación pesa (20 %) y reducir carne/lácteos ayuda mucho. Pero **no es la barra más alta**: hay otra categoría por encima. Compara de nuevo transporte y alimentación.» |
| Feedback global (rango de puntuación) | 0 %: «Revisa el gráfico: localiza la barra más alta antes de elegir.» / 100 %: «Sabes interpretar dónde se concentra tu huella y por dónde priorizar la acción. ¡Ese es el primer paso para reducirla!» |

---

## 4. Configuración H5P prevista

| Campo | Valor |
|---|---|
| Componente principal | H5P.Chart (gráfico de barras) como visualización; H5P.MultiChoice como pregunta de interpretación que recoge la evidencia. Montaje recomendado: ambos dentro de un **H5P.Column** (gráfico arriba, pregunta debajo). |
| Comportamiento | Pregunta con botón «Comprobar» activado; «Mostrar solución» activado; feedback inmediato al comprobar. El Chart se muestra siempre visible como apoyo a la lectura. |
| Reintentos | Sí — «Reintentar» activado en la pregunta (`enableRetry: true`), para que el usuario vuelva a mirar el gráfico y corrija. |
| Puntuación | Sí — 1 punto por respuesta correcta (1 punto máx.). El Chart en sí no puntúa; la puntuación la aporta la pregunta de interpretación. Barra de puntuación visible. |
| Aleatorización | Orden de las opciones A–D barajado en cada intento (`randomAnswers: true`). Los datos del gráfico son fijos (no se aleatorizan). |
| Navegación | Pantalla única, sin paginación; el usuario observa el gráfico y responde debajo. Sin temporizador. |
| Compatibilidad móvil | Sí — Chart y MultiChoice son responsive; el gráfico se reescala y las opciones son pulsables en táctil. Verificar legibilidad de etiquetas del gráfico en pantalla pequeña durante la construcción. |
| Licencia en metadatos | Fijar **CC BY-NC-SA 4.0** en el `h5p.json` al construir (no dejar «U»). |

---

## 5. Accesibilidad prevista

| Campo | Valor |
|---|---|
| Texto alternativo / datos accesibles | El gráfico **no debe transmitir la información solo por color o forma visual**: las etiquetas de cada categoría y su porcentaje deben aparecer como texto junto a cada barra. Añadir bajo el gráfico un resumen textual de los datos (la tabla 3.1) para lectores de pantalla y para quien no distinga el gráfico. |
| Contraste | Usar colores con contraste suficiente entre barras y respecto al fondo; no apoyar la diferencia entre categorías únicamente en tonos próximos. Verificar contraste AA del texto de etiquetas y opciones. |
| No depender solo del color | La categoría dominante se identifica por **altura de barra + etiqueta de % + texto**, no solo por color. El acierto/error de la pregunta se indica con icono y texto, no solo con color. |
| Navegación por teclado | La pregunta MultiChoice es operable por teclado (tabulación entre opciones, selección con Enter/Espacio) y expone etiquetas ARIA por defecto de H5P. |
| Subtítulos / transcripción | N/A — el OA no incluye vídeo ni audio. |
| Lenguaje claro | Consigna y opciones en frases cortas, vocabulario cotidiano (transporte, hogar, alimentación, consumo). Evitar tecnicismos; «huella» se usa como sinónimo de «huella de carbono» ya conocido en el curso. |

---

## 6. Reutilización

| Campo | Valor |
|---|---|
| Cursos AHC donde insertarlo | *Huella de Carbono Personal* (curso destino). Reutilizable en *Educación ambiental* y en sensibilización para *Embajador Climático* como pieza de lectura de datos. También como apoyo visual en cualquier módulo que presente el reparto de emisiones. |
| Parámetros a variar | Datos del Chart (categorías y %) para reflejar otro perfil (p. ej. huella de una **empresa**: energía, transporte de mercancías, residuos industriales) o medias de otro país; título del gráfico; enunciado y opciones de la pregunta; textos de feedback; tipo de gráfico (barras ↔ sectores). |
| Qué NO cambiar | El núcleo del OA: que haya **una categoría claramente dominante** que el usuario deba identificar, y que la conclusión correcta una «categoría con mayor % → prioridad de acción». Si se cambian los datos, la opción correcta debe seguir señalando la barra más alta. |
| Variante sugerida | Versión «empresa/organización» con el reparto típico de una pyme para el curso de Embajador Climático (mismo formato, datos distintos). |

---

## 7. Pasos para construirlo (checklist para el becario)

Construcción en el editor H5P de Moodle o en **Lumi** (escritorio), exportando el `.h5p`:

- [ ] Crear contenido nuevo y elegir el tipo **Column** (para combinar gráfico + pregunta en una sola pantalla).
- [ ] Dentro de Column, añadir un bloque **Chart**: tipo «Bar chart» (barras), título «Reparto de tu huella de carbono personal (media orientativa, % anual)».
- [ ] Introducir las 5 filas de datos de la tabla 3.1 (Transporte 30, Hogar y energía 25, Alimentación 20, Consumo y bienes 15, Residuos y otros 10), asignando un color contrastado a cada barra.
- [ ] Añadir, encima del gráfico, el texto de consigna 3.2 (puede ir en un bloque de texto del Column).
- [ ] Añadir debajo un bloque **Multiple Choice** con el enunciado 3.3 y las opciones A–D; marcar **A** como correcta (respuesta única).
- [ ] Cargar los textos de feedback por opción y el feedback global (rango 0 % y 100 %) según 3.4.
- [ ] En «Behavioural settings» de la pregunta: activar «Retry», «Show solution» y barajar respuestas (`randomAnswers`).
- [ ] Añadir bajo el gráfico el **resumen textual de los datos** (accesibilidad) y revisar contraste de colores.
- [ ] Rellenar **metadatos**: título «OA-18: Donde se concentra tu huella», autor (becario), licencia **CC BY-NC-SA 4.0**, versión **1.0.0**.
- [ ] Probar en escritorio y móvil: que el gráfico se lea, que la pregunta puntúe y que reintentar funcione.
- [ ] Exportar el `.h5p`, guardarlo en el Banco de contenido del curso y pasar la ficha a **validación del DI**.

---

> **Recordatorio final:** este documento es la **especificación de diseño** de OA-18. La construcción, el empaquetado y la publicación en Moodle quedan pendientes y deben seguir los pasos de la sección 7. Estado actual: **Empaquetado · .h5p disponible.**
