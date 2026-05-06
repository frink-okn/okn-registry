---
template: overrides/kg.html
shortname: digcfdekg
title: CFDE REVEAL Knowledge Graph
description: The CFDE REVEAL Knowledge Graph is a statistically inferred genomic evidence graph to integrate and disseminate knowledge within the Common Fund Data Ecosystem (CFDE).
stats: https://frink.renci.org/kg-stats/digcfdekg
homepage: https://cfdeknowledge.org/
funding: https://www.nsf.gov/awardsearch/showAward?AWD_ID=2535091
frink-options:
  lakefs-repo: digcfdekg
  documentation-path: digcfdekg
contacts:
  - email: flannick@broadinstitute.org
    github: "flannick"
    label: "Jason Flannick"
  - email: burtt@broadinstitute.org
    github: ""
    label: "Noël Burtt"
---
The CFDE REVEAL Knowledge Graph is a statistically inferred genomic evidence graph to integrate and disseminate knowledge within the Common Fund Data Ecosystem (CFDE).

The CFDE REVEAL Knowledge Graph connects biological processes and genes to human disease endpoints using the Common Fund Data Ecosystem (CFDE), a collection of high-profile data generation programs funded by the NIH Common Fund. CFDE datasets are represented as gene sets that are then linked to human traits by applying two Bayesian methods: PIGEAN (Priors Inferred from GEne ANnotations) to identify probabilistic relationships between these gene sets and human traits (~7,000) by jointly inferring which genes (~20,000) are trait-relevant and which gene sets predict trait-relevance; and EAGGL (Enrichment Analysis, Gene Grouping, and LLMs) to learn latent factors (~4,000) that model disease mechanisms. The base knowledge graph includes edges between genes and phenotypes, genes and disease mechanisms, and disease mechanisms and phenotypes, each annotated with a probability of association.
