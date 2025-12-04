import mermaid from 'https://unpkg.com/mermaid@10.4.0/dist/mermaid.esm.min.mjs';

mermaid.initialize({
    maxTextSize: 500000
});

// Important: necessary to make it visible to Material for MkDocs
window.mermaid = mermaid;

