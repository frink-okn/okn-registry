---
template: overrides/kg.html
shortname: monarch
title: Monarch Knowledge Graph
description: The Monarch Knowledge Graph comprises the combined knowledge of 33 biomedical resources and biomedical ontologies.
homepage: https://monarchinitiative.org/kg/about
funding: https://monarchinitiative.org/about/funding
frink-options:
  lakefs-repo: monarch
  documentation-path: monarch
  kgf:
    semantics:
      roles:
        label:
          - "http://www.w3.org/2000/01/rdf-schema#label"

contacts:
  - email: "kevin@tislab.org"
    github: kevinschaper
    label: "Kevin Schaper"
  - email: "ptgolden@email.unc.edu"
    github: ptgolden
    label: "Patrick Golden"
---
The Monarch Knowledge Graph (KG) comprises the combined knowledge of 33 biomedical resources and biomedical ontologies, and is updated with the latest data from each source once a month. The components of the Monarch KG and the associations between them are represented as nodes, edges, and labels. A data source ingest imports data from resources such as the external Panther Database or Monarch’s disease annotations to Human Phenotype Ontology terms (HPOA) and transforms them into the Monarch KG schema. Ontologies are integrated into a ‘semantic layer,’ a Biolink-conformant representation of the Phenomics Integrated Ontology (PHENIO), which serves as a hierarchical schema and classification system for the integrated data.
