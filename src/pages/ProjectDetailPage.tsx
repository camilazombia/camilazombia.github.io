import { useEffect, useRef, useState } from 'react';
import { motion, useReducedMotion } from 'framer-motion';
import { ArrowLeft } from 'lucide-react';
import { Link, useParams } from 'react-router-dom';
import { useProjects } from '../data/localizedProjects';
import { getCaseContent, isProjectId } from '../data/caseContent';
import { useLanguage } from '../i18n/LanguageContext';
import { MarkdownContent } from '../components/MarkdownContent';
import { ProjectThumbnail } from '../components/ProjectThumbnail';
import { ProjectsGallery } from '../components/ProjectsGallery';
import styles from './ProjectDetailPage.module.css';

export function ProjectDetailPage() {
  const { copy, language } = useLanguage();
  const { projectId } = useParams();
  const projects = useProjects();
  const project = projects.find(item => item.id === projectId);
  const content = project && isProjectId(project.id) ? getCaseContent(project.id, language) : undefined;
  const reduceMotion = useReducedMotion();
  const copyRef = useRef<HTMLDivElement>(null);
  const [stickyTop, setStickyTop] = useState(24);

  useEffect(() => {
    const element = copyRef.current;
    if (!element) return;
    const measure = () => setStickyTop(Math.min(24, window.innerHeight - element.offsetHeight - 24));
    const observer = new ResizeObserver(measure);
    observer.observe(element);
    window.addEventListener('resize', measure);
    measure();
    return () => { observer.disconnect(); window.removeEventListener('resize', measure); };
  }, [projectId, language]);

  useEffect(() => {
    if (!project) return;
    const title = `${project.name} | ${copy.title}`;
    document.title = title;
    document.querySelector('meta[name="description"]')?.setAttribute('content', project.description);
    document.querySelector('meta[property="og:title"]')?.setAttribute('content', title);
    document.querySelector('meta[property="og:description"]')?.setAttribute('content', project.description);
    return () => {
      document.title = copy.title;
      document.querySelector('meta[name="description"]')?.setAttribute('content', copy.description);
      document.querySelector('meta[property="og:title"]')?.setAttribute('content', copy.title);
      document.querySelector('meta[property="og:description"]')?.setAttribute('content', copy.description);
    };
  }, [project?.name, project?.description, copy]);

  if (!project || !content) return <main className={styles.page}>
    <div className={styles.missing}>
      <Link to="/" className={styles.brand}>Camila <em>Gómez</em></Link>
      <h1>{copy.projectNotFound}</h1>
      <Link to="/projects" className={styles.backLink}><ArrowLeft size={16} aria-hidden="true" /> {copy.backToPortfolio}</Link>
    </div>
  </main>;

  return <main className={styles.page} key={projectId}>
    <div className={styles.shell}>
      <section className={styles.hero} aria-labelledby="project-title">
        <motion.div className={styles.heroCopy} ref={copyRef} style={{ top: stickyTop }}
          initial={reduceMotion ? false : { opacity: 0, y: 24 }} animate={{ opacity: 1, y: 0 }}
          transition={{ duration: .5 }}>
          <nav className={styles.breadcrumbs} aria-label={language === 'es' ? 'Ruta de navegación' : 'Breadcrumb'}>
            <ol>
              <li><Link to="/">{language === 'es' ? 'Inicio' : 'Home'}</Link></li>
              <li><Link to="/projects">{copy.projects}</Link></li>
              <li aria-current="page">{project.name}</li>
            </ol>
          </nav>
          <h1 id="project-title">{project.name}</h1>
          <p className={styles.summary}>{project.description}</p>
          <dl className={styles.metadata}>
            <div><dt>{copy.role}</dt><dd>{project.role}</dd></div>
            <div><dt>{language === 'es' ? 'Proyecto' : 'Project'}</dt><dd>{project.category}</dd></div>
          </dl>
        </motion.div>
        <div className={styles.visualColumn}>
          <div className={styles.heroImage} data-project-hero><ProjectThumbnail project={project} eager /></div>
          <MarkdownContent markdown={content.markdown} language={language} />
        </div>
      </section>
      <ProjectsGallery excludeProjectId={project.id} />
    </div>
  </main>;
}
