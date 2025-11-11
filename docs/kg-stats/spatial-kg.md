# No schema name specified

No schema description specified



## Schema Diagram

```mermaid
erDiagram
GeoGeometry {
    string rdfs_label  
    uri rdfs_label  
    uri owl_sameAs  
}
KwgoAdministrativeRegion1 {
    uri owl_sameAs  
    string rdfs_label  
    uri rdfs_label  
    string kwgo_hasFIPS  
}
KwgoAdministrativeRegion2 {
    uri owl_sameAs  
    string rdfs_label  
    uri rdfs_label  
    string kwgo_hasFIPS  
}
KwgoAdministrativeRegion3 {
    uri owl_sameAs  
    string rdfs_label  
    uri rdfs_label  
    string kwgo_hasFIPS  
}
KwgoS2CellLevel13 {
    integer kwgo_cellID  
    float geo_hasMetricArea  
    uri owl_sameAs  
    string rdfs_label  
    uri rdfs_label  
}
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
    string kwgo_hasFIPS  
    integer kwgo_cellID  
    float geo_hasMetricArea  
    uri owl_sameAs  
    uri rdfs_domain  
    string rdfs_label  
    uri rdfs_label  
    uri rdfs_range  
}
OwlNegativePropertyAssertion {

}
OwlNothing {
    string kwgo_hasFIPS  
    integer kwgo_cellID  
    float geo_hasMetricArea  
    uri owl_sameAs  
    uri rdfs_domain  
    string rdfs_label  
    uri rdfs_label  
    uri rdfs_range  
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
    string kwgo_hasFIPS  
    integer kwgo_cellID  
    float geo_hasMetricArea  
    uri owl_sameAs  
    uri rdfs_domain  
    string rdfs_label  
    uri rdfs_label  
    uri rdfs_range  
}
OwlTransitiveProperty {

}
OwlRational {

}
OwlReal {

}
RdfAlt {

}
RdfBag {

}
RdfList {
    uri owl_sameAs  
}
RdfObjectProperty {
    uri owl_sameAs  
    uri rdfs_range  
    uri rdfs_domain  
}
RdfPlainLiteral {

}
RdfProperty {

}
RdfSeq {

}
RdfStatement {

}
RdfXMLLiteral {

}
RdfsClass {

}
RdfsContainer {

}
RdfsContainerMembershipProperty {

}
RdfsDatatype {

}
RdfsLiteral {

}
RdfsResource {

}
SfPolygon {
    string rdfs_label  
    uri rdfs_label  
    uri owl_sameAs  
}
XsdNCName {

}
XsdNMTOKEN {

}
XsdName {

}
XsdAnyURI {

}
XsdBase64Binary {

}
XsdBoolean {

}
XsdByte {

}
XsdDateTime {

}
XsdDateTimeStamp {

}
XsdDecimal {

}
XsdDouble {

}
XsdFloat {

}
XsdHexBinary {

}
XsdInt {

}
XsdInteger {

}
XsdLanguage {

}
XsdLong {

}
XsdNegativeInteger {

}
XsdNonNegativeInteger {

}
XsdNonPositiveInteger {

}
XsdNormalizedString {

}
XsdPositiveInteger {

}
XsdShort {

}
XsdString {

}
XsdToken {

}
XsdUnsignedByte {

}
XsdUnsignedInt {

}
XsdUnsignedLong {

}
XsdUnsignedShort {

}
GeoWktLiteral {

}

GeoGeometry ||--|o GeoWktLiteral : "geo_asWKT"
GeoGeometry ||--|o GeoGeometry : "owl_sameAs"
GeoGeometry ||--|o RdfObjectProperty : "owl_sameAs"
GeoGeometry ||--|o RdfList : "owl_sameAs"
GeoGeometry ||--|o KwgoAdministrativeRegion1 : "owl_sameAs"
GeoGeometry ||--|o OwlThing : "owl_sameAs"
GeoGeometry ||--|o SfPolygon : "owl_sameAs"
GeoGeometry ||--|o KwgoAdministrativeRegion3 : "owl_sameAs"
GeoGeometry ||--|o KwgoAdministrativeRegion2 : "owl_sameAs"
GeoGeometry ||--|o KwgoS2CellLevel13 : "owl_sameAs"
KwgoAdministrativeRegion1 ||--|o OwlThing : "kwgo_administrativePartOf"
KwgoAdministrativeRegion1 ||--|o KwgoAdministrativeRegion2 : "kwgo_administrativePartOf"
KwgoAdministrativeRegion1 ||--|o KwgoAdministrativeRegion1 : "kwgo_administrativePartOf"
KwgoAdministrativeRegion1 ||--|o OwlThing : "kwgo_sfOverlaps"
KwgoAdministrativeRegion1 ||--|o KwgoAdministrativeRegion1 : "kwgo_sfOverlaps"
KwgoAdministrativeRegion1 ||--|o KwgoAdministrativeRegion3 : "kwgo_sfOverlaps"
KwgoAdministrativeRegion1 ||--|o KwgoS2CellLevel13 : "kwgo_sfOverlaps"
KwgoAdministrativeRegion1 ||--|o KwgoAdministrativeRegion2 : "kwgo_sfOverlaps"
KwgoAdministrativeRegion1 ||--|o OwlThing : "kwgo_sfContains"
KwgoAdministrativeRegion1 ||--|o KwgoS2CellLevel13 : "kwgo_sfContains"
KwgoAdministrativeRegion1 ||--|o GeoGeometry : "owl_sameAs"
KwgoAdministrativeRegion1 ||--|o RdfObjectProperty : "owl_sameAs"
KwgoAdministrativeRegion1 ||--|o RdfList : "owl_sameAs"
KwgoAdministrativeRegion1 ||--|o KwgoAdministrativeRegion1 : "owl_sameAs"
KwgoAdministrativeRegion1 ||--|o OwlThing : "owl_sameAs"
KwgoAdministrativeRegion1 ||--|o SfPolygon : "owl_sameAs"
KwgoAdministrativeRegion1 ||--|o KwgoAdministrativeRegion3 : "owl_sameAs"
KwgoAdministrativeRegion1 ||--|o KwgoAdministrativeRegion2 : "owl_sameAs"
KwgoAdministrativeRegion1 ||--|o KwgoS2CellLevel13 : "owl_sameAs"
KwgoAdministrativeRegion1 ||--|o SfPolygon : "geo_hasGeometry"
KwgoAdministrativeRegion1 ||--|o GeoGeometry : "geo_hasGeometry"
KwgoAdministrativeRegion1 ||--|o OwlThing : "geo_hasGeometry"
KwgoAdministrativeRegion1 ||--|o SfPolygon : "geo_hasDefaultGeometry"
KwgoAdministrativeRegion1 ||--|o GeoGeometry : "geo_hasDefaultGeometry"
KwgoAdministrativeRegion1 ||--|o OwlThing : "geo_hasDefaultGeometry"
KwgoAdministrativeRegion1 ||--|o OwlThing : "kwgo_sfWithin"
KwgoAdministrativeRegion1 ||--|o KwgoAdministrativeRegion2 : "kwgo_sfWithin"
KwgoAdministrativeRegion1 ||--|o KwgoAdministrativeRegion3 : "kwgo_sfWithin"
KwgoAdministrativeRegion1 ||--|o KwgoAdministrativeRegion1 : "kwgo_sfWithin"
KwgoAdministrativeRegion2 ||--|o OwlThing : "kwgo_administrativePartOf"
KwgoAdministrativeRegion2 ||--|o KwgoAdministrativeRegion2 : "kwgo_administrativePartOf"
KwgoAdministrativeRegion2 ||--|o KwgoAdministrativeRegion1 : "kwgo_administrativePartOf"
KwgoAdministrativeRegion2 ||--|o OwlThing : "kwgo_sfOverlaps"
KwgoAdministrativeRegion2 ||--|o KwgoAdministrativeRegion1 : "kwgo_sfOverlaps"
KwgoAdministrativeRegion2 ||--|o KwgoAdministrativeRegion3 : "kwgo_sfOverlaps"
KwgoAdministrativeRegion2 ||--|o KwgoS2CellLevel13 : "kwgo_sfOverlaps"
KwgoAdministrativeRegion2 ||--|o KwgoAdministrativeRegion2 : "kwgo_sfOverlaps"
KwgoAdministrativeRegion2 ||--|o OwlThing : "kwgo_sfContains"
KwgoAdministrativeRegion2 ||--|o KwgoS2CellLevel13 : "kwgo_sfContains"
KwgoAdministrativeRegion2 ||--|o GeoGeometry : "owl_sameAs"
KwgoAdministrativeRegion2 ||--|o RdfObjectProperty : "owl_sameAs"
KwgoAdministrativeRegion2 ||--|o RdfList : "owl_sameAs"
KwgoAdministrativeRegion2 ||--|o KwgoAdministrativeRegion1 : "owl_sameAs"
KwgoAdministrativeRegion2 ||--|o OwlThing : "owl_sameAs"
KwgoAdministrativeRegion2 ||--|o SfPolygon : "owl_sameAs"
KwgoAdministrativeRegion2 ||--|o KwgoAdministrativeRegion3 : "owl_sameAs"
KwgoAdministrativeRegion2 ||--|o KwgoAdministrativeRegion2 : "owl_sameAs"
KwgoAdministrativeRegion2 ||--|o KwgoS2CellLevel13 : "owl_sameAs"
KwgoAdministrativeRegion2 ||--|o SfPolygon : "geo_hasGeometry"
KwgoAdministrativeRegion2 ||--|o GeoGeometry : "geo_hasGeometry"
KwgoAdministrativeRegion2 ||--|o OwlThing : "geo_hasGeometry"
KwgoAdministrativeRegion2 ||--|o SfPolygon : "geo_hasDefaultGeometry"
KwgoAdministrativeRegion2 ||--|o GeoGeometry : "geo_hasDefaultGeometry"
KwgoAdministrativeRegion2 ||--|o OwlThing : "geo_hasDefaultGeometry"
KwgoAdministrativeRegion2 ||--|o OwlThing : "kwgo_sfWithin"
KwgoAdministrativeRegion2 ||--|o KwgoAdministrativeRegion2 : "kwgo_sfWithin"
KwgoAdministrativeRegion2 ||--|o KwgoAdministrativeRegion3 : "kwgo_sfWithin"
KwgoAdministrativeRegion2 ||--|o KwgoAdministrativeRegion1 : "kwgo_sfWithin"
KwgoAdministrativeRegion3 ||--|o OwlThing : "kwgo_administrativePartOf"
KwgoAdministrativeRegion3 ||--|o KwgoAdministrativeRegion2 : "kwgo_administrativePartOf"
KwgoAdministrativeRegion3 ||--|o KwgoAdministrativeRegion1 : "kwgo_administrativePartOf"
KwgoAdministrativeRegion3 ||--|o SfPolygon : "geo_defaultGeometry"
KwgoAdministrativeRegion3 ||--|o GeoGeometry : "geo_defaultGeometry"
KwgoAdministrativeRegion3 ||--|o OwlThing : "geo_defaultGeometry"
KwgoAdministrativeRegion3 ||--|o OwlThing : "kwgo_sfOverlaps"
KwgoAdministrativeRegion3 ||--|o KwgoAdministrativeRegion1 : "kwgo_sfOverlaps"
KwgoAdministrativeRegion3 ||--|o KwgoAdministrativeRegion3 : "kwgo_sfOverlaps"
KwgoAdministrativeRegion3 ||--|o KwgoS2CellLevel13 : "kwgo_sfOverlaps"
KwgoAdministrativeRegion3 ||--|o KwgoAdministrativeRegion2 : "kwgo_sfOverlaps"
KwgoAdministrativeRegion3 ||--|o OwlThing : "kwgo_sfContains"
KwgoAdministrativeRegion3 ||--|o KwgoS2CellLevel13 : "kwgo_sfContains"
KwgoAdministrativeRegion3 ||--|o GeoGeometry : "owl_sameAs"
KwgoAdministrativeRegion3 ||--|o RdfObjectProperty : "owl_sameAs"
KwgoAdministrativeRegion3 ||--|o RdfList : "owl_sameAs"
KwgoAdministrativeRegion3 ||--|o KwgoAdministrativeRegion1 : "owl_sameAs"
KwgoAdministrativeRegion3 ||--|o OwlThing : "owl_sameAs"
KwgoAdministrativeRegion3 ||--|o SfPolygon : "owl_sameAs"
KwgoAdministrativeRegion3 ||--|o KwgoAdministrativeRegion3 : "owl_sameAs"
KwgoAdministrativeRegion3 ||--|o KwgoAdministrativeRegion2 : "owl_sameAs"
KwgoAdministrativeRegion3 ||--|o KwgoS2CellLevel13 : "owl_sameAs"
KwgoAdministrativeRegion3 ||--|o SfPolygon : "geo_hasGeometry"
KwgoAdministrativeRegion3 ||--|o GeoGeometry : "geo_hasGeometry"
KwgoAdministrativeRegion3 ||--|o OwlThing : "geo_hasGeometry"
KwgoAdministrativeRegion3 ||--|o OwlThing : "kwgo_sfWithin"
KwgoAdministrativeRegion3 ||--|o KwgoAdministrativeRegion2 : "kwgo_sfWithin"
KwgoAdministrativeRegion3 ||--|o KwgoAdministrativeRegion3 : "kwgo_sfWithin"
KwgoAdministrativeRegion3 ||--|o KwgoAdministrativeRegion1 : "kwgo_sfWithin"
KwgoS2CellLevel13 ||--|o OwlThing : "kwgo_sfOverlaps"
KwgoS2CellLevel13 ||--|o KwgoAdministrativeRegion1 : "kwgo_sfOverlaps"
KwgoS2CellLevel13 ||--|o KwgoAdministrativeRegion3 : "kwgo_sfOverlaps"
KwgoS2CellLevel13 ||--|o KwgoS2CellLevel13 : "kwgo_sfOverlaps"
KwgoS2CellLevel13 ||--|o KwgoAdministrativeRegion2 : "kwgo_sfOverlaps"
KwgoS2CellLevel13 ||--|o GeoGeometry : "owl_sameAs"
KwgoS2CellLevel13 ||--|o RdfObjectProperty : "owl_sameAs"
KwgoS2CellLevel13 ||--|o RdfList : "owl_sameAs"
KwgoS2CellLevel13 ||--|o KwgoAdministrativeRegion1 : "owl_sameAs"
KwgoS2CellLevel13 ||--|o OwlThing : "owl_sameAs"
KwgoS2CellLevel13 ||--|o SfPolygon : "owl_sameAs"
KwgoS2CellLevel13 ||--|o KwgoAdministrativeRegion3 : "owl_sameAs"
KwgoS2CellLevel13 ||--|o KwgoAdministrativeRegion2 : "owl_sameAs"
KwgoS2CellLevel13 ||--|o KwgoS2CellLevel13 : "owl_sameAs"
KwgoS2CellLevel13 ||--|o OwlThing : "kwgo_sfTouches"
KwgoS2CellLevel13 ||--|o KwgoS2CellLevel13 : "kwgo_sfTouches"
KwgoS2CellLevel13 ||--|o SfPolygon : "geo_hasGeometry"
KwgoS2CellLevel13 ||--|o GeoGeometry : "geo_hasGeometry"
KwgoS2CellLevel13 ||--|o OwlThing : "geo_hasGeometry"
KwgoS2CellLevel13 ||--|o SfPolygon : "geo_hasDefaultGeometry"
KwgoS2CellLevel13 ||--|o GeoGeometry : "geo_hasDefaultGeometry"
KwgoS2CellLevel13 ||--|o OwlThing : "geo_hasDefaultGeometry"
KwgoS2CellLevel13 ||--|o OwlThing : "kwgo_sfWithin"
KwgoS2CellLevel13 ||--|o KwgoAdministrativeRegion2 : "kwgo_sfWithin"
KwgoS2CellLevel13 ||--|o KwgoAdministrativeRegion3 : "kwgo_sfWithin"
KwgoS2CellLevel13 ||--|o KwgoAdministrativeRegion1 : "kwgo_sfWithin"
OwlNamedIndividual ||--|o OwlThing : "kwgo_administrativePartOf"
OwlNamedIndividual ||--|o KwgoAdministrativeRegion2 : "kwgo_administrativePartOf"
OwlNamedIndividual ||--|o KwgoAdministrativeRegion1 : "kwgo_administrativePartOf"
OwlNamedIndividual ||--|o SfPolygon : "geo_defaultGeometry"
OwlNamedIndividual ||--|o GeoGeometry : "geo_defaultGeometry"
OwlNamedIndividual ||--|o OwlThing : "geo_defaultGeometry"
OwlNamedIndividual ||--|o OwlThing : "kwgo_sfOverlaps"
OwlNamedIndividual ||--|o KwgoAdministrativeRegion1 : "kwgo_sfOverlaps"
OwlNamedIndividual ||--|o KwgoAdministrativeRegion3 : "kwgo_sfOverlaps"
OwlNamedIndividual ||--|o KwgoS2CellLevel13 : "kwgo_sfOverlaps"
OwlNamedIndividual ||--|o KwgoAdministrativeRegion2 : "kwgo_sfOverlaps"
OwlNamedIndividual ||--|o OwlThing : "kwgo_sfContains"
OwlNamedIndividual ||--|o KwgoS2CellLevel13 : "kwgo_sfContains"
OwlNamedIndividual ||--|o GeoGeometry : "owl_sameAs"
OwlNamedIndividual ||--|o RdfObjectProperty : "owl_sameAs"
OwlNamedIndividual ||--|o RdfList : "owl_sameAs"
OwlNamedIndividual ||--|o KwgoAdministrativeRegion1 : "owl_sameAs"
OwlNamedIndividual ||--|o OwlThing : "owl_sameAs"
OwlNamedIndividual ||--|o SfPolygon : "owl_sameAs"
OwlNamedIndividual ||--|o KwgoAdministrativeRegion3 : "owl_sameAs"
OwlNamedIndividual ||--|o KwgoAdministrativeRegion2 : "owl_sameAs"
OwlNamedIndividual ||--|o KwgoS2CellLevel13 : "owl_sameAs"
OwlNamedIndividual ||--|o OwlThing : "kwgo_sfTouches"
OwlNamedIndividual ||--|o KwgoS2CellLevel13 : "kwgo_sfTouches"
OwlNamedIndividual ||--|o SfPolygon : "geo_hasGeometry"
OwlNamedIndividual ||--|o GeoGeometry : "geo_hasGeometry"
OwlNamedIndividual ||--|o OwlThing : "geo_hasGeometry"
OwlNamedIndividual ||--|o OwlThing : "rdfs_domain"
OwlNamedIndividual ||--|o OwlClass : "rdfs_domain"
OwlNamedIndividual ||--|o RdfsClass : "rdfs_domain"
OwlNamedIndividual ||--|o SfPolygon : "geo_hasDefaultGeometry"
OwlNamedIndividual ||--|o GeoGeometry : "geo_hasDefaultGeometry"
OwlNamedIndividual ||--|o OwlThing : "geo_hasDefaultGeometry"
OwlNamedIndividual ||--|o OwlThing : "kwgo_sfWithin"
OwlNamedIndividual ||--|o KwgoAdministrativeRegion2 : "kwgo_sfWithin"
OwlNamedIndividual ||--|o KwgoAdministrativeRegion3 : "kwgo_sfWithin"
OwlNamedIndividual ||--|o KwgoAdministrativeRegion1 : "kwgo_sfWithin"
OwlNamedIndividual ||--|o OwlThing : "rdfs_range"
OwlNamedIndividual ||--|o OwlClass : "rdfs_range"
OwlNamedIndividual ||--|o RdfsClass : "rdfs_range"
OwlNamedIndividual ||--|o GeoWktLiteral : "geo_asWKT"
OwlNothing ||--|o OwlThing : "kwgo_administrativePartOf"
OwlNothing ||--|o KwgoAdministrativeRegion2 : "kwgo_administrativePartOf"
OwlNothing ||--|o KwgoAdministrativeRegion1 : "kwgo_administrativePartOf"
OwlNothing ||--|o SfPolygon : "geo_defaultGeometry"
OwlNothing ||--|o GeoGeometry : "geo_defaultGeometry"
OwlNothing ||--|o OwlThing : "geo_defaultGeometry"
OwlNothing ||--|o OwlThing : "kwgo_sfOverlaps"
OwlNothing ||--|o KwgoAdministrativeRegion1 : "kwgo_sfOverlaps"
OwlNothing ||--|o KwgoAdministrativeRegion3 : "kwgo_sfOverlaps"
OwlNothing ||--|o KwgoS2CellLevel13 : "kwgo_sfOverlaps"
OwlNothing ||--|o KwgoAdministrativeRegion2 : "kwgo_sfOverlaps"
OwlNothing ||--|o OwlThing : "kwgo_sfContains"
OwlNothing ||--|o KwgoS2CellLevel13 : "kwgo_sfContains"
OwlNothing ||--|o GeoGeometry : "owl_sameAs"
OwlNothing ||--|o RdfObjectProperty : "owl_sameAs"
OwlNothing ||--|o RdfList : "owl_sameAs"
OwlNothing ||--|o KwgoAdministrativeRegion1 : "owl_sameAs"
OwlNothing ||--|o OwlThing : "owl_sameAs"
OwlNothing ||--|o SfPolygon : "owl_sameAs"
OwlNothing ||--|o KwgoAdministrativeRegion3 : "owl_sameAs"
OwlNothing ||--|o KwgoAdministrativeRegion2 : "owl_sameAs"
OwlNothing ||--|o KwgoS2CellLevel13 : "owl_sameAs"
OwlNothing ||--|o OwlThing : "kwgo_sfTouches"
OwlNothing ||--|o KwgoS2CellLevel13 : "kwgo_sfTouches"
OwlNothing ||--|o SfPolygon : "geo_hasGeometry"
OwlNothing ||--|o GeoGeometry : "geo_hasGeometry"
OwlNothing ||--|o OwlThing : "geo_hasGeometry"
OwlNothing ||--|o OwlThing : "rdfs_domain"
OwlNothing ||--|o OwlClass : "rdfs_domain"
OwlNothing ||--|o RdfsClass : "rdfs_domain"
OwlNothing ||--|o SfPolygon : "geo_hasDefaultGeometry"
OwlNothing ||--|o GeoGeometry : "geo_hasDefaultGeometry"
OwlNothing ||--|o OwlThing : "geo_hasDefaultGeometry"
OwlNothing ||--|o OwlThing : "kwgo_sfWithin"
OwlNothing ||--|o KwgoAdministrativeRegion2 : "kwgo_sfWithin"
OwlNothing ||--|o KwgoAdministrativeRegion3 : "kwgo_sfWithin"
OwlNothing ||--|o KwgoAdministrativeRegion1 : "kwgo_sfWithin"
OwlNothing ||--|o OwlThing : "rdfs_range"
OwlNothing ||--|o OwlClass : "rdfs_range"
OwlNothing ||--|o RdfsClass : "rdfs_range"
OwlNothing ||--|o GeoWktLiteral : "geo_asWKT"
OwlThing ||--|o OwlThing : "kwgo_administrativePartOf"
OwlThing ||--|o KwgoAdministrativeRegion2 : "kwgo_administrativePartOf"
OwlThing ||--|o KwgoAdministrativeRegion1 : "kwgo_administrativePartOf"
OwlThing ||--|o SfPolygon : "geo_defaultGeometry"
OwlThing ||--|o GeoGeometry : "geo_defaultGeometry"
OwlThing ||--|o OwlThing : "geo_defaultGeometry"
OwlThing ||--|o OwlThing : "kwgo_sfOverlaps"
OwlThing ||--|o KwgoAdministrativeRegion1 : "kwgo_sfOverlaps"
OwlThing ||--|o KwgoAdministrativeRegion3 : "kwgo_sfOverlaps"
OwlThing ||--|o KwgoS2CellLevel13 : "kwgo_sfOverlaps"
OwlThing ||--|o KwgoAdministrativeRegion2 : "kwgo_sfOverlaps"
OwlThing ||--|o OwlThing : "kwgo_sfContains"
OwlThing ||--|o KwgoS2CellLevel13 : "kwgo_sfContains"
OwlThing ||--|o GeoGeometry : "owl_sameAs"
OwlThing ||--|o RdfObjectProperty : "owl_sameAs"
OwlThing ||--|o RdfList : "owl_sameAs"
OwlThing ||--|o KwgoAdministrativeRegion1 : "owl_sameAs"
OwlThing ||--|o OwlThing : "owl_sameAs"
OwlThing ||--|o SfPolygon : "owl_sameAs"
OwlThing ||--|o KwgoAdministrativeRegion3 : "owl_sameAs"
OwlThing ||--|o KwgoAdministrativeRegion2 : "owl_sameAs"
OwlThing ||--|o KwgoS2CellLevel13 : "owl_sameAs"
OwlThing ||--|o OwlThing : "kwgo_sfTouches"
OwlThing ||--|o KwgoS2CellLevel13 : "kwgo_sfTouches"
OwlThing ||--|o SfPolygon : "geo_hasGeometry"
OwlThing ||--|o GeoGeometry : "geo_hasGeometry"
OwlThing ||--|o OwlThing : "geo_hasGeometry"
OwlThing ||--|o OwlThing : "rdfs_domain"
OwlThing ||--|o OwlClass : "rdfs_domain"
OwlThing ||--|o RdfsClass : "rdfs_domain"
OwlThing ||--|o SfPolygon : "geo_hasDefaultGeometry"
OwlThing ||--|o GeoGeometry : "geo_hasDefaultGeometry"
OwlThing ||--|o OwlThing : "geo_hasDefaultGeometry"
OwlThing ||--|o OwlThing : "kwgo_sfWithin"
OwlThing ||--|o KwgoAdministrativeRegion2 : "kwgo_sfWithin"
OwlThing ||--|o KwgoAdministrativeRegion3 : "kwgo_sfWithin"
OwlThing ||--|o KwgoAdministrativeRegion1 : "kwgo_sfWithin"
OwlThing ||--|o OwlThing : "rdfs_range"
OwlThing ||--|o OwlClass : "rdfs_range"
OwlThing ||--|o RdfsClass : "rdfs_range"
OwlThing ||--|o GeoWktLiteral : "geo_asWKT"
RdfList ||--|o GeoGeometry : "owl_sameAs"
RdfList ||--|o RdfObjectProperty : "owl_sameAs"
RdfList ||--|o RdfList : "owl_sameAs"
RdfList ||--|o KwgoAdministrativeRegion1 : "owl_sameAs"
RdfList ||--|o OwlThing : "owl_sameAs"
RdfList ||--|o SfPolygon : "owl_sameAs"
RdfList ||--|o KwgoAdministrativeRegion3 : "owl_sameAs"
RdfList ||--|o KwgoAdministrativeRegion2 : "owl_sameAs"
RdfList ||--|o KwgoS2CellLevel13 : "owl_sameAs"
RdfObjectProperty ||--|o GeoGeometry : "owl_sameAs"
RdfObjectProperty ||--|o RdfObjectProperty : "owl_sameAs"
RdfObjectProperty ||--|o RdfList : "owl_sameAs"
RdfObjectProperty ||--|o KwgoAdministrativeRegion1 : "owl_sameAs"
RdfObjectProperty ||--|o OwlThing : "owl_sameAs"
RdfObjectProperty ||--|o SfPolygon : "owl_sameAs"
RdfObjectProperty ||--|o KwgoAdministrativeRegion3 : "owl_sameAs"
RdfObjectProperty ||--|o KwgoAdministrativeRegion2 : "owl_sameAs"
RdfObjectProperty ||--|o KwgoS2CellLevel13 : "owl_sameAs"
RdfObjectProperty ||--|o OwlThing : "rdfs_range"
RdfObjectProperty ||--|o OwlClass : "rdfs_range"
RdfObjectProperty ||--|o RdfsClass : "rdfs_range"
RdfObjectProperty ||--|o OwlThing : "rdfs_domain"
RdfObjectProperty ||--|o OwlClass : "rdfs_domain"
RdfObjectProperty ||--|o RdfsClass : "rdfs_domain"
SfPolygon ||--|o GeoWktLiteral : "geo_asWKT"
SfPolygon ||--|o GeoGeometry : "owl_sameAs"
SfPolygon ||--|o RdfObjectProperty : "owl_sameAs"
SfPolygon ||--|o RdfList : "owl_sameAs"
SfPolygon ||--|o KwgoAdministrativeRegion1 : "owl_sameAs"
SfPolygon ||--|o OwlThing : "owl_sameAs"
SfPolygon ||--|o SfPolygon : "owl_sameAs"
SfPolygon ||--|o KwgoAdministrativeRegion3 : "owl_sameAs"
SfPolygon ||--|o KwgoAdministrativeRegion2 : "owl_sameAs"
SfPolygon ||--|o KwgoS2CellLevel13 : "owl_sameAs"

```



