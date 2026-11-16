import { marked } from 'marked';
import DOMPurify from 'dompurify';
import { useEffect, useMemo, useRef, useState } from 'react';
import { createPortal } from 'react-dom';
import { ChevronLeft, ChevronRight, X } from 'lucide-react';
import './MarkdownContent.css';

/** Only repository-authored Markdown is rendered; HTML is still sanitized. */
export function MarkdownContent({ markdown, language, className = '' }: {
  markdown: string; language: 'es' | 'en'; className?: string;
}) {
  const html = useMemo(() => DOMPurify.sanitize(marked.parse(markdown.replaceAll('src="/images/gallery/', `src="${import.meta.env.BASE_URL}images/gallery/`), { async: false }), {
    ALLOWED_TAGS: ['h1', 'h2', 'h3', 'h4', 'p', 'ul', 'ol', 'li', 'strong', 'em', 'a', 'br', 'figure', 'div', 'figcaption', 'span', 'img'],
    ALLOWED_ATTR: ['class', 'href', 'lang', 'data-id', 'data-ratio', 'aria-label', 'src', 'alt', 'loading', 'decoding'],
  }), [markdown]);
  const container = useRef<HTMLDivElement>(null);
  const dialog = useRef<HTMLDialogElement>(null);
  const [gallery, setGallery] = useState<{ src: string; alt: string }[]>([]);
  const [active, setActive] = useState(0);
  const open = gallery.length > 0;
  const spanish = language === 'es';
  const imageHtml = useMemo(() => {
    const template = document.createElement('template');
    template.innerHTML = html;
    template.content.querySelectorAll('img').forEach((img, index) => {
      const button = document.createElement('button');
      button.type = 'button';
      button.className = 'case-image-open';
      button.dataset.imageIndex = String(index);
      button.setAttribute('aria-label', spanish ? `Ampliar imagen ${index + 1}` : `Enlarge image ${index + 1}`);
      img.replaceWith(button);
      button.append(img);
    });
    return template.innerHTML;
  }, [html, spanish]);

  useEffect(() => {
    if (!open) return;
    const element = dialog.current;
    const previousOverflow = document.body.style.overflow;
    element?.showModal();
    document.body.style.overflow = 'hidden';
    return () => {
      element?.close();
      document.body.style.overflow = previousOverflow;
    };
  }, [open]);

  const move = (direction: number) => setActive(index => (index + direction + gallery.length) % gallery.length);
  return <>
    <div ref={container} className={`markdown-content ${className}`} lang={language}
      onClick={event => {
        const button = (event.target as HTMLElement).closest<HTMLButtonElement>('.case-image-open');
        if (!button || !container.current) return;
        const images = Array.from(container.current.querySelectorAll('img')).map(img => ({ src: img.currentSrc || img.src, alt: img.alt }));
        setActive(Number(button.dataset.imageIndex));
        setGallery(images);
      }}
      dangerouslySetInnerHTML={{ __html: imageHtml }} />
    {createPortal(<dialog ref={dialog} className="project-lightbox"
      aria-label={spanish ? 'Galer?a de im?genes del proyecto' : 'Project image gallery'}
      onCancel={() => setGallery([])} onClose={() => setGallery([])}
      onClick={event => { if (event.target === event.currentTarget) setGallery([]); }}
      onKeyDown={event => {
        if (event.key === 'ArrowLeft') { event.preventDefault(); move(-1); }
        if (event.key === 'ArrowRight') { event.preventDefault(); move(1); }
      }}>
      <button type="button" className="project-lightbox-close" autoFocus onClick={() => setGallery([])} aria-label={spanish ? 'Cerrar' : 'Close'}><X /></button>
      {open && <>
        <img className="project-lightbox-image" src={gallery[active].src} alt={gallery[active].alt} />
        {gallery.length > 1 && <>
          <button type="button" className="project-lightbox-prev" onClick={() => move(-1)} aria-label={spanish ? 'Imagen anterior' : 'Previous image'}><ChevronLeft /></button>
          <button type="button" className="project-lightbox-next" onClick={() => move(1)} aria-label={spanish ? 'Imagen siguiente' : 'Next image'}><ChevronRight /></button>
        </>}
        <span className="project-lightbox-count" aria-live="polite" aria-atomic="true">{active + 1} / {gallery.length}</span>
      </>}
    </dialog>, document.body)}
  </>;
}
