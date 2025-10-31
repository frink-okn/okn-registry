---
template: overrides/kg.html
shortname: biobricks-aopwiki
title: BioBricks AOP-Wiki
description: BioBricks AOP-Wiki is an open knowledge graph for Adverse Outcome Pathways from the AOP-Wiki.
stats: https://frink.renci.org/kg-stats/biobricks-aopwiki-kg
homepage: https://github.com/biobricks-ai/aopwikirdf-kg
funding: https://www.nsf.gov/awardsearch/showAward?AWD_ID=2333728
sparql: https://frink.apps.renci.org/biobricks-aopwiki/sparql
tpf: https://frink.apps.renci.org/ldf/biobricks-aopwiki
frink-options:
  lakefs-repo: biobricks-aopwiki-kg
  documentation-path: biobricks-aopwiki-kg
contact:
  email: tom@insilica.co
  github: ""
  label: "Tom Luechtefeld"
---
BioBricks AOP-Wiki is an open knowledge graph for Adverse Outcome Pathways from
the AOP-Wiki.


```
provenance:
  - derivedFrom:
      label: AOPWikiRDF
      uri: https://github.com/marvinm2/AOPWikiRDF
      kind: RDF
      license:
        software:
          label: MIT License
          spdx: MIT
          uri: https://github.com/marvinm2/AOPWikiRDF/blob/master/LICENSE
      derivedFrom:
        label: AOPWiki
        kind: XML
        uri: https://aopwiki.org/
        license:
          data:
            label: Creative Commons Attribution Share Alike
            spdx: CC-BY-SA-1.0
            uri: https://aopwiki.org/handbooks/5#content-licensing-40
```
