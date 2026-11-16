import { useLanguage } from '../i18n/LanguageContext';
import { localizeProject } from '../data/localizedProjects';
import { useReducedMotion } from 'framer-motion';
import type { Project } from '../data/projects';
import styles from './ProjectThumbnail.module.css';
import { useEffect, useRef, useState } from 'react';

export function ProjectThumbnail({ project, eager = false }: { project: Project; eager?: boolean }) {
  const { language } = useLanguage();
  project = localizeProject(project, language);
  const reducedMotion = useReducedMotion();
  const videoRef = useRef<HTMLVideoElement>(null);
  const [nearby, setNearby] = useState(false);
  useEffect(() => {
    const video = videoRef.current;
    if (!video) return;
    const observer = new IntersectionObserver(([entry]) => {
      if (entry.isIntersecting) setNearby(true);
    }, { rootMargin: '200px' });
    const playback = new IntersectionObserver(([entry]) => {
      if (entry.isIntersecting && !document.hidden && !reducedMotion) void video.play().catch(() => {});
      else video.pause();
    });
    const visibility = () => {
      if (document.hidden) video.pause();
      else { const rect = video.getBoundingClientRect(); if (!reducedMotion && rect.bottom > 0 && rect.top < innerHeight && rect.right > 0 && rect.left < innerWidth) void video.play().catch(() => {}); }
    };
    observer.observe(video);
    playback.observe(video);
    document.addEventListener('visibilitychange', visibility);
    return () => { observer.disconnect(); playback.disconnect(); document.removeEventListener('visibilitychange', visibility); };
  }, [project.animatedCover, reducedMotion, nearby]);
  if (project.animatedCover) return <video ref={videoRef} className={styles.capture} src={nearby ? project.animatedCover : undefined} poster={project.thumbnail} onLoadedMetadata={event => { event.currentTarget.defaultPlaybackRate = project.playbackRate ?? 1; event.currentTarget.playbackRate = project.playbackRate ?? 1; }} loop muted playsInline controls={!!reducedMotion} preload={nearby ? 'metadata' : 'none'} aria-label={project.name} />;
  if (project.thumbnail) return <img className={styles.capture} src={project.thumbnail} alt="" loading={eager ? 'eager' : 'lazy'} decoding="async" />;
  return <div className={styles.cover} aria-hidden="true"><span>{project.category}</span><strong>{project.name}</strong><span>Camila Gómez · UX/UI &amp; Design</span></div>;
}


