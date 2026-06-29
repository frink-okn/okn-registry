---
template: overrides/kg.html
shortname: medical-device-kg
title: Medical Device Knowledge Graph
description: Knowledge graph constructed from FDA MAUDE adverse event reports using standardized FDA product codes.
stats: https://registry.okn.us/kg-stats/medical-device-kg
homepage: https://github.com/Prabhadeus/Proto-OKN
sparql: https://apps.okn.us/medical-device-kg/sparql
tpf: https://apps.okn.us/ldf/medical-device-kg

frink-options:
  lakefs-repo: maude-kg
  documentation-path: maudekg

contacts:
  - email: psingh37@pride.hofstra.edu
    github: Prabhadeus
    label: Prabhjot Singh
---

The MAUDE Knowledge Graph models FDA MAUDE adverse event reports using an ontology-first RDF design. Data is retrieved from the openFDA API using standardized FDA product codes and transformed into RDF/Turtle format. The graph enables structured querying of adverse event data through SPARQL and supports downstream statistical analysis of medical device safety patterns.

Graph statistics:
- Triples: 95,938
- File size: ~5 MB
- Data source: openFDA MAUDE API
