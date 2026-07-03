# Guía breve de reutilización — Biblioteca H5P AHC

> Para docentes, tutores y diseñadores instruccionales del Campus AHC.
> Explica cómo localizar, subir, adaptar y versionar los Objetos de Aprendizaje (OA) H5P
> sin rehacerlos desde cero.

## 1. Qué es esta biblioteca
Un conjunto de **20 OA H5P terminados**, breves, accesibles y modulares, listos para
insertarse en cualquier curso Moodle del Campus AHC. Cada OA incluye su archivo `.h5p`, su ficha
documental y su registro en el catálogo.

## 2. Cómo localizar un OA
1. Abre `01_Catalogo_general/Catalogo_H5P.md` y busca por tema, tipo H5P o curso.
2. Anota el **código** (OA-XX) y el **nombre de archivo** oficial.
3. El paquete está en `03_H5P_exportables/`; su ficha completa en `02_Fichas_OA/OA-XX_Ficha.md`.

## 3. Nomenclatura oficial (para no perderse)
```
AHC_H5P_[Tipo]_[Tema]_[Nivel]_[Curso]_[vX.Y.Z].h5p
```
Ejemplo: `AHC_H5P_DragDrop_AlcancesEmisiones_Intermedio_MedicionEmisiones_v1.0.0.h5p`
- **[Tipo]**: tipo de contenido H5P (DragDrop, DialogCards, ImageHotspots…).
- **[Tema]/[Nivel]/[Curso]**: para qué temática, nivel y curso está pensado.
- **[vX.Y.Z]**: versión semántica.

## 4. Subir un OA a Moodle (resumen)
1. Curso destino → **Banco de contenido H5P**.
2. Sube el `.h5p` (o créalo desde el banco) usando la nomenclatura oficial.
3. Completa título, descripción, **licencia (CC BY-NC-SA 4.0)**, autoría, etiquetas y versión.
4. Inserta el H5P como **actividad H5P** (si quieres calificación) o como **recurso** (solo práctica).
5. Configura la **finalización** (visualización, intento o nota mínima).
6. Prueba como **estudiante** en escritorio y móvil (navegación, reintentos, calificación, feedback).
7. Registra en el catálogo el enlace Moodle, la captura y el estado.

## 5. Adaptar un OA a otro curso
- Consulta el bloque **Reutilización** de la ficha: indica *qué se puede adaptar* y *qué no debe cambiarse*.
- Si solo cambias contexto/etiquetas: reutiliza el mismo paquete.
- Si cambias **contenido** (preguntas, textos, imágenes):
  1. Duplica la ficha e indica el nuevo contexto.
  2. Crea una nueva versión **MINOR** (p. ej. `v1.1.0`).
  3. Vuelve a pasar el checklist de calidad y el de accesibilidad antes de publicar.

## 6. Versionado (SemVer)
- **PATCH** (v1.0.**1**): corrección menor (errata, feedback, ALT) sin cambiar el aprendizaje.
- **MINOR** (v1.**1**.0): nuevo contenido o adaptación a otro curso, compatible.
- **MAJOR** (**2**.0.0): rediseño del OA o cambio de objetivo/evidencia.

## 7. Antes de dar por bueno un OA
Pasa siempre los dos checklists de `06_Revisiones_DI/`:
- `Checklist_Calidad_QA.md`
- `Checklist_Accesibilidad.md`

## 8. Principio rector AHC
> **La IA propone, el Diseñador Instruccional decide.** La herramienta acelera borradores, distractores,
> feedback y ALT, pero el objetivo, el formato definitivo y la publicación los valida el DI y el
> responsable de formación.
