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
