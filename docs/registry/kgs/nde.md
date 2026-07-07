---
template: overrides/kg.html
shortname: nde
title: NIAID Data Ecosystem KG
description: The nde (NIAID Data Ecosystem) knowledge graph is a dataset-discovery index for finding biomedical research datasets — including gene-expression / transcriptomics data (RNA-seq, microarray, single-cell / single-nucleus), other -omics, clinical, epidemiological, imaging, and flow-cytometry data — searchable by disease or condition, organism, and source repository. It mirrors dataset metadata from NCBI GEO, ArrayExpress, and 70+ repositories; coverage is deepest for infectious and immune-mediated disease (its NIAID mission) but, because it indexes general-purpose repositories such as GEO, it also covers datasets for many non-infectious diseases and conditions (e.g. cancer, diabetes, kidney disease). Use it to find and triage candidate datasets for a specific disease — for example when assembling studies for a pooled or meta-analysis of differential gene expression. It stores dataset-level metadata and links to the primary repository; it does NOT store per-sample data or computed differential-expression values (log2 fold changes / p-values).
stats: https://registry.okn.us/kg-stats/nde
homepage: https://data.niaid.nih.gov/
funding: https://www.nsf.gov/awardsearch/showAward?AWD_ID=2535091
sparql: https://apps.okn.us/nde/sparql
tpf: https://apps.okn.us/ldf/nde
frink-options:
  lakefs-repo: nde
  documentation-path: nde
keywords:
- dataset discovery
- find datasets
- gene expression
- transcriptomics
- RNA-seq
- single-cell
- microarray
- GEO
- ArrayExpress
- meta-analysis
- omics
- disease datasets
example_queries:
- What datasets are available to study gene expression in diabetic nephropathy?
- Find human RNA-seq datasets for a given kidney disease.
- Which GEO datasets exist for a specific disease, and in which species?
- List transcriptomics datasets I could pool for a differential-expression meta-analysis of a condition.
contacts:
- email: asu@scripps.edu
  github: "andrewsu"
  label: "Andrew Su"
- email: plwhetzel@gmail.com
  github: "twhetzel"
  label: "Trish Whetzel"
---

The nde (NIAID Data Ecosystem) knowledge graph is a **dataset-discovery index**: use it to find and triage biomedical research datasets — including **gene-expression / transcriptomics** studies (RNA-seq, microarray, single-cell and single-nucleus), other **-omics**, clinical, epidemiological, pathogen–host interaction, flow-cytometry, and imaging data — as candidates for downstream reanalysis such as a **pooled or meta-analysis of differential gene expression**. Datasets are searchable by **disease or condition** (`healthCondition`), **organism** (`species`), **source repository** (`includedInDataCatalog`), infectious agent, authors, funding, and publications. The graph aggregates metadata mirrored from **NCBI GEO, ArrayExpress, and over 70 repositories**; while its coverage is deepest for **infectious and immune-mediated disease** (its NIAID mission), it indexes general-purpose repositories, so it also contains many datasets for **non-infectious diseases and conditions** (for example cancer, diabetes, and kidney disease). Note that nde holds **dataset-level metadata and links to the primary repository only** — it does not store per-sample records or computed expression values, so specific per-group sample counts must be retrieved from the source repository.

The NIAID Data Ecosystem (NDE) Knowledge Graph provides structured metadata for biomedical research resources, with deep coverage of infectious and immune-mediated disease (IID). Developed by the National Institute of Allergy and Infectious Diseases in collaboration with Scripps Research, this knowledge graph powers the NIAID Data Ecosystem Discovery Portal (https://data.niaid.nih.gov), which aggregates millions of datasets from over 70 sources including NIAID-funded repositories, globally-relevant IID repositories, and general-purpose archives such as NCBI GEO.

The knowledge graph organizes metadata using Schema.org vocabulary, enabling unified search across diverse biomedical data types including -omics data (gene expression, transcriptomics, and other high-throughput assays), clinical studies, epidemiological data, pathogen-host interactions, flow cytometry, and imaging datasets. It connects datasets to their authors, funding sources, research projects, publications, and key disease and pathogen terms, facilitating discovery of resources related to COVID-19, HIV, malaria, tuberculosis, and — through its mirrored general repositories — many other diseases and conditions. By harmonizing heterogeneous metadata formats and providing both user-friendly search interfaces and programmatic API access, the NDE knowledge graph accelerates biomedical research and maximizes the impact of publicly-funded scientific data.
