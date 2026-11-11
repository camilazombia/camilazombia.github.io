# Agendamiento de citas

## Resumen

Diseño de una plataforma de agendamiento para Hacienda. La propuesta reúne la solicitud de citas y la gestión operativa de agendas, con responsabilidades diferenciadas para administrador, coordinador y agente.

## Rol y equipo

Trabajé en los flujos, las interfaces y las definiciones de comportamiento del sistema. El alcance incluyó reglas de agendamiento y permisos por perfil. No se cuenta con el detalle completo del equipo.

## Contexto y problema

El proceso estaba fragmentado: se enviaba un Excel al proveedor para habilitar la agenda, el formulario de solicitud presentaba problemas de experiencia de uso y el calendario en Teams no mostraba suficiente detalle. Esta separación dificultaba entender el proceso completo desde la configuración hasta la atención.

## Proceso

Partí de los flujos existentes descritos y definí la estructura de una plataforma con gestión por perfiles y un formulario de solicitud. El trabajo de diseño precisó reglas, límites y comportamiento de las agendas dinámicas. No se afirman pruebas con usuarios, despliegue o resultados operativos que no estén documentados.

<figure class="img-placeholder" data-ratio="16:9" data-id="hacienda-citas-01">
  <div class="img-placeholder__box">
    <p class="img-placeholder__prompt">Create a conceptual service flow diagram contrasting scattered spreadsheet, request form and calendar icons with a unified scheduling platform, no client screenshots or internal details. Style: polished product design editorial illustration with high visual detail and clean edges. Palette: deep blue, teal, warm white and neutral gray. Composition: balanced focal area, generous margins, 16:9 aspect ratio. Use abstract shapes instead of readable text or digits. No real logos, brand marks, personal data, actual client screenshots, or confidential material. This is a conceptual reconstruction, not evidence of a delivered screen or an actual research artifact.</p>
  </div>
  <figcaption lang="es">Diagrama conceptual del proceso fragmentado y la propuesta integrada.</figcaption>
  <figcaption lang="en">Conceptual diagram of the fragmented workflow and integrated proposal.</figcaption>
</figure>

## Decisiones clave de diseño

- Separar administrador, coordinador y agente para hacer explícita la responsabilidad de cada perfil.
- Concentrar el control general, incluido el correo, en el administrador para definir la configuración del servicio.
- Dar al coordinador una vista de su sede para situar la gestión en su contexto operativo.
- Diseñar agendas dinámicas en las que agregar un bloque ajuste los demás para contemplar el comportamiento conjunto del horario.
- Definir límites de solicitudes como reglas del sistema para evitar decisiones implícitas en el formulario.

<figure class="img-placeholder" data-ratio="4:3" data-id="hacienda-citas-02">
  <div class="img-placeholder__box">
    <p class="img-placeholder__prompt">Create a conceptual role responsibility diagram with administrator, office coordinator and agent represented by generic icons connected to separate permission groups, agent details abstract. Style: polished product design editorial illustration with high visual detail and clean edges. Palette: deep blue, teal, warm white and neutral gray. Composition: balanced focal area, generous margins, 4:3 aspect ratio. Use abstract shapes instead of readable text or digits. No real logos, brand marks, personal data, actual client screenshots, or confidential material. This is a conceptual reconstruction, not evidence of a delivered screen or an actual research artifact.</p>
  </div>
  <figcaption lang="es">Mapa conceptual de roles; los permisos detallados del agente están pendientes.</figcaption>
  <figcaption lang="en">Conceptual role map; detailed agent permissions remain pending.</figcaption>
</figure>

## Solución

La propuesta incluye un formulario de solicitud de citas, un perfil administrador con control total y configuración de correo y reglas, y un dashboard del coordinador para su sede con creación de agendas dinámicas. El perfil agente forma parte del modelo de roles; sus permisos detallados requieren confirmación.

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

## Resultados y aprendizajes

Antes, la operación dependía de archivos enviados al proveedor, un formulario y un calendario separado. El diseño reúne estas necesidades en una propuesta de plataforma, con roles y comportamiento de agenda definidos. Esto describe un entregable de diseño, no una implementación confirmada ni una reducción de tiempos medida. El aprendizaje es tratar reglas y permisos como parte central de la experiencia.

[DATO PENDIENTE: HC-01 | validación de permisos del agente y estado de implementación].

<figure class="img-placeholder" data-ratio="16:9" data-id="hacienda-citas-05">
  <div class="img-placeholder__box">
    <p class="img-placeholder__prompt">Create a conceptual paired mobile and desktop UI mockup for a public appointment request form with clear field grouping, a generic availability selector and confirmation state, no filled personal fields. Style: polished product design editorial illustration with high visual detail and clean edges. Palette: deep blue, teal, warm white and neutral gray. Composition: balanced focal area, generous margins, 16:9 aspect ratio. Use abstract shapes instead of readable text or digits. No real logos, brand marks, personal data, actual client screenshots, or confidential material. This is a conceptual reconstruction, not evidence of a delivered screen or an actual research artifact.</p>
  </div>
  <figcaption lang="es">Formulario conceptual de solicitud de citas con información ficticia.</figcaption>
  <figcaption lang="en">Conceptual appointment request form using fictional information.</figcaption>
</figure>

## Cierre

El caso muestra cómo hacer visible la lógica de un servicio para quienes lo administran y para quienes solicitan una cita. Los ejemplos visuales serán ficticios.
