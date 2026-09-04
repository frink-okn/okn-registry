---
template: overrides/kg.html
shortname: evoweb
title: EvoWeb
description: EvoWeb - An Open Knowledge Graph of Co-evolving Genes (NIAID)
stats: https://registry.okn.us/kg-stats/evoweb
homepage: https://data.niaid.nih.gov/
funding: https://www.nsf.gov/awardsearch/showAward?AWD_ID=2333810
frink-options:
  lakefs-repo: evoweb
  documentation-path: evoweb
  kgf:
    semantics:
      prefixes:
        evoweb: "https://purl.org/okn/frink/kg/evoweb/schema/"
      roles:
        label:
          - "http://www.w3.org/2000/01/rdf-schema#label"
      authoritative_namespaces:
        - evoweb
contacts:
- email: Erik.Wright@bcm.edu
  github: "WrightLabScience"
  label: "Erik Wright"
sparql: https://apps.okn.us/evoweb/sparql
tpf: https://apps.okn.us/ldf/evoweb
---
EvoWeb is a weighted network of protein-protein functional relations, reconstructed from prior knowledge available from genomic sequences, allowing users to find hypothetical proteins involved in protein complexes or separate steps of a biochemical pathway, as well as 12 signals of coevolution to quantify the degree of shared evolution between genes.

This project is a continuation of work done in the EvoWeaver project (https://www.nature.com/articles/s41467-025-59175-6) going beyond individual protein pairs.
