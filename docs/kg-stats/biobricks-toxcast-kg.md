# biobricks-toxcast





## Schema Diagram

```mermaid
erDiagram
OwlAllDifferent {

}
OwlAllDisjointClasses {

}
OwlAllDisjointProperties {

}
OwlAnnotation {

}
OwlAnnotationProperty {

}
OwlAsymmetricProperty {

}
OwlAxiom {

}
OwlClass {

}
OwlDataRange {
    uri rdfs_seeAlso  
    string rdfs_label  
    string rdfs_comment  
}
OwlDatatypeProperty {

}
OwlDeprecatedClass {

}
OwlDeprecatedProperty {

}
OwlFunctionalProperty {

}
OwlInverseFunctionalProperty {

}
OwlIrreflexiveProperty {

}
OwlNamedIndividual {

}
OwlNegativePropertyAssertion {

}
OwlNothing {

}
OwlObjectProperty {

}
OwlOntology {

}
OwlOntologyProperty {

}
OwlReflexiveProperty {

}
OwlRestriction {

}
OwlSymmetricProperty {

}
OwlThing {

}
OwlTransitiveProperty {

}
RdfAlt {

}
RdfBag {

}
RdfCompoundLiteral {

}
RdfList {
    string rdfs_label  
    string rdfs_comment  
}
RdfProperty {

}
RdfSeq {

}
RdfStatement {

}
RdfsClass {

}
RdfsContainer {

}
RdfsContainerMembershipProperty {

}
RdfsDatatype {
    uri rdfs_seeAlso  
    string rdfs_label  
    string rdfs_comment  
}
RdfsLiteral {

}
RdfsResource {

}
DcamVocabularyEncodingScheme {
    date dct_issued  
    string rdfs_label  
    string rdfs_comment  
    uri rdfs_seeAlso  
}
DcmitypeCollection {

}
DcmitypeDataset {

}
DcmitypeEvent {

}
DcmitypeImage {

}
DcmitypeInteractiveResource {

}
DcmitypeMovingImage {

}
DcmitypePhysicalObject {

}
DcmitypeService {

}
DcmitypeSoftware {

}
DcmitypeSound {

}
DcmitypeStillImage {

}
DcmitypeText {

}
DctAgent {

}
DctAgentClass {
    string rdfs_label  
    string rdfs_comment  
    date dct_issued  
}
DctBibliographicResource {

}
DctFileFormat {

}
DctFrequency {

}
DctJurisdiction {

}
DctLicenseDocument {

}
DctLinguisticSystem {

}
DctLocation {

}
DctLocationPeriodOrJurisdiction {

}
DctMediaType {

}
DctMediaTypeOrExtent {

}
DctMethodOfAccrual {

}
DctMethodOfInstruction {

}
DctPeriodOfTime {

}
DctPhysicalMedium {

}
DctPhysicalResource {

}
DctPolicy {

}
DctProvenanceStatement {

}
DctRightsStatement {

}
DctSizeOrDuration {

}
DctStandard {

}
Bao0000015 {
    string rdfs_label  
    string https___comptox.epa.gov_property_assayID  
}
Bao0000040 {

}
Bao0000179 {
    string rdfs_label  
    string semsci_000300  
}
HttpsW3id.orgBiolinkVocabChemicalEntity {
    string rdfs_label  
}
OboCHEMINF000000 {
    string rdfs_label  
}
OboCHEMINF000446 {
    string rdfs_label  
}
OboCHEMINF000568 {
    string rdfs_label  
}

OwlDataRange ||--|o OwlOntology : "rdfs_isDefinedBy"
OwlDataRange ||--|o RdfsResource : "rdfs_isDefinedBy"
OwlDataRange ||--|o RdfsClass : "rdfs_subClassOf"
OwlDataRange ||--|o RdfsResource : "rdfs_seeAlso"
OwlDataRange ||--|o RdfsLiteral : "rdfs_label"
OwlDataRange ||--|o RdfsLiteral : "rdfs_comment"
RdfList ||--|o RdfsLiteral : "rdfs_label"
RdfList ||--|o RdfsLiteral : "rdfs_comment"
RdfList ||--|o OwlOntology : "rdfs_isDefinedBy"
RdfList ||--|o RdfsResource : "rdfs_isDefinedBy"
RdfsDatatype ||--|o OwlOntology : "rdfs_isDefinedBy"
RdfsDatatype ||--|o RdfsResource : "rdfs_isDefinedBy"
RdfsDatatype ||--|o RdfsClass : "rdfs_subClassOf"
RdfsDatatype ||--|o RdfsResource : "rdfs_seeAlso"
RdfsDatatype ||--|o RdfsLiteral : "rdfs_label"
RdfsDatatype ||--|o RdfsLiteral : "rdfs_comment"
DcamVocabularyEncodingScheme ||--|o RdfsLiteral : "dct_issued"
DcamVocabularyEncodingScheme ||--|o RdfsLiteral : "rdfs_label"
DcamVocabularyEncodingScheme ||--|o RdfsLiteral : "rdfs_comment"
DcamVocabularyEncodingScheme ||--|o RdfsResource : "rdfs_seeAlso"
DcamVocabularyEncodingScheme ||--|o OwlOntology : "rdfs_isDefinedBy"
DcamVocabularyEncodingScheme ||--|o RdfsResource : "rdfs_isDefinedBy"
DctAgentClass ||--|o RdfsLiteral : "rdfs_label"
DctAgentClass ||--|o RdfsLiteral : "rdfs_comment"
DctAgentClass ||--|o RdfsLiteral : "dct_issued"
DctAgentClass ||--|o OwlOntology : "rdfs_isDefinedBy"
DctAgentClass ||--|o RdfsResource : "rdfs_isDefinedBy"
Bao0000015 ||--|o Bao0000040 : "bao_0000209"
Bao0000015 ||--|o RdfsLiteral : "rdfs_label"
Bao0000040 ||--|o Bao0000179 : "obo_OBI_0000299"
Bao0000040 ||--|o HttpsW3id.orgBiolinkVocabChemicalEntity : "obo_RO_0000057"
Bao0000040 ||--|o OboCHEMINF000000 : "obo_RO_0000057"
Bao0000179 ||--|o RdfsLiteral : "rdfs_label"
Bao0000179 ||--|o HttpsW3id.orgBiolinkVocabChemicalEntity : "obo_IAO_0000136"
Bao0000179 ||--|o OboCHEMINF000000 : "obo_IAO_0000136"
HttpsW3id.orgBiolinkVocabChemicalEntity ||--|o OboCHEMINF000568 : "edam_has_identifier"
HttpsW3id.orgBiolinkVocabChemicalEntity ||--|o OboCHEMINF000446 : "edam_has_identifier"
HttpsW3id.orgBiolinkVocabChemicalEntity ||--|o RdfsLiteral : "rdfs_label"
HttpsW3id.orgBiolinkVocabChemicalEntity ||--|o Bao0000040 : "obo_RO_0000056"
OboCHEMINF000000 ||--|o OboCHEMINF000568 : "edam_has_identifier"
OboCHEMINF000000 ||--|o OboCHEMINF000446 : "edam_has_identifier"
OboCHEMINF000000 ||--|o RdfsLiteral : "rdfs_label"
OboCHEMINF000000 ||--|o Bao0000040 : "obo_RO_0000056"
OboCHEMINF000446 ||--|o RdfsLiteral : "rdfs_label"
OboCHEMINF000568 ||--|o RdfsLiteral : "rdfs_label"

```



