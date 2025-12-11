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
