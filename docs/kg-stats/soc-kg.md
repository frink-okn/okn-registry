# sockg





## Schema Diagram

```mermaid
erDiagram
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
SkosCollection {

}
SkosConcept {

}
SkosConceptScheme {

}
SkosOrderedCollection {

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
EventEvent {

}
EventFactor {

}
EventProduct {

}
BiboAcademicArticle {

}
BiboArticle {

}
BiboAudioDocument {

}
BiboAudioVisualDocument {

}
BiboBill {

}
BiboBook {

}
BiboBookSection {

}
BiboBrief {

}
BiboChapter {

}
BiboCode {

}
BiboCollectedDocument {

}
BiboCollection {

}
BiboConference {

}
BiboCourtReporter {

}
BiboDocument {

}
BiboDocumentPart {

}
BiboDocumentStatus {
    string rdfs_label  
    string rdfs_comment  
}
BiboEditedBook {

}
BiboEmail {

}
BiboEvent {

}
BiboExcerpt {

}
BiboFilm {

}
BiboHearing {

}
BiboImage {

}
BiboInterview {

}
BiboIssue {

}
BiboJournal {

}
BiboLegalCaseDocument {

}
BiboLegalDecision {

}
BiboLegalDocument {

}
BiboLegislation {

}
BiboLetter {

}
BiboMagazine {

}
BiboManual {

}
BiboManuscript {

}
BiboMap {

}
BiboMultiVolumeBook {

}
BiboNewspaper {

}
BiboNote {

}
BiboPatent {

}
BiboPerformance {

}
BiboPeriodical {

}
BiboPersonalCommunication {

}
BiboPersonalCommunicationDocument {

}
BiboProceedings {

}
BiboQuote {

}
BiboReferenceSource {

}
BiboReport {

}
BiboSeries {

}
BiboSlide {

}
BiboSlideshow {

}
BiboStandard {

}
BiboStatute {

}
BiboThesis {

}
BiboThesisDegree {
    string rdfs_label  
    string rdfs_comment  
}
BiboWebpage {

}
BiboWebsite {

}
BiboWorkshop {

}
HttpsIdir.uta.eduSockg-ontology#Abstract {
    string rdfs_label  
    string https___idir.uta.edu_sockg_ontology#correspondingAuthor  
    string dct_title  
    date dct_issued  
}
HttpsIdir.uta.eduSockg-ontology#ActiveIngredient {
    string coso_casNumber  
    string rdfs_label  
}
HttpsIdir.uta.eduSockg-ontology#Amendment {
    date https___idir.uta.edu_sockg_ontology#startDate  
}
HttpsIdir.uta.eduSockg-ontology#AmendmentPlacement {
    string rdfs_label  
}
HttpsIdir.uta.eduSockg-ontology#AmendmentType {
    string rdfs_label  
}
HttpsIdir.uta.eduSockg-ontology#AnimalClass {
    string rdfs_label  
}
HttpsIdir.uta.eduSockg-ontology#AnimalSpecies {
    string dct_description  
    string rdfs_label  
}
HttpsIdir.uta.eduSockg-ontology#BiomassAnalysis {

}
HttpsIdir.uta.eduSockg-ontology#BiomassCarbohydrate {
    uri https___idir.uta.edu_sockg_ontology#fromUnit  
    uri https___idir.uta.edu_sockg_ontology#usesTreatment  
}
HttpsIdir.uta.eduSockg-ontology#BiomassEnergy {
    uri https___idir.uta.edu_sockg_ontology#fromUnit  
    uri https___idir.uta.edu_sockg_ontology#usesTreatment  
}
HttpsIdir.uta.eduSockg-ontology#BiomassMineral {
    uri https___idir.uta.edu_sockg_ontology#fromUnit  
    uri https___idir.uta.edu_sockg_ontology#usesTreatment  
}
HttpsIdir.uta.eduSockg-ontology#BookChapter {
    string rdfs_label  
    string https___idir.uta.edu_sockg_ontology#correspondingAuthor  
    date dct_issued  
    string dct_title  
}
HttpsIdir.uta.eduSockg-ontology#BroadleafOrGrass {
    string rdfs_label  
}
HttpsIdir.uta.eduSockg-ontology#ChamberPlacement {
    string rdfs_label  
}
HttpsIdir.uta.eduSockg-ontology#CoverCrop {
    string dct_description  
}
HttpsIdir.uta.eduSockg-ontology#CropRelatedMeasurement {

}
HttpsIdir.uta.eduSockg-ontology#Cultivar {
    string rdfs_label  
}
HttpsIdir.uta.eduSockg-ontology#CuttingHeight {
    string rdfs_label  
}
HttpsIdir.uta.eduSockg-ontology#Equipment {
    string rdfs_label  
}
HttpsIdir.uta.eduSockg-ontology#ErosionMeasurement {

}
HttpsIdir.uta.eduSockg-ontology#ExperimentalUnit {
    date https___idir.uta.edu_sockg_ontology#endDate  
    boolean https___idir.uta.edu_sockg_ontology#inferred  
    uri https___idir.uta.edu_sockg_ontology#unitUrl  
    date https___idir.uta.edu_sockg_ontology#startDate  
}
HttpsIdir.uta.eduSockg-ontology#FertilizerAmendment {
    string dct_description  
}
HttpsIdir.uta.eduSockg-ontology#FundingSource {
    string rdfs_label  
}
HttpsIdir.uta.eduSockg-ontology#GHGFlux {
    uri https___idir.uta.edu_sockg_ontology#fromUnit  
    uri https___idir.uta.edu_sockg_ontology#usesTreatment  
}
HttpsIdir.uta.eduSockg-ontology#GasNutrientLoss {
    uri https___idir.uta.edu_sockg_ontology#fromUnit  
    uri https___idir.uta.edu_sockg_ontology#usesTreatment  
}
HttpsIdir.uta.eduSockg-ontology#GrazingManagement {
    date https___idir.uta.edu_sockg_ontology#endDate  
    date https___idir.uta.edu_sockg_ontology#startDate  
}
HttpsIdir.uta.eduSockg-ontology#GrazingPlants {
    uri https___idir.uta.edu_sockg_ontology#fromUnit  
    uri https___idir.uta.edu_sockg_ontology#usesTreatment  
}
HttpsIdir.uta.eduSockg-ontology#GrazingRate {
    string dct_description  
}
HttpsIdir.uta.eduSockg-ontology#GrowthStage {
    string rdfs_label  
}
HttpsIdir.uta.eduSockg-ontology#GrowthStageManagement {

}
HttpsIdir.uta.eduSockg-ontology#GrowthStageRelatedMeasurement {

}
HttpsIdir.uta.eduSockg-ontology#HarvestFraction {
    uri https___idir.uta.edu_sockg_ontology#fromUnit  
    uri https___idir.uta.edu_sockg_ontology#usesTreatment  
}
HttpsIdir.uta.eduSockg-ontology#HarvestedFraction {
    string rdfs_label  
}
HttpsIdir.uta.eduSockg-ontology#Irrigation {
    string rdfs_label  
}
HttpsIdir.uta.eduSockg-ontology#JournalArticle {
    string rdfs_label  
    string https___idir.uta.edu_sockg_ontology#correspondingAuthor  
    string dct_title  
    string dct_description  
    date dct_issued  
}
HttpsIdir.uta.eduSockg-ontology#Location {
    string rdfs_label  
    date https___idir.uta.edu_sockg_ontology#endDate  
    string dct_description  
    date https___idir.uta.edu_sockg_ontology#startDate  
}
HttpsIdir.uta.eduSockg-ontology#LossesOrDeposition {
    string rdfs_label  
}
HttpsIdir.uta.eduSockg-ontology#MeasurableEntity {

}
HttpsIdir.uta.eduSockg-ontology#Measurement {

}
HttpsIdir.uta.eduSockg-ontology#NutrientEfficiency {
    uri https___idir.uta.edu_sockg_ontology#fromUnit  
    uri https___idir.uta.edu_sockg_ontology#usesTreatment  
}
HttpsIdir.uta.eduSockg-ontology#OtherEvents {
    string rdfs_label  
}
HttpsIdir.uta.eduSockg-ontology#Parameter {
    string rdfs_label  
}
HttpsIdir.uta.eduSockg-ontology#PesticidePlacement {
    string rdfs_label  
}
HttpsIdir.uta.eduSockg-ontology#PesticideTarget {
    string rdfs_label  
}
HttpsIdir.uta.eduSockg-ontology#PlantFraction {
    string rdfs_label  
}
HttpsIdir.uta.eduSockg-ontology#PlantFractionRelatedMeasurement {

}
HttpsIdir.uta.eduSockg-ontology#PlantingManagement {
    date https___idir.uta.edu_sockg_ontology#startDate  
}
HttpsIdir.uta.eduSockg-ontology#PlantingMethod {
    string rdfs_label  
}
HttpsIdir.uta.eduSockg-ontology#PopularArticle {
    string rdfs_label  
    string https___idir.uta.edu_sockg_ontology#correspondingAuthor  
    string dct_title  
    date dct_issued  
}
HttpsIdir.uta.eduSockg-ontology#PossiblySimulatedMeasurement {

}
HttpsIdir.uta.eduSockg-ontology#Proceedings {
    string rdfs_label  
    string https___idir.uta.edu_sockg_ontology#correspondingAuthor  
    string dct_title  
    string dct_description  
    date dct_issued  
}
HttpsIdir.uta.eduSockg-ontology#Project {
    string dct_description  
}
HttpsIdir.uta.eduSockg-ontology#ProjectScenario {
    string dct_description  
}
HttpsIdir.uta.eduSockg-ontology#QualityMeasurement {

}
HttpsIdir.uta.eduSockg-ontology#Report {
    string rdfs_label  
    string https___idir.uta.edu_sockg_ontology#correspondingAuthor  
    string dct_title  
    date dct_issued  
}
HttpsIdir.uta.eduSockg-ontology#ResidueManagement {
    date https___idir.uta.edu_sockg_ontology#startDate  
}
HttpsIdir.uta.eduSockg-ontology#ResidueMeasurement {
    uri https___idir.uta.edu_sockg_ontology#fromUnit  
    uri https___idir.uta.edu_sockg_ontology#usesTreatment  
}
HttpsIdir.uta.eduSockg-ontology#ResidueRemoval {
    string dct_description  
}
HttpsIdir.uta.eduSockg-ontology#Rotation {
    string dct_description  
}
HttpsIdir.uta.eduSockg-ontology#Sample {

}
HttpsIdir.uta.eduSockg-ontology#SimulationModel {
    string rdfs_label  
}
HttpsIdir.uta.eduSockg-ontology#Site {

}
HttpsIdir.uta.eduSockg-ontology#SoilBiologicalSample {
    uri https___idir.uta.edu_sockg_ontology#fromUnit  
    uri https___idir.uta.edu_sockg_ontology#usesTreatment  
}
HttpsIdir.uta.eduSockg-ontology#SoilChemicalSample {
    uri https___idir.uta.edu_sockg_ontology#fromUnit  
    uri https___idir.uta.edu_sockg_ontology#usesTreatment  
}
HttpsIdir.uta.eduSockg-ontology#SoilCover {
    uri https___idir.uta.edu_sockg_ontology#fromUnit  
    uri https___idir.uta.edu_sockg_ontology#usesTreatment  
}
HttpsIdir.uta.eduSockg-ontology#SoilPhysicalSample {
    uri https___idir.uta.edu_sockg_ontology#fromUnit  
    uri https___idir.uta.edu_sockg_ontology#usesTreatment  
}
HttpsIdir.uta.eduSockg-ontology#SoilSample {

}
HttpsIdir.uta.eduSockg-ontology#SpeciesMix {
    string rdfs_label  
}
HttpsIdir.uta.eduSockg-ontology#StartStopInterval {
    string rdfs_label  
}
HttpsIdir.uta.eduSockg-ontology#SurfaceOrLeaching {
    string rdfs_label  
}
HttpsIdir.uta.eduSockg-ontology#Thesis {
    string rdfs_label  
    string https___idir.uta.edu_sockg_ontology#correspondingAuthor  
    string dct_title  
    string dct_description  
    date dct_issued  
}
HttpsIdir.uta.eduSockg-ontology#Tillage {
    string dct_description  
}
HttpsIdir.uta.eduSockg-ontology#TillageEvent {
    string rdfs_label  
}
HttpsIdir.uta.eduSockg-ontology#TillageManagement {
    date https___idir.uta.edu_sockg_ontology#startDate  
}
HttpsIdir.uta.eduSockg-ontology#TillageMethod {
    string rdfs_label  
}
HttpsIdir.uta.eduSockg-ontology#Timing {
    string dct_description  
}
HttpsIdir.uta.eduSockg-ontology#Treatment {
    boolean https___idir.uta.edu_sockg_ontology#irrigation  
    boolean https___idir.uta.edu_sockg_ontology#tileDrainage  
    date https___idir.uta.edu_sockg_ontology#startDate  
    boolean https___idir.uta.edu_sockg_ontology#organicManagement  
    string dct_description  
}
HttpsIdir.uta.eduSockg-ontology#WaterQualityArea {
    uri https___idir.uta.edu_sockg_ontology#fromUnit  
    uri https___idir.uta.edu_sockg_ontology#usesTreatment  
}
HttpsIdir.uta.eduSockg-ontology#WaterQualityConcentration {
    uri https___idir.uta.edu_sockg_ontology#fromUnit  
    uri https___idir.uta.edu_sockg_ontology#usesTreatment  
}
HttpsIdir.uta.eduSockg-ontology#WeatherObservation {
    uri https___idir.uta.edu_sockg_ontology#fromUnit  
    uri https___idir.uta.edu_sockg_ontology#usesTreatment  
    boolean https___idir.uta.edu_sockg_ontology#badValueFlag  
}
HttpsIdir.uta.eduSockg-ontology#WindErosionArea {
    uri https___idir.uta.edu_sockg_ontology#fromUnit  
    uri https___idir.uta.edu_sockg_ontology#usesTreatment  
}
HttpsIdir.uta.eduSockg-ontology#YieldNutrientUptake {
    uri https___idir.uta.edu_sockg_ontology#fromUnit  
    uri https___idir.uta.edu_sockg_ontology#usesTreatment  
}
HttpsLod.nal.usda.govNalt7140 {
    string rdfs_label  
}
KwgoS2CellLevel13 {

}

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
BiboDocumentStatus ||--|o RdfsLiteral : "rdfs_label"
BiboDocumentStatus ||--|o RdfsLiteral : "rdfs_comment"
BiboThesisDegree ||--|o RdfsLiteral : "rdfs_label"
BiboThesisDegree ||--|o RdfsLiteral : "rdfs_comment"
HttpsIdir.uta.eduSockg-ontology#Abstract ||--|o RdfsLiteral : "rdfs_label"
HttpsIdir.uta.eduSockg-ontology#Abstract ||--|o RdfsLiteral : "dct_title"
HttpsIdir.uta.eduSockg-ontology#Abstract ||--|o RdfsLiteral : "dct_bibliographicCitation"
HttpsIdir.uta.eduSockg-ontology#Abstract ||--|o RdfsLiteral : "dct_issued"
HttpsIdir.uta.eduSockg-ontology#ActiveIngredient ||--|o RdfsLiteral : "rdfs_label"
HttpsIdir.uta.eduSockg-ontology#Amendment ||--|o HttpsIdir.uta.eduSockg-ontology#AmendmentPlacement : "https___idir.uta.edu_sockg-ontology#withPlacement"
HttpsIdir.uta.eduSockg-ontology#Amendment ||--|o HttpsIdir.uta.eduSockg-ontology#PesticideTarget : "https___idir.uta.edu_sockg-ontology#hasPesticideTarget"
HttpsIdir.uta.eduSockg-ontology#Amendment ||--|o HttpsIdir.uta.eduSockg-ontology#Measurement : "https___idir.uta.edu_sockg-ontology#hasMeasurement"
HttpsIdir.uta.eduSockg-ontology#Amendment ||--|o HttpsIdir.uta.eduSockg-ontology#ActiveIngredient : "https___idir.uta.edu_sockg-ontology#hasPesticideActiveIngredient"
HttpsIdir.uta.eduSockg-ontology#Amendment ||--|o HttpsIdir.uta.eduSockg-ontology#PesticidePlacement : "https___idir.uta.edu_sockg-ontology#withPesticidePlacement"
HttpsIdir.uta.eduSockg-ontology#Amendment ||--|o HttpsIdir.uta.eduSockg-ontology#Irrigation : "https___idir.uta.edu_sockg-ontology#usesIrrigation"
HttpsIdir.uta.eduSockg-ontology#Amendment ||--|o HttpsIdir.uta.eduSockg-ontology#AmendmentType : "https___idir.uta.edu_sockg-ontology#hasAmendmentType"
HttpsIdir.uta.eduSockg-ontology#Amendment ||--|o HttpsLod.nal.usda.govNalt7140 : "https___idir.uta.edu_sockg-ontology#hasCrop"
HttpsIdir.uta.eduSockg-ontology#AmendmentPlacement ||--|o RdfsLiteral : "rdfs_label"
HttpsIdir.uta.eduSockg-ontology#AmendmentType ||--|o RdfsLiteral : "rdfs_label"
HttpsIdir.uta.eduSockg-ontology#AnimalClass ||--|o RdfsLiteral : "rdfs_label"
HttpsIdir.uta.eduSockg-ontology#AnimalSpecies ||--|o RdfsLiteral : "rdfs_label"
HttpsIdir.uta.eduSockg-ontology#BiomassCarbohydrate ||--|o HttpsIdir.uta.eduSockg-ontology#ExperimentalUnit : "https___idir.uta.edu_sockg-ontology#fromUnit"
HttpsIdir.uta.eduSockg-ontology#BiomassCarbohydrate ||--|o HttpsIdir.uta.eduSockg-ontology#PlantFractionRelatedMeasurement : "https___idir.uta.edu_sockg-ontology#hasPlantFraction"
HttpsIdir.uta.eduSockg-ontology#BiomassCarbohydrate ||--|o HttpsIdir.uta.eduSockg-ontology#PlantFraction : "https___idir.uta.edu_sockg-ontology#hasPlantFraction"
HttpsIdir.uta.eduSockg-ontology#BiomassCarbohydrate ||--|o HttpsIdir.uta.eduSockg-ontology#Measurement : "https___idir.uta.edu_sockg-ontology#hasMeasurement"
HttpsIdir.uta.eduSockg-ontology#BiomassCarbohydrate ||--|o HttpsIdir.uta.eduSockg-ontology#Treatment : "https___idir.uta.edu_sockg-ontology#usesTreatment"
HttpsIdir.uta.eduSockg-ontology#BiomassCarbohydrate ||--|o RdfsLiteral : "dct_date"
HttpsIdir.uta.eduSockg-ontology#BiomassCarbohydrate ||--|o HttpsIdir.uta.eduSockg-ontology#GrowthStage : "https___idir.uta.edu_sockg-ontology#hasGrowthStage"
HttpsIdir.uta.eduSockg-ontology#BiomassCarbohydrate ||--|o HttpsLod.nal.usda.govNalt7140 : "https___idir.uta.edu_sockg-ontology#hasCrop"
HttpsIdir.uta.eduSockg-ontology#BiomassEnergy ||--|o HttpsIdir.uta.eduSockg-ontology#ExperimentalUnit : "https___idir.uta.edu_sockg-ontology#fromUnit"
HttpsIdir.uta.eduSockg-ontology#BiomassEnergy ||--|o HttpsIdir.uta.eduSockg-ontology#PlantFractionRelatedMeasurement : "https___idir.uta.edu_sockg-ontology#hasPlantFraction"
HttpsIdir.uta.eduSockg-ontology#BiomassEnergy ||--|o HttpsIdir.uta.eduSockg-ontology#PlantFraction : "https___idir.uta.edu_sockg-ontology#hasPlantFraction"
HttpsIdir.uta.eduSockg-ontology#BiomassEnergy ||--|o HttpsIdir.uta.eduSockg-ontology#Measurement : "https___idir.uta.edu_sockg-ontology#hasMeasurement"
HttpsIdir.uta.eduSockg-ontology#BiomassEnergy ||--|o HttpsIdir.uta.eduSockg-ontology#Treatment : "https___idir.uta.edu_sockg-ontology#usesTreatment"
HttpsIdir.uta.eduSockg-ontology#BiomassEnergy ||--|o RdfsLiteral : "dct_date"
HttpsIdir.uta.eduSockg-ontology#BiomassEnergy ||--|o HttpsIdir.uta.eduSockg-ontology#GrowthStage : "https___idir.uta.edu_sockg-ontology#hasGrowthStage"
HttpsIdir.uta.eduSockg-ontology#BiomassEnergy ||--|o HttpsLod.nal.usda.govNalt7140 : "https___idir.uta.edu_sockg-ontology#hasCrop"
HttpsIdir.uta.eduSockg-ontology#BiomassMineral ||--|o HttpsIdir.uta.eduSockg-ontology#ExperimentalUnit : "https___idir.uta.edu_sockg-ontology#fromUnit"
HttpsIdir.uta.eduSockg-ontology#BiomassMineral ||--|o HttpsIdir.uta.eduSockg-ontology#PlantFractionRelatedMeasurement : "https___idir.uta.edu_sockg-ontology#hasPlantFraction"
HttpsIdir.uta.eduSockg-ontology#BiomassMineral ||--|o HttpsIdir.uta.eduSockg-ontology#PlantFraction : "https___idir.uta.edu_sockg-ontology#hasPlantFraction"
HttpsIdir.uta.eduSockg-ontology#BiomassMineral ||--|o HttpsIdir.uta.eduSockg-ontology#Measurement : "https___idir.uta.edu_sockg-ontology#hasMeasurement"
HttpsIdir.uta.eduSockg-ontology#BiomassMineral ||--|o HttpsIdir.uta.eduSockg-ontology#Treatment : "https___idir.uta.edu_sockg-ontology#usesTreatment"
HttpsIdir.uta.eduSockg-ontology#BiomassMineral ||--|o RdfsLiteral : "dct_date"
HttpsIdir.uta.eduSockg-ontology#BiomassMineral ||--|o HttpsIdir.uta.eduSockg-ontology#GrowthStage : "https___idir.uta.edu_sockg-ontology#hasGrowthStage"
HttpsIdir.uta.eduSockg-ontology#BiomassMineral ||--|o HttpsLod.nal.usda.govNalt7140 : "https___idir.uta.edu_sockg-ontology#hasCrop"
HttpsIdir.uta.eduSockg-ontology#BookChapter ||--|o RdfsLiteral : "rdfs_label"
HttpsIdir.uta.eduSockg-ontology#BookChapter ||--|o RdfsLiteral : "dct_issued"
HttpsIdir.uta.eduSockg-ontology#BookChapter ||--|o RdfsLiteral : "dct_title"
HttpsIdir.uta.eduSockg-ontology#BookChapter ||--|o RdfsLiteral : "dct_bibliographicCitation"
HttpsIdir.uta.eduSockg-ontology#BroadleafOrGrass ||--|o RdfsLiteral : "rdfs_label"
HttpsIdir.uta.eduSockg-ontology#ChamberPlacement ||--|o RdfsLiteral : "rdfs_label"
HttpsIdir.uta.eduSockg-ontology#Cultivar ||--|o RdfsLiteral : "rdfs_label"
HttpsIdir.uta.eduSockg-ontology#CuttingHeight ||--|o RdfsLiteral : "rdfs_label"
HttpsIdir.uta.eduSockg-ontology#Equipment ||--|o RdfsLiteral : "rdfs_label"
HttpsIdir.uta.eduSockg-ontology#ExperimentalUnit ||--|o HttpsIdir.uta.eduSockg-ontology#Amendment : "https___idir.uta.edu_sockg-ontology#unitHasAmendment"
HttpsIdir.uta.eduSockg-ontology#ExperimentalUnit ||--|o HttpsIdir.uta.eduSockg-ontology#GrowthStageManagement : "https___idir.uta.edu_sockg-ontology#unitHasGrowthStageManagement"
HttpsIdir.uta.eduSockg-ontology#ExperimentalUnit ||--|o HttpsIdir.uta.eduSockg-ontology#GrazingManagement : "https___idir.uta.edu_sockg-ontology#unitHasGrazingManagement"
HttpsIdir.uta.eduSockg-ontology#ExperimentalUnit ||--|o RdfsLiteral : "dct_identifier"
HttpsIdir.uta.eduSockg-ontology#ExperimentalUnit ||--|o HttpsIdir.uta.eduSockg-ontology#PlantingManagement : "https___idir.uta.edu_sockg-ontology#unitHasPlantingManagement"
HttpsIdir.uta.eduSockg-ontology#ExperimentalUnit ||--|o HttpsIdir.uta.eduSockg-ontology#TillageManagement : "https___idir.uta.edu_sockg-ontology#unitHasTillageManagement"
HttpsIdir.uta.eduSockg-ontology#ExperimentalUnit ||--|o HttpsIdir.uta.eduSockg-ontology#ResidueManagement : "https___idir.uta.edu_sockg-ontology#unitHasResidueManagement"
HttpsIdir.uta.eduSockg-ontology#FundingSource ||--|o RdfsLiteral : "rdfs_label"
HttpsIdir.uta.eduSockg-ontology#GHGFlux ||--|o HttpsIdir.uta.eduSockg-ontology#ExperimentalUnit : "https___idir.uta.edu_sockg-ontology#fromUnit"
HttpsIdir.uta.eduSockg-ontology#GHGFlux ||--|o HttpsIdir.uta.eduSockg-ontology#ChamberPlacement : "https___idir.uta.edu_sockg-ontology#hasChamberPlacement"
HttpsIdir.uta.eduSockg-ontology#GHGFlux ||--|o HttpsIdir.uta.eduSockg-ontology#Measurement : "https___idir.uta.edu_sockg-ontology#hasMeasurement"
HttpsIdir.uta.eduSockg-ontology#GHGFlux ||--|o HttpsIdir.uta.eduSockg-ontology#Treatment : "https___idir.uta.edu_sockg-ontology#usesTreatment"
HttpsIdir.uta.eduSockg-ontology#GHGFlux ||--|o RdfsLiteral : "dct_date"
HttpsIdir.uta.eduSockg-ontology#GHGFlux ||--|o HttpsLod.nal.usda.govNalt7140 : "https___idir.uta.edu_sockg-ontology#hasCrop"
HttpsIdir.uta.eduSockg-ontology#GasNutrientLoss ||--|o HttpsIdir.uta.eduSockg-ontology#ExperimentalUnit : "https___idir.uta.edu_sockg-ontology#fromUnit"
HttpsIdir.uta.eduSockg-ontology#GasNutrientLoss ||--|o HttpsIdir.uta.eduSockg-ontology#SimulationModel : "https___idir.uta.edu_sockg-ontology#usesModel"
HttpsIdir.uta.eduSockg-ontology#GasNutrientLoss ||--|o HttpsIdir.uta.eduSockg-ontology#Measurement : "https___idir.uta.edu_sockg-ontology#hasMeasurement"
HttpsIdir.uta.eduSockg-ontology#GasNutrientLoss ||--|o HttpsIdir.uta.eduSockg-ontology#Treatment : "https___idir.uta.edu_sockg-ontology#usesTreatment"
HttpsIdir.uta.eduSockg-ontology#GasNutrientLoss ||--|o RdfsLiteral : "dct_date"
HttpsIdir.uta.eduSockg-ontology#GasNutrientLoss ||--|o HttpsIdir.uta.eduSockg-ontology#GrowthStage : "https___idir.uta.edu_sockg-ontology#hasGrowthStage"
HttpsIdir.uta.eduSockg-ontology#GasNutrientLoss ||--|o HttpsIdir.uta.eduSockg-ontology#StartStopInterval : "https___idir.uta.edu_sockg-ontology#withStartStopInterval"
HttpsIdir.uta.eduSockg-ontology#GasNutrientLoss ||--|o HttpsLod.nal.usda.govNalt7140 : "https___idir.uta.edu_sockg-ontology#hasCrop"
HttpsIdir.uta.eduSockg-ontology#GrazingManagement ||--|o HttpsIdir.uta.eduSockg-ontology#Measurement : "https___idir.uta.edu_sockg-ontology#hasMeasurement"
HttpsIdir.uta.eduSockg-ontology#GrazingManagement ||--|o HttpsIdir.uta.eduSockg-ontology#AnimalSpecies : "https___idir.uta.edu_sockg-ontology#hasAnimalSpecies"
HttpsIdir.uta.eduSockg-ontology#GrazingManagement ||--|o HttpsIdir.uta.eduSockg-ontology#OtherEvents : "https___idir.uta.edu_sockg-ontology#hasOtherEvents"
HttpsIdir.uta.eduSockg-ontology#GrazingManagement ||--|o HttpsIdir.uta.eduSockg-ontology#AnimalClass : "https___idir.uta.edu_sockg-ontology#hasAnimalClass"
HttpsIdir.uta.eduSockg-ontology#GrazingPlants ||--|o HttpsIdir.uta.eduSockg-ontology#ExperimentalUnit : "https___idir.uta.edu_sockg-ontology#fromUnit"
HttpsIdir.uta.eduSockg-ontology#GrazingPlants ||--|o HttpsIdir.uta.eduSockg-ontology#BroadleafOrGrass : "https___idir.uta.edu_sockg-ontology#hasBroadleafOrGrass"
HttpsIdir.uta.eduSockg-ontology#GrazingPlants ||--|o HttpsIdir.uta.eduSockg-ontology#Measurement : "https___idir.uta.edu_sockg-ontology#hasMeasurement"
HttpsIdir.uta.eduSockg-ontology#GrazingPlants ||--|o HttpsIdir.uta.eduSockg-ontology#Treatment : "https___idir.uta.edu_sockg-ontology#usesTreatment"
HttpsIdir.uta.eduSockg-ontology#GrazingPlants ||--|o RdfsLiteral : "dct_date"
HttpsIdir.uta.eduSockg-ontology#GrazingPlants ||--|o HttpsIdir.uta.eduSockg-ontology#SpeciesMix : "https___idir.uta.edu_sockg-ontology#hasSpeciesMix"
HttpsIdir.uta.eduSockg-ontology#GrazingPlants ||--|o HttpsIdir.uta.eduSockg-ontology#GrowthStage : "https___idir.uta.edu_sockg-ontology#hasGrowthStage"
HttpsIdir.uta.eduSockg-ontology#GrowthStage ||--|o RdfsLiteral : "rdfs_label"
HttpsIdir.uta.eduSockg-ontology#GrowthStageManagement ||--|o HttpsIdir.uta.eduSockg-ontology#GrowthStage : "https___idir.uta.edu_sockg-ontology#hasGrowthStage"
HttpsIdir.uta.eduSockg-ontology#GrowthStageManagement ||--|o RdfsLiteral : "dct_date"
HttpsIdir.uta.eduSockg-ontology#GrowthStageManagement ||--|o HttpsLod.nal.usda.govNalt7140 : "https___idir.uta.edu_sockg-ontology#hasCrop"
HttpsIdir.uta.eduSockg-ontology#HarvestFraction ||--|o HttpsIdir.uta.eduSockg-ontology#ExperimentalUnit : "https___idir.uta.edu_sockg-ontology#fromUnit"
HttpsIdir.uta.eduSockg-ontology#HarvestFraction ||--|o HttpsIdir.uta.eduSockg-ontology#PlantFractionRelatedMeasurement : "https___idir.uta.edu_sockg-ontology#hasPlantFraction"
HttpsIdir.uta.eduSockg-ontology#HarvestFraction ||--|o HttpsIdir.uta.eduSockg-ontology#PlantFraction : "https___idir.uta.edu_sockg-ontology#hasPlantFraction"
HttpsIdir.uta.eduSockg-ontology#HarvestFraction ||--|o HttpsIdir.uta.eduSockg-ontology#Measurement : "https___idir.uta.edu_sockg-ontology#hasMeasurement"
HttpsIdir.uta.eduSockg-ontology#HarvestFraction ||--|o HttpsIdir.uta.eduSockg-ontology#Treatment : "https___idir.uta.edu_sockg-ontology#usesTreatment"
HttpsIdir.uta.eduSockg-ontology#HarvestFraction ||--|o RdfsLiteral : "dct_date"
HttpsIdir.uta.eduSockg-ontology#HarvestFraction ||--|o HttpsIdir.uta.eduSockg-ontology#GrowthStage : "https___idir.uta.edu_sockg-ontology#hasGrowthStage"
HttpsIdir.uta.eduSockg-ontology#HarvestFraction ||--|o HttpsLod.nal.usda.govNalt7140 : "https___idir.uta.edu_sockg-ontology#hasCrop"
HttpsIdir.uta.eduSockg-ontology#HarvestedFraction ||--|o RdfsLiteral : "rdfs_label"
HttpsIdir.uta.eduSockg-ontology#Irrigation ||--|o RdfsLiteral : "rdfs_label"
HttpsIdir.uta.eduSockg-ontology#JournalArticle ||--|o RdfsLiteral : "rdfs_label"
HttpsIdir.uta.eduSockg-ontology#JournalArticle ||--|o RdfsLiteral : "dct_identifier"
HttpsIdir.uta.eduSockg-ontology#JournalArticle ||--|o RdfsLiteral : "dct_title"
HttpsIdir.uta.eduSockg-ontology#JournalArticle ||--|o RdfsLiteral : "dct_bibliographicCitation"
HttpsIdir.uta.eduSockg-ontology#JournalArticle ||--|o RdfsLiteral : "dct_issued"
HttpsIdir.uta.eduSockg-ontology#Location ||--|o GeoGeometry : "geo_hasGeometry"
HttpsIdir.uta.eduSockg-ontology#Location ||--|o RdfsLiteral : "rdfs_label"
HttpsIdir.uta.eduSockg-ontology#Location ||--|o HttpsIdir.uta.eduSockg-ontology#Treatment : "https___idir.uta.edu_sockg-ontology#hasTreatment"
HttpsIdir.uta.eduSockg-ontology#Location ||--|o RdfsLiteral : "dct_identifier"
HttpsIdir.uta.eduSockg-ontology#Location ||--|o KwgoAdministrativeRegion2 : "spatial_connectedTo"
HttpsIdir.uta.eduSockg-ontology#Location ||--|o HttpsIdir.uta.eduSockg-ontology#Site : "spatial_connectedTo"
HttpsIdir.uta.eduSockg-ontology#Location ||--|o KwgoS2CellLevel13 : "spatial_connectedTo"
HttpsIdir.uta.eduSockg-ontology#Location ||--|o HttpsIdir.uta.eduSockg-ontology#Location : "spatial_connectedTo"
HttpsIdir.uta.eduSockg-ontology#Location ||--|o HttpsIdir.uta.eduSockg-ontology#FundingSource : "https___idir.uta.edu_sockg-ontology#fundedBy"
HttpsIdir.uta.eduSockg-ontology#Location ||--|o HttpsIdir.uta.eduSockg-ontology#Thesis : "https___idir.uta.edu_sockg-ontology#cites"
HttpsIdir.uta.eduSockg-ontology#Location ||--|o DctBibliographicResource : "https___idir.uta.edu_sockg-ontology#cites"
HttpsIdir.uta.eduSockg-ontology#Location ||--|o HttpsIdir.uta.eduSockg-ontology#Report : "https___idir.uta.edu_sockg-ontology#cites"
HttpsIdir.uta.eduSockg-ontology#Location ||--|o HttpsIdir.uta.eduSockg-ontology#PopularArticle : "https___idir.uta.edu_sockg-ontology#cites"
HttpsIdir.uta.eduSockg-ontology#Location ||--|o HttpsIdir.uta.eduSockg-ontology#BookChapter : "https___idir.uta.edu_sockg-ontology#cites"
HttpsIdir.uta.eduSockg-ontology#Location ||--|o HttpsIdir.uta.eduSockg-ontology#Abstract : "https___idir.uta.edu_sockg-ontology#cites"
HttpsIdir.uta.eduSockg-ontology#Location ||--|o HttpsIdir.uta.eduSockg-ontology#Proceedings : "https___idir.uta.edu_sockg-ontology#cites"
HttpsIdir.uta.eduSockg-ontology#Location ||--|o HttpsIdir.uta.eduSockg-ontology#JournalArticle : "https___idir.uta.edu_sockg-ontology#cites"
HttpsIdir.uta.eduSockg-ontology#LossesOrDeposition ||--|o RdfsLiteral : "rdfs_label"
HttpsIdir.uta.eduSockg-ontology#Measurement ||--|o QudtQuantityValue : "qudt_quantityValue"
HttpsIdir.uta.eduSockg-ontology#Measurement ||--|o HttpsIdir.uta.eduSockg-ontology#Parameter : "https___idir.uta.edu_sockg-ontology#of"
HttpsIdir.uta.eduSockg-ontology#NutrientEfficiency ||--|o HttpsIdir.uta.eduSockg-ontology#ExperimentalUnit : "https___idir.uta.edu_sockg-ontology#fromUnit"
HttpsIdir.uta.eduSockg-ontology#NutrientEfficiency ||--|o HttpsIdir.uta.eduSockg-ontology#PlantFractionRelatedMeasurement : "https___idir.uta.edu_sockg-ontology#hasPlantFraction"
HttpsIdir.uta.eduSockg-ontology#NutrientEfficiency ||--|o HttpsIdir.uta.eduSockg-ontology#PlantFraction : "https___idir.uta.edu_sockg-ontology#hasPlantFraction"
HttpsIdir.uta.eduSockg-ontology#NutrientEfficiency ||--|o HttpsIdir.uta.eduSockg-ontology#Measurement : "https___idir.uta.edu_sockg-ontology#hasMeasurement"
HttpsIdir.uta.eduSockg-ontology#NutrientEfficiency ||--|o HttpsIdir.uta.eduSockg-ontology#Treatment : "https___idir.uta.edu_sockg-ontology#usesTreatment"
HttpsIdir.uta.eduSockg-ontology#NutrientEfficiency ||--|o RdfsLiteral : "dct_date"
HttpsIdir.uta.eduSockg-ontology#NutrientEfficiency ||--|o HttpsIdir.uta.eduSockg-ontology#GrowthStage : "https___idir.uta.edu_sockg-ontology#hasGrowthStage"
HttpsIdir.uta.eduSockg-ontology#NutrientEfficiency ||--|o HttpsLod.nal.usda.govNalt7140 : "https___idir.uta.edu_sockg-ontology#hasCrop"
HttpsIdir.uta.eduSockg-ontology#OtherEvents ||--|o RdfsLiteral : "rdfs_label"
HttpsIdir.uta.eduSockg-ontology#Parameter ||--|o RdfsLiteral : "rdfs_label"
HttpsIdir.uta.eduSockg-ontology#PesticidePlacement ||--|o RdfsLiteral : "rdfs_label"
HttpsIdir.uta.eduSockg-ontology#PesticideTarget ||--|o RdfsLiteral : "rdfs_label"
HttpsIdir.uta.eduSockg-ontology#PlantFraction ||--|o RdfsLiteral : "rdfs_label"
HttpsIdir.uta.eduSockg-ontology#PlantingManagement ||--|o HttpsIdir.uta.eduSockg-ontology#Measurement : "https___idir.uta.edu_sockg-ontology#hasMeasurement"
HttpsIdir.uta.eduSockg-ontology#PlantingManagement ||--|o HttpsIdir.uta.eduSockg-ontology#PlantingMethod : "https___idir.uta.edu_sockg-ontology#usesPlantingMethod"
HttpsIdir.uta.eduSockg-ontology#PlantingManagement ||--|o HttpsIdir.uta.eduSockg-ontology#Cultivar : "https___idir.uta.edu_sockg-ontology#hasCultivar"
HttpsIdir.uta.eduSockg-ontology#PlantingManagement ||--|o HttpsLod.nal.usda.govNalt7140 : "https___idir.uta.edu_sockg-ontology#hasCrop"
HttpsIdir.uta.eduSockg-ontology#PlantingMethod ||--|o RdfsLiteral : "rdfs_label"
HttpsIdir.uta.eduSockg-ontology#PopularArticle ||--|o RdfsLiteral : "rdfs_label"
HttpsIdir.uta.eduSockg-ontology#PopularArticle ||--|o RdfsLiteral : "dct_title"
HttpsIdir.uta.eduSockg-ontology#PopularArticle ||--|o RdfsLiteral : "dct_bibliographicCitation"
HttpsIdir.uta.eduSockg-ontology#PopularArticle ||--|o RdfsLiteral : "dct_issued"
HttpsIdir.uta.eduSockg-ontology#Proceedings ||--|o RdfsLiteral : "rdfs_label"
HttpsIdir.uta.eduSockg-ontology#Proceedings ||--|o RdfsLiteral : "dct_title"
HttpsIdir.uta.eduSockg-ontology#Proceedings ||--|o RdfsLiteral : "dct_bibliographicCitation"
HttpsIdir.uta.eduSockg-ontology#Proceedings ||--|o RdfsLiteral : "dct_issued"
HttpsIdir.uta.eduSockg-ontology#Report ||--|o RdfsLiteral : "rdfs_label"
HttpsIdir.uta.eduSockg-ontology#Report ||--|o RdfsLiteral : "dct_title"
HttpsIdir.uta.eduSockg-ontology#Report ||--|o RdfsLiteral : "dct_bibliographicCitation"
HttpsIdir.uta.eduSockg-ontology#Report ||--|o RdfsLiteral : "dct_issued"
HttpsIdir.uta.eduSockg-ontology#ResidueManagement ||--|o HttpsIdir.uta.eduSockg-ontology#Equipment : "https___idir.uta.edu_sockg-ontology#usesEquipment"
HttpsIdir.uta.eduSockg-ontology#ResidueManagement ||--|o HttpsIdir.uta.eduSockg-ontology#Measurement : "https___idir.uta.edu_sockg-ontology#hasMeasurement"
HttpsIdir.uta.eduSockg-ontology#ResidueManagement ||--|o HttpsIdir.uta.eduSockg-ontology#CuttingHeight : "https___idir.uta.edu_sockg-ontology#withCuttingHeight"
HttpsIdir.uta.eduSockg-ontology#ResidueManagement ||--|o HttpsIdir.uta.eduSockg-ontology#GrowthStage : "https___idir.uta.edu_sockg-ontology#hasGrowthStage"
HttpsIdir.uta.eduSockg-ontology#ResidueManagement ||--|o HttpsLod.nal.usda.govNalt7140 : "https___idir.uta.edu_sockg-ontology#hasCrop"
HttpsIdir.uta.eduSockg-ontology#ResidueMeasurement ||--|o HttpsIdir.uta.eduSockg-ontology#ExperimentalUnit : "https___idir.uta.edu_sockg-ontology#fromUnit"
HttpsIdir.uta.eduSockg-ontology#ResidueMeasurement ||--|o HttpsIdir.uta.eduSockg-ontology#Measurement : "https___idir.uta.edu_sockg-ontology#hasMeasurement"
HttpsIdir.uta.eduSockg-ontology#ResidueMeasurement ||--|o HttpsIdir.uta.eduSockg-ontology#Treatment : "https___idir.uta.edu_sockg-ontology#usesTreatment"
HttpsIdir.uta.eduSockg-ontology#ResidueMeasurement ||--|o RdfsLiteral : "dct_date"
HttpsIdir.uta.eduSockg-ontology#ResidueMeasurement ||--|o HttpsIdir.uta.eduSockg-ontology#HarvestedFraction : "https___idir.uta.edu_sockg-ontology#hasHarvestedFraction"
HttpsIdir.uta.eduSockg-ontology#ResidueMeasurement ||--|o HttpsIdir.uta.eduSockg-ontology#GrowthStage : "https___idir.uta.edu_sockg-ontology#hasGrowthStage"
HttpsIdir.uta.eduSockg-ontology#ResidueMeasurement ||--|o HttpsLod.nal.usda.govNalt7140 : "https___idir.uta.edu_sockg-ontology#hasCrop"
HttpsIdir.uta.eduSockg-ontology#SimulationModel ||--|o RdfsLiteral : "rdfs_label"
HttpsIdir.uta.eduSockg-ontology#Site ||--|o RdfsLiteral : "dct_identifier"
HttpsIdir.uta.eduSockg-ontology#Site ||--|o KwgoAdministrativeRegion2 : "spatial_connectedTo"
HttpsIdir.uta.eduSockg-ontology#Site ||--|o HttpsIdir.uta.eduSockg-ontology#Site : "spatial_connectedTo"
HttpsIdir.uta.eduSockg-ontology#Site ||--|o KwgoS2CellLevel13 : "spatial_connectedTo"
HttpsIdir.uta.eduSockg-ontology#Site ||--|o HttpsIdir.uta.eduSockg-ontology#Location : "spatial_connectedTo"
HttpsIdir.uta.eduSockg-ontology#Site ||--|o SdosText : "sdos_postalCode"
HttpsIdir.uta.eduSockg-ontology#SoilBiologicalSample ||--|o HttpsIdir.uta.eduSockg-ontology#ExperimentalUnit : "https___idir.uta.edu_sockg-ontology#fromUnit"
HttpsIdir.uta.eduSockg-ontology#SoilBiologicalSample ||--|o HttpsIdir.uta.eduSockg-ontology#Measurement : "https___idir.uta.edu_sockg-ontology#hasMeasurement"
HttpsIdir.uta.eduSockg-ontology#SoilBiologicalSample ||--|o HttpsIdir.uta.eduSockg-ontology#Treatment : "https___idir.uta.edu_sockg-ontology#usesTreatment"
HttpsIdir.uta.eduSockg-ontology#SoilBiologicalSample ||--|o RdfsLiteral : "dct_date"
HttpsIdir.uta.eduSockg-ontology#SoilBiologicalSample ||--|o QudtQuantityValue : "https___idir.uta.edu_sockg-ontology#upperDepth"
HttpsIdir.uta.eduSockg-ontology#SoilBiologicalSample ||--|o QudtQuantityValue : "https___idir.uta.edu_sockg-ontology#lowerDepth"
HttpsIdir.uta.eduSockg-ontology#SoilChemicalSample ||--|o HttpsIdir.uta.eduSockg-ontology#ExperimentalUnit : "https___idir.uta.edu_sockg-ontology#fromUnit"
HttpsIdir.uta.eduSockg-ontology#SoilChemicalSample ||--|o HttpsIdir.uta.eduSockg-ontology#SimulationModel : "https___idir.uta.edu_sockg-ontology#usesModel"
HttpsIdir.uta.eduSockg-ontology#SoilChemicalSample ||--|o HttpsIdir.uta.eduSockg-ontology#Measurement : "https___idir.uta.edu_sockg-ontology#hasMeasurement"
HttpsIdir.uta.eduSockg-ontology#SoilChemicalSample ||--|o HttpsIdir.uta.eduSockg-ontology#Treatment : "https___idir.uta.edu_sockg-ontology#usesTreatment"
HttpsIdir.uta.eduSockg-ontology#SoilChemicalSample ||--|o RdfsLiteral : "dct_date"
HttpsIdir.uta.eduSockg-ontology#SoilChemicalSample ||--|o QudtQuantityValue : "https___idir.uta.edu_sockg-ontology#upperDepth"
HttpsIdir.uta.eduSockg-ontology#SoilChemicalSample ||--|o QudtQuantityValue : "https___idir.uta.edu_sockg-ontology#lowerDepth"
HttpsIdir.uta.eduSockg-ontology#SoilCover ||--|o HttpsIdir.uta.eduSockg-ontology#Timing : "https___idir.uta.edu_sockg-ontology#hasTiming"
HttpsIdir.uta.eduSockg-ontology#SoilCover ||--|o HttpsIdir.uta.eduSockg-ontology#ExperimentalUnit : "https___idir.uta.edu_sockg-ontology#fromUnit"
HttpsIdir.uta.eduSockg-ontology#SoilCover ||--|o HttpsIdir.uta.eduSockg-ontology#Treatment : "https___idir.uta.edu_sockg-ontology#usesTreatment"
HttpsIdir.uta.eduSockg-ontology#SoilCover ||--|o RdfsLiteral : "dct_date"
HttpsIdir.uta.eduSockg-ontology#SoilCover ||--|o HttpsLod.nal.usda.govNalt7140 : "https___idir.uta.edu_sockg-ontology#hasCrop"
HttpsIdir.uta.eduSockg-ontology#SoilPhysicalSample ||--|o HttpsIdir.uta.eduSockg-ontology#ExperimentalUnit : "https___idir.uta.edu_sockg-ontology#fromUnit"
HttpsIdir.uta.eduSockg-ontology#SoilPhysicalSample ||--|o HttpsIdir.uta.eduSockg-ontology#SimulationModel : "https___idir.uta.edu_sockg-ontology#usesModel"
HttpsIdir.uta.eduSockg-ontology#SoilPhysicalSample ||--|o HttpsIdir.uta.eduSockg-ontology#Measurement : "https___idir.uta.edu_sockg-ontology#hasMeasurement"
HttpsIdir.uta.eduSockg-ontology#SoilPhysicalSample ||--|o HttpsIdir.uta.eduSockg-ontology#Treatment : "https___idir.uta.edu_sockg-ontology#usesTreatment"
HttpsIdir.uta.eduSockg-ontology#SoilPhysicalSample ||--|o RdfsLiteral : "dct_date"
HttpsIdir.uta.eduSockg-ontology#SoilPhysicalSample ||--|o QudtQuantityValue : "https___idir.uta.edu_sockg-ontology#upperDepth"
HttpsIdir.uta.eduSockg-ontology#SoilPhysicalSample ||--|o QudtQuantityValue : "https___idir.uta.edu_sockg-ontology#lowerDepth"
HttpsIdir.uta.eduSockg-ontology#SpeciesMix ||--|o RdfsLiteral : "rdfs_label"
HttpsIdir.uta.eduSockg-ontology#StartStopInterval ||--|o RdfsLiteral : "rdfs_label"
HttpsIdir.uta.eduSockg-ontology#SurfaceOrLeaching ||--|o RdfsLiteral : "rdfs_label"
HttpsIdir.uta.eduSockg-ontology#Thesis ||--|o RdfsLiteral : "rdfs_label"
HttpsIdir.uta.eduSockg-ontology#Thesis ||--|o RdfsLiteral : "dct_title"
HttpsIdir.uta.eduSockg-ontology#Thesis ||--|o RdfsLiteral : "dct_bibliographicCitation"
HttpsIdir.uta.eduSockg-ontology#Thesis ||--|o RdfsLiteral : "dct_issued"
HttpsIdir.uta.eduSockg-ontology#TillageEvent ||--|o RdfsLiteral : "rdfs_label"
HttpsIdir.uta.eduSockg-ontology#TillageManagement ||--|o HttpsIdir.uta.eduSockg-ontology#Measurement : "https___idir.uta.edu_sockg-ontology#hasMeasurement"
HttpsIdir.uta.eduSockg-ontology#TillageManagement ||--|o HttpsIdir.uta.eduSockg-ontology#TillageEvent : "https___idir.uta.edu_sockg-ontology#hasTillageEvent"
HttpsIdir.uta.eduSockg-ontology#TillageManagement ||--|o HttpsIdir.uta.eduSockg-ontology#TillageMethod : "https___idir.uta.edu_sockg-ontology#usesTillageMethod"
HttpsIdir.uta.eduSockg-ontology#TillageManagement ||--|o HttpsLod.nal.usda.govNalt7140 : "https___idir.uta.edu_sockg-ontology#hasCrop"
HttpsIdir.uta.eduSockg-ontology#TillageMethod ||--|o RdfsLiteral : "rdfs_label"
HttpsIdir.uta.eduSockg-ontology#Treatment ||--|o RdfsLiteral : "dct_identifier"
HttpsIdir.uta.eduSockg-ontology#Treatment ||--|o HttpsIdir.uta.eduSockg-ontology#Amendment : "https___idir.uta.edu_sockg-ontology#treatmentHasAmendment"
HttpsIdir.uta.eduSockg-ontology#Treatment ||--|o HttpsIdir.uta.eduSockg-ontology#PlantingManagement : "https___idir.uta.edu_sockg-ontology#treatmentHasPlantingManagement"
HttpsIdir.uta.eduSockg-ontology#Treatment ||--|o HttpsIdir.uta.eduSockg-ontology#GrazingRate : "https___idir.uta.edu_sockg-ontology#hasGrazingRate"
HttpsIdir.uta.eduSockg-ontology#Treatment ||--|o HttpsIdir.uta.eduSockg-ontology#CoverCrop : "https___idir.uta.edu_sockg-ontology#usesCoverCrop"
HttpsIdir.uta.eduSockg-ontology#Treatment ||--|o HttpsIdir.uta.eduSockg-ontology#GrazingManagement : "https___idir.uta.edu_sockg-ontology#treatmentHasGrazingManagement"
HttpsIdir.uta.eduSockg-ontology#Treatment ||--|o HttpsIdir.uta.eduSockg-ontology#Rotation : "https___idir.uta.edu_sockg-ontology#hasRotation"
HttpsIdir.uta.eduSockg-ontology#Treatment ||--|o HttpsIdir.uta.eduSockg-ontology#FertilizerAmendment : "https___idir.uta.edu_sockg-ontology#usesFertilizerAmendment"
HttpsIdir.uta.eduSockg-ontology#Treatment ||--|o HttpsIdir.uta.eduSockg-ontology#AnimalSpecies : "https___idir.uta.edu_sockg-ontology#hasAnimalSpecies"
HttpsIdir.uta.eduSockg-ontology#Treatment ||--|o HttpsIdir.uta.eduSockg-ontology#ResidueManagement : "https___idir.uta.edu_sockg-ontology#treatmentHasResidueManagement"
HttpsIdir.uta.eduSockg-ontology#Treatment ||--|o HttpsIdir.uta.eduSockg-ontology#GrowthStageManagement : "https___idir.uta.edu_sockg-ontology#treatmentHasGrowthStageManagement"
HttpsIdir.uta.eduSockg-ontology#Treatment ||--|o HttpsIdir.uta.eduSockg-ontology#ProjectScenario : "https___idir.uta.edu_sockg-ontology#hasProjectScenario"
HttpsIdir.uta.eduSockg-ontology#Treatment ||--|o HttpsIdir.uta.eduSockg-ontology#ResidueRemoval : "https___idir.uta.edu_sockg-ontology#usesResidueRemoval"
HttpsIdir.uta.eduSockg-ontology#Treatment ||--|o HttpsIdir.uta.eduSockg-ontology#Project : "https___idir.uta.edu_sockg-ontology#fromProject"
HttpsIdir.uta.eduSockg-ontology#Treatment ||--|o HttpsIdir.uta.eduSockg-ontology#TillageManagement : "https___idir.uta.edu_sockg-ontology#treatmentHasTillageManagement"
HttpsIdir.uta.eduSockg-ontology#Treatment ||--|o HttpsIdir.uta.eduSockg-ontology#Tillage : "https___idir.uta.edu_sockg-ontology#hasTillage"
HttpsIdir.uta.eduSockg-ontology#WaterQualityArea ||--|o HttpsIdir.uta.eduSockg-ontology#ExperimentalUnit : "https___idir.uta.edu_sockg-ontology#fromUnit"
HttpsIdir.uta.eduSockg-ontology#WaterQualityArea ||--|o HttpsIdir.uta.eduSockg-ontology#LossesOrDeposition : "https___idir.uta.edu_sockg-ontology#hasLossesOrDeposition"
HttpsIdir.uta.eduSockg-ontology#WaterQualityArea ||--|o HttpsIdir.uta.eduSockg-ontology#Measurement : "https___idir.uta.edu_sockg-ontology#hasMeasurement"
HttpsIdir.uta.eduSockg-ontology#WaterQualityArea ||--|o HttpsIdir.uta.eduSockg-ontology#SurfaceOrLeaching : "https___idir.uta.edu_sockg-ontology#hasSurfaceOrLeaching"
HttpsIdir.uta.eduSockg-ontology#WaterQualityArea ||--|o HttpsIdir.uta.eduSockg-ontology#Treatment : "https___idir.uta.edu_sockg-ontology#usesTreatment"
HttpsIdir.uta.eduSockg-ontology#WaterQualityArea ||--|o RdfsLiteral : "dct_date"
HttpsIdir.uta.eduSockg-ontology#WaterQualityConcentration ||--|o HttpsIdir.uta.eduSockg-ontology#ExperimentalUnit : "https___idir.uta.edu_sockg-ontology#fromUnit"
HttpsIdir.uta.eduSockg-ontology#WaterQualityConcentration ||--|o HttpsIdir.uta.eduSockg-ontology#SimulationModel : "https___idir.uta.edu_sockg-ontology#usesModel"
HttpsIdir.uta.eduSockg-ontology#WaterQualityConcentration ||--|o HttpsIdir.uta.eduSockg-ontology#Measurement : "https___idir.uta.edu_sockg-ontology#hasMeasurement"
HttpsIdir.uta.eduSockg-ontology#WaterQualityConcentration ||--|o HttpsIdir.uta.eduSockg-ontology#SurfaceOrLeaching : "https___idir.uta.edu_sockg-ontology#hasSurfaceOrLeaching"
HttpsIdir.uta.eduSockg-ontology#WaterQualityConcentration ||--|o HttpsIdir.uta.eduSockg-ontology#Treatment : "https___idir.uta.edu_sockg-ontology#usesTreatment"
HttpsIdir.uta.eduSockg-ontology#WaterQualityConcentration ||--|o RdfsLiteral : "dct_date"
HttpsIdir.uta.eduSockg-ontology#WaterQualityConcentration ||--|o HttpsIdir.uta.eduSockg-ontology#GrowthStage : "https___idir.uta.edu_sockg-ontology#hasGrowthStage"
HttpsIdir.uta.eduSockg-ontology#WaterQualityConcentration ||--|o HttpsIdir.uta.eduSockg-ontology#StartStopInterval : "https___idir.uta.edu_sockg-ontology#withStartStopInterval"
HttpsIdir.uta.eduSockg-ontology#WaterQualityConcentration ||--|o HttpsLod.nal.usda.govNalt7140 : "https___idir.uta.edu_sockg-ontology#hasCrop"
HttpsIdir.uta.eduSockg-ontology#WeatherObservation ||--|o HttpsIdir.uta.eduSockg-ontology#ExperimentalUnit : "https___idir.uta.edu_sockg-ontology#fromUnit"
HttpsIdir.uta.eduSockg-ontology#WeatherObservation ||--|o HttpsIdir.uta.eduSockg-ontology#Measurement : "https___idir.uta.edu_sockg-ontology#hasMeasurement"
HttpsIdir.uta.eduSockg-ontology#WeatherObservation ||--|o HttpsIdir.uta.eduSockg-ontology#Treatment : "https___idir.uta.edu_sockg-ontology#usesTreatment"
HttpsIdir.uta.eduSockg-ontology#WeatherObservation ||--|o RdfsLiteral : "dct_date"
HttpsIdir.uta.eduSockg-ontology#WeatherObservation ||--|o HttpsIdir.uta.eduSockg-ontology#Location : "https___idir.uta.edu_sockg-ontology#weatherAt"
HttpsIdir.uta.eduSockg-ontology#WindErosionArea ||--|o HttpsIdir.uta.eduSockg-ontology#ExperimentalUnit : "https___idir.uta.edu_sockg-ontology#fromUnit"
HttpsIdir.uta.eduSockg-ontology#WindErosionArea ||--|o HttpsIdir.uta.eduSockg-ontology#SimulationModel : "https___idir.uta.edu_sockg-ontology#usesModel"
HttpsIdir.uta.eduSockg-ontology#WindErosionArea ||--|o HttpsIdir.uta.eduSockg-ontology#LossesOrDeposition : "https___idir.uta.edu_sockg-ontology#hasLossesOrDeposition"
HttpsIdir.uta.eduSockg-ontology#WindErosionArea ||--|o HttpsIdir.uta.eduSockg-ontology#Measurement : "https___idir.uta.edu_sockg-ontology#hasMeasurement"
HttpsIdir.uta.eduSockg-ontology#WindErosionArea ||--|o HttpsIdir.uta.eduSockg-ontology#Treatment : "https___idir.uta.edu_sockg-ontology#usesTreatment"
HttpsIdir.uta.eduSockg-ontology#WindErosionArea ||--|o RdfsLiteral : "dct_date"
HttpsIdir.uta.eduSockg-ontology#WindErosionArea ||--|o HttpsIdir.uta.eduSockg-ontology#GrowthStage : "https___idir.uta.edu_sockg-ontology#hasGrowthStage"
HttpsIdir.uta.eduSockg-ontology#WindErosionArea ||--|o HttpsIdir.uta.eduSockg-ontology#StartStopInterval : "https___idir.uta.edu_sockg-ontology#withStartStopInterval"
HttpsIdir.uta.eduSockg-ontology#YieldNutrientUptake ||--|o HttpsIdir.uta.eduSockg-ontology#ExperimentalUnit : "https___idir.uta.edu_sockg-ontology#fromUnit"
HttpsIdir.uta.eduSockg-ontology#YieldNutrientUptake ||--|o HttpsIdir.uta.eduSockg-ontology#PlantFractionRelatedMeasurement : "https___idir.uta.edu_sockg-ontology#hasPlantFraction"
HttpsIdir.uta.eduSockg-ontology#YieldNutrientUptake ||--|o HttpsIdir.uta.eduSockg-ontology#PlantFraction : "https___idir.uta.edu_sockg-ontology#hasPlantFraction"
HttpsIdir.uta.eduSockg-ontology#YieldNutrientUptake ||--|o HttpsIdir.uta.eduSockg-ontology#Measurement : "https___idir.uta.edu_sockg-ontology#hasMeasurement"
HttpsIdir.uta.eduSockg-ontology#YieldNutrientUptake ||--|o HttpsIdir.uta.eduSockg-ontology#Treatment : "https___idir.uta.edu_sockg-ontology#usesTreatment"
HttpsIdir.uta.eduSockg-ontology#YieldNutrientUptake ||--|o RdfsLiteral : "dct_date"
HttpsIdir.uta.eduSockg-ontology#YieldNutrientUptake ||--|o HttpsIdir.uta.eduSockg-ontology#GrowthStage : "https___idir.uta.edu_sockg-ontology#hasGrowthStage"
HttpsIdir.uta.eduSockg-ontology#YieldNutrientUptake ||--|o HttpsLod.nal.usda.govNalt7140 : "https___idir.uta.edu_sockg-ontology#hasCrop"
HttpsLod.nal.usda.govNalt7140 ||--|o RdfsLiteral : "rdfs_label"
KwgoS2CellLevel13 ||--|o KwgoAdministrativeRegion2 : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o HttpsIdir.uta.eduSockg-ontology#Site : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o KwgoS2CellLevel13 : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o HttpsIdir.uta.eduSockg-ontology#Location : "spatial_connectedTo"

```



