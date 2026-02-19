---
template: overrides/kg.html
shortname: okn-void
title: OKN VoID graph descriptions
description: Collected VoID (Vocabulary of Interlinked Datasets) metadata for all OKN graphs
homepage: https://frink.renci.org/registry/
funding: https://www.nsf.gov/awardsearch/showAward?AWD_ID=2535091
#sparql: https://frink.apps.renci.org/okn-void/sparql
#tpf: https://frink.apps.renci.org/ldf/okn-void
frink-options:
  lakefs-repo: okn-void
  documentation-path: okn-void
contact:
  email: balhoff@renci.org
  github: "balhoff"
  label: "Jim Balhoff"
---
This is a meta-graph collecting descriptive data for all the graphs that are part of the Proto-OKN. 
Information about the kinds of classes and properties, and the number of triples used for each, 
is stored using the [VoID (Vocabulary of Interlinked Datasets) vocabulary](https://www.w3.org/TR/void/), 
as well as others such as the [VoID Extensions vocabulary](http://ldf.fi/void-ext).

```mermaid
flowchart TD
  D["void:Dataset<br/>(main dataset)"]
  DPP["Dataset Property Partition"]
  CP["Class Partition"]
  CPP["Class Property Partition"]
  OCP_TYPED["Object Class Partition"]
  OCP_UNTYPED["Untyped Object Partition"]

  NOTE_D["rdf:type void:Dataset"]
  NOTE_DPP["rdf:type void:Dataset"]
  NOTE_CP["rdf:type void:Dataset"]
  NOTE_CPP["rdf:type void:Dataset"]
  NOTE_OCP_TYPED["rdf:type void:Dataset"]
  NOTE_OCP_UNTYPED["rdf:type void:Dataset"]

  D -->|"void:triples<br/>void:distinctSubjects<br/>void:properties<br/>void:distinctObjects"| D
  D -->|"void:propertyPartition"| DPP
  D -->|"void:classPartition"| CP
  D -.-> NOTE_D

  DPP -->|"void:property"| P1["Property IRI"]
  DPP -->|"void:triples"| N1["xsd:integer"]
  DPP -.-> NOTE_DPP

  CP -->|"void:class"| C1["Class IRI"]
  CP -->|"void:entities"| N2["xsd:integer"]
  CP -->|"void:triples"| N3["xsd:integer"]
  CP -->|"void:propertyPartition"| CPP
  CP -.-> NOTE_CP

  CPP -->|"void:property"| P2["Property IRI"]
  CPP -->|"void:triples"| N4["xsd:integer"]
  CPP -->|"voidext:objectClassPartition"| OCP_TYPED
  CPP -->|"voidext:objectClassPartition"| OCP_UNTYPED
  CPP -.-> NOTE_CPP

  OCP_TYPED -->|"void:class"| C2["Target Class IRI"]
  OCP_TYPED -->|"void:triples"| N5["xsd:integer"]
  OCP_TYPED -.-> NOTE_OCP_TYPED

  OCP_UNTYPED -->|"void:triples"| N6["xsd:integer"]
  OCP_UNTYPED -.-> NOTE_OCP_UNTYPED

  classDef core fill:#eef,stroke:#447,stroke-width:1px;
  class D,DPP,CP,CPP,OCP_TYPED,OCP_UNTYPED core;
```
