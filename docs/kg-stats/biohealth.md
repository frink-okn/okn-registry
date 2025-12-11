# biohealth





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
HttpsW3id.orgBiolinkVocabEntity {
    string https___w3id.org_biolink_vocab_category  
    uri https___w3id.org_biolink_vocab_category  
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
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_METHOD_OF"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_COEXISTS_WITH"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_STIMULATES"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_LOCATION_OF(SPEC)"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_MEASURES"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_PRODUCES"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_LOCATION_OF"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___w3id.org_biolink_vocab_preventative_for_condition"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_CAUSES"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_PART_OF"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_DISRUPTS"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_PRECEDES"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___w3id.org_biolink_vocab_location_of"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_COMPLICATES"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_PREVENTS"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_USES"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_PROCESS_OF"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_PROCESS_OF"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___w3id.org_biolink_vocab_interacts_with"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___w3id.org_biolink_vocab_increases_amount_or_activity_of"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_ADMINISTERED_TO"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_CONVERTS_TO"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_same_as"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___w3id.org_biolink_vocab_associated_with"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_ASSOCIATED_WITH"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_lower_than"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___w3id.org_biolink_vocab_treats"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_AFFECTS"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_MEASUREMENT_OF"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_higher_than"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_USES"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_COMPLICATES"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_PRODUCES"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_OCCURS_IN"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_MEASURES"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_PREDISPOSES"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___w3id.org_biolink_vocab_part_of"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_DIAGNOSES"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_higher_than"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___w3id.org_biolink_vocab_subclass_of"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___w3id.org_biolink_vocab_causes"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_CONVERTS_TO"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_OCCURS_IN"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_lower_than"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_MEASUREMENT_OF"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___w3id.org_biolink_vocab_precedes"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___w3id.org_biolink_vocab_manifestation_of"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_INHIBITS"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_AUGMENTS"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___w3id.org_biolink_vocab_diagnoses"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_STIMULATES"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___w3id.org_biolink_vocab_coexists_with"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_TREATS"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_same_as"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___w3id.org_biolink_vocab_decreases_amount_or_activity_of"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_ADMINISTERED_TO"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_ISA"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_METHOD_OF"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___w3id.org_biolink_vocab_disrupts"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___w3id.org_biolink_vocab_predisposes_to_condition"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_MANIFESTATION_OF"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___w3id.org_biolink_vocab_affects"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_compared_with"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_INTERACTS_WITH"
HttpsW3id.orgBiolinkVocabEntity ||--|o RdfsLiteral : "rdfs_label"

```



## Imports


* okns:dc
* linkml:types
* okns:extended_types
* okns:owl-rdf-rdfs



## Classes

| Class | Description | Occurrences |
| --- | --- | --- |
| [HttpsW3id.orgBiolinkVocabEntity](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/classes/HttpsW3id.orgBiolinkVocabEntity.md) | None<br/>| 250976 | 





## Slots

| Slot | Description | Occurrences |
| --- | --- | --- |
| [https___biohealthkg.proto_okn.net_kg_schema_ADMINISTERED_TO](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_ADMINISTERED_TO.md) | <br/>| 234354 |
| [https___biohealthkg.proto_okn.net_kg_schema_compared_with](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_compared_with.md) | <br/>| 370807 |
| [https___biohealthkg.proto_okn.net_kg_schema_COMPLICATES](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_COMPLICATES.md) | <br/>| 53189 |
| [https___biohealthkg.proto_okn.net_kg_schema_CONVERTS_TO](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_CONVERTS_TO.md) | <br/>| 39403 |
| [https___biohealthkg.proto_okn.net_kg_schema_higher_than](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_higher_than.md) | <br/>| 99934 |
| [https___biohealthkg.proto_okn.net_kg_schema_LOCATION_OF(SPEC)](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_LOCATION_OF(SPEC).md) | <br/>| 2 |
| [https___biohealthkg.proto_okn.net_kg_schema_lower_than](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_lower_than.md) | <br/>| 18213 |
| [https___biohealthkg.proto_okn.net_kg_schema_MEASUREMENT_OF](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_MEASUREMENT_OF.md) | <br/>| 1044 |
| [https___biohealthkg.proto_okn.net_kg_schema_MEASURES](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_MEASURES.md) | <br/>| 198356 |
| [https___biohealthkg.proto_okn.net_kg_schema_METHOD_OF](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_METHOD_OF.md) | <br/>| 166871 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_ADMINISTERED_TO](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_ADMINISTERED_TO.md) | <br/>| 19210 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_AFFECTS](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_AFFECTS.md) | <br/>| 232543 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_ASSOCIATED_WITH](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_ASSOCIATED_WITH.md) | <br/>| 41914 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_AUGMENTS](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_AUGMENTS.md) | <br/>| 29081 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_CAUSES](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_CAUSES.md) | <br/>| 52999 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_COEXISTS_WITH](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_COEXISTS_WITH.md) | <br/>| 93570 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_COMPLICATES](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_COMPLICATES.md) | <br/>| 1221 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_CONVERTS_TO](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_CONVERTS_TO.md) | <br/>| 890 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_DIAGNOSES](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_DIAGNOSES.md) | <br/>| 22601 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_DISRUPTS](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_DISRUPTS.md) | <br/>| 29747 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_higher_than](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_higher_than.md) | <br/>| 3605 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_INHIBITS](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_INHIBITS.md) | <br/>| 38125 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_INTERACTS_WITH](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_INTERACTS_WITH.md) | <br/>| 115284 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_ISA](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_ISA.md) | <br/>| 25351 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_LOCATION_OF](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_LOCATION_OF.md) | <br/>| 125157 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_lower_than](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_lower_than.md) | <br/>| 442 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_MANIFESTATION_OF](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_MANIFESTATION_OF.md) | <br/>| 1622 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_MEASUREMENT_OF](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_MEASUREMENT_OF.md) | <br/>| 32 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_MEASURES](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_MEASURES.md) | <br/>| 4271 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_METHOD_OF](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_METHOD_OF.md) | <br/>| 7207 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_OCCURS_IN](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_OCCURS_IN.md) | <br/>| 3833 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_PART_OF](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_PART_OF.md) | <br/>| 55171 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_PRECEDES](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_PRECEDES.md) | <br/>| 6590 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_PREDISPOSES](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_PREDISPOSES.md) | <br/>| 25427 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_PREVENTS](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_PREVENTS.md) | <br/>| 15687 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_PROCESS_OF](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_PROCESS_OF.md) | <br/>| 89566 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_PRODUCES](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_PRODUCES.md) | <br/>| 18533 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_same_as](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_same_as.md) | <br/>| 5051 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_STIMULATES](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_STIMULATES.md) | <br/>| 36433 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_TREATS](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_TREATS.md) | <br/>| 114679 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_USES](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_USES.md) | <br/>| 11404 |
| [https___biohealthkg.proto_okn.net_kg_schema_OCCURS_IN](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_OCCURS_IN.md) | <br/>| 60478 |
| [https___biohealthkg.proto_okn.net_kg_schema_PROCESS_OF](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_PROCESS_OF.md) | <br/>| 1031114 |
| [https___biohealthkg.proto_okn.net_kg_schema_PRODUCES](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_PRODUCES.md) | <br/>| 258025 |
| [https___biohealthkg.proto_okn.net_kg_schema_same_as](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_same_as.md) | <br/>| 15090 |
| [https___biohealthkg.proto_okn.net_kg_schema_STIMULATES](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_STIMULATES.md) | <br/>| 537916 |
| [https___biohealthkg.proto_okn.net_kg_schema_USES](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_USES.md) | <br/>| 487481 |
| [https___w3id.org_biolink_vocab_affects](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___w3id.org_biolink_vocab_affects.md) | <br/>| 1758014 |
| [https___w3id.org_biolink_vocab_associated_with](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___w3id.org_biolink_vocab_associated_with.md) | <br/>| 668853 |
| [https___w3id.org_biolink_vocab_category](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___w3id.org_biolink_vocab_category.md) | <br/>| 250976 |
| [https___w3id.org_biolink_vocab_causes](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___w3id.org_biolink_vocab_causes.md) | <br/>| 924094 |
| [https___w3id.org_biolink_vocab_coexists_with](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___w3id.org_biolink_vocab_coexists_with.md) | <br/>| 1544559 |
| [https___w3id.org_biolink_vocab_decreases_amount_or_activity_of](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___w3id.org_biolink_vocab_decreases_amount_or_activity_of.md) | <br/>| 529827 |
| [https___w3id.org_biolink_vocab_diagnoses](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___w3id.org_biolink_vocab_diagnoses.md) | <br/>| 335442 |
| [https___w3id.org_biolink_vocab_disrupts](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___w3id.org_biolink_vocab_disrupts.md) | <br/>| 449816 |
| [https___w3id.org_biolink_vocab_increases_amount_or_activity_of](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___w3id.org_biolink_vocab_increases_amount_or_activity_of.md) | <br/>| 467851 |
| [https___w3id.org_biolink_vocab_interacts_with](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___w3id.org_biolink_vocab_interacts_with.md) | <br/>| 1198144 |
| [https___w3id.org_biolink_vocab_location_of](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___w3id.org_biolink_vocab_location_of.md) | <br/>| 2223662 |
| [https___w3id.org_biolink_vocab_manifestation_of](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___w3id.org_biolink_vocab_manifestation_of.md) | <br/>| 49173 |
| [https___w3id.org_biolink_vocab_part_of](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___w3id.org_biolink_vocab_part_of.md) | <br/>| 816950 |
| [https___w3id.org_biolink_vocab_precedes](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___w3id.org_biolink_vocab_precedes.md) | <br/>| 182490 |
| [https___w3id.org_biolink_vocab_predisposes_to_condition](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___w3id.org_biolink_vocab_predisposes_to_condition.md) | <br/>| 320163 |
| [https___w3id.org_biolink_vocab_preventative_for_condition](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___w3id.org_biolink_vocab_preventative_for_condition.md) | <br/>| 233021 |
| [https___w3id.org_biolink_vocab_subclass_of](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___w3id.org_biolink_vocab_subclass_of.md) | <br/>| 301438 |
| [https___w3id.org_biolink_vocab_treats](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___w3id.org_biolink_vocab_treats.md) | <br/>| 1549159 |









## IRI prefixes

* dct: http://purl.org/dc/terms/
* linkml: https://w3id.org/linkml/
* okn: https://purl.org/okn/
* okns: https://purl.org/okn/schema/
* rdf: http://www.w3.org/1999/02/22-rdf-syntax-ns#
* rdfs: http://www.w3.org/2000/01/rdf-schema#
