# biobricks-mesh





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
HttpId.nlm.nih.govMeshVocab#AllowedDescriptorQualifierPair {
    string http___id.nlm.nih.gov_mesh_vocab#lastActiveYear  
    boolean http___id.nlm.nih.gov_mesh_vocab#active  
    string rdfs_label  
}
HttpId.nlm.nih.govMeshVocab#CheckTag {
    date http___id.nlm.nih.gov_mesh_vocab#dateCreated  
    string http___id.nlm.nih.gov_mesh_vocab#historyNote  
    date http___id.nlm.nih.gov_mesh_vocab#dateRevised  
    string http___id.nlm.nih.gov_mesh_vocab#identifier  
    string http___id.nlm.nih.gov_mesh_vocab#annotation  
    boolean http___id.nlm.nih.gov_mesh_vocab#active  
    date http___id.nlm.nih.gov_mesh_vocab#dateEstablished  
    string rdfs_label  
}
HttpId.nlm.nih.govMeshVocab#Concept {
    string http___id.nlm.nih.gov_mesh_vocab#lastActiveYear  
    string http___id.nlm.nih.gov_mesh_vocab#casn1_label  
    string http___id.nlm.nih.gov_mesh_vocab#identifier  
    string http___id.nlm.nih.gov_mesh_vocab#registryNumber  
    boolean http___id.nlm.nih.gov_mesh_vocab#active  
    string http___id.nlm.nih.gov_mesh_vocab#scopeNote  
    string http___id.nlm.nih.gov_mesh_vocab#relatedRegistryNumber  
    string rdfs_label  
}
HttpId.nlm.nih.govMeshVocab#DisallowedDescriptorQualifierPair {
    string http___id.nlm.nih.gov_mesh_vocab#lastActiveYear  
    boolean http___id.nlm.nih.gov_mesh_vocab#active  
    string rdfs_label  
}
HttpId.nlm.nih.govMeshVocab#GeographicalDescriptor {
    date http___id.nlm.nih.gov_mesh_vocab#dateCreated  
    string http___id.nlm.nih.gov_mesh_vocab#historyNote  
    date http___id.nlm.nih.gov_mesh_vocab#dateRevised  
    string http___id.nlm.nih.gov_mesh_vocab#identifier  
    string http___id.nlm.nih.gov_mesh_vocab#annotation  
    boolean http___id.nlm.nih.gov_mesh_vocab#active  
    date http___id.nlm.nih.gov_mesh_vocab#dateEstablished  
    string http___id.nlm.nih.gov_mesh_vocab#previousIndexing  
    string http___id.nlm.nih.gov_mesh_vocab#onlineNote  
    string rdfs_label  
}
HttpId.nlm.nih.govMeshVocab#PublicationType {
    date http___id.nlm.nih.gov_mesh_vocab#dateCreated  
    string http___id.nlm.nih.gov_mesh_vocab#historyNote  
    date http___id.nlm.nih.gov_mesh_vocab#dateRevised  
    string http___id.nlm.nih.gov_mesh_vocab#identifier  
    string http___id.nlm.nih.gov_mesh_vocab#annotation  
    boolean http___id.nlm.nih.gov_mesh_vocab#active  
    string http___id.nlm.nih.gov_mesh_vocab#nlmClassificationNumber  
    date http___id.nlm.nih.gov_mesh_vocab#dateEstablished  
    string http___id.nlm.nih.gov_mesh_vocab#previousIndexing  
    string rdfs_label  
}
HttpId.nlm.nih.govMeshVocab#Qualifier {
    date http___id.nlm.nih.gov_mesh_vocab#dateCreated  
    string http___id.nlm.nih.gov_mesh_vocab#historyNote  
    string http___id.nlm.nih.gov_mesh_vocab#lastActiveYear  
    date http___id.nlm.nih.gov_mesh_vocab#dateRevised  
    string http___id.nlm.nih.gov_mesh_vocab#identifier  
    string http___id.nlm.nih.gov_mesh_vocab#annotation  
    boolean http___id.nlm.nih.gov_mesh_vocab#active  
    date http___id.nlm.nih.gov_mesh_vocab#dateEstablished  
    string http___id.nlm.nih.gov_mesh_vocab#onlineNote  
    string rdfs_label  
}
HttpId.nlm.nih.govMeshVocab#SCRChemical {
    date http___id.nlm.nih.gov_mesh_vocab#dateCreated  
    string http___id.nlm.nih.gov_mesh_vocab#lastActiveYear  
    date http___id.nlm.nih.gov_mesh_vocab#dateRevised  
    string http___id.nlm.nih.gov_mesh_vocab#identifier  
    string http___id.nlm.nih.gov_mesh_vocab#source  
    int32 http___id.nlm.nih.gov_mesh_vocab#frequency  
    boolean http___id.nlm.nih.gov_mesh_vocab#active  
    string http___id.nlm.nih.gov_mesh_vocab#note  
    string http___id.nlm.nih.gov_mesh_vocab#previousIndexing  
    uri http___id.nlm.nih.gov_mesh_vocab#indexerConsiderAlso  
    string rdfs_label  
}
HttpId.nlm.nih.govMeshVocab#SCRDisease {
    date http___id.nlm.nih.gov_mesh_vocab#dateCreated  
    string http___id.nlm.nih.gov_mesh_vocab#lastActiveYear  
    date http___id.nlm.nih.gov_mesh_vocab#dateRevised  
    string http___id.nlm.nih.gov_mesh_vocab#identifier  
    string http___id.nlm.nih.gov_mesh_vocab#source  
    int32 http___id.nlm.nih.gov_mesh_vocab#frequency  
    boolean http___id.nlm.nih.gov_mesh_vocab#active  
    string http___id.nlm.nih.gov_mesh_vocab#note  
    uri http___id.nlm.nih.gov_mesh_vocab#indexerConsiderAlso  
    string http___id.nlm.nih.gov_mesh_vocab#previousIndexing  
    string rdfs_label  
}
HttpId.nlm.nih.govMeshVocab#SCROrganism {
    date http___id.nlm.nih.gov_mesh_vocab#dateCreated  
    string http___id.nlm.nih.gov_mesh_vocab#lastActiveYear  
    date http___id.nlm.nih.gov_mesh_vocab#dateRevised  
    string http___id.nlm.nih.gov_mesh_vocab#identifier  
    string http___id.nlm.nih.gov_mesh_vocab#source  
    int32 http___id.nlm.nih.gov_mesh_vocab#frequency  
    boolean http___id.nlm.nih.gov_mesh_vocab#active  
    string http___id.nlm.nih.gov_mesh_vocab#note  
    string http___id.nlm.nih.gov_mesh_vocab#previousIndexing  
    uri http___id.nlm.nih.gov_mesh_vocab#indexerConsiderAlso  
    string rdfs_label  
}
HttpId.nlm.nih.govMeshVocab#SCRPopulation {
    date http___id.nlm.nih.gov_mesh_vocab#dateCreated  
    date http___id.nlm.nih.gov_mesh_vocab#dateRevised  
    string http___id.nlm.nih.gov_mesh_vocab#identifier  
    int32 http___id.nlm.nih.gov_mesh_vocab#frequency  
    boolean http___id.nlm.nih.gov_mesh_vocab#active  
    string rdfs_label  
}
HttpId.nlm.nih.govMeshVocab#SCRProtocol {
    date http___id.nlm.nih.gov_mesh_vocab#dateCreated  
    string http___id.nlm.nih.gov_mesh_vocab#lastActiveYear  
    date http___id.nlm.nih.gov_mesh_vocab#dateRevised  
    string http___id.nlm.nih.gov_mesh_vocab#identifier  
    string http___id.nlm.nih.gov_mesh_vocab#source  
    int32 http___id.nlm.nih.gov_mesh_vocab#frequency  
    boolean http___id.nlm.nih.gov_mesh_vocab#active  
    string http___id.nlm.nih.gov_mesh_vocab#note  
    string http___id.nlm.nih.gov_mesh_vocab#previousIndexing  
    uri http___id.nlm.nih.gov_mesh_vocab#indexerConsiderAlso  
    string rdfs_label  
}
HttpId.nlm.nih.govMeshVocab#Term {
    string http___id.nlm.nih.gov_mesh_vocab#prefLabel  
    date http___id.nlm.nih.gov_mesh_vocab#dateCreated  
    string http___id.nlm.nih.gov_mesh_vocab#entryVersion  
    string http___id.nlm.nih.gov_mesh_vocab#lastActiveYear  
    string http___id.nlm.nih.gov_mesh_vocab#altLabel  
    string http___id.nlm.nih.gov_mesh_vocab#identifier  
    string http___id.nlm.nih.gov_mesh_vocab#thesaurusID  
    string http___id.nlm.nih.gov_mesh_vocab#sortVersion  
    boolean http___id.nlm.nih.gov_mesh_vocab#active  
    string http___id.nlm.nih.gov_mesh_vocab#abbreviation  
    string http___id.nlm.nih.gov_mesh_vocab#lexicalTag  
}
HttpId.nlm.nih.govMeshVocab#TopicalDescriptor {
    date http___id.nlm.nih.gov_mesh_vocab#dateCreated  
    string http___id.nlm.nih.gov_mesh_vocab#lastActiveYear  
    string http___id.nlm.nih.gov_mesh_vocab#annotation  
    string http___id.nlm.nih.gov_mesh_vocab#onlineNote  
    string http___id.nlm.nih.gov_mesh_vocab#identifier  
    string http___id.nlm.nih.gov_mesh_vocab#considerAlso  
    string rdfs_label  
    date http___id.nlm.nih.gov_mesh_vocab#dateRevised  
    string http___id.nlm.nih.gov_mesh_vocab#historyNote  
    string http___id.nlm.nih.gov_mesh_vocab#publicMeSHNote  
    string http___id.nlm.nih.gov_mesh_vocab#nlmClassificationNumber  
    boolean http___id.nlm.nih.gov_mesh_vocab#active  
    date http___id.nlm.nih.gov_mesh_vocab#dateEstablished  
    string http___id.nlm.nih.gov_mesh_vocab#previousIndexing  
}
HttpId.nlm.nih.govMeshVocab#TreeNumber {
    string http___id.nlm.nih.gov_mesh_vocab#lastActiveYear  
    string rdfs_label  
    boolean http___id.nlm.nih.gov_mesh_vocab#active  
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
HttpId.nlm.nih.govMeshVocab#AllowedDescriptorQualifierPair ||--|o HttpId.nlm.nih.govMeshVocab#Qualifier : "http___id.nlm.nih.gov_mesh_vocab#hasQualifier"
HttpId.nlm.nih.govMeshVocab#AllowedDescriptorQualifierPair ||--|o HttpId.nlm.nih.govMeshVocab#GeographicalDescriptor : "http___id.nlm.nih.gov_mesh_vocab#hasDescriptor"
HttpId.nlm.nih.govMeshVocab#AllowedDescriptorQualifierPair ||--|o HttpId.nlm.nih.govMeshVocab#TopicalDescriptor : "http___id.nlm.nih.gov_mesh_vocab#hasDescriptor"
HttpId.nlm.nih.govMeshVocab#AllowedDescriptorQualifierPair ||--|o RdfsLiteral : "rdfs_label"
HttpId.nlm.nih.govMeshVocab#CheckTag ||--|o HttpId.nlm.nih.govMeshVocab#Term : "http___id.nlm.nih.gov_mesh_vocab#preferredTerm"
HttpId.nlm.nih.govMeshVocab#CheckTag ||--|o HttpId.nlm.nih.govMeshVocab#Concept : "http___id.nlm.nih.gov_mesh_vocab#preferredConcept"
HttpId.nlm.nih.govMeshVocab#CheckTag ||--|o RdfsLiteral : "rdfs_label"
HttpId.nlm.nih.govMeshVocab#Concept ||--|o HttpId.nlm.nih.govMeshVocab#Term : "http___id.nlm.nih.gov_mesh_vocab#preferredTerm"
HttpId.nlm.nih.govMeshVocab#Concept ||--|o HttpId.nlm.nih.govMeshVocab#Concept : "http___id.nlm.nih.gov_mesh_vocab#narrowerConcept"
HttpId.nlm.nih.govMeshVocab#Concept ||--|o HttpId.nlm.nih.govMeshVocab#Concept : "http___id.nlm.nih.gov_mesh_vocab#relatedConcept"
HttpId.nlm.nih.govMeshVocab#Concept ||--|o HttpId.nlm.nih.govMeshVocab#Concept : "http___id.nlm.nih.gov_mesh_vocab#broaderConcept"
HttpId.nlm.nih.govMeshVocab#Concept ||--|o HttpId.nlm.nih.govMeshVocab#Term : "http___id.nlm.nih.gov_mesh_vocab#term"
HttpId.nlm.nih.govMeshVocab#Concept ||--|o RdfsLiteral : "rdfs_label"
HttpId.nlm.nih.govMeshVocab#DisallowedDescriptorQualifierPair ||--|o HttpId.nlm.nih.govMeshVocab#Qualifier : "http___id.nlm.nih.gov_mesh_vocab#hasQualifier"
HttpId.nlm.nih.govMeshVocab#DisallowedDescriptorQualifierPair ||--|o HttpId.nlm.nih.govMeshVocab#AllowedDescriptorQualifierPair : "http___id.nlm.nih.gov_mesh_vocab#useInstead"
HttpId.nlm.nih.govMeshVocab#DisallowedDescriptorQualifierPair ||--|o HttpId.nlm.nih.govMeshVocab#DisallowedDescriptorQualifierPair : "http___id.nlm.nih.gov_mesh_vocab#useInstead"
HttpId.nlm.nih.govMeshVocab#DisallowedDescriptorQualifierPair ||--|o HttpId.nlm.nih.govMeshVocab#TopicalDescriptor : "http___id.nlm.nih.gov_mesh_vocab#useInstead"
HttpId.nlm.nih.govMeshVocab#DisallowedDescriptorQualifierPair ||--|o HttpId.nlm.nih.govMeshVocab#GeographicalDescriptor : "http___id.nlm.nih.gov_mesh_vocab#hasDescriptor"
HttpId.nlm.nih.govMeshVocab#DisallowedDescriptorQualifierPair ||--|o HttpId.nlm.nih.govMeshVocab#TopicalDescriptor : "http___id.nlm.nih.gov_mesh_vocab#hasDescriptor"
HttpId.nlm.nih.govMeshVocab#DisallowedDescriptorQualifierPair ||--|o RdfsLiteral : "rdfs_label"
HttpId.nlm.nih.govMeshVocab#GeographicalDescriptor ||--|o HttpId.nlm.nih.govMeshVocab#Term : "http___id.nlm.nih.gov_mesh_vocab#preferredTerm"
HttpId.nlm.nih.govMeshVocab#GeographicalDescriptor ||--|o HttpId.nlm.nih.govMeshVocab#Qualifier : "http___id.nlm.nih.gov_mesh_vocab#allowableQualifier"
HttpId.nlm.nih.govMeshVocab#GeographicalDescriptor ||--|o HttpId.nlm.nih.govMeshVocab#Concept : "http___id.nlm.nih.gov_mesh_vocab#concept"
HttpId.nlm.nih.govMeshVocab#GeographicalDescriptor ||--|o HttpId.nlm.nih.govMeshVocab#PublicationType : "http___id.nlm.nih.gov_mesh_vocab#broaderDescriptor"
HttpId.nlm.nih.govMeshVocab#GeographicalDescriptor ||--|o HttpId.nlm.nih.govMeshVocab#GeographicalDescriptor : "http___id.nlm.nih.gov_mesh_vocab#broaderDescriptor"
HttpId.nlm.nih.govMeshVocab#GeographicalDescriptor ||--|o HttpId.nlm.nih.govMeshVocab#TopicalDescriptor : "http___id.nlm.nih.gov_mesh_vocab#broaderDescriptor"
HttpId.nlm.nih.govMeshVocab#GeographicalDescriptor ||--|o HttpId.nlm.nih.govMeshVocab#TreeNumber : "http___id.nlm.nih.gov_mesh_vocab#treeNumber"
HttpId.nlm.nih.govMeshVocab#GeographicalDescriptor ||--|o HttpId.nlm.nih.govMeshVocab#Concept : "http___id.nlm.nih.gov_mesh_vocab#preferredConcept"
HttpId.nlm.nih.govMeshVocab#GeographicalDescriptor ||--|o RdfsLiteral : "rdfs_label"
HttpId.nlm.nih.govMeshVocab#PublicationType ||--|o HttpId.nlm.nih.govMeshVocab#Term : "http___id.nlm.nih.gov_mesh_vocab#preferredTerm"
HttpId.nlm.nih.govMeshVocab#PublicationType ||--|o HttpId.nlm.nih.govMeshVocab#Concept : "http___id.nlm.nih.gov_mesh_vocab#concept"
HttpId.nlm.nih.govMeshVocab#PublicationType ||--|o HttpId.nlm.nih.govMeshVocab#PublicationType : "http___id.nlm.nih.gov_mesh_vocab#broaderDescriptor"
HttpId.nlm.nih.govMeshVocab#PublicationType ||--|o HttpId.nlm.nih.govMeshVocab#GeographicalDescriptor : "http___id.nlm.nih.gov_mesh_vocab#broaderDescriptor"
HttpId.nlm.nih.govMeshVocab#PublicationType ||--|o HttpId.nlm.nih.govMeshVocab#TopicalDescriptor : "http___id.nlm.nih.gov_mesh_vocab#broaderDescriptor"
HttpId.nlm.nih.govMeshVocab#PublicationType ||--|o HttpId.nlm.nih.govMeshVocab#TreeNumber : "http___id.nlm.nih.gov_mesh_vocab#treeNumber"
HttpId.nlm.nih.govMeshVocab#PublicationType ||--|o HttpId.nlm.nih.govMeshVocab#PublicationType : "http___id.nlm.nih.gov_mesh_vocab#seeAlso"
HttpId.nlm.nih.govMeshVocab#PublicationType ||--|o HttpId.nlm.nih.govMeshVocab#TopicalDescriptor : "http___id.nlm.nih.gov_mesh_vocab#seeAlso"
HttpId.nlm.nih.govMeshVocab#PublicationType ||--|o HttpId.nlm.nih.govMeshVocab#Concept : "http___id.nlm.nih.gov_mesh_vocab#preferredConcept"
HttpId.nlm.nih.govMeshVocab#PublicationType ||--|o RdfsLiteral : "rdfs_label"
HttpId.nlm.nih.govMeshVocab#Qualifier ||--|o HttpId.nlm.nih.govMeshVocab#Term : "http___id.nlm.nih.gov_mesh_vocab#preferredTerm"
HttpId.nlm.nih.govMeshVocab#Qualifier ||--|o HttpId.nlm.nih.govMeshVocab#Concept : "http___id.nlm.nih.gov_mesh_vocab#concept"
HttpId.nlm.nih.govMeshVocab#Qualifier ||--|o HttpId.nlm.nih.govMeshVocab#Qualifier : "http___id.nlm.nih.gov_mesh_vocab#broaderQualifier"
HttpId.nlm.nih.govMeshVocab#Qualifier ||--|o HttpId.nlm.nih.govMeshVocab#TreeNumber : "http___id.nlm.nih.gov_mesh_vocab#treeNumber"
HttpId.nlm.nih.govMeshVocab#Qualifier ||--|o HttpId.nlm.nih.govMeshVocab#Concept : "http___id.nlm.nih.gov_mesh_vocab#preferredConcept"
HttpId.nlm.nih.govMeshVocab#Qualifier ||--|o RdfsLiteral : "rdfs_label"
HttpId.nlm.nih.govMeshVocab#SCRChemical ||--|o HttpId.nlm.nih.govMeshVocab#Term : "http___id.nlm.nih.gov_mesh_vocab#preferredTerm"
HttpId.nlm.nih.govMeshVocab#SCRChemical ||--|o HttpId.nlm.nih.govMeshVocab#Concept : "http___id.nlm.nih.gov_mesh_vocab#concept"
HttpId.nlm.nih.govMeshVocab#SCRChemical ||--|o HttpId.nlm.nih.govMeshVocab#AllowedDescriptorQualifierPair : "http___id.nlm.nih.gov_mesh_vocab#mappedTo"
HttpId.nlm.nih.govMeshVocab#SCRChemical ||--|o HttpId.nlm.nih.govMeshVocab#TopicalDescriptor : "http___id.nlm.nih.gov_mesh_vocab#mappedTo"
HttpId.nlm.nih.govMeshVocab#SCRChemical ||--|o HttpId.nlm.nih.govMeshVocab#TopicalDescriptor : "http___id.nlm.nih.gov_mesh_vocab#pharmacologicalAction"
HttpId.nlm.nih.govMeshVocab#SCRChemical ||--|o HttpId.nlm.nih.govMeshVocab#AllowedDescriptorQualifierPair : "http___id.nlm.nih.gov_mesh_vocab#preferredMappedTo"
HttpId.nlm.nih.govMeshVocab#SCRChemical ||--|o HttpId.nlm.nih.govMeshVocab#DisallowedDescriptorQualifierPair : "http___id.nlm.nih.gov_mesh_vocab#preferredMappedTo"
HttpId.nlm.nih.govMeshVocab#SCRChemical ||--|o HttpId.nlm.nih.govMeshVocab#TopicalDescriptor : "http___id.nlm.nih.gov_mesh_vocab#preferredMappedTo"
HttpId.nlm.nih.govMeshVocab#SCRChemical ||--|o HttpId.nlm.nih.govMeshVocab#AllowedDescriptorQualifierPair : "http___id.nlm.nih.gov_mesh_vocab#indexerConsiderAlso"
HttpId.nlm.nih.govMeshVocab#SCRChemical ||--|o HttpId.nlm.nih.govMeshVocab#DisallowedDescriptorQualifierPair : "http___id.nlm.nih.gov_mesh_vocab#indexerConsiderAlso"
HttpId.nlm.nih.govMeshVocab#SCRChemical ||--|o HttpId.nlm.nih.govMeshVocab#TopicalDescriptor : "http___id.nlm.nih.gov_mesh_vocab#indexerConsiderAlso"
HttpId.nlm.nih.govMeshVocab#SCRChemical ||--|o HttpId.nlm.nih.govMeshVocab#Concept : "http___id.nlm.nih.gov_mesh_vocab#preferredConcept"
HttpId.nlm.nih.govMeshVocab#SCRChemical ||--|o RdfsLiteral : "rdfs_label"
HttpId.nlm.nih.govMeshVocab#SCRDisease ||--|o HttpId.nlm.nih.govMeshVocab#Term : "http___id.nlm.nih.gov_mesh_vocab#preferredTerm"
HttpId.nlm.nih.govMeshVocab#SCRDisease ||--|o HttpId.nlm.nih.govMeshVocab#Concept : "http___id.nlm.nih.gov_mesh_vocab#concept"
HttpId.nlm.nih.govMeshVocab#SCRDisease ||--|o HttpId.nlm.nih.govMeshVocab#AllowedDescriptorQualifierPair : "http___id.nlm.nih.gov_mesh_vocab#mappedTo"
HttpId.nlm.nih.govMeshVocab#SCRDisease ||--|o HttpId.nlm.nih.govMeshVocab#TopicalDescriptor : "http___id.nlm.nih.gov_mesh_vocab#mappedTo"
HttpId.nlm.nih.govMeshVocab#SCRDisease ||--|o HttpId.nlm.nih.govMeshVocab#AllowedDescriptorQualifierPair : "http___id.nlm.nih.gov_mesh_vocab#preferredMappedTo"
HttpId.nlm.nih.govMeshVocab#SCRDisease ||--|o HttpId.nlm.nih.govMeshVocab#DisallowedDescriptorQualifierPair : "http___id.nlm.nih.gov_mesh_vocab#preferredMappedTo"
HttpId.nlm.nih.govMeshVocab#SCRDisease ||--|o HttpId.nlm.nih.govMeshVocab#TopicalDescriptor : "http___id.nlm.nih.gov_mesh_vocab#preferredMappedTo"
HttpId.nlm.nih.govMeshVocab#SCRDisease ||--|o HttpId.nlm.nih.govMeshVocab#AllowedDescriptorQualifierPair : "http___id.nlm.nih.gov_mesh_vocab#indexerConsiderAlso"
HttpId.nlm.nih.govMeshVocab#SCRDisease ||--|o HttpId.nlm.nih.govMeshVocab#DisallowedDescriptorQualifierPair : "http___id.nlm.nih.gov_mesh_vocab#indexerConsiderAlso"
HttpId.nlm.nih.govMeshVocab#SCRDisease ||--|o HttpId.nlm.nih.govMeshVocab#TopicalDescriptor : "http___id.nlm.nih.gov_mesh_vocab#indexerConsiderAlso"
HttpId.nlm.nih.govMeshVocab#SCRDisease ||--|o HttpId.nlm.nih.govMeshVocab#Concept : "http___id.nlm.nih.gov_mesh_vocab#preferredConcept"
HttpId.nlm.nih.govMeshVocab#SCRDisease ||--|o RdfsLiteral : "rdfs_label"
HttpId.nlm.nih.govMeshVocab#SCROrganism ||--|o HttpId.nlm.nih.govMeshVocab#Concept : "http___id.nlm.nih.gov_mesh_vocab#preferredConcept"
HttpId.nlm.nih.govMeshVocab#SCROrganism ||--|o HttpId.nlm.nih.govMeshVocab#Term : "http___id.nlm.nih.gov_mesh_vocab#preferredTerm"
HttpId.nlm.nih.govMeshVocab#SCROrganism ||--|o HttpId.nlm.nih.govMeshVocab#Concept : "http___id.nlm.nih.gov_mesh_vocab#concept"
HttpId.nlm.nih.govMeshVocab#SCROrganism ||--|o HttpId.nlm.nih.govMeshVocab#AllowedDescriptorQualifierPair : "http___id.nlm.nih.gov_mesh_vocab#mappedTo"
HttpId.nlm.nih.govMeshVocab#SCROrganism ||--|o HttpId.nlm.nih.govMeshVocab#TopicalDescriptor : "http___id.nlm.nih.gov_mesh_vocab#mappedTo"
HttpId.nlm.nih.govMeshVocab#SCROrganism ||--|o HttpId.nlm.nih.govMeshVocab#AllowedDescriptorQualifierPair : "http___id.nlm.nih.gov_mesh_vocab#preferredMappedTo"
HttpId.nlm.nih.govMeshVocab#SCROrganism ||--|o HttpId.nlm.nih.govMeshVocab#DisallowedDescriptorQualifierPair : "http___id.nlm.nih.gov_mesh_vocab#preferredMappedTo"
HttpId.nlm.nih.govMeshVocab#SCROrganism ||--|o HttpId.nlm.nih.govMeshVocab#TopicalDescriptor : "http___id.nlm.nih.gov_mesh_vocab#preferredMappedTo"
HttpId.nlm.nih.govMeshVocab#SCROrganism ||--|o HttpId.nlm.nih.govMeshVocab#AllowedDescriptorQualifierPair : "http___id.nlm.nih.gov_mesh_vocab#indexerConsiderAlso"
HttpId.nlm.nih.govMeshVocab#SCROrganism ||--|o HttpId.nlm.nih.govMeshVocab#DisallowedDescriptorQualifierPair : "http___id.nlm.nih.gov_mesh_vocab#indexerConsiderAlso"
HttpId.nlm.nih.govMeshVocab#SCROrganism ||--|o HttpId.nlm.nih.govMeshVocab#TopicalDescriptor : "http___id.nlm.nih.gov_mesh_vocab#indexerConsiderAlso"
HttpId.nlm.nih.govMeshVocab#SCROrganism ||--|o RdfsLiteral : "rdfs_label"
HttpId.nlm.nih.govMeshVocab#SCRPopulation ||--|o HttpId.nlm.nih.govMeshVocab#Term : "http___id.nlm.nih.gov_mesh_vocab#preferredTerm"
HttpId.nlm.nih.govMeshVocab#SCRPopulation ||--|o HttpId.nlm.nih.govMeshVocab#Concept : "http___id.nlm.nih.gov_mesh_vocab#concept"
HttpId.nlm.nih.govMeshVocab#SCRPopulation ||--|o HttpId.nlm.nih.govMeshVocab#AllowedDescriptorQualifierPair : "http___id.nlm.nih.gov_mesh_vocab#mappedTo"
HttpId.nlm.nih.govMeshVocab#SCRPopulation ||--|o HttpId.nlm.nih.govMeshVocab#TopicalDescriptor : "http___id.nlm.nih.gov_mesh_vocab#mappedTo"
HttpId.nlm.nih.govMeshVocab#SCRPopulation ||--|o HttpId.nlm.nih.govMeshVocab#AllowedDescriptorQualifierPair : "http___id.nlm.nih.gov_mesh_vocab#preferredMappedTo"
HttpId.nlm.nih.govMeshVocab#SCRPopulation ||--|o HttpId.nlm.nih.govMeshVocab#DisallowedDescriptorQualifierPair : "http___id.nlm.nih.gov_mesh_vocab#preferredMappedTo"
HttpId.nlm.nih.govMeshVocab#SCRPopulation ||--|o HttpId.nlm.nih.govMeshVocab#TopicalDescriptor : "http___id.nlm.nih.gov_mesh_vocab#preferredMappedTo"
HttpId.nlm.nih.govMeshVocab#SCRPopulation ||--|o HttpId.nlm.nih.govMeshVocab#Concept : "http___id.nlm.nih.gov_mesh_vocab#preferredConcept"
HttpId.nlm.nih.govMeshVocab#SCRPopulation ||--|o RdfsLiteral : "rdfs_label"
HttpId.nlm.nih.govMeshVocab#SCRProtocol ||--|o HttpId.nlm.nih.govMeshVocab#Concept : "http___id.nlm.nih.gov_mesh_vocab#preferredConcept"
HttpId.nlm.nih.govMeshVocab#SCRProtocol ||--|o HttpId.nlm.nih.govMeshVocab#Term : "http___id.nlm.nih.gov_mesh_vocab#preferredTerm"
HttpId.nlm.nih.govMeshVocab#SCRProtocol ||--|o HttpId.nlm.nih.govMeshVocab#Concept : "http___id.nlm.nih.gov_mesh_vocab#concept"
HttpId.nlm.nih.govMeshVocab#SCRProtocol ||--|o HttpId.nlm.nih.govMeshVocab#AllowedDescriptorQualifierPair : "http___id.nlm.nih.gov_mesh_vocab#mappedTo"
HttpId.nlm.nih.govMeshVocab#SCRProtocol ||--|o HttpId.nlm.nih.govMeshVocab#TopicalDescriptor : "http___id.nlm.nih.gov_mesh_vocab#mappedTo"
HttpId.nlm.nih.govMeshVocab#SCRProtocol ||--|o HttpId.nlm.nih.govMeshVocab#TopicalDescriptor : "http___id.nlm.nih.gov_mesh_vocab#pharmacologicalAction"
HttpId.nlm.nih.govMeshVocab#SCRProtocol ||--|o HttpId.nlm.nih.govMeshVocab#AllowedDescriptorQualifierPair : "http___id.nlm.nih.gov_mesh_vocab#preferredMappedTo"
HttpId.nlm.nih.govMeshVocab#SCRProtocol ||--|o HttpId.nlm.nih.govMeshVocab#DisallowedDescriptorQualifierPair : "http___id.nlm.nih.gov_mesh_vocab#preferredMappedTo"
HttpId.nlm.nih.govMeshVocab#SCRProtocol ||--|o HttpId.nlm.nih.govMeshVocab#TopicalDescriptor : "http___id.nlm.nih.gov_mesh_vocab#preferredMappedTo"
HttpId.nlm.nih.govMeshVocab#SCRProtocol ||--|o HttpId.nlm.nih.govMeshVocab#AllowedDescriptorQualifierPair : "http___id.nlm.nih.gov_mesh_vocab#indexerConsiderAlso"
HttpId.nlm.nih.govMeshVocab#SCRProtocol ||--|o HttpId.nlm.nih.govMeshVocab#DisallowedDescriptorQualifierPair : "http___id.nlm.nih.gov_mesh_vocab#indexerConsiderAlso"
HttpId.nlm.nih.govMeshVocab#SCRProtocol ||--|o HttpId.nlm.nih.govMeshVocab#TopicalDescriptor : "http___id.nlm.nih.gov_mesh_vocab#indexerConsiderAlso"
HttpId.nlm.nih.govMeshVocab#SCRProtocol ||--|o RdfsLiteral : "rdfs_label"
HttpId.nlm.nih.govMeshVocab#TopicalDescriptor ||--|o HttpId.nlm.nih.govMeshVocab#PublicationType : "http___id.nlm.nih.gov_mesh_vocab#seeAlso"
HttpId.nlm.nih.govMeshVocab#TopicalDescriptor ||--|o HttpId.nlm.nih.govMeshVocab#TopicalDescriptor : "http___id.nlm.nih.gov_mesh_vocab#seeAlso"
HttpId.nlm.nih.govMeshVocab#TopicalDescriptor ||--|o HttpId.nlm.nih.govMeshVocab#TopicalDescriptor : "http___id.nlm.nih.gov_mesh_vocab#pharmacologicalAction"
HttpId.nlm.nih.govMeshVocab#TopicalDescriptor ||--|o HttpId.nlm.nih.govMeshVocab#PublicationType : "http___id.nlm.nih.gov_mesh_vocab#broaderDescriptor"
HttpId.nlm.nih.govMeshVocab#TopicalDescriptor ||--|o HttpId.nlm.nih.govMeshVocab#GeographicalDescriptor : "http___id.nlm.nih.gov_mesh_vocab#broaderDescriptor"
HttpId.nlm.nih.govMeshVocab#TopicalDescriptor ||--|o HttpId.nlm.nih.govMeshVocab#TopicalDescriptor : "http___id.nlm.nih.gov_mesh_vocab#broaderDescriptor"
HttpId.nlm.nih.govMeshVocab#TopicalDescriptor ||--|o HttpId.nlm.nih.govMeshVocab#Concept : "http___id.nlm.nih.gov_mesh_vocab#preferredConcept"
HttpId.nlm.nih.govMeshVocab#TopicalDescriptor ||--|o RdfsLiteral : "rdfs_label"
HttpId.nlm.nih.govMeshVocab#TopicalDescriptor ||--|o HttpId.nlm.nih.govMeshVocab#Qualifier : "http___id.nlm.nih.gov_mesh_vocab#allowableQualifier"
HttpId.nlm.nih.govMeshVocab#TopicalDescriptor ||--|o HttpId.nlm.nih.govMeshVocab#Concept : "http___id.nlm.nih.gov_mesh_vocab#concept"
HttpId.nlm.nih.govMeshVocab#TopicalDescriptor ||--|o HttpId.nlm.nih.govMeshVocab#Term : "http___id.nlm.nih.gov_mesh_vocab#preferredTerm"
HttpId.nlm.nih.govMeshVocab#TopicalDescriptor ||--|o HttpId.nlm.nih.govMeshVocab#TreeNumber : "http___id.nlm.nih.gov_mesh_vocab#treeNumber"
HttpId.nlm.nih.govMeshVocab#TreeNumber ||--|o HttpId.nlm.nih.govMeshVocab#TreeNumber : "http___id.nlm.nih.gov_mesh_vocab#parentTreeNumber"
HttpId.nlm.nih.govMeshVocab#TreeNumber ||--|o RdfsLiteral : "rdfs_label"

