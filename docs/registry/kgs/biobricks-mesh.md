---
template: overrides/kg.html
shortname: biobricks-mesh
title: BioBricks MeSH
description: BioBricks MeSH is an open knowledge graph of Medical Subject Headings (MeSH) biomedical vocabulary.
stats: https://frink.renci.org/kg-stats/biobricks-mesh-kg
homepage: https://github.com/biobricks-ai/mesh-kg
funding: https://www.nsf.gov/awardsearch/showAward?AWD_ID=2333728
sparql: https://frink.apps.renci.org/biobricks-mesh/sparql
tpf: https://frink.apps.renci.org/ldf/biobricks-mesh
frink-options:
  lakefs-repo: biobricks-mesh-kg
  documentation-path: biobricks-mesh-kg
contact:
  email: tom@insilica.co
  github: "tomlue"
  label: "Tom Luechtefeld"
---
BioBricks MeSH is an open knowledge graph of Medical Subject Headings (MeSH)
biomedical vocabulary.

BioBricks MeSH is an open knowledge graph providing the complete Medical Subject Headings (MeSH) controlled vocabulary from the U.S. National Library of Medicine in RDF format for biomedical researchers, data scientists, and information professionals. The graph contains over 18.1 million triples representing 2.4 million biomedical entities organized into 862,579 terms, 464,362 concepts, and 249,243 chemical substance records alongside 66,110 organisms, 29,940 topical descriptors, and 6,750 diseases. The hierarchical structure is maintained through 80,096 tree numbers with parent-child relationships and complex concept mappings. Entities are richly labeled with standard rdfs:label properties (achieving 98%+ coverage across major classes) and include temporal metadata with the latest revisions dating to January 2023. Licensed as public domain (CC0-1.0), the dataset is available through a SPARQL endpoint at FRINK, enabling direct federated queries with other biomedical knowledge graphs that reference MeSH identifiers.

```
provenance:
  - derivedFrom:
      label: NLM Medical Subject Headings (MeSH)
      uri: https://www.nlm.nih.gov/mesh/
      kind: RDF
      license:
        data:
          label: Public Domain
          spdx: CC0-1.0
          uri: https://www.nlm.nih.gov/databases/download/terms_and_conditions_mesh.html
```
