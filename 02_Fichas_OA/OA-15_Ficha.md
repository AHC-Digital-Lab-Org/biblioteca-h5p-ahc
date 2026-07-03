# Ficha — OA-15: El camino de una entidad hacia el registro MITECO

> **Estado: Empaquetado.** El paquete `.h5p` de este OA está disponible en `03_H5P_exportables/`, generado a partir de esta ficha y verificado en un reproductor H5P. Esta ficha documenta su diseño (consigna, ítems, feedback y configuración); el contenido pedagógico queda a validación del Diseñador Instruccional (DI) como parte del control de calidad habitual.
>
> **Por qué existe esta ficha:** OA-15 figura en el backlog de la Biblioteca como pendiente recomendado que aporta un **tipo H5P nuevo** (Timeline / secuenciación) y cubre el verbo **Ordenar** dentro de la familia **Práctica** del plan AHC (§5). La ficha fija el alcance, el contenido real del dominio climático y los criterios de evidencia para que la construcción posterior sea fiel al diseño pedagógico y no improvisada.
>
> **Coherencia verbo–formato (obligatoria):** el tipo **H5P.Timeline (Timeline)** es idóneo para recoger la evidencia del verbo **Ordenar**, porque presenta los hitos del proceso de registro como una **línea temporal secuenciada** que el estudiante recorre en el orden correcto (calcular → reducir → compensar → inscribir → sello). La cronología es el propio esquema mental que debe interiorizar: ver los hitos colocados *en secuencia y a escala temporal* hace observable que el alumno comprende **qué va antes y qué va después**, que es exactamente lo que mide *Ordenar*. La evidencia se complementa con una micro-comprobación de orden (3 ítems "antes/después") incrustada al cierre, ya que Timeline por sí solo es expositivo-navegable y no autocalifica.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| Código OA | OA-15 |
| Título | El camino de una entidad hacia el registro MITECO |
| Tipo H5P | H5P.Timeline (Timeline / Línea del tiempo) |
| Familia (plan AHC §5) | Práctica |
| Curso destino | Registro de Huella / MITECO |
| Público | Empresas y entidades |
| Verbo Bloom | Ordenar (secuenciar hitos del proceso) |
| Versión prevista | 1.0.0 |
| Licencia | Creative Commons CC BY-NC-SA 4.0 |
| Estado | ✅ Probado en h5p.org · ⏳ Pendiente validación en Moodle |
| Archivo H5P | `OA-15_AHC_H5P_Timeline_RegistroMITECO_Intermedio_RegistroMITECO_v1.0.0.h5p` |

> Nota de trazabilidad: al construir el paquete, el título interno (`h5p.json`) será "OA-15: El camino de una entidad hacia el registro MITECO" y la licencia se fijará desde el inicio a **CC BY-NC-SA 4.0** (no dejar "U").

---

## 2. Diseño pedagógico

| Campo | Valor |
|---|---|
| Objetivo de aprendizaje | **Ordenar** correctamente los hitos del proceso por el que una entidad registra su huella de carbono en el registro del MITECO (sello *Calculo–Reduzco–Compenso*), desde el cálculo inicial hasta la obtención del sello. |
| Competencia | Alfabetización en gestión de la huella de carbono organizativa: conocer la secuencia oficial del registro MITECO y el porqué de su orden. |
| Verbo observable (Bloom) | Ordenar / Secuenciar. |
| Evidencia observable | El estudiante recorre la línea del tiempo en orden y, al cierre, **coloca 3 pares de hitos en la relación antes/después correcta** (micro-comprobación incrustada), demostrando que domina la secuencia. |
| Duración estimada | 4–6 min (microlearning: una sola idea, recorrido + comprobación breve). |
| Prerequisitos | Saber qué es la huella de carbono de una organización y la diferencia entre **reducir** y **compensar** emisiones (recomendado haber visto OA-02 *Alcances 1-2-3* y OA-08 *Mitigación vs Adaptación*). |
| Mensaje clave | El registro MITECO sigue un **orden lógico no intercambiable**: primero se **calcula** la huella, después se **reduce** (plan de reducción), luego se puede **compensar** lo no evitable, a continuación se **inscribe** la huella en el registro y, por último, se obtiene el **sello** correspondiente. *No se compensa lo que no se ha calculado, ni se sella sin inscribir.* |
| Criterio de éxito | Aciertos ≥ 2 de 3 en la micro-comprobación de orden (≈67 %) tras haber recorrido los 5 hitos de la línea del tiempo. |
| Momento de uso | Apertura / encuadre de un módulo del curso *Registro de Huella / MITECO* (da el mapa del proceso) o cierre como recapitulación del itinerario. |

---

## 3. Contenido propuesto

### 3.1. Consigna exacta (la que verá el estudiante)

> **"Recorre la línea del tiempo del registro de la huella de carbono en el MITECO. Avanza hito a hito en orden, desde el cálculo inicial hasta la obtención del sello. Al final, comprueba qué va antes y qué va después."**

### 3.2. Hitos de la línea del tiempo (eslabones, **en orden correcto**)

