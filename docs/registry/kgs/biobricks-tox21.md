---
template: overrides/kg.html
shortname: biobricks-tox21
title: BioBricks Tox21
description: >
  BioBricks Tox21 is an open knowledge graph for Tox21 toxicology screening
  data.
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
  github: ""
  label: "Tom Luechtefeld"
---
BioBricks Tox21 is an open knowledge graph for Tox21 toxicology screening data.


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
