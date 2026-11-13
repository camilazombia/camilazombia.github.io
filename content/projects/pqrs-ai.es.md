# PQRS con IA

## Resumen

Diseño de una experiencia de gestión de PQRS con apoyo de IA ante un gran volumen de solicitudes. La propuesta organiza prioridades y recomendaciones sin quitar a la persona la decisión sobre cada cambio.

## Rol y equipo

Mi contribución se centró en la experiencia de revisión de sugerencias, las acciones de cambio y el módulo de correo dinámico. La composición del equipo y las etapas de implementación no están documentadas.

## Contexto y problema

El volumen de solicitudes planteaba un reto de lectura, clasificación y asignación. Incorporar IA exigía una experiencia que permitiera revisar sus recomendaciones antes de aplicarlas, en lugar de presentar una clasificación automática como una decisión definitiva.

## Proceso

El alcance del proyecto fue el diseño de UI en Figma para la gestión de PQRS con IA, incluyendo pantallas de revisión de sugerencias, edición de campos y composición de correo. No se realizó investigación con usuarios.

<figure class="img-placeholder" data-ratio="16:9" data-id="pqrs-ai-01">
  <div class="img-placeholder__box">
    <img class="case-image" src="/images/gallery/pqrs-ai/pqrs-ai-01.png" alt="pqrs-ai-01" loading="lazy" decoding="async" />
    <p class="img-placeholder__prompt">Create a conceptual service task diagram connecting incoming requests, prioritization, summary, suggested classification and human review, abstract documents with no case identifiers. Style: polished product design editorial illustration with high visual detail and clean edges. Palette: navy, teal, pale lavender and warm white. Composition: balanced focal area, generous margins, 16:9 aspect ratio. Use abstract shapes instead of readable text or digits. No real logos, brand marks, personal data, actual client screenshots, or confidential material. This is a conceptual reconstruction, not evidence of a delivered screen or an actual research artifact.</p>
  </div>
  <figcaption lang="es">Diseño de UI en Figma para la gestión de PQRS con IA.</figcaption>
  <figcaption lang="en">UI design in Figma for AI-assisted PQRS management.</figcaption>
</figure>

## Decisiones clave de diseño

- Mostrar un resumen para apoyar la lectura sin presentar la síntesis como sustituto de la solicitud original.
- Separar tipo de radicado, subtipo, dependencia y responsable para revisar decisiones específicas.
- Ofrecer Cambiar en cada campo para mantener el control humano.
- Incluir Aplicar todos los cambios sugeridos como acción explícita de la persona.
- Plantear transparencia y reversibilidad como criterios de diseño; su implementación requiere comprobarse.

<figure class="img-placeholder" data-ratio="4:3" data-id="pqrs-ai-02">
  <div class="img-placeholder__box">
    <img class="case-image" src="/images/gallery/pqrs-ai/pqrs-ai-02.png" alt="pqrs-ai-02" loading="lazy" decoding="async" />
    <p class="img-placeholder__prompt">Create a conceptual desktop UI mockup of AI recommendations beside an original request panel, four recommendation rows each with a visible edit control icon and a separate grouped apply action, no legible labels. Style: polished product design editorial illustration with high visual detail and clean edges. Palette: navy, teal, pale lavender and warm white. Composition: balanced focal area, generous margins, 4:3 aspect ratio. Use abstract shapes instead of readable text or digits. No real logos, brand marks, personal data, actual client screenshots, or confidential material. This is a conceptual reconstruction, not evidence of a delivered screen or an actual research artifact.</p>
  </div>
  <figcaption lang="es">Diseño del panel de recomendaciones y sus acciones en Figma.</figcaption>
  <figcaption lang="en">Recommendations panel and action designs in Figma.</figcaption>
</figure>

## Solución

La IA organiza por prioridad, resume y recomienda clasificación y asignación. La interfaz permite cambiar cada campo o aplicar el conjunto de sugerencias. El módulo de envío incorpora correo dinámico y tokens inteligentes para componer mensajes. Los estados de confirmación y la persistencia de cambios requieren validación con la implementación.

