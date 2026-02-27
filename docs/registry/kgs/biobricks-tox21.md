---
template: overrides/kg.html
shortname: biobricks-tox21
title: BioBricks Tox21
description: BioBricks Tox21 is an open knowledge graph for Tox21 toxicology screening data.
stats: https://frink.renci.org/kg-stats/biobricks-tox21-kg
homepage: https://github.com/biobricks-ai/biobricks-okg
funding: https://www.nsf.gov/awardsearch/showAward?AWD_ID=2333728
sparql: https://frink.apps.renci.org/biobricks-tox21/sparql
tpf: https://frink.apps.renci.org/ldf/biobricks-tox21
frink-options:
  lakefs-repo: biobricks-tox21-kg
  documentation-path: biobricks-tox21-kg
contact:
  email: tom@insilica.co
  github: "tomlue"
  label: "Tom Luechtefeld"
---
BioBricks Tox21 is an open knowledge graph for Tox21 toxicology screening data.

BioBricks Tox21 is an open knowledge graph that transforms the Tox21 quantitative high-throughput screening (qHTS) 10K library data into structured, machine-readable RDF format. The source dataset contains over 120 million chemical assay data points across 70+ distinct assays for evaluating potential toxicity of approximately 10,000 diverse chemicals. This knowledge graph represents 8,947 chemical entities with ~27,000 triples, primarily using Chemical Information Ontology (CHEMINF) classes to describe compounds. Each chemical is identified using standardized CAS Registry Numbers through identifiers.org URIs and linked to its Tox21 source data. Developed by Insilica LLC as part of the NSF-funded BioBricks-OKG project (Award #2333728), the graph aims to harmonize chemical safety data for researchers, regulatory agencies, and pharmaceutical companies. The dataset is released under CC0-1.0 (Public Domain) license .

```
provenance:
  - derivedFrom:
      label: Tox21 Public Data
      uri: https://tripod.nih.gov/pubdata/
      kind: Database
      license:
        data:
          label: Public Domain
          spdx: CC0-1.0
          uri: https://tox21.gov/overview/operational-model/
```
