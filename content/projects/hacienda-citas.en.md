# Appointment scheduling

## Summary

A scheduling platform design for Hacienda. The proposal connects appointment requests with schedule management and distinguishes the responsibilities of administrators, coordinators, and agents.

## Role and team

I worked on flows, interfaces, and system behavior definitions, including scheduling rules and permissions by role. A complete team breakdown is not available.

## Context and problem

The process was fragmented: an Excel file was sent to a provider to enable availability, the request form had usability issues, and a separate Teams calendar lacked detail. This separation made it difficult to understand the service from configuration through appointment handling.

## Process

Using the described existing workflows, I defined a platform structure with role-based management and a request form. The design work specified rules, limits, and dynamic schedule behavior. User testing, deployment, and operational outcomes are not claimed without supporting evidence.

<figure class="img-placeholder" data-ratio="16:9" data-id="hacienda-citas-01">
  <div class="img-placeholder__box">
    <p class="img-placeholder__prompt">Create a conceptual service flow diagram contrasting scattered spreadsheet, request form and calendar icons with a unified scheduling platform, no client screenshots or internal details. Style: polished product design editorial illustration with high visual detail and clean edges. Palette: deep blue, teal, warm white and neutral gray. Composition: balanced focal area, generous margins, 16:9 aspect ratio. Use abstract shapes instead of readable text or digits. No real logos, brand marks, personal data, actual client screenshots, or confidential material. This is a conceptual reconstruction, not evidence of a delivered screen or an actual research artifact.</p>
  </div>
  <figcaption lang="es">Diagrama conceptual del proceso fragmentado y la propuesta integrada.</figcaption>
  <figcaption lang="en">Conceptual diagram of the fragmented workflow and integrated proposal.</figcaption>
</figure>

## Key design decisions

- Distinguish administrators, coordinators, and agents to clarify responsibility.
- Give the administrator overall control, including email, to configure the service.
- Provide coordinators with an office-specific dashboard to keep management grounded in their operation.
- Design dynamic schedules where adding a block adjusts the others to account for the whole schedule.
- Define request limits as system rules so the form does not rely on implicit decisions.

<figure class="img-placeholder" data-ratio="4:3" data-id="hacienda-citas-02">
  <div class="img-placeholder__box">
    <p class="img-placeholder__prompt">Create a conceptual role responsibility diagram with administrator, office coordinator and agent represented by generic icons connected to separate permission groups, agent details abstract. Style: polished product design editorial illustration with high visual detail and clean edges. Palette: deep blue, teal, warm white and neutral gray. Composition: balanced focal area, generous margins, 4:3 aspect ratio. Use abstract shapes instead of readable text or digits. No real logos, brand marks, personal data, actual client screenshots, or confidential material. This is a conceptual reconstruction, not evidence of a delivered screen or an actual research artifact.</p>
  </div>
  <figcaption lang="es">Mapa conceptual de roles; los permisos detallados del agente están pendientes.</figcaption>
  <figcaption lang="en">Conceptual role map; detailed agent permissions remain pending.</figcaption>
</figure>

## Solution

The proposal includes an appointment request form, an administrator profile controlling email and scheduling rules, and an office dashboard where coordinators create dynamic schedules. The agent is part of the role model; detailed permissions still need confirmation.

<figure class="img-placeholder" data-ratio="16:9" data-id="hacienda-citas-03">
  <div class="img-placeholder__box">
    <p class="img-placeholder__prompt">Create a conceptual desktop UI mockup of an office scheduling dashboard with abstract appointment distribution, availability cards and a clearly bounded office workspace. Style: polished product design editorial illustration with high visual detail and clean edges. Palette: deep blue, teal, warm white and neutral gray. Composition: balanced focal area, generous margins, 16:9 aspect ratio. Use abstract shapes instead of readable text or digits. No real logos, brand marks, personal data, actual client screenshots, or confidential material. This is a conceptual reconstruction, not evidence of a delivered screen or an actual research artifact.</p>
  </div>
  <figcaption lang="es">Dashboard conceptual del coordinador de sede. Datos ilustrativos.</figcaption>
  <figcaption lang="en">Conceptual office coordinator dashboard. Illustrative data.</figcaption>
</figure>

<figure class="img-placeholder" data-ratio="4:3" data-id="hacienda-citas-04">
  <div class="img-placeholder__box">
    <p class="img-placeholder__prompt">Create a conceptual desktop UI sequence in three panels showing a dynamic appointment schedule before adding a time block, during insertion and after neighboring blocks adjust, no timestamps. Style: polished product design editorial illustration with high visual detail and clean edges. Palette: deep blue, teal, warm white and neutral gray. Composition: balanced focal area, generous margins, 4:3 aspect ratio. Use abstract shapes instead of readable text or digits. No real logos, brand marks, personal data, actual client screenshots, or confidential material. This is a conceptual reconstruction, not evidence of a delivered screen or an actual research artifact.</p>
  </div>
  <figcaption lang="es">Secuencia conceptual del ajuste de bloques en una agenda dinámica.</figcaption>
  <figcaption lang="en">Conceptual sequence of block adjustment in a dynamic schedule.</figcaption>
</figure>

## Outcomes and learnings

Previously, the workflow relied on provider-bound files, a form, and a separate calendar. The design brings those needs into a platform proposal with defined roles and scheduling behavior. This is a design deliverable, not a confirmed deployment or measured time saving. The main takeaway is to treat rules and permissions as a core part of the experience.

[DATO PENDIENTE: HC-01 | confirmation of agent permissions and implementation status].

<figure class="img-placeholder" data-ratio="16:9" data-id="hacienda-citas-05">
  <div class="img-placeholder__box">
    <p class="img-placeholder__prompt">Create a conceptual paired mobile and desktop UI mockup for a public appointment request form with clear field grouping, a generic availability selector and confirmation state, no filled personal fields. Style: polished product design editorial illustration with high visual detail and clean edges. Palette: deep blue, teal, warm white and neutral gray. Composition: balanced focal area, generous margins, 16:9 aspect ratio. Use abstract shapes instead of readable text or digits. No real logos, brand marks, personal data, actual client screenshots, or confidential material. This is a conceptual reconstruction, not evidence of a delivered screen or an actual research artifact.</p>
  </div>
  <figcaption lang="es">Formulario conceptual de solicitud de citas con información ficticia.</figcaption>
  <figcaption lang="en">Conceptual appointment request form using fictional information.</figcaption>
</figure>

## Closing

The case makes service logic visible to both the people managing appointments and those requesting them. Visual examples will use fictional information.
