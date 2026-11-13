# Appointment scheduling

## Summary

A scheduling platform design for Hacienda. The proposal connects appointment requests with schedule management and distinguishes the responsibilities of administrators, coordinators, and agents.

## Role and team

I worked on flows, interfaces, and system behavior definitions, including scheduling rules and permissions by role. A complete team breakdown is not available.

## Context and problem

The process was fragmented: an Excel file was sent to a provider to enable availability, the request form had usability issues, and a separate Teams calendar lacked detail. This separation made it difficult to understand the service from configuration through appointment handling.

## Process

The project scope was UI design in Figma for an appointment scheduling platform, including role-based management screens and a request form. No user research was conducted.

<figure class="img-placeholder" data-ratio="16:9" data-id="hacienda-citas-01">
  <div class="img-placeholder__box">
    <img class="case-image" src="/images/gallery/hacienda-citas/hacienda-citas-01.png" alt="hacienda-citas-01" loading="lazy" decoding="async" />
    <p class="img-placeholder__prompt">Create a conceptual service flow diagram contrasting scattered spreadsheet, request form and calendar icons with a unified scheduling platform, no client screenshots or internal details. Style: polished product design editorial illustration with high visual detail and clean edges. Palette: deep blue, teal, warm white and neutral gray. Composition: balanced focal area, generous margins, 16:9 aspect ratio. Use abstract shapes instead of readable text or digits. No real logos, brand marks, personal data, actual client screenshots, or confidential material. This is a conceptual reconstruction, not evidence of a delivered screen or an actual research artifact.</p>
  </div>
  <figcaption lang="es">Diseño de UI en Figma para la plataforma de agendamiento de citas.</figcaption>
  <figcaption lang="en">UI design in Figma for the appointment scheduling platform.</figcaption>
</figure>

## Key design decisions

- Distinguish administrators, coordinators, and agents to clarify responsibility.
- Give the administrator overall control, including email, to configure the service.
- Provide coordinators with an office-specific dashboard to keep management grounded in their operation.
- Design dynamic schedules where adding a block adjusts the others to account for the whole schedule.
- Define request limits as system rules so the form does not rely on implicit decisions.

<figure class="img-placeholder" data-ratio="4:3" data-id="hacienda-citas-02">
  <div class="img-placeholder__box">
    <img class="case-image" src="/images/gallery/hacienda-citas/hacienda-citas-02.png" alt="hacienda-citas-02" loading="lazy" decoding="async" />
    <p class="img-placeholder__prompt">Create a conceptual role responsibility diagram with administrator, office coordinator and agent represented by generic icons connected to separate permission groups, agent details abstract. Style: polished product design editorial illustration with high visual detail and clean edges. Palette: deep blue, teal, warm white and neutral gray. Composition: balanced focal area, generous margins, 4:3 aspect ratio. Use abstract shapes instead of readable text or digits. No real logos, brand marks, personal data, actual client screenshots, or confidential material. This is a conceptual reconstruction, not evidence of a delivered screen or an actual research artifact.</p>
  </div>
  <figcaption lang="es">Diseño de las interfaces para los perfiles de la plataforma en Figma.</figcaption>
  <figcaption lang="en">Interface designs for the platform roles in Figma.</figcaption>
</figure>

## Solution

The proposal includes an appointment request form, an administrator profile controlling email and scheduling rules, and an office dashboard where coordinators create dynamic schedules. The agent is part of the role model; detailed permissions still need confirmation.

<figure class="img-placeholder" data-ratio="16:9" data-id="hacienda-citas-03">
  <div class="img-placeholder__box">
    <img class="case-image" src="/images/gallery/hacienda-citas/hacienda-citas-03.png" alt="hacienda-citas-03" loading="lazy" decoding="async" />
    <p class="img-placeholder__prompt">Create a conceptual desktop UI mockup of an office scheduling dashboard with abstract appointment distribution, availability cards and a clearly bounded office workspace. Style: polished product design editorial illustration with high visual detail and clean edges. Palette: deep blue, teal, warm white and neutral gray. Composition: balanced focal area, generous margins, 16:9 aspect ratio. Use abstract shapes instead of readable text or digits. No real logos, brand marks, personal data, actual client screenshots, or confidential material. This is a conceptual reconstruction, not evidence of a delivered screen or an actual research artifact.</p>
  </div>
  <figcaption lang="es">Diseño de UI del panel de gestión de citas en Figma.</figcaption>
  <figcaption lang="en">UI design of the appointment management dashboard in Figma.</figcaption>
</figure>

<figure class="img-placeholder" data-ratio="4:3" data-id="hacienda-citas-04">
  <div class="img-placeholder__box">
    <img class="case-image" src="/images/gallery/hacienda-citas/hacienda-citas-04.png" alt="hacienda-citas-04" loading="lazy" decoding="async" />
    <p class="img-placeholder__prompt">Create a conceptual desktop UI sequence in three panels showing a dynamic appointment schedule before adding a time block, during insertion and after neighboring blocks adjust, no timestamps. Style: polished product design editorial illustration with high visual detail and clean edges. Palette: deep blue, teal, warm white and neutral gray. Composition: balanced focal area, generous margins, 4:3 aspect ratio. Use abstract shapes instead of readable text or digits. No real logos, brand marks, personal data, actual client screenshots, or confidential material. This is a conceptual reconstruction, not evidence of a delivered screen or an actual research artifact.</p>
  </div>
  <figcaption lang="es">Diseño de la interfaz de agenda y sus estados en Figma.</figcaption>
  <figcaption lang="en">Schedule interface and state designs in Figma.</figcaption>
</figure>

## Outcomes and learnings

Previously, the workflow relied on provider-bound files, a form, and a separate calendar. The design brings those needs into a platform proposal with defined roles and scheduling behavior. This is a design deliverable, not a confirmed deployment or measured time saving. The main takeaway is to treat rules and permissions as a core part of the experience.

[DATO PENDIENTE: HC-01 | confirmation of agent permissions and implementation status].

<figure class="img-placeholder" data-ratio="16:9" data-id="hacienda-citas-05">
  <div class="img-placeholder__box">
    <img class="case-image" src="/images/gallery/hacienda-citas/hacienda-citas-05.png" alt="hacienda-citas-05" loading="lazy" decoding="async" />
    <p class="img-placeholder__prompt">Create a conceptual paired mobile and desktop UI mockup for a public appointment request form with clear field grouping, a generic availability selector and confirmation state, no filled personal fields. Style: polished product design editorial illustration with high visual detail and clean edges. Palette: deep blue, teal, warm white and neutral gray. Composition: balanced focal area, generous margins, 16:9 aspect ratio. Use abstract shapes instead of readable text or digits. No real logos, brand marks, personal data, actual client screenshots, or confidential material. This is a conceptual reconstruction, not evidence of a delivered screen or an actual research artifact.</p>
  </div>
  <figcaption lang="es">Diseño de UI del formulario de solicitud de citas en Figma.</figcaption>
  <figcaption lang="en">UI design of the appointment request form in Figma.</figcaption>
</figure>

## Closing

The case makes service logic visible to both the people managing appointments and those requesting them. Visual examples will use fictional information.
