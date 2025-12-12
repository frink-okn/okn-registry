---
template: overrides/kg.html
shortname: fiokg
title: SAWGraph FIO KG
description: The FIO (Facilities and Industries Ontology) KG is the part of the SAWGraph project that stores data about facilities from EPA's Facility Registry service (FRS) together with their NAICS industry classification and the spatial location.
# stats: 
homepage: https://sawgraph.github.io/
funding: https://www.nsf.gov/awardsearch/showAward?AWD_ID=2333782
sparql: https://frink.apps.renci.org/fiokg/sparql
tpf: https://frink.apps.renci.org/ldf/fiokg
frink-options:
  lakefs-repo: fio-kg
  documentation-path: fio-kg
contact:
  - email: katrina.schweikert@maine.edu	  
    github: "kschweikert"
    label: "Katrina Schweikert"
  - email: "torsten.hahmann@maine.edu"
    github: "thahmann"
    label: "Torsten Hahmann"
---
The FIO (Facilities and Industries Ontology) KG is a core component of the SAWGraph (Safe Agricultural Products and Water Graph) project, an NSF-funded Proto-OKN initiative to monitor and trace PFAS and other contaminants in the nation's food and water systems. This knowledge graph integrates comprehensive facility (i.e. industrial, federal, and utility facilities) and industry classification data for the coterminous United States (48 states) from EPA's Facility Registry Service (FRS), which provides an integrated source of environmental information about over 826,000 regulated facilities across air, water, and waste programs. The graph currently contains 2.6 million entities and over 10 million triples, structuring data around facilities, environmental records (monitoring, permits, enforcement), and NAICS industry codes. Each facility is spatially indexed to S2 cells (Level 13; from the Spatial KG) and Level 3 administrative regions (county subdivisions; using DataCommons URIs) using KnowWhereGraph’s spatial relations and linked to environmental interest types, compliance systems, and temporal tracking records. The dataset employs standard vocabularies including Dublin Core, PROV-O, GeoSPARQL, and Schema.org. The graph supports SPARQL queries such as for environmental compliance research, contaminant pathway analysis, and facility-industry profiling.

