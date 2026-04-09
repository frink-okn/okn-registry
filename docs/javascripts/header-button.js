(function () {
  console.log('header-button.js: loaded');
  const STYLE_ID = 'header-custom-btn-style';
  const BTN_CLASS = 'header-custom-btn';
  const CONTAINER_CLASS = 'header-custom-container';
  const styleText = `
    .md-header__inner { display: flex; align-items: center; }
    header.md-header, .md-header__inner { position: relative; }
    .${CONTAINER_CLASS} { margin-left: auto; display: flex; align-items: center; gap: 0.4rem; }
    .${BTN_CLASS} { text-decoration: none; color: inherit; padding: 0.05rem 1.8rem; border-radius: 4px; display: inline-flex; align-items: center; justify-content: center; background: rgba(255,255,255,0.12); border: 1px solid rgba(255,255,255,0.24); font-size: 0.9rem; letter-spacing: 0.01em; min-width: 10rem; }
    .${BTN_CLASS}:hover { background: rgba(255,255,255,0.2); }
    @media (max-width: 768px) { .${CONTAINER_CLASS} { display: none; } }
  `;
  function injectStyle() {
    if (document.head.querySelector(`#${STYLE_ID}`)) return;
    const s = document.createElement('style');
    s.id = STYLE_ID;
    s.textContent = styleText;
    document.head.appendChild(s);
  }
  function createButton() {
    const a = document.createElement('a');
    a.href = 'https://frink.apps.renci.org';
    a.target = '_blank';
    a.className = `md-button ${BTN_CLASS}`;
    a.setAttribute('aria-label', 'Query the OKN');
    a.textContent = 'Query the OKN';
    return a;
  }
  function insertRightAligned() {
    const headerRow = document.querySelector('.md-header__inner');
    if (!headerRow) return false;
    if (headerRow.querySelector(`.${CONTAINER_CLASS}`)) return true;
    const container = document.createElement('div');
    container.className = CONTAINER_CLASS;
    container.appendChild(createButton());
    headerRow.appendChild(container);
    console.log('header-button.js: inserted right-aligned button');
    return true;
  }
  function bootstrap() {
    injectStyle();
    if (insertRightAligned()) return;
    const obs = new MutationObserver((mutations, o) => {
      if (insertRightAligned()) o.disconnect();
    });
    const root = document.querySelector('body') || document.documentElement;
    if (root) obs.observe(root, { childList: true, subtree: true });
    setTimeout(() => { insertRightAligned(); obs.disconnect(); }, 3000);
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', bootstrap);
  } else {
    bootstrap();
  }
})();