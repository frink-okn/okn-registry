---
template: overrides/kg.html
shortname: gene-expression-atlas-okn
title: Gene Expression Atlas
description: Query pre-computed differential gene expression (log2 fold changes and adjusted p-values) for genes across diseases, tissues, cell types, developmental stages, and sex, drawn from a curated selection of 243 EMBL-EBI Expression Atlas studies. Use this graph to retrieve computed differential-expression results and expression associations for the studies it includes. It is a hand-picked subset, NOT a comprehensive index of the gene-expression datasets available for a given disease — to discover the full set of datasets for a condition (for example when assembling studies for your own pooled or meta-analysis), use a dataset-discovery index such as the NIAID Data Ecosystem (nde) graph.
stats: https://registry.okn.us/kg-stats/gene-expression-atlas-okn
homepage: https://www.ebi.ac.uk/gxa/home
funding: https://www.nsf.gov/awardsearch/showAward?AWD_ID=2535091
sparql: https://apps.okn.us/gene-expression-atlas-okn/sparql
tpf: https://apps.okn.us/ldf/gene-expression-atlas-okn
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
license: "https://creativecommons.org/licenses/by/4.0/"
---

Selected studies from the Gene Expression Atlas (https://www.ebi.ac.uk/gxa/home).

The Gene Expression Atlas Open Knowledge Network (gene-expression-atlas-okn) is a semantic knowledge graph containing selected studies from the EMBL-EBI Gene Expression Atlas, a curated database of gene expression experiments. This knowledge graph integrates 243 studies encompassing 797 assays that profile expression patterns across 152,879 genes. The data captures differential gene expression measurements with statistical metrics (log2 fold changes, adjusted p-values) linked to diverse biological contexts including anatomical entities, cell types, diseases, developmental life stages, and biological sex categories. These 243 studies are a curated *subset* of the EMBL-EBI Expression Atlas, not a comprehensive census of gene-expression experiments; the graph is therefore best used to retrieve computed differential-expression results for the studies it contains, rather than to enumerate every dataset that exists for a given disease.

Built using Biolink Model ontology standards, the knowledge graph connects genes to biological processes, molecular pathways, and protein domains through expression associations. Each study includes comprehensive metadata such as experimental factors, technology platforms, PubMed references, and contrast comparisons between test and reference groups. This structured representation enables systematic exploration of how gene expression varies across tissues, diseases, developmental stages, and experimental conditions, supporting integrative genomics research and the comparison of pre-computed differential-expression results across the studies included in this atlas. For discovering the broader landscape of datasets available for a disease across repositories such as NCBI GEO — for example to assemble studies for a new pooled or meta-analysis — use a dataset-discovery index such as the NIAID Data Ecosystem (nde) graph; this graph then provides the computed differential-expression values (genes, log2 fold changes, adjusted p-values) for the subset of studies it curates.
