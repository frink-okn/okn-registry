# spoke-genelab





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
HttpsPurl.orgOknFrinkKgSpoke-genelabSchemaMetaNode {
    integer https___purl.org_okn_frink_kg_spoke_genelab_schema_end  
    date https___purl.org_okn_frink_kg_spoke_genelab_schema_start_date  
    string https___purl.org_okn_frink_kg_spoke_genelab_schema_material_2  
    uri https___purl.org_okn_frink_kg_spoke_genelab_schema_taxonomy  
    string https___purl.org_okn_frink_kg_spoke_genelab_schema_taxonomy  
    string https___purl.org_okn_frink_kg_spoke_genelab_schema_symbol  
    string https___purl.org_okn_frink_kg_spoke_genelab_schema_factor_space_1  
    integer https___purl.org_okn_frink_kg_spoke_genelab_schema_dist_to_feature  
    integer https___purl.org_okn_frink_kg_spoke_genelab_schema_start  
    string rdfs_label  
    string https___purl.org_okn_frink_kg_spoke_genelab_schema_material_id_2  
    string https___purl.org_okn_frink_kg_spoke_genelab_schema_flight_program  
    string https___purl.org_okn_frink_kg_spoke_genelab_schema_material_1  
    string https___purl.org_okn_frink_kg_spoke_genelab_schema_material_name_2  
    string https___purl.org_okn_frink_kg_spoke_genelab_schema_technology  
    string https___purl.org_okn_frink_kg_spoke_genelab_schema_organism  
    string https___purl.org_okn_frink_kg_spoke_genelab_schema_material_name_1  
    string https___purl.org_okn_frink_kg_spoke_genelab_schema_project_type  
    uri https___purl.org_okn_frink_kg_spoke_genelab_schema_chromosome  
    string https___purl.org_okn_frink_kg_spoke_genelab_schema_chromosome  
    string https___purl.org_okn_frink_kg_spoke_genelab_schema_measurement  
    date https___purl.org_okn_frink_kg_spoke_genelab_schema_end_date  
    string rdfs_comment  
    boolean https___purl.org_okn_frink_kg_spoke_genelab_schema_in_exon  
    string https___purl.org_okn_frink_kg_spoke_genelab_schema_factors_1  
    boolean https___purl.org_okn_frink_kg_spoke_genelab_schema_in_promoter  
    string https___purl.org_okn_frink_kg_spoke_genelab_schema_project_title  
    string https___purl.org_okn_frink_kg_spoke_genelab_schema_space_program  
    boolean https___purl.org_okn_frink_kg_spoke_genelab_schema_in_intron  
    string https___purl.org_okn_frink_kg_spoke_genelab_schema_factor_space_2  
    string https___purl.org_okn_frink_kg_spoke_genelab_schema_material_id_1  
    string https___purl.org_okn_frink_kg_spoke_genelab_schema_factors_2  
}
HttpsPurl.orgOknFrinkKgSpoke-genelabSchemaMethylationRegion {
    integer https___purl.org_okn_frink_kg_spoke_genelab_schema_end  
    integer https___purl.org_okn_frink_kg_spoke_genelab_schema_start  
    uri https___purl.org_okn_frink_kg_spoke_genelab_schema_chromosome  
    string https___purl.org_okn_frink_kg_spoke_genelab_schema_chromosome  
    boolean https___purl.org_okn_frink_kg_spoke_genelab_schema_in_intron  
    boolean https___purl.org_okn_frink_kg_spoke_genelab_schema_in_promoter  
    string rdfs_label  
    integer https___purl.org_okn_frink_kg_spoke_genelab_schema_dist_to_feature  
    boolean https___purl.org_okn_frink_kg_spoke_genelab_schema_in_exon  
}
HttpsPurl.orgOknFrinkKgSpoke-genelabSchemaMission {
    string https___purl.org_okn_frink_kg_spoke_genelab_schema_space_program  
    date https___purl.org_okn_frink_kg_spoke_genelab_schema_start_date  
    date https___purl.org_okn_frink_kg_spoke_genelab_schema_end_date  
    string rdfs_label  
    string https___purl.org_okn_frink_kg_spoke_genelab_schema_flight_program  
}
HttpsW3id.orgBiolinkVocabAnatomicalEntity {

}
HttpsW3id.orgBiolinkVocabCell {

}
HttpsW3id.orgBiolinkVocabGene {
    string https___purl.org_okn_frink_kg_spoke_genelab_schema_organism  
    uri https___purl.org_okn_frink_kg_spoke_genelab_schema_taxonomy  
    string https___purl.org_okn_frink_kg_spoke_genelab_schema_taxonomy  
    string https___purl.org_okn_frink_kg_spoke_genelab_schema_symbol  
    string rdfs_label  
}
HttpsW3id.orgBiolinkVocabStudy {
    string https___purl.org_okn_frink_kg_spoke_genelab_schema_project_title  
    string https___purl.org_okn_frink_kg_spoke_genelab_schema_organism  
    string https___purl.org_okn_frink_kg_spoke_genelab_schema_project_type  
    uri https___purl.org_okn_frink_kg_spoke_genelab_schema_taxonomy  
    string https___purl.org_okn_frink_kg_spoke_genelab_schema_taxonomy  
    string rdfs_comment  
    string rdfs_label  
}
OboOBI0000070 {
    string https___purl.org_okn_frink_kg_spoke_genelab_schema_material_1  
    string https___purl.org_okn_frink_kg_spoke_genelab_schema_material_name_2  
    string https___purl.org_okn_frink_kg_spoke_genelab_schema_technology  
    string https___purl.org_okn_frink_kg_spoke_genelab_schema_material_name_1  
    string https___purl.org_okn_frink_kg_spoke_genelab_schema_material_2  
    string https___purl.org_okn_frink_kg_spoke_genelab_schema_measurement  
    string https___purl.org_okn_frink_kg_spoke_genelab_schema_factor_space_2  
    string https___purl.org_okn_frink_kg_spoke_genelab_schema_material_id_1  
    string https___purl.org_okn_frink_kg_spoke_genelab_schema_factor_space_1  
    string rdfs_label  
    string https___purl.org_okn_frink_kg_spoke_genelab_schema_material_id_2  
    string https___purl.org_okn_frink_kg_spoke_genelab_schema_factors_1  
    string https___purl.org_okn_frink_kg_spoke_genelab_schema_factors_2  
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
HttpsPurl.orgOknFrinkKgSpoke-genelabSchemaMetaNode ||--|o RdfsLiteral : "rdfs_label"
HttpsPurl.orgOknFrinkKgSpoke-genelabSchemaMetaNode ||--|o HttpsW3id.orgBiolinkVocabAnatomicalEntity : "https___purl.org_okn_frink_kg_spoke-genelab_schema_material_id_2"
HttpsPurl.orgOknFrinkKgSpoke-genelabSchemaMetaNode ||--|o HttpsW3id.orgBiolinkVocabCell : "https___purl.org_okn_frink_kg_spoke-genelab_schema_material_id_2"
HttpsPurl.orgOknFrinkKgSpoke-genelabSchemaMetaNode ||--|o RdfsLiteral : "rdfs_comment"
HttpsPurl.orgOknFrinkKgSpoke-genelabSchemaMetaNode ||--|o HttpsPurl.orgOknFrinkKgSpoke-genelabSchemaMetaNode : "https___purl.org_okn_frink_kg_spoke-genelab_schema_MetaRelationship"
HttpsPurl.orgOknFrinkKgSpoke-genelabSchemaMetaNode ||--|o HttpsW3id.orgBiolinkVocabAnatomicalEntity : "https___purl.org_okn_frink_kg_spoke-genelab_schema_material_id_1"
HttpsPurl.orgOknFrinkKgSpoke-genelabSchemaMetaNode ||--|o HttpsW3id.orgBiolinkVocabCell : "https___purl.org_okn_frink_kg_spoke-genelab_schema_material_id_1"
HttpsPurl.orgOknFrinkKgSpoke-genelabSchemaMethylationRegion ||--|o RdfsLiteral : "rdfs_label"
HttpsPurl.orgOknFrinkKgSpoke-genelabSchemaMission ||--|o HttpsW3id.orgBiolinkVocabStudy : "https___purl.org_okn_frink_kg_spoke-genelab_schema_CONDUCTED_MIcS"
HttpsPurl.orgOknFrinkKgSpoke-genelabSchemaMission ||--|o RdfsLiteral : "rdfs_label"
HttpsW3id.orgBiolinkVocabGene ||--|o HttpsW3id.orgBiolinkVocabGene : "https___purl.org_okn_frink_kg_spoke-genelab_schema_IS_ORTHOLOG_MGiG"
HttpsW3id.orgBiolinkVocabGene ||--|o HttpsPurl.orgOknFrinkKgSpoke-genelabSchemaMethylationRegion : "https___purl.org_okn_frink_kg_spoke-genelab_schema_METHYLATED_IN_MGmMR"
HttpsW3id.orgBiolinkVocabGene ||--|o RdfsLiteral : "rdfs_label"
HttpsW3id.orgBiolinkVocabStudy ||--|o OboOBI0000070 : "https___purl.org_okn_frink_kg_spoke-genelab_schema_PERFORMED_SpAS"
HttpsW3id.orgBiolinkVocabStudy ||--|o RdfsLiteral : "rdfs_comment"
HttpsW3id.orgBiolinkVocabStudy ||--|o RdfsLiteral : "rdfs_label"
OboOBI0000070 ||--|o HttpsW3id.orgBiolinkVocabAnatomicalEntity : "https___purl.org_okn_frink_kg_spoke-genelab_schema_INVESTIGATED_ASiA"
OboOBI0000070 ||--|o HttpsPurl.orgOknFrinkKgSpoke-genelabSchemaMethylationRegion : "https___purl.org_okn_frink_kg_spoke-genelab_schema_MEASURED_DIFFERENTIAL_METHYLATION_ASmMR"
OboOBI0000070 ||--|o HttpsW3id.orgBiolinkVocabCell : "https___purl.org_okn_frink_kg_spoke-genelab_schema_INVESTIGATED_ASiCT"
OboOBI0000070 ||--|o HttpsW3id.orgBiolinkVocabGene : "https___purl.org_okn_frink_kg_spoke-genelab_schema_MEASURED_DIFFERENTIAL_EXPRESSION_ASmMG"
OboOBI0000070 ||--|o HttpsW3id.orgBiolinkVocabAnatomicalEntity : "https___purl.org_okn_frink_kg_spoke-genelab_schema_material_id_1"
OboOBI0000070 ||--|o HttpsW3id.orgBiolinkVocabCell : "https___purl.org_okn_frink_kg_spoke-genelab_schema_material_id_1"
OboOBI0000070 ||--|o RdfsLiteral : "rdfs_label"
OboOBI0000070 ||--|o HttpsW3id.orgBiolinkVocabAnatomicalEntity : "https___purl.org_okn_frink_kg_spoke-genelab_schema_material_id_2"
OboOBI0000070 ||--|o HttpsW3id.orgBiolinkVocabCell : "https___purl.org_okn_frink_kg_spoke-genelab_schema_material_id_2"

```



## Imports


* okns:owl-rdf-rdfs
* okns:extended_types
* linkml:types



## Classes

| Class | Description | Occurrences |
| --- | --- | --- |
| [HttpsPurl.orgOknFrinkKgSpoke-genelabSchemaMetaNode](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-genelab/classes/HttpsPurl.orgOknFrinkKgSpoke-genelabSchemaMetaNode.md) | None<br/>| 8 | 
| [HttpsPurl.orgOknFrinkKgSpoke-genelabSchemaMethylationRegion](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-genelab/classes/HttpsPurl.orgOknFrinkKgSpoke-genelabSchemaMethylationRegion.md) | None<br/>| 5663 | 
| [HttpsPurl.orgOknFrinkKgSpoke-genelabSchemaMission](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-genelab/classes/HttpsPurl.orgOknFrinkKgSpoke-genelabSchemaMission.md) | None<br/>| 23 | 
| [HttpsW3id.orgBiolinkVocabAnatomicalEntity](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-genelab/classes/HttpsW3id.orgBiolinkVocabAnatomicalEntity.md) | None<br/>| 33 | 
| [HttpsW3id.orgBiolinkVocabCell](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-genelab/classes/HttpsW3id.orgBiolinkVocabCell.md) | None<br/>| 7 | 
| [HttpsW3id.orgBiolinkVocabGene](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-genelab/classes/HttpsW3id.orgBiolinkVocabGene.md) | None<br/>| 59756 | 
| [HttpsW3id.orgBiolinkVocabStudy](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-genelab/classes/HttpsW3id.orgBiolinkVocabStudy.md) | None<br/>| 140 | 
| [OboOBI0000070](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-genelab/classes/OboOBI0000070.md) | None<br/>| 6467 | 





## Slots

| Slot | Description | Occurrences |
| --- | --- | --- |
| [https___purl.org_okn_frink_kg_spoke_genelab_schema_adj_p_value](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-genelab/slots/https___purl.org_okn_frink_kg_spoke_genelab_schema_adj_p_value.md) | <br/>| 13208663 |
| [https___purl.org_okn_frink_kg_spoke_genelab_schema_chromosome](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-genelab/slots/https___purl.org_okn_frink_kg_spoke_genelab_schema_chromosome.md) | <br/>| 5664 |
| [https___purl.org_okn_frink_kg_spoke_genelab_schema_CONDUCTED_MIcS](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-genelab/slots/https___purl.org_okn_frink_kg_spoke_genelab_schema_CONDUCTED_MIcS.md) | <br/>| 86 |
| [https___purl.org_okn_frink_kg_spoke_genelab_schema_dist_to_feature](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-genelab/slots/https___purl.org_okn_frink_kg_spoke_genelab_schema_dist_to_feature.md) | <br/>| 5664 |
| [https___purl.org_okn_frink_kg_spoke_genelab_schema_end](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-genelab/slots/https___purl.org_okn_frink_kg_spoke_genelab_schema_end.md) | <br/>| 5664 |
| [https___purl.org_okn_frink_kg_spoke_genelab_schema_end_date](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-genelab/slots/https___purl.org_okn_frink_kg_spoke_genelab_schema_end_date.md) | <br/>| 23 |
| [https___purl.org_okn_frink_kg_spoke_genelab_schema_factor_space_1](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-genelab/slots/https___purl.org_okn_frink_kg_spoke_genelab_schema_factor_space_1.md) | <br/>| 3020 |
| [https___purl.org_okn_frink_kg_spoke_genelab_schema_factor_space_2](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-genelab/slots/https___purl.org_okn_frink_kg_spoke_genelab_schema_factor_space_2.md) | <br/>| 3104 |
| [https___purl.org_okn_frink_kg_spoke_genelab_schema_factors_1](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-genelab/slots/https___purl.org_okn_frink_kg_spoke_genelab_schema_factors_1.md) | <br/>| 17070 |
| [https___purl.org_okn_frink_kg_spoke_genelab_schema_factors_2](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-genelab/slots/https___purl.org_okn_frink_kg_spoke_genelab_schema_factors_2.md) | <br/>| 17642 |
| [https___purl.org_okn_frink_kg_spoke_genelab_schema_flight_program](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-genelab/slots/https___purl.org_okn_frink_kg_spoke_genelab_schema_flight_program.md) | <br/>| 22 |
| [https___purl.org_okn_frink_kg_spoke_genelab_schema_from](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-genelab/slots/https___purl.org_okn_frink_kg_spoke_genelab_schema_from.md) | <br/>| 8 |
| [https___purl.org_okn_frink_kg_spoke_genelab_schema_in_exon](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-genelab/slots/https___purl.org_okn_frink_kg_spoke_genelab_schema_in_exon.md) | <br/>| 5664 |
| [https___purl.org_okn_frink_kg_spoke_genelab_schema_in_intron](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-genelab/slots/https___purl.org_okn_frink_kg_spoke_genelab_schema_in_intron.md) | <br/>| 5664 |
| [https___purl.org_okn_frink_kg_spoke_genelab_schema_in_promoter](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-genelab/slots/https___purl.org_okn_frink_kg_spoke_genelab_schema_in_promoter.md) | <br/>| 5664 |
| [https___purl.org_okn_frink_kg_spoke_genelab_schema_INVESTIGATED_ASiA](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-genelab/slots/https___purl.org_okn_frink_kg_spoke_genelab_schema_INVESTIGATED_ASiA.md) | <br/>| 5033 |
| [https___purl.org_okn_frink_kg_spoke_genelab_schema_INVESTIGATED_ASiCT](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-genelab/slots/https___purl.org_okn_frink_kg_spoke_genelab_schema_INVESTIGATED_ASiCT.md) | <br/>| 1134 |
| [https___purl.org_okn_frink_kg_spoke_genelab_schema_IS_ORTHOLOG_MGiG](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-genelab/slots/https___purl.org_okn_frink_kg_spoke_genelab_schema_IS_ORTHOLOG_MGiG.md) | <br/>| 57492 |
| [https___purl.org_okn_frink_kg_spoke_genelab_schema_log2fc](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-genelab/slots/https___purl.org_okn_frink_kg_spoke_genelab_schema_log2fc.md) | <br/>| 13208663 |
| [https___purl.org_okn_frink_kg_spoke_genelab_schema_material_1](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-genelab/slots/https___purl.org_okn_frink_kg_spoke_genelab_schema_material_1.md) | <br/>| 6468 |
| [https___purl.org_okn_frink_kg_spoke_genelab_schema_material_2](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-genelab/slots/https___purl.org_okn_frink_kg_spoke_genelab_schema_material_2.md) | <br/>| 6468 |
| [https___purl.org_okn_frink_kg_spoke_genelab_schema_material_id_1](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-genelab/slots/https___purl.org_okn_frink_kg_spoke_genelab_schema_material_id_1.md) | <br/>| 6164 |
| [https___purl.org_okn_frink_kg_spoke_genelab_schema_material_id_2](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-genelab/slots/https___purl.org_okn_frink_kg_spoke_genelab_schema_material_id_2.md) | <br/>| 6164 |
| [https___purl.org_okn_frink_kg_spoke_genelab_schema_material_name_1](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-genelab/slots/https___purl.org_okn_frink_kg_spoke_genelab_schema_material_name_1.md) | <br/>| 6164 |
| [https___purl.org_okn_frink_kg_spoke_genelab_schema_material_name_2](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-genelab/slots/https___purl.org_okn_frink_kg_spoke_genelab_schema_material_name_2.md) | <br/>| 6164 |
| [https___purl.org_okn_frink_kg_spoke_genelab_schema_MEASURED_DIFFERENTIAL_EXPRESSION_ASmMG](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-genelab/slots/https___purl.org_okn_frink_kg_spoke_genelab_schema_MEASURED_DIFFERENTIAL_EXPRESSION_ASmMG.md) | <br/>| 13208662 |
| [https___purl.org_okn_frink_kg_spoke_genelab_schema_MEASURED_DIFFERENTIAL_METHYLATION_ASmMR](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-genelab/slots/https___purl.org_okn_frink_kg_spoke_genelab_schema_MEASURED_DIFFERENTIAL_METHYLATION_ASmMR.md) | <br/>| 9555 |
| [https___purl.org_okn_frink_kg_spoke_genelab_schema_measurement](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-genelab/slots/https___purl.org_okn_frink_kg_spoke_genelab_schema_measurement.md) | <br/>| 6468 |
| [https___purl.org_okn_frink_kg_spoke_genelab_schema_MetaRelationship](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-genelab/slots/https___purl.org_okn_frink_kg_spoke_genelab_schema_MetaRelationship.md) | <br/>| 8 |
| [https___purl.org_okn_frink_kg_spoke_genelab_schema_METHYLATED_IN_MGmMR](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-genelab/slots/https___purl.org_okn_frink_kg_spoke_genelab_schema_METHYLATED_IN_MGmMR.md) | <br/>| 5694 |
| [https___purl.org_okn_frink_kg_spoke_genelab_schema_methylation_diff](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-genelab/slots/https___purl.org_okn_frink_kg_spoke_genelab_schema_methylation_diff.md) | <br/>| 9556 |
| [https___purl.org_okn_frink_kg_spoke_genelab_schema_organism](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-genelab/slots/https___purl.org_okn_frink_kg_spoke_genelab_schema_organism.md) | <br/>| 58791 |
| [https___purl.org_okn_frink_kg_spoke_genelab_schema_PERFORMED_SpAS](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-genelab/slots/https___purl.org_okn_frink_kg_spoke_genelab_schema_PERFORMED_SpAS.md) | <br/>| 6467 |
| [https___purl.org_okn_frink_kg_spoke_genelab_schema_project_title](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-genelab/slots/https___purl.org_okn_frink_kg_spoke_genelab_schema_project_title.md) | <br/>| 77 |
| [https___purl.org_okn_frink_kg_spoke_genelab_schema_project_type](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-genelab/slots/https___purl.org_okn_frink_kg_spoke_genelab_schema_project_type.md) | <br/>| 141 |
| [https___purl.org_okn_frink_kg_spoke_genelab_schema_q_value](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-genelab/slots/https___purl.org_okn_frink_kg_spoke_genelab_schema_q_value.md) | <br/>| 9556 |
| [https___purl.org_okn_frink_kg_spoke_genelab_schema_space_program](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-genelab/slots/https___purl.org_okn_frink_kg_spoke_genelab_schema_space_program.md) | <br/>| 24 |
| [https___purl.org_okn_frink_kg_spoke_genelab_schema_start](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-genelab/slots/https___purl.org_okn_frink_kg_spoke_genelab_schema_start.md) | <br/>| 5664 |
| [https___purl.org_okn_frink_kg_spoke_genelab_schema_start_date](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-genelab/slots/https___purl.org_okn_frink_kg_spoke_genelab_schema_start_date.md) | <br/>| 24 |
| [https___purl.org_okn_frink_kg_spoke_genelab_schema_symbol](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-genelab/slots/https___purl.org_okn_frink_kg_spoke_genelab_schema_symbol.md) | <br/>| 58650 |
| [https___purl.org_okn_frink_kg_spoke_genelab_schema_taxonomy](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-genelab/slots/https___purl.org_okn_frink_kg_spoke_genelab_schema_taxonomy.md) | <br/>| 58791 |
| [https___purl.org_okn_frink_kg_spoke_genelab_schema_technology](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-genelab/slots/https___purl.org_okn_frink_kg_spoke_genelab_schema_technology.md) | <br/>| 6468 |
| [https___purl.org_okn_frink_kg_spoke_genelab_schema_to](https://github.com/frink-okn/graph-descriptions/blob/main/spoke-genelab/slots/https___purl.org_okn_frink_kg_spoke_genelab_schema_to.md) | <br/>| 8 |









## IRI prefixes

* linkml: https://w3id.org/linkml/
* obo: http://purl.obolibrary.org/obo/
* okn: https://purl.org/okn/
* okns: https://purl.org/okn/schema/
* rdf: http://www.w3.org/1999/02/22-rdf-syntax-ns#
* rdfs: http://www.w3.org/2000/01/rdf-schema#
* xsd: http://www.w3.org/2001/XMLSchema#
* shex: http://www.w3.org/ns/shex#
* schema: http://schema.org/
