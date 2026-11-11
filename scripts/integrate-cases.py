from pathlib import Path
root = Path(__file__).resolve().parents[1]

def edit(name, before, after):
    path = root / name
    text = path.read_text(encoding='utf-8')
    assert before in text, (name, before)
    path.write_text(text.replace(before, after), encoding='utf-8', newline='\n')

edit('src/data/projects.ts', "selection.map((project)", "selection.filter(project => !['remote-latinos-website', 'devar-colombia-website'].includes(project.id)).map((project)")
edit('src/data/projects.ts', 'Conjunto de aplicaciones de la plataforma de inglés de Niibu.', 'Ecosistema de aplicaciones con IA de Niibu para profesionales, uso personal y creadores.')
edit('src/components/CareerTimeline.tsx', "project: 'remote-latinos-website'", "project: 'video-interview'")
for name in ['ProjectsGallery', 'FeaturedProjectsGallery', 'CareerTimeline']:
    edit(f'src/components/{name}.tsx', "import { projects } from '../data/projects';", "import { useProjects } from '../data/localizedProjects';")
    marker = {'ProjectsGallery': '  const related = Boolean(excludeProjectId);', 'FeaturedProjectsGallery': '  const { copy, language } = useLanguage();', 'CareerTimeline': '  const { language, copy } = useLanguage();'}[name]
    edit(f'src/components/{name}.tsx', marker, '  const projects = useProjects();\n' + marker)
edit('src/components/ProjectTransition.tsx', "import { projects, type Project } from '../data/projects';", "import type { Project } from '../data/projects';\nimport { useProjects } from '../data/localizedProjects';")
edit('src/components/ProjectTransition.tsx', '  const navigate = useNavigate();', '  const projects = useProjects();\n  const navigate = useNavigate();')
for name in ['ProjectCard', 'ProjectThumbnail', 'ProjectStory']:
    path = root / f'src/components/{name}.tsx'
    text = path.read_text(encoding='utf-8')
    text = "import { localizeProject } from '../data/localizedProjects';\n" + text
    if name == 'ProjectCard':
        text = text.replace('  const { copy } = useLanguage();', '  const { copy, language } = useLanguage();\n  project = localizeProject(project, language);')
        text = text.replace('aria-label={`View project: ${project.name}`}', 'aria-label={`${copy.viewProject}: ${project.name}`}')
    elif name == 'ProjectStory':
        text = text.replace('  const es = language', '  project = localizeProject(project, language);\n  const es = language')
    else:
        text = "import { useLanguage } from '../i18n/LanguageContext';\n" + text
        # Insert before first hook/body statement, irrespective of formatting.
        text = text.replace('  const reducedMotion', '  const { language } = useLanguage();\n  project = localizeProject(project, language);\n  const reducedMotion')
    path.write_text(text, encoding='utf-8', newline='\n')

edit('src/components/Hero/Hero.tsx', "import styles from './Hero.module.css';", "import styles from './Hero.module.css';\nimport { getIntroduction } from '../../data/caseContent';")
path = root / 'src/components/Hero/Hero.tsx'
text = path.read_text(encoding='utf-8')
lines = text.splitlines()
lines = ['    <p className={styles.intro}>{getIntroduction(language, \'short\')}</p>' if '<p className={styles.intro}>' in line else line for line in lines]
path.write_text('\n'.join(lines) + '\n', encoding='utf-8')
edit('src/components/AboutSection.tsx', "import styles from './AboutSection.module.css';", "import styles from './AboutSection.module.css';\nimport { getIntroduction } from '../data/caseContent';\nimport { MarkdownContent } from './MarkdownContent';")
path = root / 'src/components/AboutSection.tsx'
text = path.read_text(encoding='utf-8')
start = text.index('        <p className={styles.lead}>')
end = text.index('        <div className={styles.bioActions}>', start)
text = text[:start] + "        <MarkdownContent markdown={getIntroduction(language, 'long')} language={language} />\n" + text[end:]
path.write_text(text, encoding='utf-8', newline='\n')
print('Galerías, portadas, trayectoria e introducciones integradas.')