## Imports


* okns:qudt
* okns:sdo
* linkml:types
* okns:dc
* okns:extended_types
* okns:geo
* okns:kwg
* okns:owl-rdf-rdfs
* okns:bibo



## Classes

| Class | Description | Occurrences |
| --- | --- | --- |
| [DctBibliographicResource](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/DctBibliographicResource.md) | A book, article, or other documentary resource.<br/>| 14 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpsIdir.uta.eduSockg-ontology#Abstract](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#Abstract.md) | None<br/>| 3 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpsIdir.uta.eduSockg-ontology#BookChapter](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#BookChapter.md) | None<br/>| 2 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpsIdir.uta.eduSockg-ontology#JournalArticle](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#JournalArticle.md) | None<br/>| 149 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpsIdir.uta.eduSockg-ontology#PopularArticle](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#PopularArticle.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpsIdir.uta.eduSockg-ontology#Proceedings](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#Proceedings.md) | None<br/>| 3 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpsIdir.uta.eduSockg-ontology#Report](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#Report.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpsIdir.uta.eduSockg-ontology#Thesis](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#Thesis.md) | None<br/>| 4 | 
| [GeoSpatialObject](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/GeoSpatialObject.md) | Anything spatial (being or having a shape, position or an extent).<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[GeoFeature](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/GeoFeature.md) | A discrete spatial phenomenon in a universe of discourse.<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpsIdir.uta.eduSockg-ontology#ExperimentalUnit](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#ExperimentalUnit.md) | None<br/>| 3863 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpsIdir.uta.eduSockg-ontology#Location](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#Location.md) | None<br/>| 58 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpsIdir.uta.eduSockg-ontology#Site](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#Site.md) | None<br/>| 60 | 
| [HttpsIdir.uta.eduSockg-ontology#ActiveIngredient](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#ActiveIngredient.md) | None<br/>| 84 | 
| [HttpsIdir.uta.eduSockg-ontology#AmendmentPlacement](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#AmendmentPlacement.md) | None<br/>| 10 | 
| [HttpsIdir.uta.eduSockg-ontology#AmendmentType](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#AmendmentType.md) | None<br/>| 73 | 
| [HttpsIdir.uta.eduSockg-ontology#AnimalClass](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#AnimalClass.md) | None<br/>| 4 | 
| [HttpsIdir.uta.eduSockg-ontology#AnimalSpecies](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#AnimalSpecies.md) | None<br/>| 3 | 
| [HttpsIdir.uta.eduSockg-ontology#BroadleafOrGrass](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#BroadleafOrGrass.md) | None<br/>| 2 | 
| [HttpsIdir.uta.eduSockg-ontology#ChamberPlacement](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#ChamberPlacement.md) | None<br/>| 7 | 
| [HttpsIdir.uta.eduSockg-ontology#CoverCrop](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#CoverCrop.md) | None<br/>| 8 | 
| [HttpsIdir.uta.eduSockg-ontology#Cultivar](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#Cultivar.md) | None<br/>| 308 | 
| [HttpsIdir.uta.eduSockg-ontology#CuttingHeight](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#CuttingHeight.md) | None<br/>| 17 | 
| [HttpsIdir.uta.eduSockg-ontology#Equipment](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#Equipment.md) | None<br/>| 12 | 
| [HttpsIdir.uta.eduSockg-ontology#FertilizerAmendment](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#FertilizerAmendment.md) | None<br/>| 4 | 
| [HttpsIdir.uta.eduSockg-ontology#FundingSource](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#FundingSource.md) | None<br/>| 7 | 
| [HttpsIdir.uta.eduSockg-ontology#GrazingRate](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#GrazingRate.md) | None<br/>| 3 | 
| [HttpsIdir.uta.eduSockg-ontology#GrowthStage](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#GrowthStage.md) | None<br/>| 33 | 
| [HttpsIdir.uta.eduSockg-ontology#HarvestedFraction](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#HarvestedFraction.md) | None<br/>| 12 | 
| [HttpsIdir.uta.eduSockg-ontology#Irrigation](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#Irrigation.md) | None<br/>| 4 | 
| [HttpsIdir.uta.eduSockg-ontology#LossesOrDeposition](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#LossesOrDeposition.md) | None<br/>| 2 | 
| [HttpsIdir.uta.eduSockg-ontology#MeasurableEntity](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#MeasurableEntity.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpsIdir.uta.eduSockg-ontology#Amendment](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#Amendment.md) | None<br/>| 47106 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpsIdir.uta.eduSockg-ontology#GrazingManagement](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#GrazingManagement.md) | None<br/>| 1951 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpsIdir.uta.eduSockg-ontology#GrowthStageManagement](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#GrowthStageManagement.md) | None<br/>| 5148 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpsIdir.uta.eduSockg-ontology#PlantingManagement](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#PlantingManagement.md) | None<br/>| 23728 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpsIdir.uta.eduSockg-ontology#ResidueManagement](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#ResidueManagement.md) | None<br/>| 3334 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpsIdir.uta.eduSockg-ontology#Sample](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#Sample.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpsIdir.uta.eduSockg-ontology#CropRelatedMeasurement](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#CropRelatedMeasurement.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpsIdir.uta.eduSockg-ontology#GHGFlux](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#GHGFlux.md) | None<br/>| 132766 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpsIdir.uta.eduSockg-ontology#SoilCover](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#SoilCover.md) | None<br/>| 1034 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpsIdir.uta.eduSockg-ontology#ErosionMeasurement](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#ErosionMeasurement.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpsIdir.uta.eduSockg-ontology#GrowthStageRelatedMeasurement](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#GrowthStageRelatedMeasurement.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpsIdir.uta.eduSockg-ontology#GrazingPlants](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#GrazingPlants.md) | None<br/>| 6996 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpsIdir.uta.eduSockg-ontology#ResidueMeasurement](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#ResidueMeasurement.md) | None<br/>| 18512 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpsIdir.uta.eduSockg-ontology#PlantFractionRelatedMeasurement](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#PlantFractionRelatedMeasurement.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpsIdir.uta.eduSockg-ontology#BiomassAnalysis](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#BiomassAnalysis.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpsIdir.uta.eduSockg-ontology#BiomassCarbohydrate](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#BiomassCarbohydrate.md) | None<br/>| 1367 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpsIdir.uta.eduSockg-ontology#BiomassEnergy](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#BiomassEnergy.md) | None<br/>| 799 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpsIdir.uta.eduSockg-ontology#BiomassMineral](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#BiomassMineral.md) | None<br/>| 6739 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpsIdir.uta.eduSockg-ontology#HarvestFraction](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#HarvestFraction.md) | None<br/>| 9470 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpsIdir.uta.eduSockg-ontology#NutrientEfficiency](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#NutrientEfficiency.md) | None<br/>| 5159 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpsIdir.uta.eduSockg-ontology#PossiblySimulatedMeasurement](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#PossiblySimulatedMeasurement.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpsIdir.uta.eduSockg-ontology#SoilSample](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#SoilSample.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpsIdir.uta.eduSockg-ontology#SoilBiologicalSample](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#SoilBiologicalSample.md) | None<br/>| 18273 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpsIdir.uta.eduSockg-ontology#SoilChemicalSample](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#SoilChemicalSample.md) | None<br/>| 54269 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpsIdir.uta.eduSockg-ontology#SoilPhysicalSample](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#SoilPhysicalSample.md) | None<br/>| 28237 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpsIdir.uta.eduSockg-ontology#WindErosionArea](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#WindErosionArea.md) | None<br/>| 34 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpsIdir.uta.eduSockg-ontology#YieldNutrientUptake](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#YieldNutrientUptake.md) | None<br/>| 704 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpsIdir.uta.eduSockg-ontology#QualityMeasurement](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#QualityMeasurement.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpsIdir.uta.eduSockg-ontology#GasNutrientLoss](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#GasNutrientLoss.md) | None<br/>| 2231 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpsIdir.uta.eduSockg-ontology#WaterQualityArea](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#WaterQualityArea.md) | None<br/>| 681 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpsIdir.uta.eduSockg-ontology#WaterQualityConcentration](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#WaterQualityConcentration.md) | None<br/>| 2305 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpsIdir.uta.eduSockg-ontology#TillageManagement](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#TillageManagement.md) | None<br/>| 27450 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpsIdir.uta.eduSockg-ontology#WeatherObservation](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#WeatherObservation.md) | None<br/>| 149774 | 
| [HttpsIdir.uta.eduSockg-ontology#Measurement](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#Measurement.md) | None<br/>| 3180012 | 
| [HttpsIdir.uta.eduSockg-ontology#OtherEvents](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#OtherEvents.md) | None<br/>| 2 | 
| [HttpsIdir.uta.eduSockg-ontology#Parameter](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#Parameter.md) | None<br/>| 156 | 
| [HttpsIdir.uta.eduSockg-ontology#PesticidePlacement](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#PesticidePlacement.md) | None<br/>| 5 | 
| [HttpsIdir.uta.eduSockg-ontology#PesticideTarget](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#PesticideTarget.md) | None<br/>| 38 | 
| [HttpsIdir.uta.eduSockg-ontology#PlantFraction](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#PlantFraction.md) | None<br/>| 29 | 
| [HttpsIdir.uta.eduSockg-ontology#PlantingMethod](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#PlantingMethod.md) | None<br/>| 6 | 
| [HttpsIdir.uta.eduSockg-ontology#Project](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#Project.md) | None<br/>| 3 | 
| [HttpsIdir.uta.eduSockg-ontology#ProjectScenario](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#ProjectScenario.md) | None<br/>| 19 | 
| [HttpsIdir.uta.eduSockg-ontology#ResidueRemoval](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#ResidueRemoval.md) | None<br/>| 3 | 
| [HttpsIdir.uta.eduSockg-ontology#Rotation](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#Rotation.md) | None<br/>| 66 | 
| [HttpsIdir.uta.eduSockg-ontology#SimulationModel](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#SimulationModel.md) | None<br/>| 12 | 
| [HttpsIdir.uta.eduSockg-ontology#SpeciesMix](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#SpeciesMix.md) | None<br/>| 7 | 
| [HttpsIdir.uta.eduSockg-ontology#StartStopInterval](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#StartStopInterval.md) | None<br/>| 3 | 
| [HttpsIdir.uta.eduSockg-ontology#SurfaceOrLeaching](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#SurfaceOrLeaching.md) | None<br/>| 2 | 
| [HttpsIdir.uta.eduSockg-ontology#Tillage](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#Tillage.md) | None<br/>| 8 | 
| [HttpsIdir.uta.eduSockg-ontology#TillageEvent](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#TillageEvent.md) | None<br/>| 18 | 
| [HttpsIdir.uta.eduSockg-ontology#TillageMethod](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#TillageMethod.md) | None<br/>| 61 | 
| [HttpsIdir.uta.eduSockg-ontology#Timing](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#Timing.md) | None<br/>| 7 | 
| [HttpsIdir.uta.eduSockg-ontology#Treatment](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsIdir.uta.eduSockg-ontology#Treatment.md) | None<br/>| 769 | 
| [HttpsLod.nal.usda.govNalt7140](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/HttpsLod.nal.usda.govNalt7140.md) | None<br/>| 48 | 
| [KwgoS2CellLevel13](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/classes/KwgoS2CellLevel13.md) | None<br/>| 1069 | 





## Slots

| Slot | Description | Occurrences |
| --- | --- | --- |
| [coso_casNumber](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/coso_casNumber.md) | <br/>| 84 |
| [https___idir.uta.edu_sockg_ontology#badValueFlag](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#badValueFlag.md) | <br/>| 149774 |
| [https___idir.uta.edu_sockg_ontology#cites](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#cites.md) | <br/>| 177 |
| [https___idir.uta.edu_sockg_ontology#correspondingAuthor](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#correspondingAuthor.md) | <br/>| 136 |
| [https___idir.uta.edu_sockg_ontology#endDate](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#endDate.md) | <br/>| 3974 |
| [https___idir.uta.edu_sockg_ontology#fromProject](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#fromProject.md) | <br/>| 935 |
| [https___idir.uta.edu_sockg_ontology#fromUnit](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#fromUnit.md) | <br/>| 439350 |
| [https___idir.uta.edu_sockg_ontology#fundedBy](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#fundedBy.md) | <br/>| 54 |
| [https___idir.uta.edu_sockg_ontology#hasAmendmentType](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#hasAmendmentType.md) | <br/>| 25357 |
| [https___idir.uta.edu_sockg_ontology#hasAnimalClass](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#hasAnimalClass.md) | <br/>| 1833 |
| [https___idir.uta.edu_sockg_ontology#hasAnimalSpecies](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#hasAnimalSpecies.md) | <br/>| 1954 |
| [https___idir.uta.edu_sockg_ontology#hasBroadleafOrGrass](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#hasBroadleafOrGrass.md) | <br/>| 6996 |
| [https___idir.uta.edu_sockg_ontology#hasChamberPlacement](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#hasChamberPlacement.md) | <br/>| 127419 |
| [https___idir.uta.edu_sockg_ontology#hasCrop](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#hasCrop.md) | <br/>| 278818 |
| [https___idir.uta.edu_sockg_ontology#hasCultivar](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#hasCultivar.md) | <br/>| 20926 |
| [https___idir.uta.edu_sockg_ontology#hasGrazingRate](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#hasGrazingRate.md) | <br/>| 20 |
| [https___idir.uta.edu_sockg_ontology#hasGrowthStage](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#hasGrowthStage.md) | <br/>| 56789 |
| [https___idir.uta.edu_sockg_ontology#hasHarvestedFraction](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#hasHarvestedFraction.md) | <br/>| 18154 |
| [https___idir.uta.edu_sockg_ontology#hasLossesOrDeposition](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#hasLossesOrDeposition.md) | <br/>| 149 |
| [https___idir.uta.edu_sockg_ontology#hasMeasurement](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#hasMeasurement.md) | <br/>| 3180012 |
| [https___idir.uta.edu_sockg_ontology#hasOtherEvents](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#hasOtherEvents.md) | <br/>| 4 |
| [https___idir.uta.edu_sockg_ontology#hasPesticideActiveIngredient](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#hasPesticideActiveIngredient.md) | <br/>| 16104 |
| [https___idir.uta.edu_sockg_ontology#hasPesticideTarget](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#hasPesticideTarget.md) | <br/>| 12841 |
| [https___idir.uta.edu_sockg_ontology#hasPlantFraction](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#hasPlantFraction.md) | <br/>| 24130 |
| [https___idir.uta.edu_sockg_ontology#hasProjectScenario](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#hasProjectScenario.md) | <br/>| 826 |
| [https___idir.uta.edu_sockg_ontology#hasRotation](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#hasRotation.md) | <br/>| 761 |
| [https___idir.uta.edu_sockg_ontology#hasSpeciesMix](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#hasSpeciesMix.md) | <br/>| 6996 |
| [https___idir.uta.edu_sockg_ontology#hasStandardDeviation](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#hasStandardDeviation.md) | <br/>|  |
| [https___idir.uta.edu_sockg_ontology#hasSurfaceOrLeaching](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#hasSurfaceOrLeaching.md) | <br/>| 2986 |
| [https___idir.uta.edu_sockg_ontology#hasTillage](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#hasTillage.md) | <br/>| 711 |
| [https___idir.uta.edu_sockg_ontology#hasTillageEvent](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#hasTillageEvent.md) | <br/>| 27450 |
| [https___idir.uta.edu_sockg_ontology#hasTiming](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#hasTiming.md) | <br/>| 1034 |
| [https___idir.uta.edu_sockg_ontology#hasTreatment](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#hasTreatment.md) | <br/>| 769 |
| [https___idir.uta.edu_sockg_ontology#inferred](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#inferred.md) | <br/>| 3863 |
| [https___idir.uta.edu_sockg_ontology#irrigation](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#irrigation.md) | <br/>| 774 |
| [https___idir.uta.edu_sockg_ontology#isInterpolated](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#isInterpolated.md) | <br/>| 397571 |
| [https___idir.uta.edu_sockg_ontology#lowerDepth](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#lowerDepth.md) | <br/>| 100779 |
| [https___idir.uta.edu_sockg_ontology#of](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#of.md) | <br/>| 3180012 |
| [https___idir.uta.edu_sockg_ontology#organicManagement](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#organicManagement.md) | <br/>| 769 |
| [https___idir.uta.edu_sockg_ontology#startDate](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#startDate.md) | <br/>| 107758 |
| [https___idir.uta.edu_sockg_ontology#tileDrainage](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#tileDrainage.md) | <br/>| 438 |
| [https___idir.uta.edu_sockg_ontology#treatmentHasAmendment](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#treatmentHasAmendment.md) | <br/>| 47106 |
| [https___idir.uta.edu_sockg_ontology#treatmentHasGrazingManagement](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#treatmentHasGrazingManagement.md) | <br/>| 1951 |
| [https___idir.uta.edu_sockg_ontology#treatmentHasGrowthStageManagement](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#treatmentHasGrowthStageManagement.md) | <br/>| 5148 |
| [https___idir.uta.edu_sockg_ontology#treatmentHasPlantingManagement](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#treatmentHasPlantingManagement.md) | <br/>| 23728 |
| [https___idir.uta.edu_sockg_ontology#treatmentHasResidueManagement](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#treatmentHasResidueManagement.md) | <br/>| 3334 |
| [https___idir.uta.edu_sockg_ontology#treatmentHasTillageManagement](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#treatmentHasTillageManagement.md) | <br/>| 27450 |
| [https___idir.uta.edu_sockg_ontology#unitHasAmendment](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#unitHasAmendment.md) | <br/>| 47106 |
| [https___idir.uta.edu_sockg_ontology#unitHasGrazingManagement](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#unitHasGrazingManagement.md) | <br/>| 1951 |
| [https___idir.uta.edu_sockg_ontology#unitHasGrowthStageManagement](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#unitHasGrowthStageManagement.md) | <br/>| 5148 |
| [https___idir.uta.edu_sockg_ontology#unitHasPlantingManagement](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#unitHasPlantingManagement.md) | <br/>| 23728 |
| [https___idir.uta.edu_sockg_ontology#unitHasResidueManagement](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#unitHasResidueManagement.md) | <br/>| 3334 |
| [https___idir.uta.edu_sockg_ontology#unitHasTillageManagement](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#unitHasTillageManagement.md) | <br/>| 27449 |
| [https___idir.uta.edu_sockg_ontology#unitUrl](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#unitUrl.md) | <br/>| 23 |
| [https___idir.uta.edu_sockg_ontology#upperDepth](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#upperDepth.md) | <br/>| 100779 |
| [https___idir.uta.edu_sockg_ontology#usesCoverCrop](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#usesCoverCrop.md) | <br/>| 194 |
| [https___idir.uta.edu_sockg_ontology#usesEquipment](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#usesEquipment.md) | <br/>| 3070 |
| [https___idir.uta.edu_sockg_ontology#usesFertilizerAmendment](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#usesFertilizerAmendment.md) | <br/>| 653 |
| [https___idir.uta.edu_sockg_ontology#usesIrrigation](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#usesIrrigation.md) | <br/>| 6063 |
| [https___idir.uta.edu_sockg_ontology#usesModel](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#usesModel.md) | <br/>| 923 |
| [https___idir.uta.edu_sockg_ontology#usesPlantingMethod](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#usesPlantingMethod.md) | <br/>| 22592 |
| [https___idir.uta.edu_sockg_ontology#usesResidueRemoval](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#usesResidueRemoval.md) | <br/>| 769 |
| [https___idir.uta.edu_sockg_ontology#usesTillageMethod](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#usesTillageMethod.md) | <br/>| 24709 |
| [https___idir.uta.edu_sockg_ontology#usesTreatment](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#usesTreatment.md) | <br/>| 439350 |
| [https___idir.uta.edu_sockg_ontology#weatherAt](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#weatherAt.md) | <br/>| 149774 |
| [https___idir.uta.edu_sockg_ontology#withCuttingHeight](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#withCuttingHeight.md) | <br/>| 2954 |
| [https___idir.uta.edu_sockg_ontology#withPesticidePlacement](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#withPesticidePlacement.md) | <br/>| 9498 |
| [https___idir.uta.edu_sockg_ontology#withPlacement](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#withPlacement.md) | <br/>| 24794 |
| [https___idir.uta.edu_sockg_ontology#withStartStopInterval](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/https___idir.uta.edu_sockg_ontology#withStartStopInterval.md) | <br/>| 1722 |
| [sdos_isPrimaryContact](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sdos_isPrimaryContact.md) | <br/>| 140 |
| [sdos_role](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/sdos_role.md) | <br/>| 151 |
| [spatial_connectedTo](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/spatial_connectedTo.md) | <br/>| 2322 |
| [spatial_spatiallyRelatedTo](https://github.com/frink-okn/graph-descriptions/blob/main/soc-kg/slots/spatial_spatiallyRelatedTo.md) | <br/>|  |









## IRI prefixes

* bibo: http://purl.org/ontology/bibo/
* coso: http://w3id.org/coso/v1/contaminoso#
* dcgeoid: https://datacommons.org/browser/geoId/
* dct: http://purl.org/dc/terms/
* geo: http://www.opengis.net/ont/geosparql#
* kwgo: http://stko-kwg.geog.ucsb.edu/lod/ontology/
* kwgr: http://stko-kwg.geog.ucsb.edu/lod/resource/
* linkml: https://w3id.org/linkml/
* okn: https://purl.org/okn/
* okns: https://purl.org/okn/schema/
* owl: http://www.w3.org/2002/07/owl#
* qudt: http://qudt.org/schema/qudt/
* rdfs: http://www.w3.org/2000/01/rdf-schema#
* sdos: https://schema.org/
* spatial: http://purl.org/spatialai/spatial/spatial-full#
* xsd: http://www.w3.org/2001/XMLSchema#
