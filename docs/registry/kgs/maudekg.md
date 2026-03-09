---
template: overrides/kg.html
shortname: maudekg
title: FDA MAUDE Adverse Event Knowledge Graph
description: Knowledge graph constructed from FDA MAUDE adverse event reports using standardized FDA product codes.
homepage: https://github.com/Prabhadeus/Proto-OKN
contacts:
  - email: prabh120220@gmail.com
    label: Prabhjot Singh
    github: Prabhadeus
---

The MAUDE Knowledge Graph models FDA MAUDE adverse event reports using an ontology-first RDF design. Data is retrieved from the openFDA API via standardized FDA product codes and serialized into RDF/Turtle format for SPARQL querying and downstream statistical analysis.

Graph statistics:
- Triples: 95,938
- File size: ~4.9 MB
- Data source: openFDA MAUDE API
