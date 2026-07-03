# Ficha de diseño — OA-12: Primera reunión con una pyme

> **Estado: Construido y empaquetado como `.h5p`.** El escenario incluye tres decisiones y tres finales, siguiendo esta ficha. Queda pendiente la validación pedagógica final del DI.
>
> **Por qué existe esta ficha:** el plan AHC (§5, familia *Gamificación*; §7, backlog) pide ampliar la biblioteca de 10 a ≥20 OA y cubrir el bloque de **gamificación con toma de decisiones ramificada** del curso *Embajador Climático*. OA-12 aporta un **tipo H5P nuevo** en la biblioteca (Branching Scenario) y materializa el verbo Bloom **Decidir** en un escenario realista de asesoramiento a una pyme.
>
> **Coherencia verbo-formato:** el tipo **H5P.BranchingScenario (Branching Scenario)** es el formato idóneo para recoger la evidencia del verbo **Decidir** porque obliga al estudiante a **elegir un curso de acción en cada nodo y a afrontar las consecuencias de esa elección** antes de continuar. A diferencia de un test de opción múltiple (donde una respuesta se marca "correcta" y se olvida), aquí cada decisión **bifurca el itinerario**: el camino que recorre el embajador *es* la evidencia de su criterio. La decisión se vuelve **observable** (la rama tomada queda registrada vía xAPI) y **consecuencial** (el final alcanzado refleja la calidad acumulada de sus decisiones), que es exactamente lo que "Decidir" exige demostrar.

---

## 1. Identificación

| Campo | Valor |
|---|---|
| Código OA | OA-12 |
| Título | Primera reunión con una pyme |
| Tipo H5P | H5P.BranchingScenario (Branching Scenario / Escenario ramificado) |
| Familia (plan AHC §5) | Gamificación |
| Curso destino | Embajador Climático |
| Público | Embajadores y voluntariado de la AHC |
| Verbo Bloom | Decidir |
| Versión prevista | 1.0.0 |
| Licencia | Creative Commons CC BY-NC-SA 4.0 |
| Autor | Becario H5P (por asignar) |
| Revisor | Diseñador Instruccional — pendiente de validación del diseño |
| Estado | ✅ Probado en h5p.org · ⏳ Pendiente validación en Moodle |
| Archivo H5P | `OA-12_AHC_H5P_BranchingScenario_PrimeraReunionPyme_Intermedio_EmbajadorClimatico_v1.0.0.h5p` |

> Nota de trazabilidad: cuando se construya el paquete, el título interno (`h5p.json`) será "OA-12: Primera reunion con una pyme" y la licencia se fijará desde el inicio a **CC BY-NC-SA 4.0** (no se repetirá la incidencia de licencia "U" detectada en OA-08).

---

## 2. Diseño pedagógico

| Campo | Valor |
|---|---|
| Objetivo de aprendizaje | **Decidir** cómo asesorar a una pyme en su primera reunión sobre reducción de emisiones, eligiendo en cada punto la actuación más adecuada y valorando sus consecuencias para llegar a un compromiso climático realista y aceptado por la empresa. |
| Competencia | Asesoramiento climático aplicado: trasladar el conocimiento técnico (huella de carbono, alcances 1/2/3, medidas de reducción) a una conversación de negocio, adaptando el mensaje a las prioridades y limitaciones de una pyme. |
| Verbo observable (Bloom) | Decidir |
| Evidencia observable | El estudiante recorre el escenario **eligiendo una opción en cada nodo de decisión**; la secuencia de ramas tomadas y el **final alcanzado** (óptimo / aceptable / fallido) constituyen la evidencia de su criterio. Se registra vía xAPI qué decisiones tomó. |
| Duración estimada | 6–10 min (microlearning; un único recorrido completo del escenario). |
| Prerequisitos | OA-01 (conceptos climáticos básicos) y OA-02 (alcances de emisiones 1, 2 y 3); recomendable haber visto OA-08 (mitigación vs. adaptación). |
| Mensaje clave | En una primera reunión con una pyme, **escuchar y proponer un primer paso pequeño, medible y rentable** abre la puerta a la colaboración; presionar, abrumar con datos o prometer de más la cierra. |
| Criterio de éxito | Alcanzar el **final óptimo** ("La pyme firma un primer compromiso") o el **aceptable** ("La pyme acepta una segunda reunión"). Llegar al final fallido invita a reintentar y revisar las decisiones. |
| Momento de uso | Cierre del módulo de habilidades del embajador (síntesis aplicada) o actividad práctica previa a un rol-play presencial. |

