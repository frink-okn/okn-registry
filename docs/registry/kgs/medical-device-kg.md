---
template: overrides/kg.html
shortname: medical-device-kg
title: Medical Device Knowledge Graph
description: A unified medical-device knowledge graph integrating regulatory, clinical, research, safety, and other relevant data from multiple sources.
stats: https://registry.okn.us/kg-stats/medical-device-kg
homepage: https://github.com/Prabhadeus/Proto-OKN
sparql: https://apps.okn.us/medical-device-kg/sparql
tpf: https://apps.okn.us/ldf/medical-device-kg
frink-options:
  lakefs-repo: medical-device-kg
  documentation-path: medical-device-kg
contacts:
  - email: mbukhari1@pride.hofstra.edu
    label: Mustafa Bukhari
  - email: Marco.Romanelli@hofstra.edu
    label: "Dr. Marco Romanelli"
  - email: RocheRey.C.DeGuzman@hofstra.edu
    label: "Dr. Roche C. de Guzman"
  - email: psingh37@pride.hofstra.edu
    github: Prabhadeus
    label: Prabhjot Singh
---
The Medical Device Knowledge Graph integrates medical-device data from multiple regulatory, clinical, research, and safety sources using a unified ontology-first RDF design. Source records are standardized and transformed into RDF/Turtle so related devices, manufacturers, regulatory submissions, studies, outcomes, recalls, and adverse events can be connected and queried through SPARQL. The graph supports cross-dataset analysis, medical-device safety research, risk modeling, and the continued integration of additional data sources.