<figure class="img-placeholder" data-ratio="16:9" data-id="pqrs-ai-03">
  <div class="img-placeholder__box">
    <img class="case-image" src="/images/gallery/pqrs-ai/pqrs-ai-03.png" alt="pqrs-ai-03" loading="lazy" decoding="async" />
    <p class="img-placeholder__prompt">Create a conceptual desktop UI mockup of a public service request priority list, distinct priority indicators and an adjacent abstract summary card, no actual citizen documents. Style: polished product design editorial illustration with high visual detail and clean edges. Palette: navy, teal, pale lavender and warm white. Composition: balanced focal area, generous margins, 16:9 aspect ratio. Use abstract shapes instead of readable text or digits. No real logos, brand marks, personal data, actual client screenshots, or confidential material. This is a conceptual reconstruction, not evidence of a delivered screen or an actual research artifact.</p>
  </div>
  <figcaption lang="es">Diseño de la lista de prioridades y el resumen de solicitudes en Figma.</figcaption>
  <figcaption lang="en">Priority list and request summary designs in Figma.</figcaption>
</figure>

<figure class="img-placeholder" data-ratio="4:3" data-id="pqrs-ai-04">
  <div class="img-placeholder__box">
    <img class="case-image" src="/images/gallery/pqrs-ai/pqrs-ai-04.png" alt="pqrs-ai-04" loading="lazy" decoding="async" />
    <p class="img-placeholder__prompt">Create a conceptual desktop UI mockup of an email composer with smart token chips, template preview and a clear review stage, empty recipient field and no actual message content. Style: polished product design editorial illustration with high visual detail and clean edges. Palette: navy, teal, pale lavender and warm white. Composition: balanced focal area, generous margins, 4:3 aspect ratio. Use abstract shapes instead of readable text or digits. No real logos, brand marks, personal data, actual client screenshots, or confidential material. This is a conceptual reconstruction, not evidence of a delivered screen or an actual research artifact.</p>
  </div>
  <figcaption lang="es">Diseño del compositor de correo con tokens inteligentes en Figma.</figcaption>
  <figcaption lang="en">Email composer design with smart tokens in Figma.</figcaption>
</figure>

## Resultados y aprendizajes

El entregable es una propuesta de gestión asistida que vincula recomendaciones con controles de revisión y composición de correo. No se dispone de mediciones de precisión, carga operativa o tiempo de respuesta. El aprendizaje es que una recomendación útil también debe ser comprensible y corregible.

[DATO PENDIENTE: PQ-01 | evidencia de reversión y evaluación de recomendaciones].

<figure class="img-placeholder" data-ratio="16:9" data-id="pqrs-ai-05">
  <div class="img-placeholder__box">
    <img class="case-image" src="/images/gallery/pqrs-ai/pqrs-ai-05.png" alt="pqrs-ai-05" loading="lazy" decoding="async" />
    <p class="img-placeholder__prompt">Create a conceptual conceptual interaction diagram comparing an AI suggestion, a human modification and a proposed undo review state, reversibility shown as a design intention rather than implemented proof. Style: polished product design editorial illustration with high visual detail and clean edges. Palette: navy, teal, pale lavender and warm white. Composition: balanced focal area, generous margins, 16:9 aspect ratio. Use abstract shapes instead of readable text or digits. No real logos, brand marks, personal data, actual client screenshots, or confidential material. This is a conceptual reconstruction, not evidence of a delivered screen or an actual research artifact.</p>
  </div>
  <figcaption lang="es">Diseño de las interfaces para revisar y editar sugerencias de IA en Figma.</figcaption>
  <figcaption lang="en">Interface designs for reviewing and editing AI suggestions in Figma.</figcaption>
</figure>

## Cierre

La IA sugiere y la persona decide. Ese principio guía la presentación de recomendaciones y las acciones disponibles, sin afirmar autonomía del sistema.
