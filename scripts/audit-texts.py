"""Repair confirmed text corruption and record source locations before editing."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
replacements = {
    'navegaci?n': 'navegación', 'c?mo': 'cómo', 'atenci?n': 'atención',
    'relaci?n': 'relación', 'jerarqu?a': 'jerarquía', 'acompa?a': 'acompaña',
    'secci?n': 'sección', 'selecci?n': 'selección', 're?ne': 'reúne',
    'im?genes': 'imágenes', 'decisi?n': 'decisión', 'descripci?n': 'descripción',
    'Galer?a': 'Galería', '${project.name} ? ${index + 1}': '${project.name} · ${index + 1}',
}
rows = []
paths = [root / 'index.html', root / 'README.md', *sorted((root / 'src').rglob('*')),
         *sorted((root / 'public').rglob('*'))]
for path in paths:
    if not path.is_file() or path.suffix not in {'.tsx', '.ts', '.js', '.json', '.html', '.css', '.md', '.txt', '.svg'}:
        continue
    text = path.read_bytes().decode('utf-8', errors='strict')
    original = text
    for number, line in enumerate(original.splitlines(), 1):
        fixed = line
        for before, after in replacements.items():
            fixed = fixed.replace(before, after)
        if fixed != line:
            def cell(s):
                return s.strip().replace('|', '&#124;').replace('`', '')
            rows.append(f'| {path.relative_to(root).as_posix()} | {number} | {cell(line)} | {cell(fixed)} | ES | Acento o separador sustituido por ? |')
    for before, after in replacements.items():
        text = text.replace(before, after)
    if text != original:
        path.write_text(text, encoding='utf-8', newline='\n')
reports = root / 'reports'
reports.mkdir(exist_ok=True)
(reports / 'auditoria-textos.md').write_text('''# Auditoría de textos

Auditoría editorial del código fuente y recursos de texto propios del repositorio. Se excluyen dependencias, dist, Git, archivos binarios y material temporal. Las líneas corresponden al archivo antes de corregirlo; la integración posterior puede desplazarlas o sustituir el bloque completo.

Lectura estricta UTF-8 de los archivos revisados. El documento adjunto también es UTF-8: su apariencia inicial en PowerShell provenía de la decodificación de la consola, no del archivo.

| Archivo | Línea | Texto original | Corrección | Idioma | Tipo de problema |
| --- | --- | --- | --- | --- | --- |
''' + '\n'.join(rows) + '''

## Criterio editorial

Español latinoamericano neutro e inglés estadounidense. Títulos en estilo oración, nombres de producto sin traducir, comillas tipográficas y punto medio como separador de etiquetas. Evitar guiones largos en la redacción nueva. Las entidades válidas en JSX/SVG no se sustituyen cuando el navegador las interpreta correctamente.

El HTML declara UTF-8 y un idioma inicial en inglés; LanguageProvider actualiza lang y metadatos al cambiar de idioma.

## Dudas y límites

- El ID histórico nibu-english-platform no describe el alcance actual de Niibu. Se conserva para no romper la URL y se corrige el texto visible.
- Adidas y Broken Chains aparecen vinculados en el documento: se presenta Broken Chains como ecommerce de sneakers y Adidas como referencia de la selección previa, sin afirmar contratación directa por la marca.
- No se infieren fechas, miembros del equipo ni métricas. Los datos faltantes se registran en pendientes.md.
- Los textos editoriales genéricos y la galería compartida se sustituirán por los casos específicos en las fases siguientes.
''', encoding='utf-8')
(reports / 'glosario.md').write_text('''# Glosario ES/EN

| Español | US English | Uso |
| --- | --- | --- |
| diseño UX/UI | UX/UI design | Disciplina; no convertir todo trabajo gráfico en investigación UX |
| sistema de diseño | design system | Tokens, componentes y plantillas |
| flujo principal (happy path) | happy path | Primera mención bilingüe en ES |
| flujos alternos | alternative paths | Rutas distintas del flujo principal |
| casos límite | edge cases | Comportamientos excepcionales |
| billetera | wallet | Origen y estado de ingresos |
| agendamiento de citas | appointment scheduling | Reserva y gestión de horarios |
| sede | office | Sede operativa de Hacienda |
| PQRS | PQRS | Mantener la sigla del sistema; no inferir su expansión institucional |
| radicado | case record | Registro de una solicitud, nunca identificadores reales |
| dependencia | department | Unidad responsable |
| tokens inteligentes | smart tokens | Variables del correo, distintos de tokens de diseño |
| pagos en depósito | escrow payments | No afirmar pagos realizados |
| mapa de calor | heatmap | Seguimiento, no prueba de mejora por sí solo |
| material POP | point-of-purchase materials | Piezas para puntos de contacto físicos |
| página de aterrizaje | landing page | Landing pages en nombres de proyecto |
| Niibu PRO: Get Booked | Niibu PRO: Get Booked | Nombre propio |
| Niibu: Personal AI Concierge | Niibu: Personal AI Concierge | Nombre propio |
| Niibu: Creator Studio | Niibu: Creator Studio | Nombre propio |
| datos ilustrativos | illustrative data | Cifras ficticias solo en propuestas visuales |
| pendiente | pending | Estado inicial del inventario; mantener pendiente como valor técnico |
''', encoding='utf-8')
print(f'{len(rows)} líneas corregidas; reportes creados.')
