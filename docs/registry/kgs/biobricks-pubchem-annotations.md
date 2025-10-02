---
template: overrides/kg.html
shortname: biobricks-pubchem-annotations
title: BioBricks PubChem Annotations
description: >
  BioBricks PubChem Annotations is an open knowledge graph of chemical
  annotations from PubChem.
stats: https://frink.renci.org/kg-stats/biobricks-pubchem-annotations-kg
homepage: https://github.com/biobricks-ai/pubchem-annotations-kg
funding: https://www.nsf.gov/awardsearch/showAward?AWD_ID=2333728
sparql: https://frink.apps.renci.org/biobricks-pubchem-annotations/sparql
tpf: https://frink.apps.renci.org/ldf/biobricks-pubchem-annotations
frink-options:
  lakefs-repo: biobricks-pubchem-annotations-kg
  documentation-path: biobricks-pubchem-annotations-kg
contact:
  email: tom@insilica.co
  github: ""
  label: "Tom Luechtefeld"
---
BioBricks PubChem Annotations is an open knowledge graph of chemical
annotations from PubChem.


```
provenance:
  - derivedFrom:
      label: PubChem Annotations subset
      uri: https://pubchem.ncbi.nlm.nih.gov/source/#type=Annotations
      kind: Database
      license:
        data:
          label: Multiple
          note: >
            Each annotation comes from a different data source with its
            own licensing.
```