## Imports


* linkml:types
* okns:extended_types
* okns:dc
* okns:owl-rdf-rdfs



## Classes

| Class | Description | Occurrences |
| --- | --- | --- |
| [Bao0000015](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-toxcast-kg/classes/Bao0000015.md) | None<br/>| 2205 | 
| [Bao0000040](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-toxcast-kg/classes/Bao0000040.md) | None<br/>| 3344010 | 
| [Bao0000179](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-toxcast-kg/classes/Bao0000179.md) | None<br/>| 3344010 | 
| [HttpsW3id.orgBiolinkVocabChemicalEntity](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-toxcast-kg/classes/HttpsW3id.orgBiolinkVocabChemicalEntity.md) | None<br/>| 9542 | 
| [OboCHEMINF000000](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-toxcast-kg/classes/OboCHEMINF000000.md) | None<br/>| 9542 | 
| [OboCHEMINF000446](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-toxcast-kg/classes/OboCHEMINF000446.md) | None<br/>| 9542 | 
| [OboCHEMINF000568](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-toxcast-kg/classes/OboCHEMINF000568.md) | None<br/>| 9542 | 





## Slots

| Slot | Description | Occurrences |
| --- | --- | --- |
| [bao_0000209](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-toxcast-kg/slots/bao_0000209.md) | <br/>| 3344010 |
| [edam_has_identifier](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-toxcast-kg/slots/edam_has_identifier.md) | <br/>| 19084 |
| [https___comptox.epa.gov_property_assayID](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-toxcast-kg/slots/https___comptox.epa.gov_property_assayID.md) | <br/>| 2205 |
| [obo_IAO_0000136](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-toxcast-kg/slots/obo_IAO_0000136.md) | <br/>| 3344010 |
| [obo_OBI_0000299](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-toxcast-kg/slots/obo_OBI_0000299.md) | <br/>| 3344010 |
| [obo_RO_0000056](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-toxcast-kg/slots/obo_RO_0000056.md) | <br/>| 3344010 |
| [obo_RO_0000057](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-toxcast-kg/slots/obo_RO_0000057.md) | <br/>| 3344010 |
| [semsci_000300](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-toxcast-kg/slots/semsci_000300.md) | <br/>| 3380300 |









## IRI prefixes

* bao: http://www.bioassayontology.org/bao#BAO_
* dc: http://purl.org/dc/elements/1.1/
* edam: http://edamontology.org/
* linkml: https://w3id.org/linkml/
* obo: http://purl.obolibrary.org/obo/
* okn: https://purl.org/okn/
* okns: https://purl.org/okn/schema/
* rdfs: http://www.w3.org/2000/01/rdf-schema#
* semsci: http://semanticscience.org/resource/SIO_
