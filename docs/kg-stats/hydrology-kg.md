# hydrologykg

This ontology supports querying the SAWGraph Knowledge Graph and the KnowWhereGraph. It is an adaptation of the spatial ontology originally published by the KnowWhereGraph Project



## Schema Diagram

```mermaid
erDiagram
DcamVocabularyEncodingScheme {
    uri rdfs_seeAlso  
    string rdfs_label  
    string rdfs_comment  
    date dct_issued  
    uri rdfs_isDefinedBy  
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
QudtAbstractQuantityKind {

}
QudtAngleUnit {

}
QudtAspect {

}
QudtAspectClass {
    string rdfs_label  
    uri rdfs_isDefinedBy  
    string rdfs_comment  
}
QudtBaseDimensionMagnitude {

}
QudtBinaryPrefix {

}
QudtBitEncodingType {
    integer qudt_bits  
    uri rdfs_isDefinedBy  
    string rdfs_label  
}
QudtBooleanEncodingType {
    integer qudt_bits  
    uri rdfs_isDefinedBy  
    string rdfs_label  
    integer qudt_bytes  
}
QudtByteEncodingType {
    integer qudt_bytes  
    uri rdfs_isDefinedBy  
    string rdfs_label  
}
QudtCardinalityType {
    string dct_description  
    uri rdfs_isDefinedBy  
    string rdfs_label  
    string dtype_literal  
    uri qudt_informativeReference  
}
QudtCharEncodingType {
    string rdfs_label  
    integer qudt_bytes  
    uri rdfs_isDefinedBy  
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

}
QudtCountingUnit {

}
QudtCurrencyUnit {

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
    uri rdfs_isDefinedBy  
}
QudtDecimalPrefix {

}
QudtDerivedUnit {

}
QudtDimensionlessUnit {

}
QudtDiscipline {

}
QudtEncoding {

}
QudtEndianType {
    string rdfs_label  
    string dtype_literal  
    uri rdfs_isDefinedBy  
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
    uri rdfs_isDefinedBy  
    string rdfs_label  
}
QudtIntegerEncodingType {
    integer qudt_bytes  
    uri rdfs_isDefinedBy  
    string rdfs_label  
}
QudtIntervalScale {

}
QudtLogarithmicUnit {

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
    uri rdfs_isDefinedBy  
}
QudtOrdinalScale {

}
QudtOrganization {

}
QudtPhysicalConstant {

}
QudtPlaneAngleUnit {

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
    uri rdfs_isDefinedBy  
}
QudtSolidAngleUnit {

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

}
QudtUserQuantityKind {

}
QudtVerifiable {

}
XsdString {

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
    uri rdfs_isDefinedBy  
    uri rdfs_seeAlso  
    string rdfs_comment  
    string rdfs_label  
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
    uri rdfs_isDefinedBy  
    string rdfs_comment  
    string rdfs_label  
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
    uri rdfs_isDefinedBy  
    string rdfs_comment  
    string rdfs_label  
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
    uri rdfs_isDefinedBy  
    uri rdfs_seeAlso  
    string rdfs_comment  
    string rdfs_label  
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
    decimal time_months  
    decimal time_seconds  
    decimal time_hours  
    decimal time_weeks  
    decimal time_minutes  
    decimal time_days  
    decimal time_years  
    string rdfs_label  
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
    string rdfs_label  
    string rdfs_comment  
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
    string rdfs_label  
    uri sdos_isPartOf  
    uri sdos_source  
    string rdfs_comment  
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
    string rdfs_label  
    string rdfs_comment  
}
SdosBoatReservation {

}
SdosBoatTerminal {

}
SdosBoatTrip {

}
SdosBodyMeasurementTypeEnumeration {
    string rdfs_label  
    uri sdos_isPartOf  
    uri sdos_source  
    string rdfs_comment  
}
SdosBodyOfWater {

}
SdosBone {

}
SdosBook {

}
SdosBookFormatType {
    string rdfs_label  
    uri sdos_isPartOf  
    string rdfs_comment  
}
SdosBookSeries {

}
SdosBookStore {

}
SdosBookmarkAction {

}
SdosBoolean {
    string rdfs_label  
    string rdfs_comment  
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
    string rdfs_label  
    uri sdos_contributor  
    uri sdos_isPartOf  
    string rdfs_comment  
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
    string rdfs_label  
    uri sdos_isPartOf  
    uri sdos_source  
    string rdfs_comment  
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
    string rdfs_label  
    string rdfs_comment  
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
    string rdfs_label  
    uri sdos_sameAs  
    uri sdos_contributor  
    string rdfs_comment  
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
    string rdfs_label  
    uri sdos_contributor  
    string rdfs_comment  
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
    string rdfs_label  
    string rdfs_comment  
}
SdosDigitalPlatformEnumeration {
    string rdfs_label  
    uri sdos_isPartOf  
    uri sdos_source  
    string rdfs_comment  
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
    string rdfs_label  
    uri sdos_contributor  
    string rdfs_comment  
}
SdosDrug {

}
SdosDrugClass {

}
SdosDrugCost {

}
SdosDrugCostCategory {
    string rdfs_label  
    uri sdos_isPartOf  
    string rdfs_comment  
}
SdosDrugLegalStatus {

}
SdosDrugPregnancyCategory {
    string rdfs_label  
    uri sdos_isPartOf  
    string rdfs_comment  
}
SdosDrugPrescriptionStatus {
    string rdfs_label  
    uri sdos_isPartOf  
    string rdfs_comment  
}
SdosDrugStrength {

}
SdosDryCleaningOrLaundry {

}
SdosDuration {

}
SdosEUEnergyEfficiencyEnumeration {
    string rdfs_label  
    uri sdos_isPartOf  
    uri sdos_source  
    string rdfs_comment  
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
    string rdfs_label  
    uri sdos_isPartOf  
    uri sdos_source  
    string rdfs_comment  
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
    string rdfs_label  
    uri sdos_isPartOf  
    uri sdos_source  
    string rdfs_comment  
}
SdosEventReservation {

}
SdosEventSeries {

}
SdosEventStatusType {
    string rdfs_label  
    string rdfs_comment  
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
    string rdfs_label  
    uri sdos_isPartOf  
    uri sdos_source  
    string rdfs_comment  
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
    string rdfs_label  
    uri sdos_isPartOf  
    uri sdos_source  
    string rdfs_comment  
}
SdosGamePlayMode {
    string rdfs_label  
    string rdfs_comment  
}
SdosGameServer {

}
SdosGameServerStatus {
    string rdfs_label  
    string rdfs_comment  
}
SdosGardenStore {

}
SdosGasStation {

}
SdosGatedResidenceCommunity {

}
SdosGenderType {
    string rdfs_label  
    string rdfs_comment  
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
    string rdfs_label  
    uri sdos_isPartOf  
    uri sdos_source  
    string rdfs_comment  
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
    string rdfs_label  
    uri sdos_isPartOf  
    uri sdos_source  
    string rdfs_comment  
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
    uri sdos_isPartOf  
    string rdfs_comment  
    uri sdos_source  
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
    string rdfs_label  
    uri sdos_isPartOf  
    uri sdos_source  
    string rdfs_comment  
}
SdosIncentiveStatus {
    string rdfs_label  
    uri sdos_isPartOf  
    uri sdos_source  
    string rdfs_comment  
}
SdosIncentiveType {
    string rdfs_label  
    uri sdos_isPartOf  
    uri sdos_source  
    string rdfs_comment  
}
SdosIndividualPhysician {

}
SdosIndividualProduct {

}
SdosInfectiousAgentClass {
    string rdfs_label  
    uri sdos_isPartOf  
    string rdfs_comment  
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
    string rdfs_label  
    string rdfs_comment  
}
SdosItemList {

}
SdosItemListOrderType {
    string rdfs_label  
    string rdfs_comment  
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
    uri sdos_isPartOf  
    string rdfs_comment  
    uri sdos_contributor  
    uri sdos_source  
}
SdosLegalService {

}
SdosLegalValueLevel {
    string rdfs_label  
    uri sdos_isPartOf  
    string rdfs_comment  
    uri sdos_contributor  
    uri sdos_source  
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
    string rdfs_label  
    string rdfs_comment  
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
    string rdfs_label  
    uri sdos_isPartOf  
    uri sdos_source  
    string rdfs_comment  
}
SdosMeasurementTypeEnumeration {

}
SdosMediaEnumeration {

}
SdosMediaGallery {

}
SdosMediaManipulationRatingEnumeration {
    string rdfs_label  
    uri sdos_isPartOf  
    uri sdos_source  
    string rdfs_comment  
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
    string rdfs_label  
    uri sdos_isPartOf  
    string rdfs_comment  
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
    string rdfs_label  
    uri sdos_isPartOf  
    string rdfs_comment  
}
SdosMedicalEntity {

}
SdosMedicalEnumeration {

}
SdosMedicalEvidenceLevel {
    string rdfs_label  
    uri sdos_isPartOf  
    string rdfs_comment  
}
SdosMedicalGuideline {

}
SdosMedicalGuidelineContraindication {

}
SdosMedicalGuidelineRecommendation {

}
SdosMedicalImagingTechnique {
    string rdfs_label  
    uri sdos_isPartOf  
    string rdfs_comment  
}
SdosMedicalIndication {

}
SdosMedicalIntangible {

}
SdosMedicalObservationalStudy {

}
SdosMedicalObservationalStudyDesign {
    string rdfs_label  
    uri sdos_isPartOf  
    string rdfs_comment  
}
SdosMedicalOrganization {

}
SdosMedicalProcedure {

}
SdosMedicalProcedureType {
    string rdfs_label  
    uri sdos_isPartOf  
    string rdfs_comment  
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
    string rdfs_label  
    uri sdos_isPartOf  
    string rdfs_comment  
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
    string rdfs_label  
    uri sdos_isPartOf  
    string rdfs_comment  
}
SdosMedicalWebPage {

}
SdosMedicineSystem {
    string rdfs_label  
    uri sdos_isPartOf  
    string rdfs_comment  
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
    string rdfs_label  
    uri sdos_isPartOf  
    uri sdos_source  
    string rdfs_comment  
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
    string rdfs_label  
    uri sdos_contributor  
    string rdfs_comment  
}
SdosMusicAlbumReleaseType {
    string rdfs_label  
    uri sdos_contributor  
    string rdfs_comment  
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
    string rdfs_label  
    uri sdos_contributor  
    string rdfs_comment  
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
    string rdfs_label  
    uri sdos_isPartOf  
    uri sdos_source  
    string rdfs_comment  
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
    string rdfs_label  
    string rdfs_comment  
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
    string rdfs_label  
    string rdfs_comment  
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
    string rdfs_label  
    string rdfs_comment  
}
SdosPaymentService {

}
SdosPaymentStatusType {
    string rdfs_label  
    string rdfs_comment  
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
    string rdfs_label  
    uri sdos_isPartOf  
    string rdfs_comment  
}
SdosPhysicalExam {
    string rdfs_label  
    uri sdos_isPartOf  
    string rdfs_comment  
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
    string rdfs_label  
    uri sdos_isPartOf  
    uri sdos_source  
    string rdfs_comment  
}
SdosPriceSpecification {

}
SdosPriceTypeEnumeration {
    string rdfs_label  
    uri sdos_isPartOf  
    uri sdos_source  
    string rdfs_comment  
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
    uri sdos_isPartOf  
    string rdfs_comment  
    uri sdos_source  
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
    string rdfs_label  
    uri sdos_isPartOf  
    uri sdos_source  
    string rdfs_comment  
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
    string rdfs_label  
    uri sdos_isPartOf  
    uri sdos_source  
    string rdfs_comment  
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
    string rdfs_label  
    string rdfs_comment  
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
    string rdfs_label  
    string rdfs_comment  
}
SdosResumeAction {

}
SdosReturnAction {

}
SdosReturnFeesEnumeration {
    string rdfs_label  
    uri sdos_isPartOf  
    uri sdos_source  
    string rdfs_comment  
}
SdosReturnLabelSourceEnumeration {
    string rdfs_label  
    uri sdos_isPartOf  
    uri sdos_source  
    string rdfs_comment  
}
SdosReturnMethodEnumeration {
    string rdfs_label  
    uri sdos_isPartOf  
    uri sdos_source  
    string rdfs_comment  
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
    string rdfs_label  
    string rdfs_comment  
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
    string rdfs_label  
    uri sdos_isPartOf  
    uri sdos_source  
    string rdfs_comment  
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
    string rdfs_label  
    uri sdos_contributor  
    string rdfs_comment  
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
    string rdfs_label  
    uri sdos_isPartOf  
    uri sdos_source  
    string rdfs_comment  
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
    string rdfs_label  
    uri sdos_isPartOf  
    uri sdos_source  
    string rdfs_comment  
}
SdosURL {

}
SdosUSNonprofitType {
    string rdfs_label  
    uri sdos_isPartOf  
    uri sdos_source  
    string rdfs_comment  
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
    string rdfs_label  
    uri sdos_isPartOf  
    uri sdos_source  
    string rdfs_comment  
}
SdosWearableSizeGroupEnumeration {
    string rdfs_label  
    uri sdos_isPartOf  
    uri sdos_source  
    string rdfs_comment  
}
SdosWearableSizeSystemEnumeration {
    string rdfs_label  
    uri sdos_isPartOf  
    uri sdos_source  
    string rdfs_comment  
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
    date dct_modified  
    string vaem_withAttributionTo  
    uri vaem_turtleFileURL  
    string vaem_name  
    string vaem_intent  
    string dct_title  
    string vaem_description  
    string rdfs_label  
    uri vaem_previousPublishedVersion  
    uri vaem_rdfxmlFileURL  
    string vaem_revision  
    uri vaem_latestPublishedVersion  
    uri vaem_usesNonImportedResource  
    uri vaem_logo  
    uri rdfs_isDefinedBy  
    string vaem_title  
    string vaem_namespacePrefix  
    string vaem_owner  
}
VaemGraphRole {
    string vaem_filePrefix  
    string dct_description  
    string rdfs_label  
    uri rdfs_isDefinedBy  
}
VaemParty {
    string vaem_name  
    string rdfs_label  
    uri vaem_url  
    uri rdfs_isDefinedBy  
}
VaemViewpoint {

}
VaemCatalogEntry {
    string rdfs_label  
    uri rdfs_isDefinedBy  
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
    uri voag_url  
    string voag_pointOfContact  
    uri rdfs_isDefinedBy  
    string vaem_name  
}
VoagAttributionLogo {
    string rdfs_label  
    string voag_height  
    string voag_width  
    uri rdfs_isDefinedBy  
    string vaem_description  
    uri voag_image  
    string voag_caption  
}
VoagCatalog {

}
VoagChangeFrequency {
    string rdfs_label  
    uri rdfs_isDefinedBy  
}
VoagChangeManagementProcess {

}
VoagChangeType {
    string rdfs_label  
    uri rdfs_isDefinedBy  
}
VoagConcurrenceEvent {

}
VoagConfidentialityLevel {
    string rdfs_label  
    integer dtype_order  
    uri rdfs_isDefinedBy  
    string vaem_description  
}
VoagCreativeCommonsJurisdiction {

}
VoagCreativeCommonsPermission {
    string rdfs_label  
    uri rdfs_isDefinedBy  
    string vaem_description  
}
VoagCreativeCommonsProhibition {
    string rdfs_label  
    uri rdfs_isDefinedBy  
    string vaem_description  
}
VoagCreativeCommonsRequirement {
    string rdfs_label  
    uri rdfs_isDefinedBy  
    string vaem_description  
    uri vaem_url  
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
    uri rdfs_isDefinedBy  
}
VoagGovernanceEvent {

}
VoagGovernanceProcess {

}
VoagGovernanceProtocol {

}
VoagGovernanceRole {
    string rdfs_label  
    uri rdfs_isDefinedBy  
}
VoagGovernedObject {

}
VoagGovernedService {

}
VoagGraph {

}
VoagIcon {
    string rdfs_label  
    string voag_height  
    string voag_width  
    uri rdfs_isDefinedBy  
    string vaem_description  
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
    string rdfs_label  
    uri rdfs_isDefinedBy  
    string vaem_description  
}
VoagLicenseModel {
    string rdfs_label  
    uri rdfs_isDefinedBy  
}
VoagLogo {
    string rdfs_label  
    string voag_height  
    string voag_width  
    uri rdfs_isDefinedBy  
    string vaem_description  
    uri voag_image  
    string voag_caption  
}
VoagMaturity {
    string rdfs_label  
    uri rdfs_isDefinedBy  
}
VoagNonConcurrenceEvent {

}
VoagOrganization {

}
VoagOrganizationLogo {
    string rdfs_label  
    string voag_height  
    string voag_width  
    uri rdfs_isDefinedBy  
    string vaem_description  
    uri voag_image  
    string voag_caption  
}
VoagParty {

}
VoagPedigree {
    string rdfs_label  
    uri rdfs_isDefinedBy  
}
VoagPerson {

}
VoagPriorityValue {
    string rdfs_label  
    uri rdfs_isDefinedBy  
}
VoagProcess {

}
VoagProductLogo {
    string rdfs_label  
    string voag_height  
    string voag_width  
    uri rdfs_isDefinedBy  
    uri voag_image  
    string voag_caption  
    string vaem_description  
}
VoagProvenance {
    string rdfs_label  
    uri rdfs_isDefinedBy  
}
VoagPublicationStatus {
    string rdfs_label  
    uri rdfs_isDefinedBy  
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
    uri rdfs_isDefinedBy  
}
VoagService {

}
VoagStakeholderGroup {

}
VoagStandard {

}
VoagVocabGraph {

}
Gnis-ld-usgsAirport {

}
Gnis-ld-usgsArch {

}
Gnis-ld-usgsArea {

}
Gnis-ld-usgsArroyo {

}
Gnis-ld-usgsBar {

}
Gnis-ld-usgsBasin {

}
Gnis-ld-usgsBay {

}
Gnis-ld-usgsBeach {

}
Gnis-ld-usgsBench {

}
Gnis-ld-usgsBend {

}
Gnis-ld-usgsBridge {

}
Gnis-ld-usgsBuilding {

}
Gnis-ld-usgsBuiltUpArea {

}
Gnis-ld-usgsCanal {

}
Gnis-ld-usgsCape {

}
Gnis-ld-usgsCemetery {

}
Gnis-ld-usgsCensus {

}
Gnis-ld-usgsChannel {

}
Gnis-ld-usgsChurch {

}
Gnis-ld-usgsCivilGovernment {

}
Gnis-ld-usgsCliff {

}
Gnis-ld-usgsCrater {

}
Gnis-ld-usgsCrossing {

}
Gnis-ld-usgsDam {

}
Gnis-ld-usgsDivision {

}
Gnis-ld-usgsEcologicalRegime {

}
Gnis-ld-usgsEmbankment {

}
Gnis-ld-usgsFlat {

}
Gnis-ld-usgsForest {

}
Gnis-ld-usgsGap {

}
Gnis-ld-usgsGlacier {

}
Gnis-ld-usgsGut {

}
Gnis-ld-usgsHarbor {

}
Gnis-ld-usgsHospital {

}
Gnis-ld-usgsIsland {

}
Gnis-ld-usgsIsthmus {

}
Gnis-ld-usgsLake {

}
Gnis-ld-usgsLava {

}
Gnis-ld-usgsLevee {

}
Gnis-ld-usgsLocale {

}
Gnis-ld-usgsMilitary {

}
Gnis-ld-usgsMine {

}
Gnis-ld-usgsMountainRange {

}
Gnis-ld-usgsOcean {

}
Gnis-ld-usgsOilField {

}
Gnis-ld-usgsPark {

}
Gnis-ld-usgsPlain {

}
Gnis-ld-usgsPopulatedPlace {

}
Gnis-ld-usgsPostOffice {

}
Gnis-ld-usgsRapids {

}
Gnis-ld-usgsReserve {

}
Gnis-ld-usgsReservoir {

}
Gnis-ld-usgsRidge {

}
Gnis-ld-usgsRock {

}
Gnis-ld-usgsSchool {

}
Gnis-ld-usgsSea {

}
Gnis-ld-usgsSlope {

}
Gnis-ld-usgsSpring {

}
Gnis-ld-usgsStream {

}
Gnis-ld-usgsSummit {

}
Gnis-ld-usgsSurfaceWater {

}
Gnis-ld-usgsSwamp {

}
Gnis-ld-usgsTerrain {

}
Gnis-ld-usgsTower {

}
Gnis-ld-usgsTrail {

}
Gnis-ld-usgsTunnel {

}
Gnis-ld-usgsUnknown {

}
Gnis-ld-usgsValley {

}
Gnis-ld-usgsWaterfall {

}
Gnis-ld-usgsWell {

}
Gnis-ld-usgsWoodland {

}
Gnis-ld-gnisCounty {

}
Gnis-ld-gnisState {

}
Gnis-ld-usgsFeature {

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
    uri rdfs_isDefinedBy  
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
    string rdfs_label  
    string rdfs_comment  
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
    string rdfs_label  
    string rdfs_comment  
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
    string rdfs_label  
    string rdfs_comment  
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
Sf#LineString {

}
Sf#Point {

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
B4321a9eb518ec74b0f636677676d03cc {

}
Bf03ad86fab1719a427cbb412f91529fa {

}
HttpGwml2.orgDefGwml2#GWAquifer {
    string http___sawgraph.spatialai.org_v1_il_isgs#ilSawAqId  
    string http___sawgraph.spatialai.org_v1_saw_water#aquiferType  
    string rdfs_label  
    string http___sawgraph.spatialai.org_v1_me_mgs#meMgsAqId  
}
HttpGwml2.orgDefGwml2#GWAquiferSystem {
    string http___sawgraph.spatialai.org_v1_il_isgs#ilSawAqSysId  
    string rdfs_label  
    string rdfs_comment  
    string http___sawgraph.spatialai.org_v1_me_mgs#meSawAqSysId  
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
HyfHYCanal {
    string http___nhdplusv2.spatialai.org_v1_nhdplusv2#hasCOMID  
    string http___nhdplusv2.spatialai.org_v1_nhdplusv2#hasReachCode  
    string rdfs_label  
    string http___nhdplusv2.spatialai.org_v1_nhdplusv2#hasFTYPE  
    string http___nhdplusv2.spatialai.org_v1_nhdplusv2#hasFCODE  
    string dct_title  
}
HyfHYCatchment {

}
HyfHYCatchmentRealization {

}
HyfHYElementaryFlowPath {
    string http___nhdplusv2.spatialai.org_v1_nhdplusv2#hasCOMID  
    string http___nhdplusv2.spatialai.org_v1_nhdplusv2#hasReachCode  
    string rdfs_label  
    string dct_title  
    string http___nhdplusv2.spatialai.org_v1_nhdplusv2#hasFTYPE  
    string http___nhdplusv2.spatialai.org_v1_nhdplusv2#hasFCODE  
}
HyfHYEstuary {
    string http___nhdplusv2.spatialai.org_v1_nhdplusv2#hasCOMID  
    string http___nhdplusv2.spatialai.org_v1_nhdplusv2#hasReachCode  
    string rdfs_label  
    string http___nhdplusv2.spatialai.org_v1_nhdplusv2#hasFTYPE  
    string http___nhdplusv2.spatialai.org_v1_nhdplusv2#hasFCODE  
    string dct_title  
}
HyfHYFlowPath {

}
HyfHYHydroFeature {

}
HyfHYImpoundment {
    string http___nhdplusv2.spatialai.org_v1_nhdplusv2#hasCOMID  
    string http___nhdplusv2.spatialai.org_v1_nhdplusv2#hasReachCode  
    string rdfs_label  
    string http___nhdplusv2.spatialai.org_v1_nhdplusv2#hasFTYPE  
    string http___nhdplusv2.spatialai.org_v1_nhdplusv2#hasFCODE  
    string dct_title  
}
HyfHYLagoon {
    string http___nhdplusv2.spatialai.org_v1_nhdplusv2#hasCOMID  
    string http___nhdplusv2.spatialai.org_v1_nhdplusv2#hasReachCode  
    string rdfs_label  
    string http___nhdplusv2.spatialai.org_v1_nhdplusv2#hasFTYPE  
    string http___nhdplusv2.spatialai.org_v1_nhdplusv2#hasFCODE  
    string dct_title  
}
HyfHYLake {
    string http___nhdplusv2.spatialai.org_v1_nhdplusv2#hasCOMID  
    string http___nhdplusv2.spatialai.org_v1_nhdplusv2#hasReachCode  
    string rdfs_label  
    string http___nhdplusv2.spatialai.org_v1_nhdplusv2#hasFTYPE  
    string http___nhdplusv2.spatialai.org_v1_nhdplusv2#hasFCODE  
    string dct_title  
}
HyfHYMainStem {

}
HyfHYRiver {
    string http___nhdplusv2.spatialai.org_v1_nhdplusv2#hasCOMID  
    string http___nhdplusv2.spatialai.org_v1_nhdplusv2#hasReachCode  
    string rdfs_label  
    string http___nhdplusv2.spatialai.org_v1_nhdplusv2#hasFTYPE  
    string http___nhdplusv2.spatialai.org_v1_nhdplusv2#hasFCODE  
    string dct_title  
}
HyfHYWaterBody {
    string http___nhdplusv2.spatialai.org_v1_nhdplusv2#hasCOMID  
    string http___nhdplusv2.spatialai.org_v1_nhdplusv2#hasReachCode  
    string rdfs_label  
    string http___nhdplusv2.spatialai.org_v1_nhdplusv2#hasFTYPE  
    string http___nhdplusv2.spatialai.org_v1_nhdplusv2#hasFCODE  
    string dct_title  
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
OwlRational {

}
OwlReal {

}
Sf#MultiPolygon {
    geo_wktLiteral geo_asWKT  
}
Sf#Polygon {
    geo_wktLiteral geo_asWKT  
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
    string us_sdwis_hasActivity  
    string rdfs_label  
    date us_sdwis_firstReport  
    date us_sdwis_deactivationDate  
    string us_sdwis_pwsName  
    int32 us_sdwis_serviceConnections  
    int32 us_sdwis_populationServed  
    string us_sdwis_hasOwnership  
}
UsSdwisPublicWaterSystem-GW {
    date us_sdwis_lastReport  
    string us_sdwis_hasActivity  
    string rdfs_label  
    date us_sdwis_firstReport  
    int32 us_sdwis_serviceConnections  
    string us_sdwis_pwsName  
    date us_sdwis_deactivationDate  
    int32 us_sdwis_populationServed  
    string us_sdwis_hasOwnership  
}
UsSdwisPublicWaterSystem-NCWS {

}
UsSdwisPublicWaterSystem-NTNCWS {
    date us_sdwis_lastReport  
    string us_sdwis_hasActivity  
    string rdfs_label  
    date us_sdwis_firstReport  
    int32 us_sdwis_serviceConnections  
    string us_sdwis_pwsName  
    date us_sdwis_deactivationDate  
    int32 us_sdwis_populationServed  
    string us_sdwis_hasOwnership  
}
UsSdwisPublicWaterSystem-SW {
    date us_sdwis_lastReport  
    string us_sdwis_hasActivity  
    string rdfs_label  
    date us_sdwis_firstReport  
    date us_sdwis_deactivationDate  
    string us_sdwis_pwsName  
    int32 us_sdwis_serviceConnections  
    int32 us_sdwis_populationServed  
    string us_sdwis_hasOwnership  
}
UsSdwisPublicWaterSystem-TNCWS {
    date us_sdwis_lastReport  
    string us_sdwis_hasActivity  
    string rdfs_label  
    date us_sdwis_firstReport  
    date us_sdwis_deactivationDate  
    string us_sdwis_pwsName  
    int32 us_sdwis_serviceConnections  
    int32 us_sdwis_populationServed  
    string us_sdwis_hasOwnership  
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

DcamVocabularyEncodingScheme ||--|o RdfsResource : "rdfs_seeAlso"
DcamVocabularyEncodingScheme ||--|o RdfsLiteral : "rdfs_label"
DcamVocabularyEncodingScheme ||--|o RdfsLiteral : "rdfs_comment"
DcamVocabularyEncodingScheme ||--|o RdfsLiteral : "dct_issued"
DcamVocabularyEncodingScheme ||--|o OwlOntology : "rdfs_isDefinedBy"
DcamVocabularyEncodingScheme ||--|o RdfsResource : "rdfs_isDefinedBy"
QudtAspectClass ||--|o RdfsLiteral : "rdfs_label"
QudtAspectClass ||--|o RdfsClass : "rdfs_subClassOf"
QudtAspectClass ||--|o OwlOntology : "rdfs_isDefinedBy"
QudtAspectClass ||--|o RdfsResource : "rdfs_isDefinedBy"
QudtAspectClass ||--|o RdfsLiteral : "rdfs_comment"
QudtBitEncodingType ||--|o OwlOntology : "rdfs_isDefinedBy"
QudtBitEncodingType ||--|o RdfsResource : "rdfs_isDefinedBy"
QudtBitEncodingType ||--|o RdfsLiteral : "rdfs_label"
QudtBooleanEncodingType ||--|o OwlOntology : "rdfs_isDefinedBy"
QudtBooleanEncodingType ||--|o RdfsResource : "rdfs_isDefinedBy"
QudtBooleanEncodingType ||--|o RdfsLiteral : "rdfs_label"
QudtByteEncodingType ||--|o OwlOntology : "rdfs_isDefinedBy"
QudtByteEncodingType ||--|o RdfsResource : "rdfs_isDefinedBy"
QudtByteEncodingType ||--|o RdfsLiteral : "rdfs_label"
QudtCardinalityType ||--|o OwlOntology : "rdfs_isDefinedBy"
QudtCardinalityType ||--|o RdfsResource : "rdfs_isDefinedBy"
QudtCardinalityType ||--|o RdfsLiteral : "rdfs_label"
QudtCharEncodingType ||--|o RdfsLiteral : "rdfs_label"
QudtCharEncodingType ||--|o OwlOntology : "rdfs_isDefinedBy"
QudtCharEncodingType ||--|o RdfsResource : "rdfs_isDefinedBy"
QudtDateTimeStringEncodingType ||--|o RdfsLiteral : "rdfs_label"
QudtDateTimeStringEncodingType ||--|o OwlOntology : "rdfs_isDefinedBy"
QudtDateTimeStringEncodingType ||--|o RdfsResource : "rdfs_isDefinedBy"
QudtEndianType ||--|o RdfsLiteral : "rdfs_label"
QudtEndianType ||--|o OwlOntology : "rdfs_isDefinedBy"
QudtEndianType ||--|o RdfsResource : "rdfs_isDefinedBy"
QudtFloatingPointEncodingType ||--|o OwlOntology : "rdfs_isDefinedBy"
QudtFloatingPointEncodingType ||--|o RdfsResource : "rdfs_isDefinedBy"
QudtFloatingPointEncodingType ||--|o RdfsLiteral : "rdfs_label"
QudtIntegerEncodingType ||--|o OwlOntology : "rdfs_isDefinedBy"
QudtIntegerEncodingType ||--|o RdfsResource : "rdfs_isDefinedBy"
QudtIntegerEncodingType ||--|o RdfsLiteral : "rdfs_label"
QudtOrderedType ||--|o RdfsLiteral : "rdfs_label"
QudtOrderedType ||--|o OwlOntology : "rdfs_isDefinedBy"
QudtOrderedType ||--|o RdfsResource : "rdfs_isDefinedBy"
QudtSignednessType ||--|o RdfsLiteral : "rdfs_label"
QudtSignednessType ||--|o OwlOntology : "rdfs_isDefinedBy"
QudtSignednessType ||--|o RdfsResource : "rdfs_isDefinedBy"
OwlDataRange ||--|o OwlOntology : "rdfs_isDefinedBy"
OwlDataRange ||--|o RdfsResource : "rdfs_isDefinedBy"
OwlDataRange ||--|o RdfsResource : "rdfs_seeAlso"
OwlDataRange ||--|o RdfsLiteral : "rdfs_comment"
OwlDataRange ||--|o RdfsLiteral : "rdfs_label"
OwlDataRange ||--|o RdfsClass : "rdfs_subClassOf"
OwlOntologyProperty ||--|o RdfsClass : "rdfs_range"
OwlOntologyProperty ||--|o OwlOntology : "rdfs_isDefinedBy"
OwlOntologyProperty ||--|o RdfsResource : "rdfs_isDefinedBy"
OwlOntologyProperty ||--|o RdfsLiteral : "rdfs_comment"
OwlOntologyProperty ||--|o RdfsLiteral : "rdfs_label"
OwlOntologyProperty ||--|o RdfsClass : "rdfs_domain"
RdfList ||--|o OwlOntology : "rdfs_isDefinedBy"
RdfList ||--|o RdfsResource : "rdfs_isDefinedBy"
RdfList ||--|o RdfsLiteral : "rdfs_comment"
RdfList ||--|o RdfsLiteral : "rdfs_label"
RdfsDatatype ||--|o OwlOntology : "rdfs_isDefinedBy"
RdfsDatatype ||--|o RdfsResource : "rdfs_isDefinedBy"
RdfsDatatype ||--|o RdfsResource : "rdfs_seeAlso"
RdfsDatatype ||--|o RdfsLiteral : "rdfs_comment"
RdfsDatatype ||--|o RdfsLiteral : "rdfs_label"
RdfsDatatype ||--|o RdfsClass : "rdfs_subClassOf"
TimeDayOfWeek ||--|o RdfsLiteral : "rdfs_label"
TimeTemporalUnit ||--|o RdfsLiteral : "rdfs_label"
SdosActionStatusType ||--|o RdfsLiteral : "rdfs_label"
SdosActionStatusType ||--|o RdfsLiteral : "rdfs_comment"
SdosAdultOrientedEnumeration ||--|o RdfsLiteral : "rdfs_label"
SdosAdultOrientedEnumeration ||--|o SdosURL : "sdos_isPartOf"
SdosAdultOrientedEnumeration ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosAdultOrientedEnumeration ||--|o RdfsLiteral : "rdfs_comment"
SdosBoardingPolicyType ||--|o RdfsLiteral : "rdfs_label"
SdosBoardingPolicyType ||--|o RdfsLiteral : "rdfs_comment"
SdosBodyMeasurementTypeEnumeration ||--|o RdfsLiteral : "rdfs_label"
SdosBodyMeasurementTypeEnumeration ||--|o SdosURL : "sdos_isPartOf"
SdosBodyMeasurementTypeEnumeration ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosBodyMeasurementTypeEnumeration ||--|o RdfsLiteral : "rdfs_comment"
SdosBookFormatType ||--|o RdfsLiteral : "rdfs_label"
SdosBookFormatType ||--|o SdosURL : "sdos_isPartOf"
SdosBookFormatType ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosBookFormatType ||--|o RdfsLiteral : "rdfs_comment"
SdosBoolean ||--|o RdfsLiteral : "rdfs_label"
SdosBoolean ||--|o RdfsLiteral : "rdfs_comment"
SdosCarUsageType ||--|o RdfsLiteral : "rdfs_label"
SdosCarUsageType ||--|o SdosOrganization : "sdos_contributor"
SdosCarUsageType ||--|o SdosPerson : "sdos_contributor"
SdosCarUsageType ||--|o SdosURL : "sdos_isPartOf"
SdosCarUsageType ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosCarUsageType ||--|o RdfsLiteral : "rdfs_comment"
SdosCertificationStatusEnumeration ||--|o RdfsLiteral : "rdfs_label"
SdosCertificationStatusEnumeration ||--|o SdosURL : "sdos_isPartOf"
SdosCertificationStatusEnumeration ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosCertificationStatusEnumeration ||--|o RdfsLiteral : "rdfs_comment"
SdosContactPointOption ||--|o RdfsLiteral : "rdfs_label"
SdosContactPointOption ||--|o RdfsLiteral : "rdfs_comment"
SdosDayOfWeek ||--|o RdfsLiteral : "rdfs_label"
SdosDayOfWeek ||--|o SdosURL : "sdos_sameAs"
SdosDayOfWeek ||--|o SdosOrganization : "sdos_contributor"
SdosDayOfWeek ||--|o SdosPerson : "sdos_contributor"
SdosDayOfWeek ||--|o RdfsLiteral : "rdfs_comment"
SdosDeliveryMethod ||--|o RdfsLiteral : "rdfs_label"
SdosDeliveryMethod ||--|o SdosOrganization : "sdos_contributor"
SdosDeliveryMethod ||--|o SdosPerson : "sdos_contributor"
SdosDeliveryMethod ||--|o RdfsLiteral : "rdfs_comment"
SdosDigitalDocumentPermissionType ||--|o RdfsLiteral : "rdfs_label"
SdosDigitalDocumentPermissionType ||--|o RdfsLiteral : "rdfs_comment"
SdosDigitalPlatformEnumeration ||--|o RdfsLiteral : "rdfs_label"
SdosDigitalPlatformEnumeration ||--|o SdosURL : "sdos_isPartOf"
SdosDigitalPlatformEnumeration ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosDigitalPlatformEnumeration ||--|o RdfsLiteral : "rdfs_comment"
SdosDriveWheelConfigurationValue ||--|o RdfsLiteral : "rdfs_label"
SdosDriveWheelConfigurationValue ||--|o SdosOrganization : "sdos_contributor"
SdosDriveWheelConfigurationValue ||--|o SdosPerson : "sdos_contributor"
SdosDriveWheelConfigurationValue ||--|o RdfsLiteral : "rdfs_comment"
SdosDrugCostCategory ||--|o RdfsLiteral : "rdfs_label"
SdosDrugCostCategory ||--|o SdosURL : "sdos_isPartOf"
SdosDrugCostCategory ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosDrugCostCategory ||--|o RdfsLiteral : "rdfs_comment"
SdosDrugPregnancyCategory ||--|o RdfsLiteral : "rdfs_label"
SdosDrugPregnancyCategory ||--|o SdosURL : "sdos_isPartOf"
SdosDrugPregnancyCategory ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosDrugPregnancyCategory ||--|o RdfsLiteral : "rdfs_comment"
SdosDrugPrescriptionStatus ||--|o RdfsLiteral : "rdfs_label"
SdosDrugPrescriptionStatus ||--|o SdosURL : "sdos_isPartOf"
SdosDrugPrescriptionStatus ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosDrugPrescriptionStatus ||--|o RdfsLiteral : "rdfs_comment"
SdosEUEnergyEfficiencyEnumeration ||--|o RdfsLiteral : "rdfs_label"
SdosEUEnergyEfficiencyEnumeration ||--|o SdosURL : "sdos_isPartOf"
SdosEUEnergyEfficiencyEnumeration ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosEUEnergyEfficiencyEnumeration ||--|o RdfsLiteral : "rdfs_comment"
SdosEnergyStarEnergyEfficiencyEnumeration ||--|o RdfsLiteral : "rdfs_label"
SdosEnergyStarEnergyEfficiencyEnumeration ||--|o SdosURL : "sdos_isPartOf"
SdosEnergyStarEnergyEfficiencyEnumeration ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosEnergyStarEnergyEfficiencyEnumeration ||--|o RdfsLiteral : "rdfs_comment"
SdosEventAttendanceModeEnumeration ||--|o RdfsLiteral : "rdfs_label"
SdosEventAttendanceModeEnumeration ||--|o SdosURL : "sdos_isPartOf"
SdosEventAttendanceModeEnumeration ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosEventAttendanceModeEnumeration ||--|o RdfsLiteral : "rdfs_comment"
SdosEventStatusType ||--|o RdfsLiteral : "rdfs_label"
SdosEventStatusType ||--|o RdfsLiteral : "rdfs_comment"
SdosFulfillmentTypeEnumeration ||--|o RdfsLiteral : "rdfs_label"
SdosFulfillmentTypeEnumeration ||--|o SdosURL : "sdos_isPartOf"
SdosFulfillmentTypeEnumeration ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosFulfillmentTypeEnumeration ||--|o RdfsLiteral : "rdfs_comment"
SdosGameAvailabilityEnumeration ||--|o RdfsLiteral : "rdfs_label"
SdosGameAvailabilityEnumeration ||--|o SdosURL : "sdos_isPartOf"
SdosGameAvailabilityEnumeration ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosGameAvailabilityEnumeration ||--|o RdfsLiteral : "rdfs_comment"
SdosGamePlayMode ||--|o RdfsLiteral : "rdfs_label"
SdosGamePlayMode ||--|o RdfsLiteral : "rdfs_comment"
SdosGameServerStatus ||--|o RdfsLiteral : "rdfs_label"
SdosGameServerStatus ||--|o RdfsLiteral : "rdfs_comment"
SdosGenderType ||--|o RdfsLiteral : "rdfs_label"
SdosGenderType ||--|o RdfsLiteral : "rdfs_comment"
SdosGovernmentBenefitsType ||--|o RdfsLiteral : "rdfs_label"
SdosGovernmentBenefitsType ||--|o SdosURL : "sdos_isPartOf"
SdosGovernmentBenefitsType ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosGovernmentBenefitsType ||--|o RdfsLiteral : "rdfs_comment"
SdosHealthAspectEnumeration ||--|o RdfsLiteral : "rdfs_label"
SdosHealthAspectEnumeration ||--|o SdosURL : "sdos_isPartOf"
SdosHealthAspectEnumeration ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosHealthAspectEnumeration ||--|o RdfsLiteral : "rdfs_comment"
SdosIPTCDigitalSourceEnumeration ||--|o RdfsLiteral : "rdfs_label"
SdosIPTCDigitalSourceEnumeration ||--|o SdosURL : "sdos_isPartOf"
SdosIPTCDigitalSourceEnumeration ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosIPTCDigitalSourceEnumeration ||--|o RdfsLiteral : "rdfs_comment"
SdosIncentiveQualifiedExpenseType ||--|o RdfsLiteral : "rdfs_label"
SdosIncentiveQualifiedExpenseType ||--|o SdosURL : "sdos_isPartOf"
SdosIncentiveQualifiedExpenseType ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosIncentiveQualifiedExpenseType ||--|o RdfsLiteral : "rdfs_comment"
SdosIncentiveStatus ||--|o RdfsLiteral : "rdfs_label"
SdosIncentiveStatus ||--|o SdosURL : "sdos_isPartOf"
SdosIncentiveStatus ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosIncentiveStatus ||--|o RdfsLiteral : "rdfs_comment"
SdosIncentiveType ||--|o RdfsLiteral : "rdfs_label"
SdosIncentiveType ||--|o SdosURL : "sdos_isPartOf"
SdosIncentiveType ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosIncentiveType ||--|o RdfsLiteral : "rdfs_comment"
SdosInfectiousAgentClass ||--|o RdfsLiteral : "rdfs_label"
SdosInfectiousAgentClass ||--|o SdosURL : "sdos_isPartOf"
SdosInfectiousAgentClass ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosInfectiousAgentClass ||--|o RdfsLiteral : "rdfs_comment"
SdosItemAvailability ||--|o RdfsLiteral : "rdfs_label"
SdosItemAvailability ||--|o RdfsLiteral : "rdfs_comment"
SdosItemListOrderType ||--|o RdfsLiteral : "rdfs_label"
SdosItemListOrderType ||--|o RdfsLiteral : "rdfs_comment"
SdosLegalForceStatus ||--|o RdfsLiteral : "rdfs_label"
SdosLegalForceStatus ||--|o SdosURL : "sdos_isPartOf"
SdosLegalForceStatus ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosLegalForceStatus ||--|o RdfsLiteral : "rdfs_comment"
SdosLegalForceStatus ||--|o SdosOrganization : "sdos_contributor"
SdosLegalForceStatus ||--|o SdosPerson : "sdos_contributor"
SdosLegalValueLevel ||--|o RdfsLiteral : "rdfs_label"
SdosLegalValueLevel ||--|o SdosURL : "sdos_isPartOf"
SdosLegalValueLevel ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosLegalValueLevel ||--|o RdfsLiteral : "rdfs_comment"
SdosLegalValueLevel ||--|o SdosOrganization : "sdos_contributor"
SdosLegalValueLevel ||--|o SdosPerson : "sdos_contributor"
SdosMapCategoryType ||--|o RdfsLiteral : "rdfs_label"
SdosMapCategoryType ||--|o RdfsLiteral : "rdfs_comment"
SdosMeasurementMethodEnum ||--|o RdfsLiteral : "rdfs_label"
SdosMeasurementMethodEnum ||--|o SdosURL : "sdos_isPartOf"
SdosMeasurementMethodEnum ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosMeasurementMethodEnum ||--|o RdfsLiteral : "rdfs_comment"
SdosMediaManipulationRatingEnumeration ||--|o RdfsLiteral : "rdfs_label"
SdosMediaManipulationRatingEnumeration ||--|o SdosURL : "sdos_isPartOf"
SdosMediaManipulationRatingEnumeration ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosMediaManipulationRatingEnumeration ||--|o RdfsLiteral : "rdfs_comment"
SdosMedicalAudienceType ||--|o RdfsLiteral : "rdfs_label"
SdosMedicalAudienceType ||--|o SdosURL : "sdos_isPartOf"
SdosMedicalAudienceType ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosMedicalAudienceType ||--|o RdfsLiteral : "rdfs_comment"
SdosMedicalDevicePurpose ||--|o RdfsLiteral : "rdfs_label"
SdosMedicalDevicePurpose ||--|o SdosURL : "sdos_isPartOf"
SdosMedicalDevicePurpose ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosMedicalDevicePurpose ||--|o RdfsLiteral : "rdfs_comment"
SdosMedicalEvidenceLevel ||--|o RdfsLiteral : "rdfs_label"
SdosMedicalEvidenceLevel ||--|o SdosURL : "sdos_isPartOf"
SdosMedicalEvidenceLevel ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosMedicalEvidenceLevel ||--|o RdfsLiteral : "rdfs_comment"
SdosMedicalImagingTechnique ||--|o RdfsLiteral : "rdfs_label"
SdosMedicalImagingTechnique ||--|o SdosURL : "sdos_isPartOf"
SdosMedicalImagingTechnique ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosMedicalImagingTechnique ||--|o RdfsLiteral : "rdfs_comment"
SdosMedicalObservationalStudyDesign ||--|o RdfsLiteral : "rdfs_label"
SdosMedicalObservationalStudyDesign ||--|o SdosURL : "sdos_isPartOf"
SdosMedicalObservationalStudyDesign ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosMedicalObservationalStudyDesign ||--|o RdfsLiteral : "rdfs_comment"
SdosMedicalProcedureType ||--|o RdfsLiteral : "rdfs_label"
SdosMedicalProcedureType ||--|o SdosURL : "sdos_isPartOf"
SdosMedicalProcedureType ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosMedicalProcedureType ||--|o RdfsLiteral : "rdfs_comment"
SdosMedicalSpecialty ||--|o RdfsLiteral : "rdfs_label"
SdosMedicalSpecialty ||--|o SdosURL : "sdos_isPartOf"
SdosMedicalSpecialty ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosMedicalSpecialty ||--|o RdfsLiteral : "rdfs_comment"
SdosMedicalSpecialty ||--|o SdosMedicalSpecialty : "sdos_supersededBy"
SdosMedicalSpecialty ||--|o SdosProperty : "sdos_supersededBy"
SdosMedicalSpecialty ||--|o SdosMerchantReturnEnumeration : "sdos_supersededBy"
SdosMedicalSpecialty ||--|o SdosClass : "sdos_supersededBy"
SdosMedicalSpecialty ||--|o SdosEnumeration : "sdos_supersededBy"
SdosMedicalSpecialty ||--|o RdfsClass : "rdfs_subClassOf"
SdosMedicalStudyStatus ||--|o RdfsLiteral : "rdfs_label"
SdosMedicalStudyStatus ||--|o SdosURL : "sdos_isPartOf"
SdosMedicalStudyStatus ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosMedicalStudyStatus ||--|o RdfsLiteral : "rdfs_comment"
SdosMedicalTrialDesign ||--|o RdfsLiteral : "rdfs_label"
SdosMedicalTrialDesign ||--|o SdosURL : "sdos_isPartOf"
SdosMedicalTrialDesign ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosMedicalTrialDesign ||--|o RdfsLiteral : "rdfs_comment"
SdosMedicineSystem ||--|o RdfsLiteral : "rdfs_label"
SdosMedicineSystem ||--|o SdosURL : "sdos_isPartOf"
SdosMedicineSystem ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosMedicineSystem ||--|o RdfsLiteral : "rdfs_comment"
SdosMerchantReturnEnumeration ||--|o RdfsLiteral : "rdfs_label"
SdosMerchantReturnEnumeration ||--|o SdosURL : "sdos_isPartOf"
SdosMerchantReturnEnumeration ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosMerchantReturnEnumeration ||--|o RdfsLiteral : "rdfs_comment"
SdosMusicAlbumProductionType ||--|o RdfsLiteral : "rdfs_label"
SdosMusicAlbumProductionType ||--|o SdosOrganization : "sdos_contributor"
SdosMusicAlbumProductionType ||--|o SdosPerson : "sdos_contributor"
SdosMusicAlbumProductionType ||--|o RdfsLiteral : "rdfs_comment"
SdosMusicAlbumReleaseType ||--|o RdfsLiteral : "rdfs_label"
SdosMusicAlbumReleaseType ||--|o SdosOrganization : "sdos_contributor"
SdosMusicAlbumReleaseType ||--|o SdosPerson : "sdos_contributor"
SdosMusicAlbumReleaseType ||--|o RdfsLiteral : "rdfs_comment"
SdosMusicReleaseFormatType ||--|o RdfsLiteral : "rdfs_label"
SdosMusicReleaseFormatType ||--|o SdosOrganization : "sdos_contributor"
SdosMusicReleaseFormatType ||--|o SdosPerson : "sdos_contributor"
SdosMusicReleaseFormatType ||--|o RdfsLiteral : "rdfs_comment"
SdosNLNonprofitType ||--|o RdfsLiteral : "rdfs_label"
SdosNLNonprofitType ||--|o SdosURL : "sdos_isPartOf"
SdosNLNonprofitType ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosNLNonprofitType ||--|o RdfsLiteral : "rdfs_comment"
SdosOfferItemCondition ||--|o RdfsLiteral : "rdfs_label"
SdosOfferItemCondition ||--|o RdfsLiteral : "rdfs_comment"
SdosOrderStatus ||--|o RdfsLiteral : "rdfs_label"
SdosOrderStatus ||--|o RdfsLiteral : "rdfs_comment"
SdosPaymentMethodType ||--|o RdfsLiteral : "rdfs_label"
SdosPaymentMethodType ||--|o RdfsLiteral : "rdfs_comment"
SdosPaymentStatusType ||--|o RdfsLiteral : "rdfs_label"
SdosPaymentStatusType ||--|o RdfsLiteral : "rdfs_comment"
SdosPhysicalActivityCategory ||--|o RdfsLiteral : "rdfs_label"
SdosPhysicalActivityCategory ||--|o SdosURL : "sdos_isPartOf"
SdosPhysicalActivityCategory ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosPhysicalActivityCategory ||--|o RdfsLiteral : "rdfs_comment"
SdosPhysicalExam ||--|o RdfsLiteral : "rdfs_label"
SdosPhysicalExam ||--|o SdosURL : "sdos_isPartOf"
SdosPhysicalExam ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosPhysicalExam ||--|o RdfsLiteral : "rdfs_comment"
SdosPriceComponentTypeEnumeration ||--|o RdfsLiteral : "rdfs_label"
SdosPriceComponentTypeEnumeration ||--|o SdosURL : "sdos_isPartOf"
SdosPriceComponentTypeEnumeration ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosPriceComponentTypeEnumeration ||--|o RdfsLiteral : "rdfs_comment"
SdosPriceTypeEnumeration ||--|o RdfsLiteral : "rdfs_label"
SdosPriceTypeEnumeration ||--|o SdosURL : "sdos_isPartOf"
SdosPriceTypeEnumeration ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosPriceTypeEnumeration ||--|o RdfsLiteral : "rdfs_comment"
SdosProductReturnEnumeration ||--|o RdfsLiteral : "rdfs_label"
SdosProductReturnEnumeration ||--|o SdosURL : "sdos_isPartOf"
SdosProductReturnEnumeration ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosProductReturnEnumeration ||--|o RdfsLiteral : "rdfs_comment"
SdosProductReturnEnumeration ||--|o SdosMedicalSpecialty : "sdos_supersededBy"
SdosProductReturnEnumeration ||--|o SdosProperty : "sdos_supersededBy"
SdosProductReturnEnumeration ||--|o SdosMerchantReturnEnumeration : "sdos_supersededBy"
SdosProductReturnEnumeration ||--|o SdosClass : "sdos_supersededBy"
SdosProductReturnEnumeration ||--|o SdosEnumeration : "sdos_supersededBy"
SdosPurchaseType ||--|o RdfsLiteral : "rdfs_label"
SdosPurchaseType ||--|o SdosURL : "sdos_isPartOf"
SdosPurchaseType ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosPurchaseType ||--|o RdfsLiteral : "rdfs_comment"
SdosRefundTypeEnumeration ||--|o RdfsLiteral : "rdfs_label"
SdosRefundTypeEnumeration ||--|o SdosURL : "sdos_isPartOf"
SdosRefundTypeEnumeration ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosRefundTypeEnumeration ||--|o RdfsLiteral : "rdfs_comment"
SdosReservationStatusType ||--|o RdfsLiteral : "rdfs_label"
SdosReservationStatusType ||--|o RdfsLiteral : "rdfs_comment"
SdosRestrictedDiet ||--|o RdfsLiteral : "rdfs_label"
SdosRestrictedDiet ||--|o RdfsLiteral : "rdfs_comment"
SdosReturnFeesEnumeration ||--|o RdfsLiteral : "rdfs_label"
SdosReturnFeesEnumeration ||--|o SdosURL : "sdos_isPartOf"
SdosReturnFeesEnumeration ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosReturnFeesEnumeration ||--|o RdfsLiteral : "rdfs_comment"
SdosReturnLabelSourceEnumeration ||--|o RdfsLiteral : "rdfs_label"
SdosReturnLabelSourceEnumeration ||--|o SdosURL : "sdos_isPartOf"
SdosReturnLabelSourceEnumeration ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosReturnLabelSourceEnumeration ||--|o RdfsLiteral : "rdfs_comment"
SdosReturnMethodEnumeration ||--|o RdfsLiteral : "rdfs_label"
SdosReturnMethodEnumeration ||--|o SdosURL : "sdos_isPartOf"
SdosReturnMethodEnumeration ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosReturnMethodEnumeration ||--|o RdfsLiteral : "rdfs_comment"
SdosRsvpResponseType ||--|o RdfsLiteral : "rdfs_label"
SdosRsvpResponseType ||--|o RdfsLiteral : "rdfs_comment"
SdosSizeSystemEnumeration ||--|o RdfsLiteral : "rdfs_label"
SdosSizeSystemEnumeration ||--|o SdosURL : "sdos_isPartOf"
SdosSizeSystemEnumeration ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosSizeSystemEnumeration ||--|o RdfsLiteral : "rdfs_comment"
SdosSteeringPositionValue ||--|o RdfsLiteral : "rdfs_label"
SdosSteeringPositionValue ||--|o SdosOrganization : "sdos_contributor"
SdosSteeringPositionValue ||--|o SdosPerson : "sdos_contributor"
SdosSteeringPositionValue ||--|o RdfsLiteral : "rdfs_comment"
SdosTierBenefitEnumeration ||--|o RdfsLiteral : "rdfs_label"
SdosTierBenefitEnumeration ||--|o SdosURL : "sdos_isPartOf"
SdosTierBenefitEnumeration ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosTierBenefitEnumeration ||--|o RdfsLiteral : "rdfs_comment"
SdosUKNonprofitType ||--|o RdfsLiteral : "rdfs_label"
SdosUKNonprofitType ||--|o SdosURL : "sdos_isPartOf"
SdosUKNonprofitType ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosUKNonprofitType ||--|o RdfsLiteral : "rdfs_comment"
SdosUSNonprofitType ||--|o RdfsLiteral : "rdfs_label"
SdosUSNonprofitType ||--|o SdosURL : "sdos_isPartOf"
SdosUSNonprofitType ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosUSNonprofitType ||--|o RdfsLiteral : "rdfs_comment"
SdosWearableMeasurementTypeEnumeration ||--|o RdfsLiteral : "rdfs_label"
SdosWearableMeasurementTypeEnumeration ||--|o SdosURL : "sdos_isPartOf"
SdosWearableMeasurementTypeEnumeration ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosWearableMeasurementTypeEnumeration ||--|o RdfsLiteral : "rdfs_comment"
SdosWearableSizeGroupEnumeration ||--|o RdfsLiteral : "rdfs_label"
SdosWearableSizeGroupEnumeration ||--|o SdosURL : "sdos_isPartOf"
SdosWearableSizeGroupEnumeration ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosWearableSizeGroupEnumeration ||--|o RdfsLiteral : "rdfs_comment"
SdosWearableSizeSystemEnumeration ||--|o RdfsLiteral : "rdfs_label"
SdosWearableSizeSystemEnumeration ||--|o SdosURL : "sdos_isPartOf"
SdosWearableSizeSystemEnumeration ||--|o SdosCreativeWork : "sdos_isPartOf"
SdosWearableSizeSystemEnumeration ||--|o RdfsLiteral : "rdfs_comment"
AdmsSemanticAssetDistribution ||--|o SkosConcept : "adms_status"
RdfDatatypeProperty ||--|o RdfsLiteral : "rdfs_comment"
RdfDatatypeProperty ||--|o RdfsClass : "rdfs_domain"
RdfDatatypeProperty ||--|o RdfsLiteral : "rdfs_label"
VaemGraphMetaData ||--|o RdfsLiteral : "dct_created"
VaemGraphMetaData ||--|o RdfsLiteral : "dct_modified"
VaemGraphMetaData ||--|o RdfsLiteral : "dct_title"
VaemGraphMetaData ||--|o RdfsLiteral : "rdfs_label"
VaemGraphMetaData ||--|o VaemParty : "vaem_hasOwner"
VaemGraphMetaData ||--|o OwlAnnotationProperty : "vaem_usesNonImportedResource"
VaemGraphMetaData ||--|o RdfsResource : "vaem_usesNonImportedResource"
VaemGraphMetaData ||--|o VaemGraphRole : "vaem_hasGraphRole"
VaemGraphMetaData ||--|o OwlOntology : "rdfs_isDefinedBy"
VaemGraphMetaData ||--|o RdfsResource : "rdfs_isDefinedBy"
VaemGraphMetaData ||--|o VaemParty : "vaem_hasSteward"
VaemGraphRole ||--|o RdfsLiteral : "rdfs_label"
VaemGraphRole ||--|o OwlOntology : "rdfs_isDefinedBy"
VaemGraphRole ||--|o RdfsResource : "rdfs_isDefinedBy"
VaemParty ||--|o RdfsLiteral : "rdfs_label"
VaemParty ||--|o OwlOntology : "rdfs_isDefinedBy"
VaemParty ||--|o RdfsResource : "rdfs_isDefinedBy"
VaemCatalogEntry ||--|o RdfsLiteral : "rdfs_label"
VaemCatalogEntry ||--|o OwlOntology : "rdfs_isDefinedBy"
VaemCatalogEntry ||--|o RdfsResource : "rdfs_isDefinedBy"
VoagAttribution ||--|o RdfsLiteral : "rdfs_label"
VoagAttribution ||--|o VoagAttributionLogo : "voag_hasLogo"
VoagAttribution ||--|o VoagLogo : "voag_hasLogo"
VoagAttribution ||--|o VoagOrganizationLogo : "voag_hasLogo"
VoagAttribution ||--|o OwlOntology : "rdfs_isDefinedBy"
VoagAttribution ||--|o RdfsResource : "rdfs_isDefinedBy"
VoagAttributionLogo ||--|o RdfsLiteral : "rdfs_label"
VoagAttributionLogo ||--|o OwlOntology : "rdfs_isDefinedBy"
VoagAttributionLogo ||--|o RdfsResource : "rdfs_isDefinedBy"
VoagChangeFrequency ||--|o RdfsLiteral : "rdfs_label"
VoagChangeFrequency ||--|o OwlOntology : "rdfs_isDefinedBy"
VoagChangeFrequency ||--|o RdfsResource : "rdfs_isDefinedBy"
VoagChangeFrequency ||--|o XsdAnySimpleType : "dtype_value"
VoagChangeType ||--|o RdfsLiteral : "rdfs_label"
VoagChangeType ||--|o OwlOntology : "rdfs_isDefinedBy"
VoagChangeType ||--|o RdfsResource : "rdfs_isDefinedBy"
VoagConfidentialityLevel ||--|o RdfsLiteral : "rdfs_label"
VoagConfidentialityLevel ||--|o XsdAnySimpleType : "dtype_code"
VoagConfidentialityLevel ||--|o OwlOntology : "rdfs_isDefinedBy"
VoagConfidentialityLevel ||--|o RdfsResource : "rdfs_isDefinedBy"
VoagConfidentialityLevel ||--|o XsdAnySimpleType : "dtype_value"
VoagCreativeCommonsPermission ||--|o RdfsLiteral : "rdfs_label"
VoagCreativeCommonsPermission ||--|o OwlOntology : "rdfs_isDefinedBy"
VoagCreativeCommonsPermission ||--|o RdfsResource : "rdfs_isDefinedBy"
VoagCreativeCommonsProhibition ||--|o RdfsLiteral : "rdfs_label"
VoagCreativeCommonsProhibition ||--|o OwlOntology : "rdfs_isDefinedBy"
VoagCreativeCommonsProhibition ||--|o RdfsResource : "rdfs_isDefinedBy"
VoagCreativeCommonsRequirement ||--|o RdfsLiteral : "rdfs_label"
VoagCreativeCommonsRequirement ||--|o OwlOntology : "rdfs_isDefinedBy"
VoagCreativeCommonsRequirement ||--|o RdfsResource : "rdfs_isDefinedBy"
VoagGovernance ||--|o RdfsLiteral : "rdfs_label"
VoagGovernance ||--|o OwlOntology : "rdfs_isDefinedBy"
VoagGovernance ||--|o RdfsResource : "rdfs_isDefinedBy"
VoagGovernanceRole ||--|o RdfsLiteral : "rdfs_label"
VoagGovernanceRole ||--|o OwlOntology : "rdfs_isDefinedBy"
VoagGovernanceRole ||--|o RdfsResource : "rdfs_isDefinedBy"
VoagGovernanceRole ||--|o XsdAnySimpleType : "dtype_value"
VoagIcon ||--|o RdfsLiteral : "rdfs_label"
VoagIcon ||--|o OwlOntology : "rdfs_isDefinedBy"
VoagIcon ||--|o RdfsResource : "rdfs_isDefinedBy"
VoagIssueStatus ||--|o RdfsLiteral : "rdfs_label"
VoagIssueStatus ||--|o OwlOntology : "rdfs_isDefinedBy"
VoagIssueStatus ||--|o RdfsResource : "rdfs_isDefinedBy"
VoagIssueStatus ||--|o XsdAnySimpleType : "dtype_value"
VoagLicenseModel ||--|o RdfsLiteral : "rdfs_label"
VoagLicenseModel ||--|o OwlOntology : "rdfs_isDefinedBy"
VoagLicenseModel ||--|o RdfsResource : "rdfs_isDefinedBy"
VoagLogo ||--|o RdfsLiteral : "rdfs_label"
VoagLogo ||--|o OwlOntology : "rdfs_isDefinedBy"
VoagLogo ||--|o RdfsResource : "rdfs_isDefinedBy"
VoagMaturity ||--|o RdfsLiteral : "rdfs_label"
VoagMaturity ||--|o OwlOntology : "rdfs_isDefinedBy"
VoagMaturity ||--|o RdfsResource : "rdfs_isDefinedBy"
VoagOrganizationLogo ||--|o RdfsLiteral : "rdfs_label"
VoagOrganizationLogo ||--|o OwlOntology : "rdfs_isDefinedBy"
VoagOrganizationLogo ||--|o RdfsResource : "rdfs_isDefinedBy"
VoagPedigree ||--|o RdfsLiteral : "rdfs_label"
VoagPedigree ||--|o OwlOntology : "rdfs_isDefinedBy"
VoagPedigree ||--|o RdfsResource : "rdfs_isDefinedBy"
VoagPriorityValue ||--|o RdfsLiteral : "rdfs_label"
VoagPriorityValue ||--|o OwlOntology : "rdfs_isDefinedBy"
VoagPriorityValue ||--|o RdfsResource : "rdfs_isDefinedBy"
VoagPriorityValue ||--|o XsdAnySimpleType : "dtype_value"
VoagProductLogo ||--|o RdfsLiteral : "rdfs_label"
VoagProductLogo ||--|o OwlOntology : "rdfs_isDefinedBy"
VoagProductLogo ||--|o RdfsResource : "rdfs_isDefinedBy"
VoagProvenance ||--|o RdfsLiteral : "rdfs_label"
VoagProvenance ||--|o OwlOntology : "rdfs_isDefinedBy"
VoagProvenance ||--|o RdfsResource : "rdfs_isDefinedBy"
VoagPublicationStatus ||--|o RdfsLiteral : "rdfs_label"
VoagPublicationStatus ||--|o OwlOntology : "rdfs_isDefinedBy"
VoagPublicationStatus ||--|o RdfsResource : "rdfs_isDefinedBy"
VoagPublicationStatus ||--|o XsdAnySimpleType : "dtype_value"
VoagSchemaGraph ||--|o RdfsLiteral : "rdfs_label"
VoagSchemaGraph ||--|o OwlOntology : "rdfs_isDefinedBy"
VoagSchemaGraph ||--|o RdfsResource : "rdfs_isDefinedBy"
KwgoAirPollutant ||--|o RdfsLiteral : "rdfs_label"
KwgoBlueskyWildfireObservableProperty ||--|o RdfsLiteral : "rdfs_label"
KwgoCensusObservableProperty ||--|o OwlOntology : "rdfs_isDefinedBy"
KwgoCensusObservableProperty ||--|o RdfsResource : "rdfs_isDefinedBy"
KwgoCensusObservableProperty ||--|o RdfsLiteral : "rdfs_comment"
KwgoCensusObservableProperty ||--|o RdfsLiteral : "rdfs_label"
KwgoClimateObservableProperty ||--|o RdfsLiteral : "rdfs_label"
KwgoCroplandObservableProperty ||--|o RdfsLiteral : "rdfs_label"
KwgoDroughtIntensity ||--|o RdfsLiteral : "rdfs_label"
KwgoFireCause ||--|o RdfsLiteral : "rdfs_label"
KwgoHelipadAvailability ||--|o RdfsLiteral : "rdfs_label"
KwgoHospitalStatus ||--|o RdfsLiteral : "rdfs_label"
KwgoHospitalType ||--|o RdfsLiteral : "rdfs_label"
KwgoImpactObservableProperty ||--|o RdfsLiteral : "rdfs_label"
KwgoLSADArea ||--|o RdfsLiteral : "rdfs_label"
KwgoLSADArea ||--|o RdfsLiteral : "rdfs_comment"
KwgoMTBSFireObservableProperty ||--|o RdfsLiteral : "rdfs_label"
KwgoMTBSFireObservableProperty ||--|o RdfsLiteral : "rdfs_comment"
KwgoMagnitudeObservableProperty ||--|o RdfsLiteral : "rdfs_label"
KwgoNIFCFireObservableProperty ||--|o RdfsLiteral : "rdfs_label"
KwgoPublicHealthObservableProperty ||--|o RdfsLiteral : "rdfs_label"
KwgoRoadType ||--|o RdfsLiteral : "rdfs_label"
KwgoSmokePlumeObservableProperty ||--|o RdfsLiteral : "rdfs_label"
KwgoSoilMapUnitObservableProperty ||--|o RdfsLiteral : "rdfs_label"
KwgoSoilMapUnitObservableProperty ||--|o RdfsLiteral : "rdfs_comment"
KwgoStormTrackObservableProperty ||--|o RdfsLiteral : "rdfs_label"
KwgoStormTrackletObservableProperty ||--|o RdfsLiteral : "rdfs_label"
KwgoVulnerabilityObservableProperty ||--|o RdfsLiteral : "rdfs_label"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o OwlThing : "owl_sameAs"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o RdfsLiteral : "rdfs_label"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o GeoGeometry : "geo_hasGeometry"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o KwgoAdministrativeRegion3 : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o HyfHYElementaryFlowPath : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o UsSdwisPublicWaterSystem-NTNCWS : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o UsSdwisPublicWaterSystem-TNCWS : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o MeMgsMGS-Well : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o KwgoS2CellLevel13 : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o UsSdwisPublicWaterSystem-SW : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o KwgoAdministrativeRegion : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o GeoSpatialObject : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o UsSdwisPWS-ServiceArea : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o HyfHYWaterBody : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o KwgoRegion : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o UsSdwisPublicWaterSystem-CWS : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o KwgoAdministrativeRegion2 : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o OwlThing : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o UsSdwisPublicWaterSystem-GW : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o HyfHYLake : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o KwgoAdministrativeRegion3 : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o HyfHYElementaryFlowPath : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o UsSdwisPublicWaterSystem-NTNCWS : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o UsSdwisPublicWaterSystem-TNCWS : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o MeMgsMGS-Well : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o KwgoS2CellLevel13 : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o UsSdwisPublicWaterSystem-SW : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o KwgoAdministrativeRegion : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o GeoSpatialObject : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o UsSdwisPWS-ServiceArea : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o HyfHYWaterBody : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o KwgoRegion : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o UsSdwisPublicWaterSystem-CWS : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o KwgoAdministrativeRegion2 : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o OwlThing : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o UsSdwisPublicWaterSystem-GW : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o HyfHYLake : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o OwlThing : "http___gwml2.org_def_gwml2#gwAquiferSystem"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o GeoSpatialObject : "http___gwml2.org_def_gwml2#gwAquiferSystem"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "http___gwml2.org_def_gwml2#gwAquiferSystem"
HttpGwml2.orgDefGwml2#GWAquifer ||--|o GeoGeometry : "geo_defaultGeometry"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o OwlThing : "owl_sameAs"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o OwlThing : "http___gwml2.org_def_gwml2#gwAquiferSystemPart"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "http___gwml2.org_def_gwml2#gwAquiferSystemPart"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o GeoSpatialObject : "http___gwml2.org_def_gwml2#gwAquiferSystemPart"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o RdfsLiteral : "rdfs_label"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o RdfsLiteral : "rdfs_comment"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o GeoGeometry : "geo_hasGeometry"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o KwgoAdministrativeRegion3 : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o HyfHYElementaryFlowPath : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o UsSdwisPublicWaterSystem-NTNCWS : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o UsSdwisPublicWaterSystem-TNCWS : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o MeMgsMGS-Well : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o KwgoS2CellLevel13 : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o UsSdwisPublicWaterSystem-SW : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o KwgoAdministrativeRegion : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o GeoSpatialObject : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o UsSdwisPWS-ServiceArea : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o HyfHYWaterBody : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o KwgoRegion : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o UsSdwisPublicWaterSystem-CWS : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o KwgoAdministrativeRegion2 : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o OwlThing : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o UsSdwisPublicWaterSystem-GW : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o HyfHYLake : "spatial_connectedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o KwgoAdministrativeRegion3 : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o HyfHYElementaryFlowPath : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o UsSdwisPublicWaterSystem-NTNCWS : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o UsSdwisPublicWaterSystem-TNCWS : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o MeMgsMGS-Well : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o KwgoS2CellLevel13 : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o UsSdwisPublicWaterSystem-SW : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o KwgoAdministrativeRegion : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o GeoSpatialObject : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o UsSdwisPWS-ServiceArea : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o HyfHYWaterBody : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o KwgoRegion : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o UsSdwisPublicWaterSystem-CWS : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o KwgoAdministrativeRegion2 : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o OwlThing : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o UsSdwisPublicWaterSystem-GW : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o HyfHYLake : "spatial_spatiallyRelatedTo"
HttpGwml2.orgDefGwml2#GWAquiferSystem ||--|o GeoGeometry : "geo_defaultGeometry"
HttpNhdplusv2.spatialai.orgV1Nhdplusv2#FlowPathLength ||--|o QudtQuantityValue : "qudt_quantityValue"
HttpNhdplusv2.spatialai.orgV1Nhdplusv2#FlowPathLength ||--|o OwlThing : "owl_sameAs"
HyfHYCanal ||--|o OwlThing : "owl_sameAs"
HyfHYCanal ||--|o RdfsLiteral : "rdfs_label"
HyfHYCanal ||--|o GeoGeometry : "geo_hasGeometry"
HyfHYCanal ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "spatial_connectedTo"
HyfHYCanal ||--|o KwgoAdministrativeRegion3 : "spatial_connectedTo"
HyfHYCanal ||--|o HyfHYElementaryFlowPath : "spatial_connectedTo"
HyfHYCanal ||--|o UsSdwisPublicWaterSystem-NTNCWS : "spatial_connectedTo"
HyfHYCanal ||--|o UsSdwisPublicWaterSystem-TNCWS : "spatial_connectedTo"
HyfHYCanal ||--|o MeMgsMGS-Well : "spatial_connectedTo"
HyfHYCanal ||--|o KwgoS2CellLevel13 : "spatial_connectedTo"
HyfHYCanal ||--|o UsSdwisPublicWaterSystem-SW : "spatial_connectedTo"
HyfHYCanal ||--|o KwgoAdministrativeRegion : "spatial_connectedTo"
HyfHYCanal ||--|o GeoSpatialObject : "spatial_connectedTo"
HyfHYCanal ||--|o UsSdwisPWS-ServiceArea : "spatial_connectedTo"
HyfHYCanal ||--|o HyfHYWaterBody : "spatial_connectedTo"
HyfHYCanal ||--|o KwgoRegion : "spatial_connectedTo"
HyfHYCanal ||--|o UsSdwisPublicWaterSystem-CWS : "spatial_connectedTo"
HyfHYCanal ||--|o KwgoAdministrativeRegion2 : "spatial_connectedTo"
HyfHYCanal ||--|o OwlThing : "spatial_connectedTo"
HyfHYCanal ||--|o UsSdwisPublicWaterSystem-GW : "spatial_connectedTo"
HyfHYCanal ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "spatial_connectedTo"
HyfHYCanal ||--|o HyfHYLake : "spatial_connectedTo"
HyfHYCanal ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "spatial_spatiallyRelatedTo"
HyfHYCanal ||--|o KwgoAdministrativeRegion3 : "spatial_spatiallyRelatedTo"
HyfHYCanal ||--|o HyfHYElementaryFlowPath : "spatial_spatiallyRelatedTo"
HyfHYCanal ||--|o UsSdwisPublicWaterSystem-NTNCWS : "spatial_spatiallyRelatedTo"
HyfHYCanal ||--|o UsSdwisPublicWaterSystem-TNCWS : "spatial_spatiallyRelatedTo"
HyfHYCanal ||--|o MeMgsMGS-Well : "spatial_spatiallyRelatedTo"
HyfHYCanal ||--|o KwgoS2CellLevel13 : "spatial_spatiallyRelatedTo"
HyfHYCanal ||--|o UsSdwisPublicWaterSystem-SW : "spatial_spatiallyRelatedTo"
HyfHYCanal ||--|o KwgoAdministrativeRegion : "spatial_spatiallyRelatedTo"
HyfHYCanal ||--|o GeoSpatialObject : "spatial_spatiallyRelatedTo"
HyfHYCanal ||--|o UsSdwisPWS-ServiceArea : "spatial_spatiallyRelatedTo"
HyfHYCanal ||--|o HyfHYWaterBody : "spatial_spatiallyRelatedTo"
HyfHYCanal ||--|o KwgoRegion : "spatial_spatiallyRelatedTo"
HyfHYCanal ||--|o UsSdwisPublicWaterSystem-CWS : "spatial_spatiallyRelatedTo"
HyfHYCanal ||--|o KwgoAdministrativeRegion2 : "spatial_spatiallyRelatedTo"
HyfHYCanal ||--|o OwlThing : "spatial_spatiallyRelatedTo"
HyfHYCanal ||--|o UsSdwisPublicWaterSystem-GW : "spatial_spatiallyRelatedTo"
HyfHYCanal ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "spatial_spatiallyRelatedTo"
HyfHYCanal ||--|o HyfHYLake : "spatial_spatiallyRelatedTo"
HyfHYCanal ||--|o RdfsLiteral : "dct_title"
HyfHYCanal ||--|o GeoGeometry : "geo_defaultGeometry"
HyfHYCanal ||--|o SdosText : "sdos_name"
HyfHYElementaryFlowPath ||--|o OwlThing : "http___nhdplusv2.spatialai.org_v1_nhdplusv2#hasFlowPathLength"
HyfHYElementaryFlowPath ||--|o HttpNhdplusv2.spatialai.orgV1Nhdplusv2#FlowPathLength : "http___nhdplusv2.spatialai.org_v1_nhdplusv2#hasFlowPathLength"
HyfHYElementaryFlowPath ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "spatial_connectedTo"
HyfHYElementaryFlowPath ||--|o KwgoAdministrativeRegion3 : "spatial_connectedTo"
HyfHYElementaryFlowPath ||--|o HyfHYElementaryFlowPath : "spatial_connectedTo"
HyfHYElementaryFlowPath ||--|o UsSdwisPublicWaterSystem-NTNCWS : "spatial_connectedTo"
HyfHYElementaryFlowPath ||--|o UsSdwisPublicWaterSystem-TNCWS : "spatial_connectedTo"
HyfHYElementaryFlowPath ||--|o MeMgsMGS-Well : "spatial_connectedTo"
HyfHYElementaryFlowPath ||--|o KwgoS2CellLevel13 : "spatial_connectedTo"
HyfHYElementaryFlowPath ||--|o UsSdwisPublicWaterSystem-SW : "spatial_connectedTo"
HyfHYElementaryFlowPath ||--|o KwgoAdministrativeRegion : "spatial_connectedTo"
HyfHYElementaryFlowPath ||--|o GeoSpatialObject : "spatial_connectedTo"
HyfHYElementaryFlowPath ||--|o UsSdwisPWS-ServiceArea : "spatial_connectedTo"
HyfHYElementaryFlowPath ||--|o HyfHYWaterBody : "spatial_connectedTo"
HyfHYElementaryFlowPath ||--|o KwgoRegion : "spatial_connectedTo"
HyfHYElementaryFlowPath ||--|o UsSdwisPublicWaterSystem-CWS : "spatial_connectedTo"
HyfHYElementaryFlowPath ||--|o KwgoAdministrativeRegion2 : "spatial_connectedTo"
HyfHYElementaryFlowPath ||--|o OwlThing : "spatial_connectedTo"
HyfHYElementaryFlowPath ||--|o UsSdwisPublicWaterSystem-GW : "spatial_connectedTo"
HyfHYElementaryFlowPath ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "spatial_connectedTo"
HyfHYElementaryFlowPath ||--|o HyfHYLake : "spatial_connectedTo"
HyfHYElementaryFlowPath ||--|o OwlThing : "hyf__downstreamFlowPathTC"
HyfHYElementaryFlowPath ||--|o HttpHyfo.spatialai.orgV1Hyfo#WaterFeatureRepresentation : "hyf__downstreamFlowPathTC"
HyfHYElementaryFlowPath ||--|o HyfHYFlowPath : "hyf__downstreamFlowPathTC"
HyfHYElementaryFlowPath ||--|o Bf03ad86fab1719a427cbb412f91529fa : "hyf__downstreamFlowPathTC"
HyfHYElementaryFlowPath ||--|o GeoFeature : "hyf__downstreamFlowPathTC"
HyfHYElementaryFlowPath ||--|o HyfHYElementaryFlowPath : "hyf__downstreamFlowPathTC"
HyfHYElementaryFlowPath ||--|o HyfHYCatchmentRealization : "hyf__downstreamFlowPathTC"
HyfHYElementaryFlowPath ||--|o GeoSpatialObject : "hyf__downstreamFlowPathTC"
HyfHYElementaryFlowPath ||--|o OwlThing : "owl_sameAs"
HyfHYElementaryFlowPath ||--|o RdfsLiteral : "rdfs_label"
HyfHYElementaryFlowPath ||--|o RdfsLiteral : "dct_title"
HyfHYElementaryFlowPath ||--|o HyfHYElementaryFlowPath : "hyf__upstreamWaterBody"
HyfHYElementaryFlowPath ||--|o GeoGeometry : "geo_defaultGeometry"
HyfHYElementaryFlowPath ||--|o OwlThing : "hyf__downstreamFlowPath"
HyfHYElementaryFlowPath ||--|o HttpHyfo.spatialai.orgV1Hyfo#WaterFeatureRepresentation : "hyf__downstreamFlowPath"
HyfHYElementaryFlowPath ||--|o HyfHYFlowPath : "hyf__downstreamFlowPath"
HyfHYElementaryFlowPath ||--|o Bf03ad86fab1719a427cbb412f91529fa : "hyf__downstreamFlowPath"
HyfHYElementaryFlowPath ||--|o GeoFeature : "hyf__downstreamFlowPath"
HyfHYElementaryFlowPath ||--|o HyfHYElementaryFlowPath : "hyf__downstreamFlowPath"
HyfHYElementaryFlowPath ||--|o HyfHYCatchmentRealization : "hyf__downstreamFlowPath"
HyfHYElementaryFlowPath ||--|o GeoSpatialObject : "hyf__downstreamFlowPath"
HyfHYElementaryFlowPath ||--|o GeoGeometry : "geo_hasGeometry"
HyfHYElementaryFlowPath ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "spatial_spatiallyRelatedTo"
HyfHYElementaryFlowPath ||--|o KwgoAdministrativeRegion3 : "spatial_spatiallyRelatedTo"
HyfHYElementaryFlowPath ||--|o HyfHYElementaryFlowPath : "spatial_spatiallyRelatedTo"
HyfHYElementaryFlowPath ||--|o UsSdwisPublicWaterSystem-NTNCWS : "spatial_spatiallyRelatedTo"
HyfHYElementaryFlowPath ||--|o UsSdwisPublicWaterSystem-TNCWS : "spatial_spatiallyRelatedTo"
HyfHYElementaryFlowPath ||--|o MeMgsMGS-Well : "spatial_spatiallyRelatedTo"
HyfHYElementaryFlowPath ||--|o KwgoS2CellLevel13 : "spatial_spatiallyRelatedTo"
HyfHYElementaryFlowPath ||--|o UsSdwisPublicWaterSystem-SW : "spatial_spatiallyRelatedTo"
HyfHYElementaryFlowPath ||--|o KwgoAdministrativeRegion : "spatial_spatiallyRelatedTo"
HyfHYElementaryFlowPath ||--|o GeoSpatialObject : "spatial_spatiallyRelatedTo"
HyfHYElementaryFlowPath ||--|o UsSdwisPWS-ServiceArea : "spatial_spatiallyRelatedTo"
HyfHYElementaryFlowPath ||--|o HyfHYWaterBody : "spatial_spatiallyRelatedTo"
HyfHYElementaryFlowPath ||--|o KwgoRegion : "spatial_spatiallyRelatedTo"
HyfHYElementaryFlowPath ||--|o UsSdwisPublicWaterSystem-CWS : "spatial_spatiallyRelatedTo"
HyfHYElementaryFlowPath ||--|o KwgoAdministrativeRegion2 : "spatial_spatiallyRelatedTo"
HyfHYElementaryFlowPath ||--|o OwlThing : "spatial_spatiallyRelatedTo"
HyfHYElementaryFlowPath ||--|o UsSdwisPublicWaterSystem-GW : "spatial_spatiallyRelatedTo"
HyfHYElementaryFlowPath ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "spatial_spatiallyRelatedTo"
HyfHYElementaryFlowPath ||--|o HyfHYLake : "spatial_spatiallyRelatedTo"
HyfHYElementaryFlowPath ||--|o SdosText : "sdos_name"
HyfHYEstuary ||--|o OwlThing : "owl_sameAs"
HyfHYEstuary ||--|o RdfsLiteral : "rdfs_label"
HyfHYEstuary ||--|o GeoGeometry : "geo_hasGeometry"
HyfHYEstuary ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "spatial_connectedTo"
HyfHYEstuary ||--|o KwgoAdministrativeRegion3 : "spatial_connectedTo"
HyfHYEstuary ||--|o HyfHYElementaryFlowPath : "spatial_connectedTo"
HyfHYEstuary ||--|o UsSdwisPublicWaterSystem-NTNCWS : "spatial_connectedTo"
HyfHYEstuary ||--|o UsSdwisPublicWaterSystem-TNCWS : "spatial_connectedTo"
HyfHYEstuary ||--|o MeMgsMGS-Well : "spatial_connectedTo"
HyfHYEstuary ||--|o KwgoS2CellLevel13 : "spatial_connectedTo"
HyfHYEstuary ||--|o UsSdwisPublicWaterSystem-SW : "spatial_connectedTo"
HyfHYEstuary ||--|o KwgoAdministrativeRegion : "spatial_connectedTo"
HyfHYEstuary ||--|o GeoSpatialObject : "spatial_connectedTo"
HyfHYEstuary ||--|o UsSdwisPWS-ServiceArea : "spatial_connectedTo"
HyfHYEstuary ||--|o HyfHYWaterBody : "spatial_connectedTo"
HyfHYEstuary ||--|o KwgoRegion : "spatial_connectedTo"
HyfHYEstuary ||--|o UsSdwisPublicWaterSystem-CWS : "spatial_connectedTo"
HyfHYEstuary ||--|o KwgoAdministrativeRegion2 : "spatial_connectedTo"
HyfHYEstuary ||--|o OwlThing : "spatial_connectedTo"
HyfHYEstuary ||--|o UsSdwisPublicWaterSystem-GW : "spatial_connectedTo"
HyfHYEstuary ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "spatial_connectedTo"
HyfHYEstuary ||--|o HyfHYLake : "spatial_connectedTo"
HyfHYEstuary ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "spatial_spatiallyRelatedTo"
HyfHYEstuary ||--|o KwgoAdministrativeRegion3 : "spatial_spatiallyRelatedTo"
HyfHYEstuary ||--|o HyfHYElementaryFlowPath : "spatial_spatiallyRelatedTo"
HyfHYEstuary ||--|o UsSdwisPublicWaterSystem-NTNCWS : "spatial_spatiallyRelatedTo"
HyfHYEstuary ||--|o UsSdwisPublicWaterSystem-TNCWS : "spatial_spatiallyRelatedTo"
HyfHYEstuary ||--|o MeMgsMGS-Well : "spatial_spatiallyRelatedTo"
HyfHYEstuary ||--|o KwgoS2CellLevel13 : "spatial_spatiallyRelatedTo"
HyfHYEstuary ||--|o UsSdwisPublicWaterSystem-SW : "spatial_spatiallyRelatedTo"
HyfHYEstuary ||--|o KwgoAdministrativeRegion : "spatial_spatiallyRelatedTo"
HyfHYEstuary ||--|o GeoSpatialObject : "spatial_spatiallyRelatedTo"
HyfHYEstuary ||--|o UsSdwisPWS-ServiceArea : "spatial_spatiallyRelatedTo"
HyfHYEstuary ||--|o HyfHYWaterBody : "spatial_spatiallyRelatedTo"
HyfHYEstuary ||--|o KwgoRegion : "spatial_spatiallyRelatedTo"
HyfHYEstuary ||--|o UsSdwisPublicWaterSystem-CWS : "spatial_spatiallyRelatedTo"
HyfHYEstuary ||--|o KwgoAdministrativeRegion2 : "spatial_spatiallyRelatedTo"
HyfHYEstuary ||--|o OwlThing : "spatial_spatiallyRelatedTo"
HyfHYEstuary ||--|o UsSdwisPublicWaterSystem-GW : "spatial_spatiallyRelatedTo"
HyfHYEstuary ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "spatial_spatiallyRelatedTo"
HyfHYEstuary ||--|o HyfHYLake : "spatial_spatiallyRelatedTo"
HyfHYEstuary ||--|o RdfsLiteral : "dct_title"
HyfHYEstuary ||--|o GeoGeometry : "geo_defaultGeometry"
HyfHYEstuary ||--|o SdosText : "sdos_name"
HyfHYImpoundment ||--|o OwlThing : "owl_sameAs"
HyfHYImpoundment ||--|o RdfsLiteral : "rdfs_label"
HyfHYImpoundment ||--|o GeoGeometry : "geo_hasGeometry"
HyfHYImpoundment ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "spatial_connectedTo"
HyfHYImpoundment ||--|o KwgoAdministrativeRegion3 : "spatial_connectedTo"
HyfHYImpoundment ||--|o HyfHYElementaryFlowPath : "spatial_connectedTo"
HyfHYImpoundment ||--|o UsSdwisPublicWaterSystem-NTNCWS : "spatial_connectedTo"
HyfHYImpoundment ||--|o UsSdwisPublicWaterSystem-TNCWS : "spatial_connectedTo"
HyfHYImpoundment ||--|o MeMgsMGS-Well : "spatial_connectedTo"
HyfHYImpoundment ||--|o KwgoS2CellLevel13 : "spatial_connectedTo"
HyfHYImpoundment ||--|o UsSdwisPublicWaterSystem-SW : "spatial_connectedTo"
HyfHYImpoundment ||--|o KwgoAdministrativeRegion : "spatial_connectedTo"
HyfHYImpoundment ||--|o GeoSpatialObject : "spatial_connectedTo"
HyfHYImpoundment ||--|o UsSdwisPWS-ServiceArea : "spatial_connectedTo"
HyfHYImpoundment ||--|o HyfHYWaterBody : "spatial_connectedTo"
HyfHYImpoundment ||--|o KwgoRegion : "spatial_connectedTo"
HyfHYImpoundment ||--|o UsSdwisPublicWaterSystem-CWS : "spatial_connectedTo"
HyfHYImpoundment ||--|o KwgoAdministrativeRegion2 : "spatial_connectedTo"
HyfHYImpoundment ||--|o OwlThing : "spatial_connectedTo"
HyfHYImpoundment ||--|o UsSdwisPublicWaterSystem-GW : "spatial_connectedTo"
HyfHYImpoundment ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "spatial_connectedTo"
HyfHYImpoundment ||--|o HyfHYLake : "spatial_connectedTo"
HyfHYImpoundment ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "spatial_spatiallyRelatedTo"
HyfHYImpoundment ||--|o KwgoAdministrativeRegion3 : "spatial_spatiallyRelatedTo"
HyfHYImpoundment ||--|o HyfHYElementaryFlowPath : "spatial_spatiallyRelatedTo"
HyfHYImpoundment ||--|o UsSdwisPublicWaterSystem-NTNCWS : "spatial_spatiallyRelatedTo"
HyfHYImpoundment ||--|o UsSdwisPublicWaterSystem-TNCWS : "spatial_spatiallyRelatedTo"
HyfHYImpoundment ||--|o MeMgsMGS-Well : "spatial_spatiallyRelatedTo"
HyfHYImpoundment ||--|o KwgoS2CellLevel13 : "spatial_spatiallyRelatedTo"
HyfHYImpoundment ||--|o UsSdwisPublicWaterSystem-SW : "spatial_spatiallyRelatedTo"
HyfHYImpoundment ||--|o KwgoAdministrativeRegion : "spatial_spatiallyRelatedTo"
HyfHYImpoundment ||--|o GeoSpatialObject : "spatial_spatiallyRelatedTo"
HyfHYImpoundment ||--|o UsSdwisPWS-ServiceArea : "spatial_spatiallyRelatedTo"
HyfHYImpoundment ||--|o HyfHYWaterBody : "spatial_spatiallyRelatedTo"
HyfHYImpoundment ||--|o KwgoRegion : "spatial_spatiallyRelatedTo"
HyfHYImpoundment ||--|o UsSdwisPublicWaterSystem-CWS : "spatial_spatiallyRelatedTo"
HyfHYImpoundment ||--|o KwgoAdministrativeRegion2 : "spatial_spatiallyRelatedTo"
HyfHYImpoundment ||--|o OwlThing : "spatial_spatiallyRelatedTo"
HyfHYImpoundment ||--|o UsSdwisPublicWaterSystem-GW : "spatial_spatiallyRelatedTo"
HyfHYImpoundment ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "spatial_spatiallyRelatedTo"
HyfHYImpoundment ||--|o HyfHYLake : "spatial_spatiallyRelatedTo"
HyfHYImpoundment ||--|o RdfsLiteral : "dct_title"
HyfHYImpoundment ||--|o GeoGeometry : "geo_defaultGeometry"
HyfHYImpoundment ||--|o SdosText : "sdos_name"
HyfHYLagoon ||--|o OwlThing : "owl_sameAs"
HyfHYLagoon ||--|o RdfsLiteral : "rdfs_label"
HyfHYLagoon ||--|o GeoGeometry : "geo_hasGeometry"
HyfHYLagoon ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "spatial_connectedTo"
HyfHYLagoon ||--|o KwgoAdministrativeRegion3 : "spatial_connectedTo"
HyfHYLagoon ||--|o HyfHYElementaryFlowPath : "spatial_connectedTo"
HyfHYLagoon ||--|o UsSdwisPublicWaterSystem-NTNCWS : "spatial_connectedTo"
HyfHYLagoon ||--|o UsSdwisPublicWaterSystem-TNCWS : "spatial_connectedTo"
HyfHYLagoon ||--|o MeMgsMGS-Well : "spatial_connectedTo"
HyfHYLagoon ||--|o KwgoS2CellLevel13 : "spatial_connectedTo"
HyfHYLagoon ||--|o UsSdwisPublicWaterSystem-SW : "spatial_connectedTo"
HyfHYLagoon ||--|o KwgoAdministrativeRegion : "spatial_connectedTo"
HyfHYLagoon ||--|o GeoSpatialObject : "spatial_connectedTo"
HyfHYLagoon ||--|o UsSdwisPWS-ServiceArea : "spatial_connectedTo"
HyfHYLagoon ||--|o HyfHYWaterBody : "spatial_connectedTo"
HyfHYLagoon ||--|o KwgoRegion : "spatial_connectedTo"
HyfHYLagoon ||--|o UsSdwisPublicWaterSystem-CWS : "spatial_connectedTo"
HyfHYLagoon ||--|o KwgoAdministrativeRegion2 : "spatial_connectedTo"
HyfHYLagoon ||--|o OwlThing : "spatial_connectedTo"
HyfHYLagoon ||--|o UsSdwisPublicWaterSystem-GW : "spatial_connectedTo"
HyfHYLagoon ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "spatial_connectedTo"
HyfHYLagoon ||--|o HyfHYLake : "spatial_connectedTo"
HyfHYLagoon ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "spatial_spatiallyRelatedTo"
HyfHYLagoon ||--|o KwgoAdministrativeRegion3 : "spatial_spatiallyRelatedTo"
HyfHYLagoon ||--|o HyfHYElementaryFlowPath : "spatial_spatiallyRelatedTo"
HyfHYLagoon ||--|o UsSdwisPublicWaterSystem-NTNCWS : "spatial_spatiallyRelatedTo"
HyfHYLagoon ||--|o UsSdwisPublicWaterSystem-TNCWS : "spatial_spatiallyRelatedTo"
HyfHYLagoon ||--|o MeMgsMGS-Well : "spatial_spatiallyRelatedTo"
HyfHYLagoon ||--|o KwgoS2CellLevel13 : "spatial_spatiallyRelatedTo"
HyfHYLagoon ||--|o UsSdwisPublicWaterSystem-SW : "spatial_spatiallyRelatedTo"
HyfHYLagoon ||--|o KwgoAdministrativeRegion : "spatial_spatiallyRelatedTo"
HyfHYLagoon ||--|o GeoSpatialObject : "spatial_spatiallyRelatedTo"
HyfHYLagoon ||--|o UsSdwisPWS-ServiceArea : "spatial_spatiallyRelatedTo"
HyfHYLagoon ||--|o HyfHYWaterBody : "spatial_spatiallyRelatedTo"
HyfHYLagoon ||--|o KwgoRegion : "spatial_spatiallyRelatedTo"
HyfHYLagoon ||--|o UsSdwisPublicWaterSystem-CWS : "spatial_spatiallyRelatedTo"
HyfHYLagoon ||--|o KwgoAdministrativeRegion2 : "spatial_spatiallyRelatedTo"
HyfHYLagoon ||--|o OwlThing : "spatial_spatiallyRelatedTo"
HyfHYLagoon ||--|o UsSdwisPublicWaterSystem-GW : "spatial_spatiallyRelatedTo"
HyfHYLagoon ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "spatial_spatiallyRelatedTo"
HyfHYLagoon ||--|o HyfHYLake : "spatial_spatiallyRelatedTo"
HyfHYLagoon ||--|o RdfsLiteral : "dct_title"
HyfHYLagoon ||--|o GeoGeometry : "geo_defaultGeometry"
HyfHYLagoon ||--|o SdosText : "sdos_name"
HyfHYLake ||--|o OwlThing : "owl_sameAs"
HyfHYLake ||--|o RdfsLiteral : "rdfs_label"
HyfHYLake ||--|o GeoGeometry : "geo_hasGeometry"
HyfHYLake ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "spatial_connectedTo"
HyfHYLake ||--|o KwgoAdministrativeRegion3 : "spatial_connectedTo"
HyfHYLake ||--|o HyfHYElementaryFlowPath : "spatial_connectedTo"
HyfHYLake ||--|o UsSdwisPublicWaterSystem-NTNCWS : "spatial_connectedTo"
HyfHYLake ||--|o UsSdwisPublicWaterSystem-TNCWS : "spatial_connectedTo"
HyfHYLake ||--|o MeMgsMGS-Well : "spatial_connectedTo"
HyfHYLake ||--|o KwgoS2CellLevel13 : "spatial_connectedTo"
HyfHYLake ||--|o UsSdwisPublicWaterSystem-SW : "spatial_connectedTo"
HyfHYLake ||--|o KwgoAdministrativeRegion : "spatial_connectedTo"
HyfHYLake ||--|o GeoSpatialObject : "spatial_connectedTo"
HyfHYLake ||--|o UsSdwisPWS-ServiceArea : "spatial_connectedTo"
HyfHYLake ||--|o HyfHYWaterBody : "spatial_connectedTo"
HyfHYLake ||--|o KwgoRegion : "spatial_connectedTo"
HyfHYLake ||--|o UsSdwisPublicWaterSystem-CWS : "spatial_connectedTo"
HyfHYLake ||--|o KwgoAdministrativeRegion2 : "spatial_connectedTo"
HyfHYLake ||--|o OwlThing : "spatial_connectedTo"
HyfHYLake ||--|o UsSdwisPublicWaterSystem-GW : "spatial_connectedTo"
HyfHYLake ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "spatial_connectedTo"
HyfHYLake ||--|o HyfHYLake : "spatial_connectedTo"
HyfHYLake ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "spatial_spatiallyRelatedTo"
HyfHYLake ||--|o KwgoAdministrativeRegion3 : "spatial_spatiallyRelatedTo"
HyfHYLake ||--|o HyfHYElementaryFlowPath : "spatial_spatiallyRelatedTo"
HyfHYLake ||--|o UsSdwisPublicWaterSystem-NTNCWS : "spatial_spatiallyRelatedTo"
HyfHYLake ||--|o UsSdwisPublicWaterSystem-TNCWS : "spatial_spatiallyRelatedTo"
HyfHYLake ||--|o MeMgsMGS-Well : "spatial_spatiallyRelatedTo"
HyfHYLake ||--|o KwgoS2CellLevel13 : "spatial_spatiallyRelatedTo"
HyfHYLake ||--|o UsSdwisPublicWaterSystem-SW : "spatial_spatiallyRelatedTo"
HyfHYLake ||--|o KwgoAdministrativeRegion : "spatial_spatiallyRelatedTo"
HyfHYLake ||--|o GeoSpatialObject : "spatial_spatiallyRelatedTo"
HyfHYLake ||--|o UsSdwisPWS-ServiceArea : "spatial_spatiallyRelatedTo"
HyfHYLake ||--|o HyfHYWaterBody : "spatial_spatiallyRelatedTo"
HyfHYLake ||--|o KwgoRegion : "spatial_spatiallyRelatedTo"
HyfHYLake ||--|o UsSdwisPublicWaterSystem-CWS : "spatial_spatiallyRelatedTo"
HyfHYLake ||--|o KwgoAdministrativeRegion2 : "spatial_spatiallyRelatedTo"
HyfHYLake ||--|o OwlThing : "spatial_spatiallyRelatedTo"
HyfHYLake ||--|o UsSdwisPublicWaterSystem-GW : "spatial_spatiallyRelatedTo"
HyfHYLake ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "spatial_spatiallyRelatedTo"
HyfHYLake ||--|o HyfHYLake : "spatial_spatiallyRelatedTo"
HyfHYLake ||--|o RdfsLiteral : "dct_title"
HyfHYLake ||--|o GeoGeometry : "geo_defaultGeometry"
HyfHYLake ||--|o SdosText : "sdos_name"
HyfHYRiver ||--|o OwlThing : "owl_sameAs"
HyfHYRiver ||--|o RdfsLiteral : "rdfs_label"
HyfHYRiver ||--|o GeoGeometry : "geo_hasGeometry"
HyfHYRiver ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "spatial_connectedTo"
HyfHYRiver ||--|o KwgoAdministrativeRegion3 : "spatial_connectedTo"
HyfHYRiver ||--|o HyfHYElementaryFlowPath : "spatial_connectedTo"
HyfHYRiver ||--|o UsSdwisPublicWaterSystem-NTNCWS : "spatial_connectedTo"
HyfHYRiver ||--|o UsSdwisPublicWaterSystem-TNCWS : "spatial_connectedTo"
HyfHYRiver ||--|o MeMgsMGS-Well : "spatial_connectedTo"
HyfHYRiver ||--|o KwgoS2CellLevel13 : "spatial_connectedTo"
HyfHYRiver ||--|o UsSdwisPublicWaterSystem-SW : "spatial_connectedTo"
HyfHYRiver ||--|o KwgoAdministrativeRegion : "spatial_connectedTo"
HyfHYRiver ||--|o GeoSpatialObject : "spatial_connectedTo"
HyfHYRiver ||--|o UsSdwisPWS-ServiceArea : "spatial_connectedTo"
HyfHYRiver ||--|o HyfHYWaterBody : "spatial_connectedTo"
HyfHYRiver ||--|o KwgoRegion : "spatial_connectedTo"
HyfHYRiver ||--|o UsSdwisPublicWaterSystem-CWS : "spatial_connectedTo"
HyfHYRiver ||--|o KwgoAdministrativeRegion2 : "spatial_connectedTo"
HyfHYRiver ||--|o OwlThing : "spatial_connectedTo"
HyfHYRiver ||--|o UsSdwisPublicWaterSystem-GW : "spatial_connectedTo"
HyfHYRiver ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "spatial_connectedTo"
HyfHYRiver ||--|o HyfHYLake : "spatial_connectedTo"
HyfHYRiver ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "spatial_spatiallyRelatedTo"
HyfHYRiver ||--|o KwgoAdministrativeRegion3 : "spatial_spatiallyRelatedTo"
HyfHYRiver ||--|o HyfHYElementaryFlowPath : "spatial_spatiallyRelatedTo"
HyfHYRiver ||--|o UsSdwisPublicWaterSystem-NTNCWS : "spatial_spatiallyRelatedTo"
HyfHYRiver ||--|o UsSdwisPublicWaterSystem-TNCWS : "spatial_spatiallyRelatedTo"
HyfHYRiver ||--|o MeMgsMGS-Well : "spatial_spatiallyRelatedTo"
HyfHYRiver ||--|o KwgoS2CellLevel13 : "spatial_spatiallyRelatedTo"
HyfHYRiver ||--|o UsSdwisPublicWaterSystem-SW : "spatial_spatiallyRelatedTo"
HyfHYRiver ||--|o KwgoAdministrativeRegion : "spatial_spatiallyRelatedTo"
HyfHYRiver ||--|o GeoSpatialObject : "spatial_spatiallyRelatedTo"
HyfHYRiver ||--|o UsSdwisPWS-ServiceArea : "spatial_spatiallyRelatedTo"
HyfHYRiver ||--|o HyfHYWaterBody : "spatial_spatiallyRelatedTo"
HyfHYRiver ||--|o KwgoRegion : "spatial_spatiallyRelatedTo"
HyfHYRiver ||--|o UsSdwisPublicWaterSystem-CWS : "spatial_spatiallyRelatedTo"
HyfHYRiver ||--|o KwgoAdministrativeRegion2 : "spatial_spatiallyRelatedTo"
HyfHYRiver ||--|o OwlThing : "spatial_spatiallyRelatedTo"
HyfHYRiver ||--|o UsSdwisPublicWaterSystem-GW : "spatial_spatiallyRelatedTo"
HyfHYRiver ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "spatial_spatiallyRelatedTo"
HyfHYRiver ||--|o HyfHYLake : "spatial_spatiallyRelatedTo"
HyfHYRiver ||--|o RdfsLiteral : "dct_title"
HyfHYRiver ||--|o GeoGeometry : "geo_defaultGeometry"
HyfHYRiver ||--|o SdosText : "sdos_name"
HyfHYWaterBody ||--|o OwlThing : "owl_sameAs"
HyfHYWaterBody ||--|o RdfsLiteral : "rdfs_label"
HyfHYWaterBody ||--|o GeoGeometry : "geo_hasGeometry"
HyfHYWaterBody ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "spatial_connectedTo"
HyfHYWaterBody ||--|o KwgoAdministrativeRegion3 : "spatial_connectedTo"
HyfHYWaterBody ||--|o HyfHYElementaryFlowPath : "spatial_connectedTo"
HyfHYWaterBody ||--|o UsSdwisPublicWaterSystem-NTNCWS : "spatial_connectedTo"
HyfHYWaterBody ||--|o UsSdwisPublicWaterSystem-TNCWS : "spatial_connectedTo"
HyfHYWaterBody ||--|o MeMgsMGS-Well : "spatial_connectedTo"
HyfHYWaterBody ||--|o KwgoS2CellLevel13 : "spatial_connectedTo"
HyfHYWaterBody ||--|o UsSdwisPublicWaterSystem-SW : "spatial_connectedTo"
HyfHYWaterBody ||--|o KwgoAdministrativeRegion : "spatial_connectedTo"
HyfHYWaterBody ||--|o GeoSpatialObject : "spatial_connectedTo"
HyfHYWaterBody ||--|o UsSdwisPWS-ServiceArea : "spatial_connectedTo"
HyfHYWaterBody ||--|o HyfHYWaterBody : "spatial_connectedTo"
HyfHYWaterBody ||--|o KwgoRegion : "spatial_connectedTo"
HyfHYWaterBody ||--|o UsSdwisPublicWaterSystem-CWS : "spatial_connectedTo"
HyfHYWaterBody ||--|o KwgoAdministrativeRegion2 : "spatial_connectedTo"
HyfHYWaterBody ||--|o OwlThing : "spatial_connectedTo"
HyfHYWaterBody ||--|o UsSdwisPublicWaterSystem-GW : "spatial_connectedTo"
HyfHYWaterBody ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "spatial_connectedTo"
HyfHYWaterBody ||--|o HyfHYLake : "spatial_connectedTo"
HyfHYWaterBody ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "spatial_spatiallyRelatedTo"
HyfHYWaterBody ||--|o KwgoAdministrativeRegion3 : "spatial_spatiallyRelatedTo"
HyfHYWaterBody ||--|o HyfHYElementaryFlowPath : "spatial_spatiallyRelatedTo"
HyfHYWaterBody ||--|o UsSdwisPublicWaterSystem-NTNCWS : "spatial_spatiallyRelatedTo"
HyfHYWaterBody ||--|o UsSdwisPublicWaterSystem-TNCWS : "spatial_spatiallyRelatedTo"
HyfHYWaterBody ||--|o MeMgsMGS-Well : "spatial_spatiallyRelatedTo"
HyfHYWaterBody ||--|o KwgoS2CellLevel13 : "spatial_spatiallyRelatedTo"
HyfHYWaterBody ||--|o UsSdwisPublicWaterSystem-SW : "spatial_spatiallyRelatedTo"
HyfHYWaterBody ||--|o KwgoAdministrativeRegion : "spatial_spatiallyRelatedTo"
HyfHYWaterBody ||--|o GeoSpatialObject : "spatial_spatiallyRelatedTo"
HyfHYWaterBody ||--|o UsSdwisPWS-ServiceArea : "spatial_spatiallyRelatedTo"
HyfHYWaterBody ||--|o HyfHYWaterBody : "spatial_spatiallyRelatedTo"
HyfHYWaterBody ||--|o KwgoRegion : "spatial_spatiallyRelatedTo"
HyfHYWaterBody ||--|o UsSdwisPublicWaterSystem-CWS : "spatial_spatiallyRelatedTo"
HyfHYWaterBody ||--|o KwgoAdministrativeRegion2 : "spatial_spatiallyRelatedTo"
HyfHYWaterBody ||--|o OwlThing : "spatial_spatiallyRelatedTo"
HyfHYWaterBody ||--|o UsSdwisPublicWaterSystem-GW : "spatial_spatiallyRelatedTo"
HyfHYWaterBody ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "spatial_spatiallyRelatedTo"
HyfHYWaterBody ||--|o HyfHYLake : "spatial_spatiallyRelatedTo"
HyfHYWaterBody ||--|o RdfsLiteral : "dct_title"
HyfHYWaterBody ||--|o GeoGeometry : "geo_defaultGeometry"
HyfHYWaterBody ||--|o SdosText : "sdos_name"
IlIsgsISGS-Well ||--|o OwlThing : "owl_sameAs"
IlIsgsISGS-Well ||--|o RdfsLiteral : "rdfs_label"
IlIsgsISGS-Well ||--|o IlIsgsWellYield : "il_isgs_wellYield"
IlIsgsISGS-Well ||--|o GeoGeometry : "geo_hasGeometry"
IlIsgsISGS-Well ||--|o IlIsgsWellPurpose : "il_isgs_wellPurpose"
IlIsgsISGS-Well ||--|o IlIsgsWellDepthInFt : "il_isgs_wellDepth"
IlIsgsWellDepthInFt ||--|o OwlThing : "owl_sameAs"
IlIsgsWellPurpose ||--|o RdfsLiteral : "rdfs_label"
IlIsgsWellPurpose ||--|o OwlThing : "owl_sameAs"
IlIsgsWellYield ||--|o OwlThing : "owl_sameAs"
KwgoS2CellLevel13 ||--|o OwlThing : "owl_sameAs"
KwgoS2CellLevel13 ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o KwgoAdministrativeRegion3 : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o HyfHYElementaryFlowPath : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o UsSdwisPublicWaterSystem-NTNCWS : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o UsSdwisPublicWaterSystem-TNCWS : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o MeMgsMGS-Well : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o KwgoS2CellLevel13 : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o UsSdwisPublicWaterSystem-SW : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o KwgoAdministrativeRegion : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o GeoSpatialObject : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o UsSdwisPWS-ServiceArea : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o HyfHYWaterBody : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o KwgoRegion : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o UsSdwisPublicWaterSystem-CWS : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o KwgoAdministrativeRegion2 : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o OwlThing : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o UsSdwisPublicWaterSystem-GW : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o HyfHYLake : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "spatial_spatiallyRelatedTo"
KwgoS2CellLevel13 ||--|o KwgoAdministrativeRegion3 : "spatial_spatiallyRelatedTo"
KwgoS2CellLevel13 ||--|o HyfHYElementaryFlowPath : "spatial_spatiallyRelatedTo"
KwgoS2CellLevel13 ||--|o UsSdwisPublicWaterSystem-NTNCWS : "spatial_spatiallyRelatedTo"
KwgoS2CellLevel13 ||--|o UsSdwisPublicWaterSystem-TNCWS : "spatial_spatiallyRelatedTo"
KwgoS2CellLevel13 ||--|o MeMgsMGS-Well : "spatial_spatiallyRelatedTo"
KwgoS2CellLevel13 ||--|o KwgoS2CellLevel13 : "spatial_spatiallyRelatedTo"
KwgoS2CellLevel13 ||--|o UsSdwisPublicWaterSystem-SW : "spatial_spatiallyRelatedTo"
KwgoS2CellLevel13 ||--|o KwgoAdministrativeRegion : "spatial_spatiallyRelatedTo"
KwgoS2CellLevel13 ||--|o GeoSpatialObject : "spatial_spatiallyRelatedTo"
KwgoS2CellLevel13 ||--|o UsSdwisPWS-ServiceArea : "spatial_spatiallyRelatedTo"
KwgoS2CellLevel13 ||--|o HyfHYWaterBody : "spatial_spatiallyRelatedTo"
KwgoS2CellLevel13 ||--|o KwgoRegion : "spatial_spatiallyRelatedTo"
KwgoS2CellLevel13 ||--|o UsSdwisPublicWaterSystem-CWS : "spatial_spatiallyRelatedTo"
KwgoS2CellLevel13 ||--|o KwgoAdministrativeRegion2 : "spatial_spatiallyRelatedTo"
KwgoS2CellLevel13 ||--|o OwlThing : "spatial_spatiallyRelatedTo"
KwgoS2CellLevel13 ||--|o UsSdwisPublicWaterSystem-GW : "spatial_spatiallyRelatedTo"
KwgoS2CellLevel13 ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "spatial_spatiallyRelatedTo"
KwgoS2CellLevel13 ||--|o HyfHYLake : "spatial_spatiallyRelatedTo"
MeMgsMGS-Well ||--|o GeoGeometry : "geo_hasDefaultGeometry"
MeMgsMGS-Well ||--|o OwlThing : "owl_sameAs"
MeMgsMGS-Well ||--|o RdfsLiteral : "rdfs_label"
MeMgsMGS-Well ||--|o GeoGeometry : "geo_hasGeometry"
MeMgsMGS-Well ||--|o OwlThing : "me_mgs_wellOverburden"
MeMgsMGS-Well ||--|o StadSingleData : "me_mgs_wellOverburden"
MeMgsMGS-Well ||--|o MeMgsWellOverburdenThicknessInFt : "me_mgs_wellOverburden"
MeMgsMGS-Well ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "spatial_connectedTo"
MeMgsMGS-Well ||--|o KwgoAdministrativeRegion3 : "spatial_connectedTo"
MeMgsMGS-Well ||--|o HyfHYElementaryFlowPath : "spatial_connectedTo"
MeMgsMGS-Well ||--|o UsSdwisPublicWaterSystem-NTNCWS : "spatial_connectedTo"
MeMgsMGS-Well ||--|o UsSdwisPublicWaterSystem-TNCWS : "spatial_connectedTo"
MeMgsMGS-Well ||--|o MeMgsMGS-Well : "spatial_connectedTo"
MeMgsMGS-Well ||--|o KwgoS2CellLevel13 : "spatial_connectedTo"
MeMgsMGS-Well ||--|o UsSdwisPublicWaterSystem-SW : "spatial_connectedTo"
MeMgsMGS-Well ||--|o KwgoAdministrativeRegion : "spatial_connectedTo"
MeMgsMGS-Well ||--|o GeoSpatialObject : "spatial_connectedTo"
MeMgsMGS-Well ||--|o UsSdwisPWS-ServiceArea : "spatial_connectedTo"
MeMgsMGS-Well ||--|o HyfHYWaterBody : "spatial_connectedTo"
MeMgsMGS-Well ||--|o KwgoRegion : "spatial_connectedTo"
MeMgsMGS-Well ||--|o UsSdwisPublicWaterSystem-CWS : "spatial_connectedTo"
MeMgsMGS-Well ||--|o KwgoAdministrativeRegion2 : "spatial_connectedTo"
MeMgsMGS-Well ||--|o OwlThing : "spatial_connectedTo"
MeMgsMGS-Well ||--|o UsSdwisPublicWaterSystem-GW : "spatial_connectedTo"
MeMgsMGS-Well ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "spatial_connectedTo"
MeMgsMGS-Well ||--|o HyfHYLake : "spatial_connectedTo"
MeMgsMGS-Well ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "spatial_spatiallyRelatedTo"
MeMgsMGS-Well ||--|o KwgoAdministrativeRegion3 : "spatial_spatiallyRelatedTo"
MeMgsMGS-Well ||--|o HyfHYElementaryFlowPath : "spatial_spatiallyRelatedTo"
MeMgsMGS-Well ||--|o UsSdwisPublicWaterSystem-NTNCWS : "spatial_spatiallyRelatedTo"
MeMgsMGS-Well ||--|o UsSdwisPublicWaterSystem-TNCWS : "spatial_spatiallyRelatedTo"
MeMgsMGS-Well ||--|o MeMgsMGS-Well : "spatial_spatiallyRelatedTo"
MeMgsMGS-Well ||--|o KwgoS2CellLevel13 : "spatial_spatiallyRelatedTo"
MeMgsMGS-Well ||--|o UsSdwisPublicWaterSystem-SW : "spatial_spatiallyRelatedTo"
MeMgsMGS-Well ||--|o KwgoAdministrativeRegion : "spatial_spatiallyRelatedTo"
MeMgsMGS-Well ||--|o GeoSpatialObject : "spatial_spatiallyRelatedTo"
MeMgsMGS-Well ||--|o UsSdwisPWS-ServiceArea : "spatial_spatiallyRelatedTo"
MeMgsMGS-Well ||--|o HyfHYWaterBody : "spatial_spatiallyRelatedTo"
MeMgsMGS-Well ||--|o KwgoRegion : "spatial_spatiallyRelatedTo"
MeMgsMGS-Well ||--|o UsSdwisPublicWaterSystem-CWS : "spatial_spatiallyRelatedTo"
MeMgsMGS-Well ||--|o KwgoAdministrativeRegion2 : "spatial_spatiallyRelatedTo"
MeMgsMGS-Well ||--|o OwlThing : "spatial_spatiallyRelatedTo"
MeMgsMGS-Well ||--|o UsSdwisPublicWaterSystem-GW : "spatial_spatiallyRelatedTo"
MeMgsMGS-Well ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "spatial_spatiallyRelatedTo"
MeMgsMGS-Well ||--|o HyfHYLake : "spatial_spatiallyRelatedTo"
MeMgsMGS-Well ||--|o OwlThing : "me_mgs_ofWellType"
MeMgsMGS-Well ||--|o MeMgsWellType : "me_mgs_ofWellType"
MeMgsMGS-Well ||--|o OwlThing : "me_mgs_hasUse"
MeMgsMGS-Well ||--|o MeMgsWellUse : "me_mgs_hasUse"
MeMgsMGS-Well ||--|o OwlThing : "me_mgs_wellDepth"
MeMgsMGS-Well ||--|o StadSingleData : "me_mgs_wellDepth"
MeMgsMGS-Well ||--|o MeMgsWellDepthInFt : "me_mgs_wellDepth"
MeMgsWellDepthInFt ||--|o OwlThing : "owl_sameAs"
MeMgsWellOverburdenThicknessInFt ||--|o OwlThing : "owl_sameAs"
MeMgsWellType ||--|o OwlThing : "owl_sameAs"
MeMgsWellUse ||--|o OwlThing : "owl_sameAs"
OwlDataProperty ||--|o RdfsClass : "rdfs_domain"
OwlDataProperty ||--|o OwlThing : "owl_sameAs"
Sf#MultiPolygon ||--|o OwlThing : "owl_sameAs"
Sf#Polygon ||--|o OwlThing : "owl_sameAs"
UsSdwisPWS-ServiceArea ||--|o GeoGeometry : "geo_hasDefaultGeometry"
UsSdwisPWS-ServiceArea ||--|o OwlThing : "owl_sameAs"
UsSdwisPWS-ServiceArea ||--|o OwlThing : "us_sdwis_serviceAreaType"
UsSdwisPWS-ServiceArea ||--|o UsSdwisPWS-ServiceAreaType : "us_sdwis_serviceAreaType"
UsSdwisPWS-ServiceArea ||--|o GeoGeometry : "geo_hasGeometry"
UsSdwisPWS-ServiceArea ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "spatial_connectedTo"
UsSdwisPWS-ServiceArea ||--|o KwgoAdministrativeRegion3 : "spatial_connectedTo"
UsSdwisPWS-ServiceArea ||--|o HyfHYElementaryFlowPath : "spatial_connectedTo"
UsSdwisPWS-ServiceArea ||--|o UsSdwisPublicWaterSystem-NTNCWS : "spatial_connectedTo"
UsSdwisPWS-ServiceArea ||--|o UsSdwisPublicWaterSystem-TNCWS : "spatial_connectedTo"
UsSdwisPWS-ServiceArea ||--|o MeMgsMGS-Well : "spatial_connectedTo"
UsSdwisPWS-ServiceArea ||--|o KwgoS2CellLevel13 : "spatial_connectedTo"
UsSdwisPWS-ServiceArea ||--|o UsSdwisPublicWaterSystem-SW : "spatial_connectedTo"
UsSdwisPWS-ServiceArea ||--|o KwgoAdministrativeRegion : "spatial_connectedTo"
UsSdwisPWS-ServiceArea ||--|o GeoSpatialObject : "spatial_connectedTo"
UsSdwisPWS-ServiceArea ||--|o UsSdwisPWS-ServiceArea : "spatial_connectedTo"
UsSdwisPWS-ServiceArea ||--|o HyfHYWaterBody : "spatial_connectedTo"
UsSdwisPWS-ServiceArea ||--|o KwgoRegion : "spatial_connectedTo"
UsSdwisPWS-ServiceArea ||--|o UsSdwisPublicWaterSystem-CWS : "spatial_connectedTo"
UsSdwisPWS-ServiceArea ||--|o KwgoAdministrativeRegion2 : "spatial_connectedTo"
UsSdwisPWS-ServiceArea ||--|o OwlThing : "spatial_connectedTo"
UsSdwisPWS-ServiceArea ||--|o UsSdwisPublicWaterSystem-GW : "spatial_connectedTo"
UsSdwisPWS-ServiceArea ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "spatial_connectedTo"
UsSdwisPWS-ServiceArea ||--|o HyfHYLake : "spatial_connectedTo"
UsSdwisPWS-ServiceArea ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "spatial_spatiallyRelatedTo"
UsSdwisPWS-ServiceArea ||--|o KwgoAdministrativeRegion3 : "spatial_spatiallyRelatedTo"
UsSdwisPWS-ServiceArea ||--|o HyfHYElementaryFlowPath : "spatial_spatiallyRelatedTo"
UsSdwisPWS-ServiceArea ||--|o UsSdwisPublicWaterSystem-NTNCWS : "spatial_spatiallyRelatedTo"
UsSdwisPWS-ServiceArea ||--|o UsSdwisPublicWaterSystem-TNCWS : "spatial_spatiallyRelatedTo"
UsSdwisPWS-ServiceArea ||--|o MeMgsMGS-Well : "spatial_spatiallyRelatedTo"
UsSdwisPWS-ServiceArea ||--|o KwgoS2CellLevel13 : "spatial_spatiallyRelatedTo"
UsSdwisPWS-ServiceArea ||--|o UsSdwisPublicWaterSystem-SW : "spatial_spatiallyRelatedTo"
UsSdwisPWS-ServiceArea ||--|o KwgoAdministrativeRegion : "spatial_spatiallyRelatedTo"
UsSdwisPWS-ServiceArea ||--|o GeoSpatialObject : "spatial_spatiallyRelatedTo"
UsSdwisPWS-ServiceArea ||--|o UsSdwisPWS-ServiceArea : "spatial_spatiallyRelatedTo"
UsSdwisPWS-ServiceArea ||--|o HyfHYWaterBody : "spatial_spatiallyRelatedTo"
UsSdwisPWS-ServiceArea ||--|o KwgoRegion : "spatial_spatiallyRelatedTo"
UsSdwisPWS-ServiceArea ||--|o UsSdwisPublicWaterSystem-CWS : "spatial_spatiallyRelatedTo"
UsSdwisPWS-ServiceArea ||--|o KwgoAdministrativeRegion2 : "spatial_spatiallyRelatedTo"
UsSdwisPWS-ServiceArea ||--|o OwlThing : "spatial_spatiallyRelatedTo"
UsSdwisPWS-ServiceArea ||--|o UsSdwisPublicWaterSystem-GW : "spatial_spatiallyRelatedTo"
UsSdwisPWS-ServiceArea ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "spatial_spatiallyRelatedTo"
UsSdwisPWS-ServiceArea ||--|o HyfHYLake : "spatial_spatiallyRelatedTo"
UsSdwisPWS-ServiceAreaType ||--|o RdfsLiteral : "rdfs_label"
UsSdwisPWS-ServiceAreaType ||--|o OwlThing : "owl_sameAs"
UsSdwisPWS-SourceWaterType ||--|o OwlThing : "owl_sameAs"
UsSdwisPWS-SubFeatureActivity ||--|o RdfsLiteral : "rdfs_label"
UsSdwisPWS-SubFeatureActivity ||--|o OwlThing : "owl_sameAs"
UsSdwisPWS-SubFeatureType ||--|o RdfsLiteral : "rdfs_label"
UsSdwisPWS-SubFeatureType ||--|o OwlThing : "owl_sameAs"
UsSdwisPublicWaterSystem-CWS ||--|o OwlThing : "us_sdwis_primarySourceType"
UsSdwisPublicWaterSystem-CWS ||--|o UsSdwisPWS-SourceWaterType : "us_sdwis_primarySourceType"
UsSdwisPublicWaterSystem-CWS ||--|o OwlThing : "owl_sameAs"
UsSdwisPublicWaterSystem-CWS ||--|o RdfsLiteral : "rdfs_label"
UsSdwisPublicWaterSystem-CWS ||--|o OwlThing : "us_sdwis_serviceArea"
UsSdwisPublicWaterSystem-CWS ||--|o GeoSpatialObject : "us_sdwis_serviceArea"
UsSdwisPublicWaterSystem-CWS ||--|o GeoFeature : "us_sdwis_serviceArea"
UsSdwisPublicWaterSystem-CWS ||--|o UsSdwisPWS-ServiceArea : "us_sdwis_serviceArea"
UsSdwisPublicWaterSystem-CWS ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "spatial_connectedTo"
UsSdwisPublicWaterSystem-CWS ||--|o KwgoAdministrativeRegion3 : "spatial_connectedTo"
UsSdwisPublicWaterSystem-CWS ||--|o HyfHYElementaryFlowPath : "spatial_connectedTo"
UsSdwisPublicWaterSystem-CWS ||--|o UsSdwisPublicWaterSystem-NTNCWS : "spatial_connectedTo"
UsSdwisPublicWaterSystem-CWS ||--|o UsSdwisPublicWaterSystem-TNCWS : "spatial_connectedTo"
UsSdwisPublicWaterSystem-CWS ||--|o MeMgsMGS-Well : "spatial_connectedTo"
UsSdwisPublicWaterSystem-CWS ||--|o KwgoS2CellLevel13 : "spatial_connectedTo"
UsSdwisPublicWaterSystem-CWS ||--|o UsSdwisPublicWaterSystem-SW : "spatial_connectedTo"
UsSdwisPublicWaterSystem-CWS ||--|o KwgoAdministrativeRegion : "spatial_connectedTo"
UsSdwisPublicWaterSystem-CWS ||--|o GeoSpatialObject : "spatial_connectedTo"
UsSdwisPublicWaterSystem-CWS ||--|o UsSdwisPWS-ServiceArea : "spatial_connectedTo"
UsSdwisPublicWaterSystem-CWS ||--|o HyfHYWaterBody : "spatial_connectedTo"
UsSdwisPublicWaterSystem-CWS ||--|o KwgoRegion : "spatial_connectedTo"
UsSdwisPublicWaterSystem-CWS ||--|o UsSdwisPublicWaterSystem-CWS : "spatial_connectedTo"
UsSdwisPublicWaterSystem-CWS ||--|o KwgoAdministrativeRegion2 : "spatial_connectedTo"
UsSdwisPublicWaterSystem-CWS ||--|o OwlThing : "spatial_connectedTo"
UsSdwisPublicWaterSystem-CWS ||--|o UsSdwisPublicWaterSystem-GW : "spatial_connectedTo"
UsSdwisPublicWaterSystem-CWS ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "spatial_connectedTo"
UsSdwisPublicWaterSystem-CWS ||--|o HyfHYLake : "spatial_connectedTo"
UsSdwisPublicWaterSystem-CWS ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-CWS ||--|o KwgoAdministrativeRegion3 : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-CWS ||--|o HyfHYElementaryFlowPath : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-CWS ||--|o UsSdwisPublicWaterSystem-NTNCWS : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-CWS ||--|o UsSdwisPublicWaterSystem-TNCWS : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-CWS ||--|o MeMgsMGS-Well : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-CWS ||--|o KwgoS2CellLevel13 : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-CWS ||--|o UsSdwisPublicWaterSystem-SW : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-CWS ||--|o KwgoAdministrativeRegion : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-CWS ||--|o GeoSpatialObject : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-CWS ||--|o UsSdwisPWS-ServiceArea : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-CWS ||--|o HyfHYWaterBody : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-CWS ||--|o KwgoRegion : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-CWS ||--|o UsSdwisPublicWaterSystem-CWS : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-CWS ||--|o KwgoAdministrativeRegion2 : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-CWS ||--|o OwlThing : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-CWS ||--|o UsSdwisPublicWaterSystem-GW : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-CWS ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-CWS ||--|o HyfHYLake : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-CWS ||--|o RdfsLiteral : "us_sdwis_pwsName"
UsSdwisPublicWaterSystem-GW ||--|o OwlThing : "us_sdwis_primarySourceType"
UsSdwisPublicWaterSystem-GW ||--|o UsSdwisPWS-SourceWaterType : "us_sdwis_primarySourceType"
UsSdwisPublicWaterSystem-GW ||--|o OwlThing : "owl_sameAs"
UsSdwisPublicWaterSystem-GW ||--|o RdfsLiteral : "rdfs_label"
UsSdwisPublicWaterSystem-GW ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "spatial_connectedTo"
UsSdwisPublicWaterSystem-GW ||--|o KwgoAdministrativeRegion3 : "spatial_connectedTo"
UsSdwisPublicWaterSystem-GW ||--|o HyfHYElementaryFlowPath : "spatial_connectedTo"
UsSdwisPublicWaterSystem-GW ||--|o UsSdwisPublicWaterSystem-NTNCWS : "spatial_connectedTo"
UsSdwisPublicWaterSystem-GW ||--|o UsSdwisPublicWaterSystem-TNCWS : "spatial_connectedTo"
UsSdwisPublicWaterSystem-GW ||--|o MeMgsMGS-Well : "spatial_connectedTo"
UsSdwisPublicWaterSystem-GW ||--|o KwgoS2CellLevel13 : "spatial_connectedTo"
UsSdwisPublicWaterSystem-GW ||--|o UsSdwisPublicWaterSystem-SW : "spatial_connectedTo"
UsSdwisPublicWaterSystem-GW ||--|o KwgoAdministrativeRegion : "spatial_connectedTo"
UsSdwisPublicWaterSystem-GW ||--|o GeoSpatialObject : "spatial_connectedTo"
UsSdwisPublicWaterSystem-GW ||--|o UsSdwisPWS-ServiceArea : "spatial_connectedTo"
UsSdwisPublicWaterSystem-GW ||--|o HyfHYWaterBody : "spatial_connectedTo"
UsSdwisPublicWaterSystem-GW ||--|o KwgoRegion : "spatial_connectedTo"
UsSdwisPublicWaterSystem-GW ||--|o UsSdwisPublicWaterSystem-CWS : "spatial_connectedTo"
UsSdwisPublicWaterSystem-GW ||--|o KwgoAdministrativeRegion2 : "spatial_connectedTo"
UsSdwisPublicWaterSystem-GW ||--|o OwlThing : "spatial_connectedTo"
UsSdwisPublicWaterSystem-GW ||--|o UsSdwisPublicWaterSystem-GW : "spatial_connectedTo"
UsSdwisPublicWaterSystem-GW ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "spatial_connectedTo"
UsSdwisPublicWaterSystem-GW ||--|o HyfHYLake : "spatial_connectedTo"
UsSdwisPublicWaterSystem-GW ||--|o OwlThing : "us_sdwis_serviceArea"
UsSdwisPublicWaterSystem-GW ||--|o GeoSpatialObject : "us_sdwis_serviceArea"
UsSdwisPublicWaterSystem-GW ||--|o GeoFeature : "us_sdwis_serviceArea"
UsSdwisPublicWaterSystem-GW ||--|o UsSdwisPWS-ServiceArea : "us_sdwis_serviceArea"
UsSdwisPublicWaterSystem-GW ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-GW ||--|o KwgoAdministrativeRegion3 : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-GW ||--|o HyfHYElementaryFlowPath : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-GW ||--|o UsSdwisPublicWaterSystem-NTNCWS : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-GW ||--|o UsSdwisPublicWaterSystem-TNCWS : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-GW ||--|o MeMgsMGS-Well : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-GW ||--|o KwgoS2CellLevel13 : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-GW ||--|o UsSdwisPublicWaterSystem-SW : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-GW ||--|o KwgoAdministrativeRegion : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-GW ||--|o GeoSpatialObject : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-GW ||--|o UsSdwisPWS-ServiceArea : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-GW ||--|o HyfHYWaterBody : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-GW ||--|o KwgoRegion : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-GW ||--|o UsSdwisPublicWaterSystem-CWS : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-GW ||--|o KwgoAdministrativeRegion2 : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-GW ||--|o OwlThing : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-GW ||--|o UsSdwisPublicWaterSystem-GW : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-GW ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-GW ||--|o HyfHYLake : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-GW ||--|o RdfsLiteral : "us_sdwis_pwsName"
UsSdwisPublicWaterSystem-NTNCWS ||--|o OwlThing : "us_sdwis_primarySourceType"
UsSdwisPublicWaterSystem-NTNCWS ||--|o UsSdwisPWS-SourceWaterType : "us_sdwis_primarySourceType"
UsSdwisPublicWaterSystem-NTNCWS ||--|o OwlThing : "owl_sameAs"
UsSdwisPublicWaterSystem-NTNCWS ||--|o RdfsLiteral : "rdfs_label"
UsSdwisPublicWaterSystem-NTNCWS ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "spatial_connectedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o KwgoAdministrativeRegion3 : "spatial_connectedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o HyfHYElementaryFlowPath : "spatial_connectedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o UsSdwisPublicWaterSystem-NTNCWS : "spatial_connectedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o UsSdwisPublicWaterSystem-TNCWS : "spatial_connectedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o MeMgsMGS-Well : "spatial_connectedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o KwgoS2CellLevel13 : "spatial_connectedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o UsSdwisPublicWaterSystem-SW : "spatial_connectedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o KwgoAdministrativeRegion : "spatial_connectedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o GeoSpatialObject : "spatial_connectedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o UsSdwisPWS-ServiceArea : "spatial_connectedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o HyfHYWaterBody : "spatial_connectedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o KwgoRegion : "spatial_connectedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o UsSdwisPublicWaterSystem-CWS : "spatial_connectedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o KwgoAdministrativeRegion2 : "spatial_connectedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o OwlThing : "spatial_connectedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o UsSdwisPublicWaterSystem-GW : "spatial_connectedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "spatial_connectedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o HyfHYLake : "spatial_connectedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o OwlThing : "us_sdwis_serviceArea"
UsSdwisPublicWaterSystem-NTNCWS ||--|o GeoSpatialObject : "us_sdwis_serviceArea"
UsSdwisPublicWaterSystem-NTNCWS ||--|o GeoFeature : "us_sdwis_serviceArea"
UsSdwisPublicWaterSystem-NTNCWS ||--|o UsSdwisPWS-ServiceArea : "us_sdwis_serviceArea"
UsSdwisPublicWaterSystem-NTNCWS ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o KwgoAdministrativeRegion3 : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o HyfHYElementaryFlowPath : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o UsSdwisPublicWaterSystem-NTNCWS : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o UsSdwisPublicWaterSystem-TNCWS : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o MeMgsMGS-Well : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o KwgoS2CellLevel13 : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o UsSdwisPublicWaterSystem-SW : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o KwgoAdministrativeRegion : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o GeoSpatialObject : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o UsSdwisPWS-ServiceArea : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o HyfHYWaterBody : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o KwgoRegion : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o UsSdwisPublicWaterSystem-CWS : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o KwgoAdministrativeRegion2 : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o OwlThing : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o UsSdwisPublicWaterSystem-GW : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o HyfHYLake : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-NTNCWS ||--|o RdfsLiteral : "us_sdwis_pwsName"
UsSdwisPublicWaterSystem-SW ||--|o OwlThing : "us_sdwis_primarySourceType"
UsSdwisPublicWaterSystem-SW ||--|o UsSdwisPWS-SourceWaterType : "us_sdwis_primarySourceType"
UsSdwisPublicWaterSystem-SW ||--|o OwlThing : "owl_sameAs"
UsSdwisPublicWaterSystem-SW ||--|o RdfsLiteral : "rdfs_label"
UsSdwisPublicWaterSystem-SW ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "spatial_connectedTo"
UsSdwisPublicWaterSystem-SW ||--|o KwgoAdministrativeRegion3 : "spatial_connectedTo"
UsSdwisPublicWaterSystem-SW ||--|o HyfHYElementaryFlowPath : "spatial_connectedTo"
UsSdwisPublicWaterSystem-SW ||--|o UsSdwisPublicWaterSystem-NTNCWS : "spatial_connectedTo"
UsSdwisPublicWaterSystem-SW ||--|o UsSdwisPublicWaterSystem-TNCWS : "spatial_connectedTo"
UsSdwisPublicWaterSystem-SW ||--|o MeMgsMGS-Well : "spatial_connectedTo"
UsSdwisPublicWaterSystem-SW ||--|o KwgoS2CellLevel13 : "spatial_connectedTo"
UsSdwisPublicWaterSystem-SW ||--|o UsSdwisPublicWaterSystem-SW : "spatial_connectedTo"
UsSdwisPublicWaterSystem-SW ||--|o KwgoAdministrativeRegion : "spatial_connectedTo"
UsSdwisPublicWaterSystem-SW ||--|o GeoSpatialObject : "spatial_connectedTo"
UsSdwisPublicWaterSystem-SW ||--|o UsSdwisPWS-ServiceArea : "spatial_connectedTo"
UsSdwisPublicWaterSystem-SW ||--|o HyfHYWaterBody : "spatial_connectedTo"
UsSdwisPublicWaterSystem-SW ||--|o KwgoRegion : "spatial_connectedTo"
UsSdwisPublicWaterSystem-SW ||--|o UsSdwisPublicWaterSystem-CWS : "spatial_connectedTo"
UsSdwisPublicWaterSystem-SW ||--|o KwgoAdministrativeRegion2 : "spatial_connectedTo"
UsSdwisPublicWaterSystem-SW ||--|o OwlThing : "spatial_connectedTo"
UsSdwisPublicWaterSystem-SW ||--|o UsSdwisPublicWaterSystem-GW : "spatial_connectedTo"
UsSdwisPublicWaterSystem-SW ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "spatial_connectedTo"
UsSdwisPublicWaterSystem-SW ||--|o HyfHYLake : "spatial_connectedTo"
UsSdwisPublicWaterSystem-SW ||--|o OwlThing : "us_sdwis_serviceArea"
UsSdwisPublicWaterSystem-SW ||--|o GeoSpatialObject : "us_sdwis_serviceArea"
UsSdwisPublicWaterSystem-SW ||--|o GeoFeature : "us_sdwis_serviceArea"
UsSdwisPublicWaterSystem-SW ||--|o UsSdwisPWS-ServiceArea : "us_sdwis_serviceArea"
UsSdwisPublicWaterSystem-SW ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-SW ||--|o KwgoAdministrativeRegion3 : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-SW ||--|o HyfHYElementaryFlowPath : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-SW ||--|o UsSdwisPublicWaterSystem-NTNCWS : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-SW ||--|o UsSdwisPublicWaterSystem-TNCWS : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-SW ||--|o MeMgsMGS-Well : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-SW ||--|o KwgoS2CellLevel13 : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-SW ||--|o UsSdwisPublicWaterSystem-SW : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-SW ||--|o KwgoAdministrativeRegion : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-SW ||--|o GeoSpatialObject : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-SW ||--|o UsSdwisPWS-ServiceArea : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-SW ||--|o HyfHYWaterBody : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-SW ||--|o KwgoRegion : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-SW ||--|o UsSdwisPublicWaterSystem-CWS : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-SW ||--|o KwgoAdministrativeRegion2 : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-SW ||--|o OwlThing : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-SW ||--|o UsSdwisPublicWaterSystem-GW : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-SW ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-SW ||--|o HyfHYLake : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-SW ||--|o RdfsLiteral : "us_sdwis_pwsName"
UsSdwisPublicWaterSystem-TNCWS ||--|o OwlThing : "us_sdwis_primarySourceType"
UsSdwisPublicWaterSystem-TNCWS ||--|o UsSdwisPWS-SourceWaterType : "us_sdwis_primarySourceType"
UsSdwisPublicWaterSystem-TNCWS ||--|o OwlThing : "owl_sameAs"
UsSdwisPublicWaterSystem-TNCWS ||--|o RdfsLiteral : "rdfs_label"
UsSdwisPublicWaterSystem-TNCWS ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "spatial_connectedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o KwgoAdministrativeRegion3 : "spatial_connectedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o HyfHYElementaryFlowPath : "spatial_connectedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o UsSdwisPublicWaterSystem-NTNCWS : "spatial_connectedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o UsSdwisPublicWaterSystem-TNCWS : "spatial_connectedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o MeMgsMGS-Well : "spatial_connectedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o KwgoS2CellLevel13 : "spatial_connectedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o UsSdwisPublicWaterSystem-SW : "spatial_connectedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o KwgoAdministrativeRegion : "spatial_connectedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o GeoSpatialObject : "spatial_connectedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o UsSdwisPWS-ServiceArea : "spatial_connectedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o HyfHYWaterBody : "spatial_connectedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o KwgoRegion : "spatial_connectedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o UsSdwisPublicWaterSystem-CWS : "spatial_connectedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o KwgoAdministrativeRegion2 : "spatial_connectedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o OwlThing : "spatial_connectedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o UsSdwisPublicWaterSystem-GW : "spatial_connectedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "spatial_connectedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o HyfHYLake : "spatial_connectedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o OwlThing : "us_sdwis_serviceArea"
UsSdwisPublicWaterSystem-TNCWS ||--|o GeoSpatialObject : "us_sdwis_serviceArea"
UsSdwisPublicWaterSystem-TNCWS ||--|o GeoFeature : "us_sdwis_serviceArea"
UsSdwisPublicWaterSystem-TNCWS ||--|o UsSdwisPWS-ServiceArea : "us_sdwis_serviceArea"
UsSdwisPublicWaterSystem-TNCWS ||--|o HttpGwml2.orgDefGwml2#GWAquiferSystem : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o KwgoAdministrativeRegion3 : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o HyfHYElementaryFlowPath : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o UsSdwisPublicWaterSystem-NTNCWS : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o UsSdwisPublicWaterSystem-TNCWS : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o MeMgsMGS-Well : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o KwgoS2CellLevel13 : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o UsSdwisPublicWaterSystem-SW : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o KwgoAdministrativeRegion : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o GeoSpatialObject : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o UsSdwisPWS-ServiceArea : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o HyfHYWaterBody : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o KwgoRegion : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o UsSdwisPublicWaterSystem-CWS : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o KwgoAdministrativeRegion2 : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o OwlThing : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o UsSdwisPublicWaterSystem-GW : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o HttpGwml2.orgDefGwml2#GWAquifer : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o HyfHYLake : "spatial_spatiallyRelatedTo"
UsSdwisPublicWaterSystem-TNCWS ||--|o RdfsLiteral : "us_sdwis_pwsName"

```