Cada hito es una "slide" de Timeline con su fecha/etiqueta de fase, título y texto. La **posición en la secuencia es el contenido evaluable**.

| # | Etiqueta de fase | Título del hito | Texto del hito (resumen para la slide) |
|---|---|---|---|
| 1 | Fase 1 · Punto de partida | **Calcular la huella** | La entidad mide sus emisiones de GEI. Obligatorio al menos los **Alcances 1 y 2** (combustión propia y electricidad); el **Alcance 3** suma la cadena de valor. Sin cálculo no hay nada que registrar. |
| 2 | Fase 2 · Compromiso | **Reducir las emisiones** | La entidad elabora y ejecuta un **plan de reducción** con medidas y objetivos. La reducción es prioritaria: primero se evita y se baja, no se compensa de salida. |
| 3 | Fase 3 · Lo inevitable | **Compensar (opcional)** | Las emisiones que **no se han podido reducir** pueden compensarse con **absorciones** (p. ej. proyectos forestales nacionales validados). Es voluntario y va *después* de calcular y reducir. |
| 4 | Fase 4 · Oficialización | **Inscribir en el registro MITECO** | La entidad **inscribe su huella** en el Registro de huella de carbono, compensación y proyectos de absorción del MITECO, aportando la documentación del cálculo (y, si procede, del plan de reducción). |
| 5 | Fase 5 · Reconocimiento | **Obtener el sello** | El MITECO otorga el **sello** correspondiente al nivel alcanzado: **"Calculo"**, **"Calculo y Reduzco"** o **"Calculo, Reduzco y Compenso"**. Es el resultado visible del proceso. |

> Nota de diseño: el sello es el "tres en uno" del registro MITECO; el nivel del sello depende de hasta qué hito ha llegado la entidad (de ahí que *compensar* sea opcional pero condicione el sello final).

### 3.3. Micro-comprobación de orden incrustada (autocalificable)

Como Timeline es navegable pero no califica, al final del recorrido se añade una **comprobación breve de 3 ítems "antes/después"** (vía un componente de pregunta incrustado, p. ej. Single Choice Set o True/False dentro del Column del OA). Mide la evidencia de *Ordenar*.

| Ítem | Pregunta | Opciones | Respuesta correcta | Feedback de acierto | Feedback de error |
|---|---|---|---|---|---|
| 1 | "¿Qué se hace **antes**?" | (A) Compensar emisiones · (B) **Calcular la huella** | **B — Calcular la huella** | "Correcto. No se puede compensar lo que aún no se ha medido: calcular es siempre el primer paso." | "Revisa el hito 1. Sin calcular la huella no hay dato que reducir, compensar ni registrar." |
| 2 | "¿Qué va **después** de reducir?" | (A) **Compensar lo inevitable** · (B) Volver a calcular desde cero | **A — Compensar lo inevitable** | "Correcto. Primero se reduce lo posible; lo que no se evita es lo que se compensa." | "Revisa los hitos 2 y 3. Compensar va *después* de reducir, no antes ni en su lugar." |
| 3 | "El **sello** del MITECO se obtiene…" | (A) Antes de inscribir la huella · (B) **Después de inscribirla en el registro** | **B — Después de inscribirla en el registro** | "Correcto. El sello es el último hito: primero se inscribe y luego se reconoce con el sello." | "Revisa los hitos 4 y 5. El sello llega *al final*, tras inscribir la huella en el registro." |

**Feedback global de la comprobación (rangos de puntuación previstos):**
- **3/3 (100 %):** "¡Secuencia dominada! Conoces el camino completo: Calcular → Reducir → Compensar → Inscribir → Sello."
- **2/3 (67 %, umbral de éxito):** "Bien. Tienes clara la secuencia; repasa el hito donde fallaste para afinar el orden."
- **0–1/3 (< 67 %):** "Vuelve a recorrer la línea del tiempo prestando atención al orden de los 5 hitos y reintenta."

### 3.4. Fuentes

Contenido didáctico propio de la AHC, basado en el esquema oficial del **Registro de huella de carbono, compensación y proyectos de absorción de dióxido de carbono del MITECO** y sus sellos (*Calculo / Calculo y Reduzco / Calculo, Reduzco y Compenso*). A verificar y datar por el DI antes de publicación.

---

## 4. Configuración H5P prevista

| Campo | Valor |
|---|---|
| Comportamiento | Línea del tiempo navegable con los **5 hitos en orden cronológico/lógico**; avance hito a hito (flechas anterior/siguiente) y vista general de la secuencia. Micro-comprobación de orden al final, con botón **"Comprobar"** y feedback inmediato por ítem. |
| Reintentos | **Sí** en la comprobación (`enableRetry: true`): el estudiante puede repetir la secuencia de 3 ítems hasta lograr el umbral. La línea del tiempo es re-recorrible libremente. |
| Puntuación | Timeline en sí **no puntúa** (es expositivo-navegable). La evidencia puntúa en la comprobación: **1 punto por ítem (3 puntos máx.)**, barra de puntuación visible; umbral de éxito 2/3. |
| Aleatorización | El **orden de los hitos NO se aleatoriza** (la secuencia es el contenido). En la comprobación puede barajarse el **orden de presentación de los 3 ítems** y el de las opciones A/B dentro de cada ítem, sin alterar la respuesta correcta. |
| Navegación | Lineal recomendada en primer paso (1→5); navegación libre permitida tras el primer recorrido. La comprobación aparece al cerrar la línea del tiempo. |
| Compatibilidad móvil | **Sí** (responsive). Hitos legibles en pantalla pequeña; navegación por gestos/táctil y botones grandes. Evitar textos de hito largos para no romper el layout móvil de Timeline. |

