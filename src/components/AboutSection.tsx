import { motion, useReducedMotion } from 'framer-motion';
import { ArrowDown, ArrowUpRight, Download } from 'lucide-react';
import resume from '../data/resume.json';
import { useLanguage } from '../i18n/LanguageContext';
import styles from './AboutSection.module.css';
import { getIntroduction } from '../data/caseContent';
import { MarkdownContent } from './MarkdownContent';

const memories = [
  {
    "file": "zombiagomez_Transform_the_uploaded_photo_into_a_sophisticated_6831026f-dd1a-42b4-8618-32e8ade5632c_2.png",
    "es": "Mi retrato con maquillaje y gorro de fiesta",
    "en": "My portrait with makeup and a party hat"
  },
  {
    "file": "zombiagomez_Transform_the_uploaded_photo_into_a_sophisticated_8fb75383-745a-4f9b-acab-cdbd91775805_1.png",
    "es": "Mis dos gatitos en un collage",
    "en": "A collage of my two kittens"
  },
  {
    "file": "zombiagomez_Transform_the_uploaded_photo_into_a_sophisticated_3d157a16-5c2d-40e5-a8f2-6a823bc770fa_1.png",
    "es": "Retrato de mi perrito en un collage",
    "en": "A collage portrait of my dog"
  },
  {
    "file": "zombiagomez_Transform_the_uploaded_photo_into_a_sophisticated_f1737e3d-5def-42e2-934b-72aeee6bdbc9_0.png",
    "es": "Un paseo al atardecer en Cartagena",
    "en": "A sunset walk in Cartagena"
  },
  {
    "file": "zombiagomez_Transform_the_uploaded_photo_into_a_sophisticated_994ef9f5-b20d-4e2c-ac2f-d05f29241c9c_2.png",
    "es": "Un recuerdo junto a un helado gigante",
    "en": "A memory next to a giant ice cream cone"
  }
];

export function AboutSection() {
  const { language } = useLanguage();
  const es = language === 'es';
  const reduced = useReducedMotion();
  return <article className={styles.about} id="about">
    <section className={styles.introduction} aria-labelledby="about-title">
      <motion.div className={styles.portrait} initial={reduced ? false : { opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }}>
        <div className={styles.profilePhoto}><img src={`${import.meta.env.BASE_URL}images/projects/WhatsApp%20Image%202026-11-04%20at%208.48.46%20PM.jpeg`} alt={es ? 'Camila de niña con un gorro de cumpleaños' : 'Camila as a child wearing a birthday hat'} /></div>
      </motion.div>
      <motion.div className={styles.bio} initial={reduced ? false : { opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: .1, duration: .6 }}>
        <p className={styles.eyebrow}>{es ? 'Un poco sobre mí' : 'A little about me'}</p>
        <h1 id="about-title">{es ? 'Hola, soy Camila.' : 'Hi, I’m Camila.'}</h1>
        <MarkdownContent markdown={getIntroduction(language, 'long')} language={language} />
        <div className={styles.bioActions}><a className={styles.cv} href={`${import.meta.env.BASE_URL}cv/Laura-Camila-Gomez-CV-${language}.pdf`} download><Download size={16} aria-hidden="true" />{es ? 'Descargar mi CV' : 'Download my CV'}</a><a className={styles.experienceLink} href="#experience">{es ? 'Mi experiencia' : 'My experience'}<ArrowDown size={16} aria-hidden="true" /></a></div>
        <p className={styles.education}>{es ? 'Diseño Gráfico · Universitaria de Colombia' : 'Graphic Design · Universitaria de Colombia'}<br />{es ? 'Máster en Gráfico Digital · UNIR' : 'Master’s in Digital Graphic Design · UNIR'}</p>
      </motion.div>
    </section>
    <section className={styles.experience} id="experience" aria-labelledby="experience-title">
      <header className={styles.sectionHeader}><div><p className={styles.eyebrow}>{es ? 'El camino hasta aquí' : 'The journey so far'}</p><h2 id="experience-title">{es ? 'Mi experiencia' : 'My experience'}</h2></div><span>{es ? 'Diseño gráfico → UX/UI → Producto' : 'Graphic design → UX/UI → Product'}</span></header>
      <div className={styles.jobs}>{[...resume].sort((a,b) => b.startDate.localeCompare(a.startDate)).map(job => <details className={styles.job} key={job.company}>
        <summary><span className={styles.jobDate}>{job.date[language].split(' · ')[0]}</span><span className={styles.jobTitle}><strong>{job.company}</strong><span>{job.role}</span></span><ArrowUpRight size={20} aria-hidden="true" /></summary>
        <div className={styles.jobDescription}><p>{job.date[language]}</p>{job.summary && <p>{job.summary[language]}</p>}{job.clients && <p>{es ? 'Clientes: ' : 'Clients: '}{job.clients.join(' · ')}</p>}</div>
      </details>)}</div>
    </section>
    <section className={styles.memories} aria-label={es ? 'Galería de fotos' : 'Photo gallery'}>
      <div className={styles.memoryGallery}>
        <div className={styles.memoryTrack}>
          {[0, 1].map(copy => <div className={styles.memoryGroup} key={copy} aria-hidden={copy === 1 ? true : undefined}>
            {memories.map(photo => <div className={styles.memoryCard} key={photo.file}>
              <img className={styles.memoryPhoto} src={`${import.meta.env.BASE_URL}images/about/${photo.file}`} alt={copy === 1 ? '' : photo[language]} loading="lazy" decoding="async" />
            </div>)}
          </div>)}
        </div>
      </div>
    </section>
  </article>;
}

