---
template: overrides/kg.html
shortname: maudekg
title: FDA MAUDE Adverse Event Knowledge Graph
description: Knowledge graph constructed from FDA MAUDE adverse event reports using standardized FDA product codes.
stats: https://frink.renci.org/kg-stats/maudekg
homepage: https://github.com/Prabhadeus/Proto-OKN
sparql: https://frink.apps.renci.org/maudekg/sparql
tpf: https://frink.apps.renci.org/ldf/maudekg

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
