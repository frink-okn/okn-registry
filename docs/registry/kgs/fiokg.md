---
template: overrides/kg.html
shortname: fiokg
title: SAWGraph FRS KG
description: The FRS (Facility Registry Service) KG is the part of the SAWGraph project that stores data about facilities from EPA's Facility Registry service (FRS) together with their NAICS industry classification and the spatial location.
stats: https://registry.okn.us/kg-stats/fio-kg
homepage: https://sawgraph.github.io/
funding: https://www.nsf.gov/awardsearch/showAward?AWD_ID=2333782
sparql: https://apps.okn.us/fiokg/sparql
tpf: https://apps.okn.us/ldf/fiokg
frink-options:
  lakefs-repo: fio-kg
  documentation-path: fio-kg
  kgf:
    semantics:
      prefixes:
        schema: "http://schema.org/"
        fio: "http://w3id.org/fio/v1/fio#"
        fio-epa: "http://w3id.org/fio/v1/epa-frs#"
        fio-naics: "http://w3id.org/fio/v1/naics#"
        fio-epa-data: "http://w3id.org/fio/v1/epa-frs-data#"
        protonsys: "http://proton.semanticweb.org/protonsys#"
        datacommons: "https://datacommons.org/browser/"
      roles:
        label:
          - "http://www.w3.org/2000/01/rdf-schema#label"
          - "http://purl.org/dc/terms/title"
      authoritative_namespaces:
        - fio
        - fio-epa
        - fio-naics
        - fio-epa-data
contacts:
  - email: katrina.schweikert@maine.edu
    github: "kschweikert"
    label: "Katrina Schweikert"
  - email: "torsten.hahmann@maine.edu"
    github: "thahmann"
    label: "Torsten Hahmann"
---
The FRS KG is a core component of the SAWGraph (Safe Agricultural Products and Water Graph) project, an NSF-funded Proto-OKN initiative to monitor and trace PFAS and other contaminants in the nation's food and water systems. This knowledge graph integrates comprehensive facility (i.e. industrial, federal, and utility facilities) and industry classification data for the coterminous United States (48 states) from EPA's Facility Registry Service (FRS), which provides an integrated source of environmental information about over 826,000 regulated facilities across air, water, and waste programs. The graph is built on top of the Facilities and Industries Ontology (FIO) that offers hierarchically structured NAICS industries and generalized links to facilities. The FRS KG currently contains 2.6 million entities and over 10 million triples, structuring data around facilities, environmental records (monitoring, permits, enforcement), and NAICS industry codes. Each facility is spatially indexed to S2 cells (Level 13; from the Spatial KG) and Level 3 administrative regions (county subdivisions; using DataCommons URIs) using KnowWhereGraph’s spatial relations and linked to environmental interest types, compliance systems, and temporal tracking records. The dataset employs standard vocabularies including Dublin Core, PROV-O, GeoSPARQL, and Schema.org. The graph supports SPARQL queries such as for environmental compliance research, contaminant pathway analysis, and facility-industry profiling.

