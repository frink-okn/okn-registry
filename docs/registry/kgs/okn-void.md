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
classDiagram
  class Dataset {
    void:triples : xsd:integer
    void:distinctSubjects : xsd:integer
    void:properties : xsd:integer
    void:distinctObjects : xsd:integer
  }

  class DatasetPropertyPartition {
    void:property : IRI
    void:triples : xsd:integer
  }

  class ClassPartition {
    void:class : IRI
    void:entities : xsd:integer
    void:triples : xsd:integer
  }

  class ClassPropertyPartition {
    void:property : IRI
    void:triples : xsd:integer
  }

  class ObjectClassPartition {
    void:class : IRI
    void:triples : xsd:integer
  }

  class UntypedObjectPartition {
    void:triples : xsd:integer
  }

  Dataset "1" --> "0..*" DatasetPropertyPartition : void#58;propertyPartition
  Dataset "1" --> "0..*" ClassPartition : void#58;classPartition
  ClassPartition "1" --> "0..*" ClassPropertyPartition : void#58;propertyPartition
  ClassPropertyPartition "1" --> "0..*" ObjectClassPartition : voidext#58;objectClassPartition
  ClassPropertyPartition "1" --> "0..*" UntypedObjectPartition : voidext#58;objectClassPartition

  note for Dataset "rdf:type void:Dataset"
  note for DatasetPropertyPartition "rdf:type void:Dataset"
  note for ClassPartition "rdf:type void:Dataset"
  note for ClassPropertyPartition "rdf:type void:Dataset"
  note for ObjectClassPartition "rdf:type void:Dataset"
  note for UntypedObjectPartition "rdf:type void:Dataset"
```