```



## Imports


* okns:owl-rdf-rdfs
* okns:extended_types
* linkml:types



## Classes

| Class | Description | Occurrences |
| --- | --- | --- |
| [HttpId.nlm.nih.govMeshVocab#AllowedDescriptorQualifierPair](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/classes/HttpId.nlm.nih.govMeshVocab#AllowedDescriptorQualifierPair.md) | None<br/>| 673877 | 
| [HttpId.nlm.nih.govMeshVocab#CheckTag](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/classes/HttpId.nlm.nih.govMeshVocab#CheckTag.md) | None<br/>| 2 | 
| [HttpId.nlm.nih.govMeshVocab#Concept](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/classes/HttpId.nlm.nih.govMeshVocab#Concept.md) | None<br/>| 464362 | 
| [HttpId.nlm.nih.govMeshVocab#DisallowedDescriptorQualifierPair](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/classes/HttpId.nlm.nih.govMeshVocab#DisallowedDescriptorQualifierPair.md) | None<br/>| 1032 | 
| [HttpId.nlm.nih.govMeshVocab#GeographicalDescriptor](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/classes/HttpId.nlm.nih.govMeshVocab#GeographicalDescriptor.md) | None<br/>| 400 | 
| [HttpId.nlm.nih.govMeshVocab#PublicationType](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/classes/HttpId.nlm.nih.govMeshVocab#PublicationType.md) | None<br/>| 187 | 
| [HttpId.nlm.nih.govMeshVocab#Qualifier](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/classes/HttpId.nlm.nih.govMeshVocab#Qualifier.md) | None<br/>| 84 | 
| [HttpId.nlm.nih.govMeshVocab#SCRChemical](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/classes/HttpId.nlm.nih.govMeshVocab#SCRChemical.md) | None<br/>| 249243 | 
| [HttpId.nlm.nih.govMeshVocab#SCRDisease](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/classes/HttpId.nlm.nih.govMeshVocab#SCRDisease.md) | None<br/>| 6750 | 
| [HttpId.nlm.nih.govMeshVocab#SCROrganism](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/classes/HttpId.nlm.nih.govMeshVocab#SCROrganism.md) | None<br/>| 66110 | 
| [HttpId.nlm.nih.govMeshVocab#SCRPopulation](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/classes/HttpId.nlm.nih.govMeshVocab#SCRPopulation.md) | None<br/>| 1764 | 
| [HttpId.nlm.nih.govMeshVocab#SCRProtocol](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/classes/HttpId.nlm.nih.govMeshVocab#SCRProtocol.md) | None<br/>| 1219 | 
| [HttpId.nlm.nih.govMeshVocab#Term](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/classes/HttpId.nlm.nih.govMeshVocab#Term.md) | None<br/>| 862579 | 
| [HttpId.nlm.nih.govMeshVocab#TopicalDescriptor](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/classes/HttpId.nlm.nih.govMeshVocab#TopicalDescriptor.md) | None<br/>| 29940 | 
| [HttpId.nlm.nih.govMeshVocab#TreeNumber](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/classes/HttpId.nlm.nih.govMeshVocab#TreeNumber.md) | None<br/>| 80096 | 





## Slots

| Slot | Description | Occurrences |
| --- | --- | --- |
| [http___id.nlm.nih.gov_mesh_vocab#abbreviation](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/slots/http___id.nlm.nih.gov_mesh_vocab#abbreviation.md) | <br/>| 81 |
| [http___id.nlm.nih.gov_mesh_vocab#active](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/slots/http___id.nlm.nih.gov_mesh_vocab#active.md) | <br/>| 2437645 |
| [http___id.nlm.nih.gov_mesh_vocab#allowableQualifier](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/slots/http___id.nlm.nih.gov_mesh_vocab#allowableQualifier.md) | <br/>| 622079 |
| [http___id.nlm.nih.gov_mesh_vocab#altLabel](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/slots/http___id.nlm.nih.gov_mesh_vocab#altLabel.md) | <br/>| 131103 |
| [http___id.nlm.nih.gov_mesh_vocab#annotation](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/slots/http___id.nlm.nih.gov_mesh_vocab#annotation.md) | <br/>| 12664 |
| [http___id.nlm.nih.gov_mesh_vocab#broaderConcept](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/slots/http___id.nlm.nih.gov_mesh_vocab#broaderConcept.md) | <br/>| 8850 |
| [http___id.nlm.nih.gov_mesh_vocab#broaderDescriptor](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/slots/http___id.nlm.nih.gov_mesh_vocab#broaderDescriptor.md) | <br/>| 41579 |
| [http___id.nlm.nih.gov_mesh_vocab#broaderQualifier](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/slots/http___id.nlm.nih.gov_mesh_vocab#broaderQualifier.md) | <br/>| 76 |
| [http___id.nlm.nih.gov_mesh_vocab#casn1_label](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/slots/http___id.nlm.nih.gov_mesh_vocab#casn1_label.md) | <br/>| 22720 |
| [http___id.nlm.nih.gov_mesh_vocab#concept](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/slots/http___id.nlm.nih.gov_mesh_vocab#concept.md) | <br/>| 110377 |
| [http___id.nlm.nih.gov_mesh_vocab#considerAlso](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/slots/http___id.nlm.nih.gov_mesh_vocab#considerAlso.md) | <br/>| 66 |
| [http___id.nlm.nih.gov_mesh_vocab#dateCreated](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/slots/http___id.nlm.nih.gov_mesh_vocab#dateCreated.md) | <br/>| 987872 |
| [http___id.nlm.nih.gov_mesh_vocab#dateEstablished](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/slots/http___id.nlm.nih.gov_mesh_vocab#dateEstablished.md) | <br/>| 30613 |
| [http___id.nlm.nih.gov_mesh_vocab#dateRevised](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/slots/http___id.nlm.nih.gov_mesh_vocab#dateRevised.md) | <br/>| 282462 |
| [http___id.nlm.nih.gov_mesh_vocab#entryVersion](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/slots/http___id.nlm.nih.gov_mesh_vocab#entryVersion.md) | <br/>| 16274 |
| [http___id.nlm.nih.gov_mesh_vocab#frequency](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/slots/http___id.nlm.nih.gov_mesh_vocab#frequency.md) | <br/>| 324911 |
| [http___id.nlm.nih.gov_mesh_vocab#hasDescriptor](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/slots/http___id.nlm.nih.gov_mesh_vocab#hasDescriptor.md) | <br/>| 674909 |
| [http___id.nlm.nih.gov_mesh_vocab#hasQualifier](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/slots/http___id.nlm.nih.gov_mesh_vocab#hasQualifier.md) | <br/>| 674909 |
| [http___id.nlm.nih.gov_mesh_vocab#historyNote](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/slots/http___id.nlm.nih.gov_mesh_vocab#historyNote.md) | <br/>| 26600 |
| [http___id.nlm.nih.gov_mesh_vocab#identifier](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/slots/http___id.nlm.nih.gov_mesh_vocab#identifier.md) | <br/>| 1682640 |
| [http___id.nlm.nih.gov_mesh_vocab#indexerConsiderAlso](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/slots/http___id.nlm.nih.gov_mesh_vocab#indexerConsiderAlso.md) | <br/>| 47181 |
| [http___id.nlm.nih.gov_mesh_vocab#lastActiveYear](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/slots/http___id.nlm.nih.gov_mesh_vocab#lastActiveYear.md) | <br/>| 89846 |
| [http___id.nlm.nih.gov_mesh_vocab#lexicalTag](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/slots/http___id.nlm.nih.gov_mesh_vocab#lexicalTag.md) | <br/>| 862579 |
| [http___id.nlm.nih.gov_mesh_vocab#mappedTo](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/slots/http___id.nlm.nih.gov_mesh_vocab#mappedTo.md) | <br/>| 11275 |
| [http___id.nlm.nih.gov_mesh_vocab#narrowerConcept](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/slots/http___id.nlm.nih.gov_mesh_vocab#narrowerConcept.md) | <br/>| 91735 |
| [http___id.nlm.nih.gov_mesh_vocab#nlmClassificationNumber](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/slots/http___id.nlm.nih.gov_mesh_vocab#nlmClassificationNumber.md) | <br/>| 6259 |
| [http___id.nlm.nih.gov_mesh_vocab#note](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/slots/http___id.nlm.nih.gov_mesh_vocab#note.md) | <br/>| 217700 |
| [http___id.nlm.nih.gov_mesh_vocab#onlineNote](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/slots/http___id.nlm.nih.gov_mesh_vocab#onlineNote.md) | <br/>| 3051 |
| [http___id.nlm.nih.gov_mesh_vocab#parentTreeNumber](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/slots/http___id.nlm.nih.gov_mesh_vocab#parentTreeNumber.md) | <br/>| 79955 |
| [http___id.nlm.nih.gov_mesh_vocab#pharmacologicalAction](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/slots/http___id.nlm.nih.gov_mesh_vocab#pharmacologicalAction.md) | <br/>| 15655 |
| [http___id.nlm.nih.gov_mesh_vocab#preferredConcept](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/slots/http___id.nlm.nih.gov_mesh_vocab#preferredConcept.md) | <br/>| 355699 |
| [http___id.nlm.nih.gov_mesh_vocab#preferredMappedTo](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/slots/http___id.nlm.nih.gov_mesh_vocab#preferredMappedTo.md) | <br/>| 426098 |
| [http___id.nlm.nih.gov_mesh_vocab#preferredTerm](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/slots/http___id.nlm.nih.gov_mesh_vocab#preferredTerm.md) | <br/>| 820061 |
| [http___id.nlm.nih.gov_mesh_vocab#prefLabel](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/slots/http___id.nlm.nih.gov_mesh_vocab#prefLabel.md) | <br/>| 862579 |
| [http___id.nlm.nih.gov_mesh_vocab#previousIndexing](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/slots/http___id.nlm.nih.gov_mesh_vocab#previousIndexing.md) | <br/>| 83061 |
| [http___id.nlm.nih.gov_mesh_vocab#publicMeSHNote](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/slots/http___id.nlm.nih.gov_mesh_vocab#publicMeSHNote.md) | <br/>| 26077 |
| [http___id.nlm.nih.gov_mesh_vocab#registryNumber](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/slots/http___id.nlm.nih.gov_mesh_vocab#registryNumber.md) | <br/>| 385145 |
| [http___id.nlm.nih.gov_mesh_vocab#relatedConcept](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/slots/http___id.nlm.nih.gov_mesh_vocab#relatedConcept.md) | <br/>| 8072 |
| [http___id.nlm.nih.gov_mesh_vocab#relatedRegistryNumber](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/slots/http___id.nlm.nih.gov_mesh_vocab#relatedRegistryNumber.md) | <br/>| 43667 |
| [http___id.nlm.nih.gov_mesh_vocab#scopeNote](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/slots/http___id.nlm.nih.gov_mesh_vocab#scopeNote.md) | <br/>| 32789 |
| [http___id.nlm.nih.gov_mesh_vocab#seeAlso](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/slots/http___id.nlm.nih.gov_mesh_vocab#seeAlso.md) | <br/>| 9122 |
| [http___id.nlm.nih.gov_mesh_vocab#sortVersion](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/slots/http___id.nlm.nih.gov_mesh_vocab#sortVersion.md) | <br/>| 3973 |
| [http___id.nlm.nih.gov_mesh_vocab#source](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/slots/http___id.nlm.nih.gov_mesh_vocab#source.md) | <br/>| 254652 |
| [http___id.nlm.nih.gov_mesh_vocab#term](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/slots/http___id.nlm.nih.gov_mesh_vocab#term.md) | <br/>| 392785 |
| [http___id.nlm.nih.gov_mesh_vocab#thesaurusID](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/slots/http___id.nlm.nih.gov_mesh_vocab#thesaurusID.md) | <br/>| 909053 |
| [http___id.nlm.nih.gov_mesh_vocab#treeNumber](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/slots/http___id.nlm.nih.gov_mesh_vocab#treeNumber.md) | <br/>| 63258 |
| [http___id.nlm.nih.gov_mesh_vocab#useInstead](https://github.com/frink-okn/graph-descriptions/blob/main/biobricks-mesh-kg/slots/http___id.nlm.nih.gov_mesh_vocab#useInstead.md) | <br/>| 1032 |









## IRI prefixes

* linkml: https://w3id.org/linkml/
* okn: https://purl.org/okn/
* okns: https://purl.org/okn/schema/
* rdfs: http://www.w3.org/2000/01/rdf-schema#
* xsd: http://www.w3.org/2001/XMLSchema#
* shex: http://www.w3.org/ns/shex#
* schema: http://schema.org/
