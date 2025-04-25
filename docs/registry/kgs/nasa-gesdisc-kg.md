---
template: overrides/kg.html
shortname: nasa-gesdisc-kg
title: NASA-GESDISC-KG
description: The NASA Knowledge Graph Dataset is an expansive graph-based dataset designed to integrate and interconnect information about satellite datasets, scientific publications, instruments, platforms, projects, data centers, and science keywords. This knowledge graph is particularly focused on datasets managed by NASA's Distributed Active Archive Centers (DAACs), which are NASA's data repositories responsible for archiving and distributing scientific data. In addition to NASA DAACs, the graph includes datasets from 184 data providers worldwide, including various government agencies and academic institutions.
stats: https://frink.renci.org/kg-stats/nasa-gesdisc-kg
homepage: https://disc.gsfc.nasa.gov
funding:
sparql: https://frink.apps.renci.org/nasa-gesdisc-kg/sparql
tpf: https://frink.apps.renci.org/ldf/nasa-gesdisc-kg
frink-options:
  lakefs-repo: nasa-gesdisc
  documentation-path: nasa-gesdisc
  rdf-conversion-config-path: https://github.com/frink-okn/neo4j-json-to-ttl/blob/main/conf/nasa.yaml
contact:
  email: lisa@renci.org  
  github: ""
  label: "Lisa Stillwell"
---
The primary goal of the NASA Knowledge Graph is to bridge scientific publications with the datasets they reference, facilitating deeper insights and research opportunities within NASA's scientific and data ecosystem. By organizing these interconnections within a graph structure, this dataset enables advanced analyses, such as discovering influential datasets, understanding research trends, and exploring scientific collaborations. 
