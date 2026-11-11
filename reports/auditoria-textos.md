# Auditoría de textos

Auditoría editorial del código fuente y recursos de texto propios del repositorio. Se excluyen dependencias, dist, Git, archivos binarios y material temporal. Las líneas corresponden al archivo antes de corregirlo; la integración posterior puede desplazarlas o sustituir el bloque completo.

Lectura estricta UTF-8 de los archivos revisados. El documento adjunto también es UTF-8: su apariencia inicial en PowerShell provenía de la decodificación de la consola, no del archivo.

| Archivo | Línea | Texto original | Corrección | Idioma | Tipo de problema |
| --- | --- | --- | --- | --- | --- |
| src/pages/ProjectDetailPage.tsx | 61 | <nav className={styles.breadcrumbs} aria-label={language === 'es' ? 'Ruta de navegaci?n' : 'Breadcrumb'}> | <nav className={styles.breadcrumbs} aria-label={language === 'es' ? 'Ruta de navegación' : 'Breadcrumb'}> | ES | Acento o separador sustituido por ? |
| src/pages/ProjectDetailPage.tsx | 72 | <p>La propuesta explora c?mo transformar una idea en una experiencia clara, coherente y cercana. El recorrido pone atenci?n en la relaci?n entre contenido, jerarqu?a visual y ritmo: cada elemento tiene un lugar y acompa?a a la persona de una secci?n a la siguiente.</p> | <p>La propuesta explora cómo transformar una idea en una experiencia clara, coherente y cercana. El recorrido pone atención en la relación entre contenido, jerarquía visual y ritmo: cada elemento tiene un lugar y acompaña a la persona de una sección a la siguiente.</p> | ES | Acento o separador sustituido por ? |
| src/pages/ProjectDetailPage.tsx | 73 | <p>La selecci?n visual re?ne composiciones generales y detalles para mostrar distintas escalas del proyecto. El contraste entre im?genes amplias y piezas en pareja permite detenerse en cada decisi?n, reconocer conexiones y entender el conjunto sin perder el contexto de esta descripci?n.</p> | <p>La selección visual reúne composiciones generales y detalles para mostrar distintas escalas del proyecto. El contraste entre imágenes amplias y piezas en pareja permite detenerse en cada decisión, reconocer conexiones y entender el conjunto sin perder el contexto de esta descripción.</p> | ES | Acento o separador sustituido por ? |
| src/pages/ProjectDetailPage.tsx | 136 | {!!project.gallery?.length && <div className={styles.imageGallery} aria-label={language === 'es' ? 'Galer?a del proyecto' : 'Project gallery'}> | {!!project.gallery?.length && <div className={styles.imageGallery} aria-label={language === 'es' ? 'Galería del proyecto' : 'Project gallery'}> | ES | Acento o separador sustituido por ? |
| src/pages/ProjectDetailPage.tsx | 140 | <img src={src} alt={${project.name} ? ${index + 1}} loading="lazy" /> | <img src={src} alt={${project.name} · ${index + 1}} loading="lazy" /> | ES | Acento o separador sustituido por ? |

## Criterio editorial

Español latinoamericano neutro e inglés estadounidense. Títulos en estilo oración, nombres de producto sin traducir, comillas tipográficas y punto medio como separador de etiquetas. Evitar guiones largos en la redacción nueva. Las entidades válidas en JSX/SVG no se sustituyen cuando el navegador las interpreta correctamente.

El HTML declara UTF-8 y un idioma inicial en inglés; LanguageProvider actualiza lang y metadatos al cambiar de idioma.

## Dudas y límites

- El ID histórico nibu-english-platform no describe el alcance actual de Niibu. Se conserva para no romper la URL y se corrige el texto visible.
- Adidas y Broken Chains aparecen vinculados en el documento: se presenta Broken Chains como ecommerce de sneakers y Adidas como referencia de la selección previa, sin afirmar contratación directa por la marca.
- No se infieren fechas, miembros del equipo ni métricas. Los datos faltantes se registran en pendientes.md.
- Los textos editoriales genéricos y la galería compartida se sustituirán por los casos específicos en las fases siguientes.
