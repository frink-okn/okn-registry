---
template: overrides/kg.html
shortname: ruralkg
title: Rural Resilience KG
description: Rural Resilience KG is a cross-domain knowledge graph to integrate health and justice for rural resilience.
stats: https://frink.renci.org/kg-stats/rural-kg
#homepage: 
funding: https://www.nsf.gov/awardsearch/showAward?AWD_ID=2333836
sparql: https://frink.apps.renci.org/ruralkg/sparql
tpf: https://frink.apps.renci.org/ldf/ruralkg
frink-options:
  lakefs-repo: rural-kg
  documentation-path: rural-kg
contact:
  email: jiaqi.gong@ua.edu
  github: "SAIL-UA"
  label: "Jiaqi Gong"
---
Rural Resilience KG is a cross-domain knowledge graph to integrate health and justice for rural resilience.

The Rural Resilience Knowledge Graph (RuralKG) is a cross-domain semantic resource designed for researchers, policymakers, and public health professionals studying health disparities and justice outcomes in rural America. It integrates substance abuse data from the National Survey on Drug Use and Health (NSDUH), criminal justice incidents from the National Incident-Based Reporting System (NIBRS), mental health treatment provider locations, and geospatial administrative boundaries spanning 56 states/territories, 3,253 counties, and 31,120 cities. Each county is linked to USDA Rural-Urban Continuum Codes (RUCC) to facilitate rural-urban comparative analyses. The graph contains 815,852 triples describing 67,191 entities across 16 classes, with rich connections between treatment providers (9,037) and 176 mental health services. RuralKG uses a native ontology (sail.ua.edu/ruralkg) and provides standard SPARQL access for federated querying, supporting interdisciplinary research on rural health equity, substance abuse patterns, and justice system interactions.

