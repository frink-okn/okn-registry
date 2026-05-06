---
template: overrides/kg.html
shortname: pankgraph
title: PanKgraph
description: PanKgraph — PanKbase Knowledge Graph (NIDDK)
stats: https://frink.renci.org/kg-stats/pankbase-kg
homepage: https://pankbase.org/
funding: https://www.nsf.gov/awardsearch/showAward?AWD_ID=2333810
frink-options:
  lakefs-repo: pankbase-kg
  documentation-path: pankbase-kg
  neo4j-conversion-config-path: https://raw.githubusercontent.com/frink-okn/okn-registry/refs/heads/main/docs/registry/neo4j-conf/pankgraph.yaml
contacts:
- email: drjieliu@umich.edu
  github: "jieliu6"
  label: "Jie Liu"
sparql: https://apps.okn.us/pankgraph/sparql
tpf: https://apps.okn.us/ldf/pankgraph
---
PanKgraph is a state-of-the-art Knowledge Graph developed for the study of the human pancreas. By leveraging large language models (LLMs) and diverse data types, PanKgraph enables users to uncover biological connections and insights into diabetes pathogenesis. Previously disjointed entities such as genes, single nucleotide polymorphisms (SNPs), and pancreatic expression quantitative trait loci (eQTLs) can now be explored and connected in innovative ways.

PanKbase is a comprehensive, centralized resource for the study of the human pancreas and diabetes. The PanKbase collective aims to integrate diverse type 1 diabetes (T1D) datasets with expert-curated knowledge in a centralized, open-source data hub. Since users will ultimately be able to contribute their own data, this will be a repository for reproducible, collaborative research within the pancreas and T1D realms.

PanKbase is an actively evolving resource that plans to offer integrated and computation-ready multi-omic data including genomics, epigenomics, transcriptomics, metabolomics, and proteomics, as well as other data types such as imaging and physiological data. Datasets are currently sourced from key external programs, from which human donor-derived pancreatic data and metadata are aggregated, harmonized, and disseminated.
