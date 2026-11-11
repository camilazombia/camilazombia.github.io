# PQRS con IA

## Resumen

Diseño de una experiencia de gestión de PQRS con apoyo de IA ante un gran volumen de solicitudes. La propuesta organiza prioridades y recomendaciones sin quitar a la persona la decisión sobre cada cambio.

## Rol y equipo

Mi contribución se centró en la experiencia de revisión de sugerencias, las acciones de cambio y el módulo de correo dinámico. La composición del equipo y las etapas de implementación no están documentadas.

## Contexto y problema

El volumen de solicitudes planteaba un reto de lectura, clasificación y asignación. Incorporar IA exigía una experiencia que permitiera revisar sus recomendaciones antes de aplicarlas, en lugar de presentar una clasificación automática como una decisión definitiva.

## Proceso

Definí la experiencia alrededor de las tareas descritas: priorizar, comprender la solicitud, revisar su clasificación y asignar responsabilidad. El diseño conectó las sugerencias con controles por campo y una acción conjunta. No se atribuyen al trabajo entrenamiento del modelo, pruebas de precisión o validación de impacto.

<figure class="img-placeholder" data-ratio="16:9" data-id="pqrs-ai-01">
  <div class="img-placeholder__box">
    <p class="img-placeholder__prompt">Create a conceptual service task diagram connecting incoming requests, prioritization, summary, suggested classification and human review, abstract documents with no case identifiers. Style: polished product design editorial illustration with high visual detail and clean edges. Palette: navy, teal, pale lavender and warm white. Composition: balanced focal area, generous margins, 16:9 aspect ratio. Use abstract shapes instead of readable text or digits. No real logos, brand marks, personal data, actual client screenshots, or confidential material. This is a conceptual reconstruction, not evidence of a delivered screen or an actual research artifact.</p>
  </div>
  <figcaption lang="es">Diagrama conceptual de priorización y revisión humana.</figcaption>
  <figcaption lang="en">Conceptual diagram of prioritization and human review.</figcaption>
</figure>

## Decisiones clave de diseño

- Mostrar un resumen para apoyar la lectura sin presentar la síntesis como sustituto de la solicitud original.
- Separar tipo de radicado, subtipo, dependencia y responsable para revisar decisiones específicas.
- Ofrecer Cambiar en cada campo para mantener el control humano.
- Incluir Aplicar todos los cambios sugeridos como acción explícita de la persona.
- Plantear transparencia y reversibilidad como criterios de diseño; su implementación requiere comprobarse.

<figure class="img-placeholder" data-ratio="4:3" data-id="pqrs-ai-02">
  <div class="img-placeholder__box">
    <p class="img-placeholder__prompt">Create a conceptual desktop UI mockup of AI recommendations beside an original request panel, four recommendation rows each with a visible edit control icon and a separate grouped apply action, no legible labels. Style: polished product design editorial illustration with high visual detail and clean edges. Palette: navy, teal, pale lavender and warm white. Composition: balanced focal area, generous margins, 4:3 aspect ratio. Use abstract shapes instead of readable text or digits. No real logos, brand marks, personal data, actual client screenshots, or confidential material. This is a conceptual reconstruction, not evidence of a delivered screen or an actual research artifact.</p>
  </div>
  <figcaption lang="es">Panel conceptual de recomendaciones con controles individuales y acción conjunta.</figcaption>
  <figcaption lang="en">Conceptual recommendations panel with individual controls and a combined action.</figcaption>
</figure>

## Solución

La IA organiza por prioridad, resume y recomienda clasificación y asignación. La interfaz permite cambiar cada campo o aplicar el conjunto de sugerencias. El módulo de envío incorpora correo dinámico y tokens inteligentes para componer mensajes. Los estados de confirmación y la persistencia de cambios requieren validación con la implementación.

<figure class="img-placeholder" data-ratio="16:9" data-id="pqrs-ai-03">
  <div class="img-placeholder__box">
    <p class="img-placeholder__prompt">Create a conceptual desktop UI mockup of a public service request priority list, distinct priority indicators and an adjacent abstract summary card, no actual citizen documents. Style: polished product design editorial illustration with high visual detail and clean edges. Palette: navy, teal, pale lavender and warm white. Composition: balanced focal area, generous margins, 16:9 aspect ratio. Use abstract shapes instead of readable text or digits. No real logos, brand marks, personal data, actual client screenshots, or confidential material. This is a conceptual reconstruction, not evidence of a delivered screen or an actual research artifact.</p>
  </div>
  <figcaption lang="es">Lista conceptual de prioridades y resumen de solicitudes. Datos ilustrativos.</figcaption>
  <figcaption lang="en">Conceptual request priority list and summary. Illustrative data.</figcaption>
</figure>

<figure class="img-placeholder" data-ratio="4:3" data-id="pqrs-ai-04">
  <div class="img-placeholder__box">
    <p class="img-placeholder__prompt">Create a conceptual desktop UI mockup of an email composer with smart token chips, template preview and a clear review stage, empty recipient field and no actual message content. Style: polished product design editorial illustration with high visual detail and clean edges. Palette: navy, teal, pale lavender and warm white. Composition: balanced focal area, generous margins, 4:3 aspect ratio. Use abstract shapes instead of readable text or digits. No real logos, brand marks, personal data, actual client screenshots, or confidential material. This is a conceptual reconstruction, not evidence of a delivered screen or an actual research artifact.</p>
  </div>
  <figcaption lang="es">Compositor conceptual de correo dinámico con tokens inteligentes.</figcaption>
  <figcaption lang="en">Conceptual dynamic email composer with smart tokens.</figcaption>
</figure>

## Resultados y aprendizajes

El entregable es una propuesta de gestión asistida que vincula recomendaciones con controles de revisión y composición de correo. No se dispone de mediciones de precisión, carga operativa o tiempo de respuesta. El aprendizaje es que una recomendación útil también debe ser comprensible y corregible.

[DATO PENDIENTE: PQ-01 | evidencia de reversión y evaluación de recomendaciones].

<figure class="img-placeholder" data-ratio="16:9" data-id="pqrs-ai-05">
  <div class="img-placeholder__box">
    <p class="img-placeholder__prompt">Create a conceptual conceptual interaction diagram comparing an AI suggestion, a human modification and a proposed undo review state, reversibility shown as a design intention rather than implemented proof. Style: polished product design editorial illustration with high visual detail and clean edges. Palette: navy, teal, pale lavender and warm white. Composition: balanced focal area, generous margins, 16:9 aspect ratio. Use abstract shapes instead of readable text or digits. No real logos, brand marks, personal data, actual client screenshots, or confidential material. This is a conceptual reconstruction, not evidence of a delivered screen or an actual research artifact.</p>
  </div>
  <figcaption lang="es">Esquema conceptual de control humano; reversión pendiente de verificar.</figcaption>
  <figcaption lang="en">Conceptual human oversight diagram; reversal behavior remains unverified.</figcaption>
</figure>

## Cierre

La IA sugiere y la persona decide. Ese principio guía la presentación de recomendaciones y las acciones disponibles, sin afirmar autonomía del sistema.