---

## 3. Contenido propuesto

> Esta sección define el **escenario ramificado completo**: el nodo de inicio, los **3 nodos de decisión** principales, sus opciones con la elección **recomendada marcada**, las **consecuencias** de cada rama y los **finales**. Es contenido propuesto, a validar por el DI.

### Consigna exacta (pantalla de inicio)

> **"Eres embajador climático de la Asociación Huella de Carbono. Hoy tienes tu primera reunión con *Panadería La Espiga*, una pyme de 12 personas que quiere reducir su huella pero teme que sea caro y complicado. Cada decisión que tomes cambiará el rumbo de la conversación. Decide cómo asesorarles."**
>
> Botón de inicio: **"Entrar a la reunión »"**

### Nodo 1 — Cómo abres la reunión

**Texto del nodo:** *La gerente, Marta, te recibe algo a la defensiva: "Mira, nos interesa, pero somos pequeños y vamos justos de tiempo y dinero". ¿Cómo abres?*

| Opción | Decisión | Marcada | Consecuencia (feedback de rama) |
|---|---|:--:|---|
| A | "Escucho primero: ¿qué es lo que más os preocupa de vuestro impacto y vuestros costes?" | ✅ **Recomendada** | **Acierto.** Marta se relaja: "Sobre todo la factura de la luz y los envases". Has identificado una palanca real (energía + residuos). → va al **Nodo 2**. *Feedback:* "Bien. Escuchar antes de proponer adapta el mensaje a la pyme." |
| B | "Os traigo el cálculo completo de vuestros alcances 1, 2 y 3 con 30 indicadores." | ❌ | **Error suave.** Marta se agobia: "Eso nos supera". Pierdes confianza inicial. → va al **Nodo 2** con la empresa más reticente. *Feedback:* "Demasiados datos de golpe abruman; primero conecta con su problema." |
| C | "Si no actuáis ya, lo vais a pagar caro con las nuevas normativas." | ❌ | **Error.** El tono de amenaza la cierra: "Pues entonces ya veremos". → **Final fallido** directo. *Feedback:* "Presionar con miedo rompe la confianza en una primera reunión." |

### Nodo 2 — Qué primer paso propones

**Texto del nodo:** *Has detectado que sus mayores focos son la **energía** y los **envases**. ¿Qué primer paso le propones?*

| Opción | Decisión | Marcada | Consecuencia (feedback de rama) |
|---|---|:--:|---|
| A | "Empecemos por un solo cambio medible: cambiar a iluminación LED y tarifa con energía renovable certificada. Ahorra en la factura desde el primer mes." | ✅ **Recomendada** | **Acierto.** Un primer paso pequeño, **medible y rentable**. Marta se anima. → va al **Nodo 3**. *Feedback:* "Un paso pequeño, medible y con ahorro económico genera adhesión." |
| B | "Lo ideal sería instalar placas solares, renovar toda la maquinaria y rediseñar los envases este trimestre." | ❌ | **Error suave.** Demasiado, demasiado pronto: "No tenemos presupuesto para eso ahora". → va al **Nodo 3** con dudas de viabilidad. *Feedback:* "Proponer todo a la vez choca con el presupuesto de una pyme." |
| C | "Por ahora compensa tus emisiones comprando bonos de carbono y listo." | ❌ | **Error.** Saltarse la reducción real va contra el método AHC (primero **medir y reducir**, luego compensar). → va al **Nodo 3** con un plan débil. *Feedback:* "Compensar sin reducir antes no es una buena práctica climática." |

### Nodo 3 — Cómo cierras y aseguras continuidad

