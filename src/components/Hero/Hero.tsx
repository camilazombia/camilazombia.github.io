import { Link } from 'react-router-dom';
import { Navbar } from '../Navbar';
import { Footer } from '../Footer';
import { useLanguage } from '../../i18n/LanguageContext';
import { whatsappUrl } from '../../data/contact';
import { ArrowUpRight } from 'lucide-react';
import styles from './Hero.module.css';
import { getIntroduction } from '../../data/caseContent';

export function Hero() {
  const { language, copy } = useLanguage();
  const es = language === 'es';
  const contact = es ? 'Contáctame' : 'Contact me';
  return <main className={styles.home}>
    <Navbar />
  <img className={styles.cornerBow} src={`${import.meta.env.BASE_URL}images/hero/bow-pearl.png`} alt="" aria-hidden="true" />
    <section className={styles.composition} aria-label={copy.heroTitle}>
      <img className={styles.cornerFan} src={`${import.meta.env.BASE_URL}images/hero/fan-pink.png`} alt="" aria-hidden="true" />
      <h1 className={`${styles.title} ${es ? styles.spanishTitle : ''}`}>
        <span className={styles.product}>{es ? 'DISEÑADORA' : 'PRODUCT'}</span>
        <span className={styles.designer}>{es ? 'DE PRODUCTO' : 'DESIGNER'}</span>
      </h1>

      <Link className={`${styles.portraitLink} ${styles.projects}`} to="/projects" aria-label={copy.projects}><img src={`${import.meta.env.BASE_URL}images/home/projects-portrait.png`} alt={es ? 'Galgo con corona en un marco ornamental rosa' : 'Crowned greyhound in an ornate pink frame'} /><span>{copy.projects}</span></Link>
      <Link className={`${styles.portraitLink} ${styles.about}`} to="/about" aria-label={copy.about}><img src={`${import.meta.env.BASE_URL}images/home/about-portrait.png`} alt="Laura Camila Gómez" /><span>{copy.about}</span></Link>
      <a className={`${styles.portraitLink} ${styles.contact}`} href={whatsappUrl(language)} target="_blank" rel="noopener noreferrer" aria-label={contact}><img src={`${import.meta.env.BASE_URL}images/home/contact-portrait.png`} alt={es ? 'Retrato de una niña con muñecas en un marco ornamental' : 'Portrait of a girl with dolls in an ornate frame'} /><span>{contact}</span></a>
    </section>
    <p className={styles.intro}>{getIntroduction(language, 'short').split('**').map((text, index) => index % 2 ? <strong key={index}>{text}</strong> : text)}</p>
    <nav className={styles.actions} aria-label={es ? 'Explorar el portafolio' : 'Explore the portfolio'}>
      <Link className={styles.primaryAction} to="/projects"><span>{es ? 'Ver proyectos' : 'View projects'}</span><ArrowUpRight size={18} aria-hidden="true" /></Link>
      <Link className={styles.secondaryAction} to="/about"><span>{es ? 'Sobre mí' : 'About me'}</span><ArrowUpRight size={18} aria-hidden="true" /></Link>
    </nav>
    <Footer />  </main>;
}





