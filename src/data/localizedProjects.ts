import { projects, type Project } from './projects';
import { getCaseContent, isProjectId, type ContentLanguage } from './caseContent';
import { useLanguage } from '../i18n/LanguageContext';

export function localizeProject(project: Project, language: ContentLanguage): Project {
  if (!isProjectId(project.id)) return project;
  const { markdown: _markdown, ...copy } = getCaseContent(project.id, language);
  return { ...project, ...copy };
}

export function useProjects() {
  const { language } = useLanguage();
  return projects.map(project => localizeProject(project, language));
}