**Texto del nodo:** *Marta está interesada pero cauta: "¿Y cómo sé que esto sirve para algo?". ¿Cómo cierras la reunión?*

| Opción | Decisión | Marcada | Consecuencia (feedback de rama) |
|---|---|:--:|---|
| A | "Te dejo una hoja con 1 acción, su ahorro estimado y cómo medirla. Nos vemos en 3 semanas para revisar el primer dato." | ✅ **Recomendada** | **Acierto.** Compromiso concreto, medible y con seguimiento. → **Final óptimo** si las decisiones previas fueron acertadas. *Feedback:* "Cerrar con una acción medible y una fecha de revisión asegura continuidad." |
| B | "Te mando toda la documentación por correo y ya me dirás cuando puedas." | ➖ | **Tibio.** No hay compromiso firme ni fecha. → **Final aceptable** (segunda reunión sin garantías). *Feedback:* "Sin un siguiente paso concreto, la conversación se enfría." |
| C | "Firma hoy mismo un plan a 5 años y ya iremos viendo los detalles." | ❌ | **Error.** Pedir demasiado compromiso sin confianza ni datos. → **Final fallido**. *Feedback:* "Exigir un gran compromiso en la primera reunión espanta a la pyme." |

### Finales (pantallas de cierre)

| Final | Cómo se alcanza | Mensaje de cierre |
|---|---|---|
| **Óptimo — "La pyme firma un primer compromiso"** | Camino A → A → A (escuchar, paso pequeño medible, cierre con seguimiento). | "¡Enhorabuena! Marta firma un primer compromiso medible y agenda revisión. Has demostrado el método AHC: escuchar, proponer un paso realista y asegurar continuidad. **Decisión: sobresaliente.**" |
| **Aceptable — "La pyme acepta una segunda reunión"** | Al menos una decisión tibia/floja pero ningún error grave (p. ej. caminos con una opción B). | "La reunión deja la puerta abierta: Marta acepta verte otra vez, pero sin compromiso firme. Vas por buen camino; afina el cierre con una acción medible y una fecha. **Decisión: mejorable.**" |
| **Fallido — "La pyme se cierra"** | Cualquier opción C de presión/exceso (Nodo 1C, 2C o 3C). | "La reunión se cierra sin acuerdo. Revisa: ¿escuchaste antes de proponer? ¿el primer paso era pequeño y rentable? ¿pediste un compromiso proporcionado? **Reintenta y prueba otro enfoque.**" |

**Fuente del contenido:** material didáctico propio de la AHC (método "medir → reducir → compensar", alcances 1/2/3 y buenas prácticas de asesoramiento a pymes). Personajes y empresa (*Panadería La Espiga*, Marta) son ficticios, creados para el escenario.

---

## 4. Configuración H5P prevista

| Campo | Valor |
|---|---|
| Comportamiento | Escenario lineal-ramificado con **3 nodos de decisión** y **3 finales**. Cada opción muestra una **diapositiva de consecuencia/feedback** (Branching Question + pantalla de texto) antes de avanzar al siguiente nodo. |
| Reintentos | Sí — botón **"Reiniciar el escenario"** activado al llegar a cualquier final, especialmente para reintentar tras el final fallido. |
| Puntuación | Modo **puntuación dinámica** (`scoringOption: dynamic`): cada decisión recomendada suma puntos; las opciones C restan o llevan a final fallido. Final óptimo = puntuación máxima. La puntuación se envía a Moodle vía xAPI. Alternativa a validar con el DI: usar **finales como resultado** sin puntuación numérica (solo cualitativa). |
| Aleatorización | No procede — el orden de los nodos es fijo (la lógica de bifurcación es el contenido). El orden de las **opciones dentro de cada nodo** puede mostrarse fijo para mantener la trazabilidad A/B/C. |
| Navegación | Lineal guiada por las decisiones; **sin botón "atrás"** dentro de una rama (una decisión es una decisión). Barra de progreso del escenario activada. Botón de inicio y botón de reinicio en finales. |
| Compatibilidad móvil | Sí — Branching Scenario es responsive; las opciones son botones grandes aptos para pantalla táctil. Las imágenes de fondo (si se añaden) deben tener versión ligera para móvil. |

