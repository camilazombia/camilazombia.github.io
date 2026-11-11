"""Author bilingual case files and the metadata consumed by the local portfolio."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
out = root / 'content'
(out / 'projects').mkdir(parents=True, exist_ok=True)

# Each locale has the same eight sections. Only supplied work is described as completed.
cases = [
{
'id': 'adidas', 'slug': 'broken-chains', 'brand': 'Broken Chains · BlackSip',
'title': ['Broken Chains: ecommerce de sneakers', 'Broken Chains: sneaker ecommerce'],
'role': ['Diseño UX/UI para ecommerce', 'Ecommerce UX/UI design'],
'skills': ['Benchmark, colaboración con cliente, estrategia de drops', 'Benchmarking, client collaboration, drop strategy'],
'type': ['Ecommerce', 'Ecommerce'],
'es': [
'Rediseño de Broken Chains, un ecommerce de sneakers exclusivos de marcas como Adidas y Nike. El trabajo conectó la experiencia de compra con la lógica de los lanzamientos y el contenido de la tienda.',
'Mi contribución fue el diseño para ecommerce dentro de la experiencia en BlackSip. Trabajé en mesas con el cliente para relacionar las propuestas con sus lanzamientos. La composición completa del equipo no está documentada.',
'La tienda necesitaba una experiencia acorde con un catálogo de sneakers exclusivos y con las dinámicas de los drops. El reto era conectar el lanzamiento, el contenido que lo presenta y la exploración del producto, sin tratar cada pieza como una comunicación aislada.',
'Realicé un benchmark de sitios con un concepto similar y participé en mesas de trabajo con el cliente. Estas actividades sirvieron como referencia para el rediseño y las estrategias de lanzamiento. No se dispone de evidencia de entrevistas, pruebas de usabilidad o seguimiento posterior; no se atribuyen esas actividades al proyecto.',
'- Tomar ecommerce de sneakers exclusivos como referentes para evaluar patrones pertinentes al catálogo.\n- Vincular las propuestas de compra con los drops para mantener el contexto del lanzamiento.\n- Relacionar contenido y producto para que la comunicación de campaña acompañara la exploración.\n- Trabajar las propuestas con el cliente para contrastarlas con sus necesidades comerciales.',
'La solución reúne el rediseño del ecommerce y el planteamiento de estrategias de lanzamiento y contenido acordes con los drops. Este caso se refiere a Broken Chains; mencionar Adidas y Nike describe las marcas del catálogo y no implica contratación directa por ellas.',
'El entregable documentado es el trabajo de rediseño y las propuestas vinculadas a lanzamientos. No hay una comparación comprobada del desempeño anterior y posterior. El aprendizaje del caso es que el contenido de un drop y la experiencia de compra deben planearse juntos.\n\n[DATO PENDIENTE: BC-01 | inventario aprobado de pantallas y piezas de lanzamiento].',
'Una experiencia de compra para un catálogo especializado requiere coherencia entre el producto, su lanzamiento y la forma de presentarlo.'
],
'en': [
'A redesign of Broken Chains, an ecommerce store for exclusive sneakers from brands such as Adidas and Nike. The work connected shopping with product drops and the content supporting each launch.',
'I contributed ecommerce design through my work at BlackSip. Client workshops connected the proposals with upcoming launches. The full team composition is not documented.',
'The store needed an experience suited to exclusive sneakers and product drops. The challenge was to connect the launch, its supporting content, and product discovery rather than treating each communication as a separate piece.',
'I benchmarked stores with a similar concept and took part in working sessions with the client. These activities informed the redesign and launch strategies. There is no supporting evidence for interviews, usability testing, or subsequent performance tracking, so these activities are not claimed.',
'- Use specialist sneaker stores as references for patterns relevant to the catalog.\n- Connect the shopping proposal with product drops to retain the launch context.\n- Bring content and product together so campaign communication supports discovery.\n- Review proposals with the client against their commercial needs.',
'The solution brings together the ecommerce redesign and launch and content strategies suited to drops. This case concerns Broken Chains. Adidas and Nike are mentioned as catalog brands, without implying a direct commission from either company.',
'The documented output is the redesign work and proposals supporting launches. A verified before-and-after performance comparison is not available. The key takeaway is to plan drop content and the shopping experience together.\n\n[DATO PENDIENTE: BC-01 | approved inventory of screens and launch assets].',
'A specialist shopping experience needs consistency between the product, its launch, and how it is presented.'
]
},
{
'id': 'appointment-scheduling', 'slug': 'hacienda-citas', 'brand': 'Secretaría de Hacienda',
'title': ['Agendamiento de citas', 'Appointment scheduling'],
'role': ['Diseño UX/UI', 'UX/UI design'],
'skills': ['Flujos, permisos, reglas de agendamiento, interfaces', 'Flows, permissions, scheduling rules, interfaces'],
'type': ['Plataforma de servicios públicos', 'Public service platform'],
'es': [
'Diseño de una plataforma de agendamiento para Hacienda. La propuesta reúne la solicitud de citas y la gestión operativa de agendas, con responsabilidades diferenciadas para administrador, coordinador y agente.',
'Trabajé en los flujos, las interfaces y las definiciones de comportamiento del sistema. El alcance incluyó reglas de agendamiento y permisos por perfil. No se cuenta con el detalle completo del equipo.',
'El proceso estaba fragmentado: se enviaba un Excel al proveedor para habilitar la agenda, el formulario de solicitud presentaba problemas de experiencia de uso y el calendario en Teams no mostraba suficiente detalle. Esta separación dificultaba entender el proceso completo desde la configuración hasta la atención.',
'Partí de los flujos existentes descritos y definí la estructura de una plataforma con gestión por perfiles y un formulario de solicitud. El trabajo de diseño precisó reglas, límites y comportamiento de las agendas dinámicas. No se afirman pruebas con usuarios, despliegue o resultados operativos que no estén documentados.',
'- Separar administrador, coordinador y agente para hacer explícita la responsabilidad de cada perfil.\n- Concentrar el control general, incluido el correo, en el administrador para definir la configuración del servicio.\n- Dar al coordinador una vista de su sede para situar la gestión en su contexto operativo.\n- Diseñar agendas dinámicas en las que agregar un bloque ajuste los demás para contemplar el comportamiento conjunto del horario.\n- Definir límites de solicitudes como reglas del sistema para evitar decisiones implícitas en el formulario.',
'La propuesta incluye un formulario de solicitud de citas, un perfil administrador con control total y configuración de correo y reglas, y un dashboard del coordinador para su sede con creación de agendas dinámicas. El perfil agente forma parte del modelo de roles; sus permisos detallados requieren confirmación.',
'Antes, la operación dependía de archivos enviados al proveedor, un formulario y un calendario separado. El diseño reúne estas necesidades en una propuesta de plataforma, con roles y comportamiento de agenda definidos. Esto describe un entregable de diseño, no una implementación confirmada ni una reducción de tiempos medida. El aprendizaje es tratar reglas y permisos como parte central de la experiencia.\n\n[DATO PENDIENTE: HC-01 | validación de permisos del agente y estado de implementación].',
'El caso muestra cómo hacer visible la lógica de un servicio para quienes lo administran y para quienes solicitan una cita. Los ejemplos visuales serán ficticios.'
],
'en': [
'A scheduling platform design for Hacienda. The proposal connects appointment requests with schedule management and distinguishes the responsibilities of administrators, coordinators, and agents.',
'I worked on flows, interfaces, and system behavior definitions, including scheduling rules and permissions by role. A complete team breakdown is not available.',
'The process was fragmented: an Excel file was sent to a provider to enable availability, the request form had usability issues, and a separate Teams calendar lacked detail. This separation made it difficult to understand the service from configuration through appointment handling.',
'Using the described existing workflows, I defined a platform structure with role-based management and a request form. The design work specified rules, limits, and dynamic schedule behavior. User testing, deployment, and operational outcomes are not claimed without supporting evidence.',
'- Distinguish administrators, coordinators, and agents to clarify responsibility.\n- Give the administrator overall control, including email, to configure the service.\n- Provide coordinators with an office-specific dashboard to keep management grounded in their operation.\n- Design dynamic schedules where adding a block adjusts the others to account for the whole schedule.\n- Define request limits as system rules so the form does not rely on implicit decisions.',
'The proposal includes an appointment request form, an administrator profile controlling email and scheduling rules, and an office dashboard where coordinators create dynamic schedules. The agent is part of the role model; detailed permissions still need confirmation.',
'Previously, the workflow relied on provider-bound files, a form, and a separate calendar. The design brings those needs into a platform proposal with defined roles and scheduling behavior. This is a design deliverable, not a confirmed deployment or measured time saving. The main takeaway is to treat rules and permissions as a core part of the experience.\n\n[DATO PENDIENTE: HC-01 | confirmation of agent permissions and implementation status].',
'The case makes service logic visible to both the people managing appointments and those requesting them. Visual examples will use fictional information.'
]
},
{
'id': 'pqrs-ai', 'slug': 'pqrs-ai', 'brand': 'Secretaría de Hacienda',
'title': ['PQRS con IA', 'AI-assisted PQRS'],
'role': ['Diseño UX/UI', 'UX/UI design'],
'skills': ['IA con control humano, priorización, correo dinámico', 'Human oversight of AI, prioritization, dynamic email'],
'type': ['Gestión de solicitudes', 'Request management'],
'es': [
'Diseño de una experiencia de gestión de PQRS con apoyo de IA ante un gran volumen de solicitudes. La propuesta organiza prioridades y recomendaciones sin quitar a la persona la decisión sobre cada cambio.',
'Mi contribución se centró en la experiencia de revisión de sugerencias, las acciones de cambio y el módulo de correo dinámico. La composición del equipo y las etapas de implementación no están documentadas.',
'El volumen de solicitudes planteaba un reto de lectura, clasificación y asignación. Incorporar IA exigía una experiencia que permitiera revisar sus recomendaciones antes de aplicarlas, en lugar de presentar una clasificación automática como una decisión definitiva.',
'Definí la experiencia alrededor de las tareas descritas: priorizar, comprender la solicitud, revisar su clasificación y asignar responsabilidad. El diseño conectó las sugerencias con controles por campo y una acción conjunta. No se atribuyen al trabajo entrenamiento del modelo, pruebas de precisión o validación de impacto.',
'- Mostrar un resumen para apoyar la lectura sin presentar la síntesis como sustituto de la solicitud original.\n- Separar tipo de radicado, subtipo, dependencia y responsable para revisar decisiones específicas.\n- Ofrecer Cambiar en cada campo para mantener el control humano.\n- Incluir Aplicar todos los cambios sugeridos como acción explícita de la persona.\n- Plantear transparencia y reversibilidad como criterios de diseño; su implementación requiere comprobarse.',
'La IA organiza por prioridad, resume y recomienda clasificación y asignación. La interfaz permite cambiar cada campo o aplicar el conjunto de sugerencias. El módulo de envío incorpora correo dinámico y tokens inteligentes para componer mensajes. Los estados de confirmación y la persistencia de cambios requieren validación con la implementación.',
'El entregable es una propuesta de gestión asistida que vincula recomendaciones con controles de revisión y composición de correo. No se dispone de mediciones de precisión, carga operativa o tiempo de respuesta. El aprendizaje es que una recomendación útil también debe ser comprensible y corregible.\n\n[DATO PENDIENTE: PQ-01 | evidencia de reversión y evaluación de recomendaciones].',
'La IA sugiere y la persona decide. Ese principio guía la presentación de recomendaciones y las acciones disponibles, sin afirmar autonomía del sistema.'
],
'en': [
'An AI-assisted PQRS management experience designed for a high volume of requests. The proposal organizes priorities and recommendations while leaving each change under human control.',
'My contribution focused on reviewing suggestions, changing individual fields, and composing dynamic emails. Team composition and implementation stages are not documented.',
'Request volume created a challenge for reading, classification, and assignment. Introducing AI called for an experience where people could examine recommendations before applying them, rather than treating an automated classification as final.',
'I organized the experience around the described tasks: prioritize, understand a request, review its classification, and assign responsibility. The design connected recommendations with field-level controls and a combined action. Model training, accuracy testing, and impact validation are not claimed.',
'- Present a summary to support reading without treating it as a replacement for the original request.\n- Separate case type, subtype, department, and assignee for focused review.\n- Offer Change for every field to retain human control.\n- Make Apply all suggested changes an explicit user action.\n- Treat transparency and reversibility as design criteria whose implementation still needs verification.',
'AI prioritizes requests, summarizes them, and recommends classification and assignment. People can change each field or apply the suggestions together. The sending module uses dynamic email and smart tokens to compose messages. Confirmation states and change persistence need to be checked against the implementation.',
'The deliverable is an assisted management proposal that connects recommendations with review controls and email composition. Accuracy, workload, and response-time measurements are not available. The takeaway is that a useful recommendation must also be understandable and correctable.\n\n[DATO PENDIENTE: PQ-01 | evidence of reversal behavior and recommendation evaluation].',
'AI suggests; a person decides. This principle guides how recommendations and controls are presented without claiming autonomous decision-making.'
]
},
{
'id': 'video-interview', 'slug': 'video-interview', 'brand': 'Remote Latinos',
'title': ['Video Interview', 'Video Interview'],
'role': ['Diseño UX/UI', 'UX/UI design'],
'skills': ['Flujo guiado, estados de grabación, casos límite', 'Guided flow, recording states, edge cases'],
'type': ['Selección de talento', 'Recruitment'],
'es': [
'Funcionalidad de entrevistas en video solicitada por clientes de Remote Latinos. El candidato responde preguntas según su rol, paso a paso, y la experiencia contempla la transcripción de la entrevista.',
'Trabajé en el diseño del flujo guiado y en la definición de estados y casos límite de la grabación. Los clientes aportaron la necesidad funcional; no está documentada la composición completa del equipo.',
'La necesidad era incorporar respuestas en video a preguntas relacionadas con el rol del candidato. El reto de experiencia consistía en acompañar una actividad secuencial que depende de la grabación y que debe contemplar errores y reintentos.',
'Organicé la secuencia de preguntas y la interacción de respuesta en video. El diseño consideró los estados grabando, error y reintento, junto con casos límite del recorrido. No se dispone de un protocolo de pruebas con candidatos ni de resultados de validación para atribuirlos al caso.',
'- Presentar las preguntas paso a paso para dar foco a la respuesta actual.\n- Relacionar las preguntas con el rol para mantener el contexto de la entrevista.\n- Diferenciar grabación, error y reintento para comunicar el estado de la tarea.\n- Incluir la transcripción como parte de la funcionalidad solicitada para acompañar la revisión del video.',
'La propuesta combina preguntas por rol, respuesta secuencial en video y transcripción. Los estados de grabación y recuperación forman parte del relato de diseño. Las reglas exactas de duración, permisos de cámara, interrupciones y guardado deben confirmarse con las especificaciones del producto; no se inventan aquí.',
'El resultado documentado es el diseño de una funcionalidad de entrevista con recorrido guiado y estados de grabación. No hay datos de finalización, errores o uso posterior. El aprendizaje es que diseñar una grabación implica definir también cómo se entiende y recupera un intento fallido.\n\n[DATO PENDIENTE: VI-01 | matriz aprobada de estados, recuperación y límites de grabación].',
'El foco del caso está en acompañar una tarea exigente con pasos y estados comprensibles, sin atribuir mejoras de contratación no medidas.'
],
'en': [
'A video interview feature requested by Remote Latinos clients. Candidates answer role-specific questions one step at a time, with interview transcription included in the experience.',
'I worked on the guided flow and the definition of recording states and edge cases. Clients supplied the functional need; the full delivery team is not documented.',
'The request was to add video answers to questions related to a candidate’s role. The experience challenge was to guide a sequential activity that depends on recording and must account for errors and retries.',
'I organized the question sequence and video response interaction. The design considered recording, error, and retry states, together with edge cases across the journey. There is no candidate testing protocol or validation evidence available to claim.',
'- Present questions step by step to focus attention on the current response.\n- Connect questions with the role to retain interview context.\n- Distinguish recording, error, and retry states to communicate task status.\n- Include transcription as part of the requested feature to support video review.',
'The proposal combines role-specific questions, sequential video responses, and transcription. Recording and recovery states are part of the design narrative. Exact rules for duration, camera permissions, interruptions, and saving need confirmation from product specifications and are not invented here.',
'The documented output is a guided interview feature design with recording states. Completion, error, and usage data are not available. The takeaway is that designing a recording experience also means defining how people understand and recover from a failed attempt.\n\n[DATO PENDIENTE: VI-01 | approved matrix of recording states, recovery behavior, and limits].',
'The case focuses on supporting a demanding task with understandable steps and states, without claiming unmeasured hiring improvements.'
]
},
{
'id': 'nibu-english-platform', 'slug': 'niibu', 'brand': 'Niibu',
'title': ['Niibu: tres aplicaciones con IA', 'Niibu: three AI applications'],
'role': ['Diseño UX/UI y sistema de diseño', 'UX/UI and design system design'],
'skills': ['Sistema de diseño, flujos alternos, funciones de IA', 'Design system, alternative paths, AI features'],
'type': ['Ecosistema de aplicaciones', 'Application ecosystem'],
'es': [
'Diseño de un ecosistema con Niibu PRO: Get Booked, Niibu: Personal AI Concierge y Niibu: Creator Studio. Mi contribución reunió un sistema de diseño completo y flujos preparados para desarrollo en un contexto de trabajo rápido.',
'Desarrollé tokens, componentes y plantillas, y organicé flujos principales, alternos, de error y casos límite. También trabajé en el diseño de funciones de IA. La composición completa del equipo no está documentada.',
'Las aplicaciones atienden necesidades diferentes: recibir reservas profesionales, organizar actividades personales y gestionar la actividad de creadores. El reto era dar consistencia al ecosistema sin borrar la lógica particular de cada aplicación.',
'El desarrollo fue rápido y no hubo procesos iterativos. Para orientar las decisiones, investigué aplicaciones referentes y sus flujos esperados. Estructuré el sistema de diseño y documenté recorridos para desarrollo. Este research de referentes no se presenta como investigación con usuarios ni como validación de usabilidad.',
'- Construir tokens, componentes y plantillas comunes para sostener la consistencia entre productos.\n- Documentar rutas alternas, errores y casos límite junto al happy path para precisar el comportamiento esperado.\n- Tratar cada aplicación por separado para mantener visibles sus tareas principales.\n- Diseñar funciones de IA dentro de flujos definidos, sin afirmar pruebas de precisión o eficacia no documentadas.',
'### Niibu PRO: Get Booked\n\nHerramienta para profesionales que reciben reservas y gestionan su disponibilidad. La ficha oficial describe agenda, servicios y gestión de trabajos.\n\n### Niibu: Personal AI Concierge\n\nAsistente para planificar el día, descubrir opciones de autocuidado y bienestar y registrar ciclo menstrual, medicación y calorías, funciones descritas en su ficha oficial.\n\n### Niibu: Creator Studio\n\nLa billetera permite seguir el origen de los ingresos. La ficha describe recompensas por seguidores verificados y controles antifraude, análisis entre seguidores y no seguidores, campañas con fondos en depósito, eventos y colaboraciones, suscripciones, productos etiquetados, hilos y perfil tipo portafolio. Son funciones del producto, no resultados económicos del diseño.',
'Los entregables descritos son el sistema de diseño y la organización de flujos para las aplicaciones. No se afirma una mejora medida de uso, ingresos o velocidad de desarrollo. El aprendizaje es que documentar estados y excepciones ayuda a explicitar decisiones incluso cuando el ritmo no permite iteraciones.\n\n[DATO PENDIENTE: NI-01 | inventario verificable de tokens, componentes, plantillas y flujos entregados].\n\nFuentes de funciones: [Get Booked](https://apps.apple.com/us/app/niibu-pro-get-booked/id6786669366), [Personal AI Concierge](https://apps.apple.com/us/app/niibu-personal-ai-concierge/id6762809126) y [Creator Studio](https://play.google.com/store/apps/details?id=niibu.creator.app). Las cifras de capturas son ilustrativas y no se usan como logros.',
'Un sistema compartido y recorridos explícitos permiten presentar el trabajo de diseño sin convertir la rapidez del proyecto en una afirmación de validación.'
],
'en': [
'An ecosystem spanning Niibu PRO: Get Booked, Niibu: Personal AI Concierge, and Niibu: Creator Studio. My contribution combined a complete design system with flows organized for development in a fast-moving project.',
'I developed tokens, components, and templates and organized happy paths, alternative paths, error flows, and edge cases. I also worked on AI feature design. The full team composition is not documented.',
'The applications serve different needs: receiving professional bookings, organizing personal activities, and managing creator work. The challenge was to establish consistency without erasing each application’s task structure.',
'Development moved quickly, without iterative processes. I researched reference applications and expected flows to inform decisions, structured the design system, and documented journeys for development. Reference research is not presented as user research or usability validation.',
'- Build shared tokens, components, and templates to support consistency across products.\n- Document alternative paths, errors, and edge cases alongside the happy path to clarify expected behavior.\n- Present each application separately to keep its primary tasks visible.\n- Design AI features within defined flows without claiming undocumented accuracy or effectiveness testing.',
'### Niibu PRO: Get Booked\n\nA tool for professionals receiving bookings and managing availability. Its official listing describes schedules, services, and job management.\n\n### Niibu: Personal AI Concierge\n\nAn assistant for daily planning, discovering self-care and wellness options, and tracking menstrual cycles, medication, and calories, as described in its official listing.\n\n### Niibu: Creator Studio\n\nThe wallet traces earnings to their source. The listing describes verified follower rewards and fraud checks, follower versus non-follower analytics, escrow-backed campaigns, events and collaborations, subscriptions, tagged products, threads, and a portfolio-style profile. These are product capabilities, not financial outcomes of the design.',
'The described deliverables are the design system and organized application flows. No measured improvement in usage, earnings, or development speed is claimed. The takeaway is that documenting states and exceptions makes decisions explicit even when the schedule does not allow iteration.\n\n[DATO PENDIENTE: NI-01 | verifiable inventory of delivered tokens, components, templates, and flows].\n\nFeature sources: [Get Booked](https://apps.apple.com/us/app/niibu-pro-get-booked/id6786669366), [Personal AI Concierge](https://apps.apple.com/us/app/niibu-personal-ai-concierge/id6762809126), and [Creator Studio](https://play.google.com/store/apps/details?id=niibu.creator.app). Screenshot figures are illustrative and are not treated as achievements.',
'A shared system and explicit journeys make the design contribution visible without treating project speed as evidence of validation.'
]
},
{
'id': 'publiandes-kids-platform', 'slug': 'ingles-infantil', 'brand': 'PubliAndes',
'title': ['Inglés para niños', 'English for children'],
'role': ['Diseño de bases y experiencia de aprendizaje', 'Learning foundations and experience design'],
'skills': ['Gamificación, progresión, contenido con IA', 'Gamification, progression, AI-supported content'],
'type': ['Plataforma educativa', 'Learning platform'],
'es': [
'Plataforma de inglés para niños organizada en mundos y niveles, con audio, video, cuentos y música. Desarrollé sus bases iniciales; las interacciones y el contenido se produjeron con apoyo de IA.',
'Mi aporte fue desarrollar las bases iniciales del proyecto. El apoyo de IA participó en la producción de interacciones y contenido. No se atribuye a la IA una validación pedagógica ni se dispone de la composición completa del equipo.',
'La experiencia debía reunir recursos de aprendizaje diversos dentro de un recorrido comprensible para niños. El desafío de diseño era conectar el avance por mundos y niveles con actividades y recompensas que tuvieran un lugar claro en la experiencia.',
'Desarrollé la base inicial y la propuesta de progresión. La producción de interacciones y contenido tuvo apoyo de IA e incluyó recursos audiovisuales y narrativos. No hay evidencia disponible de sesiones con niños, evaluación pedagógica o auditoría de accesibilidad; esas actividades no se presentan como realizadas.',
'- Organizar el recorrido en mundos y niveles para dar estructura al avance.\n- Combinar cuentos, música, audio y video para ofrecer distintos formatos de actividad.\n- Vincular monedas acumulables con la personalización del personaje para conectar recompensa y expresión personal.\n- Considerar legibilidad y retroalimentación como criterios de diseño infantil, sin afirmar conformidad de accesibilidad no evaluada.',
'La plataforma combina mundos, niveles y contenido multimedia. Las monedas acumuladas permiten personalizar el personaje. La propuesta visual debe mostrar tanto el avance como la relación entre las actividades y las recompensas; los detalles del sistema de monedas requieren comprobarse en los archivos del proyecto.',
'Los entregables descritos son las bases de la plataforma y las interacciones y contenidos producidos con apoyo de IA. No hay mediciones de aprendizaje, retención o accesibilidad. El aprendizaje es separar una mecánica de progresión de una prueba de eficacia educativa.\n\n[DATO PENDIENTE: IN-01 | inventario de actividades y evaluación de legibilidad, retroalimentación y accesibilidad].',
'El caso presenta una base de aprendizaje lúdico; no equipara el uso de IA o de recompensas con resultados pedagógicos demostrados.'
],
'en': [
'An English learning platform for children, organized into worlds and levels with audio, video, stories, and music. I developed the initial foundations; interactions and content were produced with AI support.',
'My contribution was developing the project’s initial foundations. AI supported interaction and content production. No educational validation is attributed to AI, and the full team composition is not available.',
'The experience needed to bring different learning resources into a journey children could understand. The design challenge was to connect progression through worlds and levels with activities and rewards that had a clear place in the experience.',
'I developed the initial foundation and progression concept. AI supported the production of interactions and content, including audiovisual and narrative resources. There is no available evidence of sessions with children, educational evaluation, or accessibility audits; these are not presented as completed activities.',
'- Structure progression through worlds and levels.\n- Combine stories, music, audio, and video to offer different activity formats.\n- Connect accumulated coins with character customization to link rewards and personal expression.\n- Consider readability and feedback as child-focused design criteria without claiming untested accessibility compliance.',
'The platform combines worlds, levels, and multimedia content. Accumulated coins can be used to personalize the character. Visual proposals should explain both progression and the relationship between activities and rewards; detailed coin rules need verification in project files.',
'The described outputs are the platform foundations and AI-supported interactions and content. Learning, retention, and accessibility measurements are not available. The takeaway is to distinguish a progression mechanic from evidence of educational effectiveness.\n\n[DATO PENDIENTE: IN-01 | activity inventory and readability, feedback, and accessibility evaluation].',
'The case presents a foundation for playful learning without equating AI or rewards with demonstrated educational outcomes.'
]
},
{
'id': 'javeriana-landings', 'slug': 'javeriana', 'brand': 'Javeriana',
'title': ['Landing pages académicas', 'Academic landing pages'],
'role': ['Diseño UX/UI', 'UX/UI design'],
'skills': ['Stakeholders, heurísticas, componentes, diseño móvil', 'Stakeholders, heuristics, components, mobile design'],
'type': ['Educación superior', 'Higher education'],
'es': [
'Diseño de landing pages para programas académicos de la Javeriana. El trabajo combinó reuniones con facultades, análisis UX/UI y archivos de Figma con componentes y versiones móviles.',
'Participé en reuniones con stakeholders de cada facultad para entender problemas, mejoras y expectativas, y desarrollé propuestas de diseño. El alcance también incluyó mesa de ayuda; no está documentado el detalle de sus tareas ni la composición completa del equipo.',
'Las facultades tenían necesidades y expectativas particulares para presentar sus programas. El reto era responder a esas diferencias y conservar criterios de experiencia coherentes entre páginas de pregrado, posgrado, MIB, especializaciones, doctorados y maestrías.',
'Recogí necesidades en reuniones con stakeholders, realicé análisis UX/UI con heurísticas y lineamientos y revisé referencias de otras universidades. Estas entradas orientaron las propuestas y las decisiones de diseño. Los archivos de Figma incluyeron componentes y versiones móviles. No se afirman pruebas con aspirantes ni métricas de conversión.',
'- Escuchar a cada facultad para situar la propuesta en sus necesidades.\n- Contrastar las páginas con heurísticas y lineamientos para fundamentar la revisión.\n- Consultar universidades referentes como apoyo a las decisiones, sin sustituir el contexto institucional.\n- Desarrollar diseños distintos según el tipo de programa para responder a diferencias de contenido.\n- Incluir componentes y versiones móviles para documentar la propuesta más allá de escritorio.',
'Se diseñaron landings de pregrado, posgrado, MIB, especializaciones, doctorados y maestrías con propuestas diferenciadas. Los archivos de Figma contienen componentes y adaptaciones móviles. La mesa de ayuda formó parte del alcance, con detalle pendiente de confirmar.',
'El entregable documentado son las propuestas de landing pages y sus archivos de diseño. No hay evidencia disponible para comparar inscripciones o consultas antes y después. El aprendizaje es que un lenguaje de componentes puede convivir con necesidades de contenido diferentes.\n\n[DATO PENDIENTE: JA-01 | inventario aprobado de landings, componentes y alcance de mesa de ayuda].',
'El caso conecta necesidades de las facultades con decisiones de interfaz. Las futuras imágenes conceptuales no reproducirán información institucional interna.'
],
'en': [
'Landing page design for Javeriana academic programs. The work combined faculty stakeholder meetings, UX/UI analysis, and Figma files with components and mobile versions.',
'I joined meetings with stakeholders from each faculty to understand problems, improvements, and expectations, and developed design proposals. Help desk work was also in scope; its detailed tasks and the complete team composition are not documented.',
'Faculties had different needs and expectations for presenting their programs. The challenge was to address those differences while maintaining coherent experience criteria across undergraduate, postgraduate, MIB, specialization, doctoral, and master’s pages.',
'I gathered needs through stakeholder meetings, conducted UX/UI analysis using heuristics and guidelines, and reviewed other universities for reference. These inputs informed proposals and design decisions. Figma files included components and mobile versions. Applicant testing and conversion metrics are not claimed.',
'- Hear from each faculty to ground proposals in their needs.\n- Review pages against heuristics and guidelines to give the analysis a clear basis.\n- Use other universities as references while retaining the institutional context.\n- Develop different designs by program type to address content differences.\n- Include components and mobile versions to document more than the desktop experience.',
'The work covered differentiated landing pages for undergraduate, postgraduate, MIB, specialization, doctoral, and master’s programs. Figma files contain components and mobile adaptations. Help desk work was included, with details still to be confirmed.',
'The documented deliverables are landing page proposals and their design files. Evidence for before-and-after enrollment or inquiry comparisons is not available. The takeaway is that a component language can support different content needs.\n\n[DATO PENDIENTE: JA-01 | approved inventory of landing pages, components, and help desk scope].',
'The case connects faculty needs with interface decisions. Future conceptual images will not reproduce internal institutional information.'
]
},
{
'id': 'flexi-digital-campaigns', 'slug': 'flexi', 'brand': 'Flexi · Freelance',
'title': ['Campañas digitales', 'Digital campaigns'],
'role': ['Diseño gráfico freelance', 'Freelance graphic design'],
'skills': ['Key visuals, email, animación, anuncios para Meta', 'Key visuals, email, animation, Meta ads'],
'type': ['Comunicación de campañas', 'Campaign communication'],
'es': [
'Diseño de campañas digitales de Flexi para temporadas como San Valentín y Black Days. El trabajo incluyó propuestas de key visuals y adaptaciones a email, piezas animadas y anuncios para Meta.',
'Mi rol fue la conceptualización visual y el diseño gráfico freelance de piezas de campaña. No se dispone del detalle del equipo ni de responsabilidades de planificación de medios.',
'Las temporadas especiales requerían comunicar productos y promociones en distintos formatos. El reto visual era sostener una idea de campaña al pasar de una composición principal a un email, una pieza animada o un anuncio.',
'Desarrollé varias propuestas de key visuals y piezas para los canales definidos. El proceso documentado es de exploración gráfica y adaptación de campaña; no se atribuyen investigación UX, experimentos publicitarios ni optimización de pauta.',
'- Explorar varias propuestas visuales para abrir opciones de dirección de campaña.\n- Usar el key visual como referencia para mantener continuidad entre piezas.\n- Adaptar la composición al email y a los formatos de Meta en lugar de tratar todos los soportes como equivalentes.\n- Incorporar piezas animadas como parte de la variedad de formatos de campaña.',
'La selección reúne key visuals, emails, piezas animadas y ads para Meta vinculados a temporadas especiales. Son entregables de comunicación visual, no un rediseño de producto digital ni una intervención documentada sobre el flujo de compra.',
'El resultado documentado es un conjunto de propuestas y adaptaciones de campaña. No se cuenta con resultados atribuibles de ventas, clics o retorno de pauta. El aprendizaje es sostener la idea visual mientras cambia el formato y su forma de lectura.\n\n[DATO PENDIENTE: FL-01 | inventario de campañas y piezas aprobadas por formato].',
'El caso destaca dirección visual y consistencia de campaña sin atribuir resultados comerciales no medidos.'
],
'en': [
'Digital campaign design for Flexi around occasions such as Valentine’s Day and Black Days. The work included key visual proposals and adaptations for email, animated assets, and Meta ads.',
'I contributed freelance visual concepts and graphic design for campaign assets. Team details and media planning responsibilities are not available.',
'Seasonal campaigns needed to communicate products and promotions across formats. The visual challenge was to retain a campaign idea as it moved from a main composition to an email, animation, or advertisement.',
'I developed several key visual proposals and assets for the specified channels. The documented process concerns visual exploration and campaign adaptation, not UX research, advertising experiments, or media optimization.',
'- Explore multiple visual proposals to offer campaign direction options.\n- Use the key visual as a reference for continuity across assets.\n- Adapt composition for email and Meta formats rather than treating all placements as equivalent.\n- Include animation in the campaign’s range of formats.',
'The selection brings together key visuals, emails, animated assets, and Meta ads for seasonal campaigns. These are visual communication deliverables, not a digital product redesign or a documented intervention in the purchase flow.',
'The documented output is a set of campaign proposals and adaptations. Attributable sales, click, or advertising return results are not available. The takeaway is to retain a visual idea while adapting to each format and reading context.\n\n[DATO PENDIENTE: FL-01 | inventory of approved campaigns and assets by format].',
'The case highlights visual direction and campaign consistency without claiming unmeasured commercial results.'
]
},
{
'id': 'the-bar-colombia', 'slug': 'the-bar-colombia', 'brand': 'The Bar Colombia · BlackSip',
'title': ['The Bar Colombia: ecommerce de lujo', 'The Bar Colombia: luxury ecommerce'],
'role': ['Diseño UX/UI para ecommerce', 'Ecommerce UX/UI design'],
'skills': ['Research, card sorting, arquitectura, seguimiento', 'Research, card sorting, information architecture, monitoring'],
'type': ['Ecommerce', 'Ecommerce'],
'es': [
'Rediseño del ecommerce The Bar Colombia con una premisa del cliente: transmitir la sensación de estar en una página de lujo. El trabajo conectó investigación, arquitectura de la información, diseño de páginas y seguimiento posterior.',
'Mi contribución incluyó desktop research, benchmark, encuestas, user personas, pilares de diseño, card sorting, arquitectura y diseño de todas las páginas. También realicé seguimiento con mapas de calor, grabaciones y Google Analytics para ajustar e iterar. El proyecto forma parte de mi experiencia en BlackSip.',
'La aspiración de lujo debía traducirse en una experiencia de compra, no quedarse en una referencia estética. El reto era relacionar el lenguaje visual de bebidas espirituosas y marcas de lujo con la forma en que las personas encuentran y evalúan el catálogo.',
'Investigué referentes de bebidas espirituosas y lujo y comparé ecommerce del sector. El user research incluyó encuestas y user personas, que acompañaron la definición de pilares de diseño. Trabajé card sorting y arquitectura de la información antes del diseño de páginas. Después hubo seguimiento con heatmaps, grabaciones y Google Analytics, con ajustes e iteraciones. No se dispone de cifras de muestra ni de impacto.',
'- Traducir la premisa de lujo en pilares de diseño para orientar decisiones más allá de preferencias estéticas.\n- Combinar referentes de marca y de ecommerce para conectar presentación y compra.\n- Trabajar la organización del catálogo con card sorting y arquitectura de la información.\n- Diseñar el conjunto de páginas para considerar la experiencia completa.\n- Revisar el comportamiento observado después del diseño para orientar ajustes, sin asumir que observar equivale a demostrar una mejora.',
'El entregable fue el rediseño de todas las páginas del ecommerce, apoyado por la arquitectura y los pilares de diseño. El seguimiento de uso formó parte del proceso y generó ajustes e iteraciones; el detalle de cada cambio y su efecto necesita documentación adicional.',
'El caso cuenta con investigación, definición de arquitectura, diseño completo y seguimiento posterior. No hay cifras disponibles para afirmar aumentos de conversión o reducciones de abandono. El aprendizaje es conectar la aspiración visual con organización del catálogo y comportamiento observado.\n\n[DATO PENDIENTE: TB-01 | comparación de conversión y abandono con periodos y cambios documentados].',
'La percepción de lujo orientó el proyecto; la investigación y el seguimiento dieron contexto a las decisiones de experiencia de compra.'
],
'en': [
'A redesign of The Bar Colombia ecommerce store, guided by the client’s request for a luxury experience. The work connected research, information architecture, page design, and subsequent monitoring.',
'My contribution included desk research, benchmarking, surveys, user personas, design pillars, card sorting, architecture, and design of all pages. I also used heatmaps, recordings, and Google Analytics for follow-up adjustments and iteration. The project was part of my work at BlackSip.',
'The luxury ambition needed to become a shopping experience rather than remain an aesthetic reference. The challenge was to connect the visual language of spirits and luxury brands with how people find and evaluate the catalog.',
'I researched spirits and luxury references and benchmarked beverage ecommerce stores. User research included surveys and personas alongside the definition of design pillars. Card sorting and information architecture preceded page design. Follow-up used heatmaps, recordings, and Google Analytics to inform adjustments and iteration. Sample sizes and impact figures are not available.',
'- Translate the luxury brief into design pillars to guide decisions beyond aesthetic preferences.\n- Combine brand and ecommerce references to connect presentation and shopping.\n- Work on catalog organization through card sorting and information architecture.\n- Design the full set of pages to consider the overall experience.\n- Use observed behavior to inform adjustments without treating observation alone as proof of improvement.',
'The deliverable was a redesign of all ecommerce pages, supported by the architecture and design pillars. Usage monitoring was part of the process and led to adjustments and iteration; the specific changes and their effects need further documentation.',
'The case includes research, architecture, full page design, and subsequent monitoring. No figures are available to claim higher conversion or lower abandonment. The takeaway is to connect visual ambition with catalog organization and observed behavior.\n\n[DATO PENDIENTE: TB-01 | conversion and abandonment comparison with documented periods and changes].',
'The luxury brief guided the project, while research and monitoring gave context to shopping experience decisions.'
]
},
{
'id': 'previsora-social-media', 'slug': 'previsora', 'brand': 'Previsora Seguros · Buentipo Anchor',
'title': ['Previsora Seguros: redes sociales', 'Previsora Seguros: social media'],
'role': ['Diseño gráfico', 'Graphic design'],
'skills': ['Colaboración editorial, variedad visual, redes sociales', 'Editorial collaboration, visual variety, social media'],
'type': ['Comunicación en redes sociales', 'Social media communication'],
'es': [
'Diseño gráfico para redes sociales de Previsora Seguros en colaboración con el content creator. El trabajo buscó ampliar la variedad del contenido y explorar piezas más dinámicas e interactivas.',
'Mi contribución fue el diseño de piezas para redes sociales dentro del trabajo en Buentipo Anchor. Colaboré con el content creator en la relación entre contenido y propuesta visual. No se atribuye diseño de la web ni de servicios de seguros.',
'La necesidad descrita era diversificar la comunicación en redes. El reto era coordinar contenido y diseño para proponer variaciones sin perder la coherencia de la marca.',
'Trabajé en equipo con el content creator para desarrollar las piezas. El proceso documentado corresponde a colaboración editorial y diseño gráfico; no hay información de investigación con asegurados, pruebas de interacción ni análisis de rendimiento para incluirlos como realizados.',
'- Colaborar con el content creator para conectar el mensaje con su expresión visual.\n- Explorar variedad de piezas para ampliar las posibilidades de comunicación.\n- Buscar recursos dinámicos e interactivos como intención de diseño, sin afirmar un aumento de participación.\n- Mantener el alcance en redes sociales para representar con precisión la contribución.',
'La selección reúne piezas de comunicación para redes sociales. El contenido específico y los formatos aprobados deben contrastarse con el archivo de campaña antes de publicar ejemplos reales. Los placeholders muestran propuestas conceptuales sin información de asegurados.',
'El entregable documentado es el trabajo de piezas para redes y la colaboración con creación de contenido. No hay mediciones de engagement ni una comparación verificable de variedad antes y después. El aprendizaje es trabajar contenido y diseño de forma conjunta.\n\n[DATO PENDIENTE: PR-01 | selección aprobada e inventario de formatos de redes sociales].',
'Un caso de comunicación visual y colaboración editorial, con un alcance limitado a redes sociales.'
],
'en': [
'Graphic design for Previsora Seguros social media in collaboration with a content creator. The work aimed to broaden content variety and explore more dynamic and interactive pieces.',
'I designed social media assets through my work at Buentipo Anchor, collaborating with the content creator to connect messages and visual proposals. Website or insurance service design is not claimed.',
'The stated need was to diversify social communication. The challenge was to coordinate content and design to propose variation while retaining brand consistency.',
'I worked with the content creator on the assets. The documented process covers editorial collaboration and graphic design. Policyholder research, interaction tests, and performance analysis are not documented and are not presented as completed activities.',
'- Collaborate with the content creator to connect the message with its visual expression.\n- Explore a range of assets to broaden communication options.\n- Pursue dynamic and interactive resources as a design intention without claiming increased engagement.\n- Keep the case focused on social media to represent the contribution accurately.',
'The selection concerns social media communication assets. Specific content and approved formats need to be checked against campaign files before real examples are published. Placeholders show conceptual proposals without policyholder information.',
'The documented output is social media design work and collaboration on content creation. Engagement measurements and a verified comparison of content variety are not available. The takeaway is to develop content and design together.\n\n[DATO PENDIENTE: PR-01 | approved selection and inventory of social media formats].',
'A case about visual communication and editorial collaboration, limited to social media.'
]
},
{
'id': 'peoplepass-graphic-design', 'slug': 'peoplepass', 'brand': 'PeoplePass',
'title': ['PeoplePass: redes sociales y material POP', 'PeoplePass: social media and POP materials'],
'role': ['Diseño gráfico', 'Graphic design'],
'skills': ['Adaptación de formatos, comunicación digital e impresa', 'Format adaptation, digital and print communication'],
'type': ['Comunicación visual', 'Visual communication'],
'es': [
'Selección de diseño gráfico para PeoplePass en redes sociales y material POP. El caso reúne comunicación digital y piezas para puntos de contacto físicos dentro de una misma identidad.',
'Mi rol fue el diseño gráfico de piezas para redes sociales y material POP. El contenido existente del portafolio también registra coordinación con proveedores y gestión de aprobaciones; el detalle de esa participación requiere confirmación.',
'El trabajo abarcó soportes con condiciones de lectura y producción diferentes. El reto era adaptar la comunicación a medios digitales y físicos sin perder continuidad de marca. No se dispone de un diagnóstico previo para afirmar problemas específicos de rendimiento.',
'Desarrollé piezas gráficas para los soportes descritos. La documentación disponible no detalla una investigación UX, una secuencia de validación ni resultados de producción; no se añaden esas etapas por seguir una plantilla de caso.',
'- Distinguir redes sociales y material POP para considerar el contexto de cada soporte.\n- Mantener coherencia de identidad entre piezas digitales y físicas.\n- Adaptar las composiciones a su formato como parte del trabajo gráfico.\n- Limitar el relato a los entregables documentados en lugar de presentar una transformación de producto.',
'La selección comprende contenido gráfico para redes y material POP. El inventario de piezas, las especificaciones de impresión y los ejemplos publicables deben comprobarse con el archivo aprobado del proyecto.',
'El resultado descrito es el conjunto de piezas de comunicación digital y física. No hay datos de alcance, recordación o ventas que puedan atribuirse al diseño. El aprendizaje es considerar el soporte y la lectura como parte de una misma decisión visual.\n\n[DATO PENDIENTE: PP-01 | inventario aprobado y alcance de coordinación con proveedores].',
'El caso muestra adaptación gráfica entre soportes, sin convertir la producción de piezas en una afirmación de impacto comercial.'
],
'en': [
'A selection of PeoplePass graphic design for social media and point-of-purchase materials. The case brings digital communication and physical touchpoints together within one identity.',
'My role involved graphic design for social media and POP materials. Existing portfolio copy also mentions supplier coordination and approval management; the details of that contribution need confirmation.',
'The work covered media with different reading and production conditions. The challenge was to adapt communication across digital and physical formats while retaining brand continuity. A prior diagnosis is not available to support specific performance problems.',
'I developed graphic assets for the described media. The available documentation does not detail UX research, a validation sequence, or production outcomes; these stages are not added simply to fill a case study template.',
'- Distinguish social media and POP materials to consider each medium’s context.\n- Maintain identity consistency across digital and physical assets.\n- Adapt compositions to their formats as part of the graphic design work.\n- Keep the narrative focused on documented outputs rather than presenting a product transformation.',
'The selection covers social media graphics and POP materials. The asset inventory, print specifications, and publishable examples need to be checked against approved project files.',
'The described output is a set of digital and physical communication assets. Reach, recall, or sales figures attributable to the design are not available. The takeaway is to consider the medium and reading context as part of the visual decision.\n\n[DATO PENDIENTE: PP-01 | approved inventory and scope of supplier coordination].',
'The case shows graphic adaptation across media without treating asset production as evidence of commercial impact.'
]
}
]

headings = {
'es': ['Resumen', 'Rol y equipo', 'Contexto y problema', 'Proceso', 'Decisiones clave de diseño', 'Solución', 'Resultados y aprendizajes', 'Cierre'],
'en': ['Summary', 'Role and team', 'Context and problem', 'Process', 'Key design decisions', 'Solution', 'Outcomes and learnings', 'Closing']
}
metadata = {}
for case in cases:
    metadata[case['id']] = {'slug': case['slug']}
    for i, lang in enumerate(['es', 'en']):
        body = f"# {case['title'][i]}\n\n" + '\n\n'.join(f'## {title}\n\n{text}' for title, text in zip(headings[lang], case[lang])) + '\n'
        (out / 'projects' / f"{case['slug']}.{lang}.md").write_text(body, encoding='utf-8')
        metadata[case['id']][lang] = {'name': case['title'][i], 'category': case['brand'], 'role': case['role'][i], 'description': case[lang][0]}
(root / 'src/data/caseMetadata.json').write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

intro = {
'es': [
'Soy Camila, diseñadora UX/UI con experiencia en productos digitales, educación, comercio electrónico y comunicación visual. Trabajo con flujos, interfaces y sistemas de diseño para convertir requisitos en propuestas claras. Este portafolio reúne mi contribución en cada proyecto: el contexto, las decisiones y los entregables, con una distinción explícita entre lo que diseñé, lo que se validó y lo que falta comprobar.',
'Mi trayectoria conecta diseño gráfico y diseño de experiencias digitales. He trabajado en aplicaciones con IA, servicios públicos, plataformas educativas, ecommerce y campañas. Según el proyecto, mi aporte ha incluido investigación de referentes, encuestas, arquitectura de la información, flujos, componentes y diseño visual.\n\nMe interesa explicar por qué una interfaz toma una forma determinada: qué problema atiende, qué reglas necesita y qué decisiones quedan en manos de la persona. También considero los estados de error y los casos límite como parte del diseño.\n\nLos casos distinguen el alcance de mi contribución y las actividades realmente realizadas. Cuando no existen datos de impacto, presento entregables y aprendizajes sin atribuir mejoras no medidas. Las propuestas visuales son conceptuales y usan información ficticia para proteger la confidencialidad.'
],
'en': [
'I’m Camila, a UX/UI designer with experience in digital products, education, ecommerce, and visual communication. I work with flows, interfaces, and design systems to turn requirements into clear proposals. This portfolio explains my contribution to each project through its context, decisions, and deliverables, distinguishing what I designed, what was validated, and what still needs evidence before it can be claimed.',
'My background connects graphic design with digital experience design. I have worked on AI applications, public services, learning platforms, ecommerce, and campaigns. Depending on the project, my contribution has included reference research, surveys, information architecture, flows, components, and visual design.\n\nI’m interested in explaining why an interface takes a particular form: the problem it addresses, the rules it needs, and the decisions that remain with the person using it. Error states and edge cases are also part of that work.\n\nEach case distinguishes my contribution from activities that were not documented. When impact data is unavailable, I present deliverables and learnings without claiming unmeasured improvements. Visual proposals are conceptual and use fictional information to protect confidentiality.'
]}
for lang, paragraphs in intro.items():
    titles = ['Introducción corta', 'Introducción larga'] if lang == 'es' else ['Short introduction', 'Long introduction']
    (out / f'portfolio-intro.{lang}.md').write_text('\n\n'.join(f'## {title}\n\n{text}' for title, text in zip(titles, paragraphs)) + '\n', encoding='utf-8')

summary = '# Proyectos / Projects\n\n| Proyecto / Project | Tipo / Type | Rol / Role | Habilidades / Skills |\n| --- | --- | --- | --- |\n'
for c in cases:
    summary += f"| {c['title'][0]} / {c['title'][1]} | {' / '.join(c['type'])} | {' / '.join(c['role'])} | {' / '.join(c['skills'])} |\n"
(out / 'projects-summary.md').write_text(summary, encoding='utf-8')

pending = [
('BC-01', 'Broken Chains', 'Inventario de pantallas y piezas de lanzamiento', 'Figma y entregables aprobados por el cliente', 'Describir el rediseño y las estrategias sin cifras; publicar conteos solo después de verificar el inventario.'),
('HC-01', 'Hacienda: citas', 'Permisos del agente y estado de implementación', 'Matriz de permisos, especificaciones y confirmación del equipo', 'Presentar roles y agenda como propuesta de diseño, sin afirmar despliegue o ahorro de tiempo.'),
('PQ-01', 'PQRS con IA', 'Reversión y evaluación de recomendaciones', 'Prototipo, criterios de aceptación y revisión con responsables del servicio', 'Explicar controles por campo y acción conjunta; describir reversibilidad como criterio pendiente, no comportamiento demostrado.'),
('VI-01', 'Video Interview', 'Estados, recuperación y límites de grabación', 'Figma, especificaciones y QA del producto', 'Presentar flujo guiado, transcripción y estados descritos sin inventar duración ni política de guardado.'),
('NI-01', 'Niibu', 'Tokens, componentes, plantillas y flujos entregados', 'Conteo de recursos y flujos en Figma con fecha de revisión real', 'Enumerar tipos de entregables sin cantidades ni afirmaciones de velocidad de desarrollo.'),
('IN-01', 'Inglés infantil', 'Actividades y evaluación de legibilidad, feedback y accesibilidad', 'Inventario de contenido y evaluación con especialistas y usuarios con autorización adecuada', 'Describir mundos, niveles, formatos y personalización como propuesta; no afirmar eficacia educativa ni conformidad.'),
('JA-01', 'Javeriana', 'Landings, componentes y alcance de mesa de ayuda', 'Figma y registro de entregas; confirmar significado de MIB con la institución', 'Enumerar tipos de programas suministrados sin cifras de páginas, captación o inscripción.'),
('FL-01', 'Flexi', 'Campañas y piezas aprobadas por formato', 'Carpeta de entregables y aprobaciones del cliente', 'Enumerar key visuals, email, animación y Meta sin adjudicar ventas ni métricas de pauta.'),
('TB-01', 'The Bar Colombia', 'Conversión y abandono, periodos comparables y cambios', 'Google Analytics autorizado, heatmaps, grabaciones anonimizadas y registro de iteraciones', 'Describir investigación, arquitectura, diseño de páginas y seguimiento; no afirmar mejoras causales sin evidencia.'),
('PR-01', 'Previsora', 'Selección aprobada y formatos de redes', 'Archivo de campaña y revisión con content creator', 'Describir colaboración y piezas sin afirmar incremento de variedad o engagement.'),
('PP-01', 'PeoplePass', 'Inventario y alcance de coordinación con proveedores', 'Archivo aprobado, especificaciones de producción y confirmación de responsabilidades', 'Limitar la contribución confirmada a redes y POP; verificar antes de contar piezas o detallar proveedores.'),
]
report = '''# Datos pendientes

Los identificadores se comparten entre ES/EN. No son métricas ni cifras de impacto. Los marcadores se conservan visibles hasta contar con evidencia. No se publican cantidades estimadas. Las alternativas siguientes pueden usarse sin inventar cifras; cualquier conteo futuro debe contrastarse con un inventario aprobado.

| ID | Proyecto | Dato pendiente | Fuente sugerida | Alternativa honesta |
| --- | --- | --- | --- | --- |
'''
report += '\n'.join('| ' + ' | '.join(row) + ' |' for row in pending)
report += '''

## Fuentes y límites

Fuente de contribuciones: documento de trabajo aportado por la autora y textos existentes del repositorio, estos últimos sujetos a las dudas indicadas en los casos. No hay evidencia para inventar fechas o nombres de colaboradores. No se requiere recolectar datos personales para completar el reporte.

Funciones de Niibu verificadas en fichas oficiales, consultadas el 10 de noviembre de 2026:

- [Niibu PRO: Get Booked](https://apps.apple.com/us/app/niibu-pro-get-booked/id6786669366): reservas profesionales, disponibilidad, servicios y gestión de trabajos.
- [Niibu: Personal AI Concierge](https://apps.apple.com/us/app/niibu-personal-ai-concierge/id6762809126): planificación, autocuidado y bienestar, registro de ciclo, medicación y calorías.
- [Niibu: Creator Studio](https://play.google.com/store/apps/details?id=niibu.creator.app): billetera con origen de ingresos, recompensas verificadas y antifraude, rendimiento por audiencia, campañas en depósito, eventos, suscripciones, productos etiquetados, hilos y perfil portafolio.

Las fichas describen capacidades del producto, no la autoría de pantallas ni resultados del trabajo de diseño. No se usan ganancias de capturas, permisos, compatibilidad, descargas ni tamaños como logros.

Las entradas remote-latinos-website y devar-colombia-website se excluyen de la selección según la decisión de la autora. El ID histórico nibu-english-platform se mantiene como URL de Niibu.
'''
(root / 'reports/pendientes.md').write_text(report, encoding='utf-8')
print('22 casos, introducciones, tabla, metadatos y pendientes creados.')
