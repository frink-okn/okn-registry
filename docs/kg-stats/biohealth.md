# biohealthkg

No schema description specified



## Schema Diagram

```mermaid
erDiagram
HttpsW3id.orgBiolinkVocabEntity {
    uri https___w3id.org_biolink_vocab_category  
    string rdfs_label  
}
RdfStatement {
    uri rdf_predicate  
    string dct_source  
}

HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___w3id.org_biolink_vocab_increases_amount_or_activity_of"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_COMPLICATES"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_COMPLICATES"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___w3id.org_biolink_vocab_predisposes_to_condition"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___w3id.org_biolink_vocab_part_of"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_USES"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_ADMINISTERED_TO"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_CONVERTS_TO"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___w3id.org_biolink_vocab_disrupts"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_MANIFESTATION_OF"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_PRODUCES"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_MEASURES"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___w3id.org_biolink_vocab_causes"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_LOCATION_OF"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_higher_than"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_CAUSES"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_compared_with"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_MEASUREMENT_OF"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_AUGMENTS"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_same_as"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_ISA"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___w3id.org_biolink_vocab_interacts_with"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_TREATS"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_lower_than"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_INHIBITS"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_AFFECTS"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___w3id.org_biolink_vocab_affects"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_lower_than"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___w3id.org_biolink_vocab_subclass_of"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___w3id.org_biolink_vocab_precedes"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_METHOD_OF"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_DISRUPTS"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_STIMULATES"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_MEASUREMENT_OF"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___w3id.org_biolink_vocab_preventative_for_condition"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___w3id.org_biolink_vocab_manifestation_of"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_same_as"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_higher_than"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_PROCESS_OF"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_ADMINISTERED_TO"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_INTERACTS_WITH"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___w3id.org_biolink_vocab_coexists_with"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_OCCURS_IN"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_DIAGNOSES"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___w3id.org_biolink_vocab_associated_with"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_USES"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_PROCESS_OF"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_COEXISTS_WITH"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___w3id.org_biolink_vocab_decreases_amount_or_activity_of"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_METHOD_OF"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_PRECEDES"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___w3id.org_biolink_vocab_location_of"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___w3id.org_biolink_vocab_diagnoses"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_LOCATION_OF(SPEC)"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_PART_OF"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_ASSOCIATED_WITH"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_PREVENTS"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_NEG_PREDISPOSES"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_OCCURS_IN"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_CONVERTS_TO"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_MEASURES"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_STIMULATES"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___biohealthkg.proto-okn.net_kg_schema_PRODUCES"
HttpsW3id.orgBiolinkVocabEntity ||--|o HttpsW3id.orgBiolinkVocabEntity : "https___w3id.org_biolink_vocab_treats"
RdfStatement ||--|o HttpsW3id.orgBiolinkVocabEntity : "rdf_subject"
RdfStatement ||--|o HttpsW3id.orgBiolinkVocabEntity : "rdf_object"

```



## Classes

| Class | Description | Occurrences |
| --- | --- | --- |
| [HttpsW3id.orgBiolinkVocabEntity](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/classes/HttpsW3id.orgBiolinkVocabEntity.md) | No class (type) description specified<br/>| 250976 | 
| [RdfStatement](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/classes/RdfStatement.md) | No class (type) description specified<br/>| 18352179 | 





## Slots

