# Ficha — OA-19: FAQ de soporte del Campus AHC

> **Estado: Empaquetado.** El paquete `.h5p` de este OA está disponible en `03_H5P_exportables/`, generado a partir de esta ficha y verificado en un reproductor H5P. Esta ficha documenta su diseño (consigna, ítems, feedback y configuración); el contenido pedagógico queda a validación del Diseñador Instruccional (DI) como parte del control de calidad habitual.
>
> **Por qué existe esta ficha:** OA-19 procede del backlog del catálogo (sección "Pendientes recomendados") como pieza que *refuerza la familia Explicación* y cubre una necesidad real de soporte del Campus (acceso, certificados, H5P, idioma). Documentarlo antes de construirlo evita retrabajo y garantiza coherencia con el resto de la biblioteca.
>
> **Coherencia verbo-formato (obligatoria):** el tipo **H5P.Accordion (Accordion)** es el formato idóneo para recoger la evidencia del verbo **Consultar**. Consultar no exige calificación ni respuesta del usuario: exige *localizar y leer bajo demanda* la información que se necesita en el momento en que se necesita. El acordeón presenta una lista de preguntas (cabeceras plegables) y revela la respuesta solo al desplegar el panel elegido, reproduciendo de forma observable la conducta "consultar una FAQ": el usuario escanea los títulos, elige el que le afecta y lee la respuesta, sin ruido ni paneles abiertos que distraigan. Es el patrón estándar de una sección de Ayuda y, por tanto, el contenedor natural para la evidencia de "Consultar".

---

## 1. Identificación

| Campo | Valor |
|---|---|
| Código OA | OA-19 |
| Título | FAQ de soporte del Campus AHC |
| Tipo H5P | H5P.Accordion (Accordion / Acordeón) |
| Familia (plan AHC §5) | Explicación |
| Curso destino | Soporte / Campus AHC (transversal) |
| Público | Todos los perfiles (ciudadanía, empresas, embajadores, personal) |
| Verbo Bloom | Consultar |
| Versión prevista | v1.0.0 |
| Licencia | Creative Commons CC BY-NC-SA 4.0 |
| Estado | ✅ Probado en h5p.org · ⏳ Pendiente validación en Moodle |
| Archivo H5P | `OA-19_AHC_H5P_Accordion_FAQCampus_Basico_Soporte_v1.0.0.h5p` |

> Nota de trazabilidad: el título interno previsto del paquete (`h5p.json`) será "OA-19: FAQ de soporte del Campus AHC". La licencia debe declararse explícitamente como CC BY-NC-SA 4.0 al construirlo (no dejar "U" / sin especificar, como ocurrió en OA-08).

---

## 2. Diseño pedagógico

| Campo | Valor |
|---|---|
| Objetivo de aprendizaje | Consultar de forma autónoma las respuestas a las dudas más frecuentes sobre el uso del Campus AHC (acceso, certificados, contenidos H5P e idioma), localizando rápidamente el panel pertinente. |
| Competencia | Autonomía digital del estudiante: saber resolver por sí mismo incidencias básicas del entorno de formación antes de escalar a soporte humano. |
| Verbo observable (Bloom) | Consultar |
| Evidencia observable | El usuario despliega el panel de la pregunta que le afecta y lee la respuesta; la evidencia es el *acto de consulta dirigida* (abre el panel correcto para su duda), no una respuesta calificable. |
| Duración estimada | 3–6 min (lectura completa); consulta puntual < 1 min (solo el panel necesario). |
| Prerequisitos | Ninguno. Estar matriculado/registrado en el Campus AHC. Pensado como primer recurso de autoayuda. |
| Mensaje clave | Antes de abrir una incidencia, la mayoría de dudas del Campus (acceso, certificados, H5P, idioma) se resuelven en esta FAQ; cada panel da una respuesta directa y, cuando procede, el paso siguiente. |
| Criterio de éxito | El usuario encuentra y abre el panel que corresponde a su duda y obtiene la respuesta sin necesidad de contactar con soporte humano. (No hay puntuación: el éxito es resolutivo, no calificable.) |
| Momento de uso | Apertura/onboarding del curso (recurso permanente de la sección "Ayuda / Soporte") y disponible de forma transversal durante todo el itinerario. |

---

## 3. Contenido propuesto

**Consigna exacta (texto introductorio del componente, encima del acordeón):**

> "Preguntas frecuentes del Campus AHC. Pulsa sobre la pregunta que te afecte para ver la respuesta. Si tras consultarla sigues con dudas, escríbenos a soporte@huelladecarbono.org."

