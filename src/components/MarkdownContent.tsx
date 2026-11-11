import { marked } from 'marked';
import DOMPurify from 'dompurify';
import { useMemo } from 'react';
import './MarkdownContent.css';

/** Only repository-authored Markdown is rendered; HTML is still sanitized. */
export function MarkdownContent({ markdown, language, className = '' }: {
  markdown: string; language: 'es' | 'en'; className?: string;
}) {
  const html = useMemo(() => DOMPurify.sanitize(marked.parse(markdown, { async: false }), {
    ALLOWED_TAGS: ['h1', 'h2', 'h3', 'h4', 'p', 'ul', 'ol', 'li', 'strong', 'em', 'a', 'br', 'figure', 'div', 'figcaption', 'span'],
    ALLOWED_ATTR: ['class', 'href', 'lang', 'data-id', 'data-ratio', 'aria-label'],
  }), [markdown]);
  return <div className={`markdown-content ${className}`} lang={language} dangerouslySetInnerHTML={{ __html: html }} />;
}