## Imports


* okns:dc
* linkml:types
* okns:qudt
* okns:kwg
* okns:extended_types
* okns:sdo
* okns:owl-rdf-rdfs
* okns:geo



## Classes

| Class | Description | Occurrences |
| --- | --- | --- |
| [HttpGwml2.orgDefGwml2#GWAquifer](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/HttpGwml2.orgDefGwml2#GWAquifer.md) | None<br/>| 8441 | 
| [HttpGwml2.orgDefGwml2#GWAquiferSystem](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/HttpGwml2.orgDefGwml2#GWAquiferSystem.md) | None<br/>| 1941 | 
| [HttpNhdplusv2.spatialai.orgV1Nhdplusv2#FlowPathLength](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/HttpNhdplusv2.spatialai.orgV1Nhdplusv2#FlowPathLength.md) | None<br/>| 434501 | 
| [OwlDataProperty](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/OwlDataProperty.md) | None<br/>| 3 | 
| [OwlThing](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/OwlThing.md) | The class of OWL individuals.<br/>| 1901253 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[B4321a9eb518ec74b0f636677676d03cc](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/B4321a9eb518ec74b0f636677676d03cc.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Bf03ad86fab1719a427cbb412f91529fa](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/Bf03ad86fab1719a427cbb412f91529fa.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpHyfo.spatialai.orgV1Hyfo#AquiferWaterFeature](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/HttpHyfo.spatialai.orgV1Hyfo#AquiferWaterFeature.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpHyfo.spatialai.orgV1Hyfo#SubsurfaceWaterFeature](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/HttpHyfo.spatialai.orgV1Hyfo#SubsurfaceWaterFeature.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpHyfo.spatialai.orgV1Hyfo#SurfaceWaterFeature](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/HttpHyfo.spatialai.orgV1Hyfo#SurfaceWaterFeature.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpHyfo.spatialai.orgV1Hyfo#WaterFeature](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/HttpHyfo.spatialai.orgV1Hyfo#WaterFeature.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpHyfo.spatialai.orgV1Hyfo#WaterFeatureRepresentation](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/HttpHyfo.spatialai.orgV1Hyfo#WaterFeatureRepresentation.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HyfHYCatchmentRealization](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/HyfHYCatchmentRealization.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HyfHYFlowPath](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/HyfHYFlowPath.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HyfHYElementaryFlowPath](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/HyfHYElementaryFlowPath.md) | None<br/>| 434501 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HyfHYMainStem](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/HyfHYMainStem.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HyfHYHydroFeature](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/HyfHYHydroFeature.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HyfHYCatchment](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/HyfHYCatchment.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HyfHYWaterBody](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/HyfHYWaterBody.md) | None<br/>| 12902 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HyfHYCanal](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/HyfHYCanal.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HyfHYEstuary](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/HyfHYEstuary.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HyfHYImpoundment](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/HyfHYImpoundment.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HyfHYLagoon](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/HyfHYLagoon.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HyfHYLake](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/HyfHYLake.md) | None<br/>| 60083 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HyfHYRiver](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/HyfHYRiver.md) | None<br/>|  | 
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
| [RdfsResource](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/RdfsResource.md) | The class resource, everything.<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RdfsLiteral](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/RdfsLiteral.md) | The class of literal values, eg. textual strings and integers.<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OwlRational](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/OwlRational.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OwlReal](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/OwlReal.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XsdAnyURI](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/XsdAnyURI.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XsdBase64Binary](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/XsdBase64Binary.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XsdBoolean](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/XsdBoolean.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XsdByte](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/XsdByte.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XsdDateTime](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/XsdDateTime.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XsdDecimal](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/XsdDecimal.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XsdDouble](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/XsdDouble.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XsdFloat](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/XsdFloat.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XsdHexBinary](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/XsdHexBinary.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XsdInt](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/XsdInt.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XsdInteger](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/XsdInteger.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XsdLanguage](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/XsdLanguage.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XsdLong](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/XsdLong.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XsdName](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/XsdName.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XsdNCName](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/XsdNCName.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XsdNegativeInteger](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/XsdNegativeInteger.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XsdNMTOKEN](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/XsdNMTOKEN.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XsdNonNegativeInteger](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/XsdNonNegativeInteger.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XsdNonPositiveInteger](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/XsdNonPositiveInteger.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XsdNormalizedString](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/XsdNormalizedString.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XsdPositiveInteger](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/XsdPositiveInteger.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XsdShort](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/XsdShort.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XsdToken](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/XsdToken.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XsdUnsignedByte](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/XsdUnsignedByte.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XsdUnsignedInt](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/XsdUnsignedInt.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XsdUnsignedLong](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/XsdUnsignedLong.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XsdUnsignedShort](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/XsdUnsignedShort.md) | None<br/>|  | 
| [Sf#MultiPolygon](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/Sf#MultiPolygon.md) | None<br/>| 22 | 
| [Sf#Polygon](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/classes/Sf#Polygon.md) | None<br/>| 10656 | 
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
| [hyf__downstreamFlowPath](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/hyf__downstreamFlowPath.md) | <br/>| 865469 |
| [hyf__downstreamFlowPathTC](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/hyf__downstreamFlowPathTC.md) | <br/>| 407803007 |
| [hyf__encompassingCatchment](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/hyf__encompassingCatchment.md) | <br/>No occurrences of this slot in the graph.|  |
| [hyf__realizedCatchment](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/hyf__realizedCatchment.md) | <br/>No occurrences of this slot in the graph.|  |
| [hyf__upstreamFlowPath](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/hyf__upstreamFlowPath.md) | <br/>No occurrences of this slot in the graph.|  |
| [hyf__upstreamWaterBody](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/hyf__upstreamWaterBody.md) | <br/>| 865469 |
| [il_isgs_hasISWSId](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/il_isgs_hasISWSId.md) | <br/>| 152051 |
| [il_isgs_hasOwner](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/il_isgs_hasOwner.md) | <br/>| 377323 |
| [il_isgs_wellDepth](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/il_isgs_wellDepth.md) | <br/>| 376687 |
| [il_isgs_wellPurpose](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/il_isgs_wellPurpose.md) | <br/>| 379496 |
| [il_isgs_wellYield](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/il_isgs_wellYield.md) | <br/>| 265368 |
| [kwgo_administrativePartOf](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/kwgo_administrativePartOf.md) | <br/>No occurrences of this slot in the graph.|  |
| [me_mgs_hasUse](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/me_mgs_hasUse.md) | <br/>| 143400 |
| [me_mgs_ofWellType](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/me_mgs_ofWellType.md) | <br/>| 144120 |
| [me_mgs_wellDepth](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/me_mgs_wellDepth.md) | <br/>| 147508 |
| [me_mgs_wellOverburden](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/me_mgs_wellOverburden.md) | <br/>| 129946 |
| [owl_imports](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/owl_imports.md) | <br/>No occurrences of this slot in the graph.|  |
| [rdf__1](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/rdf__1.md) | <br/>No occurrences of this slot in the graph.|  |
| [rdf_langRange](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/rdf_langRange.md) | <br/>No occurrences of this slot in the graph.|  |
| [skos_description](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/skos_description.md) | <br/>No occurrences of this slot in the graph.|  |
| [spatial_connectedTo](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/spatial_connectedTo.md) | <br/>| 4665700 |
| [spatial_spatiallyRelatedTo](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/spatial_spatiallyRelatedTo.md) | <br/>| 4665700 |
| [us_sdwis_buysFrom](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/us_sdwis_buysFrom.md) | <br/>No occurrences of this slot in the graph.|  |
| [us_sdwis_deactivationDate](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/us_sdwis_deactivationDate.md) | <br/>| 4524 |
| [us_sdwis_firstReport](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/us_sdwis_firstReport.md) | <br/>| 6402 |
| [us_sdwis_hasActivity](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/us_sdwis_hasActivity.md) | <br/>| 6402 |
| [us_sdwis_hasMethod](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/us_sdwis_hasMethod.md) | <br/>| 296 |
| [us_sdwis_hasOwnership](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/us_sdwis_hasOwnership.md) | <br/>| 5304 |
| [us_sdwis_hasPart](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/us_sdwis_hasPart.md) | <br/>No occurrences of this slot in the graph.|  |
| [us_sdwis_hasPermanentSource](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/us_sdwis_hasPermanentSource.md) | <br/>No occurrences of this slot in the graph.|  |
| [us_sdwis_hasSource](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/us_sdwis_hasSource.md) | <br/>No occurrences of this slot in the graph.|  |
| [us_sdwis_inCombinedSystem](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/us_sdwis_inCombinedSystem.md) | <br/>No occurrences of this slot in the graph.|  |
| [us_sdwis_lastReport](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/us_sdwis_lastReport.md) | <br/>| 6387 |
| [us_sdwis_partOf](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/us_sdwis_partOf.md) | <br/>No occurrences of this slot in the graph.|  |
| [us_sdwis_populationServed](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/us_sdwis_populationServed.md) | <br/>| 6402 |
| [us_sdwis_primarySourceType](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/us_sdwis_primarySourceType.md) | <br/>| 6190 |
| [us_sdwis_pwsName](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/us_sdwis_pwsName.md) | <br/>| 6362 |
| [us_sdwis_sellsTo](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/us_sdwis_sellsTo.md) | <br/>No occurrences of this slot in the graph.|  |
| [us_sdwis_serviceArea](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/us_sdwis_serviceArea.md) | <br/>| 5061 |
| [us_sdwis_serviceAreaType](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/us_sdwis_serviceAreaType.md) | <br/>| 6041 |
| [us_sdwis_serviceConnections](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/us_sdwis_serviceConnections.md) | <br/>| 6402 |
| [us_sdwis_sourceFor](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/us_sdwis_sourceFor.md) | <br/>No occurrences of this slot in the graph.|  |
| [xsd_length](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/xsd_length.md) | <br/>No occurrences of this slot in the graph.|  |
| [xsd_maxExclusive](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/xsd_maxExclusive.md) | <br/>No occurrences of this slot in the graph.|  |
| [xsd_maxLength](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/xsd_maxLength.md) | <br/>No occurrences of this slot in the graph.|  |
| [xsd_minExclusive](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/xsd_minExclusive.md) | <br/>No occurrences of this slot in the graph.|  |
| [xsd_minLength](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/slots/xsd_minLength.md) | <br/>No occurrences of this slot in the graph.|  |






## Types

| Type | Description |
| --- | --- |
| [OwlRational](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/types/OwlRational.md) |  |
| [OwlReal](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/types/OwlReal.md) |  |
| [XsdAnyURI](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/types/XsdAnyURI.md) |  |
| [XsdBase64Binary](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/types/XsdBase64Binary.md) |  |
| [XsdBoolean](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/types/XsdBoolean.md) |  |
| [XsdByte](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/types/XsdByte.md) |  |
| [XsdDateTime](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/types/XsdDateTime.md) |  |
| [XsdDecimal](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/types/XsdDecimal.md) |  |
| [XsdDouble](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/types/XsdDouble.md) |  |
| [XsdFloat](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/types/XsdFloat.md) |  |
| [XsdHexBinary](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/types/XsdHexBinary.md) |  |
| [XsdInt](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/types/XsdInt.md) |  |
| [XsdInteger](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/types/XsdInteger.md) |  |
| [XsdLanguage](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/types/XsdLanguage.md) |  |
| [XsdLong](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/types/XsdLong.md) |  |
| [XsdName](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/types/XsdName.md) |  |
| [XsdNCName](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/types/XsdNCName.md) |  |
| [XsdNegativeInteger](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/types/XsdNegativeInteger.md) |  |
| [XsdNMTOKEN](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/types/XsdNMTOKEN.md) |  |
| [XsdNonNegativeInteger](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/types/XsdNonNegativeInteger.md) |  |
| [XsdNonPositiveInteger](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/types/XsdNonPositiveInteger.md) |  |
| [XsdNormalizedString](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/types/XsdNormalizedString.md) |  |
| [XsdPositiveInteger](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/types/XsdPositiveInteger.md) |  |
| [XsdShort](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/types/XsdShort.md) |  |
| [XsdToken](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/types/XsdToken.md) |  |
| [XsdUnsignedByte](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/types/XsdUnsignedByte.md) |  |
| [XsdUnsignedInt](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/types/XsdUnsignedInt.md) |  |
| [XsdUnsignedLong](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/types/XsdUnsignedLong.md) |  |
| [XsdUnsignedShort](https://github.com/frink-okn/graph-descriptions/blob/main/hydrology-kg/types/XsdUnsignedShort.md) |  |





## IRI prefixes

* dc: http://purl.org/dc/elements/1.1/
* dcgeoid: https://datacommons.org/browser/geoId/
* dct: http://purl.org/dc/terms/
* geo: http://www.opengis.net/ont/geosparql#
* hyf: https://www.opengis.net/def/schema/hy_features/hyf
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
* sf: http://www.opengis.net/ont/sf
* skos: http://www.w3.org/2004/02/skos/core#
* spatial: http://purl.org/spatialai/spatial/spatial-full#
* stad: http://purl.org/spatialai/stad/v2/core/
* us_sdwis: http://sawgraph.spatialai.org/v1/us-sdwis#
* xsd: http://www.w3.org/2001/XMLSchema#