> **Sobre el feedback en este formato:** el Accordion **no es una actividad calificable**, no tiene botón "Comprobar" ni puntuación, así que **no existe feedback automático de acierto/error** propio del componente. La "retroalimentación" se redacta *dentro de la respuesta de cada panel* en clave resolutiva: confirmación de que está en el sitio correcto (equivalente a "acierto": "Sí, aquí lo tienes…") y una salida cuando el panel no resuelve el caso (equivalente a "error / no resuelto": "Si esto no soluciona tu caso, entonces…"). A continuación se especifican los paneles con ese doble cierre.

**Paneles del acordeón (título plegable → contenido de la respuesta):**

| # | Título del panel (pregunta) | Contenido de la respuesta (resumen redactado) | Cierre "resuelto" (acierto) | Cierre "no resuelto" (error / escalado) |
|---|---|---|---|---|
| 1 | ¿Cómo accedo al Campus AHC y qué hago si no recuerdo mi contraseña? | Entra desde *campus.huelladecarbono.org* con el correo con el que te registraste. Si no recuerdas la contraseña, pulsa "¿Olvidaste tu contraseña?" en la pantalla de acceso y sigue el enlace que recibirás por email (revisa también la carpeta de spam). | "Con el enlace del correo podrás crear una nueva contraseña y entrar de inmediato." | "Si no recibes el correo en 10 min o tu cuenta aparece bloqueada, escribe a soporte@huelladecarbono.org indicando tu nombre y correo de registro." |
| 2 | ¿Dónde encuentro y cómo descargo mi certificado del curso? | El certificado se genera automáticamente al completar el curso al 100 % y aprobar la evaluación final (OA-10). Lo encontrarás en tu *Perfil → Mis certificados*, en formato PDF descargable. | "Si has terminado y aprobado, el PDF aparece listo para descargar en tu perfil." | "Si completaste el curso pero el certificado no aparece, revisa que todas las actividades figuren como 'Finalizadas' y, si persiste, contacta con soporte indicando el nombre del curso." |
| 3 | ¿Por qué algunas actividades interactivas (H5P) no cargan o no se ven bien? | Las actividades interactivas H5P (tarjetas, arrastrar palabras, acordeones, vídeos…) requieren un navegador actualizado y JavaScript activado. Si una actividad sale en blanco: actualiza la página (F5), prueba con Chrome o Firefox actualizados y desactiva bloqueadores que puedan filtrar el contenido. | "Tras actualizar el navegador y recargar, la actividad H5P debería mostrarse y funcionar con normalidad." | "Si una actividad concreta sigue sin cargar, anota su nombre y el navegador que usas y avísanos: puede ser un fallo del paquete y lo revisaremos." |
| 4 | ¿Puedo cambiar el idioma del Campus? | El Campus AHC está disponible en español (castellano) por defecto. Puedes cambiar el idioma de la interfaz en *Perfil → Preferencias → Idioma*. Ten en cuenta que el **contenido de los cursos** (textos de las actividades) puede estar redactado solo en castellano aunque el menú aparezca traducido. | "Al guardar la preferencia, los menús del Campus se mostrarán en el idioma elegido." | "Si necesitas un curso completo en otro idioma y no está disponible, escríbenos: registramos la petición para futuras versiones." |
| 5 | He visto un error en una actividad o tengo otra duda no listada, ¿qué hago? | Para cualquier incidencia no cubierta arriba (datos erróneos en una actividad, enlaces rotos, dudas de matrícula), escribe a *soporte@huelladecarbono.org*. Indica tu nombre, el correo de registro, el curso y la actividad afectada, y una captura de pantalla si es posible. | "Con esos datos podremos reproducir el caso y responderte lo antes posible (habitualmente en 1–2 días laborables)." | "Si tu consulta es urgente o afecta a una evaluación con fecha límite, indícalo en el asunto del correo como 'URGENTE' para priorizar la respuesta." |

> **Fuente del contenido:** material de soporte propio de la AHC (procedimientos del Campus). Los datos operativos (dirección del Campus, correo de soporte, plazos) son **marcadores de ejemplo coherentes con el dominio** y deben **confirmarse con el responsable del Campus** antes de construir el paquete.

---

## 4. Configuración H5P prevista

| Campo | Valor previsto |
|---|---|
| Comportamiento | Acordeón de **5 paneles**, todos **plegados al inicio**; al desplegar uno, los demás permanecen como estén (comportamiento por defecto del componente, sin lógica de exclusión obligatoria). Texto introductorio (consigna) por encima de los paneles. |
| Reintentos | N/A — no es una actividad calificable; el usuario puede abrir y cerrar paneles las veces que quiera. |
| Puntuación | N/A — el Accordion **no registra puntuación** ni envía resultado de calificación. (Sí emite trazas xAPI de "experienced/interacted" al abrir paneles, útiles para analítica de uso, no para nota.) |
| Aleatorización | No. El orden de los paneles es **fijo e intencionado** (acceso → certificados → H5P → idioma → escalado a soporte), de lo más frecuente a lo más general. |
| Navegación | Cada cabecera es un control plegable (clic o Enter/Espacio). Lectura no lineal: el usuario va directo al panel que le interesa. Sin botones "Comprobar/Reintentar/Solución". |
| Compatibilidad móvil | Sí — el Accordion es responsive; las cabeceras se apilan y son cómodas de pulsar en pantalla táctil. Recurso pensado también para consulta rápida desde el móvil. |

