---
template: overrides/kg.html
shortname: climatemodelskg
title: Climate Models KG
description: Climate Models KG is a knowledge graph to support evaluation and development of climate models.
stats: https://registry.okn.us/kg-stats/climate-kg
# homepage: 
funding: https://www.nsf.gov/awardsearch/showAward?AWD_ID=2333789
sparql: https://apps.okn.us/climatemodelskg/sparql
tpf: https://apps.okn.us/ldf/climatemodelskg
frink-options:
  lakefs-repo: climatepub4-kg
  documentation-path: climatepub4-kg
  kgf:
    # rdfs:label here names ontology terms; entity display
    # names are climatepub4:name / :title.
    semantics:
      prefixes:
        climatepub4: "https://climatepub4kg.github.io/ontology#"
        climatepub4-id: "https://climatepub4kg.github.io/id/"
      roles:
        label:
          - "https://climatepub4kg.github.io/ontology#name"
          - "https://climatepub4kg.github.io/ontology#title"
          - "https://climatepub4kg.github.io/ontology#asciiname"
          - "http://www.w3.org/2000/01/rdf-schema#label"
      authoritative_namespaces:
        - climatepub4
        - climatepub4-id
contact:
  email: climatepub4kg@tuprd.onmicrosoft.com
  github: "aayushacharya"
  label: "Aayush Acharya"
---
Climate Models KG is a knowledge graph to support evaluation and development of climate models.

The Climate Models Knowledge Graph integrates structured information about climate models, experiments, and research outputs to support climate science evaluation and development. Built for climate researchers, model developers, and policy analysts, it contains 1.4 million triples describing 55,890 entities across 48 classes. The graph centers on climate model documentation, linking 394 Sources (GCMs, RCMs) to 481 Experiments conducted by 132 Institutes, producing 2,907 climate Variables measured across extensive geographic coverage including 30,062 Cities, 252 Countries, and 3,893 subdivisions. Regional climate models cover approximately 400,000 geographic locations. Entities connect to GeoNames identifiers enabling geospatial integration, while the custom ontology () structures relationships between models, physical schemes, metrics, and results. The knowledge graph supports CMIP6-related research and regional climate modeling studies.

