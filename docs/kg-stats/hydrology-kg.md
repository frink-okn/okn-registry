# hydrologykg

This ontology supports querying the SAWGraph Knowledge Graph and the KnowWhereGraph. It is an adaptation of the spatial ontology originally published by the KnowWhereGraph Project



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
SkosCollection {

}
SkosConcept {

}
SkosConceptScheme {

}
SkosOrderedCollection {

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
HttpDef.seegrid.csiro.auIsotc211Iso191502012Hm2owl#CodeList {

}
HttpDef.seegrid.csiro.auIsotc211Iso191502012Hm2owl#DataType {

}
Seegrid-basicAcceleration {

}
Seegrid-basicAngle {

}
Seegrid-basicAngularVelocity {

}
Seegrid-basicArea {

}
Seegrid-basicCurrency {

}
Seegrid-basicDistance {

}
Seegrid-basicLength {

}
Seegrid-basicMass {

}
Seegrid-basicMeasure {

}
Seegrid-basicScale {

}
Seegrid-basicTime {

}
Seegrid-basicUnitOfMeasure {

}
Seegrid-basicVector {

}
Seegrid-basicVelocity {

}
Seegrid-basicVolume {

}
Seegrid-basicWeight {

}
Seegrid-ciAddress {

}
Seegrid-ciCitation {

}
Seegrid-ciContact {

}
Seegrid-ciDate {

}
Seegrid-ciDateTypeCode {

}
Seegrid-ciOnLineFunctionCode {

}
Seegrid-ciOnlineResource {

}
Seegrid-ciPresentationFormCode {

}
Seegrid-ciResponsibleParty {

}
Seegrid-ciRoleCode {

}
Seegrid-ciSeries {

}
Seegrid-ciTelephone {

}
HyfHYCanal {

}
HyfHYCartographicRealization {

}
HyfHYCatchment {

}
HyfHYCatchmentAggregate {

}
HyfHYCatchmentArea {

}
HyfHYCatchmentDivide {

}
HyfHYCatchmentRealization {

}
HyfHYChannel {

}
HyfHYChannelNetwork {

}
HyfHYCrossSection {

}
HyfHYDendriticCatchment {

}
HyfHYDepression {

}
HyfHYDistanceDescription {

}
HyfHYDistanceFromReferent {

}
HyfHYEstuary {

}
HyfHYFlowPath {

}
HyfHYHydroFeature {

}
HyfHYHydroFeatureName {

}
HyfHYHydroLocation {

}
HyfHYHydroLocationType {

}
HyfHYHydroNetwork {

}
HyfHYHydroNexus {

}
HyfHYHydrographicNetwork {

}
HyfHYHydrometricFeature {

}
HyfHYHydrometricNetwork {

}
HyfHYImpoundment {

}
HyfHYIndirectPosition {

}
HyfHYInteriorCatchment {

}
HyfHYLagoon {

}
HyfHYLake {

}
HyfHYLongitudinalSection {

}
HyfHYNameUsage {

}
HyfHYReservoir {

}
HyfHYRiver {

}
HyfHYWaterBody {

}
HyfHYWaterBodyStratum {

}
HyfHYWaterLiquidPhase {

}
HyfHYWaterSolidPhase {

}
QudtAbstractQuantityKind {

}
QudtAngleUnit {
    string rdfs_label  
    uri qudt_hasDimensionVector  
    uri qudt_hasQuantityKind  
    uri qudt_dbpediaMatch  
    string qudt_iec61360Code  
    decimal qudt_conversionMultiplierSN  
    double qudt_conversionMultiplierSN  
    string dct_description  
    string qudt_symbol  
    string qudt_udunitsCode  
    uri qudt_informativeReference  
    uri qudt_applicableSystem  
    decimal qudt_conversionMultiplier  
    string qudt_uneceCommonCode  
    uri qudt_omUnit  
    uri rdfs_seeAlso  
    uri qudt_isoNormativeReference  
    string vaem_todo  
    qudt_LatexString qudt_latexDefinition  
    uri qudt_siExactMatch  
    qudt_LatexString qudt_expression  
    string qudt_expression  
    string qudt_plainTextDescription  
    double qudt_conversionOffsetSN  
    string rdfs_comment  
    qudt_UCUMcs qudt_ucumCode  
    string qudt_ucumCode  
    uri qudt_derivedUnitOfSystem  
    uri qudt_qkdvNumerator  
    string qudt_siUnitsExpression  
    uri qudt_definedUnitOfSystem  
    decimal qudt_factorUnitScalar  
    uri qudt_derivedCoherentUnitOfSystem  
    decimal qudt_conversionOffset  
    uri qudt_qkdvDenominator  
    qudt_LatexString qudt_latexSymbol  
    string qudt_altSymbol  
    boolean qudt_deprecated  
}
QudtAspect {

}
QudtAspectClass {
    string rdfs_comment  
    string rdfs_label  
}
QudtBaseDimensionMagnitude {

}
QudtBinaryPrefix {
    string rdfs_label  
    string dct_description  
    decimal qudt_prefixMultiplier  
    string qudt_symbol  
    double qudt_prefixMultiplierSN  
    qudt_UCUMcs qudt_ucumCode  
    string qudt_ucumCode  
}
QudtBitEncodingType {
    string rdfs_label  
    integer qudt_bits  
}
QudtBooleanEncodingType {
    string rdfs_label  
    integer qudt_bits  
    integer qudt_bytes  
}
QudtByteEncodingType {
    integer qudt_bytes  
    string rdfs_label  
}
QudtCardinalityType {
    string rdfs_label  
    string dtype_literal  
    string dct_description  
    uri qudt_informativeReference  
}
QudtCharEncodingType {
    integer qudt_bytes  
    string rdfs_label  
}
QudtCitation {

}
QudtComment {

}
QudtConcept {

}
QudtConstantValue {

}
QudtContextualUnit {
    uri qudt_dbpediaMatch  
    qudt_LatexString qudt_expression  
    string qudt_expression  
    uri qudt_hasQuantityKind  
    string qudt_iec61360Code  
    string qudt_plainTextDescription  
    string qudt_udunitsCode  
    uri qudt_applicableSystem  
    qudt_UCUMcs qudt_ucumCode  
    string qudt_ucumCode  
    decimal qudt_conversionMultiplier  
    uri qudt_informativeReference  
    string qudt_uneceCommonCode  
    string rdfs_label  
    uri qudt_hasDimensionVector  
    decimal qudt_conversionMultiplierSN  
    double qudt_conversionMultiplierSN  
    string dct_description  
    string qudt_symbol  
    string qudt_altSymbol  
    boolean qudt_deprecated  
    uri qudt_omUnit  
    uri rdfs_seeAlso  
    uri qudt_isoNormativeReference  
    string vaem_todo  
    qudt_LatexString qudt_latexDefinition  
    uri qudt_siExactMatch  
    double qudt_conversionOffsetSN  
    string rdfs_comment  
    uri qudt_derivedUnitOfSystem  
    uri qudt_qkdvNumerator  
    string qudt_siUnitsExpression  
    uri qudt_definedUnitOfSystem  
    decimal qudt_factorUnitScalar  
    uri qudt_derivedCoherentUnitOfSystem  
    decimal qudt_conversionOffset  
    uri qudt_qkdvDenominator  
    qudt_LatexString qudt_latexSymbol  
}
QudtCountingUnit {
    uri qudt_omUnit  
    uri qudt_dbpediaMatch  
    uri qudt_hasQuantityKind  
    string qudt_iec61360Code  
    string qudt_plainTextDescription  
    double qudt_conversionOffsetSN  
    uri qudt_applicableSystem  
    qudt_UCUMcs qudt_ucumCode  
    string qudt_ucumCode  
    decimal qudt_conversionMultiplier  
    decimal qudt_factorUnitScalar  
    uri qudt_informativeReference  
    string qudt_uneceCommonCode  
    string rdfs_label  
    uri qudt_hasDimensionVector  
    decimal qudt_conversionMultiplierSN  
    double qudt_conversionMultiplierSN  
    decimal qudt_conversionOffset  
    string dct_description  
    string qudt_symbol  
    string qudt_udunitsCode  
    uri rdfs_seeAlso  
    uri qudt_isoNormativeReference  
    string vaem_todo  
    qudt_LatexString qudt_latexDefinition  
    uri qudt_siExactMatch  
    qudt_LatexString qudt_expression  
    string qudt_expression  
    string rdfs_comment  
    uri qudt_derivedUnitOfSystem  
    uri qudt_qkdvNumerator  
    string qudt_siUnitsExpression  
    uri qudt_definedUnitOfSystem  
    uri qudt_derivedCoherentUnitOfSystem  
    uri qudt_qkdvDenominator  
    qudt_LatexString qudt_latexSymbol  
    string qudt_altSymbol  
    boolean qudt_deprecated  
}
QudtCurrencyUnit {
    qudt_LatexString qudt_expression  
    string qudt_expression  
    string rdfs_label  
    uri qudt_omUnit  
    integer qudt_currencyExponent  
    uri qudt_hasDimensionVector  
    uri qudt_hasQuantityKind  
    string qudt_currencyNumber  
    uri qudt_dbpediaMatch  
    string qudt_currencyCode  
    qudt_UCUMcs qudt_ucumCode  
    string qudt_ucumCode  
    decimal qudt_conversionMultiplierSN  
    double qudt_conversionMultiplierSN  
    string qudt_symbol  
    string qudt_altSymbol  
    uri qudt_informativeReference  
    decimal qudt_conversionMultiplier  
    string qudt_iec61360Code  
    string dct_description  
    string qudt_udunitsCode  
    uri qudt_applicableSystem  
    string qudt_uneceCommonCode  
    uri rdfs_seeAlso  
    uri qudt_isoNormativeReference  
    string vaem_todo  
    qudt_LatexString qudt_latexDefinition  
    uri qudt_siExactMatch  
    string qudt_plainTextDescription  
    double qudt_conversionOffsetSN  
    string rdfs_comment  
    uri qudt_derivedUnitOfSystem  
    uri qudt_qkdvNumerator  
    string qudt_siUnitsExpression  
    uri qudt_definedUnitOfSystem  
    decimal qudt_factorUnitScalar  
    uri qudt_derivedCoherentUnitOfSystem  
    decimal qudt_conversionOffset  
    uri qudt_qkdvDenominator  
    qudt_LatexString qudt_latexSymbol  
    boolean qudt_deprecated  
}
QudtDataEncoding {

}
QudtDataItem {

}
QudtDatatype {

}
QudtDateTimeStringEncodingType {
    string rdfs_label  
    string qudt_allowedPattern  
}
QudtDecimalPrefix {
    string rdfs_label  
    uri qudt_dbpediaMatch  
    string dct_description  
    decimal qudt_prefixMultiplier  
    double qudt_prefixMultiplierSN  
    uri qudt_siExactMatch  
    string qudt_symbol  
    uri qudt_informativeReference  
    qudt_UCUMcs qudt_ucumCode  
    string qudt_ucumCode  
}
QudtDerivedUnit {
    uri qudt_omUnit  
    uri rdfs_seeAlso  
    uri qudt_isoNormativeReference  
    uri qudt_dbpediaMatch  
    qudt_LatexString qudt_latexDefinition  
    uri qudt_siExactMatch  
    qudt_LatexString qudt_expression  
    string qudt_expression  
    uri qudt_hasQuantityKind  
    string qudt_iec61360Code  
    string qudt_plainTextDescription  
    double qudt_conversionOffsetSN  
    string qudt_udunitsCode  
    string rdfs_comment  
    uri qudt_applicableSystem  
    qudt_UCUMcs qudt_ucumCode  
    string qudt_ucumCode  
    decimal qudt_conversionMultiplier  
    uri qudt_derivedUnitOfSystem  
    uri qudt_qkdvNumerator  
    string qudt_siUnitsExpression  
    uri qudt_definedUnitOfSystem  
    rdf_HTML qudt_guidance  
    decimal qudt_factorUnitScalar  
    uri qudt_informativeReference  
    string qudt_uneceCommonCode  
    string rdfs_label  
    uri qudt_hasDimensionVector  
    decimal qudt_conversionMultiplierSN  
    double qudt_conversionMultiplierSN  
    uri qudt_derivedCoherentUnitOfSystem  
    decimal qudt_conversionOffset  
    uri qudt_qkdvDenominator  
    string dct_description  
    string vaem_comment  
    string qudt_symbol  
    qudt_LatexString qudt_latexSymbol  
    string qudt_altSymbol  
    boolean qudt_deprecated  
    string vaem_todo  
}
QudtDimensionlessUnit {
    string rdfs_label  
    uri qudt_hasDimensionVector  
    uri qudt_hasQuantityKind  
    uri qudt_dbpediaMatch  
    string qudt_iec61360Code  
    decimal qudt_conversionMultiplierSN  
    double qudt_conversionMultiplierSN  
    string dct_description  
    string qudt_symbol  
    string qudt_udunitsCode  
    uri qudt_informativeReference  
    uri qudt_applicableSystem  
    decimal qudt_conversionMultiplier  
    string qudt_uneceCommonCode  
    uri qudt_omUnit  
    uri rdfs_seeAlso  
    uri qudt_isoNormativeReference  
    string vaem_todo  
    qudt_LatexString qudt_latexDefinition  
    uri qudt_siExactMatch  
    qudt_LatexString qudt_expression  
    string qudt_expression  
    string qudt_plainTextDescription  
    double qudt_conversionOffsetSN  
    string rdfs_comment  
    qudt_UCUMcs qudt_ucumCode  
    string qudt_ucumCode  
    uri qudt_derivedUnitOfSystem  
    uri qudt_qkdvNumerator  
    string qudt_siUnitsExpression  
    uri qudt_definedUnitOfSystem  
    decimal qudt_factorUnitScalar  
    uri qudt_derivedCoherentUnitOfSystem  
    decimal qudt_conversionOffset  
    uri qudt_qkdvDenominator  
    qudt_LatexString qudt_latexSymbol  
    string qudt_altSymbol  
    boolean qudt_deprecated  
}
QudtDiscipline {

}
QudtEncoding {

}
QudtEndianType {
    string rdfs_label  
    string dtype_literal  
}
QudtEnumeratedValue {

}
QudtEnumeration {

}
QudtEnumerationScale {

}
QudtFigure {

}
QudtFloatingPointEncodingType {
    integer qudt_bytes  
    string rdfs_label  
}
QudtIntegerEncodingType {
    integer qudt_bytes  
    string rdfs_label  
}
QudtIntervalScale {

}
QudtLogarithmicUnit {
    string rdfs_label  
    uri qudt_hasDimensionVector  
    uri qudt_hasQuantityKind  
    uri qudt_dbpediaMatch  
    string qudt_iec61360Code  
    qudt_UCUMcs qudt_ucumCode  
    string qudt_ucumCode  
    decimal qudt_conversionMultiplierSN  
    double qudt_conversionMultiplierSN  
    string dct_description  
    uri qudt_siExactMatch  
    string qudt_symbol  
    uri qudt_informativeReference  
    uri qudt_applicableSystem  
    decimal qudt_conversionMultiplier  
    string qudt_uneceCommonCode  
    string qudt_udunitsCode  
    uri qudt_omUnit  
    uri rdfs_seeAlso  
    uri qudt_isoNormativeReference  
    string vaem_todo  
    qudt_LatexString qudt_latexDefinition  
    qudt_LatexString qudt_expression  
    string qudt_expression  
    string qudt_plainTextDescription  
    double qudt_conversionOffsetSN  
    string rdfs_comment  
    uri qudt_derivedUnitOfSystem  
    uri qudt_qkdvNumerator  
    string qudt_siUnitsExpression  
    uri qudt_definedUnitOfSystem  
    decimal qudt_factorUnitScalar  
    uri qudt_derivedCoherentUnitOfSystem  
    decimal qudt_conversionOffset  
    uri qudt_qkdvDenominator  
    qudt_LatexString qudt_latexSymbol  
    string qudt_altSymbol  
    boolean qudt_deprecated  
}
QudtMathsFunctionType {

}
QudtNISTSP811Comment {

}
QudtNominalScale {

}
QudtOrderedType {
    string rdfs_label  
    string dtype_literal  
    string qudt_plainTextDescription  
}
QudtOrdinalScale {

}
QudtOrganization {

}
QudtPhysicalConstant {

}
QudtPlaneAngleUnit {
    string rdfs_label  
    uri qudt_hasDimensionVector  
    uri qudt_hasQuantityKind  
    uri qudt_dbpediaMatch  
    string qudt_iec61360Code  
    decimal qudt_conversionMultiplierSN  
    double qudt_conversionMultiplierSN  
    string dct_description  
    string qudt_symbol  
    string qudt_udunitsCode  
    uri qudt_informativeReference  
    uri qudt_applicableSystem  
    decimal qudt_conversionMultiplier  
    string qudt_uneceCommonCode  
    uri qudt_omUnit  
    uri rdfs_seeAlso  
    uri qudt_isoNormativeReference  
    string vaem_todo  
    qudt_LatexString qudt_latexDefinition  
    uri qudt_siExactMatch  
    qudt_LatexString qudt_expression  
    string qudt_expression  
    string qudt_plainTextDescription  
    double qudt_conversionOffsetSN  
    string rdfs_comment  
    qudt_UCUMcs qudt_ucumCode  
    string qudt_ucumCode  
    uri qudt_derivedUnitOfSystem  
    uri qudt_qkdvNumerator  
    string qudt_siUnitsExpression  
    uri qudt_definedUnitOfSystem  
    decimal qudt_factorUnitScalar  
    uri qudt_derivedCoherentUnitOfSystem  
    decimal qudt_conversionOffset  
    uri qudt_qkdvDenominator  
    qudt_LatexString qudt_latexSymbol  
    string qudt_altSymbol  
    boolean qudt_deprecated  
}
QudtPrefix {

}
QudtQuantifiable {

}
QudtQuantity {

}
QudtQuantityKind {

}
QudtQuantityKindDimensionVector {

}
QudtQuantityKindDimensionVectorCGS {

}
QudtQuantityKindDimensionVectorCGS-EMU {

}
QudtQuantityKindDimensionVectorCGS-ESU {

}
QudtQuantityKindDimensionVectorCGS-GAUSS {

}
QudtQuantityKindDimensionVectorCGS-LH {

}
QudtQuantityKindDimensionVectorISO {

}
QudtQuantityKindDimensionVectorImperial {

}
QudtQuantityKindDimensionVectorSI {

}
QudtQuantityType {

}
QudtQuantityValue {

}
QudtRatioScale {

}
QudtRule {

}
QudtRuleType {

}
QudtScalarDatatype {

}
QudtScale {

}
QudtScaleType {

}
QudtSignednessType {
    string rdfs_label  
    string dtype_literal  
}
QudtSolidAngleUnit {
    string rdfs_label  
    uri qudt_hasDimensionVector  
    uri qudt_hasQuantityKind  
    uri qudt_dbpediaMatch  
    string qudt_iec61360Code  
    decimal qudt_conversionMultiplierSN  
    double qudt_conversionMultiplierSN  
    string dct_description  
    string qudt_symbol  
    string qudt_udunitsCode  
    uri qudt_informativeReference  
    uri qudt_applicableSystem  
    decimal qudt_conversionMultiplier  
    string qudt_uneceCommonCode  
    uri qudt_omUnit  
    uri rdfs_seeAlso  
    uri qudt_isoNormativeReference  
    string vaem_todo  
    qudt_LatexString qudt_latexDefinition  
    uri qudt_siExactMatch  
    qudt_LatexString qudt_expression  
    string qudt_expression  
    string qudt_plainTextDescription  
    double qudt_conversionOffsetSN  
    string rdfs_comment  
    qudt_UCUMcs qudt_ucumCode  
    string qudt_ucumCode  
    uri qudt_derivedUnitOfSystem  
    uri qudt_qkdvNumerator  
    string qudt_siUnitsExpression  
    uri qudt_definedUnitOfSystem  
    decimal qudt_factorUnitScalar  
    uri qudt_derivedCoherentUnitOfSystem  
    decimal qudt_conversionOffset  
    uri qudt_qkdvDenominator  
    qudt_LatexString qudt_latexSymbol  
    string qudt_altSymbol  
    boolean qudt_deprecated  
}
QudtStatement {

}
QudtStringEncodingType {

}
QudtSymbol {

}
QudtSystemOfQuantityKinds {

}
QudtSystemOfUnits {

}
QudtTransformType {

}
QudtUnit {
    uri qudt_omUnit  
    uri rdfs_seeAlso  
    uri qudt_isoNormativeReference  
    string vaem_todo  
    uri qudt_dbpediaMatch  
    qudt_LatexString qudt_latexDefinition  
    uri qudt_siExactMatch  
    qudt_LatexString qudt_expression  
    string qudt_expression  
    uri qudt_hasQuantityKind  
    string qudt_iec61360Code  
    string qudt_plainTextDescription  
    double qudt_conversionOffsetSN  
    string qudt_udunitsCode  
    string rdfs_comment  
    uri qudt_applicableSystem  
    qudt_UCUMcs qudt_ucumCode  
    string qudt_ucumCode  
    decimal qudt_conversionMultiplier  
    uri qudt_derivedUnitOfSystem  
    uri qudt_qkdvNumerator  
    string qudt_siUnitsExpression  
    uri qudt_definedUnitOfSystem  
    decimal qudt_factorUnitScalar  
    uri qudt_informativeReference  
    string qudt_uneceCommonCode  
    string rdfs_label  
    uri qudt_hasDimensionVector  
    decimal qudt_conversionMultiplierSN  
    double qudt_conversionMultiplierSN  
    uri qudt_derivedCoherentUnitOfSystem  
    decimal qudt_conversionOffset  
    uri qudt_qkdvDenominator  
    string dct_description  
    string qudt_symbol  
    qudt_LatexString qudt_latexSymbol  
    string qudt_altSymbol  
    boolean qudt_deprecated  
}
QudtUserQuantityKind {

}
QudtVerifiable {

}
XsdString {

}
Sdos3DModel {

}
SdosAMRadioChannel {

}
SdosAPIReference {

}
SdosAboutPage {

}
SdosAcceptAction {

}
SdosAccommodation {

}
SdosAccountingService {

}
SdosAchieveAction {

}
SdosAction {

}
SdosActionAccessSpecification {

}
SdosActionStatusType {
    string rdfs_comment  
    string rdfs_label  
}
SdosActivateAction {

}
SdosAddAction {

}
SdosAdministrativeArea {

}
SdosAdultEntertainment {

}
SdosAdultOrientedEnumeration {
    string rdfs_comment  
    string rdfs_label  
    uri sdos_source  
    uri sdos_isPartOf  
}
SdosAdvertiserContentArticle {

}
SdosAggregateOffer {

}
SdosAggregateRating {

}
SdosAgreeAction {

}
SdosAirline {

}
SdosAirport {

}
SdosAlignmentObject {

}
SdosAllocateAction {

}
SdosAmpStory {

}
SdosAmusementPark {

}
SdosAnalysisNewsArticle {

}
SdosAnatomicalStructure {

}
SdosAnatomicalSystem {

}
SdosAnimalShelter {

}
SdosAnswer {

}
SdosApartment {

}
SdosApartmentComplex {

}
SdosAppendAction {

}
SdosApplyAction {

}
SdosApprovedIndication {

}
SdosAquarium {

}
SdosArchiveComponent {

}
SdosArchiveOrganization {

}
SdosArriveAction {

}
SdosArtGallery {

}
SdosArtery {

}
SdosArticle {

}
SdosAskAction {

}
SdosAskPublicNewsArticle {

}
SdosAssessAction {

}
SdosAssignAction {

}
SdosAtlas {

}
SdosAttorney {

}
SdosAudience {

}
SdosAudioObject {

}
SdosAudioObjectSnapshot {

}
SdosAudiobook {

}
SdosAuthorizeAction {

}
SdosAutoBodyShop {

}
SdosAutoDealer {

}
SdosAutoPartsStore {

}
SdosAutoRental {

}
SdosAutoRepair {

}
SdosAutoWash {

}
SdosAutomatedTeller {

}
SdosAutomotiveBusiness {

}
SdosBackgroundNewsArticle {

}
SdosBakery {

}
SdosBankAccount {

}
SdosBankOrCreditUnion {

}
SdosBarOrPub {

}
SdosBarcode {

}
SdosBeach {

}
SdosBeautySalon {

}
SdosBedAndBreakfast {

}
SdosBedDetails {

}
SdosBedType {

}
SdosBefriendAction {

}
SdosBikeStore {

}
SdosBioChemEntity {

}
SdosBlog {

}
SdosBlogPosting {

}
SdosBloodTest {

}
SdosBoardingPolicyType {
    string rdfs_comment  
    string rdfs_label  
}
SdosBoatReservation {

}
SdosBoatTerminal {

}
SdosBoatTrip {

}
SdosBodyMeasurementTypeEnumeration {
    string rdfs_comment  
    string rdfs_label  
    uri sdos_source  
    uri sdos_isPartOf  
}
SdosBodyOfWater {

}
SdosBone {

}
SdosBook {

}
SdosBookFormatType {
    string rdfs_comment  
    string rdfs_label  
    uri sdos_isPartOf  
}
SdosBookSeries {

}
SdosBookStore {

}
SdosBookmarkAction {

}
SdosBoolean {
    string rdfs_comment  
    string rdfs_label  
}
SdosBorrowAction {

}
SdosBowlingAlley {

}
SdosBrainStructure {

}
SdosBrand {

}
SdosBreadcrumbList {

}
SdosBrewery {

}
SdosBridge {

}
SdosBroadcastChannel {

}
SdosBroadcastEvent {

}
SdosBroadcastFrequencySpecification {

}
SdosBroadcastService {

}
SdosBrokerageAccount {

}
SdosBuddhistTemple {

}
SdosBusOrCoach {

}
SdosBusReservation {

}
SdosBusStation {

}
SdosBusStop {

}
SdosBusTrip {

}
SdosBusinessAudience {

}
SdosBusinessEntityType {

}
SdosBusinessEvent {

}
SdosBusinessFunction {

}
SdosBuyAction {

}
SdosCDCPMDRecord {

}
SdosCableOrSatelliteService {

}
SdosCafeOrCoffeeShop {

}
SdosCampground {

}
SdosCampingPitch {

}
SdosCanal {

}
SdosCancelAction {

}
SdosCar {

}
SdosCarUsageType {
    uri sdos_contributor  
    string rdfs_comment  
    string rdfs_label  
    uri sdos_isPartOf  
}
SdosCasino {

}
SdosCategoryCode {

}
SdosCategoryCodeSet {

}
SdosCatholicChurch {

}
SdosCemetery {

}
SdosCertification {

}
SdosCertificationStatusEnumeration {
    string rdfs_comment  
    string rdfs_label  
    uri sdos_source  
    uri sdos_isPartOf  
}
SdosChapter {

}
SdosCheckAction {

}
SdosCheckInAction {

}
SdosCheckOutAction {

}
SdosCheckoutPage {

}
SdosChemicalSubstance {

}
SdosChildCare {

}
SdosChildrensEvent {

}
SdosChooseAction {

}
SdosChurch {

}
SdosCity {

}
SdosCityHall {

}
SdosCivicStructure {

}
SdosClaim {

}
SdosClaimReview {

}
SdosClass {

}
SdosClip {

}
SdosClothingStore {

}
SdosCode {

}
SdosCollection {

}
SdosCollectionPage {

}
SdosCollegeOrUniversity {

}
SdosComedyClub {

}
SdosComedyEvent {

}
SdosComicCoverArt {

}
SdosComicIssue {

}
SdosComicSeries {

}
SdosComicStory {

}
SdosComment {

}
SdosCommentAction {

}
SdosCommunicateAction {

}
SdosCompleteDataFeed {

}
SdosCompoundPriceSpecification {

}
SdosComputerLanguage {

}
SdosComputerStore {

}
SdosConfirmAction {

}
SdosConsortium {

}
SdosConstraintNode {

}
SdosConsumeAction {

}
SdosContactPage {

}
SdosContactPoint {

}
SdosContactPointOption {
    string rdfs_comment  
    string rdfs_label  
}
SdosContinent {

}
SdosControlAction {

}
SdosConvenienceStore {

}
SdosConversation {

}
SdosCookAction {

}
SdosCooperative {

}
SdosCorporation {

}
SdosCorrectionComment {

}
SdosCountry {

}
SdosCourse {

}
SdosCourseInstance {

}
SdosCourthouse {

}
SdosCoverArt {

}
SdosCovidTestingFacility {

}
SdosCreateAction {

}
SdosCreativeWork {

}
SdosCreativeWorkSeason {

}
SdosCreativeWorkSeries {

}
SdosCreditCard {

}
SdosCrematorium {

}
SdosCriticReview {

}
SdosCssSelectorType {

}
SdosCurrencyConversionService {

}
SdosDDxElement {

}
SdosDanceEvent {

}
SdosDanceGroup {

}
SdosDataCatalog {

}
SdosDataDownload {

}
SdosDataFeed {

}
SdosDataFeedItem {

}
SdosDataType {
    string rdfs_comment  
    string rdfs_label  
}
SdosDataset {

}
SdosDate {

}
SdosDateTime {

}
SdosDatedMoneySpecification {

}
SdosDayOfWeek {
    uri sdos_contributor  
    string rdfs_comment  
    string rdfs_label  
    uri sdos_sameAs  
}
SdosDaySpa {

}
SdosDeactivateAction {

}
SdosDefenceEstablishment {

}
SdosDefinedRegion {

}
SdosDefinedTerm {

}
SdosDefinedTermSet {

}
SdosDeleteAction {

}
SdosDeliveryChargeSpecification {

}
SdosDeliveryEvent {

}
SdosDeliveryMethod {
    uri sdos_contributor  
    string rdfs_comment  
    string rdfs_label  
}
SdosDeliveryTimeSettings {

}
SdosDemand {

}
SdosDentist {

}
SdosDepartAction {

}
SdosDepartmentStore {

}
SdosDepositAccount {

}
SdosDiagnosticLab {

}
SdosDiagnosticProcedure {

}
SdosDiet {

}
SdosDietarySupplement {

}
SdosDigitalDocument {

}
SdosDigitalDocumentPermission {

}
SdosDigitalDocumentPermissionType {
    string rdfs_comment  
    string rdfs_label  
}
SdosDigitalPlatformEnumeration {
    string rdfs_comment  
    string rdfs_label  
    uri sdos_source  
    uri sdos_isPartOf  
}
SdosDisagreeAction {

}
SdosDiscoverAction {

}
SdosDiscussionForumPosting {

}
SdosDislikeAction {

}
SdosDistance {

}
SdosDistillery {

}
SdosDonateAction {

}
SdosDoseSchedule {

}
SdosDownloadAction {

}
SdosDrawAction {

}
SdosDrawing {

}
SdosDrinkAction {

}
SdosDriveWheelConfigurationValue {
    uri sdos_contributor  
    string rdfs_comment  
    string rdfs_label  
}
SdosDrug {

}
SdosDrugClass {

}
SdosDrugCost {

}
SdosDrugCostCategory {
    string rdfs_comment  
    string rdfs_label  
    uri sdos_isPartOf  
}
SdosDrugLegalStatus {

}
SdosDrugPregnancyCategory {
    string rdfs_comment  
    string rdfs_label  
    uri sdos_isPartOf  
}
SdosDrugPrescriptionStatus {
    string rdfs_comment  
    string rdfs_label  
    uri sdos_isPartOf  
}
SdosDrugStrength {

}
SdosDryCleaningOrLaundry {

}
SdosDuration {

}
SdosEUEnergyEfficiencyEnumeration {
    string rdfs_comment  
    string rdfs_label  
    uri sdos_source  
    uri sdos_isPartOf  
}
SdosEatAction {

}
SdosEducationEvent {

}
SdosEducationalAudience {

}
SdosEducationalOccupationalCredential {

}
SdosEducationalOccupationalProgram {

}
SdosEducationalOrganization {

}
SdosElectrician {

}
SdosElectronicsStore {

}
SdosElementarySchool {

}
SdosEmailMessage {

}
SdosEmbassy {

}
SdosEmergencyService {

}
SdosEmployeeRole {

}
SdosEmployerAggregateRating {

}
SdosEmployerReview {

}
SdosEmploymentAgency {

}
SdosEndorseAction {

}
SdosEndorsementRating {

}
SdosEnergy {

}
SdosEnergyConsumptionDetails {

}
SdosEnergyEfficiencyEnumeration {

}
SdosEnergyStarEnergyEfficiencyEnumeration {
    string rdfs_comment  
    string rdfs_label  
    uri sdos_source  
    uri sdos_isPartOf  
}
SdosEngineSpecification {

}
SdosEntertainmentBusiness {

}
SdosEntryPoint {

}
SdosEnumeration {

}
SdosEpisode {

}
SdosEvent {

}
SdosEventAttendanceModeEnumeration {
    string rdfs_comment  
    string rdfs_label  
    uri sdos_source  
    uri sdos_isPartOf  
}
SdosEventReservation {

}
SdosEventSeries {

}
SdosEventStatusType {
    string rdfs_comment  
    string rdfs_label  
}
SdosEventVenue {

}
SdosExchangeRateSpecification {

}
SdosExerciseAction {

}
SdosExerciseGym {

}
SdosExercisePlan {

}
SdosExhibitionEvent {

}
SdosFAQPage {

}
SdosFMRadioChannel {

}
SdosFastFoodRestaurant {

}
SdosFestival {

}
SdosFilmAction {

}
SdosFinancialIncentive {

}
SdosFinancialProduct {

}
SdosFinancialService {

}
SdosFindAction {

}
SdosFireStation {

}
SdosFlight {

}
SdosFlightReservation {

}
SdosFloat {

}
SdosFloorPlan {

}
SdosFlorist {

}
SdosFollowAction {

}
SdosFoodEstablishment {

}
SdosFoodEstablishmentReservation {

}
SdosFoodEvent {

}
SdosFoodService {

}
SdosFulfillmentTypeEnumeration {
    string rdfs_comment  
    string rdfs_label  
    uri sdos_source  
    uri sdos_isPartOf  
}
SdosFundingAgency {

}
SdosFundingScheme {

}
SdosFurnitureStore {

}
SdosGame {

}
SdosGameAvailabilityEnumeration {
    string rdfs_comment  
    string rdfs_label  
    uri sdos_source  
    uri sdos_isPartOf  
}
SdosGamePlayMode {
    string rdfs_comment  
    string rdfs_label  
}
SdosGameServer {

}
SdosGameServerStatus {
    string rdfs_comment  
    string rdfs_label  
}
SdosGardenStore {

}
SdosGasStation {

}
SdosGatedResidenceCommunity {

}
SdosGenderType {
    string rdfs_comment  
    string rdfs_label  
}
SdosGene {

}
SdosGeneralContractor {

}
SdosGeoCircle {

}
SdosGeoCoordinates {

}
SdosGeoShape {

}
SdosGeospatialGeometry {

}
SdosGiveAction {

}
SdosGolfCourse {

}
SdosGovernmentBenefitsType {
    string rdfs_comment  
    string rdfs_label  
    uri sdos_source  
    uri sdos_isPartOf  
}
SdosGovernmentBuilding {

}
SdosGovernmentOffice {

}
SdosGovernmentOrganization {

}
SdosGovernmentPermit {

}
SdosGovernmentService {

}
SdosGrant {

}
SdosGroceryStore {

}
SdosGuide {

}
SdosHVACBusiness {

}
SdosHackathon {

}
SdosHairSalon {

}
SdosHardwareStore {

}
SdosHealthAndBeautyBusiness {

}
SdosHealthAspectEnumeration {
    string rdfs_comment  
    string rdfs_label  
    uri sdos_source  
    uri sdos_isPartOf  
}
SdosHealthClub {

}
SdosHealthInsurancePlan {

}
SdosHealthPlanCostSharingSpecification {

}
SdosHealthPlanFormulary {

}
SdosHealthPlanNetwork {

}
SdosHealthTopicContent {

}
SdosHighSchool {

}
SdosHinduTemple {

}
SdosHobbyShop {

}
SdosHomeAndConstructionBusiness {

}
SdosHomeGoodsStore {

}
SdosHospital {

}
SdosHostel {

}
SdosHotel {

}
SdosHotelRoom {

}
SdosHouse {

}
SdosHousePainter {

}
SdosHowTo {

}
SdosHowToDirection {

}
SdosHowToItem {

}
SdosHowToSection {

}
SdosHowToStep {

}
SdosHowToSupply {

}
SdosHowToTip {

}
SdosHowToTool {

}
SdosHyperToc {

}
SdosHyperTocEntry {

}
SdosIPTCDigitalSourceEnumeration {
    string rdfs_label  
    uri sdos_source  
    uri sdos_isPartOf  
    string rdfs_comment  
}
SdosIceCreamShop {

}
SdosIgnoreAction {

}
SdosImageGallery {

}
SdosImageObject {

}
SdosImageObjectSnapshot {

}
SdosImagingTest {

}
SdosIncentiveQualifiedExpenseType {
    string rdfs_comment  
    string rdfs_label  
    uri sdos_source  
    uri sdos_isPartOf  
}
SdosIncentiveStatus {
    string rdfs_comment  
    string rdfs_label  
    uri sdos_source  
    uri sdos_isPartOf  
}
SdosIncentiveType {
    string rdfs_comment  
    string rdfs_label  
    uri sdos_source  
    uri sdos_isPartOf  
}
SdosIndividualPhysician {

}
SdosIndividualProduct {

}
SdosInfectiousAgentClass {
    string rdfs_comment  
    string rdfs_label  
    uri sdos_isPartOf  
}
SdosInfectiousDisease {

}
SdosInformAction {

}
SdosInsertAction {

}
SdosInstallAction {

}
SdosInsuranceAgency {

}
SdosIntangible {

}
SdosInteger {

}
SdosInteractAction {

}
SdosInteractionCounter {

}
SdosInternetCafe {

}
SdosInvestmentFund {

}
SdosInvestmentOrDeposit {

}
SdosInviteAction {

}
SdosInvoice {

}
SdosItemAvailability {
    string rdfs_comment  
    string rdfs_label  
}
SdosItemList {

}
SdosItemListOrderType {
    string rdfs_comment  
    string rdfs_label  
}
SdosItemPage {

}
SdosJewelryStore {

}
SdosJobPosting {

}
SdosJoinAction {

}
SdosJoint {

}
SdosLakeBodyOfWater {

}
SdosLandform {

}
SdosLandmarksOrHistoricalBuildings {

}
SdosLanguage {

}
SdosLearningResource {

}
SdosLeaveAction {

}
SdosLegalForceStatus {
    string rdfs_label  
    uri sdos_source  
    uri sdos_isPartOf  
    uri sdos_contributor  
    string rdfs_comment  
}
SdosLegalService {

}
SdosLegalValueLevel {
    string rdfs_label  
    uri sdos_source  
    uri sdos_isPartOf  
    uri sdos_contributor  
    string rdfs_comment  
}
SdosLegislation {

}
SdosLegislationObject {

}
SdosLegislativeBuilding {

}
SdosLendAction {

}
SdosLibrary {

}
SdosLibrarySystem {

}
SdosLifestyleModification {

}
SdosLigament {

}
SdosLikeAction {

}
SdosLinkRole {

}
SdosLiquorStore {

}
SdosListItem {

}
SdosListenAction {

}
SdosLiteraryEvent {

}
SdosLiveBlogPosting {

}
SdosLoanOrCredit {

}
SdosLocalBusiness {

}
SdosLocationFeatureSpecification {

}
SdosLocksmith {

}
SdosLodgingBusiness {

}
SdosLodgingReservation {

}
SdosLoseAction {

}
SdosLymphaticVessel {

}
SdosManuscript {

}
SdosMap {

}
SdosMapCategoryType {
    string rdfs_comment  
    string rdfs_label  
}
SdosMarryAction {

}
SdosMass {

}
SdosMathSolver {

}
SdosMaximumDoseSchedule {

}
SdosMeasurementMethodEnum {
    string rdfs_comment  
    string rdfs_label  
    uri sdos_source  
    uri sdos_isPartOf  
}
SdosMeasurementTypeEnumeration {

}
SdosMediaEnumeration {

}
SdosMediaGallery {

}
SdosMediaManipulationRatingEnumeration {
    string rdfs_comment  
    string rdfs_label  
    uri sdos_source  
    uri sdos_isPartOf  
}
SdosMediaObject {

}
SdosMediaReview {

}
SdosMediaReviewItem {

}
SdosMediaSubscription {

}
SdosMedicalAudience {

}
SdosMedicalAudienceType {
    string rdfs_comment  
    string rdfs_label  
    uri sdos_isPartOf  
}
SdosMedicalBusiness {

}
SdosMedicalCause {

}
SdosMedicalClinic {

}
SdosMedicalCode {

}
SdosMedicalCondition {

}
SdosMedicalConditionStage {

}
SdosMedicalContraindication {

}
SdosMedicalDevice {

}
SdosMedicalDevicePurpose {
    string rdfs_comment  
    string rdfs_label  
    uri sdos_isPartOf  
}
SdosMedicalEntity {

}
SdosMedicalEnumeration {

}
SdosMedicalEvidenceLevel {
    string rdfs_comment  
    string rdfs_label  
    uri sdos_isPartOf  
}
SdosMedicalGuideline {

}
SdosMedicalGuidelineContraindication {

}
SdosMedicalGuidelineRecommendation {

}
SdosMedicalImagingTechnique {
    string rdfs_comment  
    string rdfs_label  
    uri sdos_isPartOf  
}
SdosMedicalIndication {

}
SdosMedicalIntangible {

}
SdosMedicalObservationalStudy {

}
SdosMedicalObservationalStudyDesign {
    string rdfs_comment  
    string rdfs_label  
    uri sdos_isPartOf  
}
SdosMedicalOrganization {

}
SdosMedicalProcedure {

}
SdosMedicalProcedureType {
    string rdfs_comment  
    string rdfs_label  
    uri sdos_isPartOf  
}
SdosMedicalRiskCalculator {

}
SdosMedicalRiskEstimator {

}
SdosMedicalRiskFactor {

}
SdosMedicalRiskScore {

}
SdosMedicalScholarlyArticle {

}
SdosMedicalSign {

}
SdosMedicalSignOrSymptom {

}
SdosMedicalSpecialty {
    string rdfs_label  
    uri sdos_isPartOf  
    string rdfs_comment  
}
SdosMedicalStudy {

}
SdosMedicalStudyStatus {
    string rdfs_comment  
    string rdfs_label  
    uri sdos_isPartOf  
}
SdosMedicalSymptom {

}
SdosMedicalTest {

}
SdosMedicalTestPanel {

}
SdosMedicalTherapy {

}
SdosMedicalTrial {

}
SdosMedicalTrialDesign {
    string rdfs_comment  
    string rdfs_label  
    uri sdos_isPartOf  
}
SdosMedicalWebPage {

}
SdosMedicineSystem {
    string rdfs_comment  
    string rdfs_label  
    uri sdos_isPartOf  
}
SdosMeetingRoom {

}
SdosMemberProgram {

}
SdosMemberProgramTier {

}
SdosMensClothingStore {

}
SdosMenu {

}
SdosMenuItem {

}
SdosMenuSection {

}
SdosMerchantReturnEnumeration {
    string rdfs_comment  
    string rdfs_label  
    uri sdos_source  
    uri sdos_isPartOf  
}
SdosMerchantReturnPolicy {

}
SdosMerchantReturnPolicySeasonalOverride {

}
SdosMessage {

}
SdosMiddleSchool {

}
SdosMobileApplication {

}
SdosMobilePhoneStore {

}
SdosMolecularEntity {

}
SdosMonetaryAmount {

}
SdosMonetaryAmountDistribution {

}
SdosMonetaryGrant {

}
SdosMoneyTransfer {

}
SdosMortgageLoan {

}
SdosMosque {

}
SdosMotel {

}
SdosMotorcycle {

}
SdosMotorcycleDealer {

}
SdosMotorcycleRepair {

}
SdosMotorizedBicycle {

}
SdosMountain {

}
SdosMoveAction {

}
SdosMovie {

}
SdosMovieClip {

}
SdosMovieRentalStore {

}
SdosMovieSeries {

}
SdosMovieTheater {

}
SdosMovingCompany {

}
SdosMuscle {

}
SdosMuseum {

}
SdosMusicAlbum {

}
SdosMusicAlbumProductionType {
    uri sdos_contributor  
    string rdfs_comment  
    string rdfs_label  
}
SdosMusicAlbumReleaseType {
    uri sdos_contributor  
    string rdfs_comment  
    string rdfs_label  
}
SdosMusicComposition {

}
SdosMusicEvent {

}
SdosMusicGroup {

}
SdosMusicPlaylist {

}
SdosMusicRecording {

}
SdosMusicRelease {

}
SdosMusicReleaseFormatType {
    uri sdos_contributor  
    string rdfs_comment  
    string rdfs_label  
}
SdosMusicStore {

}
SdosMusicVenue {

}
SdosMusicVideoObject {

}
SdosNGO {

}
SdosNLNonprofitType {
    string rdfs_comment  
    string rdfs_label  
    uri sdos_source  
    uri sdos_isPartOf  
}
SdosNailSalon {

}
SdosNerve {

}
SdosNewsArticle {

}
SdosNewsMediaOrganization {

}
SdosNewspaper {

}
SdosNightClub {

}
SdosNonprofitType {

}
SdosNotary {

}
SdosNoteDigitalDocument {

}
SdosNumber {

}
SdosNutritionInformation {

}
SdosObservation {

}
SdosOccupation {

}
SdosOccupationalExperienceRequirements {

}
SdosOccupationalTherapy {

}
SdosOceanBodyOfWater {

}
SdosOffer {

}
SdosOfferCatalog {

}
SdosOfferForLease {

}
SdosOfferForPurchase {

}
SdosOfferItemCondition {
    string rdfs_comment  
    string rdfs_label  
}
SdosOfferShippingDetails {

}
SdosOfficeEquipmentStore {

}
SdosOnDemandEvent {

}
SdosOnlineBusiness {

}
SdosOnlineStore {

}
SdosOpeningHoursSpecification {

}
SdosOpinionNewsArticle {

}
SdosOptician {

}
SdosOrder {

}
SdosOrderAction {

}
SdosOrderItem {

}
SdosOrderStatus {
    string rdfs_comment  
    string rdfs_label  
}
SdosOrganization {

}
SdosOrganizationRole {

}
SdosOrganizeAction {

}
SdosOutletStore {

}
SdosOwnershipInfo {

}
SdosPaintAction {

}
SdosPainting {

}
SdosPalliativeProcedure {

}
SdosParcelDelivery {

}
SdosParentAudience {

}
SdosPark {

}
SdosParkingFacility {

}
SdosPathologyTest {

}
SdosPatient {

}
SdosPawnShop {

}
SdosPayAction {

}
SdosPaymentCard {

}
SdosPaymentChargeSpecification {

}
SdosPaymentMethod {

}
SdosPaymentMethodType {
    string rdfs_comment  
    string rdfs_label  
}
SdosPaymentService {

}
SdosPaymentStatusType {
    string rdfs_comment  
    string rdfs_label  
}
SdosPeopleAudience {

}
SdosPerformAction {

}
SdosPerformanceRole {

}
SdosPerformingArtsTheater {

}
SdosPerformingGroup {

}
SdosPeriodical {

}
SdosPermit {

}
SdosPerson {

}
SdosPetStore {

}
SdosPharmacy {

}
SdosPhotograph {

}
SdosPhotographAction {

}
SdosPhysicalActivity {

}
SdosPhysicalActivityCategory {
    string rdfs_comment  
    string rdfs_label  
    uri sdos_isPartOf  
}
SdosPhysicalExam {
    string rdfs_comment  
    string rdfs_label  
    uri sdos_isPartOf  
}
SdosPhysicalTherapy {

}
SdosPhysician {

}
SdosPhysiciansOffice {

}
SdosPlace {

}
SdosPlaceOfWorship {

}
SdosPlanAction {

}
SdosPlay {

}
SdosPlayAction {

}
SdosPlayGameAction {

}
SdosPlayground {

}
SdosPlumber {

}
SdosPodcastEpisode {

}
SdosPodcastSeason {

}
SdosPodcastSeries {

}
SdosPoliceStation {

}
SdosPoliticalParty {

}
SdosPond {

}
SdosPostOffice {

}
SdosPostalAddress {

}
SdosPostalCodeRangeSpecification {

}
SdosPoster {

}
SdosPreOrderAction {

}
SdosPrependAction {

}
SdosPreschool {

}
SdosPresentationDigitalDocument {

}
SdosPreventionIndication {

}
SdosPriceComponentTypeEnumeration {
    string rdfs_comment  
    string rdfs_label  
    uri sdos_source  
    uri sdos_isPartOf  
}
SdosPriceSpecification {

}
SdosPriceTypeEnumeration {
    string rdfs_comment  
    string rdfs_label  
    uri sdos_source  
    uri sdos_isPartOf  
}
SdosProduct {

}
SdosProductCollection {

}
SdosProductGroup {

}
SdosProductModel {

}
SdosProductReturnEnumeration {
    string rdfs_label  
    uri sdos_source  
    uri sdos_isPartOf  
    string rdfs_comment  
}
SdosProductReturnPolicy {

}
SdosProfessionalService {

}
SdosProfilePage {

}
SdosProgramMembership {

}
SdosProject {

}
SdosPronounceableText {

}
SdosProperty {

}
SdosPropertyValue {

}
SdosPropertyValueSpecification {

}
SdosProtein {

}
SdosPsychologicalTreatment {

}
SdosPublicSwimmingPool {

}
SdosPublicToilet {

}
SdosPublicationEvent {

}
SdosPublicationIssue {

}
SdosPublicationVolume {

}
SdosPurchaseType {
    string rdfs_comment  
    string rdfs_label  
    uri sdos_source  
    uri sdos_isPartOf  
}
SdosQAPage {

}
SdosQualitativeValue {

}
SdosQuantitativeValue {

}
SdosQuantitativeValueDistribution {

}
SdosQuantity {

}
SdosQuestion {

}
SdosQuiz {

}
SdosQuotation {

}
SdosQuoteAction {

}
SdosRVPark {

}
SdosRadiationTherapy {

}
SdosRadioBroadcastService {

}
SdosRadioChannel {

}
SdosRadioClip {

}
SdosRadioEpisode {

}
SdosRadioSeason {

}
SdosRadioSeries {

}
SdosRadioStation {

}
SdosRating {

}
SdosReactAction {

}
SdosReadAction {

}
SdosRealEstateAgent {

}
SdosRealEstateListing {

}
SdosReceiveAction {

}
SdosRecipe {

}
SdosRecommendation {

}
SdosRecommendedDoseSchedule {

}
SdosRecyclingCenter {

}
SdosRefundTypeEnumeration {
    string rdfs_comment  
    string rdfs_label  
    uri sdos_source  
    uri sdos_isPartOf  
}
SdosRegisterAction {

}
SdosRejectAction {

}
SdosRentAction {

}
SdosRentalCarReservation {

}
SdosRepaymentSpecification {

}
SdosReplaceAction {

}
SdosReplyAction {

}
SdosReport {

}
SdosReportageNewsArticle {

}
SdosReportedDoseSchedule {

}
SdosResearchOrganization {

}
SdosResearchProject {

}
SdosResearcher {

}
SdosReservation {

}
SdosReservationPackage {

}
SdosReservationStatusType {
    string rdfs_comment  
    string rdfs_label  
}
SdosReserveAction {

}
SdosReservoir {

}
SdosResidence {

}
SdosResort {

}
SdosRestaurant {

}
SdosRestrictedDiet {
    string rdfs_comment  
    string rdfs_label  
}
SdosResumeAction {

}
SdosReturnAction {

}
SdosReturnFeesEnumeration {
    string rdfs_comment  
    string rdfs_label  
    uri sdos_source  
    uri sdos_isPartOf  
}
SdosReturnLabelSourceEnumeration {
    string rdfs_comment  
    string rdfs_label  
    uri sdos_source  
    uri sdos_isPartOf  
}
SdosReturnMethodEnumeration {
    string rdfs_comment  
    string rdfs_label  
    uri sdos_source  
    uri sdos_isPartOf  
}
SdosReview {

}
SdosReviewAction {

}
SdosReviewNewsArticle {

}
SdosRiverBodyOfWater {

}
SdosRole {

}
SdosRoofingContractor {

}
SdosRoom {

}
SdosRsvpAction {

}
SdosRsvpResponseType {
    string rdfs_comment  
    string rdfs_label  
}
SdosSaleEvent {

}
SdosSatiricalArticle {

}
SdosSchedule {

}
SdosScheduleAction {

}
SdosScholarlyArticle {

}
SdosSchool {

}
SdosSchoolDistrict {

}
SdosScreeningEvent {

}
SdosSculpture {

}
SdosSeaBodyOfWater {

}
SdosSearchAction {

}
SdosSearchRescueOrganization {

}
SdosSearchResultsPage {

}
SdosSeason {

}
SdosSeat {

}
SdosSeekToAction {

}
SdosSelfStorage {

}
SdosSellAction {

}
SdosSendAction {

}
SdosSeries {

}
SdosService {

}
SdosServiceChannel {

}
SdosServicePeriod {

}
SdosShareAction {

}
SdosSheetMusic {

}
SdosShippingConditions {

}
SdosShippingDeliveryTime {

}
SdosShippingRateSettings {

}
SdosShippingService {

}
SdosShoeStore {

}
SdosShoppingCenter {

}
SdosShortStory {

}
SdosSingleFamilyResidence {

}
SdosSiteNavigationElement {

}
SdosSizeGroupEnumeration {

}
SdosSizeSpecification {

}
SdosSizeSystemEnumeration {
    string rdfs_comment  
    string rdfs_label  
    uri sdos_source  
    uri sdos_isPartOf  
}
SdosSkiResort {

}
SdosSocialEvent {

}
SdosSocialMediaPosting {

}
SdosSoftwareApplication {

}
SdosSoftwareSourceCode {

}
SdosSolveMathAction {

}
SdosSomeProducts {

}
SdosSpeakableSpecification {

}
SdosSpecialAnnouncement {

}
SdosSpecialty {

}
SdosSportingGoodsStore {

}
SdosSportsActivityLocation {

}
SdosSportsClub {

}
SdosSportsEvent {

}
SdosSportsOrganization {

}
SdosSportsTeam {

}
SdosSpreadsheetDigitalDocument {

}
SdosStadiumOrArena {

}
SdosState {

}
SdosStatement {

}
SdosStatisticalPopulation {

}
SdosStatisticalVariable {

}
SdosStatusEnumeration {

}
SdosSteeringPositionValue {
    uri sdos_contributor  
    string rdfs_comment  
    string rdfs_label  
}
SdosStore {

}
SdosStructuredValue {

}
SdosStupidType {

}
SdosSubscribeAction {

}
SdosSubstance {

}
SdosSubwayStation {

}
SdosSuite {

}
SdosSuperficialAnatomy {

}
SdosSurgicalProcedure {

}
SdosSuspendAction {

}
SdosSyllabus {

}
SdosSynagogue {

}
SdosTVClip {

}
SdosTVEpisode {

}
SdosTVSeason {

}
SdosTVSeries {

}
SdosTable {

}
SdosTakeAction {

}
SdosTattooParlor {

}
SdosTaxi {

}
SdosTaxiReservation {

}
SdosTaxiService {

}
SdosTaxiStand {

}
SdosTaxon {

}
SdosTechArticle {

}
SdosTelevisionChannel {

}
SdosTelevisionStation {

}
SdosTennisComplex {

}
SdosText {

}
SdosTextDigitalDocument {

}
SdosTextObject {

}
SdosTheaterEvent {

}
SdosTheaterGroup {

}
SdosTherapeuticProcedure {

}
SdosThesis {

}
SdosThing {

}
SdosTicket {

}
SdosTieAction {

}
SdosTierBenefitEnumeration {
    string rdfs_comment  
    string rdfs_label  
    uri sdos_source  
    uri sdos_isPartOf  
}
SdosTime {

}
SdosTipAction {

}
SdosTireShop {

}
SdosTouristAttraction {

}
SdosTouristDestination {

}
SdosTouristInformationCenter {

}
SdosTouristTrip {

}
SdosToyStore {

}
SdosTrackAction {

}
SdosTradeAction {

}
SdosTrainReservation {

}
SdosTrainStation {

}
SdosTrainTrip {

}
SdosTransferAction {

}
SdosTravelAction {

}
SdosTravelAgency {

}
SdosTreatmentIndication {

}
SdosTrip {

}
SdosTypeAndQuantityNode {

}
SdosUKNonprofitType {
    string rdfs_comment  
    string rdfs_label  
    uri sdos_source  
    uri sdos_isPartOf  
}
SdosURL {

}
SdosUSNonprofitType {
    string rdfs_comment  
    string rdfs_label  
    uri sdos_source  
    uri sdos_isPartOf  
}
SdosUnRegisterAction {

}
SdosUnitPriceSpecification {

}
SdosUpdateAction {

}
SdosUseAction {

}
SdosUserBlocks {

}
SdosUserCheckins {

}
SdosUserComments {

}
SdosUserDownloads {

}
SdosUserInteraction {

}
SdosUserLikes {

}
SdosUserPageVisits {

}
SdosUserPlays {

}
SdosUserPlusOnes {

}
SdosUserReview {

}
SdosUserTweets {

}
SdosVacationRental {

}
SdosVehicle {

}
SdosVein {

}
SdosVessel {

}
SdosVeterinaryCare {

}
SdosVideoGallery {

}
SdosVideoGame {

}
SdosVideoGameClip {

}
SdosVideoGameSeries {

}
SdosVideoObject {

}
SdosVideoObjectSnapshot {

}
SdosViewAction {

}
SdosVirtualLocation {

}
SdosVisualArtsEvent {

}
SdosVisualArtwork {

}
SdosVitalSign {

}
SdosVolcano {

}
SdosVoteAction {

}
SdosWPAdBlock {

}
SdosWPFooter {

}
SdosWPHeader {

}
SdosWPSideBar {

}
SdosWantAction {

}
SdosWarrantyPromise {

}
SdosWarrantyScope {

}
SdosWatchAction {

}
SdosWaterfall {

}
SdosWearAction {

}
SdosWearableMeasurementTypeEnumeration {
    string rdfs_comment  
    string rdfs_label  
    uri sdos_source  
    uri sdos_isPartOf  
}
SdosWearableSizeGroupEnumeration {
    string rdfs_comment  
    string rdfs_label  
    uri sdos_source  
    uri sdos_isPartOf  
}
SdosWearableSizeSystemEnumeration {
    string rdfs_comment  
    string rdfs_label  
    uri sdos_source  
    uri sdos_isPartOf  
}
SdosWebAPI {

}
SdosWebApplication {

}
SdosWebContent {

}
SdosWebPage {

}
SdosWebPageElement {

}
SdosWebSite {

}
SdosWholesaleStore {

}
SdosWinAction {

}
SdosWinery {

}
SdosWorkBasedProgram {

}
SdosWorkersUnion {

}
SdosWriteAction {

}
SdosXPathType {

}
SdosZoo {

}
GeoFeature {

}
GeoFeatureCollection {

}
GeoGeometry {

}
GeoGeometryCollection {

}
GeoSpatialObject {

}
GeoSpatialObjectCollection {

}
SfCurve {

}
SfEnvelope {

}
SfGeometry {

}
SfGeometryCollection {

}
SfLine {

}
SfLineString {

}
SfLinearRing {

}
SfMultiCurve {

}
SfMultiLineString {

}
SfMultiPoint {

}
SfMultiPolygon {

}
SfMultiSurface {

}
SfPoint {

}
SfPolygon {

}
SfPolyhedralSurface {

}
SfSurface {

}
SfTIN {

}
SfTriangle {

}
ProvAccept {

}
ProvActivity {

}
ProvActivityInfluence {

}
ProvAgent {

}
ProvAgentInfluence {

}
ProvAssociation {

}
ProvAttribution {

}
ProvBundle {

}
ProvCollection {

}
ProvCommunication {

}
ProvContribute {

}
ProvContributor {

}
ProvCopyright {

}
ProvCreate {

}
ProvCreator {

}
ProvDelegation {

}
ProvDerivation {

}
ProvDictionary {

}
ProvDirectQueryService {

}
ProvEmptyCollection {

}
ProvEmptyDictionary {

}
ProvEnd {

}
ProvEntity {

}
ProvEntityInfluence {

}
ProvGeneration {

}
ProvInfluence {

}
ProvInsertion {

}
ProvInstantaneousEvent {

}
ProvInvalidation {

}
ProvKeyEntityPair {

}
ProvLocation {

}
ProvModify {

}
ProvOrganization {

}
ProvPerson {

}
ProvPlan {

}
ProvPrimarySource {

}
ProvPublish {

}
ProvPublisher {

}
ProvQuotation {

}
ProvRemoval {

}
ProvReplace {

}
ProvRevision {

}
ProvRightsAssignment {

}
ProvRightsHolder {

}
ProvRole {

}
ProvServiceDescription {

}
ProvSoftwareAgent {

}
ProvStart {

}
ProvSubmit {

}
ProvUsage {

}
DtypeCodeList {

}
DtypeCompositeCodeList {

}
DtypeDerivedCodeList {

}
DtypeEnumeratedValue {

}
DtypeEnumeration {

}
DtypeSimpleCodeList {

}
DtypeValueReference {

}
XsdAnySimpleType {

}
VaemAspect {

}
VaemDimension {

}
VaemDiscipline {

}
VaemDomain {

}
VaemGraphMetaData {
    uri vaem_namespace  
    string dct_title  
    string vaem_withAttributionTo  
    uri vaem_latestPublishedVersion  
    uri vaem_usesNonImportedResource  
    uri vaem_turtleFileURL  
    string vaem_owner  
    string vaem_revision  
    uri vaem_rdfxmlFileURL  
    string vaem_intent  
    string vaem_namespacePrefix  
    string rdfs_label  
    string vaem_title  
    string vaem_description  
    uri vaem_previousPublishedVersion  
    uri vaem_logo  
    string vaem_name  
    date dct_modified  
}
VaemGraphRole {
    string rdfs_label  
    string vaem_filePrefix  
    string dct_description  
}
VaemParty {
    string rdfs_label  
    uri vaem_url  
    string vaem_name  
}
VaemViewpoint {

}
TimeDateTimeDescription {

}
TimeDateTimeInterval {

}
TimeDayOfWeek {
    string rdfs_label  
}
TimeDuration {

}
TimeDurationDescription {

}
TimeGeneralDateTimeDescription {

}
TimeGeneralDurationDescription {

}
TimeInstant {

}
TimeInterval {

}
TimeJanuary {

}
TimeMonthOfYear {

}
TimeProperInterval {

}
TimeTRS {

}
TimeTemporalDuration {

}
TimeTemporalEntity {

}
TimeTemporalPosition {

}
TimeTemporalUnit {
    decimal time_weeks  
    decimal time_months  
    decimal time_hours  
    decimal time_years  
    string rdfs_label  
    decimal time_days  
    decimal time_seconds  
    decimal time_minutes  
}
TimeTimePosition {

}
TimeTimeZone {

}
TimeYear {

}
XsdDateTimeStamp {

}
XsdDuration {

}
XsdGYear {

}
XsdGYearMonth {

}
FoafGroup {

}
FoafImage {

}
FoafLabelProperty {

}
FoafOnlineAccount {

}
FoafOnlineChatAccount {

}
FoafOnlineEcommerceAccount {

}
FoafOnlineGamingAccount {

}
FoafOrganization {

}
FoafPerson {

}
FoafPersonalProfileDocument {

}
FoafProject {

}
FoafAgent {

}
FoafDocument {

}
Wn16Credential {

}
Wn16Endorsement-4 {

}
Wn16Event {

}
WotEncryptedDocument {

}
WotEndorsement {

}
WotPubKey {

}
WotSigEvent {

}
WotUser {

}
WgsPoint {

}
WgsSpatialThing {

}
IcalDomainOfRrule {

}
IcalListOfFloat {

}
IcalValarm {

}
IcalValueCAL-ADDRESS {

}
IcalValueDATE {

}
IcalValueDATE-TIME {

}
IcalValueDURATION {

}
IcalValuePERIOD {

}
IcalValueRECUR {

}
IcalVevent {

}
IcalVfreebusy {

}
IcalVjournal {

}
IcalVtimezone {

}
IcalVtodo {

}
AdmsAsset {

}
AdmsAssetDistribution {

}
AdmsAssetRepository {

}
AdmsIdentifier {

}
DcatCatalog {

}
DcatDataset {

}
DcatDistribution {

}
AdmsSemanticAssetDistribution {
    string adms_accessURL  
}
RdfDatatypeProperty {
    string rdfs_comment  
    string rdfs_label  
}
VoidDataset {

}
VoidDatasetDescription {

}
VoidLinkset {

}
VoidTechnicalFeature {

}
VaemCatalogEntry {
    string rdfs_label  
}
VaemDateUnion {

}
VoagAccredidation {

}
VoagAdministrativeEvent {

}
VoagApprovalEvent {

}
VoagApprovalProcess {

}
VoagAssignedRole {

}
VoagAttribution {
    string rdfs_label  
    string voag_pointOfContact  
    string vaem_name  
    uri voag_url  
}
VoagAttributionLogo {
    string voag_width  
    string voag_height  
    string vaem_description  
    string rdfs_label  
    uri voag_image  
    string voag_caption  
}
VoagCatalog {

}
VoagChangeFrequency {
    string rdfs_label  
}
VoagChangeManagementProcess {

}
VoagChangeType {
    string rdfs_label  
}
VoagConcurrenceEvent {

}
VoagConfidentialityLevel {
    string vaem_description  
    string rdfs_label  
    integer dtype_order  
}
VoagCreativeCommonsJurisdiction {

}
VoagCreativeCommonsPermission {
    string vaem_description  
    string rdfs_label  
}
VoagCreativeCommonsProhibition {
    string vaem_description  
    string rdfs_label  
}
VoagCreativeCommonsRequirement {
    uri vaem_url  
    string vaem_description  
    string rdfs_label  
}
VoagCreativeCommonsWork {

}
VoagDeletionEvent {

}
VoagDesignatedGovernanceRole {

}
VoagDocument {

}
VoagEnumeratedValue {

}
VoagEvent {

}
VoagFigure {

}
VoagGovernance {
    string rdfs_label  
}
VoagGovernanceEvent {

}
VoagGovernanceProcess {

}
VoagGovernanceProtocol {

}
VoagGovernanceRole {
    string rdfs_label  
}
VoagGovernedObject {

}
VoagGovernedService {

}
VoagGraph {

}
VoagIcon {
    string voag_width  
    string voag_height  
    string vaem_description  
    string rdfs_label  
    uri voag_image  
    string voag_caption  
}
VoagImage {

}
VoagIssue {

}
VoagIssueResolutionProcess {

}
VoagIssueStatus {
    string vaem_description  
    string rdfs_label  
}
VoagLicenseModel {
    string rdfs_label  
}
VoagLogo {
    string voag_width  
    string voag_height  
    string vaem_description  
    string rdfs_label  
    uri voag_image  
    string voag_caption  
}
VoagMaturity {
    string rdfs_label  
}
VoagNonConcurrenceEvent {

}
VoagOrganization {

}
VoagOrganizationLogo {
    string voag_width  
    string voag_height  
    string vaem_description  
    string rdfs_label  
    uri voag_image  
    string voag_caption  
}
VoagParty {

}
VoagPedigree {
    string rdfs_label  
}
VoagPerson {

}
VoagPriorityValue {
    string rdfs_label  
}
VoagProcess {

}
VoagProductLogo {
    string voag_width  
    string voag_height  
    string rdfs_label  
    uri voag_image  
    string voag_caption  
    string vaem_description  
}
VoagProvenance {
    string rdfs_label  
}
VoagPublicationStatus {
    string rdfs_label  
}
VoagQualifier {

}
VoagRejectionEvent {

}
VoagRetreivalEvent {

}
VoagReviewEvent {

}
VoagSchemaGraph {
    string rdfs_label  
}
VoagService {

}
VoagStakeholderGroup {

}
VoagStandard {

}
VoagVocabGraph {

}
HttpPurl.orgVocabFrbrCoreEndeavour {

}
IospressGeoCodedLocation {

}
IrdrAnimalIncident {

}
IrdrBiological {

}
IrdrClimatological {

}
IrdrConvectiveStorm {

}
IrdrDisease {

}
IrdrDrought {

}
IrdrEarthquake {

}
IrdrExtraterrestrial {

}
IrdrExtratropicalStorm {

}
IrdrExtremeTemperature {

}
IrdrFlood {

}
IrdrFog {

}
IrdrGeophysical {

}
IrdrGlacialLakeOutburst {

}
IrdrHydrological {

}
IrdrImpact {

}
IrdrInsectInfestation {

}
IrdrLandslide {

}
IrdrMassMovement {

}
IrdrMetereological {

}
IrdrSpaceWeather {

}
IrdrTropicalCyclone {

}
IrdrVolcanicActivity {

}
IrdrWaveAction {

}
IrdrWildfire {

}
KwgoATH {

}
KwgoAdministrativeRegion {

}
KwgoAdministrativeRegion0 {

}
KwgoAdministrativeRegion1 {

}
KwgoAdministrativeRegion2 {

}
KwgoAdministrativeRegion3 {

}
KwgoAdministrativeRegion4 {

}
KwgoAdministrativeRegion5 {

}
KwgoAdministrativeRegion6 {

}
KwgoAirPollutant {
    string rdfs_label  
}
KwgoAirQualityInstrument {

}
KwgoAirQualityObservation {

}
KwgoAirQualityObservationCollection {

}
KwgoAirQualitySite {

}
KwgoBlueskyModel {

}
KwgoBlueskyModeledWildfire {

}
KwgoBlueskyWildfireObservableProperty {
    string rdfs_label  
}
KwgoBlueskyWildfireObservation {

}
KwgoBlueskyWildfireObservationCollection {

}
KwgoCTH {

}
KwgoCell {

}
KwgoCensusACS5YearEstimatesObservation {

}
KwgoCensusACS5YearEstimatesObservationCollection {

}
KwgoCensusObservableProperty {
    string rdfs_comment  
    string rdfs_label  
}
KwgoChiefJudge {

}
KwgoClimateDivisionObservationCollection {

}
KwgoClimateDivisionObservationResult {

}
KwgoClimateDivisionPropertyObservationCollection {

}
KwgoClimateObservableProperty {
    string rdfs_label  
}
KwgoClimateObservation {

}
KwgoComplexFire {

}
KwgoCrisisCounselling {

}
KwgoCroplandObservableProperty {
    string rdfs_label  
}
KwgoCroplandObservation {

}
KwgoCroplandObservationCollection {

}
KwgoCroplandResult {

}
KwgoDebrisRemoval-PA-A {

}
KwgoDeclaration {

}
KwgoDirectFederalAssistance {

}
KwgoDisaster {

}
KwgoDisasterHousing {

}
KwgoDisasterUnemploymentAssistance {

}
KwgoDoD {

}
KwgoDroughtIntensity {
    string rdfs_label  
}
KwgoDroughtZone {

}
KwgoDroughtZoneOverlapObservation {

}
KwgoDroughtZoneOverlapObservationCollection {

}
KwgoEarthquake {

}
KwgoEarthquakeObservableProperty {

}
KwgoEarthquakeObservationCollection {

}
KwgoEmergencyDeclaration {

}
KwgoEventSegment {

}
KwgoExpertiseTopic {

}
KwgoFederalJudicalDistrict {

}
KwgoFieldsOfStudy {

}
KwgoFire {

}
KwgoFireCause {
    string rdfs_label  
}
KwgoFireManagementAssistance-PA-I {

}
KwgoFireManagementDeclaration {

}
KwgoFireMappingAssessmentLabel {

}
KwgoFix {

}
KwgoGeometry {

}
KwgoGeometryCollection {

}
KwgoHazard {

}
KwgoHazardEpisode {

}
KwgoHazardMitigation {

}
KwgoHelipadAvailability {
    string rdfs_label  
}
KwgoHospital {

}
KwgoHospitalStatus {
    string rdfs_label  
}
KwgoHospitalType {
    string rdfs_label  
}
KwgoHousingAssistance {

}
KwgoImpactObservableProperty {
    string rdfs_label  
}
KwgoImpactObservation {

}
KwgoImpactObservationCollection {

}
KwgoIndividualAndFamilyGrant {

}
KwgoIndividualAssistance {

}
KwgoIndividualAssistance-PA-C {

}
KwgoIndividualsAndHouseholds {

}
KwgoJudegeInfo {

}
KwgoLSADArea {
    string rdfs_comment  
    string rdfs_label  
}
KwgoLevelI {

}
KwgoLevelII {

}
KwgoLevelIII {

}
KwgoLevelIIIPediatric {

}
KwgoLevelIIPediatric {

}
KwgoLevelIIRehab {

}
KwgoLevelIV {

}
KwgoLevelIPediatric {

}
KwgoLevelIPediatricRehab {

}
KwgoLevelIRehab {

}
KwgoLevelPediatric {

}
KwgoLevelV {

}
KwgoMTBSComplexFire {

}
KwgoMTBSFire {

}
KwgoMTBSFireObservableProperty {
    string rdfs_comment  
    string rdfs_label  
}
KwgoMTBSFireObservation {

}
KwgoMTBSFireObservationCollection {

}
KwgoMTBSOutOfAreaResponseFire {

}
KwgoMTBSPrescribedFire {

}
KwgoMTBSUnknownFire {

}
KwgoMTBSWildfire {

}
KwgoMTBSWildlandFireUse {

}
KwgoMagnitudeObservableProperty {
    string rdfs_label  
}
KwgoMagnitudeObservation {

}
KwgoMagnitudeObservationCollection {

}
KwgoMajorDisasterDeclaration {

}
KwgoMappingProgram {

}
KwgoNIFCFire {

}
KwgoNIFCFireObservableProperty {
    string rdfs_label  
}
KwgoNIFCFireObservation {

}
KwgoNIFCIncidentComplexFire {

}
KwgoNIFCPrescribedFire {

}
KwgoNIFCWildfire {

}
KwgoNOAAAstronomicalLowTide {

}
KwgoNOAAAvalanche {

}
KwgoNOAABlizzard {

}
KwgoNOAACoastalFlood {

}
KwgoNOAAColdWindChill {

}
KwgoNOAADebrisFlow {

}
KwgoNOAADenseFog {

}
KwgoNOAADenseSmoke {

}
KwgoNOAADrought {

}
KwgoNOAADustDevil {

}
KwgoNOAADustStorm {

}
KwgoNOAAExcessiveHeat {

}
KwgoNOAAExtremeColdWindChill {

}
KwgoNOAAFlashFlood {

}
KwgoNOAAFlood {

}
KwgoNOAAFreezingFog {

}
KwgoNOAAFrostFreeze {

}
KwgoNOAAFunnelCloud {

}
KwgoNOAAHail {

}
KwgoNOAAHazard {

}
KwgoNOAAHeat {

}
KwgoNOAAHeavyRain {

}
KwgoNOAAHeavySnow {

}
KwgoNOAAHighSurf {

}
KwgoNOAAHighWind {

}
KwgoNOAAHurricane {

}
KwgoNOAAIceStorm {

}
KwgoNOAALake-EffectSnow {

}
KwgoNOAALakeshoreFlood {

}
KwgoNOAALightning {

}
KwgoNOAAMarineHail {

}
KwgoNOAAMarineHighWind {

}
KwgoNOAAMarineHurricaneTyphoon {

}
KwgoNOAAMarineStrongWind {

}
KwgoNOAAMarineThunderstormWind {

}
KwgoNOAAMarineTropicalDepression {

}
KwgoNOAAMarineTropicalStorm {

}
KwgoNOAARipCurrent {

}
KwgoNOAASleet {

}
KwgoNOAASneakerwave {

}
KwgoNOAAStormSurgeTide {

}
KwgoNOAAStrongWind {

}
KwgoNOAAThunderstormWind {

}
KwgoNOAATornado {

}
KwgoNOAATropicalDepression {

}
KwgoNOAATropicalStorm {

}
KwgoNOAAWaterspout {

}
KwgoNOAAWildfire {

}
KwgoNOAAWinterStorm {

}
KwgoNOAAWinterWeather {

}
KwgoNWZone {

}
KwgoNielsenMarketZone {

}
KwgoOther {

}
KwgoOutOfAreaResponseFire {

}
KwgoPARC {

}
KwgoPrescribedFire {

}
KwgoProgram {

}
KwgoProtectiveMeasures-PA-B {

}
KwgoPublicAssistance {

}
KwgoPublicBuildings-PA-F {

}
KwgoPublicHealthObservableProperty {
    string rdfs_label  
}
KwgoPublicHealthObservation {

}
KwgoPublicHealthObservationCollection {

}
KwgoPublicUtilitiesPA-G {

}
KwgoQuantity {

}
KwgoRPTC {

}
KwgoRTC {

}
KwgoRTH {

}
KwgoRecreationalOrOther-PA-H {

}
KwgoRegion {

}
KwgoRegionalCircuit {

}
KwgoRoadSegment {

}
KwgoRoadSegmentNode {

}
KwgoRoadType {
    string rdfs_label  
}
KwgoRoadsAndBridges-PA-D {

}
KwgoS2Cell {

}
KwgoSmallBusinessAdministration {

}
KwgoSmokePlumeObservableProperty {
    string rdfs_label  
}
KwgoSmokePlumeObservation {

}
KwgoSmokePlumeSnapshot {

}
KwgoSoilMapUnit {

}
KwgoSoilMapUnitObservableProperty {
    string rdfs_comment  
    string rdfs_label  
}
KwgoSoilMapUnitObservation {

}
KwgoSoilMapUnitObservationCollection {

}
KwgoSoilMapUnitOverlapObservation {

}
KwgoStormTrack {

}
KwgoStormTrackObservableProperty {
    string rdfs_label  
}
KwgoStormTrackObservation {

}
KwgoStormTrackObservationCollection {

}
KwgoStormTracklet {

}
KwgoStormTrackletObservableProperty {
    string rdfs_label  
}
KwgoStormTrackletObservation {

}
KwgoStormTrackletObservationCollection {

}
KwgoTRF {

}
KwgoTRH {

}
KwgoTornadoMagnitudeObservationCollection {

}
KwgoTraumaDescription {

}
KwgoTraumaLevelCare {

}
KwgoUSCensusMSA {

}
KwgoUSClimateDivision {

}
KwgoUSPresident {

}
KwgoVenue {

}
KwgoVulnerabilityIndexObservation {

}
KwgoVulnerabilityObservableProperty {
    string rdfs_label  
}
KwgoWaterControlFacilities-PA-E {

}
KwgoWildfire {

}
KwgoWildlandFireUse {

}
KwgoWindMagnitudeObservationCollection {

}
KwgoZipCodeArea {

}
SosaEarthquakeObservation {

}
SosaFeatureOfInterest {

}
SosaObservableProperty {

}
SosaObservation {

}
SosaObservationCollection {

}
SosaPlatform {

}
SosaResult {

}
SosaSensor {

}
B805a9e7d30eaabcb686b8ce670ed1e95 {
    string http___nhdplusv2.spatialai.org_v1_nhdplusv2#hasCOMID  
    string http___nhdplusv2.spatialai.org_v1_nhdplusv2#hasFCODE  
    string dct_title  
    string http___nhdplusv2.spatialai.org_v1_nhdplusv2#hasReachCode  
    string rdfs_label  
    string http___nhdplusv2.spatialai.org_v1_nhdplusv2#hasFTYPE  
}
HttpGwml2.orgDefGwml2#GWAquifer {
    string rdfs_label  
    string http___sawgraph.spatialai.org_v1_il_isgs#ilSawAqId  
    string http___sawgraph.spatialai.org_v1_me_mgs#meMgsAqId  
    string http___sawgraph.spatialai.org_v1_saw_water#aquiferType  
}
HttpGwml2.orgDefGwml2#GWAquiferSystem {
    string rdfs_comment  
    string rdfs_label  
    string http___sawgraph.spatialai.org_v1_me_mgs#meSawAqSysId  
    string http___sawgraph.spatialai.org_v1_il_isgs#ilSawAqSysId  
}
HttpHyfo.spatialai.orgV1Hyfo#AquiferWaterFeature {

}
HttpHyfo.spatialai.orgV1Hyfo#SubsurfaceWaterFeature {

}
HttpHyfo.spatialai.orgV1Hyfo#SurfaceWaterFeature {

}
HttpHyfo.spatialai.orgV1Hyfo#WaterFeature {

}
HttpHyfo.spatialai.orgV1Hyfo#WaterFeatureRepresentation {

}
HttpNhdplusv2.spatialai.orgV1Nhdplusv2#FlowPathLength {

}
HyfHYElementaryFlowPath {
    string http___nhdplusv2.spatialai.org_v1_nhdplusv2#hasCOMID  
    string http___nhdplusv2.spatialai.org_v1_nhdplusv2#hasFCODE  
    string dct_title  
    string http___nhdplusv2.spatialai.org_v1_nhdplusv2#hasReachCode  
    string rdfs_label  
    string http___nhdplusv2.spatialai.org_v1_nhdplusv2#hasFTYPE  
}
HyfHYMainStem {

}
IlIsgsISGS-Well {
    string il_isgs_hasOwner  
    string rdfs_label  
    string il_isgs_hasISWSId  
}
IlIsgsWellDepthInFt {
    qudt_NumericUnion qudt_numericValue  
}
IlIsgsWellPurpose {
    string rdfs_label  
}
IlIsgsWellYield {
    qudt_NumericUnion qudt_numericValue  
}
KwgoS2CellLevel13 {

}
KwgoStatisticalArea {

}
MeMgsMGS-Well {
    string rdfs_label  
}
MeMgsWellDepthInFt {
    qudt_NumericUnion qudt_numericValue  
}
MeMgsWellOverburdenThicknessInFt {
    qudt_NumericUnion qudt_numericValue  
}
MeMgsWellType {

}
MeMgsWellUse {

}
OwlDataProperty {

}
StadSingleData {

}
UsSdwisCombinedDistributionSystem {

}
UsSdwisPWS-ServiceArea {
    string us_sdwis_hasMethod  
}
UsSdwisPWS-ServiceAreaType {
    string rdfs_label  
}
UsSdwisPWS-SourceWaterType {

}
UsSdwisPWS-SubFeature {

}
UsSdwisPWS-SubFeatureActivity {
    string rdfs_label  
}
UsSdwisPWS-SubFeatureType {
    string rdfs_label  
}
UsSdwisPublicWaterSystem {

}
UsSdwisPublicWaterSystem-CWS {
    date us_sdwis_lastReport  
    int32 us_sdwis_populationServed  
    date us_sdwis_firstReport  
    string rdfs_label  
    string us_sdwis_pwsName  
    string us_sdwis_hasActivity  
    int32 us_sdwis_serviceConnections  
    string us_sdwis_hasOwnership  
    date us_sdwis_deactivationDate  
}
UsSdwisPublicWaterSystem-GW {
    date us_sdwis_lastReport  
    int32 us_sdwis_populationServed  
    date us_sdwis_firstReport  
    string rdfs_label  
    string us_sdwis_pwsName  
    string us_sdwis_hasActivity  
    int32 us_sdwis_serviceConnections  
    string us_sdwis_hasOwnership  
    date us_sdwis_deactivationDate  
}
UsSdwisPublicWaterSystem-NCWS {

}
UsSdwisPublicWaterSystem-NTNCWS {
    date us_sdwis_lastReport  
    int32 us_sdwis_populationServed  
    date us_sdwis_firstReport  
    string rdfs_label  
    string us_sdwis_pwsName  
    string us_sdwis_hasActivity  
    int32 us_sdwis_serviceConnections  
    string us_sdwis_hasOwnership  
    date us_sdwis_deactivationDate  
}
UsSdwisPublicWaterSystem-SW {
    date us_sdwis_lastReport  
    int32 us_sdwis_populationServed  
    date us_sdwis_firstReport  
    string rdfs_label  
    string us_sdwis_pwsName  
    string us_sdwis_hasActivity  
    int32 us_sdwis_serviceConnections  
    date us_sdwis_deactivationDate  
    string us_sdwis_hasOwnership  
}
UsSdwisPublicWaterSystem-TNCWS {
    date us_sdwis_lastReport  
    int32 us_sdwis_populationServed  
    date us_sdwis_firstReport  
    string rdfs_label  
    string us_sdwis_pwsName  
    string us_sdwis_hasActivity  
    int32 us_sdwis_serviceConnections  
    date us_sdwis_deactivationDate  
    string us_sdwis_hasOwnership  
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
QudtAngleUnit ||--|o RdfsLiteral : "rdfs_label"
QudtAngleUnit ||--|o QudtQuantityKindDimensionVector : "qudt_hasDimensionVector"
QudtAngleUnit ||--|o QudtQuantityKind : "qudt_hasQuantityKind"
QudtAngleUnit ||--|o OwlOntology : "rdfs_isDefinedBy"
QudtAngleUnit ||--|o RdfsResource : "rdfs_isDefinedBy"
QudtAngleUnit ||--|o RdfsResource : "rdfs_seeAlso"
QudtAngleUnit ||--|o QudtDerivedUnit : "qudt_scalingOf"
QudtAngleUnit ||--|o QudtUnit : "qudt_scalingOf"
QudtAngleUnit ||--|o QudtCountingUnit : "qudt_scalingOf"
QudtAngleUnit ||--|o QudtCurrencyUnit : "qudt_scalingOf"
QudtAngleUnit ||--|o QudtBinaryPrefix : "qudt_prefix"
QudtAngleUnit ||--|o QudtPrefix : "qudt_prefix"
QudtAngleUnit ||--|o QudtDecimalPrefix : "qudt_prefix"
QudtAngleUnit ||--|o RdfsLiteral : "rdfs_comment"
QudtAngleUnit ||--|o QudtQuantityKindDimensionVector : "qudt_qkdvNumerator"
QudtAngleUnit ||--|o QudtDecimalPrefix : "qudt_exactMatch"
QudtAngleUnit ||--|o QudtUnit : "qudt_exactMatch"
QudtAngleUnit ||--|o QudtContextualUnit : "qudt_exactMatch"
QudtAngleUnit ||--|o QudtDerivedUnit : "qudt_exactMatch"
QudtAngleUnit ||--|o QudtCountingUnit : "qudt_exactMatch"
QudtAngleUnit ||--|o QudtQuantityKindDimensionVector : "qudt_qkdvDenominator"
QudtAngleUnit ||--|o ProvEntity : "prov_wasDerivedFrom"
QudtAspectClass ||--|o RdfsLiteral : "rdfs_comment"
QudtAspectClass ||--|o RdfsLiteral : "rdfs_label"
QudtAspectClass ||--|o OwlOntology : "rdfs_isDefinedBy"
QudtAspectClass ||--|o RdfsResource : "rdfs_isDefinedBy"
QudtAspectClass ||--|o RdfsClass : "rdfs_subClassOf"
QudtBinaryPrefix ||--|o RdfsLiteral : "rdfs_label"
QudtBinaryPrefix ||--|o OwlOntology : "rdfs_isDefinedBy"
QudtBinaryPrefix ||--|o RdfsResource : "rdfs_isDefinedBy"
QudtBitEncodingType ||--|o RdfsLiteral : "rdfs_label"
QudtBitEncodingType ||--|o OwlOntology : "rdfs_isDefinedBy"
QudtBitEncodingType ||--|o RdfsResource : "rdfs_isDefinedBy"
QudtBooleanEncodingType ||--|o RdfsLiteral : "rdfs_label"
QudtBooleanEncodingType ||--|o OwlOntology : "rdfs_isDefinedBy"
QudtBooleanEncodingType ||--|o RdfsResource : "rdfs_isDefinedBy"
QudtByteEncodingType ||--|o RdfsLiteral : "rdfs_label"
QudtByteEncodingType ||--|o OwlOntology : "rdfs_isDefinedBy"
QudtByteEncodingType ||--|o RdfsResource : "rdfs_isDefinedBy"
QudtCardinalityType ||--|o RdfsLiteral : "rdfs_label"
QudtCardinalityType ||--|o OwlOntology : "rdfs_isDefinedBy"
QudtCardinalityType ||--|o RdfsResource : "rdfs_isDefinedBy"
QudtCharEncodingType ||--|o OwlOntology : "rdfs_isDefinedBy"
QudtCharEncodingType ||--|o RdfsResource : "rdfs_isDefinedBy"
QudtCharEncodingType ||--|o RdfsLiteral : "rdfs_label"
QudtContextualUnit ||--|o QudtDerivedUnit : "qudt_scalingOf"
QudtContextualUnit ||--|o QudtUnit : "qudt_scalingOf"
QudtContextualUnit ||--|o QudtCountingUnit : "qudt_scalingOf"
QudtContextualUnit ||--|o QudtCurrencyUnit : "qudt_scalingOf"
QudtContextualUnit ||--|o QudtQuantityKind : "qudt_hasQuantityKind"
QudtContextualUnit ||--|o OwlOntology : "rdfs_isDefinedBy"
QudtContextualUnit ||--|o RdfsResource : "rdfs_isDefinedBy"
QudtContextualUnit ||--|o RdfsLiteral : "rdfs_label"
QudtContextualUnit ||--|o QudtDecimalPrefix : "qudt_exactMatch"
QudtContextualUnit ||--|o QudtUnit : "qudt_exactMatch"
QudtContextualUnit ||--|o QudtContextualUnit : "qudt_exactMatch"
QudtContextualUnit ||--|o QudtDerivedUnit : "qudt_exactMatch"
QudtContextualUnit ||--|o QudtCountingUnit : "qudt_exactMatch"
QudtContextualUnit ||--|o QudtQuantityKindDimensionVector : "qudt_hasDimensionVector"
QudtContextualUnit ||--|o RdfsResource : "rdfs_seeAlso"
QudtContextualUnit ||--|o QudtBinaryPrefix : "qudt_prefix"
QudtContextualUnit ||--|o QudtPrefix : "qudt_prefix"
QudtContextualUnit ||--|o QudtDecimalPrefix : "qudt_prefix"
QudtContextualUnit ||--|o RdfsLiteral : "rdfs_comment"
QudtContextualUnit ||--|o QudtQuantityKindDimensionVector : "qudt_qkdvNumerator"
QudtContextualUnit ||--|o QudtQuantityKindDimensionVector : "qudt_qkdvDenominator"
QudtContextualUnit ||--|o ProvEntity : "prov_wasDerivedFrom"
QudtCountingUnit ||--|o QudtDerivedUnit : "qudt_scalingOf"
QudtCountingUnit ||--|o QudtUnit : "qudt_scalingOf"
QudtCountingUnit ||--|o QudtCountingUnit : "qudt_scalingOf"
QudtCountingUnit ||--|o QudtCurrencyUnit : "qudt_scalingOf"
QudtCountingUnit ||--|o QudtBinaryPrefix : "qudt_prefix"
QudtCountingUnit ||--|o QudtPrefix : "qudt_prefix"
QudtCountingUnit ||--|o QudtDecimalPrefix : "qudt_prefix"
QudtCountingUnit ||--|o QudtQuantityKind : "qudt_hasQuantityKind"
QudtCountingUnit ||--|o OwlOntology : "rdfs_isDefinedBy"
QudtCountingUnit ||--|o RdfsResource : "rdfs_isDefinedBy"
QudtCountingUnit ||--|o RdfsLiteral : "rdfs_label"
QudtCountingUnit ||--|o QudtDecimalPrefix : "qudt_exactMatch"
QudtCountingUnit ||--|o QudtUnit : "qudt_exactMatch"
QudtCountingUnit ||--|o QudtContextualUnit : "qudt_exactMatch"
QudtCountingUnit ||--|o QudtDerivedUnit : "qudt_exactMatch"
QudtCountingUnit ||--|o QudtCountingUnit : "qudt_exactMatch"
QudtCountingUnit ||--|o QudtQuantityKindDimensionVector : "qudt_hasDimensionVector"
QudtCountingUnit ||--|o RdfsResource : "rdfs_seeAlso"
QudtCountingUnit ||--|o RdfsLiteral : "rdfs_comment"
QudtCountingUnit ||--|o QudtQuantityKindDimensionVector : "qudt_qkdvNumerator"
QudtCountingUnit ||--|o QudtQuantityKindDimensionVector : "qudt_qkdvDenominator"
QudtCountingUnit ||--|o ProvEntity : "prov_wasDerivedFrom"
QudtCurrencyUnit ||--|o RdfsLiteral : "rdfs_label"
QudtCurrencyUnit ||--|o QudtQuantityKindDimensionVector : "qudt_hasDimensionVector"
QudtCurrencyUnit ||--|o QudtQuantityKind : "qudt_hasQuantityKind"
QudtCurrencyUnit ||--|o QudtBinaryPrefix : "qudt_prefix"
QudtCurrencyUnit ||--|o QudtPrefix : "qudt_prefix"
QudtCurrencyUnit ||--|o QudtDecimalPrefix : "qudt_prefix"
QudtCurrencyUnit ||--|o QudtDerivedUnit : "qudt_scalingOf"
QudtCurrencyUnit ||--|o QudtUnit : "qudt_scalingOf"
QudtCurrencyUnit ||--|o QudtCountingUnit : "qudt_scalingOf"
QudtCurrencyUnit ||--|o QudtCurrencyUnit : "qudt_scalingOf"
QudtCurrencyUnit ||--|o OwlOntology : "rdfs_isDefinedBy"
QudtCurrencyUnit ||--|o RdfsResource : "rdfs_isDefinedBy"
QudtCurrencyUnit ||--|o RdfsResource : "rdfs_seeAlso"
QudtCurrencyUnit ||--|o RdfsLiteral : "rdfs_comment"
QudtCurrencyUnit ||--|o QudtQuantityKindDimensionVector : "qudt_qkdvNumerator"
QudtCurrencyUnit ||--|o QudtDecimalPrefix : "qudt_exactMatch"
QudtCurrencyUnit ||--|o QudtUnit : "qudt_exactMatch"
QudtCurrencyUnit ||--|o QudtContextualUnit : "qudt_exactMatch"
QudtCurrencyUnit ||--|o QudtDerivedUnit : "qudt_exactMatch"
QudtCurrencyUnit ||--|o QudtCountingUnit : "qudt_exactMatch"
QudtCurrencyUnit ||--|o QudtQuantityKindDimensionVector : "qudt_qkdvDenominator"
QudtCurrencyUnit ||--|o ProvEntity : "prov_wasDerivedFrom"
QudtDateTimeStringEncodingType ||--|o RdfsLiteral : "rdfs_label"
QudtDateTimeStringEncodingType ||--|o OwlOntology : "rdfs_isDefinedBy"
QudtDateTimeStringEncodingType ||--|o RdfsResource : "rdfs_isDefinedBy"
QudtDecimalPrefix ||--|o RdfsLiteral : "rdfs_label"
QudtDecimalPrefix ||--|o QudtDecimalPrefix : "qudt_exactMatch"
QudtDecimalPrefix ||--|o QudtUnit : "qudt_exactMatch"
QudtDecimalPrefix ||--|o QudtContextualUnit : "qudt_exactMatch"
QudtDecimalPrefix ||--|o QudtDerivedUnit : "qudt_exactMatch"
QudtDecimalPrefix ||--|o QudtCountingUnit : "qudt_exactMatch"
QudtDecimalPrefix ||--|o OwlOntology : "rdfs_isDefinedBy"
QudtDecimalPrefix ||--|o RdfsResource : "rdfs_isDefinedBy"
QudtDerivedUnit ||--|o RdfsResource : "rdfs_seeAlso"
QudtDerivedUnit ||--|o QudtDerivedUnit : "qudt_scalingOf"
QudtDerivedUnit ||--|o QudtUnit : "qudt_scalingOf"
QudtDerivedUnit ||--|o QudtCountingUnit : "qudt_scalingOf"
QudtDerivedUnit ||--|o QudtCurrencyUnit : "qudt_scalingOf"
QudtDerivedUnit ||--|o QudtBinaryPrefix : "qudt_prefix"
QudtDerivedUnit ||--|o QudtPrefix : "qudt_prefix"
QudtDerivedUnit ||--|o QudtDecimalPrefix : "qudt_prefix"
QudtDerivedUnit ||--|o QudtQuantityKind : "qudt_hasQuantityKind"
QudtDerivedUnit ||--|o OwlOntology : "rdfs_isDefinedBy"
QudtDerivedUnit ||--|o RdfsResource : "rdfs_isDefinedBy"
QudtDerivedUnit ||--|o RdfsLiteral : "rdfs_comment"
QudtDerivedUnit ||--|o QudtQuantityKindDimensionVector : "qudt_qkdvNumerator"
QudtDerivedUnit ||--|o RdfsLiteral : "rdfs_label"
QudtDerivedUnit ||--|o QudtDecimalPrefix : "qudt_exactMatch"
QudtDerivedUnit ||--|o QudtUnit : "qudt_exactMatch"
QudtDerivedUnit ||--|o QudtContextualUnit : "qudt_exactMatch"
QudtDerivedUnit ||--|o QudtDerivedUnit : "qudt_exactMatch"
QudtDerivedUnit ||--|o QudtCountingUnit : "qudt_exactMatch"
QudtDerivedUnit ||--|o QudtQuantityKindDimensionVector : "qudt_hasDimensionVector"
QudtDerivedUnit ||--|o QudtQuantityKindDimensionVector : "qudt_qkdvDenominator"
QudtDerivedUnit ||--|o ProvEntity : "prov_wasDerivedFrom"
QudtDimensionlessUnit ||--|o RdfsLiteral : "rdfs_label"
QudtDimensionlessUnit ||--|o QudtQuantityKindDimensionVector : "qudt_hasDimensionVector"
QudtDimensionlessUnit ||--|o QudtQuantityKind : "qudt_hasQuantityKind"
QudtDimensionlessUnit ||--|o OwlOntology : "rdfs_isDefinedBy"
QudtDimensionlessUnit ||--|o RdfsResource : "rdfs_isDefinedBy"
QudtDimensionlessUnit ||--|o RdfsResource : "rdfs_seeAlso"
QudtDimensionlessUnit ||--|o QudtDerivedUnit : "qudt_scalingOf"
QudtDimensionlessUnit ||--|o QudtUnit : "qudt_scalingOf"
QudtDimensionlessUnit ||--|o QudtCountingUnit : "qudt_scalingOf"
QudtDimensionlessUnit ||--|o QudtCurrencyUnit : "qudt_scalingOf"
QudtDimensionlessUnit ||--|o QudtBinaryPrefix : "qudt_prefix"
QudtDimensionlessUnit ||--|o QudtPrefix : "qudt_prefix"
QudtDimensionlessUnit ||--|o QudtDecimalPrefix : "qudt_prefix"
QudtDimensionlessUnit ||--|o RdfsLiteral : "rdfs_comment"
QudtDimensionlessUnit ||--|o QudtQuantityKindDimensionVector : "qudt_qkdvNumerator"
QudtDimensionlessUnit ||--|o QudtDecimalPrefix : "qudt_exactMatch"
QudtDimensionlessUnit ||--|o QudtUnit : "qudt_exactMatch"
QudtDimensionlessUnit ||--|o QudtContextualUnit : "qudt_exactMatch"
QudtDimensionlessUnit ||--|o QudtDerivedUnit : "qudt_exactMatch"
QudtDimensionlessUnit ||--|o QudtCountingUnit : "qudt_exactMatch"
QudtDimensionlessUnit ||--|o QudtQuantityKindDimensionVector : "qudt_qkdvDenominator"
QudtDimensionlessUnit ||--|o ProvEntity : "prov_wasDerivedFrom"
QudtEndianType ||--|o RdfsLiteral : "rdfs_label"
QudtEndianType ||--|o OwlOntology : "rdfs_isDefinedBy"
QudtEndianType ||--|o RdfsResource : "rdfs_isDefinedBy"
QudtFloatingPointEncodingType ||--|o RdfsLiteral : "rdfs_label"
QudtFloatingPointEncodingType ||--|o OwlOntology : "rdfs_isDefinedBy"
QudtFloatingPointEncodingType ||--|o RdfsResource : "rdfs_isDefinedBy"
QudtIntegerEncodingType ||--|o RdfsLiteral : "rdfs_label"
QudtIntegerEncodingType ||--|o OwlOntology : "rdfs_isDefinedBy"
QudtIntegerEncodingType ||--|o RdfsResource : "rdfs_isDefinedBy"
QudtLogarithmicUnit ||--|o RdfsLiteral : "rdfs_label"
QudtLogarithmicUnit ||--|o QudtQuantityKindDimensionVector : "qudt_hasDimensionVector"
QudtLogarithmicUnit ||--|o QudtQuantityKind : "qudt_hasQuantityKind"
QudtLogarithmicUnit ||--|o OwlOntology : "rdfs_isDefinedBy"
QudtLogarithmicUnit ||--|o RdfsResource : "rdfs_isDefinedBy"
QudtLogarithmicUnit ||--|o RdfsResource : "rdfs_seeAlso"
QudtLogarithmicUnit ||--|o QudtDerivedUnit : "qudt_scalingOf"
QudtLogarithmicUnit ||--|o QudtUnit : "qudt_scalingOf"
QudtLogarithmicUnit ||--|o QudtCountingUnit : "qudt_scalingOf"
QudtLogarithmicUnit ||--|o QudtCurrencyUnit : "qudt_scalingOf"
QudtLogarithmicUnit ||--|o QudtBinaryPrefix : "qudt_prefix"
QudtLogarithmicUnit ||--|o QudtPrefix : "qudt_prefix"
QudtLogarithmicUnit ||--|o QudtDecimalPrefix : "qudt_prefix"
QudtLogarithmicUnit ||--|o RdfsLiteral : "rdfs_comment"
QudtLogarithmicUnit ||--|o QudtQuantityKindDimensionVector : "qudt_qkdvNumerator"
QudtLogarithmicUnit ||--|o QudtDecimalPrefix : "qudt_exactMatch"
QudtLogarithmicUnit ||--|o QudtUnit : "qudt_exactMatch"
QudtLogarithmicUnit ||--|o QudtContextualUnit : "qudt_exactMatch"
QudtLogarithmicUnit ||--|o QudtDerivedUnit : "qudt_exactMatch"
QudtLogarithmicUnit ||--|o QudtCountingUnit : "qudt_exactMatch"
QudtLogarithmicUnit ||--|o QudtQuantityKindDimensionVector : "qudt_qkdvDenominator"
QudtLogarithmicUnit ||--|o ProvEntity : "prov_wasDerivedFrom"
QudtOrderedType ||--|o RdfsLiteral : "rdfs_label"
QudtOrderedType ||--|o OwlOntology : "rdfs_isDefinedBy"
QudtOrderedType ||--|o RdfsResource : "rdfs_isDefinedBy"
QudtPlaneAngleUnit ||--|o RdfsLiteral : "rdfs_label"
QudtPlaneAngleUnit ||--|o QudtQuantityKindDimensionVector : "qudt_hasDimensionVector"
QudtPlaneAngleUnit ||--|o QudtQuantityKind : "qudt_hasQuantityKind"
QudtPlaneAngleUnit ||--|o OwlOntology : "rdfs_isDefinedBy"
QudtPlaneAngleUnit ||--|o RdfsResource : "rdfs_isDefinedBy"
QudtPlaneAngleUnit ||--|o RdfsResource : "rdfs_seeAlso"
QudtPlaneAngleUnit ||--|o QudtDerivedUnit : "qudt_scalingOf"
QudtPlaneAngleUnit ||--|o QudtUnit : "qudt_scalingOf"
QudtPlaneAngleUnit ||--|o QudtCountingUnit : "qudt_scalingOf"
QudtPlaneAngleUnit ||--|o QudtCurrencyUnit : "qudt_scalingOf"
QudtPlaneAngleUnit ||--|o QudtBinaryPrefix : "qudt_prefix"
QudtPlaneAngleUnit ||--|o QudtPrefix : "qudt_prefix"
QudtPlaneAngleUnit ||--|o QudtDecimalPrefix : "qudt_prefix"
QudtPlaneAngleUnit ||--|o RdfsLiteral : "rdfs_comment"
QudtPlaneAngleUnit ||--|o QudtQuantityKindDimensionVector : "qudt_qkdvNumerator"
QudtPlaneAngleUnit ||--|o QudtDecimalPrefix : "qudt_exactMatch"
QudtPlaneAngleUnit ||--|o QudtUnit : "qudt_exactMatch"
QudtPlaneAngleUnit ||--|o QudtContextualUnit : "qudt_exactMatch"
QudtPlaneAngleUnit ||--|o QudtDerivedUnit : "qudt_exactMatch"
QudtPlaneAngleUnit ||--|o QudtCountingUnit : "qudt_exactMatch"
QudtPlaneAngleUnit ||--|o QudtQuantityKindDimensionVector : "qudt_qkdvDenominator"
QudtPlaneAngleUnit ||--|o ProvEntity : "prov_wasDerivedFrom"
QudtSignednessType ||--|o RdfsLiteral : "rdfs_label"
QudtSignednessType ||--|o OwlOntology : "rdfs_isDefinedBy"
QudtSignednessType ||--|o RdfsResource : "rdfs_isDefinedBy"
QudtSolidAngleUnit ||--|o RdfsLiteral : "rdfs_label"
QudtSolidAngleUnit ||--|o QudtQuantityKindDimensionVector : "qudt_hasDimensionVector"
QudtSolidAngleUnit ||--|o QudtQuantityKind : "qudt_hasQuantityKind"
QudtSolidAngleUnit ||--|o OwlOntology : "rdfs_isDefinedBy"
QudtSolidAngleUnit ||--|o RdfsResource : "rdfs_isDefinedBy"
QudtSolidAngleUnit ||--|o RdfsResource : "rdfs_seeAlso"
QudtSolidAngleUnit ||--|o QudtDerivedUnit : "qudt_scalingOf"
QudtSolidAngleUnit ||--|o QudtUnit : "qudt_scalingOf"
QudtSolidAngleUnit ||--|o QudtCountingUnit : "qudt_scalingOf"
QudtSolidAngleUnit ||--|o QudtCurrencyUnit : "qudt_scalingOf"
QudtSolidAngleUnit ||--|o QudtBinaryPrefix : "qudt_prefix"
QudtSolidAngleUnit ||--|o QudtPrefix : "qudt_prefix"
QudtSolidAngleUnit ||--|o QudtDecimalPrefix : "qudt_prefix"
QudtSolidAngleUnit ||--|o RdfsLiteral : "rdfs_comment"
QudtSolidAngleUnit ||--|o QudtQuantityKindDimensionVector : "qudt_qkdvNumerator"
QudtSolidAngleUnit ||--|o QudtDecimalPrefix : "qudt_exactMatch"
QudtSolidAngleUnit ||--|o QudtUnit : "qudt_exactMatch"
QudtSolidAngleUnit ||--|o QudtContextualUnit : "qudt_exactMatch"
QudtSolidAngleUnit ||--|o QudtDerivedUnit : "qudt_exactMatch"
QudtSolidAngleUnit ||--|o QudtCountingUnit : "qudt_exactMatch"
QudtSolidAngleUnit ||--|o QudtQuantityKindDimensionVector : "qudt_qkdvDenominator"
QudtSolidAngleUnit ||--|o ProvEntity : "prov_wasDerivedFrom"
QudtUnit ||--|o RdfsResource : "rdfs_seeAlso"
QudtUnit ||--|o QudtDerivedUnit : "qudt_scalingOf"
QudtUnit ||--|o QudtUnit : "qudt_scalingOf"
QudtUnit ||--|o QudtCountingUnit : "qudt_scalingOf"
QudtUnit ||--|o QudtCurrencyUnit : "qudt_scalingOf"
QudtUnit ||--|o QudtBinaryPrefix : "qudt_prefix"
QudtUnit ||--|o QudtPrefix : "qudt_prefix"
QudtUnit ||--|o QudtDecimalPrefix : "qudt_prefix"
QudtUnit ||--|o QudtQuantityKind : "qudt_hasQuantityKind"
QudtUnit ||--|o OwlOntology : "rdfs_isDefinedBy"
QudtUnit ||--|o RdfsResource : "rdfs_isDefinedBy"
QudtUnit ||--|o RdfsLiteral : "rdfs_comment"
QudtUnit ||--|o QudtQuantityKindDimensionVector : "qudt_qkdvNumerator"
QudtUnit ||--|o RdfsLiteral : "rdfs_label"
QudtUnit ||--|o QudtDecimalPrefix : "qudt_exactMatch"
QudtUnit ||--|o QudtUnit : "qudt_exactMatch"
QudtUnit ||--|o QudtContextualUnit : "qudt_exactMatch"
QudtUnit ||--|o QudtDerivedUnit : "qudt_exactMatch"
QudtUnit ||--|o QudtCountingUnit : "qudt_exactMatch"
QudtUnit ||--|o QudtQuantityKindDimensionVector : "qudt_hasDimensionVector"
QudtUnit ||--|o QudtQuantityKindDimensionVector : "qudt_qkdvDenominator"
QudtUnit ||--|o ProvEntity : "prov_wasDerivedFrom"
SdosActionStatusType ||--|o RdfsLiteral : "rdfs_comment"
SdosActionStatusType ||--|o RdfsLiteral : "rdfs_label"
SdosAdultOrientedEnumeration ||--|o RdfsLiteral : "rdfs_comment"
SdosAdultOrientedEnumeration ||--|o RdfsLiteral : "rdfs_label"
SdosAdultOrientedEnumeration ||--|o SdosURL : "sdos_isPartOf"
SdosAdultOrientedEnumeration ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosBoardingPolicyType ||--|o RdfsLiteral : "rdfs_comment"
SdosBoardingPolicyType ||--|o RdfsLiteral : "rdfs_label"
SdosBodyMeasurementTypeEnumeration ||--|o RdfsLiteral : "rdfs_comment"
SdosBodyMeasurementTypeEnumeration ||--|o RdfsLiteral : "rdfs_label"
SdosBodyMeasurementTypeEnumeration ||--|o SdosURL : "sdos_isPartOf"
SdosBodyMeasurementTypeEnumeration ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosBookFormatType ||--|o RdfsLiteral : "rdfs_comment"
SdosBookFormatType ||--|o RdfsLiteral : "rdfs_label"
SdosBookFormatType ||--|o SdosURL : "sdos_isPartOf"
SdosBookFormatType ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosBoolean ||--|o RdfsLiteral : "rdfs_comment"
SdosBoolean ||--|o RdfsLiteral : "rdfs_label"
SdosCarUsageType ||--|o SdosOrganization : "sdos_contributor"
SdosCarUsageType ||--|o SdosPerson : "sdos_contributor"
SdosCarUsageType ||--|o RdfsLiteral : "rdfs_comment"
SdosCarUsageType ||--|o RdfsLiteral : "rdfs_label"
SdosCarUsageType ||--|o SdosURL : "sdos_isPartOf"
SdosCarUsageType ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosCertificationStatusEnumeration ||--|o RdfsLiteral : "rdfs_comment"
SdosCertificationStatusEnumeration ||--|o RdfsLiteral : "rdfs_label"
SdosCertificationStatusEnumeration ||--|o SdosURL : "sdos_isPartOf"
SdosCertificationStatusEnumeration ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosContactPointOption ||--|o RdfsLiteral : "rdfs_comment"
SdosContactPointOption ||--|o RdfsLiteral : "rdfs_label"
SdosDataType ||--|o RdfsLiteral : "rdfs_comment"
SdosDataType ||--|o RdfsLiteral : "rdfs_label"
SdosDayOfWeek ||--|o SdosOrganization : "sdos_contributor"
SdosDayOfWeek ||--|o SdosPerson : "sdos_contributor"
SdosDayOfWeek ||--|o RdfsLiteral : "rdfs_comment"
SdosDayOfWeek ||--|o RdfsLiteral : "rdfs_label"
SdosDayOfWeek ||--|o SdosURL : "sdos_sameAs"
SdosDeliveryMethod ||--|o SdosOrganization : "sdos_contributor"
SdosDeliveryMethod ||--|o SdosPerson : "sdos_contributor"
SdosDeliveryMethod ||--|o RdfsLiteral : "rdfs_comment"
SdosDeliveryMethod ||--|o RdfsLiteral : "rdfs_label"
SdosDigitalDocumentPermissionType ||--|o RdfsLiteral : "rdfs_comment"
SdosDigitalDocumentPermissionType ||--|o RdfsLiteral : "rdfs_label"
SdosDigitalPlatformEnumeration ||--|o RdfsLiteral : "rdfs_comment"
SdosDigitalPlatformEnumeration ||--|o RdfsLiteral : "rdfs_label"
SdosDigitalPlatformEnumeration ||--|o SdosURL : "sdos_isPartOf"
SdosDigitalPlatformEnumeration ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosDriveWheelConfigurationValue ||--|o SdosOrganization : "sdos_contributor"
SdosDriveWheelConfigurationValue ||--|o SdosPerson : "sdos_contributor"
SdosDriveWheelConfigurationValue ||--|o RdfsLiteral : "rdfs_comment"
SdosDriveWheelConfigurationValue ||--|o RdfsLiteral : "rdfs_label"
SdosDrugCostCategory ||--|o RdfsLiteral : "rdfs_comment"
SdosDrugCostCategory ||--|o RdfsLiteral : "rdfs_label"
SdosDrugCostCategory ||--|o SdosURL : "sdos_isPartOf"
SdosDrugCostCategory ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosDrugPregnancyCategory ||--|o RdfsLiteral : "rdfs_comment"
SdosDrugPregnancyCategory ||--|o RdfsLiteral : "rdfs_label"
SdosDrugPregnancyCategory ||--|o SdosURL : "sdos_isPartOf"
SdosDrugPregnancyCategory ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosDrugPrescriptionStatus ||--|o RdfsLiteral : "rdfs_comment"
SdosDrugPrescriptionStatus ||--|o RdfsLiteral : "rdfs_label"
SdosDrugPrescriptionStatus ||--|o SdosURL : "sdos_isPartOf"
SdosDrugPrescriptionStatus ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosEUEnergyEfficiencyEnumeration ||--|o RdfsLiteral : "rdfs_comment"
SdosEUEnergyEfficiencyEnumeration ||--|o RdfsLiteral : "rdfs_label"
SdosEUEnergyEfficiencyEnumeration ||--|o SdosURL : "sdos_isPartOf"
SdosEUEnergyEfficiencyEnumeration ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosEnergyStarEnergyEfficiencyEnumeration ||--|o RdfsLiteral : "rdfs_comment"
SdosEnergyStarEnergyEfficiencyEnumeration ||--|o RdfsLiteral : "rdfs_label"
SdosEnergyStarEnergyEfficiencyEnumeration ||--|o SdosURL : "sdos_isPartOf"
SdosEnergyStarEnergyEfficiencyEnumeration ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosEventAttendanceModeEnumeration ||--|o RdfsLiteral : "rdfs_comment"
SdosEventAttendanceModeEnumeration ||--|o RdfsLiteral : "rdfs_label"
SdosEventAttendanceModeEnumeration ||--|o SdosURL : "sdos_isPartOf"
SdosEventAttendanceModeEnumeration ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosEventStatusType ||--|o RdfsLiteral : "rdfs_comment"
SdosEventStatusType ||--|o RdfsLiteral : "rdfs_label"
SdosFulfillmentTypeEnumeration ||--|o RdfsLiteral : "rdfs_comment"
SdosFulfillmentTypeEnumeration ||--|o RdfsLiteral : "rdfs_label"
SdosFulfillmentTypeEnumeration ||--|o SdosURL : "sdos_isPartOf"
SdosFulfillmentTypeEnumeration ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosGameAvailabilityEnumeration ||--|o RdfsLiteral : "rdfs_comment"
SdosGameAvailabilityEnumeration ||--|o RdfsLiteral : "rdfs_label"
SdosGameAvailabilityEnumeration ||--|o SdosURL : "sdos_isPartOf"
SdosGameAvailabilityEnumeration ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosGamePlayMode ||--|o RdfsLiteral : "rdfs_comment"
SdosGamePlayMode ||--|o RdfsLiteral : "rdfs_label"
SdosGameServerStatus ||--|o RdfsLiteral : "rdfs_comment"
SdosGameServerStatus ||--|o RdfsLiteral : "rdfs_label"
SdosGenderType ||--|o RdfsLiteral : "rdfs_comment"
SdosGenderType ||--|o RdfsLiteral : "rdfs_label"
SdosGovernmentBenefitsType ||--|o RdfsLiteral : "rdfs_comment"
SdosGovernmentBenefitsType ||--|o RdfsLiteral : "rdfs_label"
SdosGovernmentBenefitsType ||--|o SdosURL : "sdos_isPartOf"
SdosGovernmentBenefitsType ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosHealthAspectEnumeration ||--|o RdfsLiteral : "rdfs_comment"
SdosHealthAspectEnumeration ||--|o RdfsLiteral : "rdfs_label"
SdosHealthAspectEnumeration ||--|o SdosURL : "sdos_isPartOf"
SdosHealthAspectEnumeration ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosIPTCDigitalSourceEnumeration ||--|o RdfsLiteral : "rdfs_label"
SdosIPTCDigitalSourceEnumeration ||--|o SdosURL : "sdos_isPartOf"
SdosIPTCDigitalSourceEnumeration ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosIPTCDigitalSourceEnumeration ||--|o RdfsLiteral : "rdfs_comment"
SdosIncentiveQualifiedExpenseType ||--|o RdfsLiteral : "rdfs_comment"
SdosIncentiveQualifiedExpenseType ||--|o RdfsLiteral : "rdfs_label"
SdosIncentiveQualifiedExpenseType ||--|o SdosURL : "sdos_isPartOf"
SdosIncentiveQualifiedExpenseType ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosIncentiveStatus ||--|o RdfsLiteral : "rdfs_comment"
SdosIncentiveStatus ||--|o RdfsLiteral : "rdfs_label"
SdosIncentiveStatus ||--|o SdosURL : "sdos_isPartOf"
SdosIncentiveStatus ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosIncentiveType ||--|o RdfsLiteral : "rdfs_comment"
SdosIncentiveType ||--|o RdfsLiteral : "rdfs_label"
SdosIncentiveType ||--|o SdosURL : "sdos_isPartOf"
SdosIncentiveType ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosInfectiousAgentClass ||--|o RdfsLiteral : "rdfs_comment"
SdosInfectiousAgentClass ||--|o RdfsLiteral : "rdfs_label"
SdosInfectiousAgentClass ||--|o SdosURL : "sdos_isPartOf"
SdosInfectiousAgentClass ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosItemAvailability ||--|o RdfsLiteral : "rdfs_comment"
SdosItemAvailability ||--|o RdfsLiteral : "rdfs_label"
SdosItemListOrderType ||--|o RdfsLiteral : "rdfs_comment"
SdosItemListOrderType ||--|o RdfsLiteral : "rdfs_label"
SdosLegalForceStatus ||--|o RdfsLiteral : "rdfs_label"
SdosLegalForceStatus ||--|o SdosURL : "sdos_isPartOf"
SdosLegalForceStatus ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosLegalForceStatus ||--|o SdosOrganization : "sdos_contributor"
SdosLegalForceStatus ||--|o SdosPerson : "sdos_contributor"
SdosLegalForceStatus ||--|o RdfsLiteral : "rdfs_comment"
SdosLegalValueLevel ||--|o RdfsLiteral : "rdfs_label"
SdosLegalValueLevel ||--|o SdosURL : "sdos_isPartOf"
SdosLegalValueLevel ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosLegalValueLevel ||--|o SdosOrganization : "sdos_contributor"
SdosLegalValueLevel ||--|o SdosPerson : "sdos_contributor"
SdosLegalValueLevel ||--|o RdfsLiteral : "rdfs_comment"
SdosMapCategoryType ||--|o RdfsLiteral : "rdfs_comment"
SdosMapCategoryType ||--|o RdfsLiteral : "rdfs_label"
SdosMeasurementMethodEnum ||--|o RdfsLiteral : "rdfs_comment"
SdosMeasurementMethodEnum ||--|o RdfsLiteral : "rdfs_label"
SdosMeasurementMethodEnum ||--|o SdosURL : "sdos_isPartOf"
SdosMeasurementMethodEnum ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosMediaManipulationRatingEnumeration ||--|o RdfsLiteral : "rdfs_comment"
SdosMediaManipulationRatingEnumeration ||--|o RdfsLiteral : "rdfs_label"
SdosMediaManipulationRatingEnumeration ||--|o SdosURL : "sdos_isPartOf"
SdosMediaManipulationRatingEnumeration ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosMedicalAudienceType ||--|o RdfsLiteral : "rdfs_comment"
SdosMedicalAudienceType ||--|o RdfsLiteral : "rdfs_label"
SdosMedicalAudienceType ||--|o SdosURL : "sdos_isPartOf"
SdosMedicalAudienceType ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosMedicalDevicePurpose ||--|o RdfsLiteral : "rdfs_comment"
SdosMedicalDevicePurpose ||--|o RdfsLiteral : "rdfs_label"
SdosMedicalDevicePurpose ||--|o SdosURL : "sdos_isPartOf"
SdosMedicalDevicePurpose ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosMedicalEvidenceLevel ||--|o RdfsLiteral : "rdfs_comment"
SdosMedicalEvidenceLevel ||--|o RdfsLiteral : "rdfs_label"
SdosMedicalEvidenceLevel ||--|o SdosURL : "sdos_isPartOf"
SdosMedicalEvidenceLevel ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosMedicalImagingTechnique ||--|o RdfsLiteral : "rdfs_comment"
SdosMedicalImagingTechnique ||--|o RdfsLiteral : "rdfs_label"
SdosMedicalImagingTechnique ||--|o SdosURL : "sdos_isPartOf"
SdosMedicalImagingTechnique ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosMedicalObservationalStudyDesign ||--|o RdfsLiteral : "rdfs_comment"
SdosMedicalObservationalStudyDesign ||--|o RdfsLiteral : "rdfs_label"
SdosMedicalObservationalStudyDesign ||--|o SdosURL : "sdos_isPartOf"
SdosMedicalObservationalStudyDesign ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosMedicalProcedureType ||--|o RdfsLiteral : "rdfs_comment"
SdosMedicalProcedureType ||--|o RdfsLiteral : "rdfs_label"
SdosMedicalProcedureType ||--|o SdosURL : "sdos_isPartOf"
SdosMedicalProcedureType ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosMedicalSpecialty ||--|o RdfsLiteral : "rdfs_label"
SdosMedicalSpecialty ||--|o SdosURL : "sdos_isPartOf"
SdosMedicalSpecialty ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosMedicalSpecialty ||--|o RdfsLiteral : "rdfs_comment"
SdosMedicalSpecialty ||--|o SdosMerchantReturnEnumeration : "sdos_supersededBy"
SdosMedicalSpecialty ||--|o SdosEnumeration : "sdos_supersededBy"
SdosMedicalSpecialty ||--|o SdosProperty : "sdos_supersededBy"
SdosMedicalSpecialty ||--|o SdosMedicalSpecialty : "sdos_supersededBy"
SdosMedicalSpecialty ||--|o SdosClass : "sdos_supersededBy"
SdosMedicalSpecialty ||--|o RdfsClass : "rdfs_subClassOf"
SdosMedicalStudyStatus ||--|o RdfsLiteral : "rdfs_comment"
SdosMedicalStudyStatus ||--|o RdfsLiteral : "rdfs_label"
SdosMedicalStudyStatus ||--|o SdosURL : "sdos_isPartOf"
SdosMedicalStudyStatus ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosMedicalTrialDesign ||--|o RdfsLiteral : "rdfs_comment"
SdosMedicalTrialDesign ||--|o RdfsLiteral : "rdfs_label"
SdosMedicalTrialDesign ||--|o SdosURL : "sdos_isPartOf"
SdosMedicalTrialDesign ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosMedicineSystem ||--|o RdfsLiteral : "rdfs_comment"
SdosMedicineSystem ||--|o RdfsLiteral : "rdfs_label"
SdosMedicineSystem ||--|o SdosURL : "sdos_isPartOf"
SdosMedicineSystem ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosMerchantReturnEnumeration ||--|o RdfsLiteral : "rdfs_comment"
SdosMerchantReturnEnumeration ||--|o RdfsLiteral : "rdfs_label"
SdosMerchantReturnEnumeration ||--|o SdosURL : "sdos_isPartOf"
SdosMerchantReturnEnumeration ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosMusicAlbumProductionType ||--|o SdosOrganization : "sdos_contributor"
SdosMusicAlbumProductionType ||--|o SdosPerson : "sdos_contributor"
SdosMusicAlbumProductionType ||--|o RdfsLiteral : "rdfs_comment"
SdosMusicAlbumProductionType ||--|o RdfsLiteral : "rdfs_label"
SdosMusicAlbumReleaseType ||--|o SdosOrganization : "sdos_contributor"
SdosMusicAlbumReleaseType ||--|o SdosPerson : "sdos_contributor"
SdosMusicAlbumReleaseType ||--|o RdfsLiteral : "rdfs_comment"
SdosMusicAlbumReleaseType ||--|o RdfsLiteral : "rdfs_label"
SdosMusicReleaseFormatType ||--|o SdosOrganization : "sdos_contributor"
SdosMusicReleaseFormatType ||--|o SdosPerson : "sdos_contributor"
SdosMusicReleaseFormatType ||--|o RdfsLiteral : "rdfs_comment"
SdosMusicReleaseFormatType ||--|o RdfsLiteral : "rdfs_label"
SdosNLNonprofitType ||--|o RdfsLiteral : "rdfs_comment"
SdosNLNonprofitType ||--|o RdfsLiteral : "rdfs_label"
SdosNLNonprofitType ||--|o SdosURL : "sdos_isPartOf"
SdosNLNonprofitType ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosOfferItemCondition ||--|o RdfsLiteral : "rdfs_comment"
SdosOfferItemCondition ||--|o RdfsLiteral : "rdfs_label"
SdosOrderStatus ||--|o RdfsLiteral : "rdfs_comment"
SdosOrderStatus ||--|o RdfsLiteral : "rdfs_label"
SdosPaymentMethodType ||--|o RdfsLiteral : "rdfs_comment"
SdosPaymentMethodType ||--|o RdfsLiteral : "rdfs_label"
SdosPaymentStatusType ||--|o RdfsLiteral : "rdfs_comment"
SdosPaymentStatusType ||--|o RdfsLiteral : "rdfs_label"
SdosPhysicalActivityCategory ||--|o RdfsLiteral : "rdfs_comment"
SdosPhysicalActivityCategory ||--|o RdfsLiteral : "rdfs_label"
SdosPhysicalActivityCategory ||--|o SdosURL : "sdos_isPartOf"
SdosPhysicalActivityCategory ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosPhysicalExam ||--|o RdfsLiteral : "rdfs_comment"
SdosPhysicalExam ||--|o RdfsLiteral : "rdfs_label"
SdosPhysicalExam ||--|o SdosURL : "sdos_isPartOf"
SdosPhysicalExam ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosPriceComponentTypeEnumeration ||--|o RdfsLiteral : "rdfs_comment"
SdosPriceComponentTypeEnumeration ||--|o RdfsLiteral : "rdfs_label"
SdosPriceComponentTypeEnumeration ||--|o SdosURL : "sdos_isPartOf"
SdosPriceComponentTypeEnumeration ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosPriceTypeEnumeration ||--|o RdfsLiteral : "rdfs_comment"
SdosPriceTypeEnumeration ||--|o RdfsLiteral : "rdfs_label"
SdosPriceTypeEnumeration ||--|o SdosURL : "sdos_isPartOf"
SdosPriceTypeEnumeration ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosProductReturnEnumeration ||--|o RdfsLiteral : "rdfs_label"
SdosProductReturnEnumeration ||--|o SdosURL : "sdos_isPartOf"
SdosProductReturnEnumeration ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosProductReturnEnumeration ||--|o RdfsLiteral : "rdfs_comment"
SdosProductReturnEnumeration ||--|o SdosMerchantReturnEnumeration : "sdos_supersededBy"
SdosProductReturnEnumeration ||--|o SdosEnumeration : "sdos_supersededBy"
SdosProductReturnEnumeration ||--|o SdosProperty : "sdos_supersededBy"
SdosProductReturnEnumeration ||--|o SdosMedicalSpecialty : "sdos_supersededBy"
SdosProductReturnEnumeration ||--|o SdosClass : "sdos_supersededBy"
SdosPurchaseType ||--|o RdfsLiteral : "rdfs_comment"
SdosPurchaseType ||--|o RdfsLiteral : "rdfs_label"
SdosPurchaseType ||--|o SdosURL : "sdos_isPartOf"
SdosPurchaseType ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosRefundTypeEnumeration ||--|o RdfsLiteral : "rdfs_comment"
SdosRefundTypeEnumeration ||--|o RdfsLiteral : "rdfs_label"
SdosRefundTypeEnumeration ||--|o SdosURL : "sdos_isPartOf"
SdosRefundTypeEnumeration ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosReservationStatusType ||--|o RdfsLiteral : "rdfs_comment"
SdosReservationStatusType ||--|o RdfsLiteral : "rdfs_label"
SdosRestrictedDiet ||--|o RdfsLiteral : "rdfs_comment"
SdosRestrictedDiet ||--|o RdfsLiteral : "rdfs_label"
SdosReturnFeesEnumeration ||--|o RdfsLiteral : "rdfs_comment"
SdosReturnFeesEnumeration ||--|o RdfsLiteral : "rdfs_label"
SdosReturnFeesEnumeration ||--|o SdosURL : "sdos_isPartOf"
SdosReturnFeesEnumeration ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosReturnLabelSourceEnumeration ||--|o RdfsLiteral : "rdfs_comment"
SdosReturnLabelSourceEnumeration ||--|o RdfsLiteral : "rdfs_label"
SdosReturnLabelSourceEnumeration ||--|o SdosURL : "sdos_isPartOf"
SdosReturnLabelSourceEnumeration ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosReturnMethodEnumeration ||--|o RdfsLiteral : "rdfs_comment"
SdosReturnMethodEnumeration ||--|o RdfsLiteral : "rdfs_label"
SdosReturnMethodEnumeration ||--|o SdosURL : "sdos_isPartOf"
SdosReturnMethodEnumeration ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosRsvpResponseType ||--|o RdfsLiteral : "rdfs_comment"
SdosRsvpResponseType ||--|o RdfsLiteral : "rdfs_label"
SdosSizeSystemEnumeration ||--|o RdfsLiteral : "rdfs_comment"
SdosSizeSystemEnumeration ||--|o RdfsLiteral : "rdfs_label"
SdosSizeSystemEnumeration ||--|o SdosURL : "sdos_isPartOf"
SdosSizeSystemEnumeration ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosSteeringPositionValue ||--|o SdosOrganization : "sdos_contributor"
SdosSteeringPositionValue ||--|o SdosPerson : "sdos_contributor"
SdosSteeringPositionValue ||--|o RdfsLiteral : "rdfs_comment"
SdosSteeringPositionValue ||--|o RdfsLiteral : "rdfs_label"
SdosTierBenefitEnumeration ||--|o RdfsLiteral : "rdfs_comment"
SdosTierBenefitEnumeration ||--|o RdfsLiteral : "rdfs_label"
SdosTierBenefitEnumeration ||--|o SdosURL : "sdos_isPartOf"
SdosTierBenefitEnumeration ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosUKNonprofitType ||--|o RdfsLiteral : "rdfs_comment"
SdosUKNonprofitType ||--|o RdfsLiteral : "rdfs_label"
SdosUKNonprofitType ||--|o SdosURL : "sdos_isPartOf"
SdosUKNonprofitType ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosUSNonprofitType ||--|o RdfsLiteral : "rdfs_comment"
SdosUSNonprofitType ||--|o RdfsLiteral : "rdfs_label"
SdosUSNonprofitType ||--|o SdosURL : "sdos_isPartOf"
SdosUSNonprofitType ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosWearableMeasurementTypeEnumeration ||--|o RdfsLiteral : "rdfs_comment"
SdosWearableMeasurementTypeEnumeration ||--|o RdfsLiteral : "rdfs_label"
SdosWearableMeasurementTypeEnumeration ||--|o SdosURL : "sdos_isPartOf"
SdosWearableMeasurementTypeEnumeration ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosWearableSizeGroupEnumeration ||--|o RdfsLiteral : "rdfs_comment"
SdosWearableSizeGroupEnumeration ||--|o RdfsLiteral : "rdfs_label"
SdosWearableSizeGroupEnumeration ||--|o SdosURL : "sdos_isPartOf"
SdosWearableSizeGroupEnumeration ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosWearableSizeSystemEnumeration ||--|o RdfsLiteral : "rdfs_comment"
SdosWearableSizeSystemEnumeration ||--|o RdfsLiteral : "rdfs_label"
SdosWearableSizeSystemEnumeration ||--|o SdosURL : "sdos_isPartOf"
SdosWearableSizeSystemEnumeration ||--|o SdosCreativeWork : "sdos_isPartOf"
VaemGraphMetaData ||--|o VaemGraphRole : "vaem_hasGraphRole"
VaemGraphMetaData ||--|o VaemParty : "vaem_hasOwner"
VaemGraphMetaData ||--|o RdfsLiteral : "dct_title"
VaemGraphMetaData ||--|o OwlAnnotationProperty : "vaem_usesNonImportedResource"
VaemGraphMetaData ||--|o RdfsResource : "vaem_usesNonImportedResource"
VaemGraphMetaData ||--|o RdfsLiteral : "dct_created"
VaemGraphMetaData ||--|o VaemParty : "vaem_hasSteward"
VaemGraphMetaData ||--|o RdfsLiteral : "rdfs_label"
VaemGraphMetaData ||--|o OwlOntology : "rdfs_isDefinedBy"
VaemGraphMetaData ||--|o RdfsResource : "rdfs_isDefinedBy"
VaemGraphMetaData ||--|o RdfsLiteral : "dct_modified"
VaemGraphRole ||--|o RdfsLiteral : "rdfs_label"
VaemGraphRole ||--|o OwlOntology : "rdfs_isDefinedBy"
VaemGraphRole ||--|o RdfsResource : "rdfs_isDefinedBy"
VaemParty ||--|o RdfsLiteral : "rdfs_label"
VaemParty ||--|o OwlOntology : "rdfs_isDefinedBy"
VaemParty ||--|o RdfsResource : "rdfs_isDefinedBy"
TimeDayOfWeek ||--|o RdfsLiteral : "rdfs_label"
TimeTemporalUnit ||--|o RdfsLiteral : "rdfs_label"
AdmsSemanticAssetDistribution ||--|o SkosConcept : "adms_status"
RdfDatatypeProperty ||--|o RdfsClass : "rdfs_domain"
RdfDatatypeProperty ||--|o RdfsLiteral : "rdfs_comment"
RdfDatatypeProperty ||--|o RdfsLiteral : "rdfs_label"
VaemCatalogEntry ||--|o OwlOntology : "rdfs_isDefinedBy"
VaemCatalogEntry ||--|o RdfsResource : "rdfs_isDefinedBy"
VaemCatalogEntry ||--|o RdfsLiteral : "rdfs_label"
VoagAttribution ||--|o RdfsLiteral : "rdfs_label"
VoagAttribution ||--|o VoagLogo : "voag_hasLogo"
VoagAttribution ||--|o VoagAttributionLogo : "voag_hasLogo"
VoagAttribution ||--|o VoagOrganizationLogo : "voag_hasLogo"
VoagAttribution ||--|o OwlOntology : "rdfs_isDefinedBy"
VoagAttribution ||--|o RdfsResource : "rdfs_isDefinedBy"
VoagAttributionLogo ||--|o RdfsLiteral : "rdfs_label"
VoagAttributionLogo ||--|o OwlOntology : "rdfs_isDefinedBy"
VoagAttributionLogo ||--|o RdfsResource : "rdfs_isDefinedBy"
VoagChangeFrequency ||--|o XsdAnySimpleType : "dtype_value"
VoagChangeFrequency ||--|o OwlOntology : "rdfs_isDefinedBy"
VoagChangeFrequency ||--|o RdfsResource : "rdfs_isDefinedBy"
VoagChangeFrequency ||--|o RdfsLiteral : "rdfs_label"
VoagChangeType ||--|o OwlOntology : "rdfs_isDefinedBy"
VoagChangeType ||--|o RdfsResource : "rdfs_isDefinedBy"
VoagChangeType ||--|o RdfsLiteral : "rdfs_label"
VoagConfidentialityLevel ||--|o RdfsLiteral : "rdfs_label"
VoagConfidentialityLevel ||--|o XsdAnySimpleType : "dtype_code"
VoagConfidentialityLevel ||--|o XsdAnySimpleType : "dtype_value"
VoagConfidentialityLevel ||--|o OwlOntology : "rdfs_isDefinedBy"
VoagConfidentialityLevel ||--|o RdfsResource : "rdfs_isDefinedBy"
VoagCreativeCommonsPermission ||--|o OwlOntology : "rdfs_isDefinedBy"
VoagCreativeCommonsPermission ||--|o RdfsResource : "rdfs_isDefinedBy"
VoagCreativeCommonsPermission ||--|o RdfsLiteral : "rdfs_label"
VoagCreativeCommonsProhibition ||--|o OwlOntology : "rdfs_isDefinedBy"
VoagCreativeCommonsProhibition ||--|o RdfsResource : "rdfs_isDefinedBy"
VoagCreativeCommonsProhibition ||--|o RdfsLiteral : "rdfs_label"
VoagCreativeCommonsRequirement ||--|o OwlOntology : "rdfs_isDefinedBy"
VoagCreativeCommonsRequirement ||--|o RdfsResource : "rdfs_isDefinedBy"
VoagCreativeCommonsRequirement ||--|o RdfsLiteral : "rdfs_label"
VoagGovernance ||--|o OwlOntology : "rdfs_isDefinedBy"
VoagGovernance ||--|o RdfsResource : "rdfs_isDefinedBy"
VoagGovernance ||--|o RdfsLiteral : "rdfs_label"
VoagGovernanceRole ||--|o XsdAnySimpleType : "dtype_value"
VoagGovernanceRole ||--|o OwlOntology : "rdfs_isDefinedBy"
VoagGovernanceRole ||--|o RdfsResource : "rdfs_isDefinedBy"
VoagGovernanceRole ||--|o RdfsLiteral : "rdfs_label"
VoagIcon ||--|o RdfsLiteral : "rdfs_label"
VoagIcon ||--|o OwlOntology : "rdfs_isDefinedBy"
VoagIcon ||--|o RdfsResource : "rdfs_isDefinedBy"
VoagIssueStatus ||--|o XsdAnySimpleType : "dtype_value"
VoagIssueStatus ||--|o OwlOntology : "rdfs_isDefinedBy"
VoagIssueStatus ||--|o RdfsResource : "rdfs_isDefinedBy"
VoagIssueStatus ||--|o RdfsLiteral : "rdfs_label"
VoagLicenseModel ||--|o OwlOntology : "rdfs_isDefinedBy"
VoagLicenseModel ||--|o RdfsResource : "rdfs_isDefinedBy"
VoagLicenseModel ||--|o RdfsLiteral : "rdfs_label"
VoagLogo ||--|o RdfsLiteral : "rdfs_label"
VoagLogo ||--|o OwlOntology : "rdfs_isDefinedBy"
VoagLogo ||--|o RdfsResource : "rdfs_isDefinedBy"
VoagMaturity ||--|o OwlOntology : "rdfs_isDefinedBy"
VoagMaturity ||--|o RdfsResource : "rdfs_isDefinedBy"
VoagMaturity ||--|o RdfsLiteral : "rdfs_label"
VoagOrganizationLogo ||--|o RdfsLiteral : "rdfs_label"
VoagOrganizationLogo ||--|o OwlOntology : "rdfs_isDefinedBy"
VoagOrganizationLogo ||--|o RdfsResource : "rdfs_isDefinedBy"
VoagPedigree ||--|o OwlOntology : "rdfs_isDefinedBy"
VoagPedigree ||--|o RdfsResource : "rdfs_isDefinedBy"
VoagPedigree ||--|o RdfsLiteral : "rdfs_label"
VoagPriorityValue ||--|o XsdAnySimpleType : "dtype_value"
VoagPriorityValue ||--|o OwlOntology : "rdfs_isDefinedBy"
VoagPriorityValue ||--|o RdfsResource : "rdfs_isDefinedBy"
VoagPriorityValue ||--|o RdfsLiteral : "rdfs_label"
VoagProductLogo ||--|o RdfsLiteral : "rdfs_label"
VoagProductLogo ||--|o OwlOntology : "rdfs_isDefinedBy"
VoagProductLogo ||--|o RdfsResource : "rdfs_isDefinedBy"
VoagProvenance ||--|o OwlOntology : "rdfs_isDefinedBy"
VoagProvenance ||--|o RdfsResource : "rdfs_isDefinedBy"
VoagProvenance ||--|o RdfsLiteral : "rdfs_label"
VoagPublicationStatus ||--|o XsdAnySimpleType : "dtype_value"
VoagPublicationStatus ||--|o OwlOntology : "rdfs_isDefinedBy"
VoagPublicationStatus ||--|o RdfsResource : "rdfs_isDefinedBy"
VoagPublicationStatus ||--|o RdfsLiteral : "rdfs_label"
VoagSchemaGraph ||--|o OwlOntology : "rdfs_isDefinedBy"
VoagSchemaGraph ||--|o RdfsResource : "rdfs_isDefinedBy"
VoagSchemaGraph ||--|o RdfsLiteral : "rdfs_label"
KwgoAirPollutant ||--|o RdfsLiteral : "rdfs_label"
KwgoBlueskyWildfireObservableProperty ||--|o RdfsLiteral : "rdfs_label"
KwgoCensusObservableProperty ||--|o RdfsLiteral : "rdfs_comment"
KwgoCensusObservableProperty ||--|o RdfsLiteral : "rdfs_label"
KwgoCensusObservableProperty ||--|o OwlOntology : "rdfs_isDefinedBy"
KwgoCensusObservableProperty ||--|o RdfsResource : "rdfs_isDefinedBy"
KwgoClimateObservableProperty ||--|o RdfsLiteral : "rdfs_label"
KwgoCroplandObservableProperty ||--|o RdfsLiteral : "rdfs_label"
KwgoDroughtIntensity ||--|o RdfsLiteral : "rdfs_label"
KwgoFireCause ||--|o RdfsLiteral : "rdfs_label"
KwgoHelipadAvailability ||--|o RdfsLiteral : "rdfs_label"
KwgoHospitalStatus ||--|o RdfsLiteral : "rdfs_label"
KwgoHospitalType ||--|o RdfsLiteral : "rdfs_label"
KwgoImpactObservableProperty ||--|o RdfsLiteral : "rdfs_label"
KwgoLSADArea ||--|o RdfsLiteral : "rdfs_comment"
KwgoLSADArea ||--|o RdfsLiteral : "rdfs_label"
KwgoMTBSFireObservableProperty ||--|o RdfsLiteral : "rdfs_comment"
KwgoMTBSFireObservableProperty ||--|o RdfsLiteral : "rdfs_label"
KwgoMagnitudeObservableProperty ||--|o RdfsLiteral : "rdfs_label"
KwgoNIFCFireObservableProperty ||--|o RdfsLiteral : "rdfs_label"
KwgoPublicHealthObservableProperty ||--|o RdfsLiteral : "rdfs_label"
KwgoRoadType ||--|o RdfsLiteral : "rdfs_label"
KwgoSmokePlumeObservableProperty ||--|o RdfsLiteral : "rdfs_label"
KwgoSoilMapUnitObservableProperty ||--|o RdfsLiteral : "rdfs_comment"
KwgoSoilMapUnitObservableProperty ||--|o RdfsLiteral : "rdfs_label"
KwgoStormTrackObservableProperty ||--|o RdfsLiteral : "rdfs_label"
KwgoStormTrackletObservableProperty ||--|o RdfsLiteral : "rdfs_label"
KwgoVulnerabilityObservableProperty ||--|o RdfsLiteral : "rdfs_label"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o OwlThing : "owl_sameAs"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o OwlThing : "http___nhdplusv2.spatialai.org_v1_nhdplusv2#hasFlowPathLength"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o HttpNhdplusv2.spatialai.orgV1Nhdplusv2#FlowPathLength : "http___nhdplusv2.spatialai.org_v1_nhdplusv2#hasFlowPathLength"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o RdfsLiteral : "dct_title"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o GeoFeature : "hyf_downstreamFlowPathTC"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o OwlThing : "hyf_downstreamFlowPathTC"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o HyfHYCatchmentRealization : "hyf_downstreamFlowPathTC"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o GeoSpatialObject : "hyf_downstreamFlowPathTC"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o HttpHyfo.spatialai.orgV1Hyfo#WaterFeatureRepresentation : "hyf_downstreamFlowPathTC"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o B805a9e7d30eaabcb686b8ce670ed1e95 : "hyf_downstreamFlowPathTC"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o HyfHYElementaryFlowPath : "hyf_downstreamFlowPathTC"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o HyfHYFlowPath : "hyf_downstreamFlowPathTC"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o SdosText : "sdos_name"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o GeoGeometry : "geo_hasGeometry"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o GeoFeature : "hyf_downstreamFlowPath"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o OwlThing : "hyf_downstreamFlowPath"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o HyfHYCatchmentRealization : "hyf_downstreamFlowPath"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o GeoSpatialObject : "hyf_downstreamFlowPath"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o HttpHyfo.spatialai.orgV1Hyfo#WaterFeatureRepresentation : "hyf_downstreamFlowPath"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o B805a9e7d30eaabcb686b8ce670ed1e95 : "hyf_downstreamFlowPath"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o HyfHYElementaryFlowPath : "hyf_downstreamFlowPath"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o HyfHYFlowPath : "hyf_downstreamFlowPath"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o GeoGeometry : "geo_defaultGeometry"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o RdfsLiteral : "rdfs_label"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o UsSdwisPublicWaterSystem-GW : "spatial_spatiallyRelatedTo"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "spatial_spatiallyRelatedTo"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o UsSdwisPublicWaterSystem-SW : "spatial_spatiallyRelatedTo"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o UsSdwisPWS-ServiceArea : "spatial_spatiallyRelatedTo"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "spatial_spatiallyRelatedTo"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o OwlThing : "spatial_spatiallyRelatedTo"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o HyfHYWaterBody : "spatial_spatiallyRelatedTo"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o UsSdwisPublicWaterSystem-NTNCWS : "spatial_spatiallyRelatedTo"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o MeMgsMGS-Well : "spatial_spatiallyRelatedTo"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o KwgoS2CellLevel13 : "spatial_spatiallyRelatedTo"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o B805a9e7d30eaabcb686b8ce670ed1e95 : "spatial_spatiallyRelatedTo"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o HyfHYHydroFeature : "spatial_spatiallyRelatedTo"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o KwgoAdministrativeRegion3 : "spatial_spatiallyRelatedTo"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o UsSdwisPublicWaterSystem-CWS : "spatial_spatiallyRelatedTo"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o GeoFeature : "spatial_spatiallyRelatedTo"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o HyfHYLake : "spatial_spatiallyRelatedTo"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o GeoSpatialObject : "spatial_spatiallyRelatedTo"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o HyfHYElementaryFlowPath : "spatial_spatiallyRelatedTo"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o KwgoAdministrativeRegion2 : "spatial_spatiallyRelatedTo"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o UsSdwisPublicWaterSystem-TNCWS : "spatial_spatiallyRelatedTo"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o KwgoRegion : "spatial_spatiallyRelatedTo"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o KwgoAdministrativeRegion : "spatial_spatiallyRelatedTo"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o UsSdwisPublicWaterSystem-GW : "spatial_connectedTo"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "spatial_connectedTo"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o UsSdwisPublicWaterSystem-SW : "spatial_connectedTo"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o UsSdwisPWS-ServiceArea : "spatial_connectedTo"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "spatial_connectedTo"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o OwlThing : "spatial_connectedTo"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o HyfHYWaterBody : "spatial_connectedTo"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o UsSdwisPublicWaterSystem-NTNCWS : "spatial_connectedTo"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o MeMgsMGS-Well : "spatial_connectedTo"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o KwgoS2CellLevel13 : "spatial_connectedTo"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o B805a9e7d30eaabcb686b8ce670ed1e95 : "spatial_connectedTo"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o HyfHYHydroFeature : "spatial_connectedTo"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o KwgoAdministrativeRegion3 : "spatial_connectedTo"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o UsSdwisPublicWaterSystem-CWS : "spatial_connectedTo"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o GeoFeature : "spatial_connectedTo"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o HyfHYLake : "spatial_connectedTo"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o GeoSpatialObject : "spatial_connectedTo"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o HyfHYElementaryFlowPath : "spatial_connectedTo"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o KwgoAdministrativeRegion2 : "spatial_connectedTo"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o UsSdwisPublicWaterSystem-TNCWS : "spatial_connectedTo"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o KwgoRegion : "spatial_connectedTo"
B805a9e7d30eaabcb686b8ce670ed1e95 ||--|o KwgoAdministrativeRegion : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o OwlThing : "owl_sameAs"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o OwlThing : "http___gwml2.org_def_gwml2#gwAquiferSystem"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o GeoSpatialObject : "http___gwml2.org_def_gwml2#gwAquiferSystem"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "http___gwml2.org_def_gwml2#gwAquiferSystem"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o GeoGeometry : "geo_defaultGeometry"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o RdfsLiteral : "rdfs_label"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o UsSdwisPublicWaterSystem-GW : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o UsSdwisPublicWaterSystem-SW : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o UsSdwisPWS-ServiceArea : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o OwlThing : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o HyfHYWaterBody : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o UsSdwisPublicWaterSystem-NTNCWS : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o MeMgsMGS-Well : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o KwgoS2CellLevel13 : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o B805a9e7d30eaabcb686b8ce670ed1e95 : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o HyfHYHydroFeature : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o KwgoAdministrativeRegion3 : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o UsSdwisPublicWaterSystem-CWS : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o GeoFeature : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o HyfHYLake : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o GeoSpatialObject : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o HyfHYElementaryFlowPath : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o KwgoAdministrativeRegion2 : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o UsSdwisPublicWaterSystem-TNCWS : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o KwgoRegion : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o KwgoAdministrativeRegion : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o UsSdwisPublicWaterSystem-GW : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o UsSdwisPublicWaterSystem-SW : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o UsSdwisPWS-ServiceArea : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o OwlThing : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o HyfHYWaterBody : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o UsSdwisPublicWaterSystem-NTNCWS : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o MeMgsMGS-Well : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o KwgoS2CellLevel13 : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o B805a9e7d30eaabcb686b8ce670ed1e95 : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o HyfHYHydroFeature : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o KwgoAdministrativeRegion3 : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o UsSdwisPublicWaterSystem-CWS : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o GeoFeature : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o HyfHYLake : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o GeoSpatialObject : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o HyfHYElementaryFlowPath : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o KwgoAdministrativeRegion2 : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o UsSdwisPublicWaterSystem-TNCWS : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o KwgoRegion : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o KwgoAdministrativeRegion : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o GeoGeometry : "geo_hasGeometry"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o OwlThing : "owl_sameAs"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o GeoGeometry : "geo_defaultGeometry"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o OwlThing : "http___gwml2.org_def_gwml2#gwAquiferSystemPart"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o GeoSpatialObject : "http___gwml2.org_def_gwml2#gwAquiferSystemPart"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "http___gwml2.org_def_gwml2#gwAquiferSystemPart"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o RdfsLiteral : "rdfs_comment"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o RdfsLiteral : "rdfs_label"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o UsSdwisPublicWaterSystem-GW : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o UsSdwisPublicWaterSystem-SW : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o UsSdwisPWS-ServiceArea : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o OwlThing : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o HyfHYWaterBody : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o UsSdwisPublicWaterSystem-NTNCWS : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o MeMgsMGS-Well : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o KwgoS2CellLevel13 : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o B805a9e7d30eaabcb686b8ce670ed1e95 : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o HyfHYHydroFeature : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o KwgoAdministrativeRegion3 : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o UsSdwisPublicWaterSystem-CWS : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o GeoFeature : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o HyfHYLake : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o GeoSpatialObject : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o HyfHYElementaryFlowPath : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o KwgoAdministrativeRegion2 : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o UsSdwisPublicWaterSystem-TNCWS : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o KwgoRegion : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o KwgoAdministrativeRegion : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o UsSdwisPublicWaterSystem-GW : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o UsSdwisPublicWaterSystem-SW : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o UsSdwisPWS-ServiceArea : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o OwlThing : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o HyfHYWaterBody : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o UsSdwisPublicWaterSystem-NTNCWS : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o MeMgsMGS-Well : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o KwgoS2CellLevel13 : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o B805a9e7d30eaabcb686b8ce670ed1e95 : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o HyfHYHydroFeature : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o KwgoAdministrativeRegion3 : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o UsSdwisPublicWaterSystem-CWS : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o GeoFeature : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o HyfHYLake : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o GeoSpatialObject : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o HyfHYElementaryFlowPath : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o KwgoAdministrativeRegion2 : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o UsSdwisPublicWaterSystem-TNCWS : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o KwgoRegion : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o KwgoAdministrativeRegion : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o GeoGeometry : "geo_hasGeometry"
HttpNhdplusv2.spatialai.orgV1Nhdplusv2#FlowPathLength ||--|o OwlThing : "owl_sameAs"
HttpNhdplusv2.spatialai.orgV1Nhdplusv2#FlowPathLength ||--|o QudtQuantityValue : "qudt_quantityValue"
HyfHYElementaryFlowPath ||--|o OwlThing : "owl_sameAs"
HyfHYElementaryFlowPath ||--|o OwlThing : "http___nhdplusv2.spatialai.org_v1_nhdplusv2#hasFlowPathLength"
HyfHYElementaryFlowPath ||--|o HttpNhdplusv2.spatialai.orgV1Nhdplusv2#FlowPathLength : "http___nhdplusv2.spatialai.org_v1_nhdplusv2#hasFlowPathLength"
HyfHYElementaryFlowPath ||--|o RdfsLiteral : "dct_title"
HyfHYElementaryFlowPath ||--|o GeoFeature : "hyf_downstreamFlowPathTC"
HyfHYElementaryFlowPath ||--|o OwlThing : "hyf_downstreamFlowPathTC"
HyfHYElementaryFlowPath ||--|o HyfHYCatchmentRealization : "hyf_downstreamFlowPathTC"
HyfHYElementaryFlowPath ||--|o GeoSpatialObject : "hyf_downstreamFlowPathTC"
HyfHYElementaryFlowPath ||--|o HttpHyfo.spatialai.orgV1Hyfo#WaterFeatureRepresentation : "hyf_downstreamFlowPathTC"
HyfHYElementaryFlowPath ||--|o B805a9e7d30eaabcb686b8ce670ed1e95 : "hyf_downstreamFlowPathTC"
HyfHYElementaryFlowPath ||--|o HyfHYElementaryFlowPath : "hyf_downstreamFlowPathTC"
HyfHYElementaryFlowPath ||--|o HyfHYFlowPath : "hyf_downstreamFlowPathTC"
HyfHYElementaryFlowPath ||--|o SdosText : "sdos_name"
HyfHYElementaryFlowPath ||--|o GeoGeometry : "geo_hasGeometry"
HyfHYElementaryFlowPath ||--|o GeoFeature : "hyf_downstreamFlowPath"
HyfHYElementaryFlowPath ||--|o OwlThing : "hyf_downstreamFlowPath"
HyfHYElementaryFlowPath ||--|o HyfHYCatchmentRealization : "hyf_downstreamFlowPath"
HyfHYElementaryFlowPath ||--|o GeoSpatialObject : "hyf_downstreamFlowPath"
HyfHYElementaryFlowPath ||--|o HttpHyfo.spatialai.orgV1Hyfo#WaterFeatureRepresentation : "hyf_downstreamFlowPath"
HyfHYElementaryFlowPath ||--|o B805a9e7d30eaabcb686b8ce670ed1e95 : "hyf_downstreamFlowPath"
HyfHYElementaryFlowPath ||--|o HyfHYElementaryFlowPath : "hyf_downstreamFlowPath"
HyfHYElementaryFlowPath ||--|o HyfHYFlowPath : "hyf_downstreamFlowPath"
HyfHYElementaryFlowPath ||--|o GeoGeometry : "geo_defaultGeometry"
HyfHYElementaryFlowPath ||--|o RdfsLiteral : "rdfs_label"
HyfHYElementaryFlowPath ||--|o UsSdwisPublicWaterSystem-GW : "spatial_spatiallyRelatedTo"
HyfHYElementaryFlowPath ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "spatial_spatiallyRelatedTo"
HyfHYElementaryFlowPath ||--|o UsSdwisPublicWaterSystem-SW : "spatial_spatiallyRelatedTo"
HyfHYElementaryFlowPath ||--|o UsSdwisPWS-ServiceArea : "spatial_spatiallyRelatedTo"
HyfHYElementaryFlowPath ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "spatial_spatiallyRelatedTo"
HyfHYElementaryFlowPath ||--|o OwlThing : "spatial_spatiallyRelatedTo"
HyfHYElementaryFlowPath ||--|o HyfHYWaterBody : "spatial_spatiallyRelatedTo"
HyfHYElementaryFlowPath ||--|o UsSdwisPublicWaterSystem-NTNCWS : "spatial_spatiallyRelatedTo"
HyfHYElementaryFlowPath ||--|o MeMgsMGS-Well : "spatial_spatiallyRelatedTo"
HyfHYElementaryFlowPath ||--|o KwgoS2CellLevel13 : "spatial_spatiallyRelatedTo"
HyfHYElementaryFlowPath ||--|o B805a9e7d30eaabcb686b8ce670ed1e95 : "spatial_spatiallyRelatedTo"
HyfHYElementaryFlowPath ||--|o HyfHYHydroFeature : "spatial_spatiallyRelatedTo"
HyfHYElementaryFlowPath ||--|o KwgoAdministrativeRegion3 : "spatial_spatiallyRelatedTo"
HyfHYElementaryFlowPath ||--|o UsSdwisPublicWaterSystem-CWS : "spatial_spatiallyRelatedTo"
HyfHYElementaryFlowPath ||--|o GeoFeature : "spatial_spatiallyRelatedTo"
HyfHYElementaryFlowPath ||--|o HyfHYLake : "spatial_spatiallyRelatedTo"
HyfHYElementaryFlowPath ||--|o GeoSpatialObject : "spatial_spatiallyRelatedTo"
HyfHYElementaryFlowPath ||--|o HyfHYElementaryFlowPath : "spatial_spatiallyRelatedTo"
HyfHYElementaryFlowPath ||--|o KwgoAdministrativeRegion2 : "spatial_spatiallyRelatedTo"
HyfHYElementaryFlowPath ||--|o UsSdwisPublicWaterSystem-TNCWS : "spatial_spatiallyRelatedTo"
HyfHYElementaryFlowPath ||--|o KwgoRegion : "spatial_spatiallyRelatedTo"
HyfHYElementaryFlowPath ||--|o KwgoAdministrativeRegion : "spatial_spatiallyRelatedTo"
HyfHYElementaryFlowPath ||--|o UsSdwisPublicWaterSystem-GW : "spatial_connectedTo"
HyfHYElementaryFlowPath ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "spatial_connectedTo"
HyfHYElementaryFlowPath ||--|o UsSdwisPublicWaterSystem-SW : "spatial_connectedTo"
HyfHYElementaryFlowPath ||--|o UsSdwisPWS-ServiceArea : "spatial_connectedTo"
HyfHYElementaryFlowPath ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "spatial_connectedTo"
HyfHYElementaryFlowPath ||--|o OwlThing : "spatial_connectedTo"
HyfHYElementaryFlowPath ||--|o HyfHYWaterBody : "spatial_connectedTo"
HyfHYElementaryFlowPath ||--|o UsSdwisPublicWaterSystem-NTNCWS : "spatial_connectedTo"
HyfHYElementaryFlowPath ||--|o MeMgsMGS-Well : "spatial_connectedTo"
HyfHYElementaryFlowPath ||--|o KwgoS2CellLevel13 : "spatial_connectedTo"
HyfHYElementaryFlowPath ||--|o B805a9e7d30eaabcb686b8ce670ed1e95 : "spatial_connectedTo"
HyfHYElementaryFlowPath ||--|o HyfHYHydroFeature : "spatial_connectedTo"
HyfHYElementaryFlowPath ||--|o KwgoAdministrativeRegion3 : "spatial_connectedTo"
HyfHYElementaryFlowPath ||--|o UsSdwisPublicWaterSystem-CWS : "spatial_connectedTo"
HyfHYElementaryFlowPath ||--|o GeoFeature : "spatial_connectedTo"
HyfHYElementaryFlowPath ||--|o HyfHYLake : "spatial_connectedTo"
HyfHYElementaryFlowPath ||--|o GeoSpatialObject : "spatial_connectedTo"
HyfHYElementaryFlowPath ||--|o HyfHYElementaryFlowPath : "spatial_connectedTo"
HyfHYElementaryFlowPath ||--|o KwgoAdministrativeRegion2 : "spatial_connectedTo"
HyfHYElementaryFlowPath ||--|o UsSdwisPublicWaterSystem-TNCWS : "spatial_connectedTo"
HyfHYElementaryFlowPath ||--|o KwgoRegion : "spatial_connectedTo"
HyfHYElementaryFlowPath ||--|o KwgoAdministrativeRegion : "spatial_connectedTo"
IlIsgsISGS-Well ||--|o IlIsgsWellYield : "il_isgs_wellYield"
IlIsgsISGS-Well ||--|o OwlThing : "owl_sameAs"
IlIsgsISGS-Well ||--|o IlIsgsWellDepthInFt : "il_isgs_wellDepth"
IlIsgsISGS-Well ||--|o RdfsLiteral : "rdfs_label"
IlIsgsISGS-Well ||--|o IlIsgsWellPurpose : "il_isgs_wellPurpose"
IlIsgsISGS-Well ||--|o GeoGeometry : "geo_hasGeometry"
IlIsgsWellDepthInFt ||--|o OwlThing : "owl_sameAs"
IlIsgsWellPurpose ||--|o OwlThing : "owl_sameAs"
IlIsgsWellPurpose ||--|o RdfsLiteral : "rdfs_label"
IlIsgsWellYield ||--|o OwlThing : "owl_sameAs"
KwgoS2CellLevel13 ||--|o OwlThing : "owl_sameAs"
KwgoS2CellLevel13 ||--|o UsSdwisPublicWaterSystem-GW : "spatial_spatiallyRelatedTo"
KwgoS2CellLevel13 ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "spatial_spatiallyRelatedTo"
KwgoS2CellLevel13 ||--|o UsSdwisPublicWaterSystem-SW : "spatial_spatiallyRelatedTo"
KwgoS2CellLevel13 ||--|o UsSdwisPWS-ServiceArea : "spatial_spatiallyRelatedTo"
KwgoS2CellLevel13 ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "spatial_spatiallyRelatedTo"
KwgoS2CellLevel13 ||--|o OwlThing : "spatial_spatiallyRelatedTo"
KwgoS2CellLevel13 ||--|o HyfHYWaterBody : "spatial_spatiallyRelatedTo"
KwgoS2CellLevel13 ||--|o UsSdwisPublicWaterSystem-NTNCWS : "spatial_spatiallyRelatedTo"
KwgoS2CellLevel13 ||--|o MeMgsMGS-Well : "spatial_spatiallyRelatedTo"
KwgoS2CellLevel13 ||--|o KwgoS2CellLevel13 : "spatial_spatiallyRelatedTo"
KwgoS2CellLevel13 ||--|o B805a9e7d30eaabcb686b8ce670ed1e95 : "spatial_spatiallyRelatedTo"
KwgoS2CellLevel13 ||--|o HyfHYHydroFeature : "spatial_spatiallyRelatedTo"
KwgoS2CellLevel13 ||--|o KwgoAdministrativeRegion3 : "spatial_spatiallyRelatedTo"
KwgoS2CellLevel13 ||--|o UsSdwisPublicWaterSystem-CWS : "spatial_spatiallyRelatedTo"
KwgoS2CellLevel13 ||--|o GeoFeature : "spatial_spatiallyRelatedTo"
KwgoS2CellLevel13 ||--|o HyfHYLake : "spatial_spatiallyRelatedTo"
KwgoS2CellLevel13 ||--|o GeoSpatialObject : "spatial_spatiallyRelatedTo"
KwgoS2CellLevel13 ||--|o HyfHYElementaryFlowPath : "spatial_spatiallyRelatedTo"
KwgoS2CellLevel13 ||--|o KwgoAdministrativeRegion2 : "spatial_spatiallyRelatedTo"
KwgoS2CellLevel13 ||--|o UsSdwisPublicWaterSystem-TNCWS : "spatial_spatiallyRelatedTo"
KwgoS2CellLevel13 ||--|o KwgoRegion : "spatial_spatiallyRelatedTo"
KwgoS2CellLevel13 ||--|o KwgoAdministrativeRegion : "spatial_spatiallyRelatedTo"
KwgoS2CellLevel13 ||--|o UsSdwisPublicWaterSystem-GW : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o UsSdwisPublicWaterSystem-SW : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o UsSdwisPWS-ServiceArea : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o OwlThing : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o HyfHYWaterBody : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o UsSdwisPublicWaterSystem-NTNCWS : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o MeMgsMGS-Well : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o KwgoS2CellLevel13 : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o B805a9e7d30eaabcb686b8ce670ed1e95 : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o HyfHYHydroFeature : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o KwgoAdministrativeRegion3 : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o UsSdwisPublicWaterSystem-CWS : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o GeoFeature : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o HyfHYLake : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o GeoSpatialObject : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o HyfHYElementaryFlowPath : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o KwgoAdministrativeRegion2 : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o UsSdwisPublicWaterSystem-TNCWS : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o KwgoRegion : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o KwgoAdministrativeRegion : "spatial_connectedTo"
MeMgsMGS-Well ||--|o OwlThing : "me_mgs_wellDepth"
MeMgsMGS-Well ||--|o StadSingleData : "me_mgs_wellDepth"
MeMgsMGS-Well ||--|o MeMgsWellDepthInFt : "me_mgs_wellDepth"
MeMgsMGS-Well ||--|o OwlThing : "owl_sameAs"
MeMgsMGS-Well ||--|o RdfsLiteral : "rdfs_label"
MeMgsMGS-Well ||--|o OwlThing : "me_mgs_ofWellType"
MeMgsMGS-Well ||--|o MeMgsWellType : "me_mgs_ofWellType"
MeMgsMGS-Well ||--|o OwlThing : "me_mgs_wellOverburden"
MeMgsMGS-Well ||--|o StadSingleData : "me_mgs_wellOverburden"
MeMgsMGS-Well ||--|o MeMgsWellOverburdenThicknessInFt : "me_mgs_wellOverburden"
MeMgsMGS-Well ||--|o OwlThing : "me_mgs_hasUse"
MeMgsMGS-Well ||--|o MeMgsWellUse : "me_mgs_hasUse"
MeMgsMGS-Well ||--|o GeoGeometry : "geo_hasDefaultGeometry"
MeMgsMGS-Well ||--|o UsSdwisPublicWaterSystem-GW : "spatial_spatiallyRelatedTo"
MeMgsMGS-Well ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "spatial_spatiallyRelatedTo"
MeMgsMGS-Well ||--|o UsSdwisPublicWaterSystem-SW : "spatial_spatiallyRelatedTo"
MeMgsMGS-Well ||--|o UsSdwisPWS-ServiceArea : "spatial_spatiallyRelatedTo"
MeMgsMGS-Well ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "spatial_spatiallyRelatedTo"
MeMgsMGS-Well ||--|o OwlThing : "spatial_spatiallyRelatedTo"
MeMgsMGS-Well ||--|o HyfHYWaterBody : "spatial_spatiallyRelatedTo"
MeMgsMGS-Well ||--|o UsSdwisPublicWaterSystem-NTNCWS : "spatial_spatiallyRelatedTo"
MeMgsMGS-Well ||--|o MeMgsMGS-Well : "spatial_spatiallyRelatedTo"
MeMgsMGS-Well ||--|o KwgoS2CellLevel13 : "spatial_spatiallyRelatedTo"
MeMgsMGS-Well ||--|o B805a9e7d30eaabcb686b8ce670ed1e95 : "spatial_spatiallyRelatedTo"
MeMgsMGS-Well ||--|o HyfHYHydroFeature : "spatial_spatiallyRelatedTo"
MeMgsMGS-Well ||--|o KwgoAdministrativeRegion3 : "spatial_spatiallyRelatedTo"
MeMgsMGS-Well ||--|o UsSdwisPublicWaterSystem-CWS : "spatial_spatiallyRelatedTo"
MeMgsMGS-Well ||--|o GeoFeature : "spatial_spatiallyRelatedTo"
MeMgsMGS-Well ||--|o HyfHYLake : "spatial_spatiallyRelatedTo"
MeMgsMGS-Well ||--|o GeoSpatialObject : "spatial_spatiallyRelatedTo"
MeMgsMGS-Well ||--|o HyfHYElementaryFlowPath : "spatial_spatiallyRelatedTo"
MeMgsMGS-Well ||--|o KwgoAdministrativeRegion2 : "spatial_spatiallyRelatedTo"
MeMgsMGS-Well ||--|o UsSdwisPublicWaterSystem-TNCWS : "spatial_spatiallyRelatedTo"
MeMgsMGS-Well ||--|o KwgoRegion : "spatial_spatiallyRelatedTo"
MeMgsMGS-Well ||--|o KwgoAdministrativeRegion : "spatial_spatiallyRelatedTo"
MeMgsMGS-Well ||--|o UsSdwisPublicWaterSystem-GW : "spatial_connectedTo"
MeMgsMGS-Well ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "spatial_connectedTo"
MeMgsMGS-Well ||--|o UsSdwisPublicWaterSystem-SW : "spatial_connectedTo"
MeMgsMGS-Well ||--|o UsSdwisPWS-ServiceArea : "spatial_connectedTo"
MeMgsMGS-Well ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "spatial_connectedTo"
MeMgsMGS-Well ||--|o OwlThing : "spatial_connectedTo"
MeMgsMGS-Well ||--|o HyfHYWaterBody : "spatial_connectedTo"
MeMgsMGS-Well ||--|o UsSdwisPublicWaterSystem-NTNCWS : "spatial_connectedTo"
MeMgsMGS-Well ||--|o MeMgsMGS-Well : "spatial_connectedTo"
MeMgsMGS-Well ||--|o KwgoS2CellLevel13 : "spatial_connectedTo"
MeMgsMGS-Well ||--|o B805a9e7d30eaabcb686b8ce670ed1e95 : "spatial_connectedTo"
MeMgsMGS-Well ||--|o HyfHYHydroFeature : "spatial_connectedTo"
MeMgsMGS-Well ||--|o KwgoAdministrativeRegion3 : "spatial_connectedTo"
MeMgsMGS-Well ||--|o UsSdwisPublicWaterSystem-CWS : "spatial_connectedTo"
MeMgsMGS-Well ||--|o GeoFeature : "spatial_connectedTo"
MeMgsMGS-Well ||--|o HyfHYLake : "spatial_connectedTo"
MeMgsMGS-Well ||--|o GeoSpatialObject : "spatial_connectedTo"
MeMgsMGS-Well ||--|o HyfHYElementaryFlowPath : "spatial_connectedTo"
MeMgsMGS-Well ||--|o KwgoAdministrativeRegion2 : "spatial_connectedTo"
MeMgsMGS-Well ||--|o UsSdwisPublicWaterSystem-TNCWS : "spatial_connectedTo"
MeMgsMGS-Well ||--|o KwgoRegion : "spatial_connectedTo"
MeMgsMGS-Well ||--|o KwgoAdministrativeRegion : "spatial_connectedTo"
MeMgsMGS-Well ||--|o GeoGeometry : "geo_hasGeometry"
MeMgsWellDepthInFt ||--|o OwlThing : "owl_sameAs"
MeMgsWellOverburdenThicknessInFt ||--|o OwlThing : "owl_sameAs"
MeMgsWellType ||--|o OwlThing : "owl_sameAs"
MeMgsWellUse ||--|o OwlThing : "owl_sameAs"
OwlDataProperty ||--|o OwlThing : "owl_sameAs"
OwlDataProperty ||--|o RdfsClass : "rdfs_domain"
UsSdwisPWS-ServiceArea ||--|o OwlThing : "owl_sameAs"
UsSdwisPWS-ServiceArea ||--|o OwlThing : "us_sdwis_serviceAreaType"
UsSdwisPWS-ServiceArea ||--|o UsSdwisPWS-ServiceAreaType : "us_sdwis_serviceAreaType"
UsSdwisPWS-ServiceArea ||--|o GeoGeometry : "geo_hasDefaultGeometry"
UsSdwisPWS-ServiceArea ||--|o UsSdwisPublicWaterSystem-GW : "spatial_spatiallyRelatedTo"
UsSdwisPWS-ServiceArea ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "spatial_spatiallyRelatedTo"
UsSdwisPWS-ServiceArea ||--|o UsSdwisPublicWaterSystem-SW : "spatial_spatiallyRelatedTo"
UsSdwisPWS-ServiceArea ||--|o UsSdwisPWS-ServiceArea : "spatial_spatiallyRelatedTo"
UsSdwisPWS-ServiceArea ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "spatial_spatiallyRelatedTo"
UsSdwisPWS-ServiceArea ||--|o OwlThing : "spatial_spatiallyRelatedTo"
UsSdwisPWS-ServiceArea ||--|o HyfHYWaterBody : "spatial_spatiallyRelatedTo"
UsSdwisPWS-ServiceArea ||--|o UsSdwisPublicWaterSystem-NTNCWS : "spatial_spatiallyRelatedTo"
UsSdwisPWS-ServiceArea ||--|o MeMgsMGS-Well : "spatial_spatiallyRelatedTo"
UsSdwisPWS-ServiceArea ||--|o KwgoS2CellLevel13 : "spatial_spatiallyRelatedTo"
UsSdwisPWS-ServiceArea ||--|o B805a9e7d30eaabcb686b8ce670ed1e95 : "spatial_spatiallyRelatedTo"
UsSdwisPWS-ServiceArea ||--|o HyfHYHydroFeature : "spatial_spatiallyRelatedTo"
UsSdwisPWS-ServiceArea ||--|o KwgoAdministrativeRegion3 : "spatial_spatiallyRelatedTo"
UsSdwisPWS-ServiceArea ||--|o UsSdwisPublicWaterSystem-CWS : "spatial_spatiallyRelatedTo"
UsSdwisPWS-ServiceArea ||--|o GeoFeature : "spatial_spatiallyRelatedTo"
UsSdwisPWS-ServiceArea ||--|o HyfHYLake : "spatial_spatiallyRelatedTo"
UsSdwisPWS-ServiceArea ||--|o GeoSpatialObject : "spatial_spatiallyRelatedTo"
UsSdwisPWS-ServiceArea ||--|o HyfHYElementaryFlowPath : "spatial_spatiallyRelatedTo"
UsSdwisPWS-ServiceArea ||--|o KwgoAdministrativeRegion2 : "spatial_spatiallyRelatedTo"
UsSdwisPWS-ServiceArea ||--|o UsSdwisPublicWaterSystem-TNCWS : "spatial_spatiallyRelatedTo"
UsSdwisPWS-ServiceArea ||--|o KwgoRegion : "spatial_spatiallyRelatedTo"
UsSdwisPWS-ServiceArea ||--|o KwgoAdministrativeRegion : "spatial_spatiallyRelatedTo"
UsSdwisPWS-ServiceArea ||--|o UsSdwisPublicWaterSystem-GW : "spatial_connectedTo"
UsSdwisPWS-ServiceArea ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "spatial_connectedTo"
UsSdwisPWS-ServiceArea ||--|o UsSdwisPublicWaterSystem-SW : "spatial_connectedTo"
UsSdwisPWS-ServiceArea ||--|o UsSdwisPWS-ServiceArea : "spatial_connectedTo"
UsSdwisPWS-ServiceArea ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "spatial_connectedTo"
UsSdwisPWS-ServiceArea ||--|o OwlThing : "spatial_connectedTo"
UsSdwisPWS-ServiceArea ||--|o HyfHYWaterBody : "spatial_connectedTo"
UsSdwisPWS-ServiceArea ||--|o UsSdwisPublicWaterSystem-NTNCWS : "spatial_connectedTo"
UsSdwisPWS-ServiceArea ||--|o MeMgsMGS-Well : "spatial_connectedTo"
UsSdwisPWS-ServiceArea ||--|o KwgoS2CellLevel13 : "spatial_connectedTo"
UsSdwisPWS-ServiceArea ||--|o B805a9e7d30eaabcb686b8ce670ed1e95 : "spatial_connectedTo"
UsSdwisPWS-ServiceArea ||--|o HyfHYHydroFeature : "spatial_connectedTo"
UsSdwisPWS-ServiceArea ||--|o KwgoAdministrativeRegion3 : "spatial_connectedTo"
UsSdwisPWS-ServiceArea ||--|o UsSdwisPublicWaterSystem-CWS : "spatial_connectedTo"
UsSdwisPWS-ServiceArea ||--|o GeoFeature : "spatial_connectedTo"
UsSdwisPWS-ServiceArea ||--|o HyfHYLake : "spatial_connectedTo"
UsSdwisPWS-ServiceArea ||--|o GeoSpatialObject : "spatial_connectedTo"
UsSdwisPWS-ServiceArea ||--|o HyfHYElementaryFlowPath : "spatial_connectedTo"
UsSdwisPWS-ServiceArea ||--|o KwgoAdministrativeRegion2 : "spatial_connectedTo"
UsSdwisPWS-ServiceArea ||--|o UsSdwisPublicWaterSystem-TNCWS : "spatial_connectedTo"
UsSdwisPWS-ServiceArea ||--|o KwgoRegion : "spatial_connectedTo"
UsSdwisPWS-ServiceArea ||--|o KwgoAdministrativeRegion : "spatial_connectedTo"
UsSdwisPWS-ServiceArea ||--|o GeoGeometry : "geo_hasGeometry"
UsSdwisPWS-ServiceAreaType ||--|o OwlThing : "owl_sameAs"
UsSdwisPWS-ServiceAreaType ||--|o RdfsLiteral : "rdfs_label"
UsSdwisPWS-SourceWaterType ||--|o OwlThing : "owl_sameAs"
UsSdwisPWS-SubFeatureActivity ||--|o OwlThing : "owl_sameAs"
UsSdwisPWS-SubFeatureActivity ||--|o RdfsLiteral : "rdfs_label"
UsSdwisPWS-SubFeatureType ||--|o OwlThing : "owl_sameAs"
UsSdwisPWS-SubFeatureType ||--|o RdfsLiteral : "rdfs_label"
UsSdwisPublicWaterSystem-CWS ||--|o OwlThing : "owl_sameAs"
UsSdwisPublicWaterSystem-CWS ||--|o RdfsLiteral : "rdfs_label"
UsSdwisPublicWaterSystem-CWS ||--|o OwlThing : "us_sdwis_primarySourceType"
UsSdwisPublicWaterSystem-CWS ||--|o UsSdwisPWS-SourceWaterType : "us_sdwis_primarySourceType"
UsSdwisPublicWaterSystem-CWS ||--|o RdfsLiteral : "us_sdwis_pwsName"
UsSdwisPublicWaterSystem-CWS ||--|o UsSdwisPublicWaterSystem-GW : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-CWS ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-CWS ||--|o UsSdwisPublicWaterSystem-SW : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-CWS ||--|o UsSdwisPWS-ServiceArea : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-CWS ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-CWS ||--|o OwlThing : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-CWS ||--|o HyfHYWaterBody : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-CWS ||--|o UsSdwisPublicWaterSystem-NTNCWS : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-CWS ||--|o MeMgsMGS-Well : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-CWS ||--|o KwgoS2CellLevel13 : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-CWS ||--|o B805a9e7d30eaabcb686b8ce670ed1e95 : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-CWS ||--|o HyfHYHydroFeature : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-CWS ||--|o KwgoAdministrativeRegion3 : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-CWS ||--|o UsSdwisPublicWaterSystem-CWS : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-CWS ||--|o GeoFeature : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-CWS ||--|o HyfHYLake : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-CWS ||--|o GeoSpatialObject : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-CWS ||--|o HyfHYElementaryFlowPath : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-CWS ||--|o KwgoAdministrativeRegion2 : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-CWS ||--|o UsSdwisPublicWaterSystem-TNCWS : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-CWS ||--|o KwgoRegion : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-CWS ||--|o KwgoAdministrativeRegion : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-CWS ||--|o UsSdwisPublicWaterSystem-GW : "spatial_connectedTo"
UsSdwisPublicWaterSystem-CWS ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "spatial_connectedTo"
UsSdwisPublicWaterSystem-CWS ||--|o UsSdwisPublicWaterSystem-SW : "spatial_connectedTo"
UsSdwisPublicWaterSystem-CWS ||--|o UsSdwisPWS-ServiceArea : "spatial_connectedTo"
UsSdwisPublicWaterSystem-CWS ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "spatial_connectedTo"
UsSdwisPublicWaterSystem-CWS ||--|o OwlThing : "spatial_connectedTo"
UsSdwisPublicWaterSystem-CWS ||--|o HyfHYWaterBody : "spatial_connectedTo"
UsSdwisPublicWaterSystem-CWS ||--|o UsSdwisPublicWaterSystem-NTNCWS : "spatial_connectedTo"
UsSdwisPublicWaterSystem-CWS ||--|o MeMgsMGS-Well : "spatial_connectedTo"
UsSdwisPublicWaterSystem-CWS ||--|o KwgoS2CellLevel13 : "spatial_connectedTo"
UsSdwisPublicWaterSystem-CWS ||--|o B805a9e7d30eaabcb686b8ce670ed1e95 : "spatial_connectedTo"
UsSdwisPublicWaterSystem-CWS ||--|o HyfHYHydroFeature : "spatial_connectedTo"
UsSdwisPublicWaterSystem-CWS ||--|o KwgoAdministrativeRegion3 : "spatial_connectedTo"
UsSdwisPublicWaterSystem-CWS ||--|o UsSdwisPublicWaterSystem-CWS : "spatial_connectedTo"
UsSdwisPublicWaterSystem-CWS ||--|o GeoFeature : "spatial_connectedTo"
UsSdwisPublicWaterSystem-CWS ||--|o HyfHYLake : "spatial_connectedTo"
UsSdwisPublicWaterSystem-CWS ||--|o GeoSpatialObject : "spatial_connectedTo"
UsSdwisPublicWaterSystem-CWS ||--|o HyfHYElementaryFlowPath : "spatial_connectedTo"
UsSdwisPublicWaterSystem-CWS ||--|o KwgoAdministrativeRegion2 : "spatial_connectedTo"
UsSdwisPublicWaterSystem-CWS ||--|o UsSdwisPublicWaterSystem-TNCWS : "spatial_connectedTo"
UsSdwisPublicWaterSystem-CWS ||--|o KwgoRegion : "spatial_connectedTo"
UsSdwisPublicWaterSystem-CWS ||--|o KwgoAdministrativeRegion : "spatial_connectedTo"
UsSdwisPublicWaterSystem-CWS ||--|o GeoFeature : "us_sdwis_serviceArea"
UsSdwisPublicWaterSystem-CWS ||--|o OwlThing : "us_sdwis_serviceArea"
UsSdwisPublicWaterSystem-CWS ||--|o GeoSpatialObject : "us_sdwis_serviceArea"
UsSdwisPublicWaterSystem-CWS ||--|o UsSdwisPWS-ServiceArea : "us_sdwis_serviceArea"
UsSdwisPublicWaterSystem-GW ||--|o RdfsLiteral : "rdfs_label"
UsSdwisPublicWaterSystem-GW ||--|o OwlThing : "owl_sameAs"
UsSdwisPublicWaterSystem-GW ||--|o OwlThing : "us_sdwis_primarySourceType"
UsSdwisPublicWaterSystem-GW ||--|o UsSdwisPWS-SourceWaterType : "us_sdwis_primarySourceType"
UsSdwisPublicWaterSystem-GW ||--|o RdfsLiteral : "us_sdwis_pwsName"
UsSdwisPublicWaterSystem-GW ||--|o UsSdwisPublicWaterSystem-GW : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-GW ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-GW ||--|o UsSdwisPublicWaterSystem-SW : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-GW ||--|o UsSdwisPWS-ServiceArea : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-GW ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-GW ||--|o OwlThing : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-GW ||--|o HyfHYWaterBody : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-GW ||--|o UsSdwisPublicWaterSystem-NTNCWS : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-GW ||--|o MeMgsMGS-Well : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-GW ||--|o KwgoS2CellLevel13 : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-GW ||--|o B805a9e7d30eaabcb686b8ce670ed1e95 : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-GW ||--|o HyfHYHydroFeature : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-GW ||--|o KwgoAdministrativeRegion3 : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-GW ||--|o UsSdwisPublicWaterSystem-CWS : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-GW ||--|o GeoFeature : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-GW ||--|o HyfHYLake : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-GW ||--|o GeoSpatialObject : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-GW ||--|o HyfHYElementaryFlowPath : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-GW ||--|o KwgoAdministrativeRegion2 : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-GW ||--|o UsSdwisPublicWaterSystem-TNCWS : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-GW ||--|o KwgoRegion : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-GW ||--|o KwgoAdministrativeRegion : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-GW ||--|o UsSdwisPublicWaterSystem-GW : "spatial_connectedTo"
UsSdwisPublicWaterSystem-GW ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "spatial_connectedTo"
UsSdwisPublicWaterSystem-GW ||--|o UsSdwisPublicWaterSystem-SW : "spatial_connectedTo"
UsSdwisPublicWaterSystem-GW ||--|o UsSdwisPWS-ServiceArea : "spatial_connectedTo"
UsSdwisPublicWaterSystem-GW ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "spatial_connectedTo"
UsSdwisPublicWaterSystem-GW ||--|o OwlThing : "spatial_connectedTo"
UsSdwisPublicWaterSystem-GW ||--|o HyfHYWaterBody : "spatial_connectedTo"
UsSdwisPublicWaterSystem-GW ||--|o UsSdwisPublicWaterSystem-NTNCWS : "spatial_connectedTo"
UsSdwisPublicWaterSystem-GW ||--|o MeMgsMGS-Well : "spatial_connectedTo"
UsSdwisPublicWaterSystem-GW ||--|o KwgoS2CellLevel13 : "spatial_connectedTo"
UsSdwisPublicWaterSystem-GW ||--|o B805a9e7d30eaabcb686b8ce670ed1e95 : "spatial_connectedTo"
UsSdwisPublicWaterSystem-GW ||--|o HyfHYHydroFeature : "spatial_connectedTo"
UsSdwisPublicWaterSystem-GW ||--|o KwgoAdministrativeRegion3 : "spatial_connectedTo"
UsSdwisPublicWaterSystem-GW ||--|o UsSdwisPublicWaterSystem-CWS : "spatial_connectedTo"
UsSdwisPublicWaterSystem-GW ||--|o GeoFeature : "spatial_connectedTo"
UsSdwisPublicWaterSystem-GW ||--|o HyfHYLake : "spatial_connectedTo"
UsSdwisPublicWaterSystem-GW ||--|o GeoSpatialObject : "spatial_connectedTo"
UsSdwisPublicWaterSystem-GW ||--|o HyfHYElementaryFlowPath : "spatial_connectedTo"
UsSdwisPublicWaterSystem-GW ||--|o KwgoAdministrativeRegion2 : "spatial_connectedTo"
UsSdwisPublicWaterSystem-GW ||--|o UsSdwisPublicWaterSystem-TNCWS : "spatial_connectedTo"
UsSdwisPublicWaterSystem-GW ||--|o KwgoRegion : "spatial_connectedTo"
UsSdwisPublicWaterSystem-GW ||--|o KwgoAdministrativeRegion : "spatial_connectedTo"
UsSdwisPublicWaterSystem-GW ||--|o GeoFeature : "us_sdwis_serviceArea"
UsSdwisPublicWaterSystem-GW ||--|o OwlThing : "us_sdwis_serviceArea"
UsSdwisPublicWaterSystem-GW ||--|o GeoSpatialObject : "us_sdwis_serviceArea"
UsSdwisPublicWaterSystem-GW ||--|o UsSdwisPWS-ServiceArea : "us_sdwis_serviceArea"
UsSdwisPublicWaterSystem-NTNCWS ||--|o RdfsLiteral : "rdfs_label"
UsSdwisPublicWaterSystem-NTNCWS ||--|o OwlThing : "owl_sameAs"
UsSdwisPublicWaterSystem-NTNCWS ||--|o OwlThing : "us_sdwis_primarySourceType"
UsSdwisPublicWaterSystem-NTNCWS ||--|o UsSdwisPWS-SourceWaterType : "us_sdwis_primarySourceType"
UsSdwisPublicWaterSystem-NTNCWS ||--|o RdfsLiteral : "us_sdwis_pwsName"
UsSdwisPublicWaterSystem-NTNCWS ||--|o UsSdwisPublicWaterSystem-GW : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o UsSdwisPublicWaterSystem-SW : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o UsSdwisPWS-ServiceArea : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o OwlThing : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o HyfHYWaterBody : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o UsSdwisPublicWaterSystem-NTNCWS : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o MeMgsMGS-Well : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o KwgoS2CellLevel13 : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o B805a9e7d30eaabcb686b8ce670ed1e95 : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o HyfHYHydroFeature : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o KwgoAdministrativeRegion3 : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o UsSdwisPublicWaterSystem-CWS : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o GeoFeature : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o HyfHYLake : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o GeoSpatialObject : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o HyfHYElementaryFlowPath : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o KwgoAdministrativeRegion2 : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o UsSdwisPublicWaterSystem-TNCWS : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o KwgoRegion : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o KwgoAdministrativeRegion : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o UsSdwisPublicWaterSystem-GW : "spatial_connectedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "spatial_connectedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o UsSdwisPublicWaterSystem-SW : "spatial_connectedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o UsSdwisPWS-ServiceArea : "spatial_connectedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "spatial_connectedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o OwlThing : "spatial_connectedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o HyfHYWaterBody : "spatial_connectedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o UsSdwisPublicWaterSystem-NTNCWS : "spatial_connectedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o MeMgsMGS-Well : "spatial_connectedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o KwgoS2CellLevel13 : "spatial_connectedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o B805a9e7d30eaabcb686b8ce670ed1e95 : "spatial_connectedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o HyfHYHydroFeature : "spatial_connectedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o KwgoAdministrativeRegion3 : "spatial_connectedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o UsSdwisPublicWaterSystem-CWS : "spatial_connectedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o GeoFeature : "spatial_connectedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o HyfHYLake : "spatial_connectedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o GeoSpatialObject : "spatial_connectedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o HyfHYElementaryFlowPath : "spatial_connectedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o KwgoAdministrativeRegion2 : "spatial_connectedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o UsSdwisPublicWaterSystem-TNCWS : "spatial_connectedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o KwgoRegion : "spatial_connectedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o KwgoAdministrativeRegion : "spatial_connectedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o GeoFeature : "us_sdwis_serviceArea"
UsSdwisPublicWaterSystem-NTNCWS ||--|o OwlThing : "us_sdwis_serviceArea"
UsSdwisPublicWaterSystem-NTNCWS ||--|o GeoSpatialObject : "us_sdwis_serviceArea"
UsSdwisPublicWaterSystem-NTNCWS ||--|o UsSdwisPWS-ServiceArea : "us_sdwis_serviceArea"
UsSdwisPublicWaterSystem-SW ||--|o RdfsLiteral : "rdfs_label"
UsSdwisPublicWaterSystem-SW ||--|o OwlThing : "owl_sameAs"
UsSdwisPublicWaterSystem-SW ||--|o OwlThing : "us_sdwis_primarySourceType"
UsSdwisPublicWaterSystem-SW ||--|o UsSdwisPWS-SourceWaterType : "us_sdwis_primarySourceType"
UsSdwisPublicWaterSystem-SW ||--|o RdfsLiteral : "us_sdwis_pwsName"
UsSdwisPublicWaterSystem-SW ||--|o UsSdwisPublicWaterSystem-GW : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-SW ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-SW ||--|o UsSdwisPublicWaterSystem-SW : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-SW ||--|o UsSdwisPWS-ServiceArea : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-SW ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-SW ||--|o OwlThing : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-SW ||--|o HyfHYWaterBody : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-SW ||--|o UsSdwisPublicWaterSystem-NTNCWS : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-SW ||--|o MeMgsMGS-Well : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-SW ||--|o KwgoS2CellLevel13 : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-SW ||--|o B805a9e7d30eaabcb686b8ce670ed1e95 : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-SW ||--|o HyfHYHydroFeature : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-SW ||--|o KwgoAdministrativeRegion3 : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-SW ||--|o UsSdwisPublicWaterSystem-CWS : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-SW ||--|o GeoFeature : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-SW ||--|o HyfHYLake : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-SW ||--|o GeoSpatialObject : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-SW ||--|o HyfHYElementaryFlowPath : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-SW ||--|o KwgoAdministrativeRegion2 : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-SW ||--|o UsSdwisPublicWaterSystem-TNCWS : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-SW ||--|o KwgoRegion : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-SW ||--|o KwgoAdministrativeRegion : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-SW ||--|o UsSdwisPublicWaterSystem-GW : "spatial_connectedTo"
UsSdwisPublicWaterSystem-SW ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "spatial_connectedTo"
UsSdwisPublicWaterSystem-SW ||--|o UsSdwisPublicWaterSystem-SW : "spatial_connectedTo"
UsSdwisPublicWaterSystem-SW ||--|o UsSdwisPWS-ServiceArea : "spatial_connectedTo"
UsSdwisPublicWaterSystem-SW ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "spatial_connectedTo"
UsSdwisPublicWaterSystem-SW ||--|o OwlThing : "spatial_connectedTo"
UsSdwisPublicWaterSystem-SW ||--|o HyfHYWaterBody : "spatial_connectedTo"
UsSdwisPublicWaterSystem-SW ||--|o UsSdwisPublicWaterSystem-NTNCWS : "spatial_connectedTo"
UsSdwisPublicWaterSystem-SW ||--|o MeMgsMGS-Well : "spatial_connectedTo"
UsSdwisPublicWaterSystem-SW ||--|o KwgoS2CellLevel13 : "spatial_connectedTo"
UsSdwisPublicWaterSystem-SW ||--|o B805a9e7d30eaabcb686b8ce670ed1e95 : "spatial_connectedTo"
UsSdwisPublicWaterSystem-SW ||--|o HyfHYHydroFeature : "spatial_connectedTo"
UsSdwisPublicWaterSystem-SW ||--|o KwgoAdministrativeRegion3 : "spatial_connectedTo"
UsSdwisPublicWaterSystem-SW ||--|o UsSdwisPublicWaterSystem-CWS : "spatial_connectedTo"
UsSdwisPublicWaterSystem-SW ||--|o GeoFeature : "spatial_connectedTo"
UsSdwisPublicWaterSystem-SW ||--|o HyfHYLake : "spatial_connectedTo"
UsSdwisPublicWaterSystem-SW ||--|o GeoSpatialObject : "spatial_connectedTo"
UsSdwisPublicWaterSystem-SW ||--|o HyfHYElementaryFlowPath : "spatial_connectedTo"
UsSdwisPublicWaterSystem-SW ||--|o KwgoAdministrativeRegion2 : "spatial_connectedTo"
UsSdwisPublicWaterSystem-SW ||--|o UsSdwisPublicWaterSystem-TNCWS : "spatial_connectedTo"
UsSdwisPublicWaterSystem-SW ||--|o KwgoRegion : "spatial_connectedTo"
UsSdwisPublicWaterSystem-SW ||--|o KwgoAdministrativeRegion : "spatial_connectedTo"
UsSdwisPublicWaterSystem-SW ||--|o GeoFeature : "us_sdwis_serviceArea"
UsSdwisPublicWaterSystem-SW ||--|o OwlThing : "us_sdwis_serviceArea"
UsSdwisPublicWaterSystem-SW ||--|o GeoSpatialObject : "us_sdwis_serviceArea"
UsSdwisPublicWaterSystem-SW ||--|o UsSdwisPWS-ServiceArea : "us_sdwis_serviceArea"
UsSdwisPublicWaterSystem-TNCWS ||--|o RdfsLiteral : "rdfs_label"
UsSdwisPublicWaterSystem-TNCWS ||--|o OwlThing : "owl_sameAs"
UsSdwisPublicWaterSystem-TNCWS ||--|o OwlThing : "us_sdwis_primarySourceType"
UsSdwisPublicWaterSystem-TNCWS ||--|o UsSdwisPWS-SourceWaterType : "us_sdwis_primarySourceType"
UsSdwisPublicWaterSystem-TNCWS ||--|o RdfsLiteral : "us_sdwis_pwsName"
UsSdwisPublicWaterSystem-TNCWS ||--|o UsSdwisPublicWaterSystem-GW : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o UsSdwisPublicWaterSystem-SW : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o UsSdwisPWS-ServiceArea : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o OwlThing : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o HyfHYWaterBody : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o UsSdwisPublicWaterSystem-NTNCWS : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o MeMgsMGS-Well : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o KwgoS2CellLevel13 : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o B805a9e7d30eaabcb686b8ce670ed1e95 : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o HyfHYHydroFeature : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o KwgoAdministrativeRegion3 : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o UsSdwisPublicWaterSystem-CWS : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o GeoFeature : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o HyfHYLake : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o GeoSpatialObject : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o HyfHYElementaryFlowPath : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o KwgoAdministrativeRegion2 : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o UsSdwisPublicWaterSystem-TNCWS : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o KwgoRegion : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o KwgoAdministrativeRegion : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o UsSdwisPublicWaterSystem-GW : "spatial_connectedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "spatial_connectedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o UsSdwisPublicWaterSystem-SW : "spatial_connectedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o UsSdwisPWS-ServiceArea : "spatial_connectedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "spatial_connectedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o OwlThing : "spatial_connectedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o HyfHYWaterBody : "spatial_connectedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o UsSdwisPublicWaterSystem-NTNCWS : "spatial_connectedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o MeMgsMGS-Well : "spatial_connectedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o KwgoS2CellLevel13 : "spatial_connectedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o B805a9e7d30eaabcb686b8ce670ed1e95 : "spatial_connectedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o HyfHYHydroFeature : "spatial_connectedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o KwgoAdministrativeRegion3 : "spatial_connectedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o UsSdwisPublicWaterSystem-CWS : "spatial_connectedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o GeoFeature : "spatial_connectedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o HyfHYLake : "spatial_connectedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o GeoSpatialObject : "spatial_connectedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o HyfHYElementaryFlowPath : "spatial_connectedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o KwgoAdministrativeRegion2 : "spatial_connectedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o UsSdwisPublicWaterSystem-TNCWS : "spatial_connectedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o KwgoRegion : "spatial_connectedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o KwgoAdministrativeRegion : "spatial_connectedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o GeoFeature : "us_sdwis_serviceArea"
UsSdwisPublicWaterSystem-TNCWS ||--|o OwlThing : "us_sdwis_serviceArea"
UsSdwisPublicWaterSystem-TNCWS ||--|o GeoSpatialObject : "us_sdwis_serviceArea"
UsSdwisPublicWaterSystem-TNCWS ||--|o UsSdwisPWS-ServiceArea : "us_sdwis_serviceArea"

```



## Imports


* okns:owl-rdf-rdfs
* okns:hyf
* okns:extended_types
* okns:qudt
* linkml:types
* okns:sf
* okns:dc
* okns:geo
* okns:kwg
* okns:sdo



## Classes

| Class | Description | Occurrences |
| --- | --- | --- |
| [B805a9e7d30eaabcb686b8ce670ed1e95](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/B805a9e7d30eaabcb686b8ce670ed1e95.md) | None<br/>| 507486 | 
| [HttpGwml2.orgDefGwml2#GWAquifer](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/HttpGwml2.orgDefGwml2#GWAquifer.md) | None<br/>| 8441 | 
| [HttpGwml2.orgDefGwml2#GWAquiferSystem](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/HttpGwml2.orgDefGwml2#GWAquiferSystem.md) | None<br/>| 1941 | 
| [HttpNhdplusv2.spatialai.orgV1Nhdplusv2#FlowPathLength](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/HttpNhdplusv2.spatialai.orgV1Nhdplusv2#FlowPathLength.md) | None<br/>| 434501 | 
| [HyfHYCatchmentRealization](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/HyfHYCatchmentRealization.md) | The HY_CatchmentRealization feature type (Figure 34) is based on the idea that there are multiple hydrology-specific perspectives of the holistic catchment concept that are used to describe a catchment as a unit of study shared across sub-domains and studies.␊␊A given catchment realization exists within a hydrologic complex in that, if a catchment realization exists, it exists in the same hydrologic complex as the catchment it realizes. In this way, any realization of a catchment has the same hydrologic determination of the catchment it realizes. If a catchment is connected with other catchments via inflow and/or outflow hydro nexuses, its realizations are also connected. A realization of the logical catchment is always of higher topological dimension than the realization of the corresponding hydro nexus topological boundary. For example, a linear flowpath realizing a catchment may be understood as an edge between inflow and outflow nodes; the areal realization of a catchment as a face bounded by linear inflow and outflow.␊␊The catchment realization features defined in this standard refer to objects on the land surface for the purpose of surface water hydrology. In other contexts, other types of catchment realization may exist. Catchment realizations that do not conform to those defined in this standard, for instance realizations in 3- or 4-dimensional perspectives, may be implemented using the general HY_CatchmentRealization type. HY_CatchmentRealization carries a shape attribute and as a realizedCatchment association.<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HyfHYFlowPath](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/HyfHYFlowPath.md) | The HY_Flowpath feature type realizes a catchment specifically as a path connecting the inflow and outflow of the catchment it realizes.␊␊HY_Flowpath specializes HY_CatchmentRealization with respect to an implied linear geometric representation including a straight or curved line. Topologically, the flowpath connects the inflow and outflow of the catchment, and is understood as an edge bounded by an inflow node and an outflow node, and corresponding to left-bank and right-bank catchment faces. Hydrologically, the flowpath is a line describing a moving particle of water.␊␊Through generalization, HY_Flowpath inherits the shape and the realizedCatchment properties. The optional shape of the flowpath is usually a single curve.<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HyfHYElementaryFlowPath](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/HyfHYElementaryFlowPath.md) | None<br/>| 434501 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HyfHYMainStem](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/HyfHYMainStem.md) | None<br/>|  | 
| [OwlDataProperty](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/OwlDataProperty.md) | None<br/>| 3 | 
| [OwlThing](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/OwlThing.md) | The class of OWL individuals.<br/>| 1974234 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpHyfo.spatialai.orgV1Hyfo#AquiferWaterFeature](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/HttpHyfo.spatialai.orgV1Hyfo#AquiferWaterFeature.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpHyfo.spatialai.orgV1Hyfo#SubsurfaceWaterFeature](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/HttpHyfo.spatialai.orgV1Hyfo#SubsurfaceWaterFeature.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpHyfo.spatialai.orgV1Hyfo#SurfaceWaterFeature](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/HttpHyfo.spatialai.orgV1Hyfo#SurfaceWaterFeature.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpHyfo.spatialai.orgV1Hyfo#WaterFeature](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/HttpHyfo.spatialai.orgV1Hyfo#WaterFeature.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpHyfo.spatialai.orgV1Hyfo#WaterFeatureRepresentation](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/HttpHyfo.spatialai.orgV1Hyfo#WaterFeatureRepresentation.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[IlIsgsISGS-Well](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/IlIsgsISGS-Well.md) | None<br/>| 379496 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[IlIsgsWellDepthInFt](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/IlIsgsWellDepthInFt.md) | None<br/>| 376687 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[IlIsgsWellPurpose](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/IlIsgsWellPurpose.md) | None<br/>| 33 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[IlIsgsWellYield](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/IlIsgsWellYield.md) | None<br/>| 265368 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[KwgoS2CellLevel13](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/KwgoS2CellLevel13.md) | None<br/>| 7404184 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[KwgoStatisticalArea](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/KwgoStatisticalArea.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MeMgsMGS-Well](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/MeMgsMGS-Well.md) | None<br/>| 147508 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MeMgsWellDepthInFt](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/MeMgsWellDepthInFt.md) | None<br/>| 147508 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MeMgsWellOverburdenThicknessInFt](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/MeMgsWellOverburdenThicknessInFt.md) | None<br/>| 129946 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MeMgsWellType](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/MeMgsWellType.md) | None<br/>| 8 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MeMgsWellUse](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/MeMgsWellUse.md) | None<br/>| 13 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[UsSdwisCombinedDistributionSystem](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/UsSdwisCombinedDistributionSystem.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[UsSdwisPublicWaterSystem](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/UsSdwisPublicWaterSystem.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[UsSdwisPublicWaterSystem-CWS](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/UsSdwisPublicWaterSystem-CWS.md) | None<br/>| 773 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[UsSdwisPublicWaterSystem-GW](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/UsSdwisPublicWaterSystem-GW.md) | None<br/>| 5936 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[UsSdwisPublicWaterSystem-NCWS](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/UsSdwisPublicWaterSystem-NCWS.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[UsSdwisPublicWaterSystem-NTNCWS](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/UsSdwisPublicWaterSystem-NTNCWS.md) | None<br/>| 858 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[UsSdwisPublicWaterSystem-SW](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/UsSdwisPublicWaterSystem-SW.md) | None<br/>| 254 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[UsSdwisPublicWaterSystem-TNCWS](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/UsSdwisPublicWaterSystem-TNCWS.md) | None<br/>| 4771 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[UsSdwisPWS-ServiceArea](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/UsSdwisPWS-ServiceArea.md) | None<br/>| 5061 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[UsSdwisPWS-ServiceAreaType](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/UsSdwisPWS-ServiceAreaType.md) | None<br/>| 28 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[UsSdwisPWS-SourceWaterType](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/UsSdwisPWS-SourceWaterType.md) | None<br/>| 5 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[UsSdwisPWS-SubFeature](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/UsSdwisPWS-SubFeature.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[UsSdwisPWS-SubFeatureType](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/UsSdwisPWS-SubFeatureType.md) | None<br/>| 22 | 
| [StadSingleData](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/StadSingleData.md) | None<br/>|  | 
| [UsSdwisPWS-SubFeatureActivity](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/UsSdwisPWS-SubFeatureActivity.md) | None<br/>| 5 | 





## Slots

| Slot | Description | Occurrences |
| --- | --- | --- |
| [http___gwml2.org_def_gwml2#gwAquiferSystem](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/http___gwml2.org_def_gwml2#gwAquiferSystem.md) | <br/>| 8339 |
| [http___gwml2.org_def_gwml2#gwAquiferSystemPart](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/http___gwml2.org_def_gwml2#gwAquiferSystemPart.md) | <br/>| 8339 |
| [http___nhdplusv2.spatialai.org_v1_nhdplusv2#hasCOMID](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/http___nhdplusv2.spatialai.org_v1_nhdplusv2#hasCOMID.md) | <br/>| 507486 |
| [http___nhdplusv2.spatialai.org_v1_nhdplusv2#hasFCODE](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/http___nhdplusv2.spatialai.org_v1_nhdplusv2#hasFCODE.md) | <br/>| 507486 |
| [http___nhdplusv2.spatialai.org_v1_nhdplusv2#hasFlowPathLength](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/http___nhdplusv2.spatialai.org_v1_nhdplusv2#hasFlowPathLength.md) | <br/>| 434501 |
| [http___nhdplusv2.spatialai.org_v1_nhdplusv2#hasFTYPE](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/http___nhdplusv2.spatialai.org_v1_nhdplusv2#hasFTYPE.md) | <br/>| 507486 |
| [http___nhdplusv2.spatialai.org_v1_nhdplusv2#hasReachCode](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/http___nhdplusv2.spatialai.org_v1_nhdplusv2#hasReachCode.md) | <br/>| 507487 |
| [http___sawgraph.spatialai.org_v1_il_isgs#ilSawAqId](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/http___sawgraph.spatialai.org_v1_il_isgs#ilSawAqId.md) | <br/>| 3469 |
| [http___sawgraph.spatialai.org_v1_il_isgs#ilSawAqSysId](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/http___sawgraph.spatialai.org_v1_il_isgs#ilSawAqSysId.md) | <br/>| 439 |
| [http___sawgraph.spatialai.org_v1_me_mgs#meMgsAqId](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/http___sawgraph.spatialai.org_v1_me_mgs#meMgsAqId.md) | <br/>| 4972 |
| [http___sawgraph.spatialai.org_v1_me_mgs#meSawAqSysId](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/http___sawgraph.spatialai.org_v1_me_mgs#meSawAqSysId.md) | <br/>| 1502 |
| [http___sawgraph.spatialai.org_v1_saw_water#aquiferType](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/http___sawgraph.spatialai.org_v1_saw_water#aquiferType.md) | <br/>| 8441 |
| [hyf_downstreamFlowPath](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/hyf_downstreamFlowPath.md) | <br/>| 865469 |
| [hyf_downstreamFlowPathTC](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/hyf_downstreamFlowPathTC.md) | <br/>| 407803007 |
| [hyf_encompassingCatchment](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/hyf_encompassingCatchment.md) | <br/>|  |
| [hyf_upstreamFlowPath](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/hyf_upstreamFlowPath.md) | <br/>|  |
| [il_isgs_hasISWSId](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/il_isgs_hasISWSId.md) | <br/>| 152051 |
| [il_isgs_hasOwner](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/il_isgs_hasOwner.md) | <br/>| 377323 |
| [il_isgs_wellDepth](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/il_isgs_wellDepth.md) | <br/>| 376687 |
| [il_isgs_wellPurpose](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/il_isgs_wellPurpose.md) | <br/>| 379496 |
| [il_isgs_wellYield](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/il_isgs_wellYield.md) | <br/>| 265368 |
| [kwgo_administrativePartOf](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/kwgo_administrativePartOf.md) | <br/>|  |
| [me_mgs_hasUse](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/me_mgs_hasUse.md) | <br/>| 143400 |
| [me_mgs_ofWellType](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/me_mgs_ofWellType.md) | <br/>| 144120 |
| [me_mgs_wellDepth](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/me_mgs_wellDepth.md) | <br/>| 147508 |
| [me_mgs_wellOverburden](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/me_mgs_wellOverburden.md) | <br/>| 129946 |
| [skos_description](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/skos_description.md) | <br/>|  |
| [spatial_connectedTo](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/spatial_connectedTo.md) | <br/>| 4665700 |
| [spatial_spatiallyRelatedTo](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/spatial_spatiallyRelatedTo.md) | <br/>| 4665700 |
| [us_sdwis_buysFrom](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/us_sdwis_buysFrom.md) | <br/>|  |
| [us_sdwis_deactivationDate](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/us_sdwis_deactivationDate.md) | <br/>| 4524 |
| [us_sdwis_firstReport](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/us_sdwis_firstReport.md) | <br/>| 6402 |
| [us_sdwis_hasActivity](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/us_sdwis_hasActivity.md) | <br/>| 6402 |
| [us_sdwis_hasMethod](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/us_sdwis_hasMethod.md) | <br/>| 296 |
| [us_sdwis_hasOwnership](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/us_sdwis_hasOwnership.md) | <br/>| 5304 |
| [us_sdwis_hasPart](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/us_sdwis_hasPart.md) | <br/>|  |
| [us_sdwis_hasPermanentSource](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/us_sdwis_hasPermanentSource.md) | <br/>|  |
| [us_sdwis_hasSource](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/us_sdwis_hasSource.md) | <br/>|  |
| [us_sdwis_inCombinedSystem](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/us_sdwis_inCombinedSystem.md) | <br/>|  |
| [us_sdwis_lastReport](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/us_sdwis_lastReport.md) | <br/>| 6387 |
| [us_sdwis_partOf](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/us_sdwis_partOf.md) | <br/>|  |
| [us_sdwis_populationServed](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/us_sdwis_populationServed.md) | <br/>| 6402 |
| [us_sdwis_primarySourceType](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/us_sdwis_primarySourceType.md) | <br/>| 6190 |
| [us_sdwis_pwsName](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/us_sdwis_pwsName.md) | <br/>| 6362 |
| [us_sdwis_sellsTo](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/us_sdwis_sellsTo.md) | <br/>|  |
| [us_sdwis_serviceArea](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/us_sdwis_serviceArea.md) | <br/>| 5061 |
| [us_sdwis_serviceAreaType](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/us_sdwis_serviceAreaType.md) | <br/>| 6041 |
| [us_sdwis_serviceConnections](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/us_sdwis_serviceConnections.md) | <br/>| 6402 |
| [us_sdwis_sourceFor](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/us_sdwis_sourceFor.md) | <br/>|  |









## IRI prefixes

* dc: http://purl.org/dc/elements/1.1/
* dcgeoid: https://datacommons.org/browser/geoId/
* dct: http://purl.org/dc/terms/
* geo: http://www.opengis.net/ont/geosparql#
* hyf: https://www.opengis.net/def/schema/hy_features/hyf/
* il_isgs: http://sawgraph.spatialai.org/v1/il-isgs#
* il_isgs_data: http://sawgraph.spatialai.org/v1/il-isgs-data#
* kwgo: http://stko-kwg.geog.ucsb.edu/lod/ontology/
* kwgr: http://stko-kwg.geog.ucsb.edu/lod/resource/
* linkml: https://w3id.org/linkml/
* me_mgs: http://sawgraph.spatialai.org/v1/me-mgs#
* me_mgs_data: http://sawgraph.spatialai.org/v1/me-mgs-data#
* okn: https://purl.org/okn/
* okns: https://purl.org/okn/schema/
* owl: http://www.w3.org/2002/07/owl#
* qudt: http://qudt.org/schema/qudt/
* rdf: http://www.w3.org/1999/02/22-rdf-syntax-ns#
* rdfs: http://www.w3.org/2000/01/rdf-schema#
* sdos: https://schema.org/
* sf: http://www.opengis.net/ont/sf#
* skos: http://www.w3.org/2004/02/skos/core#
* spatial: http://purl.org/spatialai/spatial/spatial-full#
* stad: http://purl.org/spatialai/stad/v2/core/
* us_sdwis: http://sawgraph.spatialai.org/v1/us-sdwis#
* xsd: http://www.w3.org/2001/XMLSchema#
