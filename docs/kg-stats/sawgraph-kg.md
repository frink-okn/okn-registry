# sawgraph

This ontology supports querying the SAWGraph Knowledge Graph and the KnowWhereGraph. It is an adaptation of the spatial ontology originally published by the KnowWhereGraph Project



## Schema Diagram

```mermaid
erDiagram
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
SkosCollection {

}
SkosConcept {

}
SkosConceptScheme {

}
SkosOrderedCollection {

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
B00af777bec4da87c5aebb51d94b2d478 {
    string rdfs_label  
}
B036a3008450d6ce37e35cf5a98355a60 {
    string rdfs_label  
}
B085dcda89ed6aae0d3b229e767f0a1ca {
    string rdfs_label  
}
B0d427a711311f1499a234aa8af2c66d1 {
    string rdfs_label  
}
B215b3a432e1c482d3680398a554edbbf {
    string rdfs_label  
}
B27231c83f17c76e178e0c9f5e10acc55 {
    string rdfs_label  
}
B37977f50d3140da51a9630b8a57396a1 {
    string rdfs_label  
}
B3cc7b3721547b07a4068dc98b6444b8b {
    string rdfs_label  
}
B423a0e253807f20386fc3ccbbd7e0378 {
    string rdfs_label  
}
B44bec873efc8b96cad5f525429c64e0a {
    string rdfs_label  
}
B4fd286b2a5a12e342d61412628b6e4c2 {
    string rdfs_label  
}
B53622dee107de372b2d0566f64ab6e3a {
    string rdfs_label  
}
B5e93e815b548435105d9273d424fa0e8 {
    string rdfs_label  
}
B611b8dff312692e7f32a69834c787a60 {
    string rdfs_label  
}
B623b56ef58fd82dd088819e22d655c08 {
    string rdfs_label  
}
B75dbc5841338872cea35dced609fcd77 {
    string rdfs_label  
}
B75e45ed04b2b903b9029968cada06faa {
    string rdfs_label  
}
B7728f65369357f97de36b133c9d1d5e0 {
    string rdfs_label  
}
B8aa8791a0418cd594c8b56ad21351f72 {
    string rdfs_label  
}
Ba6d85f816540f9fec5b71ba42fc2cca6 {
    string rdfs_label  
}
Ba76635ffb4afc02e78b9ef49973d089f {
    string me_egad_dep_chemicalID  
    string coso_casNumber  
    string coso_substanceID  
    string rdfs_label  
}
Bb0125be5bc4dc7be7e8452e7d22445f6 {
    string rdfs_label  
}
Bb71af62f2f3e5e5b5e0fe81f24eca409 {
    string rdfs_label  
}
Bbefc37cbdd03cae92dadef76b34dbf16 {
    string rdfs_label  
}
Bbf63deb85414ddecd89e46bce27e7f0a {
    string rdfs_label  
}
Be047d68edc8eb3ce96d7edbad5217bfc {
    string rdfs_label  
}
Be497d3b0c2656040c05e303873a2d541 {
    string rdfs_label  
}
Beb7217b5b32080b9606028314249e33b {
    string coso_casNumber  
    string coso_substanceID  
    string rdfs_label  
    string http___w3id.org_sawgraph_v1_me_egad#dep_chemicalID  
}
Beb77c26f8c395403edc359fd5f6dfb28 {
    string rdfs_label  
}
Bf04685c17c0e71ae3c98e08c75cbdfcc {
    string rdfs_label  
}
Bf584e1bfd1c74de0eb37e7b926538b83 {
    string rdfs_label  
}
CosoAggregateContaminantMeasurement {

}
CosoAirSample {

}
CosoAnalysisMethod {

}
CosoAnimalBloodSample {
    string rdfs_label  
    uri coso_fromSamplePoint  
}
CosoAnimalMaterialSample {
    string rdfs_label  
    uri coso_fromSamplePoint  
}
CosoAnimalMilkSample {
    string rdfs_label  
    uri coso_fromSamplePoint  
}
CosoAnimalOrganSample {
    string rdfs_label  
    uri coso_fromSamplePoint  
}
CosoAnimalTissueSample {
    string rdfs_label  
    uri coso_fromSamplePoint  
}
CosoBiotaSample {

}
CosoContaminantAbsoluteMeasurement {

}
CosoContaminantAbsoluteQuantityKind {

}
CosoContaminantConcentrationQuantityKind {
    string rdfs_label  
}
CosoContaminantMassQuantityKind {

}
CosoContaminantMeasurement {

}
CosoContaminantObservation {

}
CosoContaminantRelativeMeasurement {

}
CosoContaminantRelativeQuantityKind {

}
CosoContaminantReleaseObservation {

}
CosoContaminantSampleObservation {

}
CosoContaminantVolumeQuantityKind {
    string rdfs_label  
}
CosoContaminationProperty {

}
CosoDetectQuantityValue {
    uri qudt_hasUnit  
    qudt_NumericUnion qudt_numericValue  
}
CosoDetectionLimit {

}
CosoDrinkingWaterSample {
    string rdfs_label  
}
CosoFeature {

}
CosoFeatureType {

}
CosoFilteredWaterSample {

}
CosoGroundWaterSample {
    string rdfs_label  
}
CosoMaterialSample {

}
CosoMonitoredFeature {

}
CosoNonDetectQuantityValue {
    uri qudt_hasUnit  
    qudt_NumericUnion qudt_numericValue  
}
CosoObservationAnnotation {

}
CosoPlantAbovegroundSample {

}
CosoPlantMaterialSample {
    string rdfs_label  
    uri coso_fromSamplePoint  
}
CosoPlantUndergroundSample {

}
CosoPoint {

}
CosoQuantitationLimit {

}
CosoQuantityValue {

}
CosoRawWaterSample {

}
CosoReleaseFeature {

}
CosoReleasePoint {

}
CosoResultQualifier {

}
CosoSampleAnnotation {

}
CosoSampleMaterialType {

}
CosoSamplePoint {

}
CosoSampledFeature {

}
CosoSedimentSample {

}
CosoSingleContaminantMeasurement {

}
CosoSoilSample {

}
CosoSolidMaterialSample {

}
CosoSolidWasteSample {

}
CosoSubstance {

}
CosoSubstanceCollection {
    string coso_substanceID  
    string rdfs_label  
    string http___w3id.org_sawgraph_v1_me_egad#dep_chemicalID  
}
CosoSurfaceWaterSample {
    string rdfs_label  
}
CosoTreatedWaterSample {
    string rdfs_label  
}
CosoWasteWaterSample {
    string rdfs_label  
}
CosoWaterSample {
    string rdfs_label  
}
CosoWaterSampleBySource {
    string rdfs_label  
}
CosoWaterSampleByTreatment {
    string rdfs_label  
}
CosoOfComptoxSubstance {

}
CosoOfDatasetSubstance {

}
HttpW3id.orgComptoxCompToxChemicalEntity {
    string rdfs_label  
}
HttpW3id.orgComptoxV1ChemicalEntity {
    string rdfs_label  
}
HttpW3id.orgSawgraphV1Me-egad#EGAD-AggregatePFAS-Concentration {
    decimal coso_measurementValue  
    double coso_measurementValue  
    uri qudt_hasQuantityKind  
    string rdfs_label  
}
HttpW3id.orgSawgraphV1Me-egad#EGAD-AnalysisMethod {
    string rdfs_label  
}
HttpW3id.orgSawgraphV1Me-egad#EGAD-ConcentrationQualifier {
    string rdfs_label  
}
HttpW3id.orgSawgraphV1Me-egad#EGAD-MethodDetectionLimit {
    uri qudt_hasUnit  
    qudt_NumericUnion qudt_numericValue  
}
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation {
    uri coso_observedAtSamplePoint  
    uri coso_ofDatasetSubstance  
    date coso_observedTime  
    datetime coso_observedTime  
    string rdfs_label  
    uri coso_hasFeatureOfInterest  
}
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-ParameterName {
    string coso_casNumber  
    string coso_substanceID  
    string rdfs_label  
    string http___w3id.org_sawgraph_v1_me_egad#dep_chemicalID  
}
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Site {
    integer me_egad_siteNumber  
    integer http___w3id.org_sawgraph_v1_me_egad#siteNumber  
    string us_sdwis_hasPWSID  
    string rdfs_label  
}
HttpW3id.orgSawgraphV1Me-egad#EGAD-ReportingLimit {
    uri qudt_hasUnit  
    qudt_NumericUnion qudt_numericValue  
}
HttpW3id.orgSawgraphV1Me-egad#EGAD-ResultType {
    string rdfs_label  
}
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample {
    string rdfs_label  
    uri coso_fromSamplePoint  
}
HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleCollectionMethod {
    string rdfs_label  
}
HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleDetailedLocation {
    string rdfs_label  
}
HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleMaterialType {
    string rdfs_label  
}
HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleMaterialTypeQualifier {
    string rdfs_label  
}
HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint {
    string http___w3id.org_sawgraph_v1_me_egad#samplePointWebName  
    string rdfs_label  
    string http___w3id.org_sawgraph_v1_me_egad#samplePointNumber  
}
HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePointType {
    string rdfs_label  
}
HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleTreatmentStatus {
    string rdfs_label  
}
HttpW3id.orgSawgraphV1Me-egad#EGAD-SampledFeature {
    string rdfs_label  
}
HttpW3id.orgSawgraphV1Me-egad#EGAD-SinglePFAS-Concentration {
    decimal coso_measurementValue  
    double coso_measurementValue  
    uri qudt_hasQuantityKind  
    string rdfs_label  
}
HttpW3id.orgSawgraphV1Me-egad#EGAD-Site {

}
HttpW3id.orgSawgraphV1Me-egad#EGAD-SiteType {
    string rdfs_label  
}
HttpW3id.orgSawgraphV1Me-egad#EGAD-ValidationLevel {
    string rdfs_label  
}
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample {
    string rdfs_label  
    uri coso_fromSamplePoint  
}
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample {
    string rdfs_label  
    uri coso_fromSamplePoint  
}
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample {
    string rdfs_label  
    uri coso_fromSamplePoint  
}
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample {
    string rdfs_label  
    uri coso_fromSamplePoint  
}
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample {
    string rdfs_label  
    uri coso_fromSamplePoint  
}
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample {
    string rdfs_label  
    uri coso_fromSamplePoint  
}
HttpW3id.orgSawgraphV1Us-wqp#AnalyticalMethod {
    string rdfs_comment  
    string rdfs_label  
}
HttpW3id.orgSawgraphV1Us-wqp#Characteristic {
    string coso_casNumber  
    string http___w3id.org_sawgraph_v1_us_wqp#srsID  
    string rdfs_label  
    string http___w3id.org_sawgraph_v1_us_wqp#groupName  
}
HttpW3id.orgSawgraphV1Us-wqp#DefWQPGroundWaterFeatureType {
    string rdfs_comment  
    string rdfs_label  
}
HttpW3id.orgSawgraphV1Us-wqp#DefWQPGroundWaterSample {
    string rdfs_label  
}
HttpW3id.orgSawgraphV1Us-wqp#DefWQPSurfaceWaterFeatureType {
    string rdfs_comment  
    string rdfs_label  
}
HttpW3id.orgSawgraphV1Us-wqp#DefWQPSurfaceWaterSample {
    string rdfs_label  
}
HttpW3id.orgSawgraphV1Us-wqp#DefWQPWasteWaterFeatureType {
    string rdfs_comment  
    string rdfs_label  
}
HttpW3id.orgSawgraphV1Us-wqp#DefWQPWasteWaterSample {
    string rdfs_label  
}
HttpW3id.orgSawgraphV1Us-wqp#FederalUSGovernmentOrganization {
    string http___w3id.org_sawgraph_v1_us_wqp#organizationId  
    string rdfs_label  
    uri http___w3id.org_sawgraph_v1_us_wqp#organizationDescription  
}
HttpW3id.orgSawgraphV1Us-wqp#InstrumentDetectionLevel {
    uri qudt_hasUnit  
    qudt_NumericUnion qudt_numericValue  
}
HttpW3id.orgSawgraphV1Us-wqp#Lab {

}
HttpW3id.orgSawgraphV1Us-wqp#LaboratoryReportingLevel {
    uri qudt_hasUnit  
    qudt_NumericUnion qudt_numericValue  
}
HttpW3id.orgSawgraphV1Us-wqp#LocationType {
    string rdfs_comment  
    string rdfs_label  
}
HttpW3id.orgSawgraphV1Us-wqp#LowerQuantitationLimit {
    uri qudt_hasUnit  
    qudt_NumericUnion qudt_numericValue  
}
HttpW3id.orgSawgraphV1Us-wqp#LowerReportingLimit {
    uri qudt_hasUnit  
    qudt_NumericUnion qudt_numericValue  
}
HttpW3id.orgSawgraphV1Us-wqp#MethodDetectionLevel {
    uri qudt_hasUnit  
    qudt_NumericUnion qudt_numericValue  
}
HttpW3id.orgSawgraphV1Us-wqp#Observation {
    uri coso_observedAtSamplePoint  
    date coso_observedTime  
    datetime coso_observedTime  
    uri coso_ofDatasetSubstance  
    string rdfs_label  
    uri coso_hasFeatureOfInterest  
}
HttpW3id.orgSawgraphV1Us-wqp#Organization {

}
HttpW3id.orgSawgraphV1Us-wqp#PrivateNon-IndustrialOrganization {
    string http___w3id.org_sawgraph_v1_us_wqp#organizationId  
    string rdfs_label  
}
HttpW3id.orgSawgraphV1Us-wqp#Project {

}
HttpW3id.orgSawgraphV1Us-wqp#ResultMeasureQualifier {
    string rdfs_comment  
    string rdfs_label  
}
HttpW3id.orgSawgraphV1Us-wqp#Sample {
    uri http___w3id.org_sawgraph_v1_us_wqp#sampleCollectionMethod  
    uri http___w3id.org_sawgraph_v1_us_wqp#hasProjectId  
    string rdfs_label  
    string http___w3id.org_sawgraph_v1_us_wqp#sampleID  
    uri coso_fromSamplePoint  
}
HttpW3id.orgSawgraphV1Us-wqp#Sample-SpecificQuantitationLimit {
    uri qudt_hasUnit  
    qudt_NumericUnion qudt_numericValue  
}
HttpW3id.orgSawgraphV1Us-wqp#SampleCollectionMethod {

}
HttpW3id.orgSawgraphV1Us-wqp#SampleMedia {
    string rdfs_comment  
    string rdfs_label  
}
HttpW3id.orgSawgraphV1Us-wqp#SampledFeature {
    uri http___w3id.org_sawgraph_v1_us_wqp#locationType  
    string rdfs_label  
}
HttpW3id.orgSawgraphV1Us-wqp#Single-PFAS-Concentration {
    uri coso_hasResultQualifier  
}
HttpW3id.orgSawgraphV1Us-wqp#Site {
    string http___w3id.org_sawgraph_v1_us_wqp#siteName  
    string rdfs_label  
    string http___w3id.org_sawgraph_v1_us_wqp#siteId  
}
HttpW3id.orgSawgraphV1Us-wqp#StateGovernmentUSOrganization {
    string http___w3id.org_sawgraph_v1_us_wqp#organizationId  
    string rdfs_label  
    uri http___w3id.org_sawgraph_v1_us_wqp#organizationDescription  
}
HttpW3id.orgSawgraphV1Us-wqp#StateUSGovernmentOrganization {
    string http___w3id.org_sawgraph_v1_us_wqp#organizationId  
    string rdfs_label  
    uri http___w3id.org_sawgraph_v1_us_wqp#organizationDescription  
}
HttpW3id.orgSawgraphV1Us-wqp#Taxon {
    string rdfs_label  
    string http___w3id.org_sawgraph_v1_us_wqp#rank  
}
HttpW3id.orgSawgraphV1Us-wqp#TaxonGroup.FishNekton {
    string rdfs_label  
    string http___w3id.org_sawgraph_v1_us_wqp#rank  
}
KwgoS2CellLevel13 {

}
KwgoStatisticalArea {

}
MeEgadEGAD-AggregatePFAS-Concentration {
    decimal coso_measurementValue  
    double coso_measurementValue  
    uri qudt_hasQuantityKind  
    string rdfs_label  
}
MeEgadEGAD-AnalysisMethod {
    string rdfs_label  
}
MeEgadEGAD-ConcentrationQualifier {
    string rdfs_label  
}
MeEgadEGAD-MethodDetectionLimit {
    uri qudt_hasUnit  
    qudt_NumericUnion qudt_numericValue  
}
MeEgadEGAD-PFAS-Observation {
    uri coso_observedAtSamplePoint  
    date coso_observedTime  
    datetime coso_observedTime  
    string rdfs_label  
    uri coso_hasFeatureOfInterest  
}
MeEgadEGAD-PFAS-ParameterName {
    string rdfs_label  
}
MeEgadEGAD-PFAS-Site {
    integer me_egad_siteNumber  
    integer http___w3id.org_sawgraph_v1_me_egad#siteNumber  
    string us_sdwis_hasPWSID  
    string rdfs_label  
}
MeEgadEGAD-ReportingLimit {
    uri qudt_hasUnit  
    qudt_NumericUnion qudt_numericValue  
}
MeEgadEGAD-ResultType {
    string rdfs_label  
}
MeEgadEGAD-Sample {
    string rdfs_label  
    uri coso_fromSamplePoint  
}
MeEgadEGAD-SampleCollectionMethod {
    string rdfs_label  
}
MeEgadEGAD-SampleDetailedLocation {
    string rdfs_label  
}
MeEgadEGAD-SampleMaterialType {
    string rdfs_label  
}
MeEgadEGAD-SampleMaterialTypeQualifier {
    string rdfs_label  
}
MeEgadEGAD-SamplePoint {
    string rdfs_label  
}
MeEgadEGAD-SamplePointType {
    string rdfs_label  
}
MeEgadEGAD-SampleTreatmentStatus {
    string rdfs_label  
}
MeEgadEGAD-SampledFeature {
    string rdfs_label  
}
MeEgadEGAD-SinglePFAS-Concentration {
    decimal coso_measurementValue  
    double coso_measurementValue  
    uri qudt_hasQuantityKind  
    string rdfs_label  
}
MeEgadEGAD-Site {

}
MeEgadEGAD-SiteType {
    string rdfs_label  
}
MeEgadEGAD-ValidationLevel {
    string rdfs_label  
}
OboBFO0000040 {

}
OboFOODON00001002 {

}
OboFOODON00001006 {

}
OboFOODON00001015 {

}
OboFOODON00001040 {

}
OboFOODON00001041 {

}
OboFOODON00001046 {

}
OboFOODON00001057 {

}
OboFOODON00001092 {

}
OboFOODON00001093 {
    string rdfs_label  
}
OboFOODON00001105 {

}
OboFOODON00001131 {

}
OboFOODON00001134 {

}
OboFOODON00001147 {

}
OboFOODON00001172 {

}
OboFOODON00001173 {

}
OboFOODON00001175 {

}
OboFOODON00001176 {

}
OboFOODON00001209 {

}
OboFOODON00001242 {

}
OboFOODON00001248 {

}
OboFOODON00001250 {

}
OboFOODON00001251 {

}
OboFOODON00001256 {

}
OboFOODON00001257 {

}
OboFOODON00001261 {

}
OboFOODON00001262 {

}
OboFOODON00001264 {

}
OboFOODON00001274 {

}
OboFOODON00001275 {

}
OboFOODON00001283 {

}
OboFOODON00001291 {

}
OboFOODON00001293 {

}
OboFOODON00001628 {

}
OboFOODON00001635 {

}
OboFOODON00001678 {

}
OboFOODON00001783 {

}
OboFOODON00001792 {

}
OboFOODON00002044 {

}
OboFOODON00002051 {

}
OboFOODON00002127 {

}
OboFOODON00002140 {

}
OboFOODON00002142 {

}
OboFOODON00002143 {

}
OboFOODON00002147 {

}
OboFOODON00002150 {

}
OboFOODON00002153 {

}
OboFOODON00002156 {

}
OboFOODON00002159 {

}
OboFOODON00002165 {
    string rdfs_label  
}
OboFOODON00002236 {

}
OboFOODON00002265 {

}
OboFOODON00002309 {

}
OboFOODON00002381 {

}
OboFOODON00002403 {

}
OboFOODON00002452 {

}
OboFOODON00002477 {
    string rdfs_label  
}
OboFOODON00002576 {

}
OboFOODON00002581 {

}
OboFOODON00002616 {

}
OboFOODON00002689 {

}
OboFOODON00002753 {

}
OboFOODON00002765 {

}
OboFOODON00002819 {

}
OboFOODON00003004 {

}
OboFOODON00003042 {
    string rdfs_label  
}
OboFOODON00003083 {
    string rdfs_label  
}
OboFOODON00003204 {

}
OboFOODON00003425 {
    string rdfs_label  
}
OboFOODON00003567 {

}
OboFOODON00003572 {
    string rdfs_label  
}
OboFOODON00003814 {

}
OboFOODON00003816 {

}
OboFOODON00004172 {
    string rdfs_label  
}
OboFOODON00004183 {

}
OboFOODON00004242 {

}
OboFOODON00004298 {

}
OboFOODON00004331 {

}
OboFOODON00004332 {

}
OboFOODON00004333 {

}
OboFOODON00004436 {
    string rdfs_label  
}
OboFOODON00004460 {
    string rdfs_label  
}
OboFOODON00004859 {

}
OboFOODON00004862 {

}
OboFOODON00004918 {

}
OboFOODON00004921 {

}
OboFOODON02010001 {

}
OboFOODON02010005 {

}
OboFOODON02010006 {

}
OboFOODON02010012 {
    string rdfs_label  
}
OboFOODON02010013 {

}
OboFOODON02010014 {

}
OboFOODON02010015 {
    string rdfs_label  
}
OboFOODON02010024 {

}
OboFOODON02010028 {

}
OboFOODON02010029 {

}
OboFOODON02010030 {

}
OboFOODON02010031 {

}
OboFOODON02010032 {
    string rdfs_comment  
    string rdfs_label  
}
OboFOODON02010033 {

}
OboFOODON02010042 {
    string rdfs_label  
}
OboFOODON02010045 {
    string rdfs_label  
}
OboFOODON02010107 {
    string rdfs_label  
}
OboFOODON02010108 {

}
OboFOODON02010111 {

}
OboFOODON02010112 {

}
OboFOODON02020840 {
    string rdfs_label  
}
OboFOODON02020892 {
    string rdfs_label  
}
OboFOODON02021651 {
    string rdfs_label  
}
OboFOODON02021802 {

}
OboFOODON02021803 {
    string rdfs_label  
}
OboFOODON02021805 {
    string rdfs_label  
}
OboFOODON03301293 {

}
OboFOODON03301750 {

}
OboFOODON03301761 {
    string rdfs_label  
}
OboFOODON03302001 {

}
OboFOODON03303380 {

}
OboFOODON03304313 {

}
OboFOODON03304497 {

}
OboFOODON03304616 {

}
OboFOODON03306306 {

}
OboFOODON03309997 {

}
OboFOODON03310611 {

}
OboFOODON03310961 {

}
OboFOODON03315150 {

}
OboFOODON03315173 {

}
OboFOODON03315308 {

}
OboFOODON03315468 {

}
OboFOODON03315769 {

}
OboFOODON03315883 {

}
OboFOODON03316061 {

}
OboFOODON03317076 {

}
OboFOODON03317170 {

}
OboFOODON03411005 {

}
OboFOODON03411006 {

}
OboFOODON03411013 {

}
OboFOODON03411017 {

}
OboFOODON03411018 {

}
OboFOODON03411021 {

}
OboFOODON03411022 {

}
OboFOODON03411024 {

}
OboFOODON03411036 {

}
OboFOODON03411040 {

}
OboFOODON03411047 {

}
OboFOODON03411048 {

}
OboFOODON03411057 {
    string rdfs_label  
}
OboFOODON03411058 {

}
OboFOODON03411062 {

}
OboFOODON03411121 {

}
OboFOODON03411126 {

}
OboFOODON03411129 {

}
OboFOODON03411134 {

}
OboFOODON03411136 {

}
OboFOODON03411139 {

}
OboFOODON03411140 {

}
OboFOODON03411142 {

}
OboFOODON03411151 {

}
OboFOODON03411156 {

}
OboFOODON03411174 {

}
OboFOODON03411179 {

}
OboFOODON03411183 {
    string rdfs_label  
}
OboFOODON03411184 {

}
OboFOODON03411194 {

}
OboFOODON03411204 {

}
OboFOODON03411213 {

}
OboFOODON03411222 {

}
OboFOODON03411223 {

}
OboFOODON03411231 {

}
OboFOODON03411232 {

}
OboFOODON03411236 {
    string rdfs_label  
}
OboFOODON03411266 {

}
OboFOODON03411293 {

}
OboFOODON03411297 {

}
OboFOODON03411319 {

}
OboFOODON03411324 {
    string rdfs_label  
}
OboFOODON03411325 {
    string rdfs_label  
}
OboFOODON03411328 {
    string rdfs_label  
}
OboFOODON03411331 {

}
OboFOODON03411365 {

}
OboFOODON03411374 {

}
OboFOODON03411380 {

}
OboFOODON03411393 {

}
OboFOODON03411409 {

}
OboFOODON03411433 {

}
OboFOODON03411439 {

}
OboFOODON03411447 {

}
OboFOODON03411454 {

}
OboFOODON03411457 {
    string rdfs_label  
}
OboFOODON03411491 {

}
OboFOODON03411500 {

}
OboFOODON03411539 {

}
OboFOODON03411557 {

}
OboFOODON03411563 {

}
OboFOODON03411564 {

}
OboFOODON03411566 {
    string rdfs_label  
}
OboFOODON03411567 {

}
OboFOODON03411568 {

}
OboFOODON03411579 {

}
OboFOODON03411581 {

}
OboFOODON03411583 {
    string rdfs_label  
}
OboFOODON03411592 {

}
OboFOODON03411594 {

}
OboFOODON03411595 {

}
OboFOODON03411597 {

}
OboFOODON03411598 {

}
OboFOODON03411599 {

}
OboFOODON03411607 {

}
OboFOODON03411614 {

}
OboFOODON03411617 {

}
OboFOODON03411669 {
    string rdfs_label  
}
OboFOODON03411818 {

}
OboFOODON03411826 {

}
OboFOODON03411892 {

}
OboFOODON03412004 {

}
OboFOODON03412005 {

}
OboFOODON03412007 {

}
OboFOODON03412112 {

}
OboFOODON03412113 {

}
OboFOODON03412241 {

}
OboFOODON03412331 {

}
OboFOODON03412362 {

}
OboFOODON03412409 {

}
OboFOODON03412426 {

}
OboFOODON03412453 {

}
OboFOODON03412665 {

}
OboFOODON03413357 {

}
OboFOODON03413358 {
    string rdfs_label  
}
OboFOODON03413360 {

}
OboFOODON03413372 {

}
OboFOODON03413377 {

}
OboFOODON03413378 {
    string rdfs_label  
}
OboFOODON03413406 {

}
OboFOODON03413448 {

}
OboFOODON03413807 {

}
OboFOODON03413808 {

}
OboFOODON03414028 {

}
OboFOODON03414051 {

}
OboFOODON03414066 {

}
OboFOODON03414067 {

}
OboFOODON03414209 {

}
OboFOODON03414282 {

}
OboFOODON03414302 {

}
OboFOODON03414374 {

}
OboFOODON03414381 {

}
OboFOODON03414459 {

}
OboFOODON03414460 {

}
OboFOODON03414494 {

}
OboFOODON03414741 {

}
OboFOODON03414742 {

}
OboFOODON03414745 {

}
OboFOODON03414934 {

}
OboFOODON03414972 {

}
OboFOODON03420101 {

}
OboFOODON03420106 {

}
OboFOODON03420116 {
    string rdfs_label  
}
OboFOODON03420122 {

}
OboFOODON03420127 {

}
OboFOODON03420129 {

}
OboFOODON03420144 {

}
OboFOODON03420145 {

}
OboFOODON03420147 {
    string rdfs_label  
}
OboFOODON03420148 {

}
OboFOODON03420150 {
    string rdfs_label  
}
OboFOODON03420164 {

}
OboFOODON03420173 {

}
OboFOODON03420181 {
    string rdfs_label  
}
OboFOODON03420183 {

}
OboFOODON03420194 {
    string rdfs_label  
}
OboFOODON03420202 {

}
OboFOODON03420218 {

}
OboFOODON03420238 {

}
OboFOODON03420239 {

}
OboFOODON03460177 {

}
OboFOODON03602002 {

}
OboNCBITaxon1003242 {

}
OboNCBITaxon1003875 {

}
OboNCBITaxon1003877 {

}
OboNCBITaxon10184 {

}
OboNCBITaxon102804 {

}
OboNCBITaxon102809 {

}
OboNCBITaxon102810 {

}
OboNCBITaxon102812 {

}
OboNCBITaxon102814 {

}
OboNCBITaxon102818 {

}
OboNCBITaxon109170 {

}
OboNCBITaxon1110380 {

}
OboNCBITaxon1110386 {

}
OboNCBITaxon112818 {

}
OboNCBITaxon115479 {

}
OboNCBITaxon117571 {

}
OboNCBITaxon1176516 {

}
OboNCBITaxon1184124 {

}
OboNCBITaxon119950 {

}
OboNCBITaxon120289 {

}
OboNCBITaxon1203511 {

}
OboNCBITaxon123366 {

}
OboNCBITaxon123368 {

}
OboNCBITaxon123369 {

}
OboNCBITaxon125009 {

}
OboNCBITaxon126735 {
    string rdfs_label  
    string http___w3id.org_sawgraph_v1_us_wqp#rank  
}
OboNCBITaxon128017 {

}
OboNCBITaxon1307774 {

}
OboNCBITaxon1307775 {

}
OboNCBITaxon1307796 {

}
OboNCBITaxon1308840 {

}
OboNCBITaxon13105 {

}
OboNCBITaxon13106 {
    string rdfs_label  
    string http___w3id.org_sawgraph_v1_us_wqp#rank  
}
OboNCBITaxon1329799 {

}
OboNCBITaxon13336 {

}
OboNCBITaxon1338369 {

}
OboNCBITaxon13424 {

}
OboNCBITaxon13426 {

}
OboNCBITaxon13492 {

}
OboNCBITaxon13749 {

}
OboNCBITaxon1437010 {

}
OboNCBITaxon1437180 {

}
OboNCBITaxon1437183 {

}
OboNCBITaxon1437197 {

}
OboNCBITaxon1437201 {

}
OboNCBITaxon144561 {

}
OboNCBITaxon1463138 {

}
OboNCBITaxon147366 {

}
OboNCBITaxon147368 {

}
OboNCBITaxon147369 {

}
OboNCBITaxon147370 {

}
OboNCBITaxon147389 {

}
OboNCBITaxon147429 {

}
OboNCBITaxon147949 {
    string rdfs_label  
    string http___w3id.org_sawgraph_v1_us_wqp#rank  
}
OboNCBITaxon1489341 {

}
OboNCBITaxon1489388 {

}
OboNCBITaxon1489793 {

}
OboNCBITaxon1489872 {

}
OboNCBITaxon1489922 {

}
OboNCBITaxon1489923 {

}
OboNCBITaxon1489940 {

}
OboNCBITaxon15105 {

}
OboNCBITaxon151069 {

}
OboNCBITaxon151071 {

}
OboNCBITaxon1521262 {

}
OboNCBITaxon1538097 {

}
OboNCBITaxon1545897 {

}
OboNCBITaxon154810 {

}
OboNCBITaxon154811 {
    string rdfs_label  
    string http___w3id.org_sawgraph_v1_us_wqp#rank  
}
OboNCBITaxon1549675 {

}
OboNCBITaxon156152 {

}
OboNCBITaxon1589896 {

}
OboNCBITaxon159053 {

}
OboNCBITaxon1609961 {

}
OboNCBITaxon1609962 {

}
OboNCBITaxon162743 {

}
OboNCBITaxon163487 {

}
OboNCBITaxon16360 {

}
OboNCBITaxon163735 {

}
OboNCBITaxon163743 {

}
OboNCBITaxon1648004 {

}
OboNCBITaxon1648017 {

}
OboNCBITaxon1648033 {

}
OboNCBITaxon165297 {

}
OboNCBITaxon169617 {

}
OboNCBITaxon169618 {

}
OboNCBITaxon169642 {

}
OboNCBITaxon169655 {

}
OboNCBITaxon169697 {

}
OboNCBITaxon169700 {

}
OboNCBITaxon169703 {

}
OboNCBITaxon169705 {

}
OboNCBITaxon169725 {

}
OboNCBITaxon169733 {

}
OboNCBITaxon169746 {

}
OboNCBITaxon1699513 {

}
OboNCBITaxon1699523 {

}
OboNCBITaxon17047 {

}
OboNCBITaxon1705104 {

}
OboNCBITaxon171637 {

}
OboNCBITaxon171638 {

}
OboNCBITaxon1728959 {

}
OboNCBITaxon173691 {

}
OboNCBITaxon174217 {

}
OboNCBITaxon178174 {

}
OboNCBITaxon180118 {

}
OboNCBITaxon1804623 {

}
OboNCBITaxon181185 {

}
OboNCBITaxon183218 {

}
OboNCBITaxon184451 {
    string rdfs_label  
    string http___w3id.org_sawgraph_v1_us_wqp#rank  
}
OboNCBITaxon186265 {

}
OboNCBITaxon186623 {

}
OboNCBITaxon186625 {

}
OboNCBITaxon186626 {

}
OboNCBITaxon186628 {

}
OboNCBITaxon186634 {

}
OboNCBITaxon1874399 {

}
OboNCBITaxon19205 {

}
OboNCBITaxon1927087 {

}
OboNCBITaxon193297 {

}
OboNCBITaxon194251 {

}
OboNCBITaxon1968271 {

}
OboNCBITaxon1968429 {

}
OboNCBITaxon1977918 {

}
OboNCBITaxon198777 {

}
OboNCBITaxon19955 {

}
OboNCBITaxon201017 {

}
OboNCBITaxon214693 {

}
OboNCBITaxon214697 {

}
OboNCBITaxon21472 {

}
OboNCBITaxon214907 {

}
OboNCBITaxon214908 {

}
OboNCBITaxon214929 {

}
OboNCBITaxon215450 {

}
OboNCBITaxon21563 {

}
OboNCBITaxon21571 {

}
OboNCBITaxon216703 {

}
OboNCBITaxon217033 {

}
OboNCBITaxon217035 {

}
OboNCBITaxon217037 {

}
OboNCBITaxon217062 {

}
OboNCBITaxon219121 {

}
OboNCBITaxon219134 {

}
OboNCBITaxon221251 {

}
OboNCBITaxon22140 {

}
OboNCBITaxon2231382 {

}
OboNCBITaxon2231383 {

}
OboNCBITaxon2231390 {

}
OboNCBITaxon2231393 {

}
OboNCBITaxon2233838 {

}
OboNCBITaxon2233839 {

}
OboNCBITaxon2233855 {

}
OboNCBITaxon2233857 {

}
OboNCBITaxon225060 {
    string rdfs_label  
    string http___w3id.org_sawgraph_v1_us_wqp#rank  
}
OboNCBITaxon225388 {

}
OboNCBITaxon225389 {
    string rdfs_label  
    string http___w3id.org_sawgraph_v1_us_wqp#rank  
}
OboNCBITaxon22663 {

}
OboNCBITaxon22665 {

}
OboNCBITaxon22774 {

}
OboNCBITaxon22973 {

}
OboNCBITaxon22978 {

}
OboNCBITaxon2304100 {

}
OboNCBITaxon23066 {

}
OboNCBITaxon23139 {

}
OboNCBITaxon23216 {

}
OboNCBITaxon23222 {

}
OboNCBITaxon232347 {

}
OboNCBITaxon233713 {

}
OboNCBITaxon233715 {

}
OboNCBITaxon233880 {

}
OboNCBITaxon23461 {

}
OboNCBITaxon23513 {

}
OboNCBITaxon235595 {

}
OboNCBITaxon23672 {

}
OboNCBITaxon23808 {

}
OboNCBITaxon241778 {

}
OboNCBITaxon241780 {

}
OboNCBITaxon241789 {

}
OboNCBITaxon241793 {

}
OboNCBITaxon241799 {

}
OboNCBITaxon241800 {

}
OboNCBITaxon241806 {

}
OboNCBITaxon245205 {

}
OboNCBITaxon24646 {

}
OboNCBITaxon24663 {

}
OboNCBITaxon24966 {

}
OboNCBITaxon259381 {

}
OboNCBITaxon25996 {

}
OboNCBITaxon260143 {

}
OboNCBITaxon260718 {

}
OboNCBITaxon26468 {

}
OboNCBITaxon26496 {

}
OboNCBITaxon26867 {

}
OboNCBITaxon2706 {

}
OboNCBITaxon2732585 {

}
OboNCBITaxon2759 {

}
OboNCBITaxon27592 {

}
OboNCBITaxon27705 {

}
OboNCBITaxon27706 {
    string rdfs_label  
    string http___w3id.org_sawgraph_v1_us_wqp#rank  
}
OboNCBITaxon27778 {
    string rdfs_label  
    string http___w3id.org_sawgraph_v1_us_wqp#rank  
}
OboNCBITaxon278205 {

}
OboNCBITaxon2785011 {

}
OboNCBITaxon2785015 {

}
OboNCBITaxon283033 {

}
OboNCBITaxon283036 {
    string rdfs_label  
    string http___w3id.org_sawgraph_v1_us_wqp#rank  
}
OboNCBITaxon284555 {

}
OboNCBITaxon28974 {

}
OboNCBITaxon2908833 {

}
OboNCBITaxon290983 {

}
OboNCBITaxon29132 {

}
OboNCBITaxon296036 {

}
OboNCBITaxon2976026 {

}
OboNCBITaxon29780 {

}
OboNCBITaxon301453 {

}
OboNCBITaxon301959 {

}
OboNCBITaxon303185 {

}
OboNCBITaxon30870 {

}
OboNCBITaxon314145 {

}
OboNCBITaxon314146 {

}
OboNCBITaxon314147 {

}
OboNCBITaxon32443 {

}
OboNCBITaxon32519 {

}
OboNCBITaxon32523 {

}
OboNCBITaxon32524 {

}
OboNCBITaxon32525 {

}
OboNCBITaxon32561 {

}
OboNCBITaxon3268 {

}
OboNCBITaxon3275 {

}
OboNCBITaxon3282 {

}
OboNCBITaxon3296 {

}
OboNCBITaxon3297 {

}
OboNCBITaxon33090 {

}
OboNCBITaxon33154 {

}
OboNCBITaxon33208 {

}
OboNCBITaxon33213 {

}
OboNCBITaxon33317 {

}
OboNCBITaxon33511 {

}
OboNCBITaxon3394 {

}
OboNCBITaxon3395 {

}
OboNCBITaxon3398 {

}
OboNCBITaxon3400 {

}
OboNCBITaxon3440 {

}
OboNCBITaxon34542 {

}
OboNCBITaxon3465 {

}
OboNCBITaxon3468 {

}
OboNCBITaxon34815 {

}
OboNCBITaxon34816 {
    string rdfs_label  
    string http___w3id.org_sawgraph_v1_us_wqp#rank  
}
OboNCBITaxon3487 {

}
OboNCBITaxon3488 {

}
OboNCBITaxon3489 {

}
OboNCBITaxon3493 {

}
OboNCBITaxon3497 {

}
OboNCBITaxon3499 {

}
OboNCBITaxon3524 {

}
OboNCBITaxon3542 {

}
OboNCBITaxon35500 {

}
OboNCBITaxon3558 {

}
OboNCBITaxon3563 {

}
OboNCBITaxon3564 {

}
OboNCBITaxon3568 {

}
OboNCBITaxon3587 {

}
OboNCBITaxon359160 {

}
OboNCBITaxon3593 {

}
OboNCBITaxon3602 {

}
OboNCBITaxon3603 {

}
OboNCBITaxon3608 {

}
OboNCBITaxon3615 {

}
OboNCBITaxon3618 {

}
OboNCBITaxon3620 {

}
OboNCBITaxon3623 {

}
OboNCBITaxon3624 {

}
OboNCBITaxon3629 {

}
OboNCBITaxon3640 {

}
OboNCBITaxon364270 {

}
OboNCBITaxon3646 {

}
OboNCBITaxon3647 {

}
OboNCBITaxon3649 {

}
OboNCBITaxon3650 {

}
OboNCBITaxon3653 {

}
OboNCBITaxon3655 {

}
OboNCBITaxon3660 {

}
OboNCBITaxon36603 {

}
OboNCBITaxon36609 {

}
OboNCBITaxon3669 {

}
OboNCBITaxon3671 {

}
OboNCBITaxon3676 {

}
OboNCBITaxon3683 {

}
OboNCBITaxon3684 {

}
OboNCBITaxon3688 {

}
OboNCBITaxon3699 {

}
OboNCBITaxon3700 {

}
OboNCBITaxon3705 {

}
OboNCBITaxon3707 {

}
OboNCBITaxon3737 {

}
OboNCBITaxon3740 {

}
OboNCBITaxon3744 {

}
OboNCBITaxon3745 {

}
OboNCBITaxon3746 {

}
OboNCBITaxon3749 {

}
OboNCBITaxon3754 {

}
OboNCBITaxon3766 {

}
OboNCBITaxon3801 {

}
OboNCBITaxon3803 {

}
OboNCBITaxon3804 {

}
OboNCBITaxon3807 {

}
OboNCBITaxon381124 {
    string rdfs_label  
}
OboNCBITaxon3814 {

}
OboNCBITaxon3822 {

}
OboNCBITaxon3853 {

}
OboNCBITaxon38820 {

}
OboNCBITaxon3883 {

}
OboNCBITaxon3884 {

}
OboNCBITaxon3885 {

}
OboNCBITaxon3904 {

}
OboNCBITaxon3906 {

}
OboNCBITaxon3913 {

}
OboNCBITaxon3917 {

}
OboNCBITaxon3928 {

}
OboNCBITaxon3931 {

}
OboNCBITaxon4011 {

}
OboNCBITaxon4014 {

}
OboNCBITaxon4018 {

}
OboNCBITaxon4019 {

}
OboNCBITaxon4020 {

}
OboNCBITaxon4033 {

}
OboNCBITaxon4037 {

}
OboNCBITaxon4038 {

}
OboNCBITaxon4039 {

}
OboNCBITaxon40548 {

}
OboNCBITaxon4055 {

}
OboNCBITaxon4056 {

}
OboNCBITaxon40674 {

}
OboNCBITaxon40685 {

}
OboNCBITaxon4069 {

}
OboNCBITaxon4070 {

}
OboNCBITaxon4071 {

}
OboNCBITaxon4072 {

}
OboNCBITaxon4107 {

}
OboNCBITaxon4113 {

}
OboNCBITaxon4118 {

}
OboNCBITaxon4119 {

}
OboNCBITaxon4136 {

}
OboNCBITaxon4143 {

}
OboNCBITaxon4144 {

}
OboNCBITaxon41665 {

}
OboNCBITaxon41705 {

}
OboNCBITaxon41768 {

}
OboNCBITaxon41773 {

}
OboNCBITaxon41937 {

}
OboNCBITaxon41938 {

}
OboNCBITaxon41944 {

}
OboNCBITaxon41945 {

}
OboNCBITaxon41946 {

}
OboNCBITaxon41947 {

}
OboNCBITaxon4199 {

}
OboNCBITaxon4200 {

}
OboNCBITaxon4201 {

}
OboNCBITaxon4204 {

}
OboNCBITaxon4206 {

}
OboNCBITaxon4210 {

}
OboNCBITaxon42148 {

}
OboNCBITaxon4216 {

}
OboNCBITaxon42219 {

}
OboNCBITaxon4231 {

}
OboNCBITaxon4235 {

}
OboNCBITaxon424551 {

}
OboNCBITaxon424573 {

}
OboNCBITaxon426106 {

}
OboNCBITaxon4268 {

}
OboNCBITaxon4281 {

}
OboNCBITaxon4294 {

}
OboNCBITaxon432663 {

}
OboNCBITaxon4335 {

}
OboNCBITaxon4345 {

}
OboNCBITaxon43690 {

}
OboNCBITaxon43707 {

}
OboNCBITaxon43860 {

}
OboNCBITaxon4410 {

}
OboNCBITaxon4447 {

}
OboNCBITaxon4454 {

}
OboNCBITaxon4479 {

}
OboNCBITaxon4577 {

}
OboNCBITaxon4581 {

}
OboNCBITaxon45918 {

}
OboNCBITaxon4609 {

}
OboNCBITaxon4610 {

}
OboNCBITaxon4613 {

}
OboNCBITaxon46145 {

}
OboNCBITaxon4615 {

}
OboNCBITaxon4618 {

}
OboNCBITaxon46259 {
    string rdfs_label  
    string http___w3id.org_sawgraph_v1_us_wqp#rank  
}
OboNCBITaxon46260 {

}
OboNCBITaxon4637 {

}
OboNCBITaxon4638 {

}
OboNCBITaxon4639 {

}
OboNCBITaxon4640 {

}
OboNCBITaxon4641 {

}
OboNCBITaxon4642 {

}
OboNCBITaxon4668 {

}
OboNCBITaxon4671 {

}
OboNCBITaxon4678 {

}
OboNCBITaxon4710 {

}
OboNCBITaxon4719 {

}
OboNCBITaxon4731 {

}
OboNCBITaxon4732 {

}
OboNCBITaxon4734 {

}
OboNCBITaxon47605 {

}
OboNCBITaxon479623 {

}
OboNCBITaxon50173 {

}
OboNCBITaxon50174 {

}
OboNCBITaxon50190 {

}
OboNCBITaxon50384 {

}
OboNCBITaxon504568 {

}
OboNCBITaxon50457 {

}
OboNCBITaxon516948 {

}
OboNCBITaxon51952 {

}
OboNCBITaxon52838 {

}
OboNCBITaxon53868 {

}
OboNCBITaxon54476 {

}
OboNCBITaxon557010 {

}
OboNCBITaxon55961 {

}
OboNCBITaxon57918 {

}
OboNCBITaxon58023 {

}
OboNCBITaxon58024 {

}
OboNCBITaxon58228 {

}
OboNCBITaxon58486 {

}
OboNCBITaxon58860 {

}
OboNCBITaxon59165 {

}
OboNCBITaxon6072 {

}
OboNCBITaxon641307 {

}
OboNCBITaxon6447 {

}
OboNCBITaxon6544 {

}
OboNCBITaxon6545 {

}
OboNCBITaxon6547 {

}
OboNCBITaxon6548 {

}
OboNCBITaxon6550 {
    string rdfs_label  
    string http___w3id.org_sawgraph_v1_us_wqp#rank  
}
OboNCBITaxon6599 {

}
OboNCBITaxon6602 {

}
OboNCBITaxon6604 {
    string rdfs_label  
    string http___w3id.org_sawgraph_v1_us_wqp#rank  
}
OboNCBITaxon6605 {

}
OboNCBITaxon6606 {

}
OboNCBITaxon66670 {

}
OboNCBITaxon66672 {

}
OboNCBITaxon66912 {
    string rdfs_label  
    string http___w3id.org_sawgraph_v1_us_wqp#rank  
}
OboNCBITaxon66913 {
    string rdfs_label  
    string http___w3id.org_sawgraph_v1_us_wqp#rank  
}
OboNCBITaxon69108 {

}
OboNCBITaxon69109 {

}
OboNCBITaxon693794 {

}
OboNCBITaxon703407 {

}
OboNCBITaxon71243 {

}
OboNCBITaxon71274 {

}
OboNCBITaxon71275 {

}
OboNCBITaxon71611 {

}
OboNCBITaxon72025 {

}
OboNCBITaxon72171 {

}
OboNCBITaxon721789 {

}
OboNCBITaxon721813 {

}
OboNCBITaxon73496 {

}
OboNCBITaxon742010 {

}
OboNCBITaxon745060 {

}
OboNCBITaxon75287 {

}
OboNCBITaxon75288 {
    string rdfs_label  
    string http___w3id.org_sawgraph_v1_us_wqp#rank  
}
OboNCBITaxon7711 {

}
OboNCBITaxon7742 {

}
OboNCBITaxon7776 {

}
OboNCBITaxon78536 {

}
OboNCBITaxon7898 {

}
OboNCBITaxon79331 {

}
OboNCBITaxon7952 {

}
OboNCBITaxon7968 {

}
OboNCBITaxon7969 {

}
OboNCBITaxon7971 {
    string rdfs_label  
    string http___w3id.org_sawgraph_v1_us_wqp#rank  
}
OboNCBITaxon7995 {

}
OboNCBITaxon7996 {

}
OboNCBITaxon7997 {

}
OboNCBITaxon7998 {
    string rdfs_label  
    string http___w3id.org_sawgraph_v1_us_wqp#rank  
}
OboNCBITaxon8006 {

}
OboNCBITaxon8007 {

}
OboNCBITaxon8008 {

}
OboNCBITaxon8009 {

}
OboNCBITaxon8010 {
    string rdfs_label  
}
OboNCBITaxon8015 {

}
OboNCBITaxon8016 {

}
OboNCBITaxon8022 {
    string rdfs_label  
    string http___w3id.org_sawgraph_v1_us_wqp#rank  
}
OboNCBITaxon8028 {

}
OboNCBITaxon8032 {
    string rdfs_label  
    string http___w3id.org_sawgraph_v1_us_wqp#rank  
}
OboNCBITaxon8033 {

}
OboNCBITaxon8038 {
    string rdfs_label  
    string http___w3id.org_sawgraph_v1_us_wqp#rank  
}
OboNCBITaxon8111 {

}
OboNCBITaxon8112 {

}
OboNCBITaxon8165 {

}
OboNCBITaxon8166 {

}
OboNCBITaxon8167 {
    string rdfs_label  
    string http___w3id.org_sawgraph_v1_us_wqp#rank  
}
OboNCBITaxon8180 {

}
OboNCBITaxon8181 {

}
OboNCBITaxon8182 {
    string rdfs_label  
}
OboNCBITaxon83431 {

}
OboNCBITaxon84005 {

}
OboNCBITaxon84860 {

}
OboNCBITaxon8492 {

}
OboNCBITaxon85249 {

}
OboNCBITaxon85571 {

}
OboNCBITaxon866800 {

}
OboNCBITaxon8782 {

}
OboNCBITaxon8825 {

}
OboNCBITaxon89151 {

}
OboNCBITaxon8976 {

}
OboNCBITaxon9005 {

}
OboNCBITaxon9031 {

}
OboNCBITaxon9072 {

}
OboNCBITaxon9102 {

}
OboNCBITaxon9103 {

}
OboNCBITaxon911341 {

}
OboNCBITaxon91561 {

}
OboNCBITaxon91835 {

}
OboNCBITaxon91836 {

}
OboNCBITaxon91882 {

}
OboNCBITaxon91888 {

}
OboNCBITaxon9347 {

}
OboNCBITaxon96479 {

}
OboNCBITaxon980193 {

}
OboNCBITaxon981071 {

}
OboNCBITaxon9821 {

}
OboNCBITaxon9823 {

}
OboNCBITaxon9825 {

}
OboNCBITaxon9850 {

}
OboNCBITaxon986140 {

}
OboNCBITaxon9895 {

}
OboNCBITaxon9900 {

}
OboNCBITaxon9903 {

}
OboNCBITaxon9913 {

}
OboNCBITaxon9922 {

}
OboNCBITaxon9925 {

}
OboNCBITaxon9935 {

}
OboNCBITaxon9940 {

}
OboNCBITaxon99568 {

}
OboNCBITaxon9963 {

}
OboNCBITaxon9989 {

}
OboOBI0100026 {

}
OboPO0000003 {

}
OboPO0025034 {

}
OboUBERON0000948 {

}
OboUBERON0001913 {

}
OboUBERON0002097 {

}
OboUBERON0002107 {

}
OboUBERON0005079 {

}
OboUBERON0007378 {

}
OboUBERON0007379 {

}
OboUBERON0008944 {

}
QudtEnumeratedQuantity {

}
SosaProcedure {

}
SosaProperty {

}
SosaSample {

}
StadDataTransformation {

}
StadDataValue {

}
StadDatapoint {

}
StadQualityKind {

}
StadQuantity {

}
StadSingleData {

}
StadStatisticalAggregateData {

}
StadStatisticalQuantityKind {

}
XsdAnyURI {

}

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
B00af777bec4da87c5aebb51d94b2d478 ||--|o RdfsLiteral : "rdfs_label"
B00af777bec4da87c5aebb51d94b2d478 ||--|o OwlThing : "owl_sameAs"
B036a3008450d6ce37e35cf5a98355a60 ||--|o RdfsLiteral : "rdfs_label"
B036a3008450d6ce37e35cf5a98355a60 ||--|o OwlThing : "obo_RO_0002162"
B036a3008450d6ce37e35cf5a98355a60 ||--|o OwlClass : "obo_RO_0002162"
B036a3008450d6ce37e35cf5a98355a60 ||--|o OwlThing : "owl_sameAs"
B085dcda89ed6aae0d3b229e767f0a1ca ||--|o RdfsLiteral : "rdfs_label"
B085dcda89ed6aae0d3b229e767f0a1ca ||--|o OwlThing : "owl_sameAs"
B0d427a711311f1499a234aa8af2c66d1 ||--|o RdfsLiteral : "rdfs_label"
B0d427a711311f1499a234aa8af2c66d1 ||--|o OwlThing : "owl_sameAs"
B215b3a432e1c482d3680398a554edbbf ||--|o RdfsLiteral : "rdfs_label"
B215b3a432e1c482d3680398a554edbbf ||--|o OwlThing : "owl_sameAs"
B27231c83f17c76e178e0c9f5e10acc55 ||--|o RdfsLiteral : "rdfs_label"
B27231c83f17c76e178e0c9f5e10acc55 ||--|o OwlThing : "owl_sameAs"
B37977f50d3140da51a9630b8a57396a1 ||--|o RdfsLiteral : "rdfs_label"
B37977f50d3140da51a9630b8a57396a1 ||--|o OwlThing : "owl_sameAs"
B3cc7b3721547b07a4068dc98b6444b8b ||--|o RdfsLiteral : "rdfs_label"
B3cc7b3721547b07a4068dc98b6444b8b ||--|o OwlThing : "owl_sameAs"
B423a0e253807f20386fc3ccbbd7e0378 ||--|o RdfsLiteral : "rdfs_label"
B423a0e253807f20386fc3ccbbd7e0378 ||--|o OwlThing : "owl_sameAs"
B44bec873efc8b96cad5f525429c64e0a ||--|o RdfsLiteral : "rdfs_label"
B44bec873efc8b96cad5f525429c64e0a ||--|o OwlThing : "owl_sameAs"
B4fd286b2a5a12e342d61412628b6e4c2 ||--|o RdfsLiteral : "rdfs_label"
B4fd286b2a5a12e342d61412628b6e4c2 ||--|o OwlThing : "owl_sameAs"
B53622dee107de372b2d0566f64ab6e3a ||--|o RdfsLiteral : "rdfs_label"
B53622dee107de372b2d0566f64ab6e3a ||--|o OwlThing : "owl_sameAs"
B5e93e815b548435105d9273d424fa0e8 ||--|o RdfsLiteral : "rdfs_label"
B5e93e815b548435105d9273d424fa0e8 ||--|o OwlThing : "owl_sameAs"
B611b8dff312692e7f32a69834c787a60 ||--|o RdfsLiteral : "rdfs_label"
B611b8dff312692e7f32a69834c787a60 ||--|o OwlThing : "owl_sameAs"
B623b56ef58fd82dd088819e22d655c08 ||--|o RdfsLiteral : "rdfs_label"
B623b56ef58fd82dd088819e22d655c08 ||--|o OwlThing : "owl_sameAs"
B75dbc5841338872cea35dced609fcd77 ||--|o RdfsLiteral : "rdfs_label"
B75dbc5841338872cea35dced609fcd77 ||--|o OwlThing : "owl_sameAs"
B75e45ed04b2b903b9029968cada06faa ||--|o RdfsLiteral : "rdfs_label"
B75e45ed04b2b903b9029968cada06faa ||--|o OwlThing : "owl_sameAs"
B7728f65369357f97de36b133c9d1d5e0 ||--|o RdfsLiteral : "rdfs_label"
B7728f65369357f97de36b133c9d1d5e0 ||--|o OwlThing : "owl_sameAs"
B8aa8791a0418cd594c8b56ad21351f72 ||--|o RdfsLiteral : "rdfs_label"
B8aa8791a0418cd594c8b56ad21351f72 ||--|o OwlThing : "owl_sameAs"
Ba6d85f816540f9fec5b71ba42fc2cca6 ||--|o RdfsLiteral : "rdfs_label"
Ba6d85f816540f9fec5b71ba42fc2cca6 ||--|o OwlThing : "owl_sameAs"
Ba76635ffb4afc02e78b9ef49973d089f ||--|o RdfsLiteral : "dct_identifier"
Ba76635ffb4afc02e78b9ef49973d089f ||--|o OwlThing : "owl_sameAs"
Ba76635ffb4afc02e78b9ef49973d089f ||--|o RdfsLiteral : "rdfs_label"
Bb0125be5bc4dc7be7e8452e7d22445f6 ||--|o RdfsLiteral : "rdfs_label"
Bb0125be5bc4dc7be7e8452e7d22445f6 ||--|o OwlThing : "owl_sameAs"
Bb71af62f2f3e5e5b5e0fe81f24eca409 ||--|o RdfsLiteral : "rdfs_label"
Bb71af62f2f3e5e5b5e0fe81f24eca409 ||--|o OwlThing : "owl_sameAs"
Bbefc37cbdd03cae92dadef76b34dbf16 ||--|o RdfsLiteral : "rdfs_label"
Bbefc37cbdd03cae92dadef76b34dbf16 ||--|o OwlThing : "owl_sameAs"
Bbf63deb85414ddecd89e46bce27e7f0a ||--|o RdfsLiteral : "rdfs_label"
Bbf63deb85414ddecd89e46bce27e7f0a ||--|o OwlThing : "owl_sameAs"
Be047d68edc8eb3ce96d7edbad5217bfc ||--|o RdfsLiteral : "rdfs_label"
Be047d68edc8eb3ce96d7edbad5217bfc ||--|o OwlThing : "owl_sameAs"
Be497d3b0c2656040c05e303873a2d541 ||--|o RdfsLiteral : "rdfs_label"
Be497d3b0c2656040c05e303873a2d541 ||--|o OwlThing : "owl_sameAs"
Beb7217b5b32080b9606028314249e33b ||--|o HttpW3id.orgComptoxV1ChemicalEntity : "http___w3id.org_comptox_v1_sameAsComptoxSubstance"
Beb7217b5b32080b9606028314249e33b ||--|o RdfsLiteral : "dct_identifier"
Beb7217b5b32080b9606028314249e33b ||--|o OwlThing : "owl_sameAs"
Beb7217b5b32080b9606028314249e33b ||--|o OwlThing : "http___w3id.org_comptox_sameAsComptoxSubstance"
Beb7217b5b32080b9606028314249e33b ||--|o HttpW3id.orgComptoxCompToxChemicalEntity : "http___w3id.org_comptox_sameAsComptoxSubstance"
Beb7217b5b32080b9606028314249e33b ||--|o CosoSubstance : "http___w3id.org_comptox_sameAsComptoxSubstance"
Beb7217b5b32080b9606028314249e33b ||--|o Beb7217b5b32080b9606028314249e33b : "http___w3id.org_comptox_sameAsComptoxSubstance"
Beb7217b5b32080b9606028314249e33b ||--|o RdfsLiteral : "rdfs_label"
Beb7217b5b32080b9606028314249e33b ||--|o OwlNamedIndividual : "coso_hasMember"
Beb7217b5b32080b9606028314249e33b ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-ParameterName : "coso_hasMember"
Beb7217b5b32080b9606028314249e33b ||--|o Beb7217b5b32080b9606028314249e33b : "coso_hasMember"
Beb77c26f8c395403edc359fd5f6dfb28 ||--|o RdfsLiteral : "rdfs_label"
Beb77c26f8c395403edc359fd5f6dfb28 ||--|o OwlThing : "obo_RO_0002162"
Beb77c26f8c395403edc359fd5f6dfb28 ||--|o OwlClass : "obo_RO_0002162"
Beb77c26f8c395403edc359fd5f6dfb28 ||--|o OwlThing : "owl_sameAs"
Bf04685c17c0e71ae3c98e08c75cbdfcc ||--|o RdfsLiteral : "rdfs_label"
Bf04685c17c0e71ae3c98e08c75cbdfcc ||--|o OwlThing : "owl_sameAs"
Bf584e1bfd1c74de0eb37e7b926538b83 ||--|o RdfsLiteral : "rdfs_label"
Bf584e1bfd1c74de0eb37e7b926538b83 ||--|o OwlThing : "owl_sameAs"
CosoAnimalBloodSample ||--|o CosoSampledFeature : "coso_isSampleOf"
CosoAnimalBloodSample ||--|o GeoFeature : "coso_isSampleOf"
CosoAnimalBloodSample ||--|o OwlThing : "coso_isSampleOf"
CosoAnimalBloodSample ||--|o CosoFeature : "coso_isSampleOf"
CosoAnimalBloodSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampledFeature : "coso_isSampleOf"
CosoAnimalBloodSample ||--|o SosaFeatureOfInterest : "coso_isSampleOf"
CosoAnimalBloodSample ||--|o GeoSpatialObject : "coso_isSampleOf"
CosoAnimalBloodSample ||--|o MeEgadEGAD-SampleCollectionMethod : "coso_sampleAnnotation"
CosoAnimalBloodSample ||--|o OwlNamedIndividual : "coso_sampleAnnotation"
CosoAnimalBloodSample ||--|o MeEgadEGAD-SampleDetailedLocation : "coso_sampleAnnotation"
CosoAnimalBloodSample ||--|o CosoSampleAnnotation : "coso_sampleAnnotation"
CosoAnimalBloodSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleDetailedLocation : "coso_sampleAnnotation"
CosoAnimalBloodSample ||--|o MeEgadEGAD-SampleTreatmentStatus : "coso_sampleAnnotation"
CosoAnimalBloodSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleTreatmentStatus : "coso_sampleAnnotation"
CosoAnimalBloodSample ||--|o OwlThing : "coso_sampleAnnotation"
CosoAnimalBloodSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleCollectionMethod : "coso_sampleAnnotation"
CosoAnimalBloodSample ||--|o OwlThing : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionMethod"
CosoAnimalBloodSample ||--|o OwlNamedIndividual : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionMethod"
CosoAnimalBloodSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleCollectionMethod : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionMethod"
CosoAnimalBloodSample ||--|o CosoSampleAnnotation : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionMethod"
CosoAnimalBloodSample ||--|o RdfsLiteral : "dct_identifier"
CosoAnimalBloodSample ||--|o OwlThing : "owl_sameAs"
CosoAnimalBloodSample ||--|o RdfsLiteral : "rdfs_label"
CosoAnimalBloodSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampledFeature : "sosa_isSampleOf"
CosoAnimalBloodSample ||--|o OboFOODON03411183 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboFOODON03411057 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboNCBITaxon283036 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboFOODON02010107 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o HttpW3id.orgSawgraphV1Us-wqp#SampleMedia : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboFOODON00003572 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o B37977f50d3140da51a9630b8a57396a1 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboFOODON03420147 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o B215b3a432e1c482d3680398a554edbbf : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o MeEgadEGAD-SampleMaterialTypeQualifier : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o B036a3008450d6ce37e35cf5a98355a60 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboNCBITaxon66912 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboNCBITaxon7971 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboFOODON03411566 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboFOODON03420194 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboNCBITaxon381124 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o Bf584e1bfd1c74de0eb37e7b926538b83 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboFOODON00001093 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o HttpW3id.orgSawgraphV1Us-wqp#Taxon : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboNCBITaxon8022 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o B44bec873efc8b96cad5f525429c64e0a : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboFOODON00002477 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OwlThing : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o B27231c83f17c76e178e0c9f5e10acc55 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboNCBITaxon6550 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboFOODON02021651 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o Ba6d85f816540f9fec5b71ba42fc2cca6 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o CosoWaterSample : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboNCBITaxon225389 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o B423a0e253807f20386fc3ccbbd7e0378 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o MeEgadEGAD-SampleMaterialType : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboNCBITaxon8182 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboFOODON02010012 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o Bbefc37cbdd03cae92dadef76b34dbf16 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboFOODON03420150 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o B085dcda89ed6aae0d3b229e767f0a1ca : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o Bb0125be5bc4dc7be7e8452e7d22445f6 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o B0d427a711311f1499a234aa8af2c66d1 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboFOODON03411236 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboNCBITaxon6604 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboFOODON03301761 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleMaterialType : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o B7728f65369357f97de36b133c9d1d5e0 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o Be047d68edc8eb3ce96d7edbad5217bfc : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboNCBITaxon8032 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboFOODON03420181 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboFOODON02010045 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboNCBITaxon154811 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboNCBITaxon27778 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o Be497d3b0c2656040c05e303873a2d541 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboFOODON00004460 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o Beb77c26f8c395403edc359fd5f6dfb28 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o B611b8dff312692e7f32a69834c787a60 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboFOODON03411324 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o B75e45ed04b2b903b9029968cada06faa : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboFOODON03420116 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboNCBITaxon225060 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o B75dbc5841338872cea35dced609fcd77 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o CosoSampleMaterialType : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboFOODON00003083 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboNCBITaxon147949 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboFOODON03411325 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboNCBITaxon7998 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboNCBITaxon8010 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o B3cc7b3721547b07a4068dc98b6444b8b : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboNCBITaxon8038 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboNCBITaxon184451 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboFOODON02010015 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o Bbf63deb85414ddecd89e46bce27e7f0a : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboFOODON00004172 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboFOODON03411457 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboNCBITaxon75288 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboFOODON03413378 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboFOODON02010042 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o B4fd286b2a5a12e342d61412628b6e4c2 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o Bf04685c17c0e71ae3c98e08c75cbdfcc : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o B623b56ef58fd82dd088819e22d655c08 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboFOODON00003425 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o B5e93e815b548435105d9273d424fa0e8 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboFOODON00002165 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboFOODON03411669 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o B53622dee107de372b2d0566f64ab6e3a : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboNCBITaxon8167 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboFOODON02020892 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboNCBITaxon27706 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o HttpW3id.orgSawgraphV1Us-wqp#TaxonGroup.FishNekton : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboFOODON00003042 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboFOODON02021803 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboNCBITaxon46259 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboNCBITaxon34816 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleMaterialTypeQualifier : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o Bb71af62f2f3e5e5b5e0fe81f24eca409 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboNCBITaxon66913 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboFOODON03411583 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboFOODON03411328 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboFOODON00004436 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboFOODON02021805 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboFOODON03413358 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboFOODON02010032 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboFOODON02020840 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboNCBITaxon126735 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OwlNamedIndividual : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o OboNCBITaxon13106 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o B8aa8791a0418cd594c8b56ad21351f72 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o B00af777bec4da87c5aebb51d94b2d478 : "coso_sampleOfMaterialType"
CosoAnimalBloodSample ||--|o GeoFeature : "coso_fromSamplePoint"
CosoAnimalBloodSample ||--|o HttpW3id.orgSawgraphV1Us-wqp#Site : "coso_fromSamplePoint"
CosoAnimalBloodSample ||--|o OwlThing : "coso_fromSamplePoint"
CosoAnimalBloodSample ||--|o MeEgadEGAD-SamplePoint : "coso_fromSamplePoint"
CosoAnimalBloodSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint : "coso_fromSamplePoint"
CosoAnimalBloodSample ||--|o GeoSpatialObject : "coso_fromSamplePoint"
CosoAnimalBloodSample ||--|o CosoSamplePoint : "coso_fromSamplePoint"
CosoAnimalBloodSample ||--|o SosaFeatureOfInterest : "coso_fromSamplePoint"
CosoAnimalBloodSample ||--|o CosoPoint : "coso_fromSamplePoint"
CosoAnimalMaterialSample ||--|o CosoSampledFeature : "coso_isSampleOf"
CosoAnimalMaterialSample ||--|o GeoFeature : "coso_isSampleOf"
CosoAnimalMaterialSample ||--|o OwlThing : "coso_isSampleOf"
CosoAnimalMaterialSample ||--|o CosoFeature : "coso_isSampleOf"
CosoAnimalMaterialSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampledFeature : "coso_isSampleOf"
CosoAnimalMaterialSample ||--|o SosaFeatureOfInterest : "coso_isSampleOf"
CosoAnimalMaterialSample ||--|o GeoSpatialObject : "coso_isSampleOf"
CosoAnimalMaterialSample ||--|o MeEgadEGAD-SampleCollectionMethod : "coso_sampleAnnotation"
CosoAnimalMaterialSample ||--|o OwlNamedIndividual : "coso_sampleAnnotation"
CosoAnimalMaterialSample ||--|o MeEgadEGAD-SampleDetailedLocation : "coso_sampleAnnotation"
CosoAnimalMaterialSample ||--|o CosoSampleAnnotation : "coso_sampleAnnotation"
CosoAnimalMaterialSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleDetailedLocation : "coso_sampleAnnotation"
CosoAnimalMaterialSample ||--|o MeEgadEGAD-SampleTreatmentStatus : "coso_sampleAnnotation"
CosoAnimalMaterialSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleTreatmentStatus : "coso_sampleAnnotation"
CosoAnimalMaterialSample ||--|o OwlThing : "coso_sampleAnnotation"
CosoAnimalMaterialSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleCollectionMethod : "coso_sampleAnnotation"
CosoAnimalMaterialSample ||--|o OwlThing : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionMethod"
CosoAnimalMaterialSample ||--|o OwlNamedIndividual : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionMethod"
CosoAnimalMaterialSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleCollectionMethod : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionMethod"
CosoAnimalMaterialSample ||--|o CosoSampleAnnotation : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionMethod"
CosoAnimalMaterialSample ||--|o RdfsLiteral : "dct_identifier"
CosoAnimalMaterialSample ||--|o OwlThing : "owl_sameAs"
CosoAnimalMaterialSample ||--|o ProvAgent : "prov_wasAttributedTo"
CosoAnimalMaterialSample ||--|o RdfsLiteral : "rdfs_label"
CosoAnimalMaterialSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampledFeature : "sosa_isSampleOf"
CosoAnimalMaterialSample ||--|o OboFOODON03411183 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboFOODON03411057 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboNCBITaxon283036 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboFOODON02010107 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o HttpW3id.orgSawgraphV1Us-wqp#SampleMedia : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboFOODON00003572 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o B37977f50d3140da51a9630b8a57396a1 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboFOODON03420147 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o B215b3a432e1c482d3680398a554edbbf : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o MeEgadEGAD-SampleMaterialTypeQualifier : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o B036a3008450d6ce37e35cf5a98355a60 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboNCBITaxon66912 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboNCBITaxon7971 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboFOODON03411566 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboFOODON03420194 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboNCBITaxon381124 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o Bf584e1bfd1c74de0eb37e7b926538b83 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboFOODON00001093 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o HttpW3id.orgSawgraphV1Us-wqp#Taxon : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboNCBITaxon8022 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o B44bec873efc8b96cad5f525429c64e0a : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboFOODON00002477 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OwlThing : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o B27231c83f17c76e178e0c9f5e10acc55 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboNCBITaxon6550 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboFOODON02021651 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o Ba6d85f816540f9fec5b71ba42fc2cca6 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o CosoWaterSample : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboNCBITaxon225389 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o B423a0e253807f20386fc3ccbbd7e0378 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o MeEgadEGAD-SampleMaterialType : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboNCBITaxon8182 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboFOODON02010012 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o Bbefc37cbdd03cae92dadef76b34dbf16 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboFOODON03420150 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o B085dcda89ed6aae0d3b229e767f0a1ca : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o Bb0125be5bc4dc7be7e8452e7d22445f6 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o B0d427a711311f1499a234aa8af2c66d1 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboFOODON03411236 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboNCBITaxon6604 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboFOODON03301761 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleMaterialType : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o B7728f65369357f97de36b133c9d1d5e0 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o Be047d68edc8eb3ce96d7edbad5217bfc : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboNCBITaxon8032 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboFOODON03420181 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboFOODON02010045 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboNCBITaxon154811 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboNCBITaxon27778 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o Be497d3b0c2656040c05e303873a2d541 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboFOODON00004460 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o Beb77c26f8c395403edc359fd5f6dfb28 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o B611b8dff312692e7f32a69834c787a60 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboFOODON03411324 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o B75e45ed04b2b903b9029968cada06faa : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboFOODON03420116 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboNCBITaxon225060 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o B75dbc5841338872cea35dced609fcd77 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o CosoSampleMaterialType : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboFOODON00003083 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboNCBITaxon147949 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboFOODON03411325 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboNCBITaxon7998 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboNCBITaxon8010 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o B3cc7b3721547b07a4068dc98b6444b8b : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboNCBITaxon8038 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboNCBITaxon184451 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboFOODON02010015 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o Bbf63deb85414ddecd89e46bce27e7f0a : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboFOODON00004172 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboFOODON03411457 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboNCBITaxon75288 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboFOODON03413378 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboFOODON02010042 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o B4fd286b2a5a12e342d61412628b6e4c2 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o Bf04685c17c0e71ae3c98e08c75cbdfcc : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o B623b56ef58fd82dd088819e22d655c08 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboFOODON00003425 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o B5e93e815b548435105d9273d424fa0e8 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboFOODON00002165 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboFOODON03411669 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o B53622dee107de372b2d0566f64ab6e3a : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboNCBITaxon8167 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboFOODON02020892 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboNCBITaxon27706 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o HttpW3id.orgSawgraphV1Us-wqp#TaxonGroup.FishNekton : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboFOODON00003042 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboFOODON02021803 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboNCBITaxon46259 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboNCBITaxon34816 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleMaterialTypeQualifier : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o Bb71af62f2f3e5e5b5e0fe81f24eca409 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboNCBITaxon66913 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboFOODON03411583 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboFOODON03411328 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboFOODON00004436 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboFOODON02021805 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboFOODON03413358 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboFOODON02010032 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboFOODON02020840 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboNCBITaxon126735 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OwlNamedIndividual : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o OboNCBITaxon13106 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o B8aa8791a0418cd594c8b56ad21351f72 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o B00af777bec4da87c5aebb51d94b2d478 : "coso_sampleOfMaterialType"
CosoAnimalMaterialSample ||--|o GeoFeature : "coso_fromSamplePoint"
CosoAnimalMaterialSample ||--|o HttpW3id.orgSawgraphV1Us-wqp#Site : "coso_fromSamplePoint"
CosoAnimalMaterialSample ||--|o OwlThing : "coso_fromSamplePoint"
CosoAnimalMaterialSample ||--|o MeEgadEGAD-SamplePoint : "coso_fromSamplePoint"
CosoAnimalMaterialSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint : "coso_fromSamplePoint"
CosoAnimalMaterialSample ||--|o GeoSpatialObject : "coso_fromSamplePoint"
CosoAnimalMaterialSample ||--|o CosoSamplePoint : "coso_fromSamplePoint"
CosoAnimalMaterialSample ||--|o SosaFeatureOfInterest : "coso_fromSamplePoint"
CosoAnimalMaterialSample ||--|o CosoPoint : "coso_fromSamplePoint"
CosoAnimalMilkSample ||--|o CosoSampledFeature : "coso_isSampleOf"
CosoAnimalMilkSample ||--|o GeoFeature : "coso_isSampleOf"
CosoAnimalMilkSample ||--|o OwlThing : "coso_isSampleOf"
CosoAnimalMilkSample ||--|o CosoFeature : "coso_isSampleOf"
CosoAnimalMilkSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampledFeature : "coso_isSampleOf"
CosoAnimalMilkSample ||--|o SosaFeatureOfInterest : "coso_isSampleOf"
CosoAnimalMilkSample ||--|o GeoSpatialObject : "coso_isSampleOf"
CosoAnimalMilkSample ||--|o MeEgadEGAD-SampleCollectionMethod : "coso_sampleAnnotation"
CosoAnimalMilkSample ||--|o OwlNamedIndividual : "coso_sampleAnnotation"
CosoAnimalMilkSample ||--|o MeEgadEGAD-SampleDetailedLocation : "coso_sampleAnnotation"
CosoAnimalMilkSample ||--|o CosoSampleAnnotation : "coso_sampleAnnotation"
CosoAnimalMilkSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleDetailedLocation : "coso_sampleAnnotation"
CosoAnimalMilkSample ||--|o MeEgadEGAD-SampleTreatmentStatus : "coso_sampleAnnotation"
CosoAnimalMilkSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleTreatmentStatus : "coso_sampleAnnotation"
CosoAnimalMilkSample ||--|o OwlThing : "coso_sampleAnnotation"
CosoAnimalMilkSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleCollectionMethod : "coso_sampleAnnotation"
CosoAnimalMilkSample ||--|o OwlThing : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionMethod"
CosoAnimalMilkSample ||--|o OwlNamedIndividual : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionMethod"
CosoAnimalMilkSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleCollectionMethod : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionMethod"
CosoAnimalMilkSample ||--|o CosoSampleAnnotation : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionMethod"
CosoAnimalMilkSample ||--|o RdfsLiteral : "dct_identifier"
CosoAnimalMilkSample ||--|o OwlThing : "owl_sameAs"
CosoAnimalMilkSample ||--|o OwlThing : "http___w3id.org_sawgraph_v1_me-egad#sampleTreatmentStatus"
CosoAnimalMilkSample ||--|o OwlNamedIndividual : "http___w3id.org_sawgraph_v1_me-egad#sampleTreatmentStatus"
CosoAnimalMilkSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleTreatmentStatus : "http___w3id.org_sawgraph_v1_me-egad#sampleTreatmentStatus"
CosoAnimalMilkSample ||--|o CosoSampleAnnotation : "http___w3id.org_sawgraph_v1_me-egad#sampleTreatmentStatus"
CosoAnimalMilkSample ||--|o ProvAgent : "prov_wasAttributedTo"
CosoAnimalMilkSample ||--|o RdfsLiteral : "rdfs_label"
CosoAnimalMilkSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampledFeature : "sosa_isSampleOf"
CosoAnimalMilkSample ||--|o OboFOODON03411183 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboFOODON03411057 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboNCBITaxon283036 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboFOODON02010107 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o HttpW3id.orgSawgraphV1Us-wqp#SampleMedia : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboFOODON00003572 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o B37977f50d3140da51a9630b8a57396a1 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboFOODON03420147 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o B215b3a432e1c482d3680398a554edbbf : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o MeEgadEGAD-SampleMaterialTypeQualifier : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o B036a3008450d6ce37e35cf5a98355a60 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboNCBITaxon66912 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboNCBITaxon7971 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboFOODON03411566 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboFOODON03420194 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboNCBITaxon381124 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o Bf584e1bfd1c74de0eb37e7b926538b83 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboFOODON00001093 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o HttpW3id.orgSawgraphV1Us-wqp#Taxon : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboNCBITaxon8022 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o B44bec873efc8b96cad5f525429c64e0a : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboFOODON00002477 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OwlThing : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o B27231c83f17c76e178e0c9f5e10acc55 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboNCBITaxon6550 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboFOODON02021651 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o Ba6d85f816540f9fec5b71ba42fc2cca6 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o CosoWaterSample : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboNCBITaxon225389 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o B423a0e253807f20386fc3ccbbd7e0378 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o MeEgadEGAD-SampleMaterialType : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboNCBITaxon8182 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboFOODON02010012 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o Bbefc37cbdd03cae92dadef76b34dbf16 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboFOODON03420150 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o B085dcda89ed6aae0d3b229e767f0a1ca : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o Bb0125be5bc4dc7be7e8452e7d22445f6 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o B0d427a711311f1499a234aa8af2c66d1 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboFOODON03411236 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboNCBITaxon6604 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboFOODON03301761 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleMaterialType : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o B7728f65369357f97de36b133c9d1d5e0 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o Be047d68edc8eb3ce96d7edbad5217bfc : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboNCBITaxon8032 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboFOODON03420181 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboFOODON02010045 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboNCBITaxon154811 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboNCBITaxon27778 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o Be497d3b0c2656040c05e303873a2d541 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboFOODON00004460 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o Beb77c26f8c395403edc359fd5f6dfb28 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o B611b8dff312692e7f32a69834c787a60 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboFOODON03411324 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o B75e45ed04b2b903b9029968cada06faa : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboFOODON03420116 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboNCBITaxon225060 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o B75dbc5841338872cea35dced609fcd77 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o CosoSampleMaterialType : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboFOODON00003083 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboNCBITaxon147949 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboFOODON03411325 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboNCBITaxon7998 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboNCBITaxon8010 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o B3cc7b3721547b07a4068dc98b6444b8b : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboNCBITaxon8038 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboNCBITaxon184451 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboFOODON02010015 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o Bbf63deb85414ddecd89e46bce27e7f0a : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboFOODON00004172 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboFOODON03411457 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboNCBITaxon75288 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboFOODON03413378 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboFOODON02010042 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o B4fd286b2a5a12e342d61412628b6e4c2 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o Bf04685c17c0e71ae3c98e08c75cbdfcc : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o B623b56ef58fd82dd088819e22d655c08 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboFOODON00003425 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o B5e93e815b548435105d9273d424fa0e8 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboFOODON00002165 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboFOODON03411669 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o B53622dee107de372b2d0566f64ab6e3a : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboNCBITaxon8167 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboFOODON02020892 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboNCBITaxon27706 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o HttpW3id.orgSawgraphV1Us-wqp#TaxonGroup.FishNekton : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboFOODON00003042 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboFOODON02021803 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboNCBITaxon46259 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboNCBITaxon34816 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleMaterialTypeQualifier : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o Bb71af62f2f3e5e5b5e0fe81f24eca409 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboNCBITaxon66913 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboFOODON03411583 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboFOODON03411328 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboFOODON00004436 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboFOODON02021805 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboFOODON03413358 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboFOODON02010032 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboFOODON02020840 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboNCBITaxon126735 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OwlNamedIndividual : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o OboNCBITaxon13106 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o B8aa8791a0418cd594c8b56ad21351f72 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o B00af777bec4da87c5aebb51d94b2d478 : "coso_sampleOfMaterialType"
CosoAnimalMilkSample ||--|o GeoFeature : "coso_fromSamplePoint"
CosoAnimalMilkSample ||--|o HttpW3id.orgSawgraphV1Us-wqp#Site : "coso_fromSamplePoint"
CosoAnimalMilkSample ||--|o OwlThing : "coso_fromSamplePoint"
CosoAnimalMilkSample ||--|o MeEgadEGAD-SamplePoint : "coso_fromSamplePoint"
CosoAnimalMilkSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint : "coso_fromSamplePoint"
CosoAnimalMilkSample ||--|o GeoSpatialObject : "coso_fromSamplePoint"
CosoAnimalMilkSample ||--|o CosoSamplePoint : "coso_fromSamplePoint"
CosoAnimalMilkSample ||--|o SosaFeatureOfInterest : "coso_fromSamplePoint"
CosoAnimalMilkSample ||--|o CosoPoint : "coso_fromSamplePoint"
CosoAnimalOrganSample ||--|o CosoSampledFeature : "coso_isSampleOf"
CosoAnimalOrganSample ||--|o GeoFeature : "coso_isSampleOf"
CosoAnimalOrganSample ||--|o OwlThing : "coso_isSampleOf"
CosoAnimalOrganSample ||--|o CosoFeature : "coso_isSampleOf"
CosoAnimalOrganSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampledFeature : "coso_isSampleOf"
CosoAnimalOrganSample ||--|o SosaFeatureOfInterest : "coso_isSampleOf"
CosoAnimalOrganSample ||--|o GeoSpatialObject : "coso_isSampleOf"
CosoAnimalOrganSample ||--|o MeEgadEGAD-SampleCollectionMethod : "coso_sampleAnnotation"
CosoAnimalOrganSample ||--|o OwlNamedIndividual : "coso_sampleAnnotation"
CosoAnimalOrganSample ||--|o MeEgadEGAD-SampleDetailedLocation : "coso_sampleAnnotation"
CosoAnimalOrganSample ||--|o CosoSampleAnnotation : "coso_sampleAnnotation"
CosoAnimalOrganSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleDetailedLocation : "coso_sampleAnnotation"
CosoAnimalOrganSample ||--|o MeEgadEGAD-SampleTreatmentStatus : "coso_sampleAnnotation"
CosoAnimalOrganSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleTreatmentStatus : "coso_sampleAnnotation"
CosoAnimalOrganSample ||--|o OwlThing : "coso_sampleAnnotation"
CosoAnimalOrganSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleCollectionMethod : "coso_sampleAnnotation"
CosoAnimalOrganSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleDetailedLocation : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionLocation"
CosoAnimalOrganSample ||--|o OwlThing : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionLocation"
CosoAnimalOrganSample ||--|o OwlNamedIndividual : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionLocation"
CosoAnimalOrganSample ||--|o CosoSampleAnnotation : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionLocation"
CosoAnimalOrganSample ||--|o OwlThing : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionMethod"
CosoAnimalOrganSample ||--|o OwlNamedIndividual : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionMethod"
CosoAnimalOrganSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleCollectionMethod : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionMethod"
CosoAnimalOrganSample ||--|o CosoSampleAnnotation : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionMethod"
CosoAnimalOrganSample ||--|o RdfsLiteral : "dct_identifier"
CosoAnimalOrganSample ||--|o OwlThing : "owl_sameAs"
CosoAnimalOrganSample ||--|o ProvAgent : "prov_wasAttributedTo"
CosoAnimalOrganSample ||--|o RdfsLiteral : "rdfs_label"
CosoAnimalOrganSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampledFeature : "sosa_isSampleOf"
CosoAnimalOrganSample ||--|o OboFOODON03411183 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboFOODON03411057 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboNCBITaxon283036 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboFOODON02010107 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o HttpW3id.orgSawgraphV1Us-wqp#SampleMedia : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboFOODON00003572 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o B37977f50d3140da51a9630b8a57396a1 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboFOODON03420147 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o B215b3a432e1c482d3680398a554edbbf : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o MeEgadEGAD-SampleMaterialTypeQualifier : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o B036a3008450d6ce37e35cf5a98355a60 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboNCBITaxon66912 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboNCBITaxon7971 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboFOODON03411566 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboFOODON03420194 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboNCBITaxon381124 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o Bf584e1bfd1c74de0eb37e7b926538b83 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboFOODON00001093 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o HttpW3id.orgSawgraphV1Us-wqp#Taxon : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboNCBITaxon8022 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o B44bec873efc8b96cad5f525429c64e0a : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboFOODON00002477 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OwlThing : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o B27231c83f17c76e178e0c9f5e10acc55 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboNCBITaxon6550 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboFOODON02021651 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o Ba6d85f816540f9fec5b71ba42fc2cca6 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o CosoWaterSample : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboNCBITaxon225389 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o B423a0e253807f20386fc3ccbbd7e0378 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o MeEgadEGAD-SampleMaterialType : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboNCBITaxon8182 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboFOODON02010012 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o Bbefc37cbdd03cae92dadef76b34dbf16 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboFOODON03420150 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o B085dcda89ed6aae0d3b229e767f0a1ca : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o Bb0125be5bc4dc7be7e8452e7d22445f6 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o B0d427a711311f1499a234aa8af2c66d1 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboFOODON03411236 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboNCBITaxon6604 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboFOODON03301761 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleMaterialType : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o B7728f65369357f97de36b133c9d1d5e0 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o Be047d68edc8eb3ce96d7edbad5217bfc : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboNCBITaxon8032 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboFOODON03420181 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboFOODON02010045 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboNCBITaxon154811 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboNCBITaxon27778 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o Be497d3b0c2656040c05e303873a2d541 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboFOODON00004460 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o Beb77c26f8c395403edc359fd5f6dfb28 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o B611b8dff312692e7f32a69834c787a60 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboFOODON03411324 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o B75e45ed04b2b903b9029968cada06faa : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboFOODON03420116 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboNCBITaxon225060 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o B75dbc5841338872cea35dced609fcd77 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o CosoSampleMaterialType : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboFOODON00003083 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboNCBITaxon147949 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboFOODON03411325 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboNCBITaxon7998 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboNCBITaxon8010 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o B3cc7b3721547b07a4068dc98b6444b8b : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboNCBITaxon8038 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboNCBITaxon184451 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboFOODON02010015 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o Bbf63deb85414ddecd89e46bce27e7f0a : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboFOODON00004172 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboFOODON03411457 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboNCBITaxon75288 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboFOODON03413378 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboFOODON02010042 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o B4fd286b2a5a12e342d61412628b6e4c2 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o Bf04685c17c0e71ae3c98e08c75cbdfcc : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o B623b56ef58fd82dd088819e22d655c08 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboFOODON00003425 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o B5e93e815b548435105d9273d424fa0e8 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboFOODON00002165 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboFOODON03411669 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o B53622dee107de372b2d0566f64ab6e3a : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboNCBITaxon8167 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboFOODON02020892 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboNCBITaxon27706 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o HttpW3id.orgSawgraphV1Us-wqp#TaxonGroup.FishNekton : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboFOODON00003042 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboFOODON02021803 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboNCBITaxon46259 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboNCBITaxon34816 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleMaterialTypeQualifier : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o Bb71af62f2f3e5e5b5e0fe81f24eca409 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboNCBITaxon66913 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboFOODON03411583 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboFOODON03411328 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboFOODON00004436 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboFOODON02021805 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboFOODON03413358 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboFOODON02010032 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboFOODON02020840 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboNCBITaxon126735 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OwlNamedIndividual : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o OboNCBITaxon13106 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o B8aa8791a0418cd594c8b56ad21351f72 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o B00af777bec4da87c5aebb51d94b2d478 : "coso_sampleOfMaterialType"
CosoAnimalOrganSample ||--|o GeoFeature : "coso_fromSamplePoint"
CosoAnimalOrganSample ||--|o HttpW3id.orgSawgraphV1Us-wqp#Site : "coso_fromSamplePoint"
CosoAnimalOrganSample ||--|o OwlThing : "coso_fromSamplePoint"
CosoAnimalOrganSample ||--|o MeEgadEGAD-SamplePoint : "coso_fromSamplePoint"
CosoAnimalOrganSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint : "coso_fromSamplePoint"
CosoAnimalOrganSample ||--|o GeoSpatialObject : "coso_fromSamplePoint"
CosoAnimalOrganSample ||--|o CosoSamplePoint : "coso_fromSamplePoint"
CosoAnimalOrganSample ||--|o SosaFeatureOfInterest : "coso_fromSamplePoint"
CosoAnimalOrganSample ||--|o CosoPoint : "coso_fromSamplePoint"
CosoAnimalTissueSample ||--|o CosoSampledFeature : "coso_isSampleOf"
CosoAnimalTissueSample ||--|o GeoFeature : "coso_isSampleOf"
CosoAnimalTissueSample ||--|o OwlThing : "coso_isSampleOf"
CosoAnimalTissueSample ||--|o CosoFeature : "coso_isSampleOf"
CosoAnimalTissueSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampledFeature : "coso_isSampleOf"
CosoAnimalTissueSample ||--|o SosaFeatureOfInterest : "coso_isSampleOf"
CosoAnimalTissueSample ||--|o GeoSpatialObject : "coso_isSampleOf"
CosoAnimalTissueSample ||--|o MeEgadEGAD-SampleCollectionMethod : "coso_sampleAnnotation"
CosoAnimalTissueSample ||--|o OwlNamedIndividual : "coso_sampleAnnotation"
CosoAnimalTissueSample ||--|o MeEgadEGAD-SampleDetailedLocation : "coso_sampleAnnotation"
CosoAnimalTissueSample ||--|o CosoSampleAnnotation : "coso_sampleAnnotation"
CosoAnimalTissueSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleDetailedLocation : "coso_sampleAnnotation"
CosoAnimalTissueSample ||--|o MeEgadEGAD-SampleTreatmentStatus : "coso_sampleAnnotation"
CosoAnimalTissueSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleTreatmentStatus : "coso_sampleAnnotation"
CosoAnimalTissueSample ||--|o OwlThing : "coso_sampleAnnotation"
CosoAnimalTissueSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleCollectionMethod : "coso_sampleAnnotation"
CosoAnimalTissueSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleDetailedLocation : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionLocation"
CosoAnimalTissueSample ||--|o OwlThing : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionLocation"
CosoAnimalTissueSample ||--|o OwlNamedIndividual : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionLocation"
CosoAnimalTissueSample ||--|o CosoSampleAnnotation : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionLocation"
CosoAnimalTissueSample ||--|o OwlThing : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionMethod"
CosoAnimalTissueSample ||--|o OwlNamedIndividual : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionMethod"
CosoAnimalTissueSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleCollectionMethod : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionMethod"
CosoAnimalTissueSample ||--|o CosoSampleAnnotation : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionMethod"
CosoAnimalTissueSample ||--|o RdfsLiteral : "dct_identifier"
CosoAnimalTissueSample ||--|o OwlThing : "owl_sameAs"
CosoAnimalTissueSample ||--|o ProvAgent : "prov_wasAttributedTo"
CosoAnimalTissueSample ||--|o RdfsLiteral : "rdfs_label"
CosoAnimalTissueSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampledFeature : "sosa_isSampleOf"
CosoAnimalTissueSample ||--|o OboFOODON03411183 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboFOODON03411057 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboNCBITaxon283036 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboFOODON02010107 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o HttpW3id.orgSawgraphV1Us-wqp#SampleMedia : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboFOODON00003572 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o B37977f50d3140da51a9630b8a57396a1 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboFOODON03420147 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o B215b3a432e1c482d3680398a554edbbf : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o MeEgadEGAD-SampleMaterialTypeQualifier : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o B036a3008450d6ce37e35cf5a98355a60 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboNCBITaxon66912 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboNCBITaxon7971 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboFOODON03411566 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboFOODON03420194 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboNCBITaxon381124 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o Bf584e1bfd1c74de0eb37e7b926538b83 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboFOODON00001093 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o HttpW3id.orgSawgraphV1Us-wqp#Taxon : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboNCBITaxon8022 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o B44bec873efc8b96cad5f525429c64e0a : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboFOODON00002477 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OwlThing : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o B27231c83f17c76e178e0c9f5e10acc55 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboNCBITaxon6550 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboFOODON02021651 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o Ba6d85f816540f9fec5b71ba42fc2cca6 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o CosoWaterSample : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboNCBITaxon225389 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o B423a0e253807f20386fc3ccbbd7e0378 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o MeEgadEGAD-SampleMaterialType : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboNCBITaxon8182 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboFOODON02010012 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o Bbefc37cbdd03cae92dadef76b34dbf16 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboFOODON03420150 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o B085dcda89ed6aae0d3b229e767f0a1ca : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o Bb0125be5bc4dc7be7e8452e7d22445f6 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o B0d427a711311f1499a234aa8af2c66d1 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboFOODON03411236 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboNCBITaxon6604 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboFOODON03301761 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleMaterialType : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o B7728f65369357f97de36b133c9d1d5e0 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o Be047d68edc8eb3ce96d7edbad5217bfc : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboNCBITaxon8032 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboFOODON03420181 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboFOODON02010045 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboNCBITaxon154811 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboNCBITaxon27778 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o Be497d3b0c2656040c05e303873a2d541 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboFOODON00004460 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o Beb77c26f8c395403edc359fd5f6dfb28 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o B611b8dff312692e7f32a69834c787a60 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboFOODON03411324 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o B75e45ed04b2b903b9029968cada06faa : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboFOODON03420116 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboNCBITaxon225060 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o B75dbc5841338872cea35dced609fcd77 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o CosoSampleMaterialType : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboFOODON00003083 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboNCBITaxon147949 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboFOODON03411325 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboNCBITaxon7998 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboNCBITaxon8010 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o B3cc7b3721547b07a4068dc98b6444b8b : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboNCBITaxon8038 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboNCBITaxon184451 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboFOODON02010015 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o Bbf63deb85414ddecd89e46bce27e7f0a : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboFOODON00004172 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboFOODON03411457 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboNCBITaxon75288 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboFOODON03413378 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboFOODON02010042 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o B4fd286b2a5a12e342d61412628b6e4c2 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o Bf04685c17c0e71ae3c98e08c75cbdfcc : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o B623b56ef58fd82dd088819e22d655c08 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboFOODON00003425 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o B5e93e815b548435105d9273d424fa0e8 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboFOODON00002165 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboFOODON03411669 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o B53622dee107de372b2d0566f64ab6e3a : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboNCBITaxon8167 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboFOODON02020892 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboNCBITaxon27706 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o HttpW3id.orgSawgraphV1Us-wqp#TaxonGroup.FishNekton : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboFOODON00003042 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboFOODON02021803 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboNCBITaxon46259 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboNCBITaxon34816 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleMaterialTypeQualifier : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o Bb71af62f2f3e5e5b5e0fe81f24eca409 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboNCBITaxon66913 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboFOODON03411583 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboFOODON03411328 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboFOODON00004436 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboFOODON02021805 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboFOODON03413358 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboFOODON02010032 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboFOODON02020840 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboNCBITaxon126735 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OwlNamedIndividual : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o OboNCBITaxon13106 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o B8aa8791a0418cd594c8b56ad21351f72 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o B00af777bec4da87c5aebb51d94b2d478 : "coso_sampleOfMaterialType"
CosoAnimalTissueSample ||--|o GeoFeature : "coso_fromSamplePoint"
CosoAnimalTissueSample ||--|o HttpW3id.orgSawgraphV1Us-wqp#Site : "coso_fromSamplePoint"
CosoAnimalTissueSample ||--|o OwlThing : "coso_fromSamplePoint"
CosoAnimalTissueSample ||--|o MeEgadEGAD-SamplePoint : "coso_fromSamplePoint"
CosoAnimalTissueSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint : "coso_fromSamplePoint"
CosoAnimalTissueSample ||--|o GeoSpatialObject : "coso_fromSamplePoint"
CosoAnimalTissueSample ||--|o CosoSamplePoint : "coso_fromSamplePoint"
CosoAnimalTissueSample ||--|o SosaFeatureOfInterest : "coso_fromSamplePoint"
CosoAnimalTissueSample ||--|o CosoPoint : "coso_fromSamplePoint"
CosoContaminantConcentrationQuantityKind ||--|o RdfsLiteral : "rdfs_label"
CosoContaminantConcentrationQuantityKind ||--|o OwlThing : "owl_sameAs"
CosoContaminantVolumeQuantityKind ||--|o RdfsLiteral : "rdfs_label"
CosoContaminantVolumeQuantityKind ||--|o OwlThing : "owl_sameAs"
CosoContaminationProperty ||--|o OwlThing : "owl_sameAs"
CosoDetectQuantityValue ||--|o QudtUnit : "qudt_hasUnit"
CosoDetectQuantityValue ||--|o QudtContextualUnit : "qudt_hasUnit"
CosoDetectQuantityValue ||--|o QudtLogarithmicUnit : "qudt_hasUnit"
CosoDetectQuantityValue ||--|o QudtCurrencyUnit : "qudt_hasUnit"
CosoDetectQuantityValue ||--|o QudtDerivedUnit : "qudt_hasUnit"
CosoDetectQuantityValue ||--|o QudtCountingUnit : "qudt_hasUnit"
CosoDetectQuantityValue ||--|o QudtEnumeratedValue : "qudt_enumeratedValue"
CosoDetectQuantityValue ||--|o OwlThing : "owl_sameAs"
CosoDrinkingWaterSample ||--|o RdfsLiteral : "rdfs_label"
CosoDrinkingWaterSample ||--|o OwlThing : "owl_sameAs"
CosoGroundWaterSample ||--|o RdfsLiteral : "rdfs_label"
CosoGroundWaterSample ||--|o OwlThing : "owl_sameAs"
CosoNonDetectQuantityValue ||--|o QudtUnit : "qudt_hasUnit"
CosoNonDetectQuantityValue ||--|o QudtContextualUnit : "qudt_hasUnit"
CosoNonDetectQuantityValue ||--|o QudtLogarithmicUnit : "qudt_hasUnit"
CosoNonDetectQuantityValue ||--|o QudtCurrencyUnit : "qudt_hasUnit"
CosoNonDetectQuantityValue ||--|o QudtDerivedUnit : "qudt_hasUnit"
CosoNonDetectQuantityValue ||--|o QudtCountingUnit : "qudt_hasUnit"
CosoNonDetectQuantityValue ||--|o QudtEnumeratedValue : "qudt_enumeratedValue"
CosoNonDetectQuantityValue ||--|o OwlThing : "owl_sameAs"
CosoPlantMaterialSample ||--|o CosoSampledFeature : "coso_isSampleOf"
CosoPlantMaterialSample ||--|o GeoFeature : "coso_isSampleOf"
CosoPlantMaterialSample ||--|o OwlThing : "coso_isSampleOf"
CosoPlantMaterialSample ||--|o CosoFeature : "coso_isSampleOf"
CosoPlantMaterialSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampledFeature : "coso_isSampleOf"
CosoPlantMaterialSample ||--|o SosaFeatureOfInterest : "coso_isSampleOf"
CosoPlantMaterialSample ||--|o GeoSpatialObject : "coso_isSampleOf"
CosoPlantMaterialSample ||--|o MeEgadEGAD-SampleCollectionMethod : "coso_sampleAnnotation"
CosoPlantMaterialSample ||--|o OwlNamedIndividual : "coso_sampleAnnotation"
CosoPlantMaterialSample ||--|o MeEgadEGAD-SampleDetailedLocation : "coso_sampleAnnotation"
CosoPlantMaterialSample ||--|o CosoSampleAnnotation : "coso_sampleAnnotation"
CosoPlantMaterialSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleDetailedLocation : "coso_sampleAnnotation"
CosoPlantMaterialSample ||--|o MeEgadEGAD-SampleTreatmentStatus : "coso_sampleAnnotation"
CosoPlantMaterialSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleTreatmentStatus : "coso_sampleAnnotation"
CosoPlantMaterialSample ||--|o OwlThing : "coso_sampleAnnotation"
CosoPlantMaterialSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleCollectionMethod : "coso_sampleAnnotation"
CosoPlantMaterialSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleDetailedLocation : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionLocation"
CosoPlantMaterialSample ||--|o OwlThing : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionLocation"
CosoPlantMaterialSample ||--|o OwlNamedIndividual : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionLocation"
CosoPlantMaterialSample ||--|o CosoSampleAnnotation : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionLocation"
CosoPlantMaterialSample ||--|o OwlThing : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionMethod"
CosoPlantMaterialSample ||--|o OwlNamedIndividual : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionMethod"
CosoPlantMaterialSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleCollectionMethod : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionMethod"
CosoPlantMaterialSample ||--|o CosoSampleAnnotation : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionMethod"
CosoPlantMaterialSample ||--|o RdfsLiteral : "dct_identifier"
CosoPlantMaterialSample ||--|o OwlThing : "owl_sameAs"
CosoPlantMaterialSample ||--|o ProvAgent : "prov_wasAttributedTo"
CosoPlantMaterialSample ||--|o RdfsLiteral : "rdfs_label"
CosoPlantMaterialSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampledFeature : "sosa_isSampleOf"
CosoPlantMaterialSample ||--|o OboFOODON03411183 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboFOODON03411057 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboNCBITaxon283036 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboFOODON02010107 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o HttpW3id.orgSawgraphV1Us-wqp#SampleMedia : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboFOODON00003572 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o B37977f50d3140da51a9630b8a57396a1 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboFOODON03420147 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o B215b3a432e1c482d3680398a554edbbf : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o MeEgadEGAD-SampleMaterialTypeQualifier : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o B036a3008450d6ce37e35cf5a98355a60 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboNCBITaxon66912 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboNCBITaxon7971 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboFOODON03411566 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboFOODON03420194 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboNCBITaxon381124 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o Bf584e1bfd1c74de0eb37e7b926538b83 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboFOODON00001093 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o HttpW3id.orgSawgraphV1Us-wqp#Taxon : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboNCBITaxon8022 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o B44bec873efc8b96cad5f525429c64e0a : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboFOODON00002477 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OwlThing : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o B27231c83f17c76e178e0c9f5e10acc55 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboNCBITaxon6550 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboFOODON02021651 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o Ba6d85f816540f9fec5b71ba42fc2cca6 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o CosoWaterSample : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboNCBITaxon225389 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o B423a0e253807f20386fc3ccbbd7e0378 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o MeEgadEGAD-SampleMaterialType : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboNCBITaxon8182 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboFOODON02010012 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o Bbefc37cbdd03cae92dadef76b34dbf16 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboFOODON03420150 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o B085dcda89ed6aae0d3b229e767f0a1ca : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o Bb0125be5bc4dc7be7e8452e7d22445f6 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o B0d427a711311f1499a234aa8af2c66d1 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboFOODON03411236 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboNCBITaxon6604 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboFOODON03301761 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleMaterialType : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o B7728f65369357f97de36b133c9d1d5e0 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o Be047d68edc8eb3ce96d7edbad5217bfc : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboNCBITaxon8032 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboFOODON03420181 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboFOODON02010045 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboNCBITaxon154811 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboNCBITaxon27778 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o Be497d3b0c2656040c05e303873a2d541 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboFOODON00004460 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o Beb77c26f8c395403edc359fd5f6dfb28 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o B611b8dff312692e7f32a69834c787a60 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboFOODON03411324 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o B75e45ed04b2b903b9029968cada06faa : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboFOODON03420116 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboNCBITaxon225060 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o B75dbc5841338872cea35dced609fcd77 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o CosoSampleMaterialType : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboFOODON00003083 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboNCBITaxon147949 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboFOODON03411325 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboNCBITaxon7998 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboNCBITaxon8010 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o B3cc7b3721547b07a4068dc98b6444b8b : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboNCBITaxon8038 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboNCBITaxon184451 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboFOODON02010015 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o Bbf63deb85414ddecd89e46bce27e7f0a : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboFOODON00004172 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboFOODON03411457 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboNCBITaxon75288 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboFOODON03413378 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboFOODON02010042 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o B4fd286b2a5a12e342d61412628b6e4c2 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o Bf04685c17c0e71ae3c98e08c75cbdfcc : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o B623b56ef58fd82dd088819e22d655c08 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboFOODON00003425 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o B5e93e815b548435105d9273d424fa0e8 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboFOODON00002165 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboFOODON03411669 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o B53622dee107de372b2d0566f64ab6e3a : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboNCBITaxon8167 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboFOODON02020892 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboNCBITaxon27706 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o HttpW3id.orgSawgraphV1Us-wqp#TaxonGroup.FishNekton : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboFOODON00003042 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboFOODON02021803 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboNCBITaxon46259 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboNCBITaxon34816 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleMaterialTypeQualifier : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o Bb71af62f2f3e5e5b5e0fe81f24eca409 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboNCBITaxon66913 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboFOODON03411583 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboFOODON03411328 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboFOODON00004436 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboFOODON02021805 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboFOODON03413358 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboFOODON02010032 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboFOODON02020840 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboNCBITaxon126735 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OwlNamedIndividual : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o OboNCBITaxon13106 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o B8aa8791a0418cd594c8b56ad21351f72 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o B00af777bec4da87c5aebb51d94b2d478 : "coso_sampleOfMaterialType"
CosoPlantMaterialSample ||--|o GeoFeature : "coso_fromSamplePoint"
CosoPlantMaterialSample ||--|o HttpW3id.orgSawgraphV1Us-wqp#Site : "coso_fromSamplePoint"
CosoPlantMaterialSample ||--|o OwlThing : "coso_fromSamplePoint"
CosoPlantMaterialSample ||--|o MeEgadEGAD-SamplePoint : "coso_fromSamplePoint"
CosoPlantMaterialSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint : "coso_fromSamplePoint"
CosoPlantMaterialSample ||--|o GeoSpatialObject : "coso_fromSamplePoint"
CosoPlantMaterialSample ||--|o CosoSamplePoint : "coso_fromSamplePoint"
CosoPlantMaterialSample ||--|o SosaFeatureOfInterest : "coso_fromSamplePoint"
CosoPlantMaterialSample ||--|o CosoPoint : "coso_fromSamplePoint"
CosoSubstanceCollection ||--|o RdfsLiteral : "dct_identifier"
CosoSubstanceCollection ||--|o OwlThing : "owl_sameAs"
CosoSubstanceCollection ||--|o RdfsLiteral : "rdfs_label"
CosoSubstanceCollection ||--|o OwlNamedIndividual : "coso_hasMember"
CosoSubstanceCollection ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-ParameterName : "coso_hasMember"
CosoSubstanceCollection ||--|o Beb7217b5b32080b9606028314249e33b : "coso_hasMember"
CosoSurfaceWaterSample ||--|o RdfsLiteral : "rdfs_label"
CosoSurfaceWaterSample ||--|o OwlThing : "owl_sameAs"
CosoTreatedWaterSample ||--|o RdfsLiteral : "rdfs_label"
CosoTreatedWaterSample ||--|o OwlThing : "owl_sameAs"
CosoWasteWaterSample ||--|o RdfsLiteral : "rdfs_label"
CosoWasteWaterSample ||--|o OwlThing : "owl_sameAs"
CosoWaterSample ||--|o RdfsLiteral : "rdfs_label"
CosoWaterSample ||--|o OwlThing : "owl_sameAs"
CosoWaterSampleBySource ||--|o RdfsLiteral : "rdfs_label"
CosoWaterSampleBySource ||--|o OwlThing : "owl_sameAs"
CosoWaterSampleByTreatment ||--|o RdfsLiteral : "rdfs_label"
CosoWaterSampleByTreatment ||--|o OwlThing : "owl_sameAs"
HttpW3id.orgComptoxCompToxChemicalEntity ||--|o RdfsLiteral : "rdfs_label"
HttpW3id.orgComptoxCompToxChemicalEntity ||--|o OwlThing : "owl_sameAs"
HttpW3id.orgComptoxV1ChemicalEntity ||--|o RdfsLiteral : "rdfs_label"
HttpW3id.orgSawgraphV1Me-egad#EGAD-AggregatePFAS-Concentration ||--|o MeEgadEGAD-ConcentrationQualifier : "coso_resultAnnotation"
HttpW3id.orgSawgraphV1Me-egad#EGAD-AggregatePFAS-Concentration ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-ValidationLevel : "coso_resultAnnotation"
HttpW3id.orgSawgraphV1Me-egad#EGAD-AggregatePFAS-Concentration ||--|o OwlNamedIndividual : "coso_resultAnnotation"
HttpW3id.orgSawgraphV1Me-egad#EGAD-AggregatePFAS-Concentration ||--|o MeEgadEGAD-MethodDetectionLimit : "coso_resultAnnotation"
HttpW3id.orgSawgraphV1Me-egad#EGAD-AggregatePFAS-Concentration ||--|o MeEgadEGAD-ValidationLevel : "coso_resultAnnotation"
HttpW3id.orgSawgraphV1Me-egad#EGAD-AggregatePFAS-Concentration ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-ReportingLimit : "coso_resultAnnotation"
HttpW3id.orgSawgraphV1Me-egad#EGAD-AggregatePFAS-Concentration ||--|o OwlThing : "coso_resultAnnotation"
HttpW3id.orgSawgraphV1Me-egad#EGAD-AggregatePFAS-Concentration ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-ConcentrationQualifier : "coso_resultAnnotation"
HttpW3id.orgSawgraphV1Me-egad#EGAD-AggregatePFAS-Concentration ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-MethodDetectionLimit : "coso_resultAnnotation"
HttpW3id.orgSawgraphV1Me-egad#EGAD-AggregatePFAS-Concentration ||--|o MeEgadEGAD-ReportingLimit : "coso_resultAnnotation"
HttpW3id.orgSawgraphV1Me-egad#EGAD-AggregatePFAS-Concentration ||--|o QudtEnumeratedValue : "coso_measurementValue"
HttpW3id.orgSawgraphV1Me-egad#EGAD-AggregatePFAS-Concentration ||--|o QudtConcept : "coso_measurementValue"
HttpW3id.orgSawgraphV1Me-egad#EGAD-AggregatePFAS-Concentration ||--|o QudtVerifiable : "coso_measurementValue"
HttpW3id.orgSawgraphV1Me-egad#EGAD-AggregatePFAS-Concentration ||--|o CosoResultQualifier : "http___w3id.org_sawgraph_v1_me-egad#methodDetectionLimit"
HttpW3id.orgSawgraphV1Me-egad#EGAD-AggregatePFAS-Concentration ||--|o CosoDetectionLimit : "http___w3id.org_sawgraph_v1_me-egad#methodDetectionLimit"
HttpW3id.orgSawgraphV1Me-egad#EGAD-AggregatePFAS-Concentration ||--|o OwlThing : "http___w3id.org_sawgraph_v1_me-egad#methodDetectionLimit"
HttpW3id.orgSawgraphV1Me-egad#EGAD-AggregatePFAS-Concentration ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-MethodDetectionLimit : "http___w3id.org_sawgraph_v1_me-egad#methodDetectionLimit"
HttpW3id.orgSawgraphV1Me-egad#EGAD-AggregatePFAS-Concentration ||--|o QudtQuantifiable : "http___w3id.org_sawgraph_v1_me-egad#methodDetectionLimit"
HttpW3id.orgSawgraphV1Me-egad#EGAD-AggregatePFAS-Concentration ||--|o QudtQuantity : "http___w3id.org_sawgraph_v1_me-egad#methodDetectionLimit"
HttpW3id.orgSawgraphV1Me-egad#EGAD-AggregatePFAS-Concentration ||--|o QudtConcept : "http___w3id.org_sawgraph_v1_me-egad#methodDetectionLimit"
HttpW3id.orgSawgraphV1Me-egad#EGAD-AggregatePFAS-Concentration ||--|o StadDatapoint : "http___w3id.org_sawgraph_v1_me-egad#methodDetectionLimit"
HttpW3id.orgSawgraphV1Me-egad#EGAD-AggregatePFAS-Concentration ||--|o QudtQuantityKind : "qudt_hasQuantityKind"
HttpW3id.orgSawgraphV1Me-egad#EGAD-AggregatePFAS-Concentration ||--|o OwlThing : "http___w3id.org_sawgraph_v1_me-egad#validationQualifier"
HttpW3id.orgSawgraphV1Me-egad#EGAD-AggregatePFAS-Concentration ||--|o OwlNamedIndividual : "http___w3id.org_sawgraph_v1_me-egad#validationQualifier"
HttpW3id.orgSawgraphV1Me-egad#EGAD-AggregatePFAS-Concentration ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-ConcentrationQualifier : "http___w3id.org_sawgraph_v1_me-egad#validationQualifier"
HttpW3id.orgSawgraphV1Me-egad#EGAD-AggregatePFAS-Concentration ||--|o OwlThing : "owl_sameAs"
HttpW3id.orgSawgraphV1Me-egad#EGAD-AggregatePFAS-Concentration ||--|o QudtConcept : "coso_measurementUnit"
HttpW3id.orgSawgraphV1Me-egad#EGAD-AggregatePFAS-Concentration ||--|o QudtUnit : "coso_measurementUnit"
HttpW3id.orgSawgraphV1Me-egad#EGAD-AggregatePFAS-Concentration ||--|o QudtQuantityValue : "qudt_quantityValue"
HttpW3id.orgSawgraphV1Me-egad#EGAD-AggregatePFAS-Concentration ||--|o RdfsLiteral : "rdfs_label"
HttpW3id.orgSawgraphV1Me-egad#EGAD-AggregatePFAS-Concentration ||--|o OwlNamedIndividual : "http___w3id.org_sawgraph_v1_me-egad#labQualifier"
HttpW3id.orgSawgraphV1Me-egad#EGAD-AggregatePFAS-Concentration ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-ConcentrationQualifier : "http___w3id.org_sawgraph_v1_me-egad#labQualifier"
HttpW3id.orgSawgraphV1Me-egad#EGAD-AggregatePFAS-Concentration ||--|o CosoQuantitationLimit : "http___w3id.org_sawgraph_v1_me-egad#reportingLimit"
HttpW3id.orgSawgraphV1Me-egad#EGAD-AggregatePFAS-Concentration ||--|o CosoResultQualifier : "http___w3id.org_sawgraph_v1_me-egad#reportingLimit"
HttpW3id.orgSawgraphV1Me-egad#EGAD-AggregatePFAS-Concentration ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-ReportingLimit : "http___w3id.org_sawgraph_v1_me-egad#reportingLimit"
HttpW3id.orgSawgraphV1Me-egad#EGAD-AggregatePFAS-Concentration ||--|o OwlThing : "http___w3id.org_sawgraph_v1_me-egad#reportingLimit"
HttpW3id.orgSawgraphV1Me-egad#EGAD-AggregatePFAS-Concentration ||--|o QudtQuantifiable : "http___w3id.org_sawgraph_v1_me-egad#reportingLimit"
HttpW3id.orgSawgraphV1Me-egad#EGAD-AggregatePFAS-Concentration ||--|o QudtQuantity : "http___w3id.org_sawgraph_v1_me-egad#reportingLimit"
HttpW3id.orgSawgraphV1Me-egad#EGAD-AggregatePFAS-Concentration ||--|o QudtConcept : "http___w3id.org_sawgraph_v1_me-egad#reportingLimit"
HttpW3id.orgSawgraphV1Me-egad#EGAD-AggregatePFAS-Concentration ||--|o StadDatapoint : "http___w3id.org_sawgraph_v1_me-egad#reportingLimit"
HttpW3id.orgSawgraphV1Me-egad#EGAD-AggregatePFAS-Concentration ||--|o OwlNamedIndividual : "stad_hasQualityKind"
HttpW3id.orgSawgraphV1Me-egad#EGAD-AggregatePFAS-Concentration ||--|o QudtQuantityKind : "stad_hasQualityKind"
HttpW3id.orgSawgraphV1Me-egad#EGAD-AggregatePFAS-Concentration ||--|o CosoContaminantConcentrationQuantityKind : "stad_hasQualityKind"
HttpW3id.orgSawgraphV1Me-egad#EGAD-AggregatePFAS-Concentration ||--|o CosoContaminationProperty : "stad_hasQualityKind"
HttpW3id.orgSawgraphV1Me-egad#EGAD-AggregatePFAS-Concentration ||--|o StadQualityKind : "stad_hasQualityKind"
HttpW3id.orgSawgraphV1Me-egad#EGAD-AggregatePFAS-Concentration ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-ValidationLevel : "http___w3id.org_sawgraph_v1_me-egad#validationLevel"
HttpW3id.orgSawgraphV1Me-egad#EGAD-AggregatePFAS-Concentration ||--|o OwlNamedIndividual : "http___w3id.org_sawgraph_v1_me-egad#validationLevel"
HttpW3id.orgSawgraphV1Me-egad#EGAD-AggregatePFAS-Concentration ||--|o OwlThing : "http___w3id.org_sawgraph_v1_me-egad#validationLevel"
HttpW3id.orgSawgraphV1Me-egad#EGAD-AnalysisMethod ||--|o RdfsLiteral : "rdfs_label"
HttpW3id.orgSawgraphV1Me-egad#EGAD-AnalysisMethod ||--|o OwlThing : "owl_sameAs"
HttpW3id.orgSawgraphV1Me-egad#EGAD-ConcentrationQualifier ||--|o RdfsLiteral : "rdfs_label"
HttpW3id.orgSawgraphV1Me-egad#EGAD-ConcentrationQualifier ||--|o OwlThing : "owl_sameAs"
HttpW3id.orgSawgraphV1Me-egad#EGAD-MethodDetectionLimit ||--|o QudtUnit : "qudt_hasUnit"
HttpW3id.orgSawgraphV1Me-egad#EGAD-MethodDetectionLimit ||--|o QudtContextualUnit : "qudt_hasUnit"
HttpW3id.orgSawgraphV1Me-egad#EGAD-MethodDetectionLimit ||--|o QudtLogarithmicUnit : "qudt_hasUnit"
HttpW3id.orgSawgraphV1Me-egad#EGAD-MethodDetectionLimit ||--|o QudtCurrencyUnit : "qudt_hasUnit"
HttpW3id.orgSawgraphV1Me-egad#EGAD-MethodDetectionLimit ||--|o QudtDerivedUnit : "qudt_hasUnit"
HttpW3id.orgSawgraphV1Me-egad#EGAD-MethodDetectionLimit ||--|o QudtCountingUnit : "qudt_hasUnit"
HttpW3id.orgSawgraphV1Me-egad#EGAD-MethodDetectionLimit ||--|o OwlThing : "owl_sameAs"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o GeoFeature : "coso_observedAtSamplePoint"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o HttpW3id.orgSawgraphV1Us-wqp#Site : "coso_observedAtSamplePoint"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o OwlThing : "coso_observedAtSamplePoint"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o MeEgadEGAD-SamplePoint : "coso_observedAtSamplePoint"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint : "coso_observedAtSamplePoint"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o GeoSpatialObject : "coso_observedAtSamplePoint"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o CosoSamplePoint : "coso_observedAtSamplePoint"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o SosaFeatureOfInterest : "coso_observedAtSamplePoint"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o CosoPoint : "coso_observedAtSamplePoint"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o OwlNamedIndividual : "coso_ofDatasetSubstance"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o CosoSubstanceCollection : "coso_ofDatasetSubstance"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o HttpW3id.orgSawgraphV1Us-wqp#Characteristic : "coso_ofDatasetSubstance"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o Beb7217b5b32080b9606028314249e33b : "coso_ofDatasetSubstance"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o OwlThing : "coso_ofDatasetSubstance"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-ParameterName : "coso_ofDatasetSubstance"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o OwlNamedIndividual : "coso_ofSubstance"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o CosoSubstanceCollection : "coso_ofSubstance"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o Beb7217b5b32080b9606028314249e33b : "coso_ofSubstance"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o OwlThing : "coso_ofSubstance"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-ParameterName : "coso_ofSubstance"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o Ba76635ffb4afc02e78b9ef49973d089f : "coso_ofSubstance"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample : "coso_analyzedSample"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample : "coso_analyzedSample"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o SosaFeatureOfInterest : "coso_analyzedSample"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o CosoPlantMaterialSample : "coso_analyzedSample"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample : "coso_analyzedSample"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample : "coso_analyzedSample"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o MeEgadEGAD-Sample : "coso_analyzedSample"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o CosoAnimalTissueSample : "coso_analyzedSample"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o CosoAnimalOrganSample : "coso_analyzedSample"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o HttpW3id.orgSawgraphV1Us-wqp#Sample : "coso_analyzedSample"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o SosaSample : "coso_analyzedSample"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o CosoMaterialSample : "coso_analyzedSample"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o CosoAnimalMilkSample : "coso_analyzedSample"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample : "coso_analyzedSample"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o CosoAnimalBloodSample : "coso_analyzedSample"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o OwlThing : "coso_analyzedSample"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample : "coso_analyzedSample"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o CosoAnimalMaterialSample : "coso_analyzedSample"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample : "coso_analyzedSample"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o MeEgadEGAD-AnalysisMethod : "coso_analysisMethod"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o OwlNamedIndividual : "coso_analysisMethod"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-AnalysisMethod : "coso_analysisMethod"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o GeoFeature : "coso_observedAtPoint"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o OwlThing : "coso_observedAtPoint"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o MeEgadEGAD-SamplePoint : "coso_observedAtPoint"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint : "coso_observedAtPoint"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o GeoSpatialObject : "coso_observedAtPoint"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o SosaFeatureOfInterest : "coso_observedAtPoint"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o CosoPoint : "coso_observedAtPoint"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample : "coso_hasAnyFeatureOfInterest"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample : "coso_hasAnyFeatureOfInterest"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o SosaFeatureOfInterest : "coso_hasAnyFeatureOfInterest"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o CosoPlantMaterialSample : "coso_hasAnyFeatureOfInterest"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample : "coso_hasAnyFeatureOfInterest"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint : "coso_hasAnyFeatureOfInterest"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample : "coso_hasAnyFeatureOfInterest"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o MeEgadEGAD-Sample : "coso_hasAnyFeatureOfInterest"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o CosoAnimalTissueSample : "coso_hasAnyFeatureOfInterest"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o CosoAnimalOrganSample : "coso_hasAnyFeatureOfInterest"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o MeEgadEGAD-SampledFeature : "coso_hasAnyFeatureOfInterest"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o MeEgadEGAD-SamplePoint : "coso_hasAnyFeatureOfInterest"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample : "coso_hasAnyFeatureOfInterest"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o CosoAnimalMilkSample : "coso_hasAnyFeatureOfInterest"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o CosoAnimalBloodSample : "coso_hasAnyFeatureOfInterest"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o OwlThing : "coso_hasAnyFeatureOfInterest"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampledFeature : "coso_hasAnyFeatureOfInterest"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample : "coso_hasAnyFeatureOfInterest"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o CosoAnimalMaterialSample : "coso_hasAnyFeatureOfInterest"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample : "coso_hasAnyFeatureOfInterest"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o OwlThing : "http___w3id.org_sawgraph_v1_me-egad#resultType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o OwlNamedIndividual : "http___w3id.org_sawgraph_v1_me-egad#resultType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-ResultType : "http___w3id.org_sawgraph_v1_me-egad#resultType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o CosoObservationAnnotation : "http___w3id.org_sawgraph_v1_me-egad#resultType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o OwlThing : "owl_sameAs"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o ProvAgent : "prov_wasAttributedTo"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o RdfsLiteral : "rdfs_label"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SinglePFAS-Concentration : "coso_hasResult"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o MeEgadEGAD-SinglePFAS-Concentration : "coso_hasResult"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-AggregatePFAS-Concentration : "coso_hasResult"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o MeEgadEGAD-AggregatePFAS-Concentration : "coso_hasResult"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o HttpW3id.orgSawgraphV1Us-wqp#Single-PFAS-Concentration : "coso_hasResult"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o SosaResult : "coso_hasResult"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o CosoContaminantMeasurement : "coso_hasResult"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o OwlThing : "coso_hasResult"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o QudtQuantifiable : "coso_hasResult"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o QudtQuantity : "coso_hasResult"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o QudtConcept : "coso_hasResult"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o StadDatapoint : "coso_hasResult"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o OwlNamedIndividual : "coso_observationAnnotation"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-ResultType : "coso_observationAnnotation"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o OwlThing : "coso_observationAnnotation"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o CosoObservationAnnotation : "coso_observationAnnotation"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o MeEgadEGAD-ResultType : "coso_observationAnnotation"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o OwlNamedIndividual : "coso_observedProperty"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o OwlThing : "coso_observedProperty"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o QudtQuantityKind : "coso_observedProperty"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o CosoContaminantConcentrationQuantityKind : "coso_observedProperty"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o CosoContaminationProperty : "coso_observedProperty"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o StadQualityKind : "coso_observedProperty"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o SosaProperty : "coso_observedProperty"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o GeoFeature : "coso_hasFeatureOfInterest"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o MeEgadEGAD-SampledFeature : "coso_hasFeatureOfInterest"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o OwlThing : "coso_hasFeatureOfInterest"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o CosoFeature : "coso_hasFeatureOfInterest"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampledFeature : "coso_hasFeatureOfInterest"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o SosaFeatureOfInterest : "coso_hasFeatureOfInterest"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation ||--|o GeoSpatialObject : "coso_hasFeatureOfInterest"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-ParameterName ||--|o HttpW3id.orgComptoxV1ChemicalEntity : "http___w3id.org_comptox_v1_sameAsComptoxSubstance"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-ParameterName ||--|o RdfsLiteral : "dct_identifier"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-ParameterName ||--|o OwlThing : "owl_sameAs"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-ParameterName ||--|o OwlThing : "http___w3id.org_comptox_sameAsComptoxSubstance"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-ParameterName ||--|o HttpW3id.orgComptoxCompToxChemicalEntity : "http___w3id.org_comptox_sameAsComptoxSubstance"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-ParameterName ||--|o CosoSubstance : "http___w3id.org_comptox_sameAsComptoxSubstance"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-ParameterName ||--|o Beb7217b5b32080b9606028314249e33b : "http___w3id.org_comptox_sameAsComptoxSubstance"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-ParameterName ||--|o RdfsLiteral : "rdfs_label"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-ParameterName ||--|o OwlNamedIndividual : "coso_hasMember"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-ParameterName ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-ParameterName : "coso_hasMember"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-ParameterName ||--|o Beb7217b5b32080b9606028314249e33b : "coso_hasMember"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Site ||--|o GeoGeometry : "geo_hasGeometry"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Site ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SiteType : "http___w3id.org_sawgraph_v1_me-egad#siteType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Site ||--|o OwlNamedIndividual : "http___w3id.org_sawgraph_v1_me-egad#siteType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Site ||--|o MeEgadEGAD-SiteType : "me_egad_siteType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Site ||--|o OwlNamedIndividual : "me_egad_siteType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Site ||--|o RdfsLiteral : "dct_identifier"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Site ||--|o KwgoS2CellLevel13 : "spatial_spatiallyRelatedTo"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Site ||--|o KwgoAdministrativeRegion : "spatial_spatiallyRelatedTo"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Site ||--|o OwlThing : "spatial_spatiallyRelatedTo"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Site ||--|o MeEgadEGAD-SamplePoint : "spatial_spatiallyRelatedTo"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Site ||--|o KwgoAdministrativeRegion3 : "spatial_spatiallyRelatedTo"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Site ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint : "spatial_spatiallyRelatedTo"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Site ||--|o MeEgadEGAD-PFAS-Site : "spatial_spatiallyRelatedTo"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Site ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Site : "spatial_spatiallyRelatedTo"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Site ||--|o GeoSpatialObject : "spatial_spatiallyRelatedTo"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Site ||--|o KwgoRegion : "spatial_spatiallyRelatedTo"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Site ||--|o OwlThing : "owl_sameAs"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Site ||--|o GeoGeometry : "geo_hasDefaultGeometry"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Site ||--|o RdfsLiteral : "rdfs_label"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Site ||--|o KwgoS2CellLevel13 : "spatial_connectedTo"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Site ||--|o KwgoAdministrativeRegion : "spatial_connectedTo"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Site ||--|o OwlThing : "spatial_connectedTo"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Site ||--|o MeEgadEGAD-SamplePoint : "spatial_connectedTo"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Site ||--|o KwgoAdministrativeRegion3 : "spatial_connectedTo"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Site ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint : "spatial_connectedTo"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Site ||--|o MeEgadEGAD-PFAS-Site : "spatial_connectedTo"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Site ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Site : "spatial_connectedTo"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Site ||--|o GeoSpatialObject : "spatial_connectedTo"
HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Site ||--|o KwgoRegion : "spatial_connectedTo"
HttpW3id.orgSawgraphV1Me-egad#EGAD-ReportingLimit ||--|o QudtUnit : "qudt_hasUnit"
HttpW3id.orgSawgraphV1Me-egad#EGAD-ReportingLimit ||--|o QudtContextualUnit : "qudt_hasUnit"
HttpW3id.orgSawgraphV1Me-egad#EGAD-ReportingLimit ||--|o QudtLogarithmicUnit : "qudt_hasUnit"
HttpW3id.orgSawgraphV1Me-egad#EGAD-ReportingLimit ||--|o QudtCurrencyUnit : "qudt_hasUnit"
HttpW3id.orgSawgraphV1Me-egad#EGAD-ReportingLimit ||--|o QudtDerivedUnit : "qudt_hasUnit"
HttpW3id.orgSawgraphV1Me-egad#EGAD-ReportingLimit ||--|o QudtCountingUnit : "qudt_hasUnit"
HttpW3id.orgSawgraphV1Me-egad#EGAD-ReportingLimit ||--|o OwlThing : "owl_sameAs"
HttpW3id.orgSawgraphV1Me-egad#EGAD-ResultType ||--|o RdfsLiteral : "rdfs_label"
HttpW3id.orgSawgraphV1Me-egad#EGAD-ResultType ||--|o OwlThing : "owl_sameAs"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o CosoSampledFeature : "coso_isSampleOf"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o GeoFeature : "coso_isSampleOf"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OwlThing : "coso_isSampleOf"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o CosoFeature : "coso_isSampleOf"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampledFeature : "coso_isSampleOf"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o SosaFeatureOfInterest : "coso_isSampleOf"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o GeoSpatialObject : "coso_isSampleOf"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o MeEgadEGAD-SampleCollectionMethod : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OwlNamedIndividual : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o MeEgadEGAD-SampleDetailedLocation : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o CosoSampleAnnotation : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleDetailedLocation : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o MeEgadEGAD-SampleTreatmentStatus : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleTreatmentStatus : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OwlThing : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleCollectionMethod : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleDetailedLocation : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionLocation"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OwlThing : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionLocation"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OwlNamedIndividual : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionLocation"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o CosoSampleAnnotation : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionLocation"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OwlThing : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionMethod"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OwlNamedIndividual : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionMethod"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleCollectionMethod : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionMethod"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o CosoSampleAnnotation : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionMethod"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o RdfsLiteral : "dct_identifier"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OwlThing : "owl_sameAs"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OwlThing : "http___w3id.org_sawgraph_v1_me-egad#sampleTreatmentStatus"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OwlNamedIndividual : "http___w3id.org_sawgraph_v1_me-egad#sampleTreatmentStatus"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleTreatmentStatus : "http___w3id.org_sawgraph_v1_me-egad#sampleTreatmentStatus"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o CosoSampleAnnotation : "http___w3id.org_sawgraph_v1_me-egad#sampleTreatmentStatus"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o ProvAgent : "prov_wasAttributedTo"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o RdfsLiteral : "rdfs_label"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampledFeature : "sosa_isSampleOf"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboFOODON03411183 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboFOODON03411057 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboNCBITaxon283036 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboFOODON02010107 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o HttpW3id.orgSawgraphV1Us-wqp#SampleMedia : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboFOODON00003572 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o B37977f50d3140da51a9630b8a57396a1 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboFOODON03420147 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o B215b3a432e1c482d3680398a554edbbf : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o MeEgadEGAD-SampleMaterialTypeQualifier : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o B036a3008450d6ce37e35cf5a98355a60 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboNCBITaxon66912 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboNCBITaxon7971 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboFOODON03411566 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboFOODON03420194 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboNCBITaxon381124 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o Bf584e1bfd1c74de0eb37e7b926538b83 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboFOODON00001093 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o HttpW3id.orgSawgraphV1Us-wqp#Taxon : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboNCBITaxon8022 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o B44bec873efc8b96cad5f525429c64e0a : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboFOODON00002477 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OwlThing : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o B27231c83f17c76e178e0c9f5e10acc55 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboNCBITaxon6550 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboFOODON02021651 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o Ba6d85f816540f9fec5b71ba42fc2cca6 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o CosoWaterSample : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboNCBITaxon225389 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o B423a0e253807f20386fc3ccbbd7e0378 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o MeEgadEGAD-SampleMaterialType : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboNCBITaxon8182 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboFOODON02010012 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o Bbefc37cbdd03cae92dadef76b34dbf16 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboFOODON03420150 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o B085dcda89ed6aae0d3b229e767f0a1ca : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o Bb0125be5bc4dc7be7e8452e7d22445f6 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o B0d427a711311f1499a234aa8af2c66d1 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboFOODON03411236 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboNCBITaxon6604 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboFOODON03301761 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleMaterialType : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o B7728f65369357f97de36b133c9d1d5e0 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o Be047d68edc8eb3ce96d7edbad5217bfc : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboNCBITaxon8032 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboFOODON03420181 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboFOODON02010045 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboNCBITaxon154811 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboNCBITaxon27778 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o Be497d3b0c2656040c05e303873a2d541 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboFOODON00004460 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o Beb77c26f8c395403edc359fd5f6dfb28 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o B611b8dff312692e7f32a69834c787a60 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboFOODON03411324 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o B75e45ed04b2b903b9029968cada06faa : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboFOODON03420116 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboNCBITaxon225060 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o B75dbc5841338872cea35dced609fcd77 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o CosoSampleMaterialType : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboFOODON00003083 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboNCBITaxon147949 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboFOODON03411325 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboNCBITaxon7998 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboNCBITaxon8010 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o B3cc7b3721547b07a4068dc98b6444b8b : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboNCBITaxon8038 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboNCBITaxon184451 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboFOODON02010015 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o Bbf63deb85414ddecd89e46bce27e7f0a : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboFOODON00004172 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboFOODON03411457 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboNCBITaxon75288 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboFOODON03413378 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboFOODON02010042 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o B4fd286b2a5a12e342d61412628b6e4c2 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o Bf04685c17c0e71ae3c98e08c75cbdfcc : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o B623b56ef58fd82dd088819e22d655c08 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboFOODON00003425 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o B5e93e815b548435105d9273d424fa0e8 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboFOODON00002165 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboFOODON03411669 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o B53622dee107de372b2d0566f64ab6e3a : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboNCBITaxon8167 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboFOODON02020892 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboNCBITaxon27706 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o HttpW3id.orgSawgraphV1Us-wqp#TaxonGroup.FishNekton : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboFOODON00003042 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboFOODON02021803 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboNCBITaxon46259 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboNCBITaxon34816 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleMaterialTypeQualifier : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o Bb71af62f2f3e5e5b5e0fe81f24eca409 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboNCBITaxon66913 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboFOODON03411583 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboFOODON03411328 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboFOODON00004436 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboFOODON02021805 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboFOODON03413358 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboFOODON02010032 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboFOODON02020840 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboNCBITaxon126735 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OwlNamedIndividual : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OboNCBITaxon13106 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o B8aa8791a0418cd594c8b56ad21351f72 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o B00af777bec4da87c5aebb51d94b2d478 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o GeoFeature : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o HttpW3id.orgSawgraphV1Us-wqp#Site : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o OwlThing : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o MeEgadEGAD-SamplePoint : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o GeoSpatialObject : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o CosoSamplePoint : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o SosaFeatureOfInterest : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample ||--|o CosoPoint : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleCollectionMethod ||--|o RdfsLiteral : "rdfs_label"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleCollectionMethod ||--|o OwlThing : "owl_sameAs"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleDetailedLocation ||--|o RdfsLiteral : "rdfs_label"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleDetailedLocation ||--|o OwlThing : "owl_sameAs"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleMaterialType ||--|o RdfsLiteral : "rdfs_label"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleMaterialType ||--|o OwlThing : "owl_sameAs"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleMaterialTypeQualifier ||--|o RdfsLiteral : "rdfs_label"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleMaterialTypeQualifier ||--|o OwlThing : "obo_RO_0002162"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleMaterialTypeQualifier ||--|o OwlClass : "obo_RO_0002162"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleMaterialTypeQualifier ||--|o OwlThing : "owl_sameAs"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePointType : "http___w3id.org_sawgraph_v1_me-egad#samplePointType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint ||--|o OwlThing : "http___w3id.org_sawgraph_v1_me-egad#samplePointType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint ||--|o OwlNamedIndividual : "http___w3id.org_sawgraph_v1_me-egad#samplePointType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Site : "http___w3id.org_sawgraph_v1_me-egad#associatedSite"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint ||--|o MeEgadEGAD-PFAS-Site : "http___w3id.org_sawgraph_v1_me-egad#associatedSite"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint ||--|o GeoGeometry : "geo_hasGeometry"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint ||--|o HttpW3id.orgSawgraphV1Us-wqp#SampledFeature : "coso_pointFromFeature"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint ||--|o GeoFeature : "coso_pointFromFeature"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint ||--|o MeEgadEGAD-SampledFeature : "coso_pointFromFeature"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint ||--|o OwlThing : "coso_pointFromFeature"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint ||--|o CosoFeature : "coso_pointFromFeature"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampledFeature : "coso_pointFromFeature"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint ||--|o SosaFeatureOfInterest : "coso_pointFromFeature"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint ||--|o GeoSpatialObject : "coso_pointFromFeature"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint ||--|o RdfsLiteral : "dct_identifier"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint ||--|o KwgoS2CellLevel13 : "spatial_spatiallyRelatedTo"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint ||--|o KwgoAdministrativeRegion : "spatial_spatiallyRelatedTo"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint ||--|o OwlThing : "spatial_spatiallyRelatedTo"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint ||--|o MeEgadEGAD-SamplePoint : "spatial_spatiallyRelatedTo"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint ||--|o KwgoAdministrativeRegion3 : "spatial_spatiallyRelatedTo"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint : "spatial_spatiallyRelatedTo"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint ||--|o MeEgadEGAD-PFAS-Site : "spatial_spatiallyRelatedTo"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Site : "spatial_spatiallyRelatedTo"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint ||--|o GeoSpatialObject : "spatial_spatiallyRelatedTo"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint ||--|o KwgoRegion : "spatial_spatiallyRelatedTo"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint ||--|o OwlThing : "owl_sameAs"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint ||--|o GeoGeometry : "geo_hasDefaultGeometry"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint ||--|o RdfsLiteral : "rdfs_label"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint ||--|o KwgoS2CellLevel13 : "spatial_connectedTo"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint ||--|o KwgoAdministrativeRegion : "spatial_connectedTo"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint ||--|o OwlThing : "spatial_connectedTo"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint ||--|o MeEgadEGAD-SamplePoint : "spatial_connectedTo"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint ||--|o KwgoAdministrativeRegion3 : "spatial_connectedTo"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint : "spatial_connectedTo"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint ||--|o MeEgadEGAD-PFAS-Site : "spatial_connectedTo"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Site : "spatial_connectedTo"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint ||--|o GeoSpatialObject : "spatial_connectedTo"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint ||--|o KwgoRegion : "spatial_connectedTo"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePointType ||--|o RdfsLiteral : "rdfs_label"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePointType ||--|o OwlThing : "owl_sameAs"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleTreatmentStatus ||--|o RdfsLiteral : "rdfs_label"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleTreatmentStatus ||--|o OwlThing : "owl_sameAs"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SampledFeature ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePointType : "http___w3id.org_sawgraph_v1_me-egad#sampledFeatureType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SampledFeature ||--|o OwlThing : "http___w3id.org_sawgraph_v1_me-egad#sampledFeatureType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SampledFeature ||--|o OwlNamedIndividual : "http___w3id.org_sawgraph_v1_me-egad#sampledFeatureType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SampledFeature ||--|o CosoFeatureType : "http___w3id.org_sawgraph_v1_me-egad#sampledFeatureType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SampledFeature ||--|o RdfsLiteral : "rdfs_label"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SampledFeature ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePointType : "coso_ofFeatureType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SampledFeature ||--|o OwlThing : "coso_ofFeatureType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SampledFeature ||--|o OwlNamedIndividual : "coso_ofFeatureType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SampledFeature ||--|o CosoFeatureType : "coso_ofFeatureType"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SampledFeature ||--|o OwlThing : "owl_sameAs"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SinglePFAS-Concentration ||--|o MeEgadEGAD-ConcentrationQualifier : "coso_resultAnnotation"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SinglePFAS-Concentration ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-ValidationLevel : "coso_resultAnnotation"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SinglePFAS-Concentration ||--|o OwlNamedIndividual : "coso_resultAnnotation"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SinglePFAS-Concentration ||--|o MeEgadEGAD-MethodDetectionLimit : "coso_resultAnnotation"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SinglePFAS-Concentration ||--|o MeEgadEGAD-ValidationLevel : "coso_resultAnnotation"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SinglePFAS-Concentration ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-ReportingLimit : "coso_resultAnnotation"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SinglePFAS-Concentration ||--|o OwlThing : "coso_resultAnnotation"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SinglePFAS-Concentration ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-ConcentrationQualifier : "coso_resultAnnotation"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SinglePFAS-Concentration ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-MethodDetectionLimit : "coso_resultAnnotation"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SinglePFAS-Concentration ||--|o MeEgadEGAD-ReportingLimit : "coso_resultAnnotation"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SinglePFAS-Concentration ||--|o QudtEnumeratedValue : "coso_measurementValue"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SinglePFAS-Concentration ||--|o QudtConcept : "coso_measurementValue"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SinglePFAS-Concentration ||--|o QudtVerifiable : "coso_measurementValue"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SinglePFAS-Concentration ||--|o CosoResultQualifier : "http___w3id.org_sawgraph_v1_me-egad#methodDetectionLimit"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SinglePFAS-Concentration ||--|o CosoDetectionLimit : "http___w3id.org_sawgraph_v1_me-egad#methodDetectionLimit"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SinglePFAS-Concentration ||--|o OwlThing : "http___w3id.org_sawgraph_v1_me-egad#methodDetectionLimit"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SinglePFAS-Concentration ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-MethodDetectionLimit : "http___w3id.org_sawgraph_v1_me-egad#methodDetectionLimit"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SinglePFAS-Concentration ||--|o QudtQuantifiable : "http___w3id.org_sawgraph_v1_me-egad#methodDetectionLimit"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SinglePFAS-Concentration ||--|o QudtQuantity : "http___w3id.org_sawgraph_v1_me-egad#methodDetectionLimit"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SinglePFAS-Concentration ||--|o QudtConcept : "http___w3id.org_sawgraph_v1_me-egad#methodDetectionLimit"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SinglePFAS-Concentration ||--|o StadDatapoint : "http___w3id.org_sawgraph_v1_me-egad#methodDetectionLimit"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SinglePFAS-Concentration ||--|o QudtQuantityKind : "qudt_hasQuantityKind"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SinglePFAS-Concentration ||--|o OwlThing : "http___w3id.org_sawgraph_v1_me-egad#validationQualifier"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SinglePFAS-Concentration ||--|o OwlNamedIndividual : "http___w3id.org_sawgraph_v1_me-egad#validationQualifier"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SinglePFAS-Concentration ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-ConcentrationQualifier : "http___w3id.org_sawgraph_v1_me-egad#validationQualifier"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SinglePFAS-Concentration ||--|o OwlThing : "owl_sameAs"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SinglePFAS-Concentration ||--|o QudtConcept : "coso_measurementUnit"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SinglePFAS-Concentration ||--|o QudtUnit : "coso_measurementUnit"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SinglePFAS-Concentration ||--|o QudtQuantityValue : "qudt_quantityValue"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SinglePFAS-Concentration ||--|o RdfsLiteral : "rdfs_label"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SinglePFAS-Concentration ||--|o OwlNamedIndividual : "http___w3id.org_sawgraph_v1_me-egad#labQualifier"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SinglePFAS-Concentration ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-ConcentrationQualifier : "http___w3id.org_sawgraph_v1_me-egad#labQualifier"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SinglePFAS-Concentration ||--|o CosoQuantitationLimit : "http___w3id.org_sawgraph_v1_me-egad#reportingLimit"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SinglePFAS-Concentration ||--|o CosoResultQualifier : "http___w3id.org_sawgraph_v1_me-egad#reportingLimit"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SinglePFAS-Concentration ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-ReportingLimit : "http___w3id.org_sawgraph_v1_me-egad#reportingLimit"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SinglePFAS-Concentration ||--|o OwlThing : "http___w3id.org_sawgraph_v1_me-egad#reportingLimit"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SinglePFAS-Concentration ||--|o QudtQuantifiable : "http___w3id.org_sawgraph_v1_me-egad#reportingLimit"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SinglePFAS-Concentration ||--|o QudtQuantity : "http___w3id.org_sawgraph_v1_me-egad#reportingLimit"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SinglePFAS-Concentration ||--|o QudtConcept : "http___w3id.org_sawgraph_v1_me-egad#reportingLimit"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SinglePFAS-Concentration ||--|o StadDatapoint : "http___w3id.org_sawgraph_v1_me-egad#reportingLimit"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SinglePFAS-Concentration ||--|o OwlNamedIndividual : "stad_hasQualityKind"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SinglePFAS-Concentration ||--|o QudtQuantityKind : "stad_hasQualityKind"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SinglePFAS-Concentration ||--|o CosoContaminantConcentrationQuantityKind : "stad_hasQualityKind"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SinglePFAS-Concentration ||--|o CosoContaminationProperty : "stad_hasQualityKind"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SinglePFAS-Concentration ||--|o StadQualityKind : "stad_hasQualityKind"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SinglePFAS-Concentration ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-ValidationLevel : "http___w3id.org_sawgraph_v1_me-egad#validationLevel"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SinglePFAS-Concentration ||--|o OwlNamedIndividual : "http___w3id.org_sawgraph_v1_me-egad#validationLevel"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SinglePFAS-Concentration ||--|o OwlThing : "http___w3id.org_sawgraph_v1_me-egad#validationLevel"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SiteType ||--|o RdfsLiteral : "rdfs_label"
HttpW3id.orgSawgraphV1Me-egad#EGAD-SiteType ||--|o OwlThing : "owl_sameAs"
HttpW3id.orgSawgraphV1Me-egad#EGAD-ValidationLevel ||--|o RdfsLiteral : "rdfs_label"
HttpW3id.orgSawgraphV1Me-egad#EGAD-ValidationLevel ||--|o OwlThing : "owl_sameAs"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o CosoSampledFeature : "coso_isSampleOf"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o GeoFeature : "coso_isSampleOf"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OwlThing : "coso_isSampleOf"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o CosoFeature : "coso_isSampleOf"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampledFeature : "coso_isSampleOf"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o SosaFeatureOfInterest : "coso_isSampleOf"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o GeoSpatialObject : "coso_isSampleOf"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o MeEgadEGAD-SampleCollectionMethod : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OwlNamedIndividual : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o MeEgadEGAD-SampleDetailedLocation : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o CosoSampleAnnotation : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleDetailedLocation : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o MeEgadEGAD-SampleTreatmentStatus : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleTreatmentStatus : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OwlThing : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleCollectionMethod : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OwlThing : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionMethod"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OwlNamedIndividual : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionMethod"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleCollectionMethod : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionMethod"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o CosoSampleAnnotation : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionMethod"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o RdfsLiteral : "dct_identifier"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OwlThing : "owl_sameAs"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o ProvAgent : "prov_wasAttributedTo"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o RdfsLiteral : "rdfs_label"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampledFeature : "sosa_isSampleOf"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboFOODON03411183 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboFOODON03411057 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboNCBITaxon283036 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboFOODON02010107 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o HttpW3id.orgSawgraphV1Us-wqp#SampleMedia : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboFOODON00003572 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o B37977f50d3140da51a9630b8a57396a1 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboFOODON03420147 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o B215b3a432e1c482d3680398a554edbbf : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o MeEgadEGAD-SampleMaterialTypeQualifier : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o B036a3008450d6ce37e35cf5a98355a60 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboNCBITaxon66912 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboNCBITaxon7971 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboFOODON03411566 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboFOODON03420194 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboNCBITaxon381124 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o Bf584e1bfd1c74de0eb37e7b926538b83 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboFOODON00001093 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o HttpW3id.orgSawgraphV1Us-wqp#Taxon : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboNCBITaxon8022 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o B44bec873efc8b96cad5f525429c64e0a : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboFOODON00002477 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OwlThing : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o B27231c83f17c76e178e0c9f5e10acc55 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboNCBITaxon6550 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboFOODON02021651 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o Ba6d85f816540f9fec5b71ba42fc2cca6 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o CosoWaterSample : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboNCBITaxon225389 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o B423a0e253807f20386fc3ccbbd7e0378 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o MeEgadEGAD-SampleMaterialType : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboNCBITaxon8182 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboFOODON02010012 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o Bbefc37cbdd03cae92dadef76b34dbf16 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboFOODON03420150 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o B085dcda89ed6aae0d3b229e767f0a1ca : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o Bb0125be5bc4dc7be7e8452e7d22445f6 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o B0d427a711311f1499a234aa8af2c66d1 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboFOODON03411236 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboNCBITaxon6604 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboFOODON03301761 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleMaterialType : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o B7728f65369357f97de36b133c9d1d5e0 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o Be047d68edc8eb3ce96d7edbad5217bfc : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboNCBITaxon8032 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboFOODON03420181 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboFOODON02010045 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboNCBITaxon154811 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboNCBITaxon27778 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o Be497d3b0c2656040c05e303873a2d541 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboFOODON00004460 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o Beb77c26f8c395403edc359fd5f6dfb28 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o B611b8dff312692e7f32a69834c787a60 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboFOODON03411324 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o B75e45ed04b2b903b9029968cada06faa : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboFOODON03420116 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboNCBITaxon225060 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o B75dbc5841338872cea35dced609fcd77 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o CosoSampleMaterialType : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboFOODON00003083 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboNCBITaxon147949 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboFOODON03411325 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboNCBITaxon7998 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboNCBITaxon8010 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o B3cc7b3721547b07a4068dc98b6444b8b : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboNCBITaxon8038 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboNCBITaxon184451 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboFOODON02010015 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o Bbf63deb85414ddecd89e46bce27e7f0a : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboFOODON00004172 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboFOODON03411457 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboNCBITaxon75288 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboFOODON03413378 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboFOODON02010042 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o B4fd286b2a5a12e342d61412628b6e4c2 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o Bf04685c17c0e71ae3c98e08c75cbdfcc : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o B623b56ef58fd82dd088819e22d655c08 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboFOODON00003425 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o B5e93e815b548435105d9273d424fa0e8 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboFOODON00002165 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboFOODON03411669 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o B53622dee107de372b2d0566f64ab6e3a : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboNCBITaxon8167 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboFOODON02020892 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboNCBITaxon27706 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o HttpW3id.orgSawgraphV1Us-wqp#TaxonGroup.FishNekton : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboFOODON00003042 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboFOODON02021803 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboNCBITaxon46259 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboNCBITaxon34816 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleMaterialTypeQualifier : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o Bb71af62f2f3e5e5b5e0fe81f24eca409 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboNCBITaxon66913 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboFOODON03411583 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboFOODON03411328 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboFOODON00004436 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboFOODON02021805 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboFOODON03413358 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboFOODON02010032 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboFOODON02020840 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboNCBITaxon126735 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OwlNamedIndividual : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OboNCBITaxon13106 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o B8aa8791a0418cd594c8b56ad21351f72 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o B00af777bec4da87c5aebb51d94b2d478 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o GeoFeature : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o HttpW3id.orgSawgraphV1Us-wqp#Site : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o OwlThing : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o MeEgadEGAD-SamplePoint : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o GeoSpatialObject : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o CosoSamplePoint : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o SosaFeatureOfInterest : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample ||--|o CosoPoint : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o CosoSampledFeature : "coso_isSampleOf"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o GeoFeature : "coso_isSampleOf"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OwlThing : "coso_isSampleOf"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o CosoFeature : "coso_isSampleOf"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampledFeature : "coso_isSampleOf"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o SosaFeatureOfInterest : "coso_isSampleOf"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o GeoSpatialObject : "coso_isSampleOf"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o MeEgadEGAD-SampleCollectionMethod : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OwlNamedIndividual : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o MeEgadEGAD-SampleDetailedLocation : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o CosoSampleAnnotation : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleDetailedLocation : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o MeEgadEGAD-SampleTreatmentStatus : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleTreatmentStatus : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OwlThing : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleCollectionMethod : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleDetailedLocation : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionLocation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OwlThing : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionLocation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OwlNamedIndividual : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionLocation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o CosoSampleAnnotation : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionLocation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OwlThing : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionMethod"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OwlNamedIndividual : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionMethod"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleCollectionMethod : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionMethod"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o CosoSampleAnnotation : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionMethod"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o RdfsLiteral : "dct_identifier"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OwlThing : "http___w3id.org_sawgraph_v1_me-egad#sampleTreatmentStatus"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OwlNamedIndividual : "http___w3id.org_sawgraph_v1_me-egad#sampleTreatmentStatus"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleTreatmentStatus : "http___w3id.org_sawgraph_v1_me-egad#sampleTreatmentStatus"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o CosoSampleAnnotation : "http___w3id.org_sawgraph_v1_me-egad#sampleTreatmentStatus"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OwlThing : "owl_sameAs"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o ProvAgent : "prov_wasAttributedTo"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o RdfsLiteral : "rdfs_label"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampledFeature : "sosa_isSampleOf"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboFOODON03411183 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboFOODON03411057 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboNCBITaxon283036 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboFOODON02010107 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o HttpW3id.orgSawgraphV1Us-wqp#SampleMedia : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboFOODON00003572 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o B37977f50d3140da51a9630b8a57396a1 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboFOODON03420147 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o B215b3a432e1c482d3680398a554edbbf : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o MeEgadEGAD-SampleMaterialTypeQualifier : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o B036a3008450d6ce37e35cf5a98355a60 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboNCBITaxon66912 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboNCBITaxon7971 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboFOODON03411566 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboFOODON03420194 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboNCBITaxon381124 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o Bf584e1bfd1c74de0eb37e7b926538b83 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboFOODON00001093 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o HttpW3id.orgSawgraphV1Us-wqp#Taxon : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboNCBITaxon8022 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o B44bec873efc8b96cad5f525429c64e0a : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboFOODON00002477 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OwlThing : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o B27231c83f17c76e178e0c9f5e10acc55 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboNCBITaxon6550 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboFOODON02021651 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o Ba6d85f816540f9fec5b71ba42fc2cca6 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o CosoWaterSample : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboNCBITaxon225389 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o B423a0e253807f20386fc3ccbbd7e0378 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o MeEgadEGAD-SampleMaterialType : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboNCBITaxon8182 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboFOODON02010012 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o Bbefc37cbdd03cae92dadef76b34dbf16 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboFOODON03420150 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o B085dcda89ed6aae0d3b229e767f0a1ca : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o Bb0125be5bc4dc7be7e8452e7d22445f6 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o B0d427a711311f1499a234aa8af2c66d1 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboFOODON03411236 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboNCBITaxon6604 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboFOODON03301761 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleMaterialType : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o B7728f65369357f97de36b133c9d1d5e0 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o Be047d68edc8eb3ce96d7edbad5217bfc : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboNCBITaxon8032 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboFOODON03420181 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboFOODON02010045 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboNCBITaxon154811 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboNCBITaxon27778 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o Be497d3b0c2656040c05e303873a2d541 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboFOODON00004460 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o Beb77c26f8c395403edc359fd5f6dfb28 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o B611b8dff312692e7f32a69834c787a60 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboFOODON03411324 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o B75e45ed04b2b903b9029968cada06faa : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboFOODON03420116 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboNCBITaxon225060 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o B75dbc5841338872cea35dced609fcd77 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o CosoSampleMaterialType : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboFOODON00003083 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboNCBITaxon147949 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboFOODON03411325 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboNCBITaxon7998 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboNCBITaxon8010 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o B3cc7b3721547b07a4068dc98b6444b8b : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboNCBITaxon8038 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboNCBITaxon184451 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboFOODON02010015 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o Bbf63deb85414ddecd89e46bce27e7f0a : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboFOODON00004172 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboFOODON03411457 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboNCBITaxon75288 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboFOODON03413378 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboFOODON02010042 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o B4fd286b2a5a12e342d61412628b6e4c2 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o Bf04685c17c0e71ae3c98e08c75cbdfcc : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o B623b56ef58fd82dd088819e22d655c08 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboFOODON00003425 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o B5e93e815b548435105d9273d424fa0e8 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboFOODON00002165 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboFOODON03411669 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o B53622dee107de372b2d0566f64ab6e3a : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboNCBITaxon8167 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboFOODON02020892 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboNCBITaxon27706 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o HttpW3id.orgSawgraphV1Us-wqp#TaxonGroup.FishNekton : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboFOODON00003042 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboFOODON02021803 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboNCBITaxon46259 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboNCBITaxon34816 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleMaterialTypeQualifier : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o Bb71af62f2f3e5e5b5e0fe81f24eca409 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboNCBITaxon66913 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboFOODON03411583 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboFOODON03411328 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboFOODON00004436 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboFOODON02021805 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboFOODON03413358 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboFOODON02010032 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboFOODON02020840 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboNCBITaxon126735 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OwlNamedIndividual : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OboNCBITaxon13106 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o B8aa8791a0418cd594c8b56ad21351f72 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o B00af777bec4da87c5aebb51d94b2d478 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o GeoFeature : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o HttpW3id.orgSawgraphV1Us-wqp#Site : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o OwlThing : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o MeEgadEGAD-SamplePoint : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o GeoSpatialObject : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o CosoSamplePoint : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o SosaFeatureOfInterest : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample ||--|o CosoPoint : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o CosoSampledFeature : "coso_isSampleOf"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o GeoFeature : "coso_isSampleOf"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OwlThing : "coso_isSampleOf"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o CosoFeature : "coso_isSampleOf"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampledFeature : "coso_isSampleOf"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o SosaFeatureOfInterest : "coso_isSampleOf"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o GeoSpatialObject : "coso_isSampleOf"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o MeEgadEGAD-SampleCollectionMethod : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OwlNamedIndividual : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o MeEgadEGAD-SampleDetailedLocation : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o CosoSampleAnnotation : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleDetailedLocation : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o MeEgadEGAD-SampleTreatmentStatus : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleTreatmentStatus : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OwlThing : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleCollectionMethod : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleDetailedLocation : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionLocation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OwlThing : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionLocation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OwlNamedIndividual : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionLocation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o CosoSampleAnnotation : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionLocation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OwlThing : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionMethod"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OwlNamedIndividual : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionMethod"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleCollectionMethod : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionMethod"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o CosoSampleAnnotation : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionMethod"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o RdfsLiteral : "dct_identifier"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OwlThing : "http___w3id.org_sawgraph_v1_me-egad#sampleTreatmentStatus"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OwlNamedIndividual : "http___w3id.org_sawgraph_v1_me-egad#sampleTreatmentStatus"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleTreatmentStatus : "http___w3id.org_sawgraph_v1_me-egad#sampleTreatmentStatus"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o CosoSampleAnnotation : "http___w3id.org_sawgraph_v1_me-egad#sampleTreatmentStatus"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OwlThing : "owl_sameAs"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o ProvAgent : "prov_wasAttributedTo"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o RdfsLiteral : "rdfs_label"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampledFeature : "sosa_isSampleOf"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboFOODON03411183 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboFOODON03411057 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboNCBITaxon283036 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboFOODON02010107 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o HttpW3id.orgSawgraphV1Us-wqp#SampleMedia : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboFOODON00003572 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o B37977f50d3140da51a9630b8a57396a1 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboFOODON03420147 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o B215b3a432e1c482d3680398a554edbbf : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o MeEgadEGAD-SampleMaterialTypeQualifier : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o B036a3008450d6ce37e35cf5a98355a60 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboNCBITaxon66912 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboNCBITaxon7971 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboFOODON03411566 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboFOODON03420194 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboNCBITaxon381124 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o Bf584e1bfd1c74de0eb37e7b926538b83 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboFOODON00001093 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o HttpW3id.orgSawgraphV1Us-wqp#Taxon : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboNCBITaxon8022 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o B44bec873efc8b96cad5f525429c64e0a : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboFOODON00002477 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OwlThing : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o B27231c83f17c76e178e0c9f5e10acc55 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboNCBITaxon6550 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboFOODON02021651 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o Ba6d85f816540f9fec5b71ba42fc2cca6 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o CosoWaterSample : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboNCBITaxon225389 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o B423a0e253807f20386fc3ccbbd7e0378 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o MeEgadEGAD-SampleMaterialType : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboNCBITaxon8182 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboFOODON02010012 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o Bbefc37cbdd03cae92dadef76b34dbf16 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboFOODON03420150 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o B085dcda89ed6aae0d3b229e767f0a1ca : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o Bb0125be5bc4dc7be7e8452e7d22445f6 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o B0d427a711311f1499a234aa8af2c66d1 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboFOODON03411236 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboNCBITaxon6604 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboFOODON03301761 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleMaterialType : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o B7728f65369357f97de36b133c9d1d5e0 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o Be047d68edc8eb3ce96d7edbad5217bfc : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboNCBITaxon8032 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboFOODON03420181 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboFOODON02010045 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboNCBITaxon154811 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboNCBITaxon27778 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o Be497d3b0c2656040c05e303873a2d541 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboFOODON00004460 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o Beb77c26f8c395403edc359fd5f6dfb28 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o B611b8dff312692e7f32a69834c787a60 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboFOODON03411324 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o B75e45ed04b2b903b9029968cada06faa : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboFOODON03420116 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboNCBITaxon225060 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o B75dbc5841338872cea35dced609fcd77 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o CosoSampleMaterialType : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboFOODON00003083 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboNCBITaxon147949 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboFOODON03411325 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboNCBITaxon7998 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboNCBITaxon8010 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o B3cc7b3721547b07a4068dc98b6444b8b : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboNCBITaxon8038 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboNCBITaxon184451 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboFOODON02010015 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o Bbf63deb85414ddecd89e46bce27e7f0a : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboFOODON00004172 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboFOODON03411457 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboNCBITaxon75288 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboFOODON03413378 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboFOODON02010042 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o B4fd286b2a5a12e342d61412628b6e4c2 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o Bf04685c17c0e71ae3c98e08c75cbdfcc : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o B623b56ef58fd82dd088819e22d655c08 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboFOODON00003425 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o B5e93e815b548435105d9273d424fa0e8 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboFOODON00002165 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboFOODON03411669 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o B53622dee107de372b2d0566f64ab6e3a : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboNCBITaxon8167 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboFOODON02020892 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboNCBITaxon27706 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o HttpW3id.orgSawgraphV1Us-wqp#TaxonGroup.FishNekton : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboFOODON00003042 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboFOODON02021803 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboNCBITaxon46259 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboNCBITaxon34816 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleMaterialTypeQualifier : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o Bb71af62f2f3e5e5b5e0fe81f24eca409 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboNCBITaxon66913 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboFOODON03411583 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboFOODON03411328 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboFOODON00004436 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboFOODON02021805 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboFOODON03413358 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboFOODON02010032 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboFOODON02020840 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboNCBITaxon126735 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OwlNamedIndividual : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OboNCBITaxon13106 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o B8aa8791a0418cd594c8b56ad21351f72 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o B00af777bec4da87c5aebb51d94b2d478 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o GeoFeature : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o HttpW3id.orgSawgraphV1Us-wqp#Site : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o OwlThing : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o MeEgadEGAD-SamplePoint : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o GeoSpatialObject : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o CosoSamplePoint : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o SosaFeatureOfInterest : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample ||--|o CosoPoint : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o CosoSampledFeature : "coso_isSampleOf"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o GeoFeature : "coso_isSampleOf"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OwlThing : "coso_isSampleOf"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o CosoFeature : "coso_isSampleOf"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampledFeature : "coso_isSampleOf"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o SosaFeatureOfInterest : "coso_isSampleOf"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o GeoSpatialObject : "coso_isSampleOf"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o MeEgadEGAD-SampleCollectionMethod : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OwlNamedIndividual : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o MeEgadEGAD-SampleDetailedLocation : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o CosoSampleAnnotation : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleDetailedLocation : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o MeEgadEGAD-SampleTreatmentStatus : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleTreatmentStatus : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OwlThing : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleCollectionMethod : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OwlThing : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionMethod"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OwlNamedIndividual : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionMethod"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleCollectionMethod : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionMethod"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o CosoSampleAnnotation : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionMethod"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o RdfsLiteral : "dct_identifier"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OwlThing : "owl_sameAs"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o ProvAgent : "prov_wasAttributedTo"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o RdfsLiteral : "rdfs_label"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampledFeature : "sosa_isSampleOf"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboFOODON03411183 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboFOODON03411057 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboNCBITaxon283036 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboFOODON02010107 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o HttpW3id.orgSawgraphV1Us-wqp#SampleMedia : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboFOODON00003572 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o B37977f50d3140da51a9630b8a57396a1 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboFOODON03420147 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o B215b3a432e1c482d3680398a554edbbf : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o MeEgadEGAD-SampleMaterialTypeQualifier : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o B036a3008450d6ce37e35cf5a98355a60 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboNCBITaxon66912 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboNCBITaxon7971 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboFOODON03411566 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboFOODON03420194 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboNCBITaxon381124 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o Bf584e1bfd1c74de0eb37e7b926538b83 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboFOODON00001093 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o HttpW3id.orgSawgraphV1Us-wqp#Taxon : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboNCBITaxon8022 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o B44bec873efc8b96cad5f525429c64e0a : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboFOODON00002477 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OwlThing : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o B27231c83f17c76e178e0c9f5e10acc55 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboNCBITaxon6550 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboFOODON02021651 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o Ba6d85f816540f9fec5b71ba42fc2cca6 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o CosoWaterSample : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboNCBITaxon225389 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o B423a0e253807f20386fc3ccbbd7e0378 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o MeEgadEGAD-SampleMaterialType : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboNCBITaxon8182 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboFOODON02010012 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o Bbefc37cbdd03cae92dadef76b34dbf16 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboFOODON03420150 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o B085dcda89ed6aae0d3b229e767f0a1ca : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o Bb0125be5bc4dc7be7e8452e7d22445f6 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o B0d427a711311f1499a234aa8af2c66d1 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboFOODON03411236 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboNCBITaxon6604 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboFOODON03301761 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleMaterialType : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o B7728f65369357f97de36b133c9d1d5e0 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o Be047d68edc8eb3ce96d7edbad5217bfc : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboNCBITaxon8032 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboFOODON03420181 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboFOODON02010045 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboNCBITaxon154811 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboNCBITaxon27778 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o Be497d3b0c2656040c05e303873a2d541 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboFOODON00004460 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o Beb77c26f8c395403edc359fd5f6dfb28 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o B611b8dff312692e7f32a69834c787a60 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboFOODON03411324 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o B75e45ed04b2b903b9029968cada06faa : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboFOODON03420116 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboNCBITaxon225060 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o B75dbc5841338872cea35dced609fcd77 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o CosoSampleMaterialType : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboFOODON00003083 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboNCBITaxon147949 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboFOODON03411325 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboNCBITaxon7998 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboNCBITaxon8010 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o B3cc7b3721547b07a4068dc98b6444b8b : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboNCBITaxon8038 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboNCBITaxon184451 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboFOODON02010015 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o Bbf63deb85414ddecd89e46bce27e7f0a : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboFOODON00004172 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboFOODON03411457 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboNCBITaxon75288 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboFOODON03413378 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboFOODON02010042 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o B4fd286b2a5a12e342d61412628b6e4c2 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o Bf04685c17c0e71ae3c98e08c75cbdfcc : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o B623b56ef58fd82dd088819e22d655c08 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboFOODON00003425 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o B5e93e815b548435105d9273d424fa0e8 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboFOODON00002165 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboFOODON03411669 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o B53622dee107de372b2d0566f64ab6e3a : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboNCBITaxon8167 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboFOODON02020892 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboNCBITaxon27706 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o HttpW3id.orgSawgraphV1Us-wqp#TaxonGroup.FishNekton : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboFOODON00003042 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboFOODON02021803 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboNCBITaxon46259 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboNCBITaxon34816 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleMaterialTypeQualifier : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o Bb71af62f2f3e5e5b5e0fe81f24eca409 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboNCBITaxon66913 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboFOODON03411583 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboFOODON03411328 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboFOODON00004436 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboFOODON02021805 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboFOODON03413358 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboFOODON02010032 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboFOODON02020840 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboNCBITaxon126735 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OwlNamedIndividual : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OboNCBITaxon13106 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o B8aa8791a0418cd594c8b56ad21351f72 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o B00af777bec4da87c5aebb51d94b2d478 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o GeoFeature : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o HttpW3id.orgSawgraphV1Us-wqp#Site : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o OwlThing : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o MeEgadEGAD-SamplePoint : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o GeoSpatialObject : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o CosoSamplePoint : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o SosaFeatureOfInterest : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample ||--|o CosoPoint : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o CosoSampledFeature : "coso_isSampleOf"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o GeoFeature : "coso_isSampleOf"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OwlThing : "coso_isSampleOf"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o CosoFeature : "coso_isSampleOf"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampledFeature : "coso_isSampleOf"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o SosaFeatureOfInterest : "coso_isSampleOf"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o GeoSpatialObject : "coso_isSampleOf"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o MeEgadEGAD-SampleCollectionMethod : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OwlNamedIndividual : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o MeEgadEGAD-SampleDetailedLocation : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o CosoSampleAnnotation : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleDetailedLocation : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o MeEgadEGAD-SampleTreatmentStatus : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleTreatmentStatus : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OwlThing : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleCollectionMethod : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleDetailedLocation : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionLocation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OwlThing : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionLocation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OwlNamedIndividual : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionLocation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o CosoSampleAnnotation : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionLocation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OwlThing : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionMethod"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OwlNamedIndividual : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionMethod"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleCollectionMethod : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionMethod"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o CosoSampleAnnotation : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionMethod"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o RdfsLiteral : "dct_identifier"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OwlThing : "owl_sameAs"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OwlThing : "http___w3id.org_sawgraph_v1_me-egad#sampleTreatmentStatus"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OwlNamedIndividual : "http___w3id.org_sawgraph_v1_me-egad#sampleTreatmentStatus"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleTreatmentStatus : "http___w3id.org_sawgraph_v1_me-egad#sampleTreatmentStatus"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o CosoSampleAnnotation : "http___w3id.org_sawgraph_v1_me-egad#sampleTreatmentStatus"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o ProvAgent : "prov_wasAttributedTo"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o RdfsLiteral : "rdfs_label"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampledFeature : "sosa_isSampleOf"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboFOODON03411183 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboFOODON03411057 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboNCBITaxon283036 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboFOODON02010107 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o HttpW3id.orgSawgraphV1Us-wqp#SampleMedia : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboFOODON00003572 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o B37977f50d3140da51a9630b8a57396a1 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboFOODON03420147 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o B215b3a432e1c482d3680398a554edbbf : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o MeEgadEGAD-SampleMaterialTypeQualifier : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o B036a3008450d6ce37e35cf5a98355a60 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboNCBITaxon66912 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboNCBITaxon7971 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboFOODON03411566 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboFOODON03420194 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboNCBITaxon381124 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o Bf584e1bfd1c74de0eb37e7b926538b83 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboFOODON00001093 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o HttpW3id.orgSawgraphV1Us-wqp#Taxon : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboNCBITaxon8022 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o B44bec873efc8b96cad5f525429c64e0a : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboFOODON00002477 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OwlThing : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o B27231c83f17c76e178e0c9f5e10acc55 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboNCBITaxon6550 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboFOODON02021651 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o Ba6d85f816540f9fec5b71ba42fc2cca6 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o CosoWaterSample : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboNCBITaxon225389 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o B423a0e253807f20386fc3ccbbd7e0378 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o MeEgadEGAD-SampleMaterialType : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboNCBITaxon8182 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboFOODON02010012 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o Bbefc37cbdd03cae92dadef76b34dbf16 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboFOODON03420150 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o B085dcda89ed6aae0d3b229e767f0a1ca : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o Bb0125be5bc4dc7be7e8452e7d22445f6 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o B0d427a711311f1499a234aa8af2c66d1 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboFOODON03411236 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboNCBITaxon6604 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboFOODON03301761 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleMaterialType : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o B7728f65369357f97de36b133c9d1d5e0 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o Be047d68edc8eb3ce96d7edbad5217bfc : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboNCBITaxon8032 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboFOODON03420181 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboFOODON02010045 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboNCBITaxon154811 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboNCBITaxon27778 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o Be497d3b0c2656040c05e303873a2d541 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboFOODON00004460 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o Beb77c26f8c395403edc359fd5f6dfb28 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o B611b8dff312692e7f32a69834c787a60 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboFOODON03411324 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o B75e45ed04b2b903b9029968cada06faa : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboFOODON03420116 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboNCBITaxon225060 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o B75dbc5841338872cea35dced609fcd77 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o CosoSampleMaterialType : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboFOODON00003083 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboNCBITaxon147949 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboFOODON03411325 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboNCBITaxon7998 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboNCBITaxon8010 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o B3cc7b3721547b07a4068dc98b6444b8b : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboNCBITaxon8038 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboNCBITaxon184451 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboFOODON02010015 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o Bbf63deb85414ddecd89e46bce27e7f0a : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboFOODON00004172 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboFOODON03411457 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboNCBITaxon75288 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboFOODON03413378 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboFOODON02010042 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o B4fd286b2a5a12e342d61412628b6e4c2 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o Bf04685c17c0e71ae3c98e08c75cbdfcc : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o B623b56ef58fd82dd088819e22d655c08 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboFOODON00003425 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o B5e93e815b548435105d9273d424fa0e8 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboFOODON00002165 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboFOODON03411669 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o B53622dee107de372b2d0566f64ab6e3a : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboNCBITaxon8167 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboFOODON02020892 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboNCBITaxon27706 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o HttpW3id.orgSawgraphV1Us-wqp#TaxonGroup.FishNekton : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboFOODON00003042 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboFOODON02021803 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboNCBITaxon46259 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboNCBITaxon34816 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleMaterialTypeQualifier : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o Bb71af62f2f3e5e5b5e0fe81f24eca409 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboNCBITaxon66913 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboFOODON03411583 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboFOODON03411328 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboFOODON00004436 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboFOODON02021805 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboFOODON03413358 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboFOODON02010032 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboFOODON02020840 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboNCBITaxon126735 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OwlNamedIndividual : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OboNCBITaxon13106 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o B8aa8791a0418cd594c8b56ad21351f72 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o B00af777bec4da87c5aebb51d94b2d478 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o GeoFeature : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o HttpW3id.orgSawgraphV1Us-wqp#Site : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o OwlThing : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o MeEgadEGAD-SamplePoint : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o GeoSpatialObject : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o CosoSamplePoint : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o SosaFeatureOfInterest : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample ||--|o CosoPoint : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o CosoSampledFeature : "coso_isSampleOf"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o GeoFeature : "coso_isSampleOf"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OwlThing : "coso_isSampleOf"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o CosoFeature : "coso_isSampleOf"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampledFeature : "coso_isSampleOf"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o SosaFeatureOfInterest : "coso_isSampleOf"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o GeoSpatialObject : "coso_isSampleOf"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o MeEgadEGAD-SampleCollectionMethod : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OwlNamedIndividual : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o MeEgadEGAD-SampleDetailedLocation : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o CosoSampleAnnotation : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleDetailedLocation : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o MeEgadEGAD-SampleTreatmentStatus : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleTreatmentStatus : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OwlThing : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleCollectionMethod : "coso_sampleAnnotation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleDetailedLocation : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionLocation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OwlThing : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionLocation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OwlNamedIndividual : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionLocation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o CosoSampleAnnotation : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionLocation"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OwlThing : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionMethod"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OwlNamedIndividual : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionMethod"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleCollectionMethod : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionMethod"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o CosoSampleAnnotation : "http___w3id.org_sawgraph_v1_me-egad#sampleCollectionMethod"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o RdfsLiteral : "dct_identifier"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OwlThing : "owl_sameAs"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OwlThing : "http___w3id.org_sawgraph_v1_me-egad#sampleTreatmentStatus"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OwlNamedIndividual : "http___w3id.org_sawgraph_v1_me-egad#sampleTreatmentStatus"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleTreatmentStatus : "http___w3id.org_sawgraph_v1_me-egad#sampleTreatmentStatus"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o CosoSampleAnnotation : "http___w3id.org_sawgraph_v1_me-egad#sampleTreatmentStatus"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o ProvAgent : "prov_wasAttributedTo"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o RdfsLiteral : "rdfs_label"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampledFeature : "sosa_isSampleOf"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboFOODON03411183 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboFOODON03411057 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboNCBITaxon283036 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboFOODON02010107 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o HttpW3id.orgSawgraphV1Us-wqp#SampleMedia : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboFOODON00003572 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o B37977f50d3140da51a9630b8a57396a1 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboFOODON03420147 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o B215b3a432e1c482d3680398a554edbbf : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o MeEgadEGAD-SampleMaterialTypeQualifier : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o B036a3008450d6ce37e35cf5a98355a60 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboNCBITaxon66912 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboNCBITaxon7971 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboFOODON03411566 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboFOODON03420194 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboNCBITaxon381124 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o Bf584e1bfd1c74de0eb37e7b926538b83 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboFOODON00001093 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o HttpW3id.orgSawgraphV1Us-wqp#Taxon : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboNCBITaxon8022 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o B44bec873efc8b96cad5f525429c64e0a : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboFOODON00002477 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OwlThing : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o B27231c83f17c76e178e0c9f5e10acc55 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboNCBITaxon6550 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboFOODON02021651 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o Ba6d85f816540f9fec5b71ba42fc2cca6 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o CosoWaterSample : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboNCBITaxon225389 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o B423a0e253807f20386fc3ccbbd7e0378 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o MeEgadEGAD-SampleMaterialType : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboNCBITaxon8182 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboFOODON02010012 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o Bbefc37cbdd03cae92dadef76b34dbf16 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboFOODON03420150 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o B085dcda89ed6aae0d3b229e767f0a1ca : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o Bb0125be5bc4dc7be7e8452e7d22445f6 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o B0d427a711311f1499a234aa8af2c66d1 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboFOODON03411236 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboNCBITaxon6604 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboFOODON03301761 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleMaterialType : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o B7728f65369357f97de36b133c9d1d5e0 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o Be047d68edc8eb3ce96d7edbad5217bfc : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboNCBITaxon8032 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboFOODON03420181 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboFOODON02010045 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboNCBITaxon154811 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboNCBITaxon27778 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o Be497d3b0c2656040c05e303873a2d541 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboFOODON00004460 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o Beb77c26f8c395403edc359fd5f6dfb28 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o B611b8dff312692e7f32a69834c787a60 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboFOODON03411324 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o B75e45ed04b2b903b9029968cada06faa : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboFOODON03420116 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboNCBITaxon225060 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o B75dbc5841338872cea35dced609fcd77 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o CosoSampleMaterialType : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboFOODON00003083 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboNCBITaxon147949 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboFOODON03411325 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboNCBITaxon7998 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboNCBITaxon8010 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o B3cc7b3721547b07a4068dc98b6444b8b : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboNCBITaxon8038 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboNCBITaxon184451 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboFOODON02010015 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o Bbf63deb85414ddecd89e46bce27e7f0a : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboFOODON00004172 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboFOODON03411457 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboNCBITaxon75288 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboFOODON03413378 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboFOODON02010042 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o B4fd286b2a5a12e342d61412628b6e4c2 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o Bf04685c17c0e71ae3c98e08c75cbdfcc : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o B623b56ef58fd82dd088819e22d655c08 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboFOODON00003425 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o B5e93e815b548435105d9273d424fa0e8 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboFOODON00002165 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboFOODON03411669 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o B53622dee107de372b2d0566f64ab6e3a : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboNCBITaxon8167 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboFOODON02020892 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboNCBITaxon27706 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o HttpW3id.orgSawgraphV1Us-wqp#TaxonGroup.FishNekton : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboFOODON00003042 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboFOODON02021803 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboNCBITaxon46259 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboNCBITaxon34816 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleMaterialTypeQualifier : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o Bb71af62f2f3e5e5b5e0fe81f24eca409 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboNCBITaxon66913 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboFOODON03411583 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboFOODON03411328 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboFOODON00004436 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboFOODON02021805 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboFOODON03413358 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboFOODON02010032 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboFOODON02020840 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboNCBITaxon126735 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OwlNamedIndividual : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OboNCBITaxon13106 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o B8aa8791a0418cd594c8b56ad21351f72 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o B00af777bec4da87c5aebb51d94b2d478 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o GeoFeature : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o HttpW3id.orgSawgraphV1Us-wqp#Site : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o OwlThing : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o MeEgadEGAD-SamplePoint : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o GeoSpatialObject : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o CosoSamplePoint : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o SosaFeatureOfInterest : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample ||--|o CosoPoint : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Us-wqp#AnalyticalMethod ||--|o RdfsLiteral : "rdfs_comment"
HttpW3id.orgSawgraphV1Us-wqp#AnalyticalMethod ||--|o RdfsLiteral : "rdfs_label"
HttpW3id.orgSawgraphV1Us-wqp#Characteristic ||--|o HttpW3id.orgComptoxV1ChemicalEntity : "http___w3id.org_comptox_v1_sameAsComptoxSubstance"
HttpW3id.orgSawgraphV1Us-wqp#Characteristic ||--|o RdfsLiteral : "rdfs_label"
HttpW3id.orgSawgraphV1Us-wqp#DefWQPGroundWaterFeatureType ||--|o RdfsLiteral : "rdfs_comment"
HttpW3id.orgSawgraphV1Us-wqp#DefWQPGroundWaterFeatureType ||--|o RdfsLiteral : "rdfs_label"
HttpW3id.orgSawgraphV1Us-wqp#DefWQPGroundWaterSample ||--|o RdfsLiteral : "rdfs_label"
HttpW3id.orgSawgraphV1Us-wqp#DefWQPGroundWaterSample ||--|o OwlThing : "owl_sameAs"
HttpW3id.orgSawgraphV1Us-wqp#DefWQPSurfaceWaterFeatureType ||--|o RdfsLiteral : "rdfs_comment"
HttpW3id.orgSawgraphV1Us-wqp#DefWQPSurfaceWaterFeatureType ||--|o RdfsLiteral : "rdfs_label"
HttpW3id.orgSawgraphV1Us-wqp#DefWQPSurfaceWaterSample ||--|o RdfsLiteral : "rdfs_label"
HttpW3id.orgSawgraphV1Us-wqp#DefWQPSurfaceWaterSample ||--|o OwlThing : "owl_sameAs"
HttpW3id.orgSawgraphV1Us-wqp#DefWQPWasteWaterFeatureType ||--|o RdfsLiteral : "rdfs_comment"
HttpW3id.orgSawgraphV1Us-wqp#DefWQPWasteWaterFeatureType ||--|o RdfsLiteral : "rdfs_label"
HttpW3id.orgSawgraphV1Us-wqp#DefWQPWasteWaterSample ||--|o RdfsLiteral : "rdfs_label"
HttpW3id.orgSawgraphV1Us-wqp#DefWQPWasteWaterSample ||--|o OwlThing : "owl_sameAs"
HttpW3id.orgSawgraphV1Us-wqp#FederalUSGovernmentOrganization ||--|o RdfsLiteral : "rdfs_label"
HttpW3id.orgSawgraphV1Us-wqp#InstrumentDetectionLevel ||--|o QudtUnit : "qudt_hasUnit"
HttpW3id.orgSawgraphV1Us-wqp#InstrumentDetectionLevel ||--|o QudtContextualUnit : "qudt_hasUnit"
HttpW3id.orgSawgraphV1Us-wqp#InstrumentDetectionLevel ||--|o QudtLogarithmicUnit : "qudt_hasUnit"
HttpW3id.orgSawgraphV1Us-wqp#InstrumentDetectionLevel ||--|o QudtCurrencyUnit : "qudt_hasUnit"
HttpW3id.orgSawgraphV1Us-wqp#InstrumentDetectionLevel ||--|o QudtDerivedUnit : "qudt_hasUnit"
HttpW3id.orgSawgraphV1Us-wqp#InstrumentDetectionLevel ||--|o QudtCountingUnit : "qudt_hasUnit"
HttpW3id.orgSawgraphV1Us-wqp#LaboratoryReportingLevel ||--|o QudtUnit : "qudt_hasUnit"
HttpW3id.orgSawgraphV1Us-wqp#LaboratoryReportingLevel ||--|o QudtContextualUnit : "qudt_hasUnit"
HttpW3id.orgSawgraphV1Us-wqp#LaboratoryReportingLevel ||--|o QudtLogarithmicUnit : "qudt_hasUnit"
HttpW3id.orgSawgraphV1Us-wqp#LaboratoryReportingLevel ||--|o QudtCurrencyUnit : "qudt_hasUnit"
HttpW3id.orgSawgraphV1Us-wqp#LaboratoryReportingLevel ||--|o QudtDerivedUnit : "qudt_hasUnit"
HttpW3id.orgSawgraphV1Us-wqp#LaboratoryReportingLevel ||--|o QudtCountingUnit : "qudt_hasUnit"
HttpW3id.orgSawgraphV1Us-wqp#LocationType ||--|o RdfsLiteral : "rdfs_comment"
HttpW3id.orgSawgraphV1Us-wqp#LocationType ||--|o RdfsLiteral : "rdfs_label"
HttpW3id.orgSawgraphV1Us-wqp#LowerQuantitationLimit ||--|o QudtUnit : "qudt_hasUnit"
HttpW3id.orgSawgraphV1Us-wqp#LowerQuantitationLimit ||--|o QudtContextualUnit : "qudt_hasUnit"
HttpW3id.orgSawgraphV1Us-wqp#LowerQuantitationLimit ||--|o QudtLogarithmicUnit : "qudt_hasUnit"
HttpW3id.orgSawgraphV1Us-wqp#LowerQuantitationLimit ||--|o QudtCurrencyUnit : "qudt_hasUnit"
HttpW3id.orgSawgraphV1Us-wqp#LowerQuantitationLimit ||--|o QudtDerivedUnit : "qudt_hasUnit"
HttpW3id.orgSawgraphV1Us-wqp#LowerQuantitationLimit ||--|o QudtCountingUnit : "qudt_hasUnit"
HttpW3id.orgSawgraphV1Us-wqp#LowerReportingLimit ||--|o QudtUnit : "qudt_hasUnit"
HttpW3id.orgSawgraphV1Us-wqp#LowerReportingLimit ||--|o QudtContextualUnit : "qudt_hasUnit"
HttpW3id.orgSawgraphV1Us-wqp#LowerReportingLimit ||--|o QudtLogarithmicUnit : "qudt_hasUnit"
HttpW3id.orgSawgraphV1Us-wqp#LowerReportingLimit ||--|o QudtCurrencyUnit : "qudt_hasUnit"
HttpW3id.orgSawgraphV1Us-wqp#LowerReportingLimit ||--|o QudtDerivedUnit : "qudt_hasUnit"
HttpW3id.orgSawgraphV1Us-wqp#LowerReportingLimit ||--|o QudtCountingUnit : "qudt_hasUnit"
HttpW3id.orgSawgraphV1Us-wqp#MethodDetectionLevel ||--|o QudtUnit : "qudt_hasUnit"
HttpW3id.orgSawgraphV1Us-wqp#MethodDetectionLevel ||--|o QudtContextualUnit : "qudt_hasUnit"
HttpW3id.orgSawgraphV1Us-wqp#MethodDetectionLevel ||--|o QudtLogarithmicUnit : "qudt_hasUnit"
HttpW3id.orgSawgraphV1Us-wqp#MethodDetectionLevel ||--|o QudtCurrencyUnit : "qudt_hasUnit"
HttpW3id.orgSawgraphV1Us-wqp#MethodDetectionLevel ||--|o QudtDerivedUnit : "qudt_hasUnit"
HttpW3id.orgSawgraphV1Us-wqp#MethodDetectionLevel ||--|o QudtCountingUnit : "qudt_hasUnit"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o GeoFeature : "coso_observedAtSamplePoint"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o HttpW3id.orgSawgraphV1Us-wqp#Site : "coso_observedAtSamplePoint"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o OwlThing : "coso_observedAtSamplePoint"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o MeEgadEGAD-SamplePoint : "coso_observedAtSamplePoint"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint : "coso_observedAtSamplePoint"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o GeoSpatialObject : "coso_observedAtSamplePoint"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o CosoSamplePoint : "coso_observedAtSamplePoint"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o SosaFeatureOfInterest : "coso_observedAtSamplePoint"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o CosoPoint : "coso_observedAtSamplePoint"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample : "coso_analyzedSample"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample : "coso_analyzedSample"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o SosaFeatureOfInterest : "coso_analyzedSample"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o CosoPlantMaterialSample : "coso_analyzedSample"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample : "coso_analyzedSample"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample : "coso_analyzedSample"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o MeEgadEGAD-Sample : "coso_analyzedSample"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o CosoAnimalTissueSample : "coso_analyzedSample"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o CosoAnimalOrganSample : "coso_analyzedSample"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o HttpW3id.orgSawgraphV1Us-wqp#Sample : "coso_analyzedSample"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o SosaSample : "coso_analyzedSample"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o CosoMaterialSample : "coso_analyzedSample"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o CosoAnimalMilkSample : "coso_analyzedSample"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample : "coso_analyzedSample"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o CosoAnimalBloodSample : "coso_analyzedSample"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o OwlThing : "coso_analyzedSample"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample : "coso_analyzedSample"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o CosoAnimalMaterialSample : "coso_analyzedSample"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample : "coso_analyzedSample"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SinglePFAS-Concentration : "coso_hasResult"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o MeEgadEGAD-SinglePFAS-Concentration : "coso_hasResult"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-AggregatePFAS-Concentration : "coso_hasResult"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o MeEgadEGAD-AggregatePFAS-Concentration : "coso_hasResult"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o HttpW3id.orgSawgraphV1Us-wqp#Single-PFAS-Concentration : "coso_hasResult"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o SosaResult : "coso_hasResult"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o CosoContaminantMeasurement : "coso_hasResult"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o OwlThing : "coso_hasResult"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o QudtQuantifiable : "coso_hasResult"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o QudtQuantity : "coso_hasResult"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o QudtConcept : "coso_hasResult"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o StadDatapoint : "coso_hasResult"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o OwlNamedIndividual : "coso_observedProperty"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o OwlThing : "coso_observedProperty"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o QudtQuantityKind : "coso_observedProperty"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o CosoContaminantConcentrationQuantityKind : "coso_observedProperty"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o CosoContaminationProperty : "coso_observedProperty"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o StadQualityKind : "coso_observedProperty"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o SosaProperty : "coso_observedProperty"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o ProvAgent : "prov_wasAttributedTo"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o OwlNamedIndividual : "coso_ofDatasetSubstance"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o CosoSubstanceCollection : "coso_ofDatasetSubstance"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o HttpW3id.orgSawgraphV1Us-wqp#Characteristic : "coso_ofDatasetSubstance"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o Beb7217b5b32080b9606028314249e33b : "coso_ofDatasetSubstance"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o OwlThing : "coso_ofDatasetSubstance"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-ParameterName : "coso_ofDatasetSubstance"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o RdfsLiteral : "rdfs_label"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o GeoFeature : "coso_hasFeatureOfInterest"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o MeEgadEGAD-SampledFeature : "coso_hasFeatureOfInterest"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o OwlThing : "coso_hasFeatureOfInterest"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o CosoFeature : "coso_hasFeatureOfInterest"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampledFeature : "coso_hasFeatureOfInterest"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o SosaFeatureOfInterest : "coso_hasFeatureOfInterest"
HttpW3id.orgSawgraphV1Us-wqp#Observation ||--|o GeoSpatialObject : "coso_hasFeatureOfInterest"
HttpW3id.orgSawgraphV1Us-wqp#PrivateNon-IndustrialOrganization ||--|o RdfsLiteral : "rdfs_label"
HttpW3id.orgSawgraphV1Us-wqp#ResultMeasureQualifier ||--|o RdfsLiteral : "rdfs_comment"
HttpW3id.orgSawgraphV1Us-wqp#ResultMeasureQualifier ||--|o RdfsLiteral : "rdfs_label"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o HttpW3id.orgSawgraphV1Us-wqp#SampleCollectionMethod : "http___w3id.org_sawgraph_v1_us-wqp#sampleCollectionMethod"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o HttpW3id.orgSawgraphV1Us-wqp#Project : "http___w3id.org_sawgraph_v1_us-wqp#hasProjectId"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o RdfsLiteral : "rdfs_label"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboFOODON03411183 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboFOODON03411057 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboNCBITaxon283036 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboFOODON02010107 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o HttpW3id.orgSawgraphV1Us-wqp#SampleMedia : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboFOODON00003572 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o B37977f50d3140da51a9630b8a57396a1 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboFOODON03420147 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o B215b3a432e1c482d3680398a554edbbf : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o MeEgadEGAD-SampleMaterialTypeQualifier : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o B036a3008450d6ce37e35cf5a98355a60 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboNCBITaxon66912 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboNCBITaxon7971 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboFOODON03411566 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboFOODON03420194 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboNCBITaxon381124 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o Bf584e1bfd1c74de0eb37e7b926538b83 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboFOODON00001093 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o HttpW3id.orgSawgraphV1Us-wqp#Taxon : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboNCBITaxon8022 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o B44bec873efc8b96cad5f525429c64e0a : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboFOODON00002477 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OwlThing : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o B27231c83f17c76e178e0c9f5e10acc55 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboNCBITaxon6550 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboFOODON02021651 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o Ba6d85f816540f9fec5b71ba42fc2cca6 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o CosoWaterSample : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboNCBITaxon225389 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o B423a0e253807f20386fc3ccbbd7e0378 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o MeEgadEGAD-SampleMaterialType : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboNCBITaxon8182 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboFOODON02010012 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o Bbefc37cbdd03cae92dadef76b34dbf16 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboFOODON03420150 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o B085dcda89ed6aae0d3b229e767f0a1ca : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o Bb0125be5bc4dc7be7e8452e7d22445f6 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o B0d427a711311f1499a234aa8af2c66d1 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboFOODON03411236 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboNCBITaxon6604 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboFOODON03301761 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleMaterialType : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o B7728f65369357f97de36b133c9d1d5e0 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o Be047d68edc8eb3ce96d7edbad5217bfc : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboNCBITaxon8032 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboFOODON03420181 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboFOODON02010045 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboNCBITaxon154811 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboNCBITaxon27778 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o Be497d3b0c2656040c05e303873a2d541 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboFOODON00004460 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o Beb77c26f8c395403edc359fd5f6dfb28 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o B611b8dff312692e7f32a69834c787a60 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboFOODON03411324 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o B75e45ed04b2b903b9029968cada06faa : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboFOODON03420116 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboNCBITaxon225060 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o B75dbc5841338872cea35dced609fcd77 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o CosoSampleMaterialType : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboFOODON00003083 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboNCBITaxon147949 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboFOODON03411325 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboNCBITaxon7998 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboNCBITaxon8010 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o B3cc7b3721547b07a4068dc98b6444b8b : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboNCBITaxon8038 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboNCBITaxon184451 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboFOODON02010015 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o Bbf63deb85414ddecd89e46bce27e7f0a : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboFOODON00004172 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboFOODON03411457 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboNCBITaxon75288 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboFOODON03413378 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboFOODON02010042 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o B4fd286b2a5a12e342d61412628b6e4c2 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o Bf04685c17c0e71ae3c98e08c75cbdfcc : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o B623b56ef58fd82dd088819e22d655c08 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboFOODON00003425 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o B5e93e815b548435105d9273d424fa0e8 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboFOODON00002165 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboFOODON03411669 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o B53622dee107de372b2d0566f64ab6e3a : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboNCBITaxon8167 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboFOODON02020892 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboNCBITaxon27706 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o HttpW3id.orgSawgraphV1Us-wqp#TaxonGroup.FishNekton : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboFOODON00003042 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboFOODON02021803 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboNCBITaxon46259 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboNCBITaxon34816 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleMaterialTypeQualifier : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o Bb71af62f2f3e5e5b5e0fe81f24eca409 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboNCBITaxon66913 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboFOODON03411583 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboFOODON03411328 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboFOODON00004436 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboFOODON02021805 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboFOODON03413358 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboFOODON02010032 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboFOODON02020840 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboNCBITaxon126735 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OwlNamedIndividual : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OboNCBITaxon13106 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o B8aa8791a0418cd594c8b56ad21351f72 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o B00af777bec4da87c5aebb51d94b2d478 : "coso_sampleOfMaterialType"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o GeoFeature : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o HttpW3id.orgSawgraphV1Us-wqp#Site : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o OwlThing : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o MeEgadEGAD-SamplePoint : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o GeoSpatialObject : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o CosoSamplePoint : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o SosaFeatureOfInterest : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Us-wqp#Sample ||--|o CosoPoint : "coso_fromSamplePoint"
HttpW3id.orgSawgraphV1Us-wqp#Sample-SpecificQuantitationLimit ||--|o QudtUnit : "qudt_hasUnit"
HttpW3id.orgSawgraphV1Us-wqp#Sample-SpecificQuantitationLimit ||--|o QudtContextualUnit : "qudt_hasUnit"
HttpW3id.orgSawgraphV1Us-wqp#Sample-SpecificQuantitationLimit ||--|o QudtLogarithmicUnit : "qudt_hasUnit"
HttpW3id.orgSawgraphV1Us-wqp#Sample-SpecificQuantitationLimit ||--|o QudtCurrencyUnit : "qudt_hasUnit"
HttpW3id.orgSawgraphV1Us-wqp#Sample-SpecificQuantitationLimit ||--|o QudtDerivedUnit : "qudt_hasUnit"
HttpW3id.orgSawgraphV1Us-wqp#Sample-SpecificQuantitationLimit ||--|o QudtCountingUnit : "qudt_hasUnit"
HttpW3id.orgSawgraphV1Us-wqp#SampleMedia ||--|o RdfsLiteral : "rdfs_comment"
HttpW3id.orgSawgraphV1Us-wqp#SampleMedia ||--|o RdfsLiteral : "rdfs_label"
HttpW3id.orgSawgraphV1Us-wqp#SampledFeature ||--|o HttpW3id.orgSawgraphV1Us-wqp#DefWQPSurfaceWaterFeatureType : "http___w3id.org_sawgraph_v1_us-wqp#locationType"
HttpW3id.orgSawgraphV1Us-wqp#SampledFeature ||--|o HttpW3id.orgSawgraphV1Us-wqp#LocationType : "http___w3id.org_sawgraph_v1_us-wqp#locationType"
HttpW3id.orgSawgraphV1Us-wqp#SampledFeature ||--|o HttpW3id.orgSawgraphV1Us-wqp#DefWQPGroundWaterFeatureType : "http___w3id.org_sawgraph_v1_us-wqp#locationType"
HttpW3id.orgSawgraphV1Us-wqp#SampledFeature ||--|o RdfsLiteral : "rdfs_label"
HttpW3id.orgSawgraphV1Us-wqp#Single-PFAS-Concentration ||--|o CosoResultQualifier : "coso_hasResultQualifier"
HttpW3id.orgSawgraphV1Us-wqp#Single-PFAS-Concentration ||--|o HttpW3id.orgSawgraphV1Us-wqp#InstrumentDetectionLevel : "coso_hasResultQualifier"
HttpW3id.orgSawgraphV1Us-wqp#Single-PFAS-Concentration ||--|o HttpW3id.orgSawgraphV1Us-wqp#ResultMeasureQualifier : "coso_hasResultQualifier"
HttpW3id.orgSawgraphV1Us-wqp#Single-PFAS-Concentration ||--|o HttpW3id.orgSawgraphV1Us-wqp#Sample-SpecificQuantitationLimit : "coso_hasResultQualifier"
HttpW3id.orgSawgraphV1Us-wqp#Single-PFAS-Concentration ||--|o HttpW3id.orgSawgraphV1Us-wqp#LowerReportingLimit : "coso_hasResultQualifier"
HttpW3id.orgSawgraphV1Us-wqp#Single-PFAS-Concentration ||--|o OwlThing : "coso_hasResultQualifier"
HttpW3id.orgSawgraphV1Us-wqp#Single-PFAS-Concentration ||--|o HttpW3id.orgSawgraphV1Us-wqp#LaboratoryReportingLevel : "coso_hasResultQualifier"
HttpW3id.orgSawgraphV1Us-wqp#Single-PFAS-Concentration ||--|o HttpW3id.orgSawgraphV1Us-wqp#LowerQuantitationLimit : "coso_hasResultQualifier"
HttpW3id.orgSawgraphV1Us-wqp#Single-PFAS-Concentration ||--|o HttpW3id.orgSawgraphV1Us-wqp#MethodDetectionLevel : "coso_hasResultQualifier"
HttpW3id.orgSawgraphV1Us-wqp#Single-PFAS-Concentration ||--|o QudtQuantityValue : "qudt_quantityValue"
HttpW3id.orgSawgraphV1Us-wqp#Site ||--|o GeoGeometry : "geo_hasGeometry"
HttpW3id.orgSawgraphV1Us-wqp#Site ||--|o HttpW3id.orgSawgraphV1Us-wqp#SampledFeature : "coso_pointFromFeature"
HttpW3id.orgSawgraphV1Us-wqp#Site ||--|o GeoFeature : "coso_pointFromFeature"
HttpW3id.orgSawgraphV1Us-wqp#Site ||--|o MeEgadEGAD-SampledFeature : "coso_pointFromFeature"
HttpW3id.orgSawgraphV1Us-wqp#Site ||--|o OwlThing : "coso_pointFromFeature"
HttpW3id.orgSawgraphV1Us-wqp#Site ||--|o CosoFeature : "coso_pointFromFeature"
HttpW3id.orgSawgraphV1Us-wqp#Site ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampledFeature : "coso_pointFromFeature"
HttpW3id.orgSawgraphV1Us-wqp#Site ||--|o SosaFeatureOfInterest : "coso_pointFromFeature"
HttpW3id.orgSawgraphV1Us-wqp#Site ||--|o GeoSpatialObject : "coso_pointFromFeature"
HttpW3id.orgSawgraphV1Us-wqp#Site ||--|o ProvAgent : "prov_wasAttributedTo"
HttpW3id.orgSawgraphV1Us-wqp#Site ||--|o RdfsLiteral : "rdfs_label"
HttpW3id.orgSawgraphV1Us-wqp#StateGovernmentUSOrganization ||--|o RdfsLiteral : "rdfs_label"
HttpW3id.orgSawgraphV1Us-wqp#StateUSGovernmentOrganization ||--|o RdfsLiteral : "rdfs_label"
HttpW3id.orgSawgraphV1Us-wqp#Taxon ||--|o RdfsLiteral : "rdfs_label"
HttpW3id.orgSawgraphV1Us-wqp#TaxonGroup.FishNekton ||--|o RdfsLiteral : "rdfs_label"
KwgoS2CellLevel13 ||--|o KwgoS2CellLevel13 : "spatial_spatiallyRelatedTo"
KwgoS2CellLevel13 ||--|o KwgoAdministrativeRegion : "spatial_spatiallyRelatedTo"
KwgoS2CellLevel13 ||--|o OwlThing : "spatial_spatiallyRelatedTo"
KwgoS2CellLevel13 ||--|o MeEgadEGAD-SamplePoint : "spatial_spatiallyRelatedTo"
KwgoS2CellLevel13 ||--|o KwgoAdministrativeRegion3 : "spatial_spatiallyRelatedTo"
KwgoS2CellLevel13 ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint : "spatial_spatiallyRelatedTo"
KwgoS2CellLevel13 ||--|o MeEgadEGAD-PFAS-Site : "spatial_spatiallyRelatedTo"
KwgoS2CellLevel13 ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Site : "spatial_spatiallyRelatedTo"
KwgoS2CellLevel13 ||--|o GeoSpatialObject : "spatial_spatiallyRelatedTo"
KwgoS2CellLevel13 ||--|o KwgoRegion : "spatial_spatiallyRelatedTo"
KwgoS2CellLevel13 ||--|o OwlThing : "owl_sameAs"
KwgoS2CellLevel13 ||--|o KwgoS2CellLevel13 : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o KwgoAdministrativeRegion : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o OwlThing : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o MeEgadEGAD-SamplePoint : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o KwgoAdministrativeRegion3 : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o MeEgadEGAD-PFAS-Site : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Site : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o GeoSpatialObject : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o KwgoRegion : "spatial_connectedTo"
MeEgadEGAD-AggregatePFAS-Concentration ||--|o MeEgadEGAD-ConcentrationQualifier : "coso_resultAnnotation"
MeEgadEGAD-AggregatePFAS-Concentration ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-ValidationLevel : "coso_resultAnnotation"
MeEgadEGAD-AggregatePFAS-Concentration ||--|o OwlNamedIndividual : "coso_resultAnnotation"
MeEgadEGAD-AggregatePFAS-Concentration ||--|o MeEgadEGAD-MethodDetectionLimit : "coso_resultAnnotation"
MeEgadEGAD-AggregatePFAS-Concentration ||--|o MeEgadEGAD-ValidationLevel : "coso_resultAnnotation"
MeEgadEGAD-AggregatePFAS-Concentration ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-ReportingLimit : "coso_resultAnnotation"
MeEgadEGAD-AggregatePFAS-Concentration ||--|o OwlThing : "coso_resultAnnotation"
MeEgadEGAD-AggregatePFAS-Concentration ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-ConcentrationQualifier : "coso_resultAnnotation"
MeEgadEGAD-AggregatePFAS-Concentration ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-MethodDetectionLimit : "coso_resultAnnotation"
MeEgadEGAD-AggregatePFAS-Concentration ||--|o MeEgadEGAD-ReportingLimit : "coso_resultAnnotation"
MeEgadEGAD-AggregatePFAS-Concentration ||--|o QudtEnumeratedValue : "coso_measurementValue"
MeEgadEGAD-AggregatePFAS-Concentration ||--|o QudtConcept : "coso_measurementValue"
MeEgadEGAD-AggregatePFAS-Concentration ||--|o QudtVerifiable : "coso_measurementValue"
MeEgadEGAD-AggregatePFAS-Concentration ||--|o QudtQuantityKind : "qudt_hasQuantityKind"
MeEgadEGAD-AggregatePFAS-Concentration ||--|o MeEgadEGAD-ConcentrationQualifier : "me_egad_labQualifier"
MeEgadEGAD-AggregatePFAS-Concentration ||--|o OwlNamedIndividual : "me_egad_labQualifier"
MeEgadEGAD-AggregatePFAS-Concentration ||--|o OwlThing : "owl_sameAs"
MeEgadEGAD-AggregatePFAS-Concentration ||--|o QudtConcept : "coso_measurementUnit"
MeEgadEGAD-AggregatePFAS-Concentration ||--|o QudtUnit : "coso_measurementUnit"
MeEgadEGAD-AggregatePFAS-Concentration ||--|o CosoResultQualifier : "me_egad_methodDetectionLimit"
MeEgadEGAD-AggregatePFAS-Concentration ||--|o CosoDetectionLimit : "me_egad_methodDetectionLimit"
MeEgadEGAD-AggregatePFAS-Concentration ||--|o MeEgadEGAD-MethodDetectionLimit : "me_egad_methodDetectionLimit"
MeEgadEGAD-AggregatePFAS-Concentration ||--|o OwlThing : "me_egad_methodDetectionLimit"
MeEgadEGAD-AggregatePFAS-Concentration ||--|o QudtQuantifiable : "me_egad_methodDetectionLimit"
MeEgadEGAD-AggregatePFAS-Concentration ||--|o QudtQuantity : "me_egad_methodDetectionLimit"
MeEgadEGAD-AggregatePFAS-Concentration ||--|o QudtConcept : "me_egad_methodDetectionLimit"
MeEgadEGAD-AggregatePFAS-Concentration ||--|o StadDatapoint : "me_egad_methodDetectionLimit"
MeEgadEGAD-AggregatePFAS-Concentration ||--|o QudtQuantityValue : "qudt_quantityValue"
MeEgadEGAD-AggregatePFAS-Concentration ||--|o RdfsLiteral : "rdfs_label"
MeEgadEGAD-AggregatePFAS-Concentration ||--|o OwlThing : "me_egad_validationLevel"
MeEgadEGAD-AggregatePFAS-Concentration ||--|o OwlNamedIndividual : "me_egad_validationLevel"
MeEgadEGAD-AggregatePFAS-Concentration ||--|o MeEgadEGAD-ValidationLevel : "me_egad_validationLevel"
MeEgadEGAD-AggregatePFAS-Concentration ||--|o CosoQuantitationLimit : "me_egad_reportingLimit"
MeEgadEGAD-AggregatePFAS-Concentration ||--|o CosoResultQualifier : "me_egad_reportingLimit"
MeEgadEGAD-AggregatePFAS-Concentration ||--|o OwlThing : "me_egad_reportingLimit"
MeEgadEGAD-AggregatePFAS-Concentration ||--|o QudtQuantifiable : "me_egad_reportingLimit"
MeEgadEGAD-AggregatePFAS-Concentration ||--|o QudtQuantity : "me_egad_reportingLimit"
MeEgadEGAD-AggregatePFAS-Concentration ||--|o QudtConcept : "me_egad_reportingLimit"
MeEgadEGAD-AggregatePFAS-Concentration ||--|o MeEgadEGAD-ReportingLimit : "me_egad_reportingLimit"
MeEgadEGAD-AggregatePFAS-Concentration ||--|o StadDatapoint : "me_egad_reportingLimit"
MeEgadEGAD-AggregatePFAS-Concentration ||--|o MeEgadEGAD-ConcentrationQualifier : "me_egad_validationQualifier"
MeEgadEGAD-AggregatePFAS-Concentration ||--|o OwlThing : "me_egad_validationQualifier"
MeEgadEGAD-AggregatePFAS-Concentration ||--|o OwlNamedIndividual : "me_egad_validationQualifier"
MeEgadEGAD-AnalysisMethod ||--|o RdfsLiteral : "rdfs_label"
MeEgadEGAD-AnalysisMethod ||--|o OwlThing : "owl_sameAs"
MeEgadEGAD-ConcentrationQualifier ||--|o RdfsLiteral : "rdfs_label"
MeEgadEGAD-ConcentrationQualifier ||--|o OwlThing : "owl_sameAs"
MeEgadEGAD-MethodDetectionLimit ||--|o QudtUnit : "qudt_hasUnit"
MeEgadEGAD-MethodDetectionLimit ||--|o QudtContextualUnit : "qudt_hasUnit"
MeEgadEGAD-MethodDetectionLimit ||--|o QudtLogarithmicUnit : "qudt_hasUnit"
MeEgadEGAD-MethodDetectionLimit ||--|o QudtCurrencyUnit : "qudt_hasUnit"
MeEgadEGAD-MethodDetectionLimit ||--|o QudtDerivedUnit : "qudt_hasUnit"
MeEgadEGAD-MethodDetectionLimit ||--|o QudtCountingUnit : "qudt_hasUnit"
MeEgadEGAD-MethodDetectionLimit ||--|o OwlThing : "owl_sameAs"
MeEgadEGAD-PFAS-Observation ||--|o GeoFeature : "coso_observedAtSamplePoint"
MeEgadEGAD-PFAS-Observation ||--|o HttpW3id.orgSawgraphV1Us-wqp#Site : "coso_observedAtSamplePoint"
MeEgadEGAD-PFAS-Observation ||--|o OwlThing : "coso_observedAtSamplePoint"
MeEgadEGAD-PFAS-Observation ||--|o MeEgadEGAD-SamplePoint : "coso_observedAtSamplePoint"
MeEgadEGAD-PFAS-Observation ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint : "coso_observedAtSamplePoint"
MeEgadEGAD-PFAS-Observation ||--|o GeoSpatialObject : "coso_observedAtSamplePoint"
MeEgadEGAD-PFAS-Observation ||--|o CosoSamplePoint : "coso_observedAtSamplePoint"
MeEgadEGAD-PFAS-Observation ||--|o SosaFeatureOfInterest : "coso_observedAtSamplePoint"
MeEgadEGAD-PFAS-Observation ||--|o CosoPoint : "coso_observedAtSamplePoint"
MeEgadEGAD-PFAS-Observation ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample : "coso_analyzedSample"
MeEgadEGAD-PFAS-Observation ||--|o HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample : "coso_analyzedSample"
MeEgadEGAD-PFAS-Observation ||--|o SosaFeatureOfInterest : "coso_analyzedSample"
MeEgadEGAD-PFAS-Observation ||--|o CosoPlantMaterialSample : "coso_analyzedSample"
MeEgadEGAD-PFAS-Observation ||--|o HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample : "coso_analyzedSample"
MeEgadEGAD-PFAS-Observation ||--|o HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample : "coso_analyzedSample"
MeEgadEGAD-PFAS-Observation ||--|o MeEgadEGAD-Sample : "coso_analyzedSample"
MeEgadEGAD-PFAS-Observation ||--|o CosoAnimalTissueSample : "coso_analyzedSample"
MeEgadEGAD-PFAS-Observation ||--|o CosoAnimalOrganSample : "coso_analyzedSample"
MeEgadEGAD-PFAS-Observation ||--|o HttpW3id.orgSawgraphV1Us-wqp#Sample : "coso_analyzedSample"
MeEgadEGAD-PFAS-Observation ||--|o SosaSample : "coso_analyzedSample"
MeEgadEGAD-PFAS-Observation ||--|o CosoMaterialSample : "coso_analyzedSample"
MeEgadEGAD-PFAS-Observation ||--|o CosoAnimalMilkSample : "coso_analyzedSample"
MeEgadEGAD-PFAS-Observation ||--|o HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample : "coso_analyzedSample"
MeEgadEGAD-PFAS-Observation ||--|o CosoAnimalBloodSample : "coso_analyzedSample"
MeEgadEGAD-PFAS-Observation ||--|o OwlThing : "coso_analyzedSample"
MeEgadEGAD-PFAS-Observation ||--|o HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample : "coso_analyzedSample"
MeEgadEGAD-PFAS-Observation ||--|o CosoAnimalMaterialSample : "coso_analyzedSample"
MeEgadEGAD-PFAS-Observation ||--|o HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample : "coso_analyzedSample"
MeEgadEGAD-PFAS-Observation ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample : "coso_hasAnyFeatureOfInterest"
MeEgadEGAD-PFAS-Observation ||--|o HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample : "coso_hasAnyFeatureOfInterest"
MeEgadEGAD-PFAS-Observation ||--|o SosaFeatureOfInterest : "coso_hasAnyFeatureOfInterest"
MeEgadEGAD-PFAS-Observation ||--|o CosoPlantMaterialSample : "coso_hasAnyFeatureOfInterest"
MeEgadEGAD-PFAS-Observation ||--|o HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample : "coso_hasAnyFeatureOfInterest"
MeEgadEGAD-PFAS-Observation ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint : "coso_hasAnyFeatureOfInterest"
MeEgadEGAD-PFAS-Observation ||--|o HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample : "coso_hasAnyFeatureOfInterest"
MeEgadEGAD-PFAS-Observation ||--|o MeEgadEGAD-Sample : "coso_hasAnyFeatureOfInterest"
MeEgadEGAD-PFAS-Observation ||--|o CosoAnimalTissueSample : "coso_hasAnyFeatureOfInterest"
MeEgadEGAD-PFAS-Observation ||--|o CosoAnimalOrganSample : "coso_hasAnyFeatureOfInterest"
MeEgadEGAD-PFAS-Observation ||--|o MeEgadEGAD-SampledFeature : "coso_hasAnyFeatureOfInterest"
MeEgadEGAD-PFAS-Observation ||--|o MeEgadEGAD-SamplePoint : "coso_hasAnyFeatureOfInterest"
MeEgadEGAD-PFAS-Observation ||--|o HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample : "coso_hasAnyFeatureOfInterest"
MeEgadEGAD-PFAS-Observation ||--|o CosoAnimalMilkSample : "coso_hasAnyFeatureOfInterest"
MeEgadEGAD-PFAS-Observation ||--|o CosoAnimalBloodSample : "coso_hasAnyFeatureOfInterest"
MeEgadEGAD-PFAS-Observation ||--|o OwlThing : "coso_hasAnyFeatureOfInterest"
MeEgadEGAD-PFAS-Observation ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampledFeature : "coso_hasAnyFeatureOfInterest"
MeEgadEGAD-PFAS-Observation ||--|o HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample : "coso_hasAnyFeatureOfInterest"
MeEgadEGAD-PFAS-Observation ||--|o CosoAnimalMaterialSample : "coso_hasAnyFeatureOfInterest"
MeEgadEGAD-PFAS-Observation ||--|o HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample : "coso_hasAnyFeatureOfInterest"
MeEgadEGAD-PFAS-Observation ||--|o MeEgadEGAD-ResultType : "me_egad_resultType"
MeEgadEGAD-PFAS-Observation ||--|o OwlThing : "me_egad_resultType"
MeEgadEGAD-PFAS-Observation ||--|o OwlNamedIndividual : "me_egad_resultType"
MeEgadEGAD-PFAS-Observation ||--|o CosoObservationAnnotation : "me_egad_resultType"
MeEgadEGAD-PFAS-Observation ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SinglePFAS-Concentration : "coso_hasResult"
MeEgadEGAD-PFAS-Observation ||--|o MeEgadEGAD-SinglePFAS-Concentration : "coso_hasResult"
MeEgadEGAD-PFAS-Observation ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-AggregatePFAS-Concentration : "coso_hasResult"
MeEgadEGAD-PFAS-Observation ||--|o MeEgadEGAD-AggregatePFAS-Concentration : "coso_hasResult"
MeEgadEGAD-PFAS-Observation ||--|o HttpW3id.orgSawgraphV1Us-wqp#Single-PFAS-Concentration : "coso_hasResult"
MeEgadEGAD-PFAS-Observation ||--|o SosaResult : "coso_hasResult"
MeEgadEGAD-PFAS-Observation ||--|o CosoContaminantMeasurement : "coso_hasResult"
MeEgadEGAD-PFAS-Observation ||--|o OwlThing : "coso_hasResult"
MeEgadEGAD-PFAS-Observation ||--|o QudtQuantifiable : "coso_hasResult"
MeEgadEGAD-PFAS-Observation ||--|o QudtQuantity : "coso_hasResult"
MeEgadEGAD-PFAS-Observation ||--|o QudtConcept : "coso_hasResult"
MeEgadEGAD-PFAS-Observation ||--|o StadDatapoint : "coso_hasResult"
MeEgadEGAD-PFAS-Observation ||--|o MeEgadEGAD-AnalysisMethod : "coso_analysisMethod"
MeEgadEGAD-PFAS-Observation ||--|o OwlNamedIndividual : "coso_analysisMethod"
MeEgadEGAD-PFAS-Observation ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-AnalysisMethod : "coso_analysisMethod"
MeEgadEGAD-PFAS-Observation ||--|o OwlNamedIndividual : "coso_observationAnnotation"
MeEgadEGAD-PFAS-Observation ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-ResultType : "coso_observationAnnotation"
MeEgadEGAD-PFAS-Observation ||--|o OwlThing : "coso_observationAnnotation"
MeEgadEGAD-PFAS-Observation ||--|o CosoObservationAnnotation : "coso_observationAnnotation"
MeEgadEGAD-PFAS-Observation ||--|o MeEgadEGAD-ResultType : "coso_observationAnnotation"
MeEgadEGAD-PFAS-Observation ||--|o GeoFeature : "coso_observedAtPoint"
MeEgadEGAD-PFAS-Observation ||--|o OwlThing : "coso_observedAtPoint"
MeEgadEGAD-PFAS-Observation ||--|o MeEgadEGAD-SamplePoint : "coso_observedAtPoint"
MeEgadEGAD-PFAS-Observation ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint : "coso_observedAtPoint"
MeEgadEGAD-PFAS-Observation ||--|o GeoSpatialObject : "coso_observedAtPoint"
MeEgadEGAD-PFAS-Observation ||--|o SosaFeatureOfInterest : "coso_observedAtPoint"
MeEgadEGAD-PFAS-Observation ||--|o CosoPoint : "coso_observedAtPoint"
MeEgadEGAD-PFAS-Observation ||--|o OwlThing : "owl_sameAs"
MeEgadEGAD-PFAS-Observation ||--|o ProvAgent : "prov_wasAttributedTo"
MeEgadEGAD-PFAS-Observation ||--|o RdfsLiteral : "rdfs_label"
MeEgadEGAD-PFAS-Observation ||--|o GeoFeature : "coso_hasFeatureOfInterest"
MeEgadEGAD-PFAS-Observation ||--|o MeEgadEGAD-SampledFeature : "coso_hasFeatureOfInterest"
MeEgadEGAD-PFAS-Observation ||--|o OwlThing : "coso_hasFeatureOfInterest"
MeEgadEGAD-PFAS-Observation ||--|o CosoFeature : "coso_hasFeatureOfInterest"
MeEgadEGAD-PFAS-Observation ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampledFeature : "coso_hasFeatureOfInterest"
MeEgadEGAD-PFAS-Observation ||--|o SosaFeatureOfInterest : "coso_hasFeatureOfInterest"
MeEgadEGAD-PFAS-Observation ||--|o GeoSpatialObject : "coso_hasFeatureOfInterest"
MeEgadEGAD-PFAS-Observation ||--|o OwlNamedIndividual : "coso_ofSubstance"
MeEgadEGAD-PFAS-Observation ||--|o CosoSubstanceCollection : "coso_ofSubstance"
MeEgadEGAD-PFAS-Observation ||--|o Beb7217b5b32080b9606028314249e33b : "coso_ofSubstance"
MeEgadEGAD-PFAS-Observation ||--|o OwlThing : "coso_ofSubstance"
MeEgadEGAD-PFAS-Observation ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-ParameterName : "coso_ofSubstance"
MeEgadEGAD-PFAS-Observation ||--|o Ba76635ffb4afc02e78b9ef49973d089f : "coso_ofSubstance"
MeEgadEGAD-PFAS-ParameterName ||--|o RdfsLiteral : "rdfs_label"
MeEgadEGAD-PFAS-ParameterName ||--|o OwlThing : "owl_sameAs"
MeEgadEGAD-PFAS-Site ||--|o GeoGeometry : "geo_hasGeometry"
MeEgadEGAD-PFAS-Site ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SiteType : "http___w3id.org_sawgraph_v1_me-egad#siteType"
MeEgadEGAD-PFAS-Site ||--|o OwlNamedIndividual : "http___w3id.org_sawgraph_v1_me-egad#siteType"
MeEgadEGAD-PFAS-Site ||--|o MeEgadEGAD-SiteType : "me_egad_siteType"
MeEgadEGAD-PFAS-Site ||--|o OwlNamedIndividual : "me_egad_siteType"
MeEgadEGAD-PFAS-Site ||--|o RdfsLiteral : "dct_identifier"
MeEgadEGAD-PFAS-Site ||--|o KwgoS2CellLevel13 : "spatial_spatiallyRelatedTo"
MeEgadEGAD-PFAS-Site ||--|o KwgoAdministrativeRegion : "spatial_spatiallyRelatedTo"
MeEgadEGAD-PFAS-Site ||--|o OwlThing : "spatial_spatiallyRelatedTo"
MeEgadEGAD-PFAS-Site ||--|o MeEgadEGAD-SamplePoint : "spatial_spatiallyRelatedTo"
MeEgadEGAD-PFAS-Site ||--|o KwgoAdministrativeRegion3 : "spatial_spatiallyRelatedTo"
MeEgadEGAD-PFAS-Site ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint : "spatial_spatiallyRelatedTo"
MeEgadEGAD-PFAS-Site ||--|o MeEgadEGAD-PFAS-Site : "spatial_spatiallyRelatedTo"
MeEgadEGAD-PFAS-Site ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Site : "spatial_spatiallyRelatedTo"
MeEgadEGAD-PFAS-Site ||--|o GeoSpatialObject : "spatial_spatiallyRelatedTo"
MeEgadEGAD-PFAS-Site ||--|o KwgoRegion : "spatial_spatiallyRelatedTo"
MeEgadEGAD-PFAS-Site ||--|o OwlThing : "owl_sameAs"
MeEgadEGAD-PFAS-Site ||--|o GeoGeometry : "geo_hasDefaultGeometry"
MeEgadEGAD-PFAS-Site ||--|o RdfsLiteral : "rdfs_label"
MeEgadEGAD-PFAS-Site ||--|o KwgoS2CellLevel13 : "spatial_connectedTo"
MeEgadEGAD-PFAS-Site ||--|o KwgoAdministrativeRegion : "spatial_connectedTo"
MeEgadEGAD-PFAS-Site ||--|o OwlThing : "spatial_connectedTo"
MeEgadEGAD-PFAS-Site ||--|o MeEgadEGAD-SamplePoint : "spatial_connectedTo"
MeEgadEGAD-PFAS-Site ||--|o KwgoAdministrativeRegion3 : "spatial_connectedTo"
MeEgadEGAD-PFAS-Site ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint : "spatial_connectedTo"
MeEgadEGAD-PFAS-Site ||--|o MeEgadEGAD-PFAS-Site : "spatial_connectedTo"
MeEgadEGAD-PFAS-Site ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Site : "spatial_connectedTo"
MeEgadEGAD-PFAS-Site ||--|o GeoSpatialObject : "spatial_connectedTo"
MeEgadEGAD-PFAS-Site ||--|o KwgoRegion : "spatial_connectedTo"
MeEgadEGAD-ReportingLimit ||--|o QudtUnit : "qudt_hasUnit"
MeEgadEGAD-ReportingLimit ||--|o QudtContextualUnit : "qudt_hasUnit"
MeEgadEGAD-ReportingLimit ||--|o QudtLogarithmicUnit : "qudt_hasUnit"
MeEgadEGAD-ReportingLimit ||--|o QudtCurrencyUnit : "qudt_hasUnit"
MeEgadEGAD-ReportingLimit ||--|o QudtDerivedUnit : "qudt_hasUnit"
MeEgadEGAD-ReportingLimit ||--|o QudtCountingUnit : "qudt_hasUnit"
MeEgadEGAD-ReportingLimit ||--|o OwlThing : "owl_sameAs"
MeEgadEGAD-ResultType ||--|o RdfsLiteral : "rdfs_label"
MeEgadEGAD-ResultType ||--|o OwlThing : "owl_sameAs"
MeEgadEGAD-Sample ||--|o MeEgadEGAD-SampleCollectionMethod : "coso_sampleAnnotation"
MeEgadEGAD-Sample ||--|o OwlNamedIndividual : "coso_sampleAnnotation"
MeEgadEGAD-Sample ||--|o MeEgadEGAD-SampleDetailedLocation : "coso_sampleAnnotation"
MeEgadEGAD-Sample ||--|o CosoSampleAnnotation : "coso_sampleAnnotation"
MeEgadEGAD-Sample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleDetailedLocation : "coso_sampleAnnotation"
MeEgadEGAD-Sample ||--|o MeEgadEGAD-SampleTreatmentStatus : "coso_sampleAnnotation"
MeEgadEGAD-Sample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleTreatmentStatus : "coso_sampleAnnotation"
MeEgadEGAD-Sample ||--|o OwlThing : "coso_sampleAnnotation"
MeEgadEGAD-Sample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleCollectionMethod : "coso_sampleAnnotation"
MeEgadEGAD-Sample ||--|o RdfsLiteral : "dct_identifier"
MeEgadEGAD-Sample ||--|o OwlThing : "me_egad_sampleTreatmentStatus"
MeEgadEGAD-Sample ||--|o OwlNamedIndividual : "me_egad_sampleTreatmentStatus"
MeEgadEGAD-Sample ||--|o MeEgadEGAD-SampleTreatmentStatus : "me_egad_sampleTreatmentStatus"
MeEgadEGAD-Sample ||--|o CosoSampleAnnotation : "me_egad_sampleTreatmentStatus"
MeEgadEGAD-Sample ||--|o MeEgadEGAD-SampleCollectionMethod : "me_egad_sampleCollectionMethod"
MeEgadEGAD-Sample ||--|o OwlThing : "me_egad_sampleCollectionMethod"
MeEgadEGAD-Sample ||--|o OwlNamedIndividual : "me_egad_sampleCollectionMethod"
MeEgadEGAD-Sample ||--|o CosoSampleAnnotation : "me_egad_sampleCollectionMethod"
MeEgadEGAD-Sample ||--|o OwlThing : "owl_sameAs"
MeEgadEGAD-Sample ||--|o ProvAgent : "prov_wasAttributedTo"
MeEgadEGAD-Sample ||--|o RdfsLiteral : "rdfs_label"
MeEgadEGAD-Sample ||--|o OwlThing : "me_egad_sampleCollectionLocation"
MeEgadEGAD-Sample ||--|o OwlNamedIndividual : "me_egad_sampleCollectionLocation"
MeEgadEGAD-Sample ||--|o CosoSampleAnnotation : "me_egad_sampleCollectionLocation"
MeEgadEGAD-Sample ||--|o MeEgadEGAD-SampleDetailedLocation : "me_egad_sampleCollectionLocation"
MeEgadEGAD-Sample ||--|o OboFOODON03411183 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboFOODON03411057 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboNCBITaxon283036 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboFOODON02010107 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o HttpW3id.orgSawgraphV1Us-wqp#SampleMedia : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboFOODON00003572 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o B37977f50d3140da51a9630b8a57396a1 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboFOODON03420147 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o B215b3a432e1c482d3680398a554edbbf : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o MeEgadEGAD-SampleMaterialTypeQualifier : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o B036a3008450d6ce37e35cf5a98355a60 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboNCBITaxon66912 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboNCBITaxon7971 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboFOODON03411566 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboFOODON03420194 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboNCBITaxon381124 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o Bf584e1bfd1c74de0eb37e7b926538b83 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboFOODON00001093 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o HttpW3id.orgSawgraphV1Us-wqp#Taxon : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboNCBITaxon8022 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o B44bec873efc8b96cad5f525429c64e0a : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboFOODON00002477 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OwlThing : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o B27231c83f17c76e178e0c9f5e10acc55 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboNCBITaxon6550 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboFOODON02021651 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o Ba6d85f816540f9fec5b71ba42fc2cca6 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o CosoWaterSample : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboNCBITaxon225389 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o B423a0e253807f20386fc3ccbbd7e0378 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o MeEgadEGAD-SampleMaterialType : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboNCBITaxon8182 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboFOODON02010012 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o Bbefc37cbdd03cae92dadef76b34dbf16 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboFOODON03420150 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o B085dcda89ed6aae0d3b229e767f0a1ca : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o Bb0125be5bc4dc7be7e8452e7d22445f6 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o B0d427a711311f1499a234aa8af2c66d1 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboFOODON03411236 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboNCBITaxon6604 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboFOODON03301761 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleMaterialType : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o B7728f65369357f97de36b133c9d1d5e0 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o Be047d68edc8eb3ce96d7edbad5217bfc : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboNCBITaxon8032 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboFOODON03420181 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboFOODON02010045 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboNCBITaxon154811 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboNCBITaxon27778 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o Be497d3b0c2656040c05e303873a2d541 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboFOODON00004460 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o Beb77c26f8c395403edc359fd5f6dfb28 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o B611b8dff312692e7f32a69834c787a60 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboFOODON03411324 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o B75e45ed04b2b903b9029968cada06faa : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboFOODON03420116 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboNCBITaxon225060 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o B75dbc5841338872cea35dced609fcd77 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o CosoSampleMaterialType : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboFOODON00003083 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboNCBITaxon147949 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboFOODON03411325 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboNCBITaxon7998 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboNCBITaxon8010 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o B3cc7b3721547b07a4068dc98b6444b8b : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboNCBITaxon8038 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboNCBITaxon184451 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboFOODON02010015 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o Bbf63deb85414ddecd89e46bce27e7f0a : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboFOODON00004172 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboFOODON03411457 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboNCBITaxon75288 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboFOODON03413378 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboFOODON02010042 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o B4fd286b2a5a12e342d61412628b6e4c2 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o Bf04685c17c0e71ae3c98e08c75cbdfcc : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o B623b56ef58fd82dd088819e22d655c08 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboFOODON00003425 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o B5e93e815b548435105d9273d424fa0e8 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboFOODON00002165 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboFOODON03411669 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o B53622dee107de372b2d0566f64ab6e3a : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboNCBITaxon8167 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboFOODON02020892 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboNCBITaxon27706 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o HttpW3id.orgSawgraphV1Us-wqp#TaxonGroup.FishNekton : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboFOODON00003042 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboFOODON02021803 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboNCBITaxon46259 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboNCBITaxon34816 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleMaterialTypeQualifier : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o Bb71af62f2f3e5e5b5e0fe81f24eca409 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboNCBITaxon66913 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboFOODON03411583 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboFOODON03411328 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboFOODON00004436 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboFOODON02021805 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboFOODON03413358 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboFOODON02010032 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboFOODON02020840 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboNCBITaxon126735 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OwlNamedIndividual : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o OboNCBITaxon13106 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o B8aa8791a0418cd594c8b56ad21351f72 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o B00af777bec4da87c5aebb51d94b2d478 : "coso_sampleOfMaterialType"
MeEgadEGAD-Sample ||--|o GeoFeature : "coso_fromSamplePoint"
MeEgadEGAD-Sample ||--|o HttpW3id.orgSawgraphV1Us-wqp#Site : "coso_fromSamplePoint"
MeEgadEGAD-Sample ||--|o OwlThing : "coso_fromSamplePoint"
MeEgadEGAD-Sample ||--|o MeEgadEGAD-SamplePoint : "coso_fromSamplePoint"
MeEgadEGAD-Sample ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint : "coso_fromSamplePoint"
MeEgadEGAD-Sample ||--|o GeoSpatialObject : "coso_fromSamplePoint"
MeEgadEGAD-Sample ||--|o CosoSamplePoint : "coso_fromSamplePoint"
MeEgadEGAD-Sample ||--|o SosaFeatureOfInterest : "coso_fromSamplePoint"
MeEgadEGAD-Sample ||--|o CosoPoint : "coso_fromSamplePoint"
MeEgadEGAD-SampleCollectionMethod ||--|o RdfsLiteral : "rdfs_label"
MeEgadEGAD-SampleCollectionMethod ||--|o OwlThing : "owl_sameAs"
MeEgadEGAD-SampleDetailedLocation ||--|o RdfsLiteral : "rdfs_label"
MeEgadEGAD-SampleDetailedLocation ||--|o OwlThing : "owl_sameAs"
MeEgadEGAD-SampleMaterialType ||--|o RdfsLiteral : "rdfs_label"
MeEgadEGAD-SampleMaterialType ||--|o OwlThing : "owl_sameAs"
MeEgadEGAD-SampleMaterialTypeQualifier ||--|o RdfsLiteral : "rdfs_label"
MeEgadEGAD-SampleMaterialTypeQualifier ||--|o OwlThing : "owl_sameAs"
MeEgadEGAD-SamplePoint ||--|o GeoGeometry : "geo_hasGeometry"
MeEgadEGAD-SamplePoint ||--|o HttpW3id.orgSawgraphV1Us-wqp#SampledFeature : "coso_pointFromFeature"
MeEgadEGAD-SamplePoint ||--|o GeoFeature : "coso_pointFromFeature"
MeEgadEGAD-SamplePoint ||--|o MeEgadEGAD-SampledFeature : "coso_pointFromFeature"
MeEgadEGAD-SamplePoint ||--|o OwlThing : "coso_pointFromFeature"
MeEgadEGAD-SamplePoint ||--|o CosoFeature : "coso_pointFromFeature"
MeEgadEGAD-SamplePoint ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SampledFeature : "coso_pointFromFeature"
MeEgadEGAD-SamplePoint ||--|o SosaFeatureOfInterest : "coso_pointFromFeature"
MeEgadEGAD-SamplePoint ||--|o GeoSpatialObject : "coso_pointFromFeature"
MeEgadEGAD-SamplePoint ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Site : "me_egad_associatedSite"
MeEgadEGAD-SamplePoint ||--|o MeEgadEGAD-PFAS-Site : "me_egad_associatedSite"
MeEgadEGAD-SamplePoint ||--|o RdfsLiteral : "dct_identifier"
MeEgadEGAD-SamplePoint ||--|o KwgoS2CellLevel13 : "spatial_spatiallyRelatedTo"
MeEgadEGAD-SamplePoint ||--|o KwgoAdministrativeRegion : "spatial_spatiallyRelatedTo"
MeEgadEGAD-SamplePoint ||--|o OwlThing : "spatial_spatiallyRelatedTo"
MeEgadEGAD-SamplePoint ||--|o MeEgadEGAD-SamplePoint : "spatial_spatiallyRelatedTo"
MeEgadEGAD-SamplePoint ||--|o KwgoAdministrativeRegion3 : "spatial_spatiallyRelatedTo"
MeEgadEGAD-SamplePoint ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint : "spatial_spatiallyRelatedTo"
MeEgadEGAD-SamplePoint ||--|o MeEgadEGAD-PFAS-Site : "spatial_spatiallyRelatedTo"
MeEgadEGAD-SamplePoint ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Site : "spatial_spatiallyRelatedTo"
MeEgadEGAD-SamplePoint ||--|o GeoSpatialObject : "spatial_spatiallyRelatedTo"
MeEgadEGAD-SamplePoint ||--|o KwgoRegion : "spatial_spatiallyRelatedTo"
MeEgadEGAD-SamplePoint ||--|o OwlThing : "owl_sameAs"
MeEgadEGAD-SamplePoint ||--|o GeoGeometry : "geo_hasDefaultGeometry"
MeEgadEGAD-SamplePoint ||--|o RdfsLiteral : "rdfs_label"
MeEgadEGAD-SamplePoint ||--|o MeEgadEGAD-SamplePointType : "me_egad_samplePointType"
MeEgadEGAD-SamplePoint ||--|o OwlThing : "me_egad_samplePointType"
MeEgadEGAD-SamplePoint ||--|o OwlNamedIndividual : "me_egad_samplePointType"
MeEgadEGAD-SamplePoint ||--|o KwgoS2CellLevel13 : "spatial_connectedTo"
MeEgadEGAD-SamplePoint ||--|o KwgoAdministrativeRegion : "spatial_connectedTo"
MeEgadEGAD-SamplePoint ||--|o OwlThing : "spatial_connectedTo"
MeEgadEGAD-SamplePoint ||--|o MeEgadEGAD-SamplePoint : "spatial_connectedTo"
MeEgadEGAD-SamplePoint ||--|o KwgoAdministrativeRegion3 : "spatial_connectedTo"
MeEgadEGAD-SamplePoint ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint : "spatial_connectedTo"
MeEgadEGAD-SamplePoint ||--|o MeEgadEGAD-PFAS-Site : "spatial_connectedTo"
MeEgadEGAD-SamplePoint ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Site : "spatial_connectedTo"
MeEgadEGAD-SamplePoint ||--|o GeoSpatialObject : "spatial_connectedTo"
MeEgadEGAD-SamplePoint ||--|o KwgoRegion : "spatial_connectedTo"
MeEgadEGAD-SamplePointType ||--|o RdfsLiteral : "rdfs_label"
MeEgadEGAD-SamplePointType ||--|o OwlThing : "owl_sameAs"
MeEgadEGAD-SampleTreatmentStatus ||--|o RdfsLiteral : "rdfs_label"
MeEgadEGAD-SampleTreatmentStatus ||--|o OwlThing : "owl_sameAs"
MeEgadEGAD-SampledFeature ||--|o RdfsLiteral : "rdfs_label"
MeEgadEGAD-SampledFeature ||--|o MeEgadEGAD-SamplePointType : "me_egad_sampledFeatureType"
MeEgadEGAD-SampledFeature ||--|o OwlNamedIndividual : "me_egad_sampledFeatureType"
MeEgadEGAD-SampledFeature ||--|o OwlThing : "owl_sameAs"
MeEgadEGAD-SinglePFAS-Concentration ||--|o MeEgadEGAD-ConcentrationQualifier : "coso_resultAnnotation"
MeEgadEGAD-SinglePFAS-Concentration ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-ValidationLevel : "coso_resultAnnotation"
MeEgadEGAD-SinglePFAS-Concentration ||--|o OwlNamedIndividual : "coso_resultAnnotation"
MeEgadEGAD-SinglePFAS-Concentration ||--|o MeEgadEGAD-MethodDetectionLimit : "coso_resultAnnotation"
MeEgadEGAD-SinglePFAS-Concentration ||--|o MeEgadEGAD-ValidationLevel : "coso_resultAnnotation"
MeEgadEGAD-SinglePFAS-Concentration ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-ReportingLimit : "coso_resultAnnotation"
MeEgadEGAD-SinglePFAS-Concentration ||--|o OwlThing : "coso_resultAnnotation"
MeEgadEGAD-SinglePFAS-Concentration ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-ConcentrationQualifier : "coso_resultAnnotation"
MeEgadEGAD-SinglePFAS-Concentration ||--|o HttpW3id.orgSawgraphV1Me-egad#EGAD-MethodDetectionLimit : "coso_resultAnnotation"
MeEgadEGAD-SinglePFAS-Concentration ||--|o MeEgadEGAD-ReportingLimit : "coso_resultAnnotation"
MeEgadEGAD-SinglePFAS-Concentration ||--|o QudtEnumeratedValue : "coso_measurementValue"
MeEgadEGAD-SinglePFAS-Concentration ||--|o QudtConcept : "coso_measurementValue"
MeEgadEGAD-SinglePFAS-Concentration ||--|o QudtVerifiable : "coso_measurementValue"
MeEgadEGAD-SinglePFAS-Concentration ||--|o QudtQuantityKind : "qudt_hasQuantityKind"
MeEgadEGAD-SinglePFAS-Concentration ||--|o MeEgadEGAD-ConcentrationQualifier : "me_egad_labQualifier"
MeEgadEGAD-SinglePFAS-Concentration ||--|o OwlNamedIndividual : "me_egad_labQualifier"
MeEgadEGAD-SinglePFAS-Concentration ||--|o OwlThing : "owl_sameAs"
MeEgadEGAD-SinglePFAS-Concentration ||--|o QudtConcept : "coso_measurementUnit"
MeEgadEGAD-SinglePFAS-Concentration ||--|o QudtUnit : "coso_measurementUnit"
MeEgadEGAD-SinglePFAS-Concentration ||--|o CosoResultQualifier : "me_egad_methodDetectionLimit"
MeEgadEGAD-SinglePFAS-Concentration ||--|o CosoDetectionLimit : "me_egad_methodDetectionLimit"
MeEgadEGAD-SinglePFAS-Concentration ||--|o MeEgadEGAD-MethodDetectionLimit : "me_egad_methodDetectionLimit"
MeEgadEGAD-SinglePFAS-Concentration ||--|o OwlThing : "me_egad_methodDetectionLimit"
MeEgadEGAD-SinglePFAS-Concentration ||--|o QudtQuantifiable : "me_egad_methodDetectionLimit"
MeEgadEGAD-SinglePFAS-Concentration ||--|o QudtQuantity : "me_egad_methodDetectionLimit"
MeEgadEGAD-SinglePFAS-Concentration ||--|o QudtConcept : "me_egad_methodDetectionLimit"
MeEgadEGAD-SinglePFAS-Concentration ||--|o StadDatapoint : "me_egad_methodDetectionLimit"
MeEgadEGAD-SinglePFAS-Concentration ||--|o QudtQuantityValue : "qudt_quantityValue"
MeEgadEGAD-SinglePFAS-Concentration ||--|o RdfsLiteral : "rdfs_label"
MeEgadEGAD-SinglePFAS-Concentration ||--|o OwlThing : "me_egad_validationLevel"
MeEgadEGAD-SinglePFAS-Concentration ||--|o OwlNamedIndividual : "me_egad_validationLevel"
MeEgadEGAD-SinglePFAS-Concentration ||--|o MeEgadEGAD-ValidationLevel : "me_egad_validationLevel"
MeEgadEGAD-SinglePFAS-Concentration ||--|o CosoQuantitationLimit : "me_egad_reportingLimit"
MeEgadEGAD-SinglePFAS-Concentration ||--|o CosoResultQualifier : "me_egad_reportingLimit"
MeEgadEGAD-SinglePFAS-Concentration ||--|o OwlThing : "me_egad_reportingLimit"
MeEgadEGAD-SinglePFAS-Concentration ||--|o QudtQuantifiable : "me_egad_reportingLimit"
MeEgadEGAD-SinglePFAS-Concentration ||--|o QudtQuantity : "me_egad_reportingLimit"
MeEgadEGAD-SinglePFAS-Concentration ||--|o QudtConcept : "me_egad_reportingLimit"
MeEgadEGAD-SinglePFAS-Concentration ||--|o MeEgadEGAD-ReportingLimit : "me_egad_reportingLimit"
MeEgadEGAD-SinglePFAS-Concentration ||--|o StadDatapoint : "me_egad_reportingLimit"
MeEgadEGAD-SinglePFAS-Concentration ||--|o MeEgadEGAD-ConcentrationQualifier : "me_egad_validationQualifier"
MeEgadEGAD-SinglePFAS-Concentration ||--|o OwlThing : "me_egad_validationQualifier"
MeEgadEGAD-SinglePFAS-Concentration ||--|o OwlNamedIndividual : "me_egad_validationQualifier"
MeEgadEGAD-SiteType ||--|o RdfsLiteral : "rdfs_label"
MeEgadEGAD-SiteType ||--|o OwlThing : "owl_sameAs"
MeEgadEGAD-ValidationLevel ||--|o RdfsLiteral : "rdfs_label"
MeEgadEGAD-ValidationLevel ||--|o OwlThing : "owl_sameAs"
OboFOODON00001093 ||--|o RdfsLiteral : "rdfs_label"
OboFOODON00001093 ||--|o OwlThing : "owl_sameAs"
OboFOODON00002165 ||--|o RdfsLiteral : "rdfs_label"
OboFOODON00002165 ||--|o OwlThing : "owl_sameAs"
OboFOODON00002477 ||--|o RdfsLiteral : "rdfs_label"
OboFOODON00002477 ||--|o OwlThing : "owl_sameAs"
OboFOODON00003042 ||--|o RdfsLiteral : "rdfs_label"
OboFOODON00003042 ||--|o OwlThing : "owl_sameAs"
OboFOODON00003083 ||--|o RdfsLiteral : "rdfs_label"
OboFOODON00003083 ||--|o OwlThing : "owl_sameAs"
OboFOODON00003425 ||--|o RdfsLiteral : "rdfs_label"
OboFOODON00003425 ||--|o OwlThing : "owl_sameAs"
OboFOODON00003572 ||--|o RdfsLiteral : "rdfs_label"
OboFOODON00003572 ||--|o OwlThing : "owl_sameAs"
OboFOODON00004172 ||--|o RdfsLiteral : "rdfs_label"
OboFOODON00004172 ||--|o OwlThing : "owl_sameAs"
OboFOODON00004436 ||--|o RdfsLiteral : "rdfs_label"
OboFOODON00004436 ||--|o OwlThing : "owl_sameAs"
OboFOODON00004460 ||--|o RdfsLiteral : "rdfs_label"
OboFOODON00004460 ||--|o OwlThing : "obo_RO_0002162"
OboFOODON00004460 ||--|o OwlClass : "obo_RO_0002162"
OboFOODON00004460 ||--|o OwlThing : "owl_sameAs"
OboFOODON02010012 ||--|o RdfsLiteral : "rdfs_label"
OboFOODON02010012 ||--|o OwlThing : "owl_sameAs"
OboFOODON02010015 ||--|o RdfsLiteral : "rdfs_label"
OboFOODON02010015 ||--|o OwlThing : "owl_sameAs"
OboFOODON02010032 ||--|o RdfsLiteral : "rdfs_comment"
OboFOODON02010032 ||--|o RdfsLiteral : "rdfs_label"
OboFOODON02010032 ||--|o OwlThing : "owl_sameAs"
OboFOODON02010042 ||--|o RdfsLiteral : "rdfs_label"
OboFOODON02010042 ||--|o OwlThing : "owl_sameAs"
OboFOODON02010045 ||--|o RdfsLiteral : "rdfs_label"
OboFOODON02010045 ||--|o OwlThing : "owl_sameAs"
OboFOODON02010107 ||--|o RdfsLiteral : "rdfs_label"
OboFOODON02010107 ||--|o OwlThing : "owl_sameAs"
OboFOODON02020840 ||--|o RdfsLiteral : "rdfs_label"
OboFOODON02020840 ||--|o OwlThing : "owl_sameAs"
OboFOODON02020892 ||--|o RdfsLiteral : "rdfs_label"
OboFOODON02020892 ||--|o OwlThing : "owl_sameAs"
OboFOODON02021651 ||--|o RdfsLiteral : "rdfs_label"
OboFOODON02021651 ||--|o OwlThing : "owl_sameAs"
OboFOODON02021803 ||--|o RdfsLiteral : "rdfs_label"
OboFOODON02021803 ||--|o OwlThing : "owl_sameAs"
OboFOODON02021805 ||--|o RdfsLiteral : "rdfs_label"
OboFOODON02021805 ||--|o OwlThing : "owl_sameAs"
OboFOODON03301761 ||--|o RdfsLiteral : "rdfs_label"
OboFOODON03301761 ||--|o OwlThing : "owl_sameAs"
OboFOODON03411057 ||--|o RdfsLiteral : "rdfs_label"
OboFOODON03411057 ||--|o OwlThing : "owl_sameAs"
OboFOODON03411183 ||--|o RdfsLiteral : "rdfs_label"
OboFOODON03411183 ||--|o OwlThing : "owl_sameAs"
OboFOODON03411236 ||--|o RdfsLiteral : "rdfs_label"
OboFOODON03411236 ||--|o OwlThing : "owl_sameAs"
OboFOODON03411324 ||--|o RdfsLiteral : "rdfs_label"
OboFOODON03411324 ||--|o OwlThing : "owl_sameAs"
OboFOODON03411325 ||--|o RdfsLiteral : "rdfs_label"
OboFOODON03411325 ||--|o OwlThing : "owl_sameAs"
OboFOODON03411328 ||--|o RdfsLiteral : "rdfs_label"
OboFOODON03411328 ||--|o OwlThing : "owl_sameAs"
OboFOODON03411457 ||--|o RdfsLiteral : "rdfs_label"
OboFOODON03411457 ||--|o OwlThing : "owl_sameAs"
OboFOODON03411566 ||--|o RdfsLiteral : "rdfs_label"
OboFOODON03411566 ||--|o OwlThing : "owl_sameAs"
OboFOODON03411583 ||--|o RdfsLiteral : "rdfs_label"
OboFOODON03411583 ||--|o OwlThing : "owl_sameAs"
OboFOODON03411669 ||--|o RdfsLiteral : "rdfs_label"
OboFOODON03411669 ||--|o OwlThing : "owl_sameAs"
OboFOODON03413358 ||--|o RdfsLiteral : "rdfs_label"
OboFOODON03413358 ||--|o OwlThing : "owl_sameAs"
OboFOODON03413378 ||--|o RdfsLiteral : "rdfs_label"
OboFOODON03413378 ||--|o OwlThing : "owl_sameAs"
OboFOODON03420116 ||--|o RdfsLiteral : "rdfs_label"
OboFOODON03420116 ||--|o OwlThing : "owl_sameAs"
OboFOODON03420147 ||--|o RdfsLiteral : "rdfs_label"
OboFOODON03420147 ||--|o OwlThing : "owl_sameAs"
OboFOODON03420150 ||--|o RdfsLiteral : "rdfs_label"
OboFOODON03420150 ||--|o OwlThing : "owl_sameAs"
OboFOODON03420181 ||--|o RdfsLiteral : "rdfs_label"
OboFOODON03420181 ||--|o OwlThing : "obo_RO_0002162"
OboFOODON03420181 ||--|o OwlClass : "obo_RO_0002162"
OboFOODON03420181 ||--|o OwlThing : "owl_sameAs"
OboFOODON03420194 ||--|o RdfsLiteral : "rdfs_label"
OboFOODON03420194 ||--|o OwlThing : "owl_sameAs"
OboNCBITaxon126735 ||--|o RdfsLiteral : "rdfs_label"
OboNCBITaxon13106 ||--|o RdfsLiteral : "rdfs_label"
OboNCBITaxon147949 ||--|o RdfsLiteral : "rdfs_label"
OboNCBITaxon147949 ||--|o OwlThing : "owl_sameAs"
OboNCBITaxon154811 ||--|o RdfsLiteral : "rdfs_label"
OboNCBITaxon184451 ||--|o RdfsLiteral : "rdfs_label"
OboNCBITaxon225060 ||--|o RdfsLiteral : "rdfs_label"
OboNCBITaxon225389 ||--|o RdfsLiteral : "rdfs_label"
OboNCBITaxon27706 ||--|o RdfsLiteral : "rdfs_label"
OboNCBITaxon27706 ||--|o OwlThing : "owl_sameAs"
OboNCBITaxon27778 ||--|o RdfsLiteral : "rdfs_label"
OboNCBITaxon283036 ||--|o RdfsLiteral : "rdfs_label"
OboNCBITaxon34816 ||--|o RdfsLiteral : "rdfs_label"
OboNCBITaxon381124 ||--|o RdfsLiteral : "rdfs_label"
OboNCBITaxon381124 ||--|o OwlThing : "owl_sameAs"
OboNCBITaxon46259 ||--|o RdfsLiteral : "rdfs_label"
OboNCBITaxon6550 ||--|o RdfsLiteral : "rdfs_label"
OboNCBITaxon6604 ||--|o RdfsLiteral : "rdfs_label"
OboNCBITaxon66912 ||--|o RdfsLiteral : "rdfs_label"
OboNCBITaxon66913 ||--|o RdfsLiteral : "rdfs_label"
OboNCBITaxon75288 ||--|o RdfsLiteral : "rdfs_label"
OboNCBITaxon7971 ||--|o RdfsLiteral : "rdfs_label"
OboNCBITaxon7998 ||--|o RdfsLiteral : "rdfs_label"
OboNCBITaxon8010 ||--|o RdfsLiteral : "rdfs_label"
OboNCBITaxon8010 ||--|o OwlThing : "owl_sameAs"
OboNCBITaxon8022 ||--|o RdfsLiteral : "rdfs_label"
OboNCBITaxon8032 ||--|o RdfsLiteral : "rdfs_label"
OboNCBITaxon8038 ||--|o RdfsLiteral : "rdfs_label"
OboNCBITaxon8038 ||--|o OwlThing : "owl_sameAs"
OboNCBITaxon8167 ||--|o RdfsLiteral : "rdfs_label"
OboNCBITaxon8182 ||--|o RdfsLiteral : "rdfs_label"
OboNCBITaxon8182 ||--|o OwlThing : "owl_sameAs"
StadQualityKind ||--|o OwlThing : "owl_sameAs"
StadStatisticalQuantityKind ||--|o OwlThing : "owl_sameAs"

```



## Imports


* okns:extended_types
* linkml:types
* okns:dc
* okns:sdo
* okns:owl-rdf-rdfs
* okns:qudt
* okns:skos
* okns:sf
* okns:geo
* okns:prov
* okns:kwg



## Classes

| Class | Description | Occurrences |
| --- | --- | --- |
| [B00af777bec4da87c5aebb51d94b2d478](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/B00af777bec4da87c5aebb51d94b2d478.md) | None<br/>| 1 | 
| [B036a3008450d6ce37e35cf5a98355a60](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/B036a3008450d6ce37e35cf5a98355a60.md) | None<br/>| 1 | 
| [B085dcda89ed6aae0d3b229e767f0a1ca](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/B085dcda89ed6aae0d3b229e767f0a1ca.md) | None<br/>| 1 | 
| [B0d427a711311f1499a234aa8af2c66d1](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/B0d427a711311f1499a234aa8af2c66d1.md) | None<br/>| 1 | 
| [B215b3a432e1c482d3680398a554edbbf](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/B215b3a432e1c482d3680398a554edbbf.md) | None<br/>| 1 | 
| [B27231c83f17c76e178e0c9f5e10acc55](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/B27231c83f17c76e178e0c9f5e10acc55.md) | None<br/>| 1 | 
| [B37977f50d3140da51a9630b8a57396a1](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/B37977f50d3140da51a9630b8a57396a1.md) | None<br/>| 1 | 
| [B3cc7b3721547b07a4068dc98b6444b8b](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/B3cc7b3721547b07a4068dc98b6444b8b.md) | None<br/>| 2 | 
| [B423a0e253807f20386fc3ccbbd7e0378](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/B423a0e253807f20386fc3ccbbd7e0378.md) | None<br/>| 1 | 
| [B44bec873efc8b96cad5f525429c64e0a](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/B44bec873efc8b96cad5f525429c64e0a.md) | None<br/>| 1 | 
| [B4fd286b2a5a12e342d61412628b6e4c2](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/B4fd286b2a5a12e342d61412628b6e4c2.md) | None<br/>| 1 | 
| [B53622dee107de372b2d0566f64ab6e3a](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/B53622dee107de372b2d0566f64ab6e3a.md) | None<br/>| 6 | 
| [B5e93e815b548435105d9273d424fa0e8](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/B5e93e815b548435105d9273d424fa0e8.md) | None<br/>| 1 | 
| [B611b8dff312692e7f32a69834c787a60](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/B611b8dff312692e7f32a69834c787a60.md) | None<br/>| 6 | 
| [B623b56ef58fd82dd088819e22d655c08](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/B623b56ef58fd82dd088819e22d655c08.md) | None<br/>| 1 | 
| [B75dbc5841338872cea35dced609fcd77](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/B75dbc5841338872cea35dced609fcd77.md) | None<br/>| 1 | 
| [B75e45ed04b2b903b9029968cada06faa](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/B75e45ed04b2b903b9029968cada06faa.md) | None<br/>| 1 | 
| [B7728f65369357f97de36b133c9d1d5e0](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/B7728f65369357f97de36b133c9d1d5e0.md) | None<br/>| 1 | 
| [B8aa8791a0418cd594c8b56ad21351f72](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/B8aa8791a0418cd594c8b56ad21351f72.md) | None<br/>| 3 | 
| [Ba6d85f816540f9fec5b71ba42fc2cca6](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/Ba6d85f816540f9fec5b71ba42fc2cca6.md) | None<br/>| 9 | 
| [Ba76635ffb4afc02e78b9ef49973d089f](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/Ba76635ffb4afc02e78b9ef49973d089f.md) | None<br/>| 195 | 
| [Bb0125be5bc4dc7be7e8452e7d22445f6](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/Bb0125be5bc4dc7be7e8452e7d22445f6.md) | None<br/>| 1 | 
| [Bb71af62f2f3e5e5b5e0fe81f24eca409](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/Bb71af62f2f3e5e5b5e0fe81f24eca409.md) | None<br/>| 1 | 
| [Bbefc37cbdd03cae92dadef76b34dbf16](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/Bbefc37cbdd03cae92dadef76b34dbf16.md) | None<br/>| 1 | 
| [Bbf63deb85414ddecd89e46bce27e7f0a](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/Bbf63deb85414ddecd89e46bce27e7f0a.md) | None<br/>| 1 | 
| [Be047d68edc8eb3ce96d7edbad5217bfc](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/Be047d68edc8eb3ce96d7edbad5217bfc.md) | None<br/>| 1 | 
| [Be497d3b0c2656040c05e303873a2d541](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/Be497d3b0c2656040c05e303873a2d541.md) | None<br/>| 1 | 
| [Beb7217b5b32080b9606028314249e33b](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/Beb7217b5b32080b9606028314249e33b.md) | None<br/>| 145 | 
| [Beb77c26f8c395403edc359fd5f6dfb28](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/Beb77c26f8c395403edc359fd5f6dfb28.md) | None<br/>| 1 | 
| [Bf04685c17c0e71ae3c98e08c75cbdfcc](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/Bf04685c17c0e71ae3c98e08c75cbdfcc.md) | None<br/>| 2 | 
| [Bf584e1bfd1c74de0eb37e7b926538b83](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/Bf584e1bfd1c74de0eb37e7b926538b83.md) | None<br/>| 4 | 
| [HttpW3id.orgSawgraphV1Us-wqp#FederalUSGovernmentOrganization](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgSawgraphV1Us-wqp#FederalUSGovernmentOrganization.md) | None<br/>| 3 | 
| [HttpW3id.orgSawgraphV1Us-wqp#InstrumentDetectionLevel](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgSawgraphV1Us-wqp#InstrumentDetectionLevel.md) | None<br/>| 620 | 
| [HttpW3id.orgSawgraphV1Us-wqp#LaboratoryReportingLevel](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgSawgraphV1Us-wqp#LaboratoryReportingLevel.md) | None<br/>| 29824 | 
| [HttpW3id.orgSawgraphV1Us-wqp#LowerQuantitationLimit](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgSawgraphV1Us-wqp#LowerQuantitationLimit.md) | None<br/>| 1928 | 
| [HttpW3id.orgSawgraphV1Us-wqp#LowerReportingLimit](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgSawgraphV1Us-wqp#LowerReportingLimit.md) | None<br/>| 32677 | 
| [HttpW3id.orgSawgraphV1Us-wqp#MethodDetectionLevel](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgSawgraphV1Us-wqp#MethodDetectionLevel.md) | None<br/>| 52116 | 
| [HttpW3id.orgSawgraphV1Us-wqp#PrivateNon-IndustrialOrganization](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgSawgraphV1Us-wqp#PrivateNon-IndustrialOrganization.md) | None<br/>| 1 | 
| [HttpW3id.orgSawgraphV1Us-wqp#ResultMeasureQualifier](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgSawgraphV1Us-wqp#ResultMeasureQualifier.md) | None<br/>| 250 | 
| [HttpW3id.orgSawgraphV1Us-wqp#Sample-SpecificQuantitationLimit](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgSawgraphV1Us-wqp#Sample-SpecificQuantitationLimit.md) | None<br/>| 155 | 
| [HttpW3id.orgSawgraphV1Us-wqp#StateUSGovernmentOrganization](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgSawgraphV1Us-wqp#StateUSGovernmentOrganization.md) | None<br/>| 2 | 
| [HttpW3id.orgSawgraphV1Us-wqp#StateGovernmentUSOrganization](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgSawgraphV1Us-wqp#StateGovernmentUSOrganization.md) | None<br/>| 5 | 
| [HttpW3id.orgSawgraphV1Us-wqp#TaxonGroup.FishNekton](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgSawgraphV1Us-wqp#TaxonGroup.FishNekton.md) | None<br/>| 53 | 
| [OwlThing](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OwlThing.md) | The class of OWL individuals.<br/>| 14758 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CosoDetectionLimit](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/CosoDetectionLimit.md) | The lowest concentration of a substance that can be reliably detected as present with a reasonable degree of confidence.<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CosoDetectQuantityValue](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/CosoDetectQuantityValue.md) | A Quantity Value that represents a detection of the contaminant.<br/>| 305577 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CosoFeatureType](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/CosoFeatureType.md) | A category applied to differentiate discrete spatial phenomenon.<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpW3id.orgSawgraphV1Us-wqp#LocationType](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgSawgraphV1Us-wqp#LocationType.md) | None<br/>| 91 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpW3id.orgSawgraphV1Us-wqp#DefWQPGroundWaterFeatureType](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgSawgraphV1Us-wqp#DefWQPGroundWaterFeatureType.md) | None<br/>| 3 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpW3id.orgSawgraphV1Us-wqp#DefWQPSurfaceWaterFeatureType](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgSawgraphV1Us-wqp#DefWQPSurfaceWaterFeatureType.md) | None<br/>| 14 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpW3id.orgSawgraphV1Us-wqp#DefWQPWasteWaterFeatureType](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgSawgraphV1Us-wqp#DefWQPWasteWaterFeatureType.md) | None<br/>| 3 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CosoNonDetectQuantityValue](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/CosoNonDetectQuantityValue.md) | A Quantity Value that represents a non-detection of the contaminant. No numeric value is specified.<br/>| 898774 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CosoObservationAnnotation](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/CosoObservationAnnotation.md) | Metadata that qualifies an observation<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CosoOfComptoxSubstance](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/CosoOfComptoxSubstance.md) | A relation between an entity and a chemical substance as identified by Comptox<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CosoOfDatasetSubstance](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/CosoOfDatasetSubstance.md) | A relation between an entity and a chemical substance as identified in a dataset specific controlled vocabulary<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CosoQuantitationLimit](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/CosoQuantitationLimit.md) | The lowest concentration of a substance that can be reliably measured with acceptable precision and accuracy.<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CosoQuantityValue](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/CosoQuantityValue.md) | A Quantity Value expresses the magnitude and kind of a quantity as a product of a numerical value or enumerated value and a unit of measure.<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CosoResultQualifier](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/CosoResultQualifier.md) | Something that qualifies the result, such as quality control assessment, limitation on the precision or minimum detectable amount.<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CosoSampleAnnotation](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/CosoSampleAnnotation.md) | Metadata that qualifies a sample<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpW3id.orgSawgraphV1Us-wqp#Project](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgSawgraphV1Us-wqp#Project.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CosoSampleMaterialType](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/CosoSampleMaterialType.md) | The type of material that was sampled<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpW3id.orgSawgraphV1Us-wqp#SampleMedia](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgSawgraphV1Us-wqp#SampleMedia.md) | None<br/>| 8 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpW3id.orgSawgraphV1Us-wqp#Taxon](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgSawgraphV1Us-wqp#Taxon.md) | None<br/>| 67 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CosoSubstance](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/CosoSubstance.md) | Any organic or inorganic substance of a particular molecular identity, including any combination of these substances occurring in whole or in part as a result of a chemical reaction or occurring in nature, and any element or uncombined radical.<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpW3id.orgComptoxV1ChemicalEntity](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgComptoxV1ChemicalEntity.md) | None<br/>| 90 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpW3id.orgSawgraphV1Us-wqp#Characteristic](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgSawgraphV1Us-wqp#Characteristic.md) | None<br/>| 50 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CosoSubstanceCollection](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/CosoSubstanceCollection.md) | A collection of more than one substances.<br/>| 10 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpW3id.orgComptoxCompToxChemicalEntity](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgComptoxCompToxChemicalEntity.md) | None<br/>| 44 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpW3id.orgSawgraphV1Me-egad#EGAD-ConcentrationQualifier](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgSawgraphV1Me-egad#EGAD-ConcentrationQualifier.md) | None<br/>| 56 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpW3id.orgSawgraphV1Me-egad#EGAD-MethodDetectionLimit](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgSawgraphV1Me-egad#EGAD-MethodDetectionLimit.md) | Areas with land use activities which are potential and/or actual sources of contamination and areas where biological and surface water sampling is conducted.<br/>| 7006 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-ParameterName](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-ParameterName.md) | None<br/>| 101 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpW3id.orgSawgraphV1Me-egad#EGAD-ReportingLimit](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgSawgraphV1Me-egad#EGAD-ReportingLimit.md) | None<br/>| 4480 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpW3id.orgSawgraphV1Me-egad#EGAD-ResultType](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgSawgraphV1Me-egad#EGAD-ResultType.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleCollectionMethod](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleCollectionMethod.md) | None<br/>| 25 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleDetailedLocation](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleDetailedLocation.md) | None<br/>| 23 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleMaterialType](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleMaterialType.md) | None<br/>| 46 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleMaterialTypeQualifier](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleMaterialTypeQualifier.md) | None<br/>| 32 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePointType](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePointType.md) | None<br/>| 65 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleTreatmentStatus](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgSawgraphV1Me-egad#EGAD-SampleTreatmentStatus.md) | None<br/>| 2 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpW3id.orgSawgraphV1Me-egad#EGAD-SiteType](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgSawgraphV1Me-egad#EGAD-SiteType.md) | None<br/>| 62 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpW3id.orgSawgraphV1Me-egad#EGAD-ValidationLevel](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgSawgraphV1Me-egad#EGAD-ValidationLevel.md) | None<br/>| 6 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[KwgoS2CellLevel13](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/KwgoS2CellLevel13.md) | None<br/>| 86344 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[KwgoStatisticalArea](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/KwgoStatisticalArea.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MeEgadEGAD-ConcentrationQualifier](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/MeEgadEGAD-ConcentrationQualifier.md) | None<br/>| 56 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MeEgadEGAD-MethodDetectionLimit](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/MeEgadEGAD-MethodDetectionLimit.md) | Areas with land use activities which are potential and/or actual sources of contamination and areas where biological and surface water sampling is conducted.<br/>| 7006 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MeEgadEGAD-PFAS-ParameterName](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/MeEgadEGAD-PFAS-ParameterName.md) | None<br/>| 101 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MeEgadEGAD-ReportingLimit](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/MeEgadEGAD-ReportingLimit.md) | None<br/>| 4480 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MeEgadEGAD-ResultType](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/MeEgadEGAD-ResultType.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MeEgadEGAD-SampleCollectionMethod](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/MeEgadEGAD-SampleCollectionMethod.md) | None<br/>| 25 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MeEgadEGAD-SampleDetailedLocation](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/MeEgadEGAD-SampleDetailedLocation.md) | None<br/>| 23 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MeEgadEGAD-SampleMaterialType](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/MeEgadEGAD-SampleMaterialType.md) | None<br/>| 46 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MeEgadEGAD-SampleMaterialTypeQualifier](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/MeEgadEGAD-SampleMaterialTypeQualifier.md) | None<br/>| 32 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MeEgadEGAD-SamplePointType](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/MeEgadEGAD-SamplePointType.md) | None<br/>| 65 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MeEgadEGAD-SampleTreatmentStatus](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/MeEgadEGAD-SampleTreatmentStatus.md) | None<br/>| 2 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MeEgadEGAD-SiteType](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/MeEgadEGAD-SiteType.md) | None<br/>| 62 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MeEgadEGAD-ValidationLevel](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/MeEgadEGAD-ValidationLevel.md) | None<br/>| 6 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboBFO0000040](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboBFO0000040.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00001002](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00001002.md) | The FoodOn "food product" class is provided as a branch under which new food product categories and food products themselves can be placed. Here classes are provided to differentiate a food product by its food composition, processing and/or consumption characteristics. This avoids brand name products but it may include generic food dish categories. It has a much greater depth and polyhierarchy than other agency product type schemes have in an effort to group related products together.  The upper level basis of this tree originated in the environment ontology (ENVO) and from the US Code of Federal Regulations.<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00001006](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00001006.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00001015](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00001015.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00001040](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00001040.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00001041](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00001041.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00001046](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00001046.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00001057](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00001057.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00001092](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00001092.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00001093](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00001093.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00001105](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00001105.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00001131](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00001131.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00001134](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00001134.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00001147](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00001147.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00001172](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00001172.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00001173](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00001173.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00001175](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00001175.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00001176](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00001176.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00001209](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00001209.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00001242](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00001242.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00001248](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00001248.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00001250](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00001250.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00001251](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00001251.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00001256](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00001256.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00001257](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00001257.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00001261](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00001261.md) | FAO definition for vegetable: "Vegetables are plants cultivated both as field crops and garden crops, both in the open and under glass." and also: "Vegetables are grouped according to botanic characteristics as follows: leafy or stem vegetables (e.g., cabbage); fruit-bearing vegetables (e.g., melons); flower vegetables (e.g., cauliflowers); root, bulb and tuberous vegetables (e.g., onion); leguminous vegetables (e.g., green peas); other vegetables (e.g., green maize and mushrooms)."<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00001262](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00001262.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00001264](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00001264.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00001274](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00001274.md) | Regarding American regulatory aspects of egg products, see this summary:␊https://www.politico.com/agenda/story/2016/03/crazy-us-chicken-egg-regulation-graphic-000077<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00001275](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00001275.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00001283](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00001283.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00001291](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00001291.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00001293](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00001293.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00001628](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00001628.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00001635](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00001635.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00001678](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00001678.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00001783](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00001783.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00001792](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00001792.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00002044](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00002044.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00002051](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00002051.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00002140](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00002140.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00002142](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00002142.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00002143](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00002143.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00002147](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00002147.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00002150](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00002150.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00002153](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00002153.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00002156](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00002156.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00002159](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00002159.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00002165](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00002165.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00002236](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00002236.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00002265](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00002265.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00002309](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00002309.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00002381](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00002381.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00002403](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00002403.md) | This class is the top of FOODON's main food product hierarchy which is described in the https://www.foodon.org website, and can be searched in lookup services like https://www.ebi.ac.uk/ols/<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00002452](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00002452.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00002477](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00002477.md) | "Typically, it falls into two categories: ‘feathered’ or ‘furred’. Feathered game or game birds include grouse, pheasant, partridge, quail, snipe, wild duck, woodcock and wood pigeon. Furred game includes hare, rabbit, venison and ‘wild’ boar." [source: http://welshgamemeat.wales/en/what-is-game-meat/]<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00002576](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00002576.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00002581](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00002581.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00002616](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00002616.md) | An avian animal which is dead or alive and has a relatively intact body.<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00002689](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00002689.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00002753](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00002753.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00002765](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00002765.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00002819](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00002819.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00003004](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00003004.md) | A whole animal can be dead or alive, but its body must be relatively intact.<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00003042](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00003042.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00003083](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00003083.md) | A veal which is dead or alive and has a relatively intact body.<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00003204](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00003204.md) | "Eating one of these small bananas (about 100 g) covers the vitamin A requirement for 2 days. The Cavendish variety, on the other hand, contains almost no vitamin A. Growing vitamin A-rich banana varieties in more countries could contribute to a decline in global vitamin A deficiency." [http://www.fao.org/zhc/detail-events/en/c/446573/]<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00003425](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00003425.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00003567](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00003567.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00003572](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00003572.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00003814](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00003814.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00003816](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00003816.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00004172](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00004172.md) | None<br/>| 2 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00004183](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00004183.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00004242](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00004242.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00004298](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00004298.md) | A poultry which is dead or alive and has a relatively intact body.<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00004331](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00004331.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00004332](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00004332.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00004333](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00004333.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00004436](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00004436.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00004460](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00004460.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00004859](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00004859.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00004862](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00004862.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00004918](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00004918.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00004921](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00004921.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON02010001](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON02010001.md) | This includes things like eggs and milk.<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON02010005](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON02010005.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON02010006](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON02010006.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON02010012](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON02010012.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON02010013](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON02010013.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON02010014](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON02010014.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON02010015](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON02010015.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON02010024](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON02010024.md) | For a carcass with skin, use "animal carcass"<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON02010028](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON02010028.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON02021805](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON02021805.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON02010029](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON02010029.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON02010030](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON02010030.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON02010031](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON02010031.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON02010032](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON02010032.md) | None<br/>| 3 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON02010033](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON02010033.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON02010042](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON02010042.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON02010045](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON02010045.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON02010107](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON02010107.md) | Damion Dooley Feb 6, 2017: Good meat cut resources to incorporate for Canada: The CFIA Meat Cuts Manual http://www.inspection.gc.ca/food/labelling/meat-cuts/eng/1300126276015/1300126372856<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON02010108](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON02010108.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON02010111](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON02010111.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON02010112](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON02010112.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON02020840](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON02020840.md) | A bison which is dead or alive and has a relatively intact body.<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON02020892](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON02020892.md) | A cow which is dead or alive and has a relatively intact body.<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON02021651](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON02021651.md) | A pig which is dead or alive and has a relatively intact body.<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON02021802](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON02021802.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON02021803](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON02021803.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03301293](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03301293.md) | SIREN DB annotation:␊* whole, natural shape FOODON:03430150␊* not heat-treated FOODON:03440003␊* whole plant or most parts used FOODON:03420150␊* water removal process FOODON:03460138␊* preservation by dehydration or drying FOODON:03470116␊* food animal as consumer FOODON:03510015<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03302001](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03302001.md) | SIREN DB annotation:␊* part of animal FOODON:03420164<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03303380](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03303380.md) | SIREN DB annotation:␊* whole, natural shape FOODON:03430150␊* not heat-treated FOODON:03440003␊* part of plant FOODON:03420174<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03304313](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03304313.md) | SIREN DB annotation:␊* whole, natural shape FOODON:03430150␊* not heat-treated FOODON:03440003␊* germinated or sprouted seed FOODON:03420102<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03304497](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03304497.md) | SIREN DB annotation:␊* whole, natural shape FOODON:03430150␊* seed (anatomical part) FOODON:03420155<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03304616](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03304616.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03306306](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03306306.md) | SIREN DB annotation:␊* semiliquid FOODON:03430103␊* blood UBERON:0000178<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03309997](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03309997.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON00002127](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON00002127.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03301750](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03301750.md) | SIREN DB annotation:␊* whole, natural shape FOODON:03430150␊* not heat-treated FOODON:03440003␊* whole plant or most parts used FOODON:03420150␊* non-food animal as food consumer FOODON:03510013␊* food animal as consumer FOODON:03510015<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03301761](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03301761.md) | SIREN DB annotation:␊* whole, natural shape FOODON:03430150␊* not heat-treated FOODON:03440003␊* whole plant or most parts used FOODON:03420150␊* non-food animal as food consumer FOODON:03510013␊* food animal as consumer FOODON:03510015<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03310611](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03310611.md) | SIREN DB annotation:␊* meat color, undesignated or unknown (deprecated) FOODON:03530003␊* skeletal meat part FOODON:03420175<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03310961](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03310961.md) | SIREN DB annotation:␊* part of animal FOODON:03420164<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03315150](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03315150.md) | SIREN DB annotation:␊* milk (mammary secretion) UBERON:0001913<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03315173](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03315173.md) | SIREN DB annotation:␊* skeletal meat part FOODON:03420175<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03315308](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03315308.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03315468](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03315468.md) | SIREN DB annotation:␊* solid FOODON:03430151␊* meat part of animal FOODON:03420103<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03315769](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03315769.md) | SIREN DB annotation:␊* liquid, low viscosity, with no visible particles FOODON:03430123␊* not heat-treated FOODON:03440003␊* blood UBERON:0000178<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03315883](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03315883.md) | SIREN DB annotation:␊* solid FOODON:03430151␊* meat part of animal FOODON:03420103<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03316061](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03316061.md) | This term is ambiguous about whether shell remains on egg or not, i.e. this encompasses both an uncooked egg in shell, or a boiled peeled egg, or a fried egg.<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03317076](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03317076.md) | SIREN DB annotation:␊* solid FOODON:03430151␊* root, tuber or bulb FOODON:03420238<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03317170](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03317170.md) | SIREN DB annotation:␊* animal body or body part FOODON:03420127<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411005](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411005.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411006](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411006.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411013](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411013.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411017](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411017.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411018](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411018.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411021](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411021.md) | This is equivalent to:␊␊'fish (food source)' or 'shellfish (food source)' or 'crustacean (food source)' or 'echinoderm (food source)' or 'coelenterate (food source)'␊␊However, this disjunction appears to be a burden on reasoners, and so this is currently not implemented.<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411022](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411022.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411024](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411024.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411036](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411036.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411047](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411047.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411048](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411048.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411057](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411057.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411058](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411058.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411062](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411062.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411121](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411121.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411129](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411129.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411134](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411134.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411136](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411136.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411139](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411139.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411140](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411140.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411142](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411142.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411151](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411151.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411156](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411156.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411174](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411174.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411179](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411179.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411183](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411183.md) | A sheep which is dead or alive and has a relatively intact body.<br/>| 2 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411184](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411184.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411194](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411194.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411213](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411213.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411222](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411222.md) | "Most fish are ectothermic ('cold-blooded'), allowing their body temperatures to vary as ambient temperatures change, though some of the large active swimmers like white shark and tuna can hold a higher core temperature." - https://en.wikipedia.org/wiki/Fish<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411223](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411223.md) | A mussel which is dead or alive and has a relatively intact body.<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411231](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411231.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411232](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411232.md) | LanguaL curation note: Use 'field corn' for any breakfast cereals or snack foods having 'corn' as the main ingredient.<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411236](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411236.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411266](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411266.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411293](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411293.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411297](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411297.md) | LanguaL curation note: For a unicellular animal, use *ALGAE OR FUNGUS USED AS FOOD SOURCE*.<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411319](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411319.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411324](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411324.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411325](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411325.md) | A beaver which is dead or alive and has a relatively intact body.<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411328](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411328.md) | A goat which is dead or alive and has a relatively intact body.<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411331](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411331.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411365](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411365.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411598](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411598.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411040](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411040.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03412007](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03412007.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03414066](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03414066.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03414067](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03414067.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411374](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411374.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411380](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411380.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411393](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411393.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411409](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411409.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411433](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411433.md) | Covers both freshwater and saltwater organisms<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411439](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411439.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411447](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411447.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411454](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411454.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411457](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411457.md) | A chicken which is dead or alive and has a relatively intact body.<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411491](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411491.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411500](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411500.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411539](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411539.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411557](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411557.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411563](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411563.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411564](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411564.md) | This was LanguaL definition: Individual plant or animal from which the food product or its major ingredient is derived; also a chemical food source [FDA CFSAN 1995].<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411566](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411566.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411567](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411567.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411568](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411568.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411579](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411579.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411581](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411581.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03412005](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03412005.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411204](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411204.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411583](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411583.md) | A deer which is dead or alive and has a relatively intact body.<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411592](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411592.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411594](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411594.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411595](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411595.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411597](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411597.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411599](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411599.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411607](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411607.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411614](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411614.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411617](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411617.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411669](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411669.md) | A lamb which is dead or alive and has a relatively intact body.<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411818](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411818.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03414028](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03414028.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411826](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411826.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411892](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411892.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03412004](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03412004.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03412112](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03412112.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03412113](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03412113.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03412241](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03412241.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03412331](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03412331.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03412362](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03412362.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03412409](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03412409.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03412426](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03412426.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03412453](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03412453.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03412665](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03412665.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03413357](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03413357.md) | LanguaL curation note: This term is for CLASSIFICATION ONLY; DO NOT USE term in indexing. Use a more precise narrower term.<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03413358](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03413358.md) | None<br/>| 2 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03413360](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03413360.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03413372](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03413372.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03413377](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03413377.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03413378](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03413378.md) | None<br/>| 2 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03413406](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03413406.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03413448](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03413448.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03413807](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03413807.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03411126](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03411126.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03413808](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03413808.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03414051](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03414051.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03414209](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03414209.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03414282](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03414282.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03414302](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03414302.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03414374](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03414374.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03414381](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03414381.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03414459](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03414459.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03414460](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03414460.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03414494](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03414494.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03414741](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03414741.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03414742](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03414742.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03414745](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03414745.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03414934](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03414934.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03414972](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03414972.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03420101](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03420101.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03420106](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03420106.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03420116](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03420116.md) | LanguaL curation note: "e.g. *LEAF*, *ROOT OR TUBER*, *ORGAN MEAT*, *MILK* OR *EGG*; it also includes components of parts, such as *CREAM*, and extracts, concentrates or isolates, such as *PROTEIN EXTRACT* or *SUGAR*."<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03420122](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03420122.md) | LanguaL curation note: *BLOOD* AND *INK, AQUATIC ANIMAL* are now listed under organism substance.<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03420127](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03420127.md) | This class and its subclasses can be used if it is ambiguous whether the reference is being made to a whole animal or some part of it, including parts of organs rather than whole organs.␊␊LanguaL curation note: Includes carcass meat, organ meat, and nonmeat parts of animals, as well as the whole animal.<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03420173](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03420173.md) | LanguaL curation note: Used when the entire animal body is the food source. Head or tail may have been removed. Use the appropriate narrower term depending on the presence or absence of skin, feathers, scales, fins and/or entrails. The body may have been cut into pieces or disintegrated.<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03420147](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03420147.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03420129](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03420129.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03420144](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03420144.md) | LanguaL curation note: This broad term is used for the plant as a whole, excluding the root and the fruit; for any piece consisting of two or more individual parts (e.g., a celery stalk with the leaf blades attached); or for any mixture of two or more individual parts (e.g., mushroom stems and pieces).<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03420145](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03420145.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03420148](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03420148.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03420150](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03420150.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03420164](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03420164.md) | Langual note: Includes eggs and milk that, although separated from the animal, are produced as integral parts and are affected by the animal's food intake and metabolism.<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03420181](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03420181.md) | LanguaL curation note: Compare *SHELL (SEED)*.<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03420183](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03420183.md) | LanguaL curation note: Compare *GERMINATED OR SPROUTED SEED* and *STEM, STALK (WITHOUT LEAVES)*.<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03420194](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03420194.md) | LanguaL curation note: Fish roe are indexed under *OVARY, ROE*.<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03420202](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03420202.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03420218](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03420218.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03420238](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03420238.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03420239](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03420239.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03460177](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03460177.md) | LanguaL curation note: With the exception of peanut (see *PEANUT OR PEANUT BUTTER ADDED*), used when a nut or seed ingredient is the second ingredient in order of predominance.<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboFOODON03602002](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboFOODON03602002.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon1003242](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon1003242.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon1003875](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon1003875.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon1003877](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon1003877.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon10184](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon10184.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon102804](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon102804.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon102809](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon102809.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon102810](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon102810.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon102812](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon102812.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon102814](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon102814.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon102818](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon102818.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon109170](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon109170.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon1110380](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon1110380.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon1110386](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon1110386.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon112818](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon112818.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon115479](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon115479.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon117571](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon117571.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon1176516](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon1176516.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon1184124](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon1184124.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon119950](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon119950.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon120289](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon120289.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon1203511](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon1203511.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon123366](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon123366.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon123368](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon123368.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon123369](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon123369.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon125009](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon125009.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon126735](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon126735.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon128017](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon128017.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon1307774](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon1307774.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon1307775](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon1307775.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon1307796](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon1307796.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon1308840](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon1308840.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon1329799](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon1329799.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon13336](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon13336.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon1338369](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon1338369.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon13424](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon13424.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon13426](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon13426.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon13492](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon13492.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon13749](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon13749.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon1437010](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon1437010.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon1437180](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon1437180.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon1437183](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon1437183.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon1437197](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon1437197.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon1437201](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon1437201.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon144561](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon144561.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon1463138](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon1463138.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon147366](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon147366.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon147368](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon147368.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon147369](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon147369.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon147370](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon147370.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon147389](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon147389.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon147429](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon147429.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon147949](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon147949.md) | None<br/>| 2 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon1489341](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon1489341.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon1489388](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon1489388.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon1489793](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon1489793.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon1489872](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon1489872.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon1489922](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon1489922.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon1489923](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon1489923.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon30870](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon30870.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon225388](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon225388.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon225389](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon225389.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon1489940](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon1489940.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon15105](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon15105.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon151069](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon151069.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon151071](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon151071.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon1521262](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon1521262.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon1538097](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon1538097.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon1545897](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon1545897.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon1549675](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon1549675.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon156152](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon156152.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon1589896](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon1589896.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon159053](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon159053.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon1609961](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon1609961.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon1609962](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon1609962.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon162743](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon162743.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon163487](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon163487.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon16360](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon16360.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon163735](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon163735.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon163743](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon163743.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon1648004](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon1648004.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon1648017](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon1648017.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon1648033](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon1648033.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon165297](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon165297.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon169617](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon169617.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon169618](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon169618.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon169642](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon169642.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon169655](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon169655.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon169697](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon169697.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon169700](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon169700.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon169703](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon169703.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon169705](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon169705.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon169725](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon169725.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon169733](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon169733.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon169746](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon169746.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon1699513](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon1699513.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon1699523](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon1699523.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon17047](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon17047.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon1705104](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon1705104.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon171637](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon171637.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon171638](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon171638.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon1728959](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon1728959.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon173691](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon173691.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon174217](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon174217.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon178174](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon178174.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon180118](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon180118.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon1804623](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon1804623.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon181185](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon181185.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon183218](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon183218.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon184451](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon184451.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon186265](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon186265.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon186623](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon186623.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon186625](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon186625.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon186626](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon186626.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon186628](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon186628.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon186634](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon186634.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon1874399](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon1874399.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon19205](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon19205.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon1927087](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon1927087.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon193297](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon193297.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon194251](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon194251.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon1968271](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon1968271.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon1968429](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon1968429.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon1977918](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon1977918.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon198777](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon198777.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon19955](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon19955.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon201017](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon201017.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon214693](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon214693.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon214697](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon214697.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon21472](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon21472.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon214907](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon214907.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon214908](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon214908.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon214929](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon214929.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon215450](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon215450.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon21563](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon21563.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon21571](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon21571.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon216703](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon216703.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon217033](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon217033.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon217035](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon217035.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon217037](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon217037.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon217062](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon217062.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon219121](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon219121.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon219134](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon219134.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon221251](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon221251.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon22140](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon22140.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon2231382](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon2231382.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon2231383](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon2231383.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon2231390](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon2231390.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon2231393](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon2231393.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon2233838](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon2233838.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon2233839](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon2233839.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon2233855](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon2233855.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon2233857](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon2233857.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon22663](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon22663.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon22665](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon22665.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon22774](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon22774.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon22973](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon22973.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon22978](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon22978.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon2304100](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon2304100.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon23066](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon23066.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon23139](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon23139.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon23216](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon23216.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon23222](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon23222.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon232347](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon232347.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon233713](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon233713.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon233715](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon233715.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon233880](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon233880.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon23461](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon23461.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon23513](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon23513.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon235595](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon235595.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon23672](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon23672.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon23808](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon23808.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon241778](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon241778.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon241780](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon241780.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon241789](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon241789.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon241793](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon241793.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon241799](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon241799.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon241800](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon241800.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon241806](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon241806.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon245205](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon245205.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon24646](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon24646.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon24663](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon24663.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon24966](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon24966.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon259381](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon259381.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon25996](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon25996.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon260143](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon260143.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon260718](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon260718.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon26468](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon26468.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon26496](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon26496.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon26867](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon26867.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon2706](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon2706.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon2732585](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon2732585.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon2759](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon2759.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon27592](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon27592.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon27705](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon27705.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon225060](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon225060.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon27706](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon27706.md) | None<br/>| 2 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon27778](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon27778.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon278205](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon278205.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon2785011](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon2785011.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon2785015](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon2785015.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon284555](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon284555.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon28974](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon28974.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon2908833](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon2908833.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon290983](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon290983.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon29132](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon29132.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon296036](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon296036.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon2976026](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon2976026.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon29780](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon29780.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon301453](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon301453.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon301959](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon301959.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon303185](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon303185.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon314145](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon314145.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon314146](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon314146.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon314147](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon314147.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon32443](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon32443.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon32519](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon32519.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon32523](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon32523.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon32524](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon32524.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon32525](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon32525.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon32561](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon32561.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3268](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3268.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3275](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3275.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3282](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3282.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3296](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3296.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3297](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3297.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon33090](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon33090.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon33154](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon33154.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon33208](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon33208.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon33213](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon33213.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon33317](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon33317.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon33511](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon33511.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3394](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3394.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3395](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3395.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3398](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3398.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3400](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3400.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3440](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3440.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon34542](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon34542.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3465](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3465.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3468](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3468.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon34815](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon34815.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon34816](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon34816.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon46259](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon46259.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3487](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3487.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3488](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3488.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3489](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3489.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3493](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3493.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3497](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3497.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3499](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3499.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3524](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3524.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3542](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3542.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon35500](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon35500.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3558](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3558.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3563](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3563.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3564](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3564.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3568](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3568.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3587](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3587.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon359160](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon359160.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3593](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3593.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3602](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3602.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3603](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3603.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3608](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3608.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3615](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3615.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3618](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3618.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3620](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3620.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3623](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3623.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3624](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3624.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3629](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3629.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3640](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3640.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon364270](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon364270.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3646](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3646.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3647](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3647.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3649](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3649.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3650](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3650.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3653](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3653.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3655](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3655.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3660](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3660.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon36603](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon36603.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon36609](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon36609.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3669](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3669.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3671](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3671.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3676](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3676.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3683](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3683.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3684](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3684.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3688](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3688.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3699](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3699.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3700](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3700.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3705](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3705.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3707](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3707.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3737](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3737.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3740](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3740.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3744](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3744.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3745](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3745.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3746](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3746.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3749](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3749.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3754](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3754.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3766](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3766.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3801](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3801.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3803](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3803.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3804](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3804.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3807](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3807.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon381124](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon381124.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3814](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3814.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3822](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3822.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3853](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3853.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon38820](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon38820.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3883](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3883.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3884](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3884.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3885](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3885.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3904](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3904.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3906](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3906.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3913](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3913.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3917](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3917.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3928](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3928.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon3931](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon3931.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon4011](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon4011.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon4014](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon4014.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon4018](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon4018.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon4019](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon4019.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon4020](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon4020.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon4033](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon4033.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon4037](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon4037.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon4038](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon4038.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon4039](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon4039.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon40548](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon40548.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon4055](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon4055.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon4056](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon4056.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon40674](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon40674.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon40685](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon40685.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon4069](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon4069.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon4070](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon4070.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon4071](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon4071.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon4072](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon4072.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon4107](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon4107.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon4113](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon4113.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon4118](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon4118.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon4119](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon4119.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon4136](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon4136.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon4143](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon4143.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon4144](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon4144.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon41665](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon41665.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon41705](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon41705.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon41768](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon41768.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon41773](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon41773.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon41937](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon41937.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon41938](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon41938.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon41944](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon41944.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon41945](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon41945.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon41946](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon41946.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon41947](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon41947.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon4199](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon4199.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon4200](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon4200.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon4201](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon4201.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon4204](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon4204.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon4206](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon4206.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon4210](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon4210.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon42148](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon42148.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon4216](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon4216.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon42219](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon42219.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon4231](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon4231.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon4235](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon4235.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon424551](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon424551.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon424573](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon424573.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon426106](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon426106.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon4268](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon4268.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon4281](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon4281.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon4294](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon4294.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon432663](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon432663.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon4335](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon4335.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon4345](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon4345.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon43690](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon43690.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon43707](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon43707.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon43860](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon43860.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon4410](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon4410.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon4447](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon4447.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon4454](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon4454.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon4479](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon4479.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon4577](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon4577.md) | FoodOn Note: the NCBITaxon exact synonym "maize" is more appropriate for "Zea mays subsp. mays"<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon4581](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon4581.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon45918](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon45918.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon4609](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon4609.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon4610](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon4610.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon4613](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon4613.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon46145](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon46145.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon4615](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon4615.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon4618](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon4618.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon46260](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon46260.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon4637](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon4637.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon4638](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon4638.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon4639](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon4639.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon4640](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon4640.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon4641](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon4641.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon4642](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon4642.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon4668](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon4668.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon4671](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon4671.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon4678](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon4678.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon4710](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon4710.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon4719](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon4719.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon4731](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon4731.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon4732](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon4732.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon4734](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon4734.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon47605](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon47605.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon479623](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon479623.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon50173](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon50173.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon50174](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon50174.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon50190](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon50190.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon50384](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon50384.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon66912](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon66912.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon504568](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon504568.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon8016](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon8016.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon8022](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon8022.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon8028](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon8028.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon8032](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon8032.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon50457](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon50457.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon516948](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon516948.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon51952](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon51952.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon52838](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon52838.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon53868](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon53868.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon54476](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon54476.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon557010](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon557010.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon55961](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon55961.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon57918](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon57918.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon58023](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon58023.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon58024](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon58024.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon58228](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon58228.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon58486](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon58486.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon58860](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon58860.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon59165](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon59165.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon6072](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon6072.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon641307](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon641307.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon6447](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon6447.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon6544](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon6544.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon6545](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon6545.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon6547](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon6547.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon6548](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon6548.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon6550](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon6550.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon6599](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon6599.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon6602](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon6602.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon6604](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon6604.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon6605](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon6605.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon6606](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon6606.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon66670](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon66670.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon66672](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon66672.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon69108](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon69108.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon69109](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon69109.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon693794](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon693794.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon703407](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon703407.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon71243](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon71243.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon71274](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon71274.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon71275](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon71275.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon71611](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon71611.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon72025](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon72025.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon72171](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon72171.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon721789](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon721789.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon721813](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon721813.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon73496](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon73496.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon742010](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon742010.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon745060](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon745060.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon7711](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon7711.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon7742](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon7742.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon7776](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon7776.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon78536](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon78536.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon7898](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon7898.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon79331](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon79331.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon7952](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon7952.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon7968](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon7968.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon154810](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon154810.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon154811](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon154811.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon7969](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon7969.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon7971](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon7971.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon7995](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon7995.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon7996](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon7996.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon75287](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon75287.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon75288](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon75288.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon7997](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon7997.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon66913](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon66913.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon7998](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon7998.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon8006](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon8006.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon8007](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon8007.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon8008](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon8008.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon8009](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon8009.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon8010](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon8010.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon8015](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon8015.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon8033](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon8033.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon8038](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon8038.md) | None<br/>| 3 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon8111](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon8111.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon8112](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon8112.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon8165](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon8165.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon283033](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon283033.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon283036](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon283036.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon8166](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon8166.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon8167](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon8167.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon8180](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon8180.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon13105](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon13105.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon13106](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon13106.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon8181](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon8181.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon8182](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon8182.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon83431](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon83431.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon84005](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon84005.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon84860](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon84860.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon8492](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon8492.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon85249](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon85249.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon85571](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon85571.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon866800](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon866800.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon8782](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon8782.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon8825](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon8825.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon89151](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon89151.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon8976](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon8976.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon9005](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon9005.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon9031](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon9031.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon9072](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon9072.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon9102](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon9102.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon9103](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon9103.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon911341](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon911341.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon91561](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon91561.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon91835](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon91835.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon91836](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon91836.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon91882](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon91882.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon91888](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon91888.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon9347](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon9347.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon96479](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon96479.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon980193](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon980193.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon981071](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon981071.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon9821](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon9821.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon9823](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon9823.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon9825](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon9825.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon9850](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon9850.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon986140](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon986140.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon9895](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon9895.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon9900](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon9900.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon9903](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon9903.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon9913](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon9913.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon9922](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon9922.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon9925](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon9925.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon9935](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon9935.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon9940](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon9940.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon99568](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon99568.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon9963](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon9963.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboNCBITaxon9989](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboNCBITaxon9989.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboOBI0100026](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboOBI0100026.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboPO0000003](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboPO0000003.md) | Examples include plant embryo (PO:0009009), megagametophyte (PO:0025279) and microgametophyte (PO:0025280).<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboPO0025034](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboPO0025034.md) | LanguaL definition: The flat or fleshy expanded blade (lamina) including a small and insignificant leafstalk but excluding a large and fleshy leafstalk such as celery stalks or rhubarb stalks.␊␊LanguaL curation note: If the part indexed consists of a large leafstalk and a leaf blade, use *PLANT ABOVE SURFACE, EXCLUDING FRUIT OR SEED*. Compare *STEM, STALK (WITHOUT LEAVES)*.<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboUBERON0000948](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboUBERON0000948.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboUBERON0001913](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboUBERON0001913.md) | LanguaL curation note: See scope note for *MILK OR MILK COMPONENT*. for lowfat milk use *FAT PARTIALLY REMOVED*; for skim milk, use *FAT FULLY REMOVED* (both found in D3. TREATMENT APPLIED).<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboUBERON0002097](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboUBERON0002097.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboUBERON0002107](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboUBERON0002107.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboUBERON0005079](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboUBERON0005079.md) | LanguaL term definition: The covering of a bird or reptile egg.<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboUBERON0007378](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboUBERON0007378.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboUBERON0007379](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboUBERON0007379.md) | LanguaL curation note: The egg shell functions as a container. Therefore, the physical state of a raw egg in the shell is *LIQUID, HIGH VISCOSITY, WITH NO VISIBLE PARTICLES*.<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OboUBERON0008944](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/OboUBERON0008944.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[QudtEnumeratedQuantity](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/QudtEnumeratedQuantity.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SosaProcedure](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/SosaProcedure.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CosoAnalysisMethod](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/CosoAnalysisMethod.md) | The analysis method used to identify the contaminant.<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpW3id.orgSawgraphV1Us-wqp#AnalyticalMethod](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgSawgraphV1Us-wqp#AnalyticalMethod.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpW3id.orgSawgraphV1Me-egad#EGAD-AnalysisMethod](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgSawgraphV1Me-egad#EGAD-AnalysisMethod.md) | None<br/>| 13 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpW3id.orgSawgraphV1Us-wqp#SampleCollectionMethod](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgSawgraphV1Us-wqp#SampleCollectionMethod.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MeEgadEGAD-AnalysisMethod](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/MeEgadEGAD-AnalysisMethod.md) | None<br/>| 13 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SosaProperty](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/SosaProperty.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CosoContaminantAbsoluteQuantityKind](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/CosoContaminantAbsoluteQuantityKind.md) | A type of contaminant quantity that is an absolute amount, such as a mass or volume.<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CosoContaminantConcentrationQuantityKind](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/CosoContaminantConcentrationQuantityKind.md) | A type of contaminant quantity that is a concentration measurement.<br/>| 4 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CosoContaminantMassQuantityKind](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/CosoContaminantMassQuantityKind.md) | The type of quantity that is measured for the contaminant.<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CosoContaminantRelativeQuantityKind](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/CosoContaminantRelativeQuantityKind.md) | A type of contaminant quantity that is a relative amount, such as a concentration.<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CosoContaminantVolumeQuantityKind](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/CosoContaminantVolumeQuantityKind.md) | A type of contaminant quantity that is a volume measurement.<br/>| 2 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CosoContaminationProperty](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/CosoContaminationProperty.md) | An observable quality of a feature related to its contamination.<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SosaSample](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/SosaSample.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CosoAnimalBloodSample](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/CosoAnimalBloodSample.md) | None<br/>| 5 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CosoAnimalMaterialSample](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/CosoAnimalMaterialSample.md) | None<br/>| 11 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CosoAnimalMilkSample](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/CosoAnimalMilkSample.md) | None<br/>| 429 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CosoAnimalOrganSample](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/CosoAnimalOrganSample.md) | None<br/>| 82 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CosoAnimalTissueSample](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/CosoAnimalTissueSample.md) | None<br/>| 894 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CosoBiotaSample](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/CosoBiotaSample.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CosoFilteredWaterSample](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/CosoFilteredWaterSample.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CosoMaterialSample](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/CosoMaterialSample.md) | A physical, tangible sample.<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CosoAirSample](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/CosoAirSample.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CosoSolidMaterialSample](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/CosoSolidMaterialSample.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CosoSedimentSample](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/CosoSedimentSample.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CosoSolidWasteSample](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/CosoSolidWasteSample.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpW3id.orgSawgraphV1Us-wqp#Sample](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgSawgraphV1Us-wqp#Sample.md) | None<br/>| 5109 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CosoPlantAbovegroundSample](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/CosoPlantAbovegroundSample.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CosoPlantMaterialSample](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/CosoPlantMaterialSample.md) | None<br/>| 252 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CosoPlantUndergroundSample](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/CosoPlantUndergroundSample.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CosoRawWaterSample](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/CosoRawWaterSample.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CosoSoilSample](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/CosoSoilSample.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CosoWaterSample](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/CosoWaterSample.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CosoWaterSampleBySource](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/CosoWaterSampleBySource.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CosoDrinkingWaterSample](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/CosoDrinkingWaterSample.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CosoGroundWaterSample](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/CosoGroundWaterSample.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpW3id.orgSawgraphV1Us-wqp#DefWQPGroundWaterSample](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgSawgraphV1Us-wqp#DefWQPGroundWaterSample.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CosoSurfaceWaterSample](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/CosoSurfaceWaterSample.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpW3id.orgSawgraphV1Us-wqp#DefWQPSurfaceWaterSample](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgSawgraphV1Us-wqp#DefWQPSurfaceWaterSample.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CosoWasteWaterSample](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/CosoWasteWaterSample.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpW3id.orgSawgraphV1Us-wqp#DefWQPWasteWaterSample](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgSawgraphV1Us-wqp#DefWQPWasteWaterSample.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CosoWaterSampleByTreatment](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/CosoWaterSampleByTreatment.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CosoTreatedWaterSample](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/CosoTreatedWaterSample.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgSawgraphV1Me-egad#EGAD-Sample.md) | None<br/>| 23024 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgSawgraphV1Me-egad-data#DefEGADBeefBloodSample.md) | None<br/>| 81 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgSawgraphV1Me-egad-data#DefEGADDrinkingWaterSample.md) | None<br/>| 156 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgSawgraphV1Me-egad-data#DefEGADGroundWaterSample.md) | None<br/>| 14713 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgSawgraphV1Me-egad-data#DefEGADPorkBloodSample.md) | None<br/>| 2 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSoilSample.md) | None<br/>| 3253 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgSawgraphV1Me-egad-data#DefEGADSurfaceWaterSample.md) | None<br/>| 486 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MeEgadEGAD-Sample](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/MeEgadEGAD-Sample.md) | None<br/>| 23024 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[StadQualityKind](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/StadQualityKind.md) | None<br/>| 4 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[StadQuantity](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/StadQuantity.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[StadSingleData](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/StadSingleData.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[StadStatisticalAggregateData](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/StadStatisticalAggregateData.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[StadStatisticalQuantityKind](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/StadStatisticalQuantityKind.md) | None<br/>| 2 | 
| [ProvAgent](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/ProvAgent.md) | An agent is something that bears some form of responsibility for an activity taking place, for the existence of an entity, or for another agent's activity.<br/>| 686 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ProvOrganization](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/ProvOrganization.md) | An organization is a social or legal institution such as a company, society, etc.<br/>| 77 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpW3id.orgSawgraphV1Us-wqp#Organization](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgSawgraphV1Us-wqp#Organization.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpW3id.orgSawgraphV1Us-wqp#Lab](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgSawgraphV1Us-wqp#Lab.md) | None<br/>|  | 
| [SosaFeatureOfInterest](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/SosaFeatureOfInterest.md) | None<br/>| 46048 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CosoFeature](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/CosoFeature.md) | The discrete spatial phenomenon that is the target of the observation.<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CosoMonitoredFeature](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/CosoMonitoredFeature.md) | The discrete spatial phenomenon that is the target of a release observation due to environmental monitoring.<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CosoPoint](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/CosoPoint.md) | The point location at which an observation occurred.<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CosoReleaseFeature](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/CosoReleaseFeature.md) | The discrete spatial phenomenon that may be the target of a release observation.<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CosoReleasePoint](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/CosoReleasePoint.md) | The point location at which a release observation occurred.<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CosoSampledFeature](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/CosoSampledFeature.md) | The discrete spatial phenomenon that is the target of a sample observation.<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpW3id.orgSawgraphV1Us-wqp#SampledFeature](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgSawgraphV1Us-wqp#SampledFeature.md) | None<br/>| 472 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CosoSamplePoint](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/CosoSamplePoint.md) | The point location at which a sample observation occurred.<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpW3id.orgSawgraphV1Us-wqp#Site](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgSawgraphV1Us-wqp#Site.md) | None<br/>| 388 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Site](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Site.md) | None<br/>| 1014 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpW3id.orgSawgraphV1Me-egad#EGAD-SampledFeature](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgSawgraphV1Me-egad#EGAD-SampledFeature.md) | None<br/>| 8040 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgSawgraphV1Me-egad#EGAD-SamplePoint.md) | None<br/>| 8324 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpW3id.orgSawgraphV1Me-egad#EGAD-Site](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgSawgraphV1Me-egad#EGAD-Site.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MeEgadEGAD-PFAS-Site](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/MeEgadEGAD-PFAS-Site.md) | None<br/>| 1014 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MeEgadEGAD-SampledFeature](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/MeEgadEGAD-SampledFeature.md) | None<br/>| 8040 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MeEgadEGAD-SamplePoint](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/MeEgadEGAD-SamplePoint.md) | None<br/>| 8324 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MeEgadEGAD-Site](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/MeEgadEGAD-Site.md) | None<br/>|  | 
| [SosaObservation](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/SosaObservation.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CosoContaminantObservation](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/CosoContaminantObservation.md) | An observation of a contaminant.<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CosoContaminantReleaseObservation](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/CosoContaminantReleaseObservation.md) | An observation of a contaminant that was released into the environment.<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CosoContaminantSampleObservation](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/CosoContaminantSampleObservation.md) | An observation of a contaminant that was sampled from the environment.<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpW3id.orgSawgraphV1Us-wqp#Observation](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgSawgraphV1Us-wqp#Observation.md) | None<br/>| 128674 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgSawgraphV1Me-egad#EGAD-PFAS-Observation.md) | None<br/>| 576763 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MeEgadEGAD-PFAS-Observation](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/MeEgadEGAD-PFAS-Observation.md) | None<br/>| 576763 | 
| [SosaResult](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/SosaResult.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CosoAggregateContaminantMeasurement](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/CosoAggregateContaminantMeasurement.md) | The result of an observation about contaminant(s) that is an aggregate measurement. This can be a spatial, temporal or contaminant aggregate.<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CosoContaminantAbsoluteMeasurement](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/CosoContaminantAbsoluteMeasurement.md) | The result of an observation about a contaminant that is an absolute measurement.<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CosoContaminantMeasurement](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/CosoContaminantMeasurement.md) | The result of an observation about a contaminant or contaminants.<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CosoContaminantRelativeMeasurement](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/CosoContaminantRelativeMeasurement.md) | The result of an observation about a contaminant that is a relative measurement.<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CosoSingleContaminantMeasurement](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/CosoSingleContaminantMeasurement.md) | The result of an observation about a contaminant that is a single measurement, i.e. a single contaminant at one location from one sample.<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpW3id.orgSawgraphV1Us-wqp#Single-PFAS-Concentration](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgSawgraphV1Us-wqp#Single-PFAS-Concentration.md) | None<br/>| 128674 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpW3id.orgSawgraphV1Me-egad#EGAD-AggregatePFAS-Concentration](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgSawgraphV1Me-egad#EGAD-AggregatePFAS-Concentration.md) | None<br/>| 37677 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[HttpW3id.orgSawgraphV1Me-egad#EGAD-SinglePFAS-Concentration](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/HttpW3id.orgSawgraphV1Me-egad#EGAD-SinglePFAS-Concentration.md) | None<br/>| 539086 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MeEgadEGAD-AggregatePFAS-Concentration](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/MeEgadEGAD-AggregatePFAS-Concentration.md) | None<br/>| 37677 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MeEgadEGAD-SinglePFAS-Concentration](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/MeEgadEGAD-SinglePFAS-Concentration.md) | None<br/>| 539086 | 
| [StadDatapoint](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/StadDatapoint.md) | None<br/>|  | 
| [StadDataTransformation](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/StadDataTransformation.md) | None<br/>|  | 
| [StadDataValue](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/StadDataValue.md) | None<br/>|  | 
| [XsdAnyURI](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/classes/XsdAnyURI.md) | None<br/>|  | 





## Slots

| Slot | Description | Occurrences |
| --- | --- | --- |
| [coso_analysisMethod](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/coso_analysisMethod.md) | <br/>| 1155212 |
| [coso_analyzedSample](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/coso_analyzedSample.md) | A relation between an observation of a contaminant and the sample that was an...<br/>| 1282200 |
| [coso_casNumber](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/coso_casNumber.md) | The cas number of the substance<br/>| 226 |
| [coso_fromSamplePoint](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/coso_fromSamplePoint.md) | A relation between a physical material sample and the location where the samp...<br/>| 51183 |
| [coso_hasAnyFeatureOfInterest](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/coso_hasAnyFeatureOfInterest.md) | A relation between an observation of a contaminant and a feature it is the su...<br/>| 3461978 |
| [coso_hasFeatureOfInterest](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/coso_hasFeatureOfInterest.md) | A relation between an observation of a contaminant and a feature it is the su...<br/>| 1282898 |
| [coso_hasMember](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/coso_hasMember.md) | <br/>| 13 |
| [coso_hasResult](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/coso_hasResult.md) | A relation between an observation of a contaminant and the measurement that i...<br/>| 1282200 |
| [coso_hasResultQualifier](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/coso_hasResultQualifier.md) | A relation between measured result and metadata that qualifies the result<br/>| 170567 |
| [coso_isSampleOf](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/coso_isSampleOf.md) | A relation between a physcial material sample and the geographic feature the ...<br/>| 23037 |
| [coso_measurementUnit](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/coso_measurementUnit.md) | The unit of measurement the describes the result<br/>| 285114 |
| [coso_measurementValue](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/coso_measurementValue.md) | The numeric value or enumerated value that quantifies or qualifies the result<br/>| 1156116 |
| [coso_observationAnnotation](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/coso_observationAnnotation.md) | A relation between an observation of a contaminant and additional metadata ab...<br/>| 1153526 |
| [coso_observedAtPoint](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/coso_observedAtPoint.md) | A relation between an observation of a contaminant and the point that the obs...<br/>| 1154228 |
| [coso_observedAtReleasePoint](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/coso_observedAtReleasePoint.md) | A relation between an observation of a contaminant that was released and the ...<br/>|  |
| [coso_observedAtSamplePoint](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/coso_observedAtSamplePoint.md) | A relation between an observation of a contaminant from a material sample and...<br/>| 1282902 |
| [coso_observedProperty](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/coso_observedProperty.md) | A relation between an observation and the type of contamination property bein...<br/>| 705437 |
| [coso_observedTime](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/coso_observedTime.md) | The time at which the contaminant was observed in the environment<br/>| 1282272 |
| [coso_ofComptoxSubstance](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/coso_ofComptoxSubstance.md) | A relation between an entity and a chemical substance as identified by Compto...<br/>|  |
| [coso_ofDatasetSubstance](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/coso_ofDatasetSubstance.md) | A relation between an entity and a chemical substance as identified in a data...<br/>| 705437 |
| [coso_ofFeatureType](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/coso_ofFeatureType.md) | A relation between a feature and a controlled vocabulary term that describes ...<br/>| 8021 |
| [coso_ofSubstance](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/coso_ofSubstance.md) | A relation between an observation of a contaminant and the substance or subst...<br/>| 1153526 |
| [coso_pointFromFeature](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/coso_pointFromFeature.md) | A relation between a point location and the larger geospatial feature it is a...<br/>| 16468 |
| [coso_releaseFeature](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/coso_releaseFeature.md) | A relation between an observation of a contaminant that was released and the ...<br/>|  |
| [coso_resultAnnotation](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/coso_resultAnnotation.md) | A relation between a result and additional metadata about the result<br/>| 4651480 |
| [coso_sampleAnnotation](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/coso_sampleAnnotation.md) | A relation between a material sample and additional metadata about the sample<br/>| 107712 |
| [coso_sampledFeature](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/coso_sampledFeature.md) | A relation between an observation of a contaminant from a sample and the feat...<br/>|  |
| [coso_sampleOfMaterialType](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/coso_sampleOfMaterialType.md) | A relation between a material sample and the type of material<br/>| 56478 |
| [coso_substanceID](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/coso_substanceID.md) | The unique identifier for the substance<br/>| 194 |
| [coso_usedAnalysisMethod](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/coso_usedAnalysisMethod.md) | A relation between an observation of a contaminant and the analysis method th...<br/>|  |
| [http___sawgraph.spatialai.org_v1_sdwis#pwsidNumber](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/http___sawgraph.spatialai.org_v1_sdwis#pwsidNumber.md) | Uniquely identifies the water system within a specific state<br/>|  |
| [http___w3id.org_comptox_sameAsComptoxSubstance](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/http___w3id.org_comptox_sameAsComptoxSubstance.md) | A relation between an dataset specific substance and the same substance as id...<br/>| 55 |
| [http___w3id.org_comptox_v1_sameAsComptoxSubstance](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/http___w3id.org_comptox_v1_sameAsComptoxSubstance.md) | A relation between an dataset specific substance and the same substance as id...<br/>| 125 |
| [http___w3id.org_sawgraph_v1_me_egad#associatedSite](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/http___w3id.org_sawgraph_v1_me_egad#associatedSite.md) | <br/>| 9572 |
| [http___w3id.org_sawgraph_v1_me_egad#dep_chemicalID](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/http___w3id.org_sawgraph_v1_me_egad#dep_chemicalID.md) | <br/>| 4 |
| [http___w3id.org_sawgraph_v1_me_egad#labQualifier](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/http___w3id.org_sawgraph_v1_me_egad#labQualifier.md) | <br/>| 489050 |
| [http___w3id.org_sawgraph_v1_me_egad#methodDetectionLimit](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/http___w3id.org_sawgraph_v1_me_egad#methodDetectionLimit.md) | <br/>| 577732 |
| [http___w3id.org_sawgraph_v1_me_egad#reportingLimit](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/http___w3id.org_sawgraph_v1_me_egad#reportingLimit.md) | <br/>| 579249 |
| [http___w3id.org_sawgraph_v1_me_egad#resultType](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/http___w3id.org_sawgraph_v1_me_egad#resultType.md) | <br/>| 576763 |
| [http___w3id.org_sawgraph_v1_me_egad#sampleCollectionLocation](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/http___w3id.org_sawgraph_v1_me_egad#sampleCollectionLocation.md) | <br/>| 15556 |
| [http___w3id.org_sawgraph_v1_me_egad#sampleCollectionMethod](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/http___w3id.org_sawgraph_v1_me_egad#sampleCollectionMethod.md) | <br/>| 22690 |
| [http___w3id.org_sawgraph_v1_me_egad#sampledFeatureType](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/http___w3id.org_sawgraph_v1_me_egad#sampledFeatureType.md) | <br/>| 8021 |
| [http___w3id.org_sawgraph_v1_me_egad#sampleID](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/http___w3id.org_sawgraph_v1_me_egad#sampleID.md) | Sample identifier in the EGAD dataset from the state of Maine<br/>|  |
| [http___w3id.org_sawgraph_v1_me_egad#samplePointNumber](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/http___w3id.org_sawgraph_v1_me_egad#samplePointNumber.md) | Sample point number in the EGAD dataset from the state of Maine<br/>| 8324 |
| [http___w3id.org_sawgraph_v1_me_egad#samplePointType](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/http___w3id.org_sawgraph_v1_me_egad#samplePointType.md) | <br/>| 16345 |
| [http___w3id.org_sawgraph_v1_me_egad#samplePointWebName](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/http___w3id.org_sawgraph_v1_me_egad#samplePointWebName.md) | Sample point web name in the EGAD dataset from the state of Maine<br/>| 8324 |
| [http___w3id.org_sawgraph_v1_me_egad#sampleTreatmentStatus](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/http___w3id.org_sawgraph_v1_me_egad#sampleTreatmentStatus.md) | <br/>| 15610 |
| [http___w3id.org_sawgraph_v1_me_egad#siteNumber](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/http___w3id.org_sawgraph_v1_me_egad#siteNumber.md) | Site number in the EGAD dataset from the state of Maine<br/>| 1027 |
| [http___w3id.org_sawgraph_v1_me_egad#siteType](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/http___w3id.org_sawgraph_v1_me_egad#siteType.md) | <br/>| 1409 |
| [http___w3id.org_sawgraph_v1_me_egad#validationLevel](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/http___w3id.org_sawgraph_v1_me_egad#validationLevel.md) | <br/>| 567749 |
| [http___w3id.org_sawgraph_v1_me_egad#validationQualifier](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/http___w3id.org_sawgraph_v1_me_egad#validationQualifier.md) | <br/>| 505846 |
| [http___w3id.org_sawgraph_v1_sdwis#pwsidNumber](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/http___w3id.org_sawgraph_v1_sdwis#pwsidNumber.md) | Uniquely identifies the water system within a specific state<br/>|  |
| [http___w3id.org_sawgraph_v1_us_wqp#groupName](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/http___w3id.org_sawgraph_v1_us_wqp#groupName.md) | <br/>| 50 |
| [http___w3id.org_sawgraph_v1_us_wqp#hasProjectId](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/http___w3id.org_sawgraph_v1_us_wqp#hasProjectId.md) | <br/>| 5109 |
| [http___w3id.org_sawgraph_v1_us_wqp#locationType](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/http___w3id.org_sawgraph_v1_us_wqp#locationType.md) | <br/>| 388 |
| [http___w3id.org_sawgraph_v1_us_wqp#organizationDescription](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/http___w3id.org_sawgraph_v1_us_wqp#organizationDescription.md) | <br/>| 8 |
| [http___w3id.org_sawgraph_v1_us_wqp#organizationId](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/http___w3id.org_sawgraph_v1_us_wqp#organizationId.md) | <br/>| 11 |
| [http___w3id.org_sawgraph_v1_us_wqp#rank](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/http___w3id.org_sawgraph_v1_us_wqp#rank.md) | <br/>| 67 |
| [http___w3id.org_sawgraph_v1_us_wqp#sampleCollectionMethod](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/http___w3id.org_sawgraph_v1_us_wqp#sampleCollectionMethod.md) | <br/>| 5001 |
| [http___w3id.org_sawgraph_v1_us_wqp#sampleID](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/http___w3id.org_sawgraph_v1_us_wqp#sampleID.md) | <br/>| 5109 |
| [http___w3id.org_sawgraph_v1_us_wqp#siteId](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/http___w3id.org_sawgraph_v1_us_wqp#siteId.md) | <br/>| 388 |
| [http___w3id.org_sawgraph_v1_us_wqp#siteName](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/http___w3id.org_sawgraph_v1_us_wqp#siteName.md) | <br/>| 388 |
| [http___w3id.org_sawgraph_v1_us_wqp#srsID](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/http___w3id.org_sawgraph_v1_us_wqp#srsID.md) | <br/>| 47 |
| [http___www.geneontology.org_formats_oboInOwl#created_by](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/http___www.geneontology.org_formats_oboInOwl#created_by.md) | <br/>|  |
| [http___www.geneontology.org_formats_oboInOwl#creation_date](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/http___www.geneontology.org_formats_oboInOwl#creation_date.md) | <br/>|  |
| [http___www.geneontology.org_formats_oboInOwl#hasAlternativeId](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/http___www.geneontology.org_formats_oboInOwl#hasAlternativeId.md) | <br/>|  |
| [http___www.geneontology.org_formats_oboInOwl#hasBroadSynonym](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/http___www.geneontology.org_formats_oboInOwl#hasBroadSynonym.md) | <br/>|  |
| [http___www.geneontology.org_formats_oboInOwl#hasDbXref](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/http___www.geneontology.org_formats_oboInOwl#hasDbXref.md) | <br/>| 2 |
| [http___www.geneontology.org_formats_oboInOwl#hasExactSynonym](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/http___www.geneontology.org_formats_oboInOwl#hasExactSynonym.md) | <br/>|  |
| [http___www.geneontology.org_formats_oboInOwl#hasNarrowSynonym](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/http___www.geneontology.org_formats_oboInOwl#hasNarrowSynonym.md) | <br/>|  |
| [http___www.geneontology.org_formats_oboInOwl#hasOBONamespace](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/http___www.geneontology.org_formats_oboInOwl#hasOBONamespace.md) | <br/>|  |
| [http___www.geneontology.org_formats_oboInOwl#hasRelatedSynonym](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/http___www.geneontology.org_formats_oboInOwl#hasRelatedSynonym.md) | <br/>|  |
| [http___www.geneontology.org_formats_oboInOwl#hasSynonym](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/http___www.geneontology.org_formats_oboInOwl#hasSynonym.md) | <br/>|  |
| [http___www.geneontology.org_formats_oboInOwl#id](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/http___www.geneontology.org_formats_oboInOwl#id.md) | <br/>|  |
| [http___www.geneontology.org_formats_oboInOwl#inSubset](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/http___www.geneontology.org_formats_oboInOwl#inSubset.md) | <br/>|  |
| [kwgo_administrativePartOf](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/kwgo_administrativePartOf.md) | <br/>|  |
| [me_egad_associatedSite](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/me_egad_associatedSite.md) | <br/>| 9572 |
| [me_egad_dep_chemicalID](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/me_egad_dep_chemicalID.md) | <br/>| 4 |
| [me_egad_labQualifier](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/me_egad_labQualifier.md) | <br/>| 489050 |
| [me_egad_methodDetectionLimit](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/me_egad_methodDetectionLimit.md) | <br/>| 577732 |
| [me_egad_reportingLimit](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/me_egad_reportingLimit.md) | <br/>| 579249 |
| [me_egad_resultType](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/me_egad_resultType.md) | <br/>| 576763 |
| [me_egad_sampleCollectionLocation](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/me_egad_sampleCollectionLocation.md) | <br/>| 15556 |
| [me_egad_sampleCollectionMethod](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/me_egad_sampleCollectionMethod.md) | <br/>| 22690 |
| [me_egad_sampledFeatureType](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/me_egad_sampledFeatureType.md) | <br/>| 8021 |
| [me_egad_sampleID](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/me_egad_sampleID.md) | Sample identifier in the EGAD dataset from the state of Maine<br/>|  |
| [me_egad_samplePointNumber](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/me_egad_samplePointNumber.md) | Sample point number in the EGAD dataset from the state of Maine<br/>|  |
| [me_egad_samplePointType](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/me_egad_samplePointType.md) | <br/>| 16345 |
| [me_egad_samplePointWebName](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/me_egad_samplePointWebName.md) | Sample point web name in the EGAD dataset from the state of Maine<br/>|  |
| [me_egad_sampleTreatmentStatus](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/me_egad_sampleTreatmentStatus.md) | <br/>| 15610 |
| [me_egad_siteNumber](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/me_egad_siteNumber.md) | Site number in the EGAD dataset from the state of Maine<br/>| 1027 |
| [me_egad_siteType](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/me_egad_siteType.md) | <br/>| 1382 |
| [me_egad_validationLevel](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/me_egad_validationLevel.md) | <br/>| 567749 |
| [me_egad_validationQualifier](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/me_egad_validationQualifier.md) | <br/>| 505846 |
| [obo_BFO_0000050](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/obo_BFO_0000050.md) | <br/>|  |
| [obo_BFO_0000051](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/obo_BFO_0000051.md) | <br/>|  |
| [obo_IAO_0000111](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/obo_IAO_0000111.md) | <br/>|  |
| [obo_IAO_0000112](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/obo_IAO_0000112.md) | <br/>|  |
| [obo_IAO_0000114](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/obo_IAO_0000114.md) | <br/>|  |
| [obo_IAO_0000115](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/obo_IAO_0000115.md) | <br/>|  |
| [obo_IAO_0000116](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/obo_IAO_0000116.md) | <br/>|  |
| [obo_IAO_0000117](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/obo_IAO_0000117.md) | <br/>|  |
| [obo_IAO_0000118](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/obo_IAO_0000118.md) | <br/>|  |
| [obo_IAO_0000119](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/obo_IAO_0000119.md) | <br/>|  |
| [obo_IAO_0000412](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/obo_IAO_0000412.md) | <br/>| 2 |
| [obo_IAO_0000600](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/obo_IAO_0000600.md) | <br/>|  |
| [obo_RO_0001000](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/obo_RO_0001000.md) | <br/>|  |
| [obo_RO_0001900](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/obo_RO_0001900.md) | <br/>|  |
| [obo_RO_0002131](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/obo_RO_0002131.md) | <br/>|  |
| [obo_RO_0002160](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/obo_RO_0002160.md) | <br/>|  |
| [obo_RO_0002162](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/obo_RO_0002162.md) | Connects a biological entity to its taxon of origin<br/>| 2 |
| [obo_RO_0003001](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/obo_RO_0003001.md) | <br/>|  |
| [owl_ObjectPropertyChain](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/owl_ObjectPropertyChain.md) | <br/>|  |
| [owl_someValueFrom](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/owl_someValueFrom.md) | <br/>|  |
| [qudt_quantityKind](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/qudt_quantityKind.md) | <br/>|  |
| [qudt_wikidataMatch](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/qudt_wikidataMatch.md) | <br/>| 1 |
| [skos_description](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/skos_description.md) | <br/>|  |
| [sosa_isSampleOf](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/sosa_isSampleOf.md) | <br/>| 23037 |
| [sosa_usedProcedure](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/sosa_usedProcedure.md) | <br/>|  |
| [spatial_connectedTo](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/spatial_connectedTo.md) | <br/>| 43360 |
| [spatial_spatiallyRelatedTo](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/spatial_spatiallyRelatedTo.md) | <br/>| 43360 |
| [stad_hasQualityKind](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/stad_hasQualityKind.md) | <br/>| 576776 |
| [stad_hasTransformationKind](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/stad_hasTransformationKind.md) | <br/>|  |
| [us_sdwis_hasPWSID](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/slots/us_sdwis_hasPWSID.md) | <br/>| 183 |






## Types

| Type | Description |
| --- | --- |
| [XsdAnyURI](https://github.com/frink-okn/graph-descriptions/blob/main/sawgraph-kg/types/XsdAnyURI.md) |  |





## IRI prefixes

* coso: http://w3id.org/coso/v1/contaminoso#
* dc: http://purl.org/dc/elements/1.1/
* dcgeoid: https://datacommons.org/browser/geoId/
* dct: http://purl.org/dc/terms/
* geo: http://www.opengis.net/ont/geosparql#
* kwgo: http://stko-kwg.geog.ucsb.edu/lod/ontology/
* kwgr: http://stko-kwg.geog.ucsb.edu/lod/resource/
* linkml: https://w3id.org/linkml/
* me_egad: http://sawgraph.spatialai.org/v1/me-egad#
* me_egad_data: http://sawgraph.spatialai.org/v1/me-egad-data#
* obo: http://purl.obolibrary.org/obo/
* okn: https://purl.org/okn/
* okns: https://purl.org/okn/schema/
* owl: http://www.w3.org/2002/07/owl#
* prov: http://www.w3.org/ns/prov#
* qudt: http://qudt.org/schema/qudt/
* rdf: http://www.w3.org/1999/02/22-rdf-syntax-ns#
* rdfs: http://www.w3.org/2000/01/rdf-schema#
* sdos: https://schema.org/
* sf: http://www.opengis.net/ont/sf#
* skos: http://www.w3.org/2004/02/skos/core#
* sosa: http://www.w3.org/ns/sosa/
* spatial: http://purl.org/spatialai/spatial/spatial-full#
* stad: http://purl.org/spatialai/stad/v2/core/
* time: http://www.w3.org/2006/time#
* us_sdwis: http://sawgraph.spatialai.org/v1/us-sdwis#
* vaem: http://www.linkedmodel.org/schema/vaem#
* vann: http://purl.org/vocab/vann/
* wd: http://www.wikidata.org/entity/
* xsd: http://www.w3.org/2001/XMLSchema#