| Slot | Description | Occurrences |
| --- | --- | --- |
| [dct_source](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/dct_source.md) | No slot (predicate) description specified<br/>| 18352179 |
| [https___biohealthkg.proto_okn.net_kg_schema_ADMINISTERED_TO](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_ADMINISTERED_TO.md) | No slot (predicate) description specified<br/>| 234354 |
| [https___biohealthkg.proto_okn.net_kg_schema_compared_with](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_compared_with.md) | No slot (predicate) description specified<br/>| 370807 |
| [https___biohealthkg.proto_okn.net_kg_schema_COMPLICATES](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_COMPLICATES.md) | No slot (predicate) description specified<br/>| 53189 |
| [https___biohealthkg.proto_okn.net_kg_schema_CONVERTS_TO](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_CONVERTS_TO.md) | No slot (predicate) description specified<br/>| 39403 |
| [https___biohealthkg.proto_okn.net_kg_schema_higher_than](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_higher_than.md) | No slot (predicate) description specified<br/>| 99934 |
| [https___biohealthkg.proto_okn.net_kg_schema_LOCATION_OF(SPEC)](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_LOCATION_OF(SPEC).md) | No slot (predicate) description specified<br/>| 2 |
| [https___biohealthkg.proto_okn.net_kg_schema_lower_than](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_lower_than.md) | No slot (predicate) description specified<br/>| 18213 |
| [https___biohealthkg.proto_okn.net_kg_schema_MEASUREMENT_OF](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_MEASUREMENT_OF.md) | No slot (predicate) description specified<br/>| 1044 |
| [https___biohealthkg.proto_okn.net_kg_schema_MEASURES](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_MEASURES.md) | No slot (predicate) description specified<br/>| 198356 |
| [https___biohealthkg.proto_okn.net_kg_schema_METHOD_OF](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_METHOD_OF.md) | No slot (predicate) description specified<br/>| 166871 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_ADMINISTERED_TO](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_ADMINISTERED_TO.md) | No slot (predicate) description specified<br/>| 19210 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_AFFECTS](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_AFFECTS.md) | No slot (predicate) description specified<br/>| 232543 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_ASSOCIATED_WITH](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_ASSOCIATED_WITH.md) | No slot (predicate) description specified<br/>| 41914 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_AUGMENTS](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_AUGMENTS.md) | No slot (predicate) description specified<br/>| 29081 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_CAUSES](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_CAUSES.md) | No slot (predicate) description specified<br/>| 52999 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_COEXISTS_WITH](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_COEXISTS_WITH.md) | No slot (predicate) description specified<br/>| 93570 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_COMPLICATES](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_COMPLICATES.md) | No slot (predicate) description specified<br/>| 1221 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_CONVERTS_TO](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_CONVERTS_TO.md) | No slot (predicate) description specified<br/>| 890 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_DIAGNOSES](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_DIAGNOSES.md) | No slot (predicate) description specified<br/>| 22601 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_DISRUPTS](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_DISRUPTS.md) | No slot (predicate) description specified<br/>| 29747 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_higher_than](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_higher_than.md) | No slot (predicate) description specified<br/>| 3605 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_INHIBITS](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_INHIBITS.md) | No slot (predicate) description specified<br/>| 38125 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_INTERACTS_WITH](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_INTERACTS_WITH.md) | No slot (predicate) description specified<br/>| 115284 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_ISA](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_ISA.md) | No slot (predicate) description specified<br/>| 25351 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_LOCATION_OF](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_LOCATION_OF.md) | No slot (predicate) description specified<br/>| 125157 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_lower_than](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_lower_than.md) | No slot (predicate) description specified<br/>| 442 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_MANIFESTATION_OF](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_MANIFESTATION_OF.md) | No slot (predicate) description specified<br/>| 1622 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_MEASUREMENT_OF](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_MEASUREMENT_OF.md) | No slot (predicate) description specified<br/>| 32 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_MEASURES](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_MEASURES.md) | No slot (predicate) description specified<br/>| 4271 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_METHOD_OF](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_METHOD_OF.md) | No slot (predicate) description specified<br/>| 7207 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_OCCURS_IN](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_OCCURS_IN.md) | No slot (predicate) description specified<br/>| 3833 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_PART_OF](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_PART_OF.md) | No slot (predicate) description specified<br/>| 55171 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_PRECEDES](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_PRECEDES.md) | No slot (predicate) description specified<br/>| 6590 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_PREDISPOSES](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_PREDISPOSES.md) | No slot (predicate) description specified<br/>| 25427 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_PREVENTS](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_PREVENTS.md) | No slot (predicate) description specified<br/>| 15687 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_PROCESS_OF](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_PROCESS_OF.md) | No slot (predicate) description specified<br/>| 89566 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_PRODUCES](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_PRODUCES.md) | No slot (predicate) description specified<br/>| 18533 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_same_as](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_same_as.md) | No slot (predicate) description specified<br/>| 5051 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_STIMULATES](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_STIMULATES.md) | No slot (predicate) description specified<br/>| 36433 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_TREATS](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_TREATS.md) | No slot (predicate) description specified<br/>| 114679 |
| [https___biohealthkg.proto_okn.net_kg_schema_NEG_USES](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_NEG_USES.md) | No slot (predicate) description specified<br/>| 11404 |
| [https___biohealthkg.proto_okn.net_kg_schema_OCCURS_IN](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_OCCURS_IN.md) | No slot (predicate) description specified<br/>| 60478 |
| [https___biohealthkg.proto_okn.net_kg_schema_PROCESS_OF](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_PROCESS_OF.md) | No slot (predicate) description specified<br/>| 1031114 |
| [https___biohealthkg.proto_okn.net_kg_schema_PRODUCES](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_PRODUCES.md) | No slot (predicate) description specified<br/>| 258025 |
| [https___biohealthkg.proto_okn.net_kg_schema_same_as](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_same_as.md) | No slot (predicate) description specified<br/>| 15090 |
| [https___biohealthkg.proto_okn.net_kg_schema_STIMULATES](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_STIMULATES.md) | No slot (predicate) description specified<br/>| 537916 |
| [https___biohealthkg.proto_okn.net_kg_schema_USES](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___biohealthkg.proto_okn.net_kg_schema_USES.md) | No slot (predicate) description specified<br/>| 487481 |
| [https___w3id.org_biolink_vocab_affects](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___w3id.org_biolink_vocab_affects.md) | No slot (predicate) description specified<br/>| 1758014 |
| [https___w3id.org_biolink_vocab_associated_with](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___w3id.org_biolink_vocab_associated_with.md) | No slot (predicate) description specified<br/>| 668853 |
| [https___w3id.org_biolink_vocab_category](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___w3id.org_biolink_vocab_category.md) | No slot (predicate) description specified<br/>| 250976 |
| [https___w3id.org_biolink_vocab_causes](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___w3id.org_biolink_vocab_causes.md) | No slot (predicate) description specified<br/>| 924094 |
| [https___w3id.org_biolink_vocab_coexists_with](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___w3id.org_biolink_vocab_coexists_with.md) | No slot (predicate) description specified<br/>| 1544559 |
| [https___w3id.org_biolink_vocab_decreases_amount_or_activity_of](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___w3id.org_biolink_vocab_decreases_amount_or_activity_of.md) | No slot (predicate) description specified<br/>| 529827 |
| [https___w3id.org_biolink_vocab_diagnoses](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___w3id.org_biolink_vocab_diagnoses.md) | No slot (predicate) description specified<br/>| 335442 |
| [https___w3id.org_biolink_vocab_disrupts](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___w3id.org_biolink_vocab_disrupts.md) | No slot (predicate) description specified<br/>| 449816 |
| [https___w3id.org_biolink_vocab_increases_amount_or_activity_of](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___w3id.org_biolink_vocab_increases_amount_or_activity_of.md) | No slot (predicate) description specified<br/>| 467851 |
| [https___w3id.org_biolink_vocab_interacts_with](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___w3id.org_biolink_vocab_interacts_with.md) | No slot (predicate) description specified<br/>| 1198144 |
| [https___w3id.org_biolink_vocab_location_of](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___w3id.org_biolink_vocab_location_of.md) | No slot (predicate) description specified<br/>| 2223662 |
| [https___w3id.org_biolink_vocab_manifestation_of](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___w3id.org_biolink_vocab_manifestation_of.md) | No slot (predicate) description specified<br/>| 49173 |
| [https___w3id.org_biolink_vocab_part_of](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___w3id.org_biolink_vocab_part_of.md) | No slot (predicate) description specified<br/>| 816950 |
| [https___w3id.org_biolink_vocab_precedes](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___w3id.org_biolink_vocab_precedes.md) | No slot (predicate) description specified<br/>| 182490 |
| [https___w3id.org_biolink_vocab_predisposes_to_condition](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___w3id.org_biolink_vocab_predisposes_to_condition.md) | No slot (predicate) description specified<br/>| 320163 |
| [https___w3id.org_biolink_vocab_preventative_for_condition](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___w3id.org_biolink_vocab_preventative_for_condition.md) | No slot (predicate) description specified<br/>| 233021 |
| [https___w3id.org_biolink_vocab_subclass_of](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___w3id.org_biolink_vocab_subclass_of.md) | No slot (predicate) description specified<br/>| 301438 |
| [https___w3id.org_biolink_vocab_treats](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/https___w3id.org_biolink_vocab_treats.md) | No slot (predicate) description specified<br/>| 1549159 |
| [rdf_object](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/rdf_object.md) | No slot (predicate) description specified<br/>| 18352179 |
| [rdf_predicate](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/rdf_predicate.md) | No slot (predicate) description specified<br/>| 18352179 |
| [rdf_subject](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/rdf_subject.md) | No slot (predicate) description specified<br/>| 18352179 |
| [rdfs_label](https://github.com/frink-okn/graph-descriptions/blob/main/biohealth/slots/rdfs_label.md) | No slot (predicate) description specified<br/>| 250976 |









## IRI prefixes

* dct: http://purl.org/dc/terms/
* linkml: https://w3id.org/linkml/
* rdf: http://www.w3.org/1999/02/22-rdf-syntax-ns#
* rdfs: http://www.w3.org/2000/01/rdf-schema#
* xsd: http://www.w3.org/2001/XMLSchema#
* shex: http://www.w3.org/ns/shex#
* schema: http://schema.org/
