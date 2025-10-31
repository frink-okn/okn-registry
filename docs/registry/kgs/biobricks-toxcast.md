---
template: overrides/kg.html
shortname: biobricks-toxcast
title: BioBricks ToxCast
description: BioBricks ToxCast is an open knowledge graph for EPA ToxCast high-throughput screening data.
stats: https://frink.renci.org/kg-stats/biobricks-toxcast-kg
homepage: https://github.com/biobricks-ai/biobricks-okg
funding: https://www.nsf.gov/awardsearch/showAward?AWD_ID=2333728
sparql: https://frink.apps.renci.org/biobricks-toxcast/sparql
tpf: https://frink.apps.renci.org/ldf/biobricks-toxcast
frink-options:
  lakefs-repo: biobricks-toxcast-kg
  documentation-path: biobricks-toxcast-kg
contact:
  email: tom@insilica.co
  github: ""
  label: "Tom Luechtefeld"
---
BioBricks ToxCast is an open knowledge graph for EPA ToxCast high-throughput
screening data.


```
provenance:
  - derivedFrom:
      label: EPA ToxCast
      uri: https://www.epa.gov/comptox-tools/exploring-toxcast-data
      kind: Database
      license:
        data:
          label: Public Domain
          spdx: CC0-1.0
```
