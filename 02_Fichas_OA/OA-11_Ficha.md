# Ficha de diseño — OA-11: Empareja el EcoGesto con su impacto

> **Estado: Construido y empaquetado como `.h5p`.**
> El paquete OA-11 implementa las seis parejas descritas en esta ficha y está disponible en `03_H5P_exportables/`.
>
> **Por qué existe esta ficha:** el backlog de la biblioteca (`01_Catalogo_general/backlog.md`, §"Pendientes recomendados") detecta que la categoría **Gamificación** del plan AHC (§5) **no está cubierta** por los 10 OA terminados. OA-11 introduce un **tipo H5P nuevo en la biblioteca — Memory Game —** y abre la familia de gamificación, avanzando hacia el objetivo del plan de ≥20 OA prototipados.
>
> **Coherencia verbo-formato (obligatoria):** el verbo Bloom de este OA es **Relacionar**. **H5P.MemoryGame (Memory Game)** es el formato idóneo porque la evidencia natural del verbo "relacionar" es **asociar dos elementos que forman una pareja con sentido**. En el Memory Game, el aprendiz **descubre y empareja cartas** (un EcoGesto con su impacto/ahorro): el acto de unir las dos mitades de una pareja **es** la demostración observable y autocalificable de que ha relacionado correctamente el gesto con su efecto. El componente solo valida la pareja cuando la asociación es correcta, de modo que cada acierto es evidencia directa del verbo, sin texto libre que interpretar. El formato añade además la capa lúdica (memoria + descubrimiento) que da nombre a la familia **Gamificación**.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| Código OA | OA-11 |
| Título | Empareja el EcoGesto con su impacto |
| Tipo H5P | H5P.MemoryGame (Memory Game / Juego de memoria) |
| Familia (plan AHC §5) | Gamificación *(tipo nuevo en la biblioteca)* |
| Curso destino | Educación ambiental / EcoGestos |
| Público | Ciudadanía |
| Verbo Bloom | Relacionar |
| Versión prevista | v1.0.0 |
| Licencia | Creative Commons CC BY-NC-SA 4.0 |
| Estado | ✅ Probado en h5p.org · ⏳ Pendiente validación en Moodle |
| Archivo H5P | `OA-11_AHC_H5P_MemoryGame_EcoGestos_Basico_EducacionAmbiental_v1.0.0.h5p` |

> Nota de trazabilidad: propuesta tomada del backlog (`backlog.md`, fila "Empareja EcoGesto–impacto → Memory Game → Relacionar"). Autor del diseño: Equipo de Diseño Instruccional AHC. Construcción asignada (cuando se autorice): Becario H5P. Revisor: Diseñador Instruccional — pendiente de validación del diseño.

---

## 2. Diseño pedagógico

| Campo | Valor |
|---|---|
| Objetivo de aprendizaje | Relacionar cada **EcoGesto** cotidiano con su **impacto o ahorro** asociado (ahorro de CO₂, agua o energía), emparejando correctamente las cartas. |
| Competencia | Alfabetización climática práctica: reconocer que los pequeños gestos diarios tienen un efecto medible sobre la huella de carbono y los recursos. |
| Verbo observable (Bloom) | **Relacionar** (asociar / emparejar). |
| Evidencia observable | El aprendiz descubre y **empareja correctamente las 6 parejas** EcoGesto ↔ impacto; el componente solo da por válida cada pareja cuando la asociación es correcta y registra el resultado. |
| Duración estimada | 3–5 min (microlearning). |
| Prerequisitos | Idea básica de "huella de carbono" y de que las acciones diarias consumen recursos/energía. Ninguno técnico. |
| Mensaje clave | **Cada EcoGesto tiene un impacto medible**: cambios pequeños y repetidos (transporte, agua, energía, residuos, consumo) suman un ahorro real de CO₂ y recursos. |
| Criterio de éxito | Completar el tablero emparejando las **6 parejas** (12 cartas). Logro pleno = tablero resuelto; refuerzo del aprendizaje = resolverlo con el **menor número de intentos/tiempo** posible. |
| Momento de uso | **Apertura motivadora** (enganche lúdico al inicio del módulo de EcoGestos) o **cierre/refuerzo** (consolidación tras ver los gestos en contenido previo). |

---

## 3. Contenido propuesto

### 3.1 Consigna exacta (texto a mostrar)

