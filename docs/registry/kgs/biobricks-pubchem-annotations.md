---
template: overrides/kg.html
shortname: biobricks-pubchem-annotations
title: BioBricks PubChem Annotations
description: BioBricks PubChem Annotations is an open knowledge graph of chemical annotations from PubChem.
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
  github: "tomlue"
  label: "Tom Luechtefeld"
---
BioBricks PubChem Annotations is an open knowledge graph of chemical
annotations from PubChem.

BioBricks PubChem Annotations is an open knowledge graph providing structured access to chemical annotations originally sourced from PubChem's Annotations subset, targeting researchers in cheminformatics, toxicology, and environmental health. The graph contains over 10.7 million annotations (87.4 million triples total) describing chemical compounds through text-based annotations including regulatory data, physical properties, biological activities, and hazard information. Each annotation follows the W3C Web Annotation Data Model, linking PubChem compound identifiers to textual annotation bodies covering topics from state-level contaminant limits to chemical synthesis methods. The knowledge graph interoperates with the broader PubChem RDF ecosystem through shared compound URIs in the namespace. Annotations derive from multiple heterogeneous sources with varying licenses, documented in PubChem's source metadata.

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