---

## 5. Accesibilidad prevista

| Campo | Valor |
|---|---|
| Texto ALT en imágenes | Toda imagen del escenario (foto de la panadería, retrato de Marta, iconos de decisión) llevará **ALT descriptivo**. Si una imagen es decorativa, ALT vacío (`alt=""`). |
| Contraste | Texto sobre fondo con contraste **AA mínimo (4.5:1)**; los botones de opción no dependerán solo del color para distinguirse. |
| No depender solo del color | El feedback de acierto/error se expresará con **texto y etiqueta** ("Acierto" / "Error"), no solo con verde/rojo. |
| Navegación por teclado | Las opciones de cada nodo serán **operables por teclado** (tabulación + Enter); foco visible en el botón activo. |
| Subtítulos / transcripción | El diseño base es **solo texto e imagen** (sin vídeo ni audio). Si en una versión futura se añade locución de los personajes, será obligatorio incluir **subtítulos VTT y transcripción**. |
| Lenguaje claro | Frases cortas, registro de conversación real, sin jerga técnica innecesaria; los términos técnicos (alcances, compensación) se usan en contexto comprensible. |
| Carga cognitiva | Máximo **3 opciones por nodo** y una sola decisión por pantalla, para no saturar. |

---

## 6. Reutilización

| Campo | Valor |
|---|---|
| Cursos AHC donde insertarlo | **Embajador Climático** (uso principal); reutilizable en formación de **voluntariado**, en talleres para **empresas/pymes** y como práctica previa a rol-plays presenciales. |
| Qué parámetros variar | El **sector de la pyme** (panadería → taller, comercio, restaurante…), las **palancas detectadas** (energía/residuos → movilidad/agua), los **nombres** de empresa y personaje, y el **nivel de dificultad** (añadir/retirar nodos de decisión). |
| Qué NO debe cambiarse | El núcleo evaluativo: la lógica **escuchar → paso pequeño y medible → compromiso proporcionado** que conduce al final óptimo, y la penalización de las conductas de presión/exceso/compensar-sin-reducir. |
| Variables/parámetros del OA | `branchingScenario.content` (nodos y bifurcaciones), `startScreen` (consigna inicial), `endScreens` (finales óptimo/aceptable/fallido), `scoringOption` (modo de puntuación), feedback de cada Branching Question. |
| Cursos compatibles | Cualquier itinerario AHC de habilidades de asesoramiento o sensibilización a empresas; encaja en la familia *Gamificación* del plan §5. |

---

## 7. Pasos para construirlo (checklist para el becario)

> Construir solo **después** de que el DI valide este diseño.

- [ ] Crear contenido nuevo en el **editor H5P** (Moodle Banco de contenido) o en **Lumi**, tipo **Branching Scenario**.
- [ ] Fijar en metadatos: título "OA-12: Primera reunion con una pyme", autor, y **licencia CC BY-NC-SA 4.0** desde el inicio.
- [ ] Crear la **pantalla de inicio** con la consigna exacta de la §3 y el botón "Entrar a la reunión".
- [ ] Montar el **Nodo 1** (Branching Question, 3 opciones A/B/C) y enlazar cada opción a su diapositiva de consecuencia con el feedback de la §3.
- [ ] Montar el **Nodo 2** y el **Nodo 3** del mismo modo, respetando las ramas (C de presión → final fallido).
- [ ] Crear los **3 finales** (óptimo, aceptable, fallido) con sus mensajes de cierre y el botón de **reinicio**.
- [ ] Configurar el comportamiento de la §4: puntuación dinámica, sin "atrás" en rama, barra de progreso, reinicio en finales.
- [ ] Revisar **accesibilidad** (§5): ALT en imágenes, contraste, operable por teclado, feedback con texto + color.
- [ ] Probar **todos los caminos** (al menos: A-A-A óptimo; un camino aceptable; cada C → fallido) y en **móvil**.
- [ ] **Exportar el `.h5p`**, guardarlo en el Banco de contenido del curso *Embajador Climático* y entregar al DI para validación final y publicación en Moodle.