## Classes

| Class | Description | Occurrences |
| --- | --- | --- |
| [GeoGeometry](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/GeoGeometry.md) | No class (type) description specified<br/>| 251854 | 
| [GeoWktLiteral](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/GeoWktLiteral.md) | No class (type) description specified<br/>| 0 | 
| [KwgoAdministrativeRegion1](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/KwgoAdministrativeRegion1.md) | No class (type) description specified<br/>| 2 | 
| [KwgoAdministrativeRegion2](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/KwgoAdministrativeRegion2.md) | No class (type) description specified<br/>| 118 | 
| [KwgoAdministrativeRegion3](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/KwgoAdministrativeRegion3.md) | No class (type) description specified<br/>| 2225 | 
| [KwgoS2CellLevel13](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/KwgoS2CellLevel13.md) | No class (type) description specified<br/>| 249509 | 
| [OwlObjectProperty](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/OwlObjectProperty.md) | No class (type) description specified<br/>| 0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OwlAsymmetricProperty](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/OwlAsymmetricProperty.md) | No class (type) description specified<br/>| 0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OwlInverseFunctionalProperty](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/OwlInverseFunctionalProperty.md) | No class (type) description specified<br/>| 0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OwlIrreflexiveProperty](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/OwlIrreflexiveProperty.md) | No class (type) description specified<br/>| 0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OwlReflexiveProperty](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/OwlReflexiveProperty.md) | No class (type) description specified<br/>| 0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OwlSymmetricProperty](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/OwlSymmetricProperty.md) | No class (type) description specified<br/>| 0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OwlTransitiveProperty](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/OwlTransitiveProperty.md) | No class (type) description specified<br/>| 0 | 
| [OwlThing](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/OwlThing.md) | No class (type) description specified<br/>| 571175 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OwlNamedIndividual](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/OwlNamedIndividual.md) | No class (type) description specified<br/>| 0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OwlNothing](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/OwlNothing.md) | No class (type) description specified<br/>| 0 | 
| [RdfList](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/RdfList.md) | No class (type) description specified<br/>| 1 | 
| [RdfObjectProperty](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/RdfObjectProperty.md) | No class (type) description specified<br/>| 1 | 
| [RdfProperty](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/RdfProperty.md) | No class (type) description specified<br/>| 0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OwlAnnotationProperty](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/OwlAnnotationProperty.md) | No class (type) description specified<br/>| 0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OwlDatatypeProperty](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/OwlDatatypeProperty.md) | No class (type) description specified<br/>| 0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OwlDeprecatedProperty](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/OwlDeprecatedProperty.md) | No class (type) description specified<br/>| 0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OwlFunctionalProperty](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/OwlFunctionalProperty.md) | No class (type) description specified<br/>| 0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OwlOntologyProperty](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/OwlOntologyProperty.md) | No class (type) description specified<br/>| 0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RdfsContainerMembershipProperty](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/RdfsContainerMembershipProperty.md) | No class (type) description specified<br/>| 0 | 
| [RdfStatement](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/RdfStatement.md) | No class (type) description specified<br/>| 0 | 
| [RdfsClass](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/RdfsClass.md) | No class (type) description specified<br/>| 0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OwlClass](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/OwlClass.md) | No class (type) description specified<br/>| 0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OwlRestriction](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/OwlRestriction.md) | No class (type) description specified<br/>| 0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OwlDeprecatedClass](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/OwlDeprecatedClass.md) | No class (type) description specified<br/>| 0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RdfsDatatype](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/RdfsDatatype.md) | No class (type) description specified<br/>| 0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OwlDataRange](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/OwlDataRange.md) | No class (type) description specified<br/>| 0 | 
| [RdfsContainer](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/RdfsContainer.md) | No class (type) description specified<br/>| 0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RdfAlt](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/RdfAlt.md) | No class (type) description specified<br/>| 0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RdfBag](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/RdfBag.md) | No class (type) description specified<br/>| 0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RdfSeq](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/RdfSeq.md) | No class (type) description specified<br/>| 0 | 
| [RdfsLiteral](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/RdfsLiteral.md) | No class (type) description specified<br/>| 0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OwlRational](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/OwlRational.md) | No class (type) description specified<br/>| 0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OwlReal](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/OwlReal.md) | No class (type) description specified<br/>| 0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RdfPlainLiteral](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/RdfPlainLiteral.md) | No class (type) description specified<br/>| 0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RdfXMLLiteral](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/RdfXMLLiteral.md) | No class (type) description specified<br/>| 0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XsdAnyURI](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/XsdAnyURI.md) | No class (type) description specified<br/>| 0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XsdBase64Binary](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/XsdBase64Binary.md) | No class (type) description specified<br/>| 0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XsdBoolean](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/XsdBoolean.md) | No class (type) description specified<br/>| 0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XsdByte](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/XsdByte.md) | No class (type) description specified<br/>| 0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XsdDateTime](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/XsdDateTime.md) | No class (type) description specified<br/>| 0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XsdDateTimeStamp](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/XsdDateTimeStamp.md) | No class (type) description specified<br/>| 0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XsdDecimal](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/XsdDecimal.md) | No class (type) description specified<br/>| 0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XsdDouble](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/XsdDouble.md) | No class (type) description specified<br/>| 0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XsdFloat](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/XsdFloat.md) | No class (type) description specified<br/>| 0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XsdHexBinary](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/XsdHexBinary.md) | No class (type) description specified<br/>| 0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XsdInt](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/XsdInt.md) | No class (type) description specified<br/>| 0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XsdInteger](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/XsdInteger.md) | No class (type) description specified<br/>| 0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XsdLanguage](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/XsdLanguage.md) | No class (type) description specified<br/>| 0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XsdLong](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/XsdLong.md) | No class (type) description specified<br/>| 0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XsdName](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/XsdName.md) | No class (type) description specified<br/>| 0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XsdNCName](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/XsdNCName.md) | No class (type) description specified<br/>| 0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XsdNegativeInteger](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/XsdNegativeInteger.md) | No class (type) description specified<br/>| 0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XsdNMTOKEN](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/XsdNMTOKEN.md) | No class (type) description specified<br/>| 0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XsdNonNegativeInteger](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/XsdNonNegativeInteger.md) | No class (type) description specified<br/>| 0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XsdNonPositiveInteger](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/XsdNonPositiveInteger.md) | No class (type) description specified<br/>| 0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XsdNormalizedString](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/XsdNormalizedString.md) | No class (type) description specified<br/>| 0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XsdPositiveInteger](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/XsdPositiveInteger.md) | No class (type) description specified<br/>| 0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XsdShort](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/XsdShort.md) | No class (type) description specified<br/>| 0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XsdString](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/XsdString.md) | No class (type) description specified<br/>| 0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XsdToken](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/XsdToken.md) | No class (type) description specified<br/>| 0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XsdUnsignedByte](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/XsdUnsignedByte.md) | No class (type) description specified<br/>| 0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XsdUnsignedInt](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/XsdUnsignedInt.md) | No class (type) description specified<br/>| 0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XsdUnsignedLong](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/XsdUnsignedLong.md) | No class (type) description specified<br/>| 0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XsdUnsignedShort](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/XsdUnsignedShort.md) | No class (type) description specified<br/>| 0 | 
| [RdfsResource](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/RdfsResource.md) | No class (type) description specified<br/>| 0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OwlAllDifferent](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/OwlAllDifferent.md) | No class (type) description specified<br/>| 0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OwlAllDisjointClasses](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/OwlAllDisjointClasses.md) | No class (type) description specified<br/>| 0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OwlAllDisjointProperties](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/OwlAllDisjointProperties.md) | No class (type) description specified<br/>| 0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OwlAnnotation](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/OwlAnnotation.md) | No class (type) description specified<br/>| 0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OwlAxiom](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/OwlAxiom.md) | No class (type) description specified<br/>| 0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OwlNegativePropertyAssertion](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/OwlNegativePropertyAssertion.md) | No class (type) description specified<br/>| 0 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OwlOntology](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/OwlOntology.md) | No class (type) description specified<br/>| 0 | 
| [Sf#Polygon](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/classes/Sf#Polygon.md) | No class (type) description specified<br/>| 251736 | 





## Slots

| Slot | Description | Occurrences |
| --- | --- | --- |
| [geo_asWKT](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/geo_asWKT.md) | No slot (predicate) description specified<br/>| 251854 |
| [geo_defaultGeometry](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/geo_defaultGeometry.md) | No slot (predicate) description specified<br/>| 2225 |
| [geo_hasDefaultGeometry](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/geo_hasDefaultGeometry.md) | No slot (predicate) description specified<br/>| 249629 |
| [geo_hasGeometry](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/geo_hasGeometry.md) | No slot (predicate) description specified<br/>| 251854 |
| [geo_hasMetricArea](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/geo_hasMetricArea.md) | No slot (predicate) description specified<br/>| 249509 |
| [kwgo_administrativePartOf](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/kwgo_administrativePartOf.md) | No slot (predicate) description specified<br/>| 2345 |
| [kwgo_cellID](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/kwgo_cellID.md) | No slot (predicate) description specified<br/>| 249509 |
| [kwgo_hasFIPS](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/kwgo_hasFIPS.md) | No slot (predicate) description specified<br/>| 2345 |
| [kwgo_sfContains](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/kwgo_sfContains.md) | No slot (predicate) description specified<br/>| 923206 |
| [kwgo_sfOverlaps](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/kwgo_sfOverlaps.md) | No slot (predicate) description specified<br/>| 287124 |
| [kwgo_sfTouches](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/kwgo_sfTouches.md) | No slot (predicate) description specified<br/>| 2007528 |
| [kwgo_sfWithin](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/kwgo_sfWithin.md) | No slot (predicate) description specified<br/>| 925551 |
| [owl_allValuesFrom](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/owl_allValuesFrom.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [owl_annotatedProperty](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/owl_annotatedProperty.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [owl_annotatedSource](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/owl_annotatedSource.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [owl_annotatedTarget](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/owl_annotatedTarget.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [owl_assertionProperty](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/owl_assertionProperty.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [owl_backwardCompatibleWith](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/owl_backwardCompatibleWith.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [owl_bottomDataProperty](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/owl_bottomDataProperty.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [owl_bottomObjectProperty](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/owl_bottomObjectProperty.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [owl_cardinality](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/owl_cardinality.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [owl_complementOf](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/owl_complementOf.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [owl_datatypeComplementOf](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/owl_datatypeComplementOf.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [owl_deprecated](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/owl_deprecated.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [owl_differentFrom](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/owl_differentFrom.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [owl_disjointUnionOf](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/owl_disjointUnionOf.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [owl_disjointWith](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/owl_disjointWith.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [owl_distinctMembers](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/owl_distinctMembers.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [owl_equivalentClass](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/owl_equivalentClass.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [owl_equivalentProperty](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/owl_equivalentProperty.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [owl_hasKey](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/owl_hasKey.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [owl_hasSelf](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/owl_hasSelf.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [owl_hasValue](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/owl_hasValue.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [owl_imports](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/owl_imports.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [owl_incompatibleWith](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/owl_incompatibleWith.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [owl_intersectionOf](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/owl_intersectionOf.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [owl_inverseOf](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/owl_inverseOf.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [owl_maxCardinality](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/owl_maxCardinality.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [owl_maxQualifiedCardinality](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/owl_maxQualifiedCardinality.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [owl_members](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/owl_members.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [owl_minCardinality](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/owl_minCardinality.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [owl_minQualifiedCardinality](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/owl_minQualifiedCardinality.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [owl_onClass](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/owl_onClass.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [owl_onDataRange](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/owl_onDataRange.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [owl_onDatatype](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/owl_onDatatype.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [owl_oneOf](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/owl_oneOf.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [owl_onProperties](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/owl_onProperties.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [owl_onProperty](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/owl_onProperty.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [owl_priorVersion](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/owl_priorVersion.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [owl_propertyChainAxiom](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/owl_propertyChainAxiom.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [owl_propertyDisjointWith](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/owl_propertyDisjointWith.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [owl_qualifiedCardinality](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/owl_qualifiedCardinality.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [owl_sameAs](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/owl_sameAs.md) | No slot (predicate) description specified<br/>| 571175 |
| [owl_someValuesFrom](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/owl_someValuesFrom.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [owl_sourceIndividual](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/owl_sourceIndividual.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [owl_targetIndividual](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/owl_targetIndividual.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [owl_targetValue](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/owl_targetValue.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [owl_topDataProperty](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/owl_topDataProperty.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [owl_unionOf](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/owl_unionOf.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [owl_versionInfo](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/owl_versionInfo.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [owl_versionIRI](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/owl_versionIRI.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [owl_withRestrictions](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/owl_withRestrictions.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [rdf__1](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/rdf__1.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [rdf_first](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/rdf_first.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [rdf_langRange](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/rdf_langRange.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [rdf_object](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/rdf_object.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [rdf_predicate](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/rdf_predicate.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [rdf_rest](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/rdf_rest.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [rdf_subject](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/rdf_subject.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [rdf_type](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/rdf_type.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [rdf_value](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/rdf_value.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [rdfs_comment](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/rdfs_comment.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [rdfs_domain](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/rdfs_domain.md) | No slot (predicate) description specified<br/>| 1 |
| [rdfs_isDefinedBy](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/rdfs_isDefinedBy.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [rdfs_label](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/rdfs_label.md) | No slot (predicate) description specified<br/>| 503708 |
| [rdfs_range](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/rdfs_range.md) | No slot (predicate) description specified<br/>| 1 |
| [rdfs_seeAlso](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/rdfs_seeAlso.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [rdfs_subClassOf](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/rdfs_subClassOf.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [rdfs_subPropertyOf](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/rdfs_subPropertyOf.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [xsd_length](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/xsd_length.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [xsd_maxExclusive](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/xsd_maxExclusive.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [xsd_maxInclusive](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/xsd_maxInclusive.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [xsd_maxLength](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/xsd_maxLength.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [xsd_minExclusive](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/xsd_minExclusive.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [xsd_minInclusive](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/xsd_minInclusive.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [xsd_minLength](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/xsd_minLength.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |
| [xsd_pattern](https://github.com/frink-okn/graph-descriptions/blob/main/spatial-kg/slots/xsd_pattern.md) | No slot (predicate) description specified<br/>No occurrences of this slot in the graph.| 0 |









## IRI prefixes

* geo: http://www.opengis.net/ont/geosparql#
* kwgo: http://stko-kwg.geog.ucsb.edu/lod/ontology/
* kwgr: http://stko-kwg.geog.ucsb.edu/lod/resource/
* linkml: https://w3id.org/linkml/
* owl: http://www.w3.org/2002/07/owl#
* rdf: http://www.w3.org/1999/02/22-rdf-syntax-ns#
* rdfs: http://www.w3.org/2000/01/rdf-schema#
* sf: http://www.opengis.net/ont/sf
* xsd: http://www.w3.org/2001/XMLSchema#
* shex: http://www.w3.org/ns/shex#
* schema: http://schema.org/
