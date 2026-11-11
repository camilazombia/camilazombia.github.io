import metadata from './caseMetadata.json';

export type ProjectId = keyof typeof metadata;
export type ContentLanguage = 'es' | 'en';
const documents = import.meta.glob<string>('../../content/projects/*.md', {
  query: '?raw', import: 'default', eager: true,
});
const introductions = import.meta.glob<string>('../../content/portfolio-intro.*.md', {
  query: '?raw', import: 'default', eager: true,
});

export function isProjectId(id: string): id is ProjectId {
  return Object.hasOwn(metadata, id);
}

export function getCaseContent(id: ProjectId, language: ContentLanguage) {
  const entry = metadata[id];
  const markdown = documents[`../../content/projects/${entry.slug}.${language}.md`];
  if (!markdown) throw new Error(`Missing case content: ${id}/${language}`);
  const summary = markdown.split(/^## /m)[1].split('\n\n')[1].trim();
  return { ...entry[language], description: summary, markdown };
}

export function getIntroduction(language: ContentLanguage, length: 'short' | 'long') {
  const markdown = introductions[`../../content/portfolio-intro.${language}.md`];
  if (!markdown) throw new Error(`Missing introduction: ${language}`);
  return markdown.split(/^## .+\r?\n/m)[length === 'short' ? 1 : 2].trim();
}