> **"Da la vuelta a las cartas y empareja cada EcoGesto con su impacto. Encuentra las 6 parejas en el menor número de intentos."**

Texto de cierre al completar el tablero (mensaje de finalización propuesto):

> **"¡Tablero completo! Has emparejado los 6 EcoGestos con su impacto. Cada uno de estos gestos, repetido cada día, reduce tu huella de carbono."**

### 3.2 Parejas (12 cartas = 6 parejas)

Cada **pareja** está formada por dos cartas: **Carta A = EcoGesto** y **Carta B = impacto/ahorro**. La asociación correcta es la fila completa. (En el editor, cada pareja se crea como un par de imágenes/textos con el mismo identificador de pareja; el texto bajo cada carta se usa como descripción accesible.)

| # | Carta A — EcoGesto | Carta B — Impacto / ahorro | Relación correcta (clave del DI) |
|:--:|---|---|---|
| 1 | 🚲 **Ir en bici al trabajo** (5 km/día) en lugar del coche | **≈ 0,7 kg de CO₂ evitados por trayecto** | Transporte activo → menos CO₂ |
| 2 | 🚿 **Ducha de 5 min** en vez de 10 min | **≈ 50 litros de agua ahorrados por ducha** | Menos tiempo de ducha → ahorro de agua |
| 3 | 💡 **Cambiar bombillas a LED** | **≈ 80 % menos de electricidad que las incandescentes** | Iluminación eficiente → ahorro de energía |
| 4 | 🥗 **Un día a la semana sin carne** | **≈ 0,8 kg de CO₂ evitados por comida** | Dieta baja en carne → menos CO₂ |
| 5 | ♻️ **Separar y reciclar los residuos** | **Menos residuos a vertedero y menos metano (CH₄)** | Reciclaje → menos metano del vertedero |
| 6 | 🔌 **Apagar aparatos en vez de dejarlos en standby** | **Hasta un 10 % menos en la factura eléctrica del hogar** | Eliminar consumo fantasma → ahorro de energía |

> Nota de contenido: las cifras son **órdenes de magnitud orientativos y didácticos** propios de la AHC, para ilustrar que el gesto tiene impacto; el DI puede ajustarlas a las referencias oficiales que prefiera antes de construir. Lo **invariable** es la asociación gesto ↔ tipo de ahorro (la clave evaluativa).

### 3.3 Feedback de acierto / error

Memory Game no admite feedback de texto libre por carta; el feedback es **conductual** (la mecánica del juego) más los textos globales configurables. Diseño previsto:

| Situación | Feedback previsto |
|---|---|
| **Acierto** (dos cartas forman pareja) | Las dos cartas **quedan reveladas y emparejadas** (permanecen boca arriba, resaltadas). Micro-refuerzo lúdico (efecto/sonido de "match" si se activa). Mensaje de progreso: *"¡Pareja! Este EcoGesto reduce tu huella."* |
| **Error** (dos cartas no forman pareja) | Las cartas **se vuelven a girar boca abajo** tras un instante; el aprendiz debe recordar y reintentar. No penaliza más allá de sumar un intento. |
| **Tablero completo** (6 parejas) | Mensaje de finalización (ver 3.1) + **resumen de resultado**: número de parejas, intentos realizados y tiempo. Refuerzo: *"Cada gesto cuenta: repetidos cada día, suman."* |

---

## 4. Configuración H5P prevista

| Campo | Valor previsto |
|---|---|
| Comportamiento | Mecánica estándar de Memory Game: voltear dos cartas; si coinciden, quedan emparejadas; si no, se ocultan. **6 parejas / 12 cartas.** |
| Reintentos | Sí — implícitos en la mecánica (el aprendiz repite hasta completar). Botón **"Reiniciar/Jugar de nuevo"** activado al terminar. |
| Puntuación | Resultado por **número de intentos y tiempo** hasta completar el tablero (cuanto menos, mejor). Se reporta vía **xAPI** "completado". *(Memory Game no asigna una nota 0–10 por hueco; el DI decidirá si se usa solo como "completado" o si se mapea el desempeño a calificación en Moodle.)* |
| Aleatorización | **Sí** — el componente **baraja la posición de las cartas** en cada inicio, de modo que el tablero cambia en cada intento (refuerza memoria, evita memorizar posiciones). |
| Navegación | Una sola pantalla/tablero; sin paginación. Interacción por clic/toque sobre las cartas. |
| Compatibilidad móvil | **Sí** — Memory Game es responsive y táctil; el tablero se reordena a cuadrícula adaptable en pantallas pequeñas. Conviene revisar que 12 cartas con texto+icono se lean bien en móvil (ver §5). |

