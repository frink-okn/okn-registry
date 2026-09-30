---
template: overrides/kg.html
shortname: gene-expression-atlas-okn
title: Gene Expression Atlas
description: Query pre-computed differential gene expression (log2 fold changes and adjusted p-values) for genes across diseases, tissues, cell types, developmental stages, and sex, derived from the bulk EMBL-EBI Expression Atlas — 4,668 studies and 14,850 contrasts carrying 8.8 million differential-expression associations across 70 organisms. Use this graph to retrieve computed differential-expression values. It covers essentially all of the bulk Expression Atlas, but it is NOT a cross-repository dataset-discovery index — the Single Cell Expression Atlas is excluded entirely, baseline (non-differential) experiments carry no expression values, and disease annotation is sparse free text. To discover the full set of datasets for a condition (for example when assembling studies for your own pooled or meta-analysis), use a dataset-discovery index such as the NIAID Data Ecosystem (nde) graph.
stats: https://registry.okn.us/kg-stats/gene-expression-atlas-okn
homepage: https://www.ebi.ac.uk/gxa/home
funding: https://www.nsf.gov/awardsearch/showAward?AWD_ID=2535091
sparql: https://apps.okn.us/gene-expression-atlas-okn/sparql
tpf: https://apps.okn.us/ldf/gene-expression-atlas-okn
frink-options:
  lakefs-repo: gene-expression-atlas-okn
  documentation-path: gene-expression-atlas-okn
  kgf:
    semantics:
      prefixes:
        wobd: "http://purl.org/okn/wobd/"
      roles:
        label:
          - "https://w3id.org/biolink/vocab/name"
          - "https://w3id.org/biolink/vocab/symbol"
      authoritative_namespaces:
        - wobd
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

The Gene Expression Atlas Open Knowledge Network (gene-expression-atlas-okn) is a semantic knowledge graph built from the **bulk** EMBL-EBI Expression Atlas, a curated database of gene expression experiments. It integrates **4,668 studies** encompassing **14,850 contrasts (assays)** and **8,828,953 differential-expression associations** over **832,742 genes**, spanning **70 organisms**. The data captures differential gene expression measurements with statistical metrics (log2 fold changes, adjusted p-values) linked to diverse biological contexts including anatomical entities, cell types, diseases, developmental life stages, and biological sex categories.

## Scope

- **Source**: the bulk Expression Atlas only, ingested from `ftp.ebi.ac.uk:/pub/databases/microarray/data/atlas/experiments`. Study coverage is effectively complete — 4,183 of the 4,187 differential experiments currently listed by EBI are present.
- **Not species-limited**: 70 organisms are represented. Human (1,671 studies) and mouse (1,323) lead, but plants and model organisms are fully included — *Arabidopsis* (638), rat (188), *Drosophila* (150), maize, rice, yeast, pig, chicken, *C. elegans*, zebrafish, and others.
- **Single-cell is excluded.** No experiment from the [Single Cell Expression Atlas](https://www.ebi.ac.uk/gxa/sc/home) appears in this graph; the two atlases live in separate FTP trees and only the bulk tree is ingested.
- **Differential only.** All 375 baseline (non-differential) experiments are present as `biolink:Study` metadata nodes but carry **no assays and no expression values** — baseline expression levels (e.g. TPMs) were not ingested.
- **Significance filtering.** Gene-level associations are emitted only where adjusted p-value <= 0.01 **and** |log2 fold change| >= 1.0. Genes measured but not differentially expressed are omitted. Roughly 81% of studies (3,798 / 4,673 in the source build) yield any DE associations at all.
- **Taxon typing is partial.** All 70 organisms appear as `okn-wobd:organism` string literals, but only nine (human, mouse, rat, zebrafish, *Drosophila*, *C. elegans*, *S. cerevisiae*, *Arabidopsis*, *A. nidulans*) receive NCBITaxon URIs via `biolink:in_taxon`. Queries that filter on taxon URIs will silently miss the remaining species.
- **Disease annotation is sparse and unnormalized.** Disease labels come from submitter-supplied SDRF characteristics and are not fully reconciled to MONDO, so a single condition may appear under several free-text spellings and many studies carry no disease annotation.

Built using Biolink Model ontology standards, the knowledge graph connects genes to biological processes, molecular pathways, and protein domains through expression associations (287,615 GO/Reactome/InterPro enrichment associations). Each study includes metadata such as experimental factors, technology platforms, PubMed references, and contrast comparisons between test and reference groups. This structured representation enables systematic exploration of how gene expression varies across tissues, diseases, developmental stages, and experimental conditions, supporting integrative genomics research and the comparison of pre-computed differential-expression results across the atlas.

For **discovering** the landscape of datasets available for a disease across repositories such as NCBI GEO — for example to assemble studies for a new pooled or meta-analysis — use a dataset-discovery index such as the NIAID Data Ecosystem (nde) graph. Although this graph mirrors the bulk Expression Atlas nearly completely, the Expression Atlas is itself a curated analysis resource rather than a census of published expression datasets, and its disease annotation is sparse; a condition with many datasets in GEO may match only a handful of studies here. This graph then provides the computed differential-expression values (genes, log2 fold changes, adjusted p-values) for the studies it does contain.

The graph is produced by the open-source pipeline at [SuLab/OKN-WOBD](https://github.com/SuLab/OKN-WOBD) (`src/okn_wobd/gxa/`).
