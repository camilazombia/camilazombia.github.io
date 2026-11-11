# AI-assisted PQRS

## Summary

An AI-assisted PQRS management experience designed for a high volume of requests. The proposal organizes priorities and recommendations while leaving each change under human control.

## Role and team

My contribution focused on reviewing suggestions, changing individual fields, and composing dynamic emails. Team composition and implementation stages are not documented.

## Context and problem

Request volume created a challenge for reading, classification, and assignment. Introducing AI called for an experience where people could examine recommendations before applying them, rather than treating an automated classification as final.

## Process

I organized the experience around the described tasks: prioritize, understand a request, review its classification, and assign responsibility. The design connected recommendations with field-level controls and a combined action. Model training, accuracy testing, and impact validation are not claimed.

<figure class="img-placeholder" data-ratio="16:9" data-id="pqrs-ai-01">
  <div class="img-placeholder__box">
    <p class="img-placeholder__prompt">Create a conceptual service task diagram connecting incoming requests, prioritization, summary, suggested classification and human review, abstract documents with no case identifiers. Style: polished product design editorial illustration with high visual detail and clean edges. Palette: navy, teal, pale lavender and warm white. Composition: balanced focal area, generous margins, 16:9 aspect ratio. Use abstract shapes instead of readable text or digits. No real logos, brand marks, personal data, actual client screenshots, or confidential material. This is a conceptual reconstruction, not evidence of a delivered screen or an actual research artifact.</p>
  </div>
  <figcaption lang="es">Diagrama conceptual de priorización y revisión humana.</figcaption>
  <figcaption lang="en">Conceptual diagram of prioritization and human review.</figcaption>
</figure>

## Key design decisions

- Present a summary to support reading without treating it as a replacement for the original request.
- Separate case type, subtype, department, and assignee for focused review.
- Offer Change for every field to retain human control.
- Make Apply all suggested changes an explicit user action.
- Treat transparency and reversibility as design criteria whose implementation still needs verification.

<figure class="img-placeholder" data-ratio="4:3" data-id="pqrs-ai-02">
  <div class="img-placeholder__box">
    <p class="img-placeholder__prompt">Create a conceptual desktop UI mockup of AI recommendations beside an original request panel, four recommendation rows each with a visible edit control icon and a separate grouped apply action, no legible labels. Style: polished product design editorial illustration with high visual detail and clean edges. Palette: navy, teal, pale lavender and warm white. Composition: balanced focal area, generous margins, 4:3 aspect ratio. Use abstract shapes instead of readable text or digits. No real logos, brand marks, personal data, actual client screenshots, or confidential material. This is a conceptual reconstruction, not evidence of a delivered screen or an actual research artifact.</p>
  </div>
  <figcaption lang="es">Panel conceptual de recomendaciones con controles individuales y acción conjunta.</figcaption>
  <figcaption lang="en">Conceptual recommendations panel with individual controls and a combined action.</figcaption>
</figure>

## Solution

AI prioritizes requests, summarizes them, and recommends classification and assignment. People can change each field or apply the suggestions together. The sending module uses dynamic email and smart tokens to compose messages. Confirmation states and change persistence need to be checked against the implementation.

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

## Outcomes and learnings

The deliverable is an assisted management proposal that connects recommendations with review controls and email composition. Accuracy, workload, and response-time measurements are not available. The takeaway is that a useful recommendation must also be understandable and correctable.

[DATO PENDIENTE: PQ-01 | evidence of reversal behavior and recommendation evaluation].

<figure class="img-placeholder" data-ratio="16:9" data-id="pqrs-ai-05">
  <div class="img-placeholder__box">
    <p class="img-placeholder__prompt">Create a conceptual conceptual interaction diagram comparing an AI suggestion, a human modification and a proposed undo review state, reversibility shown as a design intention rather than implemented proof. Style: polished product design editorial illustration with high visual detail and clean edges. Palette: navy, teal, pale lavender and warm white. Composition: balanced focal area, generous margins, 16:9 aspect ratio. Use abstract shapes instead of readable text or digits. No real logos, brand marks, personal data, actual client screenshots, or confidential material. This is a conceptual reconstruction, not evidence of a delivered screen or an actual research artifact.</p>
  </div>
  <figcaption lang="es">Esquema conceptual de control humano; reversión pendiente de verificar.</figcaption>
  <figcaption lang="en">Conceptual human oversight diagram; reversal behavior remains unverified.</figcaption>
</figure>

## Closing

AI suggests; a person decides. This principle guides how recommendations and controls are presented without claiming autonomous decision-making.
