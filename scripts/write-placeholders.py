"""Insert bilingual conceptual-image briefs in the authored case files."""
from pathlib import Path
import html
import re

root = Path(__file__).resolve().parents[1]
# Section index, image subject/composition, ES caption, EN caption, illustrative figures.
briefs = {
'niibu': [
(4, 'UI design system board with token swatches, spacing samples, reusable mobile components and page templates, organized in a precise modular grid', 'Tablero conceptual de tokens, componentes y plantillas del sistema de diseño.', 'Conceptual board of design tokens, components, and templates.', False),
(5, 'flow diagram with a clear main path and branching alternative routes, error recovery and edge cases, using unlabeled nodes and distinct line styles', 'Mapa conceptual que distingue flujo principal, alternativas y errores.', 'Conceptual map distinguishing the happy path, alternatives, and errors.', False),
(6, 'mobile UI mockup for a professional booking application, showing availability blocks, a service catalog and appointment controls in one phone', 'Propuesta conceptual de Get Booked: disponibilidad y reservas profesionales.', 'Conceptual Get Booked proposal: professional availability and bookings.', False),
(6, 'mobile UI mockup for a personal AI concierge, with daily planning cards, wellness discovery and abstract private health tracking modules, no medical readings', 'Propuesta conceptual de Personal AI Concierge: planificación y seguimiento personal.', 'Conceptual Personal AI Concierge proposal: daily planning and personal tracking.', False),
(6, 'mobile UI mockup for a creator application, highlighting a wallet with traceable earning sources, reward states and a compact audience comparison chart with abstract values', 'Propuesta conceptual de Creator Studio: origen de ingresos y estados de recompensas.', 'Conceptual Creator Studio proposal: earning sources and reward states.', True),
],
'broken-chains': [
(4, 'research reference board comparing generic exclusive sneaker ecommerce patterns, launch imagery and product browsing layouts, no real website screenshots', 'Tablero conceptual de referentes de ecommerce y lanzamientos.', 'Conceptual board of ecommerce and launch references.', False),
(5, 'flow diagram connecting a sneaker drop announcement, launch landing page, product discovery and product detail, with abstract unlabeled nodes', 'Diagrama conceptual de la relación entre drop, contenido y producto.', 'Conceptual relationship between a drop, its content, and the product.', False),
(6, 'desktop UI mockup of an exclusive sneaker store homepage, editorial launch hero, product grid and strong product photography, entirely unbranded footwear', 'Propuesta conceptual de página de inicio para sneakers exclusivos.', 'Conceptual homepage proposal for exclusive sneakers.', False),
(6, 'paired desktop and mobile UI mockups for a sneaker product page, with large unbranded shoe photography, size selectors and a clear purchase action', 'Propuesta conceptual de detalle de producto en escritorio y móvil.', 'Conceptual product detail proposal on desktop and mobile.', False),
(7, 'editorial campaign board pairing an unbranded sneaker drop composition with matching ecommerce content cards, aligned visual rhythm and generous negative space', 'Composición conceptual que conecta piezas del lanzamiento y tienda.', 'Conceptual composition connecting launch assets and the store.', False),
],
'hacienda-citas': [
(4, 'service flow diagram contrasting scattered spreadsheet, request form and calendar icons with a unified scheduling platform, no client screenshots or internal details', 'Diagrama conceptual del proceso fragmentado y la propuesta integrada.', 'Conceptual diagram of the fragmented workflow and integrated proposal.', False),
(5, 'role responsibility diagram with administrator, office coordinator and agent represented by generic icons connected to separate permission groups, agent details abstract', 'Mapa conceptual de roles; los permisos detallados del agente están pendientes.', 'Conceptual role map; detailed agent permissions remain pending.', False),
(6, 'desktop UI mockup of an office scheduling dashboard with abstract appointment distribution, availability cards and a clearly bounded office workspace', 'Dashboard conceptual del coordinador de sede.', 'Conceptual office coordinator dashboard.', True),
(6, 'desktop UI sequence in three panels showing a dynamic appointment schedule before adding a time block, during insertion and after neighboring blocks adjust, no timestamps', 'Secuencia conceptual del ajuste de bloques en una agenda dinámica.', 'Conceptual sequence of block adjustment in a dynamic schedule.', False),
(7, 'paired mobile and desktop UI mockup for a public appointment request form with clear field grouping, a generic availability selector and confirmation state, no filled personal fields', 'Formulario conceptual de solicitud de citas con información ficticia.', 'Conceptual appointment request form using fictional information.', False),
],
'pqrs-ai': [
(4, 'service task diagram connecting incoming requests, prioritization, summary, suggested classification and human review, abstract documents with no case identifiers', 'Diagrama conceptual de priorización y revisión humana.', 'Conceptual diagram of prioritization and human review.', False),
(5, 'desktop UI mockup of AI recommendations beside an original request panel, four recommendation rows each with a visible edit control icon and a separate grouped apply action, no legible labels', 'Panel conceptual de recomendaciones con controles individuales y acción conjunta.', 'Conceptual recommendations panel with individual controls and a combined action.', False),
(6, 'desktop UI mockup of a public service request priority list, distinct priority indicators and an adjacent abstract summary card, no actual citizen documents', 'Lista conceptual de prioridades y resumen de solicitudes.', 'Conceptual request priority list and summary.', True),
(6, 'desktop UI mockup of an email composer with smart token chips, template preview and a clear review stage, empty recipient field and no actual message content', 'Compositor conceptual de correo dinámico con tokens inteligentes.', 'Conceptual dynamic email composer with smart tokens.', False),
(7, 'conceptual interaction diagram comparing an AI suggestion, a human modification and a proposed undo review state, reversibility shown as a design intention rather than implemented proof', 'Esquema conceptual de control humano; reversión pendiente de verificar.', 'Conceptual human oversight diagram; reversal behavior remains unverified.', False),
],
'video-interview': [
(4, 'candidate journey flow diagram linking role-based questions, a recording step and interview transcription, simple unlabeled sequential nodes', 'Recorrido conceptual de preguntas por rol, video y transcripción.', 'Conceptual journey from role-specific questions to video and transcription.', False),
(5, 'UI state board with recording, error and retry panels for a video interview, generic camera icons and distinct controls, no real candidate image', 'Tablero conceptual de estados: grabación, error y reintento.', 'Conceptual state board: recording, error, and retry.', False),
(6, 'desktop UI mockup of a guided video interview question screen, single question placeholder, blank camera silhouette and step indicator without digits', 'Pantalla conceptual de entrevista guiada, centrada en una pregunta.', 'Conceptual guided interview screen focused on one question.', False),
(6, 'desktop UI mockup pairing an abstract video frame with a transcription panel built from illegible line shapes, no actual recorded interview or candidate data', 'Propuesta conceptual de revisión de video y transcripción.', 'Conceptual proposal for video and transcript review.', False),
(7, 'conceptual recovery flow board for a recording interruption and retry, open decision nodes indicating rules to confirm, no claimed autosave or duration rules', 'Mapa conceptual de recuperación; reglas específicas pendientes de confirmar.', 'Conceptual recovery map; specific rules await confirmation.', False),
],
'ingles-infantil': [
(4, 'child-focused learning journey illustration with connected worlds and levels, friendly landscape paths and clearly separated activity islands, no achievement statistics', 'Mapa conceptual de mundos y niveles de aprendizaje.', 'Conceptual map of learning worlds and levels.', False),
(5, 'child-friendly UI component board with large touch targets, clear visual feedback states, simple audio controls and generous spacing, no accessibility certification badges', 'Tablero conceptual de legibilidad, controles y retroalimentación infantil.', 'Conceptual board of child-focused readability, controls, and feedback.', False),
(6, 'tablet UI mockup of an interactive illustrated story with a friendly fictional character, audio playback controls and clear next-step affordance, no readable story text', 'Propuesta conceptual de cuento interactivo con audio.', 'Conceptual interactive story proposal with audio.', False),
(6, 'playful character customization UI with fictional accessories and an abstract coin reward indicator, no prices or currency labels', 'Propuesta conceptual de personalización del personaje con monedas.', 'Conceptual character customization with coins.', True),
(7, 'multimedia learning storyboard with separate audio, video, story and music tiles, showing AI-supported production as an abstract creative tool, no claims of measured learning gains', 'Storyboard conceptual de recursos multimedia producidos con apoyo de IA.', 'Conceptual storyboard of multimedia resources produced with AI support.', False),
],
'javeriana': [
(4, 'research synthesis board with generic faculty meeting notes, heuristic review markers and university reference layout thumbnails, no logos or internal notes', 'Síntesis conceptual de necesidades de facultades y análisis heurístico.', 'Conceptual synthesis of faculty needs and heuristic review.', False),
(5, 'UI component library board for an academic website, reusable program cards, information sections and inquiry controls in an organized design canvas', 'Tablero conceptual de componentes para páginas académicas.', 'Conceptual component board for academic pages.', False),
(6, 'comparison board of distinct desktop academic program landing pages, undergraduate and graduate page structures, varying editorial hierarchy and abstract course blocks', 'Comparación conceptual de landings por tipo de programa.', 'Conceptual comparison of landing pages by program type.', False),
(6, 'mobile UI mockups for academic program landing pages, stacked content hierarchy, readable spacing and prominent inquiry control, no institutional marks', 'Propuestas conceptuales de versiones móviles de programas.', 'Conceptual mobile versions of program pages.', False),
(7, 'design handoff board connecting academic landing page variants with reusable components and mobile adaptations, no implied analytics results', 'Mapa conceptual de entregables: variantes, componentes y versiones móviles.', 'Conceptual deliverable map: variants, components, and mobile adaptations.', False),
],
'flexi': [
(4, 'graphic campaign exploration board with multiple unbranded footwear key visual directions for a romantic seasonal occasion and a bold sales occasion, no promotional prices', 'Exploración conceptual de key visuals para temporadas especiales.', 'Conceptual key visual exploration for seasonal campaigns.', False),
(5, 'graphic composition diagram showing a single footwear key visual adapted into email, vertical social and square ad formats, consistent imagery and varied cropping', 'Diagrama conceptual de adaptación de una campaña entre formatos.', 'Conceptual diagram of campaign adaptation across formats.', False),
(6, 'email campaign mockup with a large unbranded footwear product photo, modular editorial blocks and abstract call-to-action shapes, no real promotion copy', 'Propuesta conceptual de email de campaña.', 'Conceptual campaign email proposal.', False),
(6, 'animation storyboard in consecutive panels featuring an unbranded shoe product, layered color transitions and distinct motion beats, no platform logos', 'Storyboard conceptual de una pieza animada de campaña.', 'Conceptual storyboard for an animated campaign asset.', False),
(7, 'social advertising asset board of square and vertical footwear compositions with consistent seasonal palette and no actual brand marks or performance charts', 'Selección conceptual de anuncios adaptados a redes.', 'Conceptual selection of social advertising adaptations.', False),
],
'the-bar-colombia': [
(4, 'luxury spirits research moodboard with unbranded bottle silhouettes, rich material textures, refined lighting and abstract ecommerce reference panels, no copied websites', 'Moodboard conceptual de bebidas espirituosas y lenguaje de lujo.', 'Conceptual spirits and luxury visual language moodboard.', False),
(5, 'card sorting and information architecture board, abstract category cards clustered into a navigational tree, no actual research participant responses', 'Representación conceptual de card sorting y arquitectura de información.', 'Conceptual representation of card sorting and information architecture.', False),
(6, 'desktop UI mockup of a premium spirits ecommerce homepage, elegant unbranded bottle still life, spacious editorial hierarchy and curated product cards', 'Propuesta conceptual de página de inicio del ecommerce.', 'Conceptual ecommerce homepage proposal.', False),
(6, 'paired desktop and mobile UI mockups for a premium spirits product page, unbranded bottle photography, product information blocks and clear shopping action', 'Detalle de producto conceptual en escritorio y móvil.', 'Conceptual desktop and mobile product detail.', False),
(7, 'conceptual analytics review board with an abstract heatmap overlay, session recording timeline and generic trend chart beside a design iteration panel, no real analytics or claimed uplift', 'Tablero conceptual de seguimiento e iteración, sin resultados reales.', 'Conceptual monitoring and iteration board without actual results.', True),
],
'previsora': [
(4, 'editorial collaboration process diagram pairing content creation and graphic design before a shared social asset board, no internal messages', 'Diagrama conceptual de colaboración entre contenido y diseño.', 'Conceptual collaboration diagram for content and design.', False),
(5, 'graphic direction board for a generic insurance social presence with varied compositions, illustration treatments and consistent identity cues, no real brand marks', 'Tablero conceptual de variedad visual para redes de seguros.', 'Conceptual visual variety board for insurance social media.', False),
(6, 'social media composition board using abstract insurance-related everyday scenes, varied static layouts and generic content blocks, no policyholder documents', 'Propuestas conceptuales de piezas estáticas para redes.', 'Conceptual static social media assets.', False),
(6, 'conceptual storyboard exploring a dynamic social post and a generic interactive prompt, differentiated states without claiming deployed interaction features', 'Exploración conceptual de piezas dinámicas e interactivas.', 'Conceptual exploration of dynamic and interactive assets.', False),
(7, 'cohesive social media grid combining abstract illustrations and varied editorial framing, no follower counts, engagement charts or performance badges', 'Selección conceptual de piezas coherentes y variadas.', 'Conceptual selection of consistent, varied assets.', False),
],
'peoplepass': [
(4, 'visual communication touchpoint diagram linking social content and physical point-of-purchase materials, no real customer data or company marks', 'Mapa conceptual de soportes digitales y físicos.', 'Conceptual map of digital and physical media.', False),
(5, 'graphic identity adaptation board showing consistent color, spacing and hierarchy across a social tile and a physical display, abstract generic typography marks', 'Tablero conceptual de continuidad de identidad entre soportes.', 'Conceptual board of identity continuity across media.', False),
(6, 'social graphic mockup board with generic employee benefit themed illustrations and varied post compositions, no actual benefit values or personal records', 'Propuesta conceptual de contenido para redes sociales.', 'Conceptual social media content proposal.', False),
(6, 'studio product photograph mockup of unbranded point-of-purchase print materials, tabletop display and leaflet with abstract layouts, realistic paper texture, no invented production specifications', 'Mockup conceptual de material POP, sin especificaciones de impresión confirmadas.', 'Conceptual POP material mockup, without confirmed print specifications.', False),
(7, 'editorial presentation board pairing social graphics with physical communication mockups, consistent visual identity and no sales or audience statistics', 'Selección conceptual que relaciona comunicación digital y física.', 'Conceptual selection connecting digital and physical communication.', False),
]
}

