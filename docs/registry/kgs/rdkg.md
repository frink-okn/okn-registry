---
template: overrides/kg.html
shortname: rdkg
title: Rare Disease Knowledge Graph
description: RDKG is an open knowledge graph for rare diseases that integrates standardized disease identifiers and cross-references to support discovery and evidence synthesis.
#homepage: https:// 
frink-options:
  lakefs-repo: rdkg
  documentation-path: rdkg
contacts:
  - email: jinlian.wang@uth.tmc.edu
    github: wnagjl99
    label: Jinlian Wang
---

Rare Disease Knowledge Graph (RDKG) is an open knowledge graph that harmonizes rare disease entities and their cross-references to major biomedical terminologies. It is designed to support rare disease knowledge discovery, entity linking across sources, and downstream analytics for evidence synthesis.

provenance:
  - derivedFrom:
      label: MONDO Disease Ontology
      uri: https://mondo.monarchinitiative.org/
      kind: Ontology

  - derivedFrom:
      label: Orphanet / ORDO
      uri: https://www.orpha.net/
      kind: Database/Ontology

  - derivedFrom:
      label: OMIM Phenotypic Series (OMIMPS)
      uri: https://omim.org/
      kind: Database

  - derivedFrom:
      label: UMLS
      uri: https://www.nlm.nih.gov/research/umls/
      kind: Terminology