---

## 5. Accesibilidad prevista

| Campo | Valor previsto |
|---|---|
| ALT en imágenes/cartas | **Sí — obligatorio.** Cada carta (icono/imagen) llevará texto **alternativo descriptivo** (p. ej. ALT = "Bicicleta: ir en bici al trabajo"; ALT = "0,7 kg de CO₂ evitados"). El ALT es además lo que lee el lector de pantalla para identificar cada carta. |
| Contraste | Texto de las cartas en **alto contraste** sobre el fondo; no usar tonos de verde sobre verde. Verificar ratio ≥ 4,5:1. |
| No depender solo del color | El estado "emparejada" se indicará por **posición/permanencia boca arriba + ALT**, no solo por color. |
| Navegación por teclado | Memory Game es **operable por teclado** (foco y selección de cartas con Tab/Enter); se verificará en construcción que el foco es visible y el orden es lógico. |
| Subtítulos / transcripción | **N/A** — el OA no incluye vídeo ni audio. Si se activan efectos de sonido de "match", serán **opcionales y no portadores de información** (la información viaja por imagen+texto). |
| Lenguaje claro | Frases cortas, una idea por carta, vocabulario cotidiano; las cifras se acompañan de unidad clara (kg CO₂, litros, %). |
| Carga cognitiva | 6 parejas (12 cartas) es un tamaño cómodo para microlearning; no superar este número para no saturar la memoria de trabajo. |

---

## 6. Reutilización

| Campo | Valor |
|---|---|
| Cursos AHC donde insertarlo | **Educación ambiental / EcoGestos** (destino principal); también **Huella Personal** (como enganche lúdico), formaciones de **sensibilización para ciudadanía**, y jornadas/eventos AHC como dinámica rápida. |
| Qué se puede variar (parámetros) | Las **parejas** (cambiar gestos/impactos por otro set temático: agua, movilidad, energía…), el **número de parejas** (4–8 según público/tiempo), la **consigna** y los **mensajes** de progreso/finalización, los **iconos/imágenes** de las cartas, y los efectos/sonidos. |
| Qué NO debe cambiarse | La **asociación correcta EcoGesto ↔ impacto** de cada pareja (núcleo evaluativo del verbo Relacionar) y el principio de "un gesto = un impacto medible". |
| Variantes sugeridas | *"Empareja el residuo con su contenedor"*, *"Empareja la energía renovable con su fuente"*, *"Empareja el alimento con su huella de CO₂"* — mismo formato, distinto set de cartas. |

---

## 7. Pasos para construirlo (checklist para el becario)

Cuando el DI **autorice** el diseño, montar el OA en el editor H5P:

1. [ ] Abrir el editor H5P (Moodle → **Banco de contenido → Añadir → Memory Game**, o **Lumi Desktop**).
2. [ ] Crear **6 parejas de cartas** (12 cartas). En cada pareja: Carta A = EcoGesto (icono/imagen + texto del §3.2) y Carta B = impacto/ahorro (texto/imagen). Usar el campo de descripción/ALT de cada carta.
3. [ ] Escribir la **consigna** del §3.1 en el campo de instrucción y los **mensajes** de acierto/finalización del §3.3.
4. [ ] Configurar comportamiento (§4): barajar cartas activado, botón "Jugar de nuevo", efectos de sonido opcionales.
5. [ ] Rellenar **ALT** en todas las cartas y revisar **contraste** y **navegación por teclado** (§5).
6. [ ] Fijar **metadatos**: título "OA-11: Empareja el EcoGesto con su impacto", autor AHC, **licencia CC BY-NC-SA 4.0** (no dejar "U").
7. [ ] Probar en **escritorio y móvil**; verificar que las 6 parejas se emparejan correctamente.
8. [ ] **Exportar** el paquete `.h5p` y guardarlo en el Banco de contenido del curso.
9. [ ] Enviar al **DI para validación** y, tras el visto bueno, **publicar y enlazar** en Moodle. Actualizar el backlog (OA-11 → prototipado/terminado).

---

> **Estado de entrega:** paquete construido y validado técnicamente; queda la validación pedagógica final del DI.