---

## 5. Accesibilidad prevista

| Campo | Valor previsto |
|---|---|
| ALT en imágenes | N/A en el diseño base (sin imágenes). Si al construir se añade algún icono o captura ilustrativa en una respuesta, deberá llevar texto ALT descriptivo. |
| Subtítulos (VTT) / Transcripción | N/A — el diseño no incluye vídeo ni audio. |
| Contraste alto | Sí — usar los estilos por defecto de H5P, con contraste adecuado texto/fondo en cabeceras y paneles. |
| Navegación por teclado | Sí — el Accordion es operable por teclado: foco sobre cada cabecera con Tab y despliegue con Enter/Espacio; el componente expone los estados ARIA de expandido/colapsado para lectores de pantalla. |
| No depender solo del color | Sí — el estado abierto/cerrado se indica con el icono de flecha y el cambio de la cabecera, no solo con color. |
| Lenguaje claro | Sí — preguntas formuladas tal como las haría el usuario ("¿Cómo accedo…?"), respuestas en frases cortas, vocabulario sin jerga técnica innecesaria y pasos numerables cuando hay un procedimiento. |
| Carga cognitiva baja | Sí — una idea por panel, todos plegados al inicio para no saturar, y un orden lógico de lo más frecuente a lo más general. |

---

## 6. Reutilización

| Campo | Valor |
|---|---|
| Cursos AHC donde insertarlo | Sección "Ayuda / Soporte" de **cualquier curso** del Campus (Estrategia Climática, Huella Personal, Embajador Climático, Registro MITECO, EcoGestos, Eventos sostenibles…). Al ser transversal y no calificable, encaja como recurso permanente en todos los itinerarios. |
| Qué parámetros variar | Los **paneles** (`panels[]`): se pueden añadir, quitar o reescribir preguntas para adaptarlas a un curso concreto (p. ej. añadir una FAQ específica de "cómo registrar tu entidad en MITECO" en el curso Registro MITECO). También el **texto de la consigna** y la **dirección de soporte**. |
| Qué NO debe cambiarse | El propósito de autoayuda y el cierre con vía de escalado a soporte humano (último panel). No convertirlo en actividad calificable: rompería la coherencia verbo-formato (Consultar ≠ evaluar). |
| Variables/parámetros del OA | `title` (título), texto introductorio/consigna, `panels[]` (cada panel: `title` = pregunta + `content` = respuesta HTML). El Accordion no tiene `behaviour` de calificación que ajustar. |

---

## 7. Pasos para construirlo (checklist para el becario)

- [ ] Abrir el editor H5P (H5P.org, app **Lumi** de escritorio o el plugin de H5P en Moodle / Banco de contenido del curso).
- [ ] Crear contenido nuevo y seleccionar el tipo **Accordion** (instalarlo desde el Hub si no aparece en la lista).
- [ ] Poner el **título**: "OA-19: FAQ de soporte del Campus AHC".
- [ ] Añadir el **texto introductorio / consigna** (apartado 3) por encima de los paneles, si el curso lo requiere (puede ir como bloque de texto del propio curso o en el primer panel).
- [ ] Crear **5 paneles** ("Add panel"): en cada uno, copiar la **pregunta** como *Title* y la **respuesta** completa (incluyendo el cierre "resuelto" y el de "escalado") como *Content*, respetando el orden 1→5.
- [ ] Confirmar con el responsable del Campus los **datos operativos** (URL del Campus, correo de soporte, plazos) antes de dar por buenos los textos de ejemplo.
- [ ] Revisar **tildes y ortografía** en castellano de todos los paneles.
- [ ] En **Metadatos**: fijar la licencia a **CC BY-NC-SA 4.0**, autoría AHC y versión **v1.0.0** (no dejar la licencia como "U").
- [ ] **Previsualizar**: comprobar que los 5 paneles abren/cierran por ratón y por teclado, y que se ven bien en móvil.
- [ ] **Exportar** el paquete `.h5p` ("Reuse / Download") o guardarlo en el **Banco de contenido** del curso de Moodle.
- [ ] Entregar al **DI** para validación final antes de publicar y enlazar la actividad en la sección de Ayuda.