> Nota de implementación: para que el OA califique en Moodle, se recomienda envolver Timeline + comprobación en un **H5P.Column** (o equivalente), de modo que la actividad emita xAPI con la puntuación de la comprobación.

---

## 5. Accesibilidad prevista

| Campo | Valor |
|---|---|
| ALT en imágenes | Toda imagen/icono de hito llevará **texto alternativo** descriptivo (p. ej. ALT del icono del sello: "Sello del MITECO de huella de carbono"). Si un hito no tiene imagen, no se inserta decorativa sin ALT. |
| Contraste | Cumplir **contraste AA** texto/fondo en etiquetas de fase, títulos y textos de hito; no usar gris claro sobre blanco. Estado de acierto/error de la comprobación con contraste suficiente. |
| No depender solo del color | Acierto/error se indicará además con **icono y etiqueta de texto** ("Correcto" / "Revisa"), no solo con verde/rojo. |
| Navegación por teclado | Recorrido de la línea del tiempo y respuesta de la comprobación **operables por teclado** (tabulación a controles anterior/siguiente y a las opciones; foco visible). |
| Subtítulos / transcripción | El OA **no incluye vídeo ni audio** en su diseño base, por lo que no requiere subtítulos VTT ni transcripción. Si en una variante se añadiera un vídeo de hito, **deberá** llevar subtítulos VTT y transcripción. |
| Lenguaje claro | Frases cortas, una idea por hito, términos del dominio (calcular/reducir/compensar/inscribir/sello) definidos en su primer uso; evitar jerga administrativa innecesaria. |

---

## 6. Reutilización

| Campo | Valor |
|---|---|
| Cursos AHC donde insertarlo | *Registro de Huella / MITECO* (curso destino). También como **encuadre** en *Embajador Climático* (visión del proceso institucional) y como recapitulación en módulos de *huella organizativa* para empresas. |
| Qué parámetros variar | Textos de los hitos y etiquetas de fase; imágenes/iconos de cada hito; enunciados y opciones de la comprobación; textos de feedback por rango; idioma de la interfaz. |
| Qué NO cambiar | El **orden de los 5 hitos** (Calcular → Reducir → Compensar → Inscribir → Sello) y la relación *antes/después* de la comprobación: son el núcleo evaluativo del verbo *Ordenar*. |
| Variantes posibles | (a) Versión "ciudadanía"/huella personal cambiando los hitos a un itinerario doméstico (sin MITECO); (b) versión ampliada con un 6.º hito de **renovación/seguimiento anual** del sello. Cualquier variante mantiene el patrón "secuencia + comprobación de orden". |

---

## 7. Pasos para construirlo (checklist para el becario)

1. **Abrir el editor H5P** (Lumi en local, o el plugin H5P / Banco de contenido de Moodle) y crear contenido de tipo **Timeline**.
2. Poner el **título** del paquete: `OA-15: El camino de una entidad hacia el registro MITECO`.
3. Crear los **5 hitos (eventos)** de la línea del tiempo **en orden**, copiando título y texto de la tabla §3.2; asignar a cada uno su **etiqueta de fase** y una fecha/etiqueta temporal coherente con la secuencia.
4. Añadir a cada hito (opcional) un **icono o imagen** y su **texto ALT** (§5).
5. Envolver la actividad en un **H5P.Column** y añadir debajo la **micro-comprobación de orden** (3 ítems "antes/después", p. ej. Single Choice Set o 3× True/False) con las respuestas correctas y los **feedbacks** de §3.3.
6. Configurar **comportamiento** (§4): "Comprobar" y "Reintentar" activados; feedback por ítem; barajar el orden de los 3 ítems y de las opciones; **no** barajar los hitos.
7. Fijar **puntuación** de la comprobación (3 puntos máx., umbral 2/3) y los **rangos de feedback global** de §3.3.
8. Establecer **metadatos**: licencia **CC BY-NC-SA 4.0**, autoría AHC, versión **1.0.0**.
9. Probar en **escritorio y móvil**: que la línea del tiempo se recorra, que la comprobación califique y que el feedback aparezca; verificar **teclado** y **contraste**.
10. **Exportar el `.h5p`** desde el editor, nombrarlo `OA-15_Camino_registro_MITECO_v1.0.0.h5p`, dejarlo para **validación del DI** y, tras el visto bueno, subirlo al **Banco de contenido** del curso y enlazar la actividad en Moodle.
