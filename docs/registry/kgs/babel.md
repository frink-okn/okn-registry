---
template: overrides/kg.html
shortname: babel
title: Babel KG
description: Babel creates cliques of equivalent identifiers across many biomedical vocabularies
homepage: https://github.com/NCATSTranslator/Babel
#sparql: https://apps.okn.us/babel/sparql
#tpf: https://apps.okn.us/ldf/babel
frink-options:
  lakefs-repo: babel
  documentation-path: babel
contact:
  email: balhoff@renci.org
  github: "balhoff"
  label: "Jim Balhoff"
license: "https://creativecommons.org/licenses/by/4.0/"
---
The [Biomedical Data Translator](https://ncats.nih.gov/translator) integrates
data across many data sources. One source of difficulty is that different data
sources use different vocabularies. One source may represent water as
[MESH:D014867](https://meshb.nlm.nih.gov/record/ui?ui=D014867), while another
may use the identifier [DRUGBANK:DB09145](https://go.drugbank.com/drugs/DB09145). When integrating, we
need to recognize that both of these identifiers are identifying the same
concept.

Babel integrates the specific naming systems used in the Translator, creating
equivalent sets across multiple semantic types following the conventions
established by the [Biolink Model](https://github.com/biolink/biolink-model).

This graph is an RDF rendering of Data Translators Babel dataset.
```