palettes = {
'niibu': 'soft violet, pale mint, warm white and dark charcoal',
'broken-chains': 'charcoal, warm white and restrained electric blue',
'hacienda-citas': 'deep blue, teal, warm white and neutral gray',
'pqrs-ai': 'navy, teal, pale lavender and warm white',
'video-interview': 'deep purple, cool gray and warm white',
'ingles-infantil': 'sunshine yellow, soft turquoise, coral and cream',
'javeriana': 'navy, warm cream, muted gold and neutral gray',
'flexi': 'warm rose, charcoal, cream and seasonal red accents',
'the-bar-colombia': 'deep charcoal, warm ivory, amber and muted gold',
'previsora': 'muted green, warm white, navy and coral accents',
'peoplepass': 'deep teal, warm white, coral and neutral gray',
}
inventory = '''# Inventario de propuestas de imagen

55 imágenes conceptuales pendientes. Cada ID identifica una imagen compartida por ES/EN, no dos imágenes distintas. Los placeholders no son capturas de entregables ni prueba de procesos realizados. Los pies y prompts aclaran los límites. No se han generado imágenes.

| ID | Proyecto | Ubicación (sección) | Proporción | Prompt en inglés | Estado |
| --- | --- | --- | --- | --- | --- |
'''
for slug, items in briefs.items():
    blocks = {}
    for number, (section, subject, es, en, illustrative) in enumerate(items, 1):
        image_id = f'{slug}-{number:02}'
        ratio = '4:3' if number in [2, 4] else '16:9'
        prompt = (f'Create a conceptual {subject}. Style: polished product design editorial illustration with high visual detail and clean edges. '
                  f'Palette: {palettes[slug]}. Composition: balanced focal area, generous margins, {ratio} aspect ratio. '
                  'Use abstract shapes instead of readable text or digits. No real logos, brand marks, personal data, actual client screenshots, or confidential material. '
                  'This is a conceptual reconstruction, not evidence of a delivered screen or an actual research artifact.')
        if illustrative:
            es += ' Datos ilustrativos.'
            en += ' Illustrative data.'
        block = f'''<figure class="img-placeholder" data-ratio="{ratio}" data-id="{image_id}">
  <div class="img-placeholder__box">
    <p class="img-placeholder__prompt">{html.escape(prompt)}</p>
  </div>
  <figcaption lang="es">{html.escape(es)}</figcaption>
  <figcaption lang="en">{html.escape(en)}</figcaption>
</figure>'''
        blocks.setdefault(section, []).append(block)
        inventory += f'| {image_id} | {slug} | {section} | {ratio} | {prompt} | pendiente |\n'
    for lang in ['es', 'en']:
        path = root / 'content/projects' / f'{slug}.{lang}.md'
        text = path.read_text(encoding='utf-8')
        text = re.sub(r'\n\n<figure class="img-placeholder".*?</figure>', '', text, flags=re.S)
        parts = re.split(r'(?=^## )', text, flags=re.M)
        for section, figures in blocks.items():
            parts[section] = parts[section].rstrip() + '\n\n' + '\n\n'.join(figures) + '\n\n'
        path.write_text(''.join(parts).rstrip() + '\n', encoding='utf-8')
(root / 'content/image-prompts.md').write_text(inventory, encoding='utf-8')
print('55 placeholders compartidos en 22 casos; inventario generado.')
