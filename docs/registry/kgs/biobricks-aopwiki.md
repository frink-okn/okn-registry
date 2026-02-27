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
  github: "tomlue"
  label: "Tom Luechtefeld"
---
BioBricks AOP-Wiki is an open knowledge graph for Adverse Outcome Pathways from
the AOP-Wiki.

The BioBricks AOP-Wiki knowledge graph serves toxicologists, regulatory scientists, and environmental health researchers by providing structured representations of Adverse Outcome Pathways (AOPs) that link molecular initiating events to adverse health outcomes. This knowledge graph contains 493 AOPs, 1,469 key events, and 2,060 key event relationships, totaling 184,303 triples that capture the mechanistic understanding of chemical toxicity pathways. The dataset integrates chemical entities (including CHEMINF molecular descriptors), biological processes (GO terms), and organism/organ/cell-type contexts, with extensive cross-references to ChEBI, ChEMBL, PubChem, KEGG, and Wikidata through 13,692 exact matches and additional identifier mappings. Licensed under CC-BY-SA-1.0 with regular updates (last modified November 2024), the graph is derived from the collaborative AOP-Wiki project and is accessible via a SPARQL endpoint through FRINK, enabling federated queries for chemical hazard assessment and predictive toxicology applications.


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
