---
template: overrides/kg.html
shortname: gene-expression-atlas-okn
title: Gene Expression Atlas
description: Selected studies from the Gene Expression Atlas (https://www.ebi.ac.uk/gxa/home).
stats: https://frink.renci.org/kg-stats/gene-expression-atlas-okn
homepage: https://www.ebi.ac.uk/gxa/home
funding: https://www.nsf.gov/awardsearch/showAward?AWD_ID=2535091
sparql: https://frink.apps.renci.org/gene-expression-atlas-okn/sparql
tpf: https://frink.apps.renci.org/ldf/gene-expression-atlas-okn
frink-options:
  lakefs-repo: gene-expression-atlas-okn
  documentation-path: gene-expression-atlas-okn
contacts:
- email: asu@scripps.edu
  github: "andrewsu"
  label: "Andrew Su"
- email: plwhetzel@gmail.com
  github: "twhetzel"
  label: "Trish Whetzel" 
---

Selected studies from the Gene Expression Atlas (https://www.ebi.ac.uk/gxa/home).

The Gene Expression Atlas Open Knowledge Network (gene-expression-atlas-okn) is a semantic knowledge graph containing selected studies from the EMBL-EBI Gene Expression Atlas, a curated database of gene expression experiments. This knowledge graph integrates 243 studies encompassing 797 assays that profile expression patterns across 152,879 genes. The data captures differential gene expression measurements with statistical metrics (log2 fold changes, adjusted p-values) linked to diverse biological contexts including anatomical entities, cell types, diseases, developmental life stages, and biological sex categories.

Built using Biolink Model ontology standards, the knowledge graph connects genes to biological processes, molecular pathways, and protein domains through expression associations. Each study includes comprehensive metadata such as experimental factors, technology platforms, PubMed references, and contrast comparisons between test and reference groups. This structured representation enables systematic exploration of how gene expression varies across tissues, diseases, developmental stages, and experimental conditions, supporting integrative genomics research and cross-study meta-analyses.
