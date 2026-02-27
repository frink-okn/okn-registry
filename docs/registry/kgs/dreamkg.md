---
template: overrides/kg.html
shortname: dreamkg
title: DREAM-KG
description: Develop Dynamic, REsponsive, Adaptive, and Multifaceted Knowledge Graphs to Address Homelessness With Explainable AI
stats: https://frink.renci.org/kg-stats/dream-kg
homepage: https://dreamkg.com/
funding: https://www.nsf.gov/awardsearch/showAward?AWD_ID=2333703
sparql: https://frink.apps.renci.org/dreamkg/sparql
tpf: https://frink.apps.renci.org/ldf/dreamkg
frink-options:
  lakefs-repo: dream-kg
  documentation-path: dream-kg
contact:
  email: yuzhou.chen@temple.edu  
  github: "yuzhouguangc"
  label: "Yuzhou Chen"
---
Dynamic, REsponsive, Adaptive, and Multifaceted Knowledge Graph (DREAM-KG) is an Open Knowledge Network to partially address homelessness with consideration of the social, economic, environmental, and political factors.

DREAM-KG (Dynamic, REsponsive, Adaptive, and Multifaceted Knowledge Graph) is an Open Knowledge Network addressing homelessness for case workers, service providers, law enforcement, nonprofits, and people experiencing homelessness. The graph integrates 87 social service organizations with their locations, contact information, and 87 distinct service offerings, structured using Schema.org vocabulary for interoperability. It contains 32,460 triples across 1,764 entities, primarily modeling service availability (609 opening hours specifications), service categories (157 CategoryCodes), and target audiences (81 audience types). Data is extensively linked to Aunt Bertha's social services directory (1,392 external references) and employs W3C PROV ontology for provenance tracking of all entities through transformation activities. Services are geocoded with latitude/longitude, categorized by populations served (abuse survivors, adults, teens, African American communities).