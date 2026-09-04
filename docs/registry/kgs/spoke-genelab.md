---
template: overrides/kg.html
shortname: spoke-genelab
title: SPOKE GeneLab
description: The spoke-genelab KG complements the spokeokn (SPOKE Open Knowledge
  Network) KG and is designed to integrate omics data from NASA’s Open Science
  Data Repository (OSDR/GeneLab), which hosts results from spaceflight
  experiments.
stats: https://registry.okn.us/kg-stats/spoke-genelab
homepage: https://github.com/BaranziniLab/spoke_genelab
funding: https://www.nsf.gov/awardsearch/showAward?AWD_ID=2333819
sparql: https://apps.okn.us/spoke-genelab/sparql
tpf: https://apps.okn.us/ldf/spoke-genelab
frink-options:
  lakefs-repo: spoke-genelab-kg
  documentation-path: spoke-genelab
  neo4j-conversion-config-path: https://raw.githubusercontent.com/frink-okn/okn-registry/refs/heads/main/docs/registry/neo4j-conf/spoke-genelab.yaml
  kgf:
    semantics:
      prefixes:
        spoke-genelab: "https://purl.org/okn/frink/kg/spoke-genelab/schema/"
        spoke-genelab-node: "https://purl.org/okn/frink/kg/spoke-genelab/node/"
        spoke-genelab-rel: "https://purl.org/okn/frink/kg/spoke-genelab/relationship/"
      roles:
        label:
          - "http://www.w3.org/2000/01/rdf-schema#label"
          - "https://purl.org/okn/frink/kg/spoke-genelab/schema/project_title"
      authoritative_namespaces:
        - spoke-genelab
        - spoke-genelab-node
        - spoke-genelab-rel
contact:
  email: sergio.baranzini@ucsf.edu
  github: "baranzini-lab"
  label: "Sergio Baranzini"
license: "https://creativecommons.org/publicdomain/zero/1.0/"
---
The spoke-genelab KG complements the spoke-okn (SPOKE Open Knowledge Network) KG and is designed to integrate omics data from NASA’s Open Science Data Repository (OSDR/GeneLab), which hosts results from spaceflight experiments. 

The current release includes transcriptional profiling (RNA-Seq, DNA microarray) and epigenomic profiling (DNA methylation) data from model organisms flown in space or maintained as ground controls. Differential expression and methylation signatures are pre-computed to facilitate comparisons between spaceflight and control conditions. Genes from model organisms are systematically mapped to their human orthologs, which allows integration with SPOKE’s rich network of human biology, including pathways, phenotypes, and therapeutic targets. Cell and tissue types are mapped to the Cell (CL) and Uber Anatomy Ontology (UBERON) ontology, respectively.
