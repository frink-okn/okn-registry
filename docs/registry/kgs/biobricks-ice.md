---
template: overrides/kg.html
shortname: biobricks-ice
title: BioBricks ICE
description: BioBricks ICE (Integrated Chemical Environment) is an open knowledge graph for cheminformatics and chemical safety data from EPA's CompTox database.
stats: https://frink.renci.org/kg-stats/biobricks-ice-kg
homepage: https://github.com/biobricks-ai/biobricks-okg
funding: https://www.nsf.gov/awardsearch/showAward?AWD_ID=2333728
sparql: https://frink.apps.renci.org/biobricks-ice/sparql
tpf: https://frink.apps.renci.org/ldf/biobricks-ice
frink-options:
  lakefs-repo: biobricks-ice-kg
  documentation-path: biobricks-ice-kg
contact:
  email: tom@insilica.co
  github: "tomlue"
  label: "Tom Luechtefeld"
---
BioBricks ICE (Integrated Chemical Environment) is an open knowledge graph for
cheminformatics and chemical safety data from EPA's CompTox database.

BioBricks ICE (Integrated Chemical Environment) is an open knowledge graph that serves toxicologists, computational chemists, and environmental health researchers by integrating chemical safety and bioassay data from the EPA's NICEATM ICE database. The graph contains 27.4 million triples describing 206,543 chemical entities linked to over 3 million bioassay measurements across 2,063 standardized assays. Core entities include chemical substances (identified via EPA DSSTox IDs), bioassays (BAO ontology), assay measurements, and mechanistic targets with gene and UMLS identifiers. The graph employs established vocabularies including the BioAssay Ontology (BAO), Chemical Information Ontology (CHEMINF), Semanticscience Integrated Ontology (SIO), and Relation Ontology (RO). External linkages to EPA CompTox Dashboard, NCBI Gene, and UMLS enable cross-database queries. Licensed as public domain (CC0-1.0), the graph supports federation with other toxicology and biomedical knowledge graphs.


```
provenance:
  - derivedFrom:
      label: NICEATM ICE
      uri: https://ice.ntp.niehs.nih.gov/
      kind: Database
      license:
        data:
          label: Public Domain
          spdx: CC0-1.0
          uri: https://ice.ntp.niehs.nih.gov/DATASETDESCRIPTION
          note: >
            All data in ICE are publicly available with no restrictions on use.
```
