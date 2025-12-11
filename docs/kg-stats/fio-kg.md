# fiokg

This ontology supports querying the SAWGraph Knowledge Graph and the KnowWhereGraph. It is an adaptation of the spatial ontology originally published by the KnowWhereGraph Project



## Schema Diagram

```mermaid
erDiagram
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
Bd7175f49ca206d160fdb4fee4dad2747 {
    string dct_description  
    string rdfs_label  
}
Bf500d8a8b0381e9decef451f20ba1677 {
    string dct_description  
    string rdfs_label  
}
Fio-epa-frsAgency {
    string rdfs_label  
}
Fio-epa-frsAgency.Agriculture {
    string rdfs_label  
}
Fio-epa-frsAgency.Commerce {
    string rdfs_label  
}
Fio-epa-frsAgency.Congress {
    string rdfs_label  
}
Fio-epa-frsAgency.Defense {
    string rdfs_label  
}
Fio-epa-frsAgency.Energy {
    string rdfs_label  
}
Fio-epa-frsAgency.HealthandHumanServices {
    string rdfs_label  
}
Fio-epa-frsAgency.HomelandSecurity {
    string rdfs_label  
}
Fio-epa-frsAgency.HousingandUrbanDevelopment {
    string rdfs_label  
}
Fio-epa-frsAgency.Interior {
    string rdfs_label  
}
Fio-epa-frsAgency.Judicial {
    string rdfs_label  
}
Fio-epa-frsAgency.Justice {
    string rdfs_label  
}
Fio-epa-frsAgency.Labor {
    string rdfs_label  
}
Fio-epa-frsAgency.State {
    string rdfs_label  
}
Fio-epa-frsAgency.Transportation {
    string rdfs_label  
}
Fio-epa-frsAgency.Treasury {
    string rdfs_label  
}
Fio-epa-frsAgency.VeteransAffairs {
    string rdfs_label  
}
Fio-epa-frsAirProgram {
    string dct_description  
    string rdfs_label  
}
Fio-epa-frsAnimalOperation {
    string dct_description  
    string rdfs_label  
}
Fio-epa-frsAssistanceSupportProgram {
    string dct_description  
    string rdfs_label  
}
Fio-epa-frsChemicalReleaseProgram {
    string dct_description  
    string rdfs_label  
}
Fio-epa-frsChemicalStorageProgram {
    string dct_description  
    string rdfs_label  
}
Fio-epa-frsChemicalstorageprograms {

}
Fio-epa-frsCoastalOceanProgram {
    string dct_description  
    string rdfs_label  
}
Fio-epa-frsComplianceInterest {
    string dct_description  
    string rdfs_label  
}
Fio-epa-frsComplianceRecord {
    uri fio_epa_frs_fromSystem  
    uri fio_epa_frs_ofInterestType  
    string rdfs_label  
}
Fio-epa-frsComplianceSystem {
    string dct_description  
    string rdfs_label  
}
Fio-epa-frsDrinkingWaterProgram {
    string dct_description  
    string rdfs_label  
}
Fio-epa-frsEPA-PFAS-Facility {
    date dct_modified  
    string fio_epa_frs_hasFRSId  
    uri fio_epa_frs_hasRecord  
    string rdfs_label  
}
Fio-epa-frsEcologyOperation {
    string dct_description  
    string rdfs_label  
}
Fio-epa-frsElectronicPermitSystem {
    string dct_description  
    string rdfs_label  
}
Fio-epa-frsEnforcementActivity {
    uri fio_epa_frs_hasSupplementalRecord  
    uri fio_epa_frs_fromSystem  
    uri fio_epa_frs_ofInterestType  
    datetime prov_startedAtTime  
    string dct_description  
    uri fio_epa_frs_hasRecord  
    string rdfs_label  
}
Fio-epa-frsEnforcementInterest {
    string dct_description  
    string rdfs_label  
}
Fio-epa-frsEnforcementSystem {
    string dct_description  
    string rdfs_label  
}
Fio-epa-frsEnforcementTrackingRecord {
    uri fio_epa_frs_hasSupplementalRecord  
    uri fio_epa_frs_fromSystem  
    datetime prov_endedAtTime  
    uri fio_epa_frs_ofInterestType  
    datetime prov_startedAtTime  
    string dct_description  
    uri fio_epa_frs_hasRecord  
    string rdfs_label  
}
Fio-epa-frsEnvironmentalInterestByProgram {
    string dct_description  
    string rdfs_label  
}
Fio-epa-frsEnvironmentalInterestByRecordType {

}
Fio-epa-frsEnvironmentalInterestType {
    string rdfs_label  
}
Fio-epa-frsFRS-Facility {
    uri fio_epa_frs_fromSystem  
    uri fio_epa_frs_ofInterestType  
    string rdfs_label  
    datetime prov_startedAtTime  
    uri fio_epa_frs_hasSupplementalRecord  
    string fio_epa_frs_hasFRSId  
    string dct_description  
    uri fio_epa_frs_hasRecord  
    date dct_modified  
    datetime prov_endedAtTime  
}
Fio-epa-frsFacilitySiteIdentification {
    string dct_description  
    string rdfs_label  
}
Fio-epa-frsFacilityType {
    string rdfs_label  
}
Fio-epa-frsGrantSystem {
    string dct_description  
    string rdfs_label  
}
Fio-epa-frsGroundWaterProgram {
    string dct_description  
    string rdfs_label  
}
Fio-epa-frsHazardousWasteProgram {
    string dct_description  
    string rdfs_label  
}
Fio-epa-frsHealthSafetyProgram {
    string dct_description  
    string rdfs_label  
}
Fio-epa-frsLegacySystem {
    string dct_description  
    string rdfs_label  
}
Fio-epa-frsLegalEnforcementActivities {
    string dct_description  
    string rdfs_label  
}
Fio-epa-frsMonitoringRecord {

}
Fio-epa-frsPermitInterest {
    string dct_description  
    string rdfs_label  
}
Fio-epa-frsPermitRecord {
    uri fio_epa_frs_hasSupplementalRecord  
    uri fio_epa_frs_fromSystem  
    datetime prov_endedAtTime  
    uri fio_epa_frs_ofInterestType  
    datetime prov_startedAtTime  
    string dct_description  
    uri fio_epa_frs_hasRecord  
    string rdfs_label  
}
Fio-epa-frsPermitSystem {
    string dct_description  
    string rdfs_label  
}
Fio-epa-frsPesticidesProgram {
    string dct_description  
    string rdfs_label  
}
Fio-epa-frsProgramInformationSystem {
    string dct_description  
    string rdfs_label  
}
Fio-epa-frsProjectRecord {
    uri fio_epa_frs_fromSystem  
    datetime prov_endedAtTime  
    uri fio_epa_frs_ofInterestType  
    datetime prov_startedAtTime  
    string dct_description  
    string rdfs_label  
}
Fio-epa-frsProjectSystem {
    string dct_description  
    string rdfs_label  
}
Fio-epa-frsRadiationProtectionProgram {
    string dct_description  
    string rdfs_label  
}
Fio-epa-frsRecord {
    uri fio_epa_frs_hasSupplementalRecord  
    uri fio_epa_frs_fromSystem  
    uri fio_epa_frs_ofInterestType  
    uri fio_epa_frs_hasRecord  
    string rdfs_label  
}
Fio-epa-frsRegistrationRecord {
    uri fio_epa_frs_hasSupplementalRecord  
    uri fio_epa_frs_fromSystem  
    uri fio_epa_frs_ofInterestType  
    datetime prov_startedAtTime  
    string dct_description  
    uri fio_epa_frs_hasRecord  
    string rdfs_label  
}
Fio-epa-frsRegistryInterest {
    string dct_description  
    string rdfs_label  
}
Fio-epa-frsRegistrySystem {
    string dct_description  
    string rdfs_label  
}
Fio-epa-frsRemediationRedevelopmentProgram {
    string dct_description  
    string rdfs_label  
}
Fio-epa-frsReportingInterest {
    string dct_description  
    string rdfs_label  
}
Fio-epa-frsReportingRecord {
    uri fio_epa_frs_hasSupplementalRecord  
    uri fio_epa_frs_fromSystem  
    datetime prov_endedAtTime  
    uri fio_epa_frs_ofInterestType  
    datetime prov_startedAtTime  
    string dct_description  
    uri fio_epa_frs_hasRecord  
    string rdfs_label  
}
Fio-epa-frsReportingSystem {
    string dct_description  
    string rdfs_label  
}
Fio-epa-frsRiskInterest {
    string dct_description  
    string rdfs_label  
}
Fio-epa-frsRiskPlanRecord {
    uri fio_epa_frs_hasSupplementalRecord  
    uri fio_epa_frs_fromSystem  
    uri fio_epa_frs_ofInterestType  
    datetime prov_startedAtTime  
    string dct_description  
    uri fio_epa_frs_hasRecord  
    string rdfs_label  
}
Fio-epa-frsSiteInterest {
    string dct_description  
    string rdfs_label  
}
Fio-epa-frsSiteRecord {
    uri fio_epa_frs_hasSupplementalRecord  
    uri fio_epa_frs_fromSystem  
    datetime prov_endedAtTime  
    uri fio_epa_frs_ofInterestType  
    datetime prov_startedAtTime  
    string dct_description  
    uri fio_epa_frs_hasRecord  
    string rdfs_label  
}
Fio-epa-frsSiteSystem {
    string dct_description  
    string rdfs_label  
}
Fio-epa-frsSolidWasteProgram {
    string dct_description  
    string rdfs_label  
}
Fio-epa-frsStateSystem {
    string dct_description  
    string rdfs_label  
}
Fio-epa-frsStateTrackingRecord {
    uri fio_epa_frs_hasSupplementalRecord  
    uri fio_epa_frs_fromSystem  
    uri fio_epa_frs_ofInterestType  
    datetime prov_startedAtTime  
    string dct_description  
    uri fio_epa_frs_hasRecord  
    string rdfs_label  
}
Fio-epa-frsStationSystem {

}
Fio-epa-frsSupplementalRecord {
    uri fio_epa_frs_hasSupplementalRecord  
    uri fio_epa_frs_fromSystem  
    datetime prov_endedAtTime  
    uri fio_epa_frs_ofInterestType  
    datetime prov_startedAtTime  
    string dct_description  
    uri fio_epa_frs_hasRecord  
    string rdfs_label  
}
Fio-epa-frsTribalSystem {
    string dct_description  
    string rdfs_label  
}
Fio-epa-frsTribalTrackingRecord {
    uri fio_epa_frs_fromSystem  
    uri fio_epa_frs_ofInterestType  
    datetime prov_startedAtTime  
    string dct_description  
    string rdfs_label  
}
Fio-epa-frsUndergroundStorageTankProgram {
    string dct_description  
    string rdfs_label  
}
Fio-epa-frsWasteWaterProgram {
    string dct_description  
    string rdfs_label  
}
Fio-epa-frsWaterResourcesProgram {
    string dct_description  
    string rdfs_label  
}
FioFacility {

}
FioIndustry {

}
FioOrganization {

}
KwgoS2CellLevel13 {

}
KwgoStatisticalArea {

}
NaicsNAICS-Industry {

}
NaicsNAICS-IndustryCode {
    date fio_ofYear  
    string rdfs_label  
}
NaicsNAICS-IndustryGroup {
    date fio_ofYear  
    string rdfs_label  
}
NaicsNAICS-IndustrySector {
    date fio_ofYear  
    string rdfs_label  
}
NaicsNAICS-IndustrySubsector {
    date fio_ofYear  
    string rdfs_label  
}

TimeDayOfWeek ||--|o RdfsLiteral : "rdfs_label"
TimeTemporalUnit ||--|o RdfsLiteral : "rdfs_label"
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
Bd7175f49ca206d160fdb4fee4dad2747 ||--|o RdfsLiteral : "rdfs_label"
Bd7175f49ca206d160fdb4fee4dad2747 ||--|o OwlThing : "owl_sameAs"
Bf500d8a8b0381e9decef451f20ba1677 ||--|o RdfsLiteral : "rdfs_label"
Bf500d8a8b0381e9decef451f20ba1677 ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsAgency ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsAgency ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsAgency.Agriculture ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsAgency.Agriculture ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsAgency.Commerce ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsAgency.Commerce ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsAgency.Congress ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsAgency.Congress ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsAgency.Defense ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsAgency.Defense ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsAgency.Energy ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsAgency.Energy ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsAgency.HealthandHumanServices ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsAgency.HealthandHumanServices ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsAgency.HomelandSecurity ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsAgency.HomelandSecurity ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsAgency.HousingandUrbanDevelopment ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsAgency.HousingandUrbanDevelopment ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsAgency.Interior ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsAgency.Interior ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsAgency.Judicial ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsAgency.Judicial ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsAgency.Justice ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsAgency.Justice ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsAgency.Labor ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsAgency.Labor ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsAgency.State ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsAgency.State ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsAgency.Transportation ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsAgency.Transportation ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsAgency.Treasury ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsAgency.Treasury ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsAgency.VeteransAffairs ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsAgency.VeteransAffairs ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsAirProgram ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsAirProgram ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsAnimalOperation ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsAnimalOperation ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsAssistanceSupportProgram ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsAssistanceSupportProgram ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsChemicalReleaseProgram ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsChemicalReleaseProgram ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsChemicalStorageProgram ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsChemicalStorageProgram ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsCoastalOceanProgram ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsCoastalOceanProgram ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsComplianceInterest ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsComplianceInterest ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsComplianceRecord ||--|o RdfsLiteral : "dct_identifier"
Fio-epa-frsComplianceRecord ||--|o Fio-epa-frsLegacySystem : "fio-epa-frs_fromSystem"
Fio-epa-frsComplianceRecord ||--|o Fio-epa-frsPermitSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsComplianceRecord ||--|o Fio-epa-frsStateSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsComplianceRecord ||--|o Fio-epa-frsProjectSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsComplianceRecord ||--|o Fio-epa-frsComplianceSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsComplianceRecord ||--|o Fio-epa-frsSiteSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsComplianceRecord ||--|o RdfsResource : "fio-epa-frs_fromSystem"
Fio-epa-frsComplianceRecord ||--|o Fio-epa-frsRegistrySystem : "fio-epa-frs_fromSystem"
Fio-epa-frsComplianceRecord ||--|o Fio-epa-frsEnforcementSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsComplianceRecord ||--|o Fio-epa-frsGrantSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsComplianceRecord ||--|o Fio-epa-frsReportingSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsComplianceRecord ||--|o Fio-epa-frsProgramInformationSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsComplianceRecord ||--|o Fio-epa-frsTribalSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsComplianceRecord ||--|o OwlThing : "fio-epa-frs_fromSystem"
Fio-epa-frsComplianceRecord ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsComplianceRecord ||--|o NaicsNAICS-IndustryGroup : "fio_ofIndustry"
Fio-epa-frsComplianceRecord ||--|o RdfsResource : "fio_ofIndustry"
Fio-epa-frsComplianceRecord ||--|o NaicsNAICS-IndustrySector : "fio_ofIndustry"
Fio-epa-frsComplianceRecord ||--|o OwlNamedIndividual : "fio_ofIndustry"
Fio-epa-frsComplianceRecord ||--|o NaicsNAICS-IndustryCode : "fio_ofIndustry"
Fio-epa-frsComplianceRecord ||--|o OwlThing : "fio_ofIndustry"
Fio-epa-frsComplianceRecord ||--|o FioIndustry : "fio_ofIndustry"
Fio-epa-frsComplianceRecord ||--|o NaicsNAICS-IndustrySubsector : "fio_ofIndustry"
Fio-epa-frsComplianceRecord ||--|o Bd7175f49ca206d160fdb4fee4dad2747 : "fio-epa-frs_ofInterestType"
Fio-epa-frsComplianceRecord ||--|o Fio-epa-frsRadiationProtectionProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsComplianceRecord ||--|o Fio-epa-frsEnforcementInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsComplianceRecord ||--|o Fio-epa-frsGroundWaterProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsComplianceRecord ||--|o Fio-epa-frsAssistanceSupportProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsComplianceRecord ||--|o Fio-epa-frsCoastalOceanProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsComplianceRecord ||--|o Fio-epa-frsHazardousWasteProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsComplianceRecord ||--|o Bf500d8a8b0381e9decef451f20ba1677 : "fio-epa-frs_ofInterestType"
Fio-epa-frsComplianceRecord ||--|o Fio-epa-frsReportingInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsComplianceRecord ||--|o Fio-epa-frsAnimalOperation : "fio-epa-frs_ofInterestType"
Fio-epa-frsComplianceRecord ||--|o Fio-epa-frsSolidWasteProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsComplianceRecord ||--|o Fio-epa-frsComplianceInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsComplianceRecord ||--|o Fio-epa-frsHealthSafetyProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsComplianceRecord ||--|o Fio-epa-frsSiteInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsComplianceRecord ||--|o Fio-epa-frsRemediationRedevelopmentProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsComplianceRecord ||--|o Fio-epa-frsUndergroundStorageTankProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsComplianceRecord ||--|o Fio-epa-frsDrinkingWaterProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsComplianceRecord ||--|o Fio-epa-frsRegistryInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsComplianceRecord ||--|o OwlThing : "fio-epa-frs_ofInterestType"
Fio-epa-frsComplianceRecord ||--|o Fio-epa-frsWaterResourcesProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsComplianceRecord ||--|o Fio-epa-frsChemicalReleaseProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsComplianceRecord ||--|o Fio-epa-frsPermitInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsComplianceRecord ||--|o RdfsResource : "fio-epa-frs_ofInterestType"
Fio-epa-frsComplianceRecord ||--|o Fio-epa-frsAirProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsComplianceRecord ||--|o Fio-epa-frsWasteWaterProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsComplianceRecord ||--|o Fio-epa-frsPesticidesProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsComplianceRecord ||--|o Fio-epa-frsRiskInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsComplianceRecord ||--|o Fio-epa-frsEnvironmentalInterestByProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsComplianceRecord ||--|o Fio-epa-frsLegalEnforcementActivities : "fio-epa-frs_ofInterestType"
Fio-epa-frsComplianceRecord ||--|o Fio-epa-frsElectronicPermitSystem : "fio-epa-frs_ofInterestType"
Fio-epa-frsComplianceRecord ||--|o Fio-epa-frsEnvironmentalInterestType : "fio-epa-frs_ofInterestType"
Fio-epa-frsComplianceRecord ||--|o Fio-epa-frsFacilitySiteIdentification : "fio-epa-frs_ofInterestType"
Fio-epa-frsComplianceRecord ||--|o Fio-epa-frsChemicalStorageProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsComplianceRecord ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsComplianceRecord ||--|o NaicsNAICS-IndustryGroup : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsComplianceRecord ||--|o RdfsResource : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsComplianceRecord ||--|o NaicsNAICS-IndustrySector : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsComplianceRecord ||--|o OwlNamedIndividual : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsComplianceRecord ||--|o NaicsNAICS-IndustryCode : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsComplianceRecord ||--|o OwlThing : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsComplianceRecord ||--|o FioIndustry : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsComplianceRecord ||--|o NaicsNAICS-IndustrySubsector : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsComplianceSystem ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsComplianceSystem ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsDrinkingWaterProgram ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsDrinkingWaterProgram ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsEPA-PFAS-Facility ||--|o GeoGeometry : "geo_hasGeometry"
Fio-epa-frsEPA-PFAS-Facility ||--|o RdfsLiteral : "dct_identifier"
Fio-epa-frsEPA-PFAS-Facility ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsEPA-PFAS-Facility ||--|o RdfsLiteral : "dct_modified"
Fio-epa-frsEPA-PFAS-Facility ||--|o Bd7175f49ca206d160fdb4fee4dad2747 : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEPA-PFAS-Facility ||--|o Fio-epa-frsRadiationProtectionProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEPA-PFAS-Facility ||--|o Fio-epa-frsEnforcementInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEPA-PFAS-Facility ||--|o Fio-epa-frsGroundWaterProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEPA-PFAS-Facility ||--|o Fio-epa-frsAssistanceSupportProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEPA-PFAS-Facility ||--|o Fio-epa-frsCoastalOceanProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEPA-PFAS-Facility ||--|o Fio-epa-frsHazardousWasteProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEPA-PFAS-Facility ||--|o Bf500d8a8b0381e9decef451f20ba1677 : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEPA-PFAS-Facility ||--|o Fio-epa-frsReportingInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEPA-PFAS-Facility ||--|o Fio-epa-frsAnimalOperation : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEPA-PFAS-Facility ||--|o Fio-epa-frsSolidWasteProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEPA-PFAS-Facility ||--|o Fio-epa-frsHealthSafetyProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEPA-PFAS-Facility ||--|o Fio-epa-frsComplianceInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEPA-PFAS-Facility ||--|o Fio-epa-frsSiteInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEPA-PFAS-Facility ||--|o Fio-epa-frsRemediationRedevelopmentProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEPA-PFAS-Facility ||--|o Fio-epa-frsChemicalStorageProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEPA-PFAS-Facility ||--|o Fio-epa-frsUndergroundStorageTankProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEPA-PFAS-Facility ||--|o Fio-epa-frsDrinkingWaterProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEPA-PFAS-Facility ||--|o Fio-epa-frsRegistryInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEPA-PFAS-Facility ||--|o OwlThing : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEPA-PFAS-Facility ||--|o Fio-epa-frsWaterResourcesProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEPA-PFAS-Facility ||--|o Fio-epa-frsPermitInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEPA-PFAS-Facility ||--|o RdfsResource : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEPA-PFAS-Facility ||--|o Fio-epa-frsAirProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEPA-PFAS-Facility ||--|o Fio-epa-frsWasteWaterProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEPA-PFAS-Facility ||--|o Fio-epa-frsPesticidesProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEPA-PFAS-Facility ||--|o Fio-epa-frsRiskInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEPA-PFAS-Facility ||--|o Fio-epa-frsEnvironmentalInterestByProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEPA-PFAS-Facility ||--|o Fio-epa-frsLegalEnforcementActivities : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEPA-PFAS-Facility ||--|o Fio-epa-frsElectronicPermitSystem : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEPA-PFAS-Facility ||--|o Fio-epa-frsEnvironmentalInterestType : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEPA-PFAS-Facility ||--|o Fio-epa-frsFacilitySiteIdentification : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEPA-PFAS-Facility ||--|o Fio-epa-frsChemicalReleaseProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEPA-PFAS-Facility ||--|o NaicsNAICS-IndustryGroup : "fio_ofIndustry"
Fio-epa-frsEPA-PFAS-Facility ||--|o RdfsResource : "fio_ofIndustry"
Fio-epa-frsEPA-PFAS-Facility ||--|o NaicsNAICS-IndustrySector : "fio_ofIndustry"
Fio-epa-frsEPA-PFAS-Facility ||--|o OwlNamedIndividual : "fio_ofIndustry"
Fio-epa-frsEPA-PFAS-Facility ||--|o NaicsNAICS-IndustryCode : "fio_ofIndustry"
Fio-epa-frsEPA-PFAS-Facility ||--|o OwlThing : "fio_ofIndustry"
Fio-epa-frsEPA-PFAS-Facility ||--|o FioIndustry : "fio_ofIndustry"
Fio-epa-frsEPA-PFAS-Facility ||--|o NaicsNAICS-IndustrySubsector : "fio_ofIndustry"
Fio-epa-frsEPA-PFAS-Facility ||--|o Fio-epa-frsEPA-PFAS-Facility : "spatial_connectedTo"
Fio-epa-frsEPA-PFAS-Facility ||--|o KwgoAdministrativeRegion3 : "spatial_connectedTo"
Fio-epa-frsEPA-PFAS-Facility ||--|o KwgoRegion : "spatial_connectedTo"
Fio-epa-frsEPA-PFAS-Facility ||--|o RdfsResource : "spatial_connectedTo"
Fio-epa-frsEPA-PFAS-Facility ||--|o KwgoAdministrativeRegion : "spatial_connectedTo"
Fio-epa-frsEPA-PFAS-Facility ||--|o KwgoS2CellLevel13 : "spatial_connectedTo"
Fio-epa-frsEPA-PFAS-Facility ||--|o GeoSpatialObject : "spatial_connectedTo"
Fio-epa-frsEPA-PFAS-Facility ||--|o OwlThing : "spatial_connectedTo"
Fio-epa-frsEPA-PFAS-Facility ||--|o KwgoAdministrativeRegion2 : "spatial_connectedTo"
Fio-epa-frsEPA-PFAS-Facility ||--|o Fio-epa-frsFRS-Facility : "spatial_connectedTo"
Fio-epa-frsEPA-PFAS-Facility ||--|o Fio-epa-frsFacilityType : "fio-epa-frs_ofFacilityType"
Fio-epa-frsEPA-PFAS-Facility ||--|o RdfsResource : "fio-epa-frs_ofFacilityType"
Fio-epa-frsEPA-PFAS-Facility ||--|o OwlThing : "fio-epa-frs_ofFacilityType"
Fio-epa-frsEPA-PFAS-Facility ||--|o RdfsLiteral : "dct_created"
Fio-epa-frsEPA-PFAS-Facility ||--|o Fio-epa-frsEPA-PFAS-Facility : "spatial_spatiallyRelatedTo"
Fio-epa-frsEPA-PFAS-Facility ||--|o KwgoAdministrativeRegion3 : "spatial_spatiallyRelatedTo"
Fio-epa-frsEPA-PFAS-Facility ||--|o KwgoRegion : "spatial_spatiallyRelatedTo"
Fio-epa-frsEPA-PFAS-Facility ||--|o RdfsResource : "spatial_spatiallyRelatedTo"
Fio-epa-frsEPA-PFAS-Facility ||--|o KwgoAdministrativeRegion : "spatial_spatiallyRelatedTo"
Fio-epa-frsEPA-PFAS-Facility ||--|o KwgoS2CellLevel13 : "spatial_spatiallyRelatedTo"
Fio-epa-frsEPA-PFAS-Facility ||--|o GeoSpatialObject : "spatial_spatiallyRelatedTo"
Fio-epa-frsEPA-PFAS-Facility ||--|o OwlThing : "spatial_spatiallyRelatedTo"
Fio-epa-frsEPA-PFAS-Facility ||--|o KwgoAdministrativeRegion2 : "spatial_spatiallyRelatedTo"
Fio-epa-frsEPA-PFAS-Facility ||--|o Fio-epa-frsFRS-Facility : "spatial_spatiallyRelatedTo"
Fio-epa-frsEPA-PFAS-Facility ||--|o SdosPostalAddress : "sdos_address"
Fio-epa-frsEPA-PFAS-Facility ||--|o SdosText : "sdos_address"
Fio-epa-frsEPA-PFAS-Facility ||--|o Fio-epa-frsAgency.Interior : "fio_ownedBy"
Fio-epa-frsEPA-PFAS-Facility ||--|o Fio-epa-frsAgency.Transportation : "fio_ownedBy"
Fio-epa-frsEPA-PFAS-Facility ||--|o Fio-epa-frsAgency.Agriculture : "fio_ownedBy"
Fio-epa-frsEPA-PFAS-Facility ||--|o RdfsResource : "fio_ownedBy"
Fio-epa-frsEPA-PFAS-Facility ||--|o Fio-epa-frsAgency.HealthandHumanServices : "fio_ownedBy"
Fio-epa-frsEPA-PFAS-Facility ||--|o Fio-epa-frsAgency.HomelandSecurity : "fio_ownedBy"
Fio-epa-frsEPA-PFAS-Facility ||--|o Fio-epa-frsAgency.Defense : "fio_ownedBy"
Fio-epa-frsEPA-PFAS-Facility ||--|o Fio-epa-frsAgency.Justice : "fio_ownedBy"
Fio-epa-frsEPA-PFAS-Facility ||--|o OwlNamedIndividual : "fio_ownedBy"
Fio-epa-frsEPA-PFAS-Facility ||--|o Fio-epa-frsAgency : "fio_ownedBy"
Fio-epa-frsEPA-PFAS-Facility ||--|o Fio-epa-frsAgency.Commerce : "fio_ownedBy"
Fio-epa-frsEPA-PFAS-Facility ||--|o Fio-epa-frsAgency.Energy : "fio_ownedBy"
Fio-epa-frsEPA-PFAS-Facility ||--|o Fio-epa-frsAgency.VeteransAffairs : "fio_ownedBy"
Fio-epa-frsEPA-PFAS-Facility ||--|o Fio-epa-frsReportingRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsEPA-PFAS-Facility ||--|o Fio-epa-frsStateTrackingRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsEPA-PFAS-Facility ||--|o Fio-epa-frsTribalTrackingRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsEPA-PFAS-Facility ||--|o Fio-epa-frsRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsEPA-PFAS-Facility ||--|o RdfsResource : "fio-epa-frs_hasRecord"
Fio-epa-frsEPA-PFAS-Facility ||--|o Fio-epa-frsPermitRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsEPA-PFAS-Facility ||--|o Fio-epa-frsRegistrationRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsEPA-PFAS-Facility ||--|o Fio-epa-frsSiteRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsEPA-PFAS-Facility ||--|o Fio-epa-frsEnforcementActivity : "fio-epa-frs_hasRecord"
Fio-epa-frsEPA-PFAS-Facility ||--|o Fio-epa-frsProjectRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsEPA-PFAS-Facility ||--|o Fio-epa-frsComplianceRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsEPA-PFAS-Facility ||--|o Fio-epa-frsRiskPlanRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsEPA-PFAS-Facility ||--|o OwlThing : "fio-epa-frs_hasRecord"
Fio-epa-frsEPA-PFAS-Facility ||--|o Fio-epa-frsEnforcementTrackingRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsEPA-PFAS-Facility ||--|o Fio-epa-frsSupplementalRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsEPA-PFAS-Facility ||--|o Fio-epa-frsFRS-Facility : "fio-epa-frs_hasRecord"
Fio-epa-frsEPA-PFAS-Facility ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsEPA-PFAS-Facility ||--|o RdfsLiteral : "dct_alternative"
Fio-epa-frsEcologyOperation ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsEcologyOperation ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsElectronicPermitSystem ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsElectronicPermitSystem ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsReportingRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsStateTrackingRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsEnforcementActivity ||--|o RdfsResource : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsPermitRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsSiteRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsRegistrationRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsEnforcementActivity : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsRiskPlanRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsEnforcementActivity ||--|o OwlThing : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsEnforcementTrackingRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsSupplementalRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsFRS-Facility : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsEnforcementActivity ||--|o RdfsLiteral : "dct_identifier"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsLegacySystem : "fio-epa-frs_fromSystem"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsPermitSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsStateSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsProjectSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsComplianceSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsSiteSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsEnforcementActivity ||--|o RdfsResource : "fio-epa-frs_fromSystem"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsRegistrySystem : "fio-epa-frs_fromSystem"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsEnforcementSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsGrantSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsReportingSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsProgramInformationSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsTribalSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsEnforcementActivity ||--|o OwlThing : "fio-epa-frs_fromSystem"
Fio-epa-frsEnforcementActivity ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsEnforcementActivity ||--|o Bd7175f49ca206d160fdb4fee4dad2747 : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsRadiationProtectionProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsEnforcementInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsGroundWaterProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsAssistanceSupportProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsCoastalOceanProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsHazardousWasteProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementActivity ||--|o Bf500d8a8b0381e9decef451f20ba1677 : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsReportingInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsAnimalOperation : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsSolidWasteProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsHealthSafetyProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsComplianceInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsSiteInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsRemediationRedevelopmentProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsChemicalStorageProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsUndergroundStorageTankProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsDrinkingWaterProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsRegistryInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementActivity ||--|o OwlThing : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsWaterResourcesProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsPermitInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementActivity ||--|o RdfsResource : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsAirProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsWasteWaterProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsPesticidesProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsRiskInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsEnvironmentalInterestByProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsLegalEnforcementActivities : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsElectronicPermitSystem : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsEnvironmentalInterestType : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsFacilitySiteIdentification : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsChemicalReleaseProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementActivity ||--|o NaicsNAICS-IndustryGroup : "fio_ofIndustry"
Fio-epa-frsEnforcementActivity ||--|o RdfsResource : "fio_ofIndustry"
Fio-epa-frsEnforcementActivity ||--|o NaicsNAICS-IndustrySector : "fio_ofIndustry"
Fio-epa-frsEnforcementActivity ||--|o OwlNamedIndividual : "fio_ofIndustry"
Fio-epa-frsEnforcementActivity ||--|o NaicsNAICS-IndustryCode : "fio_ofIndustry"
Fio-epa-frsEnforcementActivity ||--|o OwlThing : "fio_ofIndustry"
Fio-epa-frsEnforcementActivity ||--|o FioIndustry : "fio_ofIndustry"
Fio-epa-frsEnforcementActivity ||--|o NaicsNAICS-IndustrySubsector : "fio_ofIndustry"
Fio-epa-frsEnforcementActivity ||--|o Bd7175f49ca206d160fdb4fee4dad2747 : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsRadiationProtectionProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsEnforcementInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsGroundWaterProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsAssistanceSupportProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsCoastalOceanProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsHazardousWasteProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementActivity ||--|o Bf500d8a8b0381e9decef451f20ba1677 : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsReportingInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsAnimalOperation : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsSolidWasteProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsComplianceInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsHealthSafetyProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsSiteInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsRemediationRedevelopmentProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsUndergroundStorageTankProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsDrinkingWaterProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsRegistryInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementActivity ||--|o OwlThing : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsWaterResourcesProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsChemicalReleaseProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsPermitInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementActivity ||--|o RdfsResource : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsAirProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsWasteWaterProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsPesticidesProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsRiskInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsEnvironmentalInterestByProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsLegalEnforcementActivities : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsElectronicPermitSystem : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsEnvironmentalInterestType : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsFacilitySiteIdentification : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsChemicalStorageProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsReportingRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsStateTrackingRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsTribalTrackingRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsEnforcementActivity ||--|o RdfsResource : "fio-epa-frs_hasRecord"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsPermitRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsRegistrationRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsSiteRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsEnforcementActivity : "fio-epa-frs_hasRecord"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsProjectRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsComplianceRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsRiskPlanRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsEnforcementActivity ||--|o OwlThing : "fio-epa-frs_hasRecord"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsEnforcementTrackingRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsSupplementalRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsEnforcementActivity ||--|o Fio-epa-frsFRS-Facility : "fio-epa-frs_hasRecord"
Fio-epa-frsEnforcementActivity ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsEnforcementActivity ||--|o NaicsNAICS-IndustryGroup : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsEnforcementActivity ||--|o RdfsResource : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsEnforcementActivity ||--|o NaicsNAICS-IndustrySector : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsEnforcementActivity ||--|o OwlNamedIndividual : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsEnforcementActivity ||--|o NaicsNAICS-IndustryCode : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsEnforcementActivity ||--|o OwlThing : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsEnforcementActivity ||--|o FioIndustry : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsEnforcementActivity ||--|o NaicsNAICS-IndustrySubsector : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsEnforcementInterest ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsEnforcementInterest ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsEnforcementSystem ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsEnforcementSystem ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsReportingRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsStateTrackingRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsEnforcementTrackingRecord ||--|o RdfsResource : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsPermitRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsSiteRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsRegistrationRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsEnforcementActivity : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsRiskPlanRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsEnforcementTrackingRecord ||--|o OwlThing : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsEnforcementTrackingRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsSupplementalRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsFRS-Facility : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsEnforcementTrackingRecord ||--|o RdfsLiteral : "dct_identifier"
Fio-epa-frsEnforcementTrackingRecord ||--|o NaicsNAICS-IndustryGroup : "fio-epa-frs_ofSecondaryIndustry"
Fio-epa-frsEnforcementTrackingRecord ||--|o RdfsResource : "fio-epa-frs_ofSecondaryIndustry"
Fio-epa-frsEnforcementTrackingRecord ||--|o OwlNamedIndividual : "fio-epa-frs_ofSecondaryIndustry"
Fio-epa-frsEnforcementTrackingRecord ||--|o NaicsNAICS-IndustryCode : "fio-epa-frs_ofSecondaryIndustry"
Fio-epa-frsEnforcementTrackingRecord ||--|o OwlThing : "fio-epa-frs_ofSecondaryIndustry"
Fio-epa-frsEnforcementTrackingRecord ||--|o FioIndustry : "fio-epa-frs_ofSecondaryIndustry"
Fio-epa-frsEnforcementTrackingRecord ||--|o NaicsNAICS-IndustrySubsector : "fio-epa-frs_ofSecondaryIndustry"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsLegacySystem : "fio-epa-frs_fromSystem"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsPermitSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsStateSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsProjectSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsComplianceSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsSiteSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsEnforcementTrackingRecord ||--|o RdfsResource : "fio-epa-frs_fromSystem"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsRegistrySystem : "fio-epa-frs_fromSystem"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsEnforcementSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsGrantSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsReportingSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsProgramInformationSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsTribalSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsEnforcementTrackingRecord ||--|o OwlThing : "fio-epa-frs_fromSystem"
Fio-epa-frsEnforcementTrackingRecord ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsEnforcementTrackingRecord ||--|o Bd7175f49ca206d160fdb4fee4dad2747 : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsRadiationProtectionProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsEnforcementInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsGroundWaterProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsAssistanceSupportProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsCoastalOceanProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsHazardousWasteProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementTrackingRecord ||--|o Bf500d8a8b0381e9decef451f20ba1677 : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsReportingInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsAnimalOperation : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsSolidWasteProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsHealthSafetyProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsComplianceInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsSiteInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsRemediationRedevelopmentProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsChemicalStorageProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsUndergroundStorageTankProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsDrinkingWaterProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsRegistryInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementTrackingRecord ||--|o OwlThing : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsWaterResourcesProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsPermitInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementTrackingRecord ||--|o RdfsResource : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsAirProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsWasteWaterProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsPesticidesProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsRiskInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsEnvironmentalInterestByProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsLegalEnforcementActivities : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsElectronicPermitSystem : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsEnvironmentalInterestType : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsFacilitySiteIdentification : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsChemicalReleaseProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsEnforcementTrackingRecord ||--|o NaicsNAICS-IndustryGroup : "fio_ofIndustry"
Fio-epa-frsEnforcementTrackingRecord ||--|o RdfsResource : "fio_ofIndustry"
Fio-epa-frsEnforcementTrackingRecord ||--|o NaicsNAICS-IndustrySector : "fio_ofIndustry"
Fio-epa-frsEnforcementTrackingRecord ||--|o OwlNamedIndividual : "fio_ofIndustry"
Fio-epa-frsEnforcementTrackingRecord ||--|o NaicsNAICS-IndustryCode : "fio_ofIndustry"
Fio-epa-frsEnforcementTrackingRecord ||--|o OwlThing : "fio_ofIndustry"
Fio-epa-frsEnforcementTrackingRecord ||--|o FioIndustry : "fio_ofIndustry"
Fio-epa-frsEnforcementTrackingRecord ||--|o NaicsNAICS-IndustrySubsector : "fio_ofIndustry"
Fio-epa-frsEnforcementTrackingRecord ||--|o Bd7175f49ca206d160fdb4fee4dad2747 : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsRadiationProtectionProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsEnforcementInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsGroundWaterProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsAssistanceSupportProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsCoastalOceanProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsHazardousWasteProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementTrackingRecord ||--|o Bf500d8a8b0381e9decef451f20ba1677 : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsReportingInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsAnimalOperation : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsSolidWasteProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsComplianceInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsHealthSafetyProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsSiteInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsRemediationRedevelopmentProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsUndergroundStorageTankProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsDrinkingWaterProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsRegistryInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementTrackingRecord ||--|o OwlThing : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsWaterResourcesProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsChemicalReleaseProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsPermitInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementTrackingRecord ||--|o RdfsResource : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsAirProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsWasteWaterProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsPesticidesProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsRiskInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsEnvironmentalInterestByProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsLegalEnforcementActivities : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsElectronicPermitSystem : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsEnvironmentalInterestType : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsFacilitySiteIdentification : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsChemicalStorageProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsReportingRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsStateTrackingRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsTribalTrackingRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsEnforcementTrackingRecord ||--|o RdfsResource : "fio-epa-frs_hasRecord"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsPermitRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsRegistrationRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsSiteRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsEnforcementActivity : "fio-epa-frs_hasRecord"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsProjectRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsComplianceRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsRiskPlanRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsEnforcementTrackingRecord ||--|o OwlThing : "fio-epa-frs_hasRecord"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsEnforcementTrackingRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsSupplementalRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsEnforcementTrackingRecord ||--|o Fio-epa-frsFRS-Facility : "fio-epa-frs_hasRecord"
Fio-epa-frsEnforcementTrackingRecord ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsEnforcementTrackingRecord ||--|o NaicsNAICS-IndustryGroup : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsEnforcementTrackingRecord ||--|o RdfsResource : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsEnforcementTrackingRecord ||--|o NaicsNAICS-IndustrySector : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsEnforcementTrackingRecord ||--|o OwlNamedIndividual : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsEnforcementTrackingRecord ||--|o NaicsNAICS-IndustryCode : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsEnforcementTrackingRecord ||--|o OwlThing : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsEnforcementTrackingRecord ||--|o FioIndustry : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsEnforcementTrackingRecord ||--|o NaicsNAICS-IndustrySubsector : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsEnvironmentalInterestByProgram ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsEnvironmentalInterestByProgram ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsEnvironmentalInterestType ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsEnvironmentalInterestType ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsLegacySystem : "fio-epa-frs_fromSystem"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsPermitSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsStateSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsProjectSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsComplianceSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsSiteSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsFRS-Facility ||--|o RdfsResource : "fio-epa-frs_fromSystem"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsRegistrySystem : "fio-epa-frs_fromSystem"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsEnforcementSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsGrantSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsReportingSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsProgramInformationSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsTribalSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsFRS-Facility ||--|o OwlThing : "fio-epa-frs_fromSystem"
Fio-epa-frsFRS-Facility ||--|o NaicsNAICS-IndustryGroup : "fio_ofIndustry"
Fio-epa-frsFRS-Facility ||--|o RdfsResource : "fio_ofIndustry"
Fio-epa-frsFRS-Facility ||--|o NaicsNAICS-IndustrySector : "fio_ofIndustry"
Fio-epa-frsFRS-Facility ||--|o OwlNamedIndividual : "fio_ofIndustry"
Fio-epa-frsFRS-Facility ||--|o NaicsNAICS-IndustryCode : "fio_ofIndustry"
Fio-epa-frsFRS-Facility ||--|o OwlThing : "fio_ofIndustry"
Fio-epa-frsFRS-Facility ||--|o FioIndustry : "fio_ofIndustry"
Fio-epa-frsFRS-Facility ||--|o NaicsNAICS-IndustrySubsector : "fio_ofIndustry"
Fio-epa-frsFRS-Facility ||--|o Bd7175f49ca206d160fdb4fee4dad2747 : "fio-epa-frs_ofInterestType"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsRadiationProtectionProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsEnforcementInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsGroundWaterProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsAssistanceSupportProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsCoastalOceanProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsHazardousWasteProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsFRS-Facility ||--|o Bf500d8a8b0381e9decef451f20ba1677 : "fio-epa-frs_ofInterestType"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsReportingInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsAnimalOperation : "fio-epa-frs_ofInterestType"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsSolidWasteProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsComplianceInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsHealthSafetyProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsSiteInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsRemediationRedevelopmentProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsUndergroundStorageTankProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsDrinkingWaterProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsRegistryInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsFRS-Facility ||--|o OwlThing : "fio-epa-frs_ofInterestType"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsWaterResourcesProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsChemicalReleaseProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsPermitInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsFRS-Facility ||--|o RdfsResource : "fio-epa-frs_ofInterestType"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsAirProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsWasteWaterProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsPesticidesProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsRiskInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsEnvironmentalInterestByProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsLegalEnforcementActivities : "fio-epa-frs_ofInterestType"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsElectronicPermitSystem : "fio-epa-frs_ofInterestType"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsEnvironmentalInterestType : "fio-epa-frs_ofInterestType"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsFacilitySiteIdentification : "fio-epa-frs_ofInterestType"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsChemicalStorageProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsFacilityType : "fio-epa-frs_ofFacilityType"
Fio-epa-frsFRS-Facility ||--|o RdfsResource : "fio-epa-frs_ofFacilityType"
Fio-epa-frsFRS-Facility ||--|o OwlThing : "fio-epa-frs_ofFacilityType"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsEPA-PFAS-Facility : "spatial_spatiallyRelatedTo"
Fio-epa-frsFRS-Facility ||--|o KwgoAdministrativeRegion3 : "spatial_spatiallyRelatedTo"
Fio-epa-frsFRS-Facility ||--|o KwgoRegion : "spatial_spatiallyRelatedTo"
Fio-epa-frsFRS-Facility ||--|o RdfsResource : "spatial_spatiallyRelatedTo"
Fio-epa-frsFRS-Facility ||--|o KwgoAdministrativeRegion : "spatial_spatiallyRelatedTo"
Fio-epa-frsFRS-Facility ||--|o KwgoS2CellLevel13 : "spatial_spatiallyRelatedTo"
Fio-epa-frsFRS-Facility ||--|o GeoSpatialObject : "spatial_spatiallyRelatedTo"
Fio-epa-frsFRS-Facility ||--|o OwlThing : "spatial_spatiallyRelatedTo"
Fio-epa-frsFRS-Facility ||--|o KwgoAdministrativeRegion2 : "spatial_spatiallyRelatedTo"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsFRS-Facility : "spatial_spatiallyRelatedTo"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsAgency.Interior : "fio_ownedBy"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsAgency.Transportation : "fio_ownedBy"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsAgency.Agriculture : "fio_ownedBy"
Fio-epa-frsFRS-Facility ||--|o RdfsResource : "fio_ownedBy"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsAgency.HealthandHumanServices : "fio_ownedBy"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsAgency.HomelandSecurity : "fio_ownedBy"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsAgency.Defense : "fio_ownedBy"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsAgency.Justice : "fio_ownedBy"
Fio-epa-frsFRS-Facility ||--|o OwlNamedIndividual : "fio_ownedBy"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsAgency : "fio_ownedBy"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsAgency.Commerce : "fio_ownedBy"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsAgency.Energy : "fio_ownedBy"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsAgency.VeteransAffairs : "fio_ownedBy"
Fio-epa-frsFRS-Facility ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsFRS-Facility ||--|o RdfsLiteral : "dct_alternative"
Fio-epa-frsFRS-Facility ||--|o GeoGeometry : "geo_hasGeometry"
Fio-epa-frsFRS-Facility ||--|o RdfsLiteral : "dct_identifier"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsReportingRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsStateTrackingRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsFRS-Facility ||--|o RdfsResource : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsPermitRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsSiteRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsRegistrationRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsEnforcementActivity : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsRiskPlanRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsFRS-Facility ||--|o OwlThing : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsEnforcementTrackingRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsSupplementalRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsFRS-Facility : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsFRS-Facility ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsEPA-PFAS-Facility : "spatial_connectedTo"
Fio-epa-frsFRS-Facility ||--|o KwgoAdministrativeRegion3 : "spatial_connectedTo"
Fio-epa-frsFRS-Facility ||--|o KwgoRegion : "spatial_connectedTo"
Fio-epa-frsFRS-Facility ||--|o RdfsResource : "spatial_connectedTo"
Fio-epa-frsFRS-Facility ||--|o KwgoAdministrativeRegion : "spatial_connectedTo"
Fio-epa-frsFRS-Facility ||--|o KwgoS2CellLevel13 : "spatial_connectedTo"
Fio-epa-frsFRS-Facility ||--|o GeoSpatialObject : "spatial_connectedTo"
Fio-epa-frsFRS-Facility ||--|o OwlThing : "spatial_connectedTo"
Fio-epa-frsFRS-Facility ||--|o KwgoAdministrativeRegion2 : "spatial_connectedTo"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsFRS-Facility : "spatial_connectedTo"
Fio-epa-frsFRS-Facility ||--|o RdfsLiteral : "dct_created"
Fio-epa-frsFRS-Facility ||--|o SdosPostalAddress : "sdos_address"
Fio-epa-frsFRS-Facility ||--|o SdosText : "sdos_address"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsReportingRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsStateTrackingRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsTribalTrackingRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsFRS-Facility ||--|o RdfsResource : "fio-epa-frs_hasRecord"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsPermitRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsRegistrationRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsSiteRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsEnforcementActivity : "fio-epa-frs_hasRecord"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsProjectRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsComplianceRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsRiskPlanRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsFRS-Facility ||--|o OwlThing : "fio-epa-frs_hasRecord"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsEnforcementTrackingRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsSupplementalRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsFRS-Facility : "fio-epa-frs_hasRecord"
Fio-epa-frsFRS-Facility ||--|o NaicsNAICS-IndustryGroup : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsFRS-Facility ||--|o RdfsResource : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsFRS-Facility ||--|o NaicsNAICS-IndustrySector : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsFRS-Facility ||--|o OwlNamedIndividual : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsFRS-Facility ||--|o NaicsNAICS-IndustryCode : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsFRS-Facility ||--|o OwlThing : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsFRS-Facility ||--|o FioIndustry : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsFRS-Facility ||--|o NaicsNAICS-IndustrySubsector : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsFRS-Facility ||--|o NaicsNAICS-IndustryGroup : "fio-epa-frs_ofSecondaryIndustry"
Fio-epa-frsFRS-Facility ||--|o RdfsResource : "fio-epa-frs_ofSecondaryIndustry"
Fio-epa-frsFRS-Facility ||--|o OwlNamedIndividual : "fio-epa-frs_ofSecondaryIndustry"
Fio-epa-frsFRS-Facility ||--|o NaicsNAICS-IndustryCode : "fio-epa-frs_ofSecondaryIndustry"
Fio-epa-frsFRS-Facility ||--|o OwlThing : "fio-epa-frs_ofSecondaryIndustry"
Fio-epa-frsFRS-Facility ||--|o FioIndustry : "fio-epa-frs_ofSecondaryIndustry"
Fio-epa-frsFRS-Facility ||--|o NaicsNAICS-IndustrySubsector : "fio-epa-frs_ofSecondaryIndustry"
Fio-epa-frsFRS-Facility ||--|o RdfsLiteral : "dct_modified"
Fio-epa-frsFRS-Facility ||--|o Bd7175f49ca206d160fdb4fee4dad2747 : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsRadiationProtectionProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsEnforcementInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsGroundWaterProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsAssistanceSupportProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsCoastalOceanProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsHazardousWasteProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsFRS-Facility ||--|o Bf500d8a8b0381e9decef451f20ba1677 : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsReportingInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsAnimalOperation : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsSolidWasteProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsHealthSafetyProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsComplianceInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsSiteInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsRemediationRedevelopmentProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsChemicalStorageProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsUndergroundStorageTankProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsDrinkingWaterProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsRegistryInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsFRS-Facility ||--|o OwlThing : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsWaterResourcesProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsPermitInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsFRS-Facility ||--|o RdfsResource : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsAirProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsWasteWaterProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsPesticidesProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsRiskInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsEnvironmentalInterestByProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsLegalEnforcementActivities : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsElectronicPermitSystem : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsEnvironmentalInterestType : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsFacilitySiteIdentification : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsFRS-Facility ||--|o Fio-epa-frsChemicalReleaseProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsFacilitySiteIdentification ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsFacilitySiteIdentification ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsFacilityType ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsFacilityType ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsGrantSystem ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsGrantSystem ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsGroundWaterProgram ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsGroundWaterProgram ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsHazardousWasteProgram ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsHazardousWasteProgram ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsHealthSafetyProgram ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsHealthSafetyProgram ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsLegacySystem ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsLegacySystem ||--|o Fio-epa-frsPermitSystem : "fio-epa-frs_replacedBy"
Fio-epa-frsLegacySystem ||--|o Fio-epa-frsSiteSystem : "fio-epa-frs_replacedBy"
Fio-epa-frsLegacySystem ||--|o RdfsResource : "fio-epa-frs_replacedBy"
Fio-epa-frsLegacySystem ||--|o Fio-epa-frsProgramInformationSystem : "fio-epa-frs_replacedBy"
Fio-epa-frsLegacySystem ||--|o OwlThing : "fio-epa-frs_replacedBy"
Fio-epa-frsLegacySystem ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsLegalEnforcementActivities ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsLegalEnforcementActivities ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsPermitInterest ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsPermitInterest ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsReportingRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsStateTrackingRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsPermitRecord ||--|o RdfsResource : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsPermitRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsSiteRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsRegistrationRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsEnforcementActivity : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsRiskPlanRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsPermitRecord ||--|o OwlThing : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsEnforcementTrackingRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsSupplementalRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsFRS-Facility : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsPermitRecord ||--|o RdfsLiteral : "dct_identifier"
Fio-epa-frsPermitRecord ||--|o NaicsNAICS-IndustryGroup : "fio-epa-frs_ofSecondaryIndustry"
Fio-epa-frsPermitRecord ||--|o RdfsResource : "fio-epa-frs_ofSecondaryIndustry"
Fio-epa-frsPermitRecord ||--|o OwlNamedIndividual : "fio-epa-frs_ofSecondaryIndustry"
Fio-epa-frsPermitRecord ||--|o NaicsNAICS-IndustryCode : "fio-epa-frs_ofSecondaryIndustry"
Fio-epa-frsPermitRecord ||--|o OwlThing : "fio-epa-frs_ofSecondaryIndustry"
Fio-epa-frsPermitRecord ||--|o FioIndustry : "fio-epa-frs_ofSecondaryIndustry"
Fio-epa-frsPermitRecord ||--|o NaicsNAICS-IndustrySubsector : "fio-epa-frs_ofSecondaryIndustry"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsLegacySystem : "fio-epa-frs_fromSystem"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsPermitSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsStateSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsProjectSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsComplianceSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsSiteSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsPermitRecord ||--|o RdfsResource : "fio-epa-frs_fromSystem"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsRegistrySystem : "fio-epa-frs_fromSystem"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsEnforcementSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsGrantSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsReportingSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsProgramInformationSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsTribalSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsPermitRecord ||--|o OwlThing : "fio-epa-frs_fromSystem"
Fio-epa-frsPermitRecord ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsPermitRecord ||--|o Bd7175f49ca206d160fdb4fee4dad2747 : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsRadiationProtectionProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsEnforcementInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsGroundWaterProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsAssistanceSupportProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsCoastalOceanProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsHazardousWasteProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsPermitRecord ||--|o Bf500d8a8b0381e9decef451f20ba1677 : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsReportingInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsAnimalOperation : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsSolidWasteProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsHealthSafetyProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsComplianceInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsSiteInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsRemediationRedevelopmentProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsChemicalStorageProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsUndergroundStorageTankProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsDrinkingWaterProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsRegistryInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsPermitRecord ||--|o OwlThing : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsWaterResourcesProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsPermitInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsPermitRecord ||--|o RdfsResource : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsAirProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsWasteWaterProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsPesticidesProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsRiskInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsEnvironmentalInterestByProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsLegalEnforcementActivities : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsElectronicPermitSystem : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsEnvironmentalInterestType : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsFacilitySiteIdentification : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsChemicalReleaseProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsPermitRecord ||--|o NaicsNAICS-IndustryGroup : "fio_ofIndustry"
Fio-epa-frsPermitRecord ||--|o RdfsResource : "fio_ofIndustry"
Fio-epa-frsPermitRecord ||--|o NaicsNAICS-IndustrySector : "fio_ofIndustry"
Fio-epa-frsPermitRecord ||--|o OwlNamedIndividual : "fio_ofIndustry"
Fio-epa-frsPermitRecord ||--|o NaicsNAICS-IndustryCode : "fio_ofIndustry"
Fio-epa-frsPermitRecord ||--|o OwlThing : "fio_ofIndustry"
Fio-epa-frsPermitRecord ||--|o FioIndustry : "fio_ofIndustry"
Fio-epa-frsPermitRecord ||--|o NaicsNAICS-IndustrySubsector : "fio_ofIndustry"
Fio-epa-frsPermitRecord ||--|o Bd7175f49ca206d160fdb4fee4dad2747 : "fio-epa-frs_ofInterestType"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsRadiationProtectionProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsEnforcementInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsGroundWaterProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsAssistanceSupportProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsCoastalOceanProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsHazardousWasteProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsPermitRecord ||--|o Bf500d8a8b0381e9decef451f20ba1677 : "fio-epa-frs_ofInterestType"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsReportingInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsAnimalOperation : "fio-epa-frs_ofInterestType"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsSolidWasteProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsComplianceInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsHealthSafetyProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsSiteInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsRemediationRedevelopmentProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsUndergroundStorageTankProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsDrinkingWaterProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsRegistryInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsPermitRecord ||--|o OwlThing : "fio-epa-frs_ofInterestType"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsWaterResourcesProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsChemicalReleaseProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsPermitInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsPermitRecord ||--|o RdfsResource : "fio-epa-frs_ofInterestType"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsAirProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsWasteWaterProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsPesticidesProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsRiskInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsEnvironmentalInterestByProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsLegalEnforcementActivities : "fio-epa-frs_ofInterestType"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsElectronicPermitSystem : "fio-epa-frs_ofInterestType"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsEnvironmentalInterestType : "fio-epa-frs_ofInterestType"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsFacilitySiteIdentification : "fio-epa-frs_ofInterestType"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsChemicalStorageProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsReportingRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsStateTrackingRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsTribalTrackingRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsPermitRecord ||--|o RdfsResource : "fio-epa-frs_hasRecord"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsPermitRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsRegistrationRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsSiteRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsEnforcementActivity : "fio-epa-frs_hasRecord"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsProjectRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsComplianceRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsRiskPlanRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsPermitRecord ||--|o OwlThing : "fio-epa-frs_hasRecord"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsEnforcementTrackingRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsSupplementalRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsPermitRecord ||--|o Fio-epa-frsFRS-Facility : "fio-epa-frs_hasRecord"
Fio-epa-frsPermitRecord ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsPermitRecord ||--|o NaicsNAICS-IndustryGroup : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsPermitRecord ||--|o RdfsResource : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsPermitRecord ||--|o NaicsNAICS-IndustrySector : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsPermitRecord ||--|o OwlNamedIndividual : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsPermitRecord ||--|o NaicsNAICS-IndustryCode : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsPermitRecord ||--|o OwlThing : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsPermitRecord ||--|o FioIndustry : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsPermitRecord ||--|o NaicsNAICS-IndustrySubsector : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsPermitSystem ||--|o RdfsResource : "fio-epa-frs_partOf"
Fio-epa-frsPermitSystem ||--|o Fio-epa-frsReportingSystem : "fio-epa-frs_partOf"
Fio-epa-frsPermitSystem ||--|o Fio-epa-frsProgramInformationSystem : "fio-epa-frs_partOf"
Fio-epa-frsPermitSystem ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsPermitSystem ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsPesticidesProgram ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsPesticidesProgram ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsProgramInformationSystem ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsProgramInformationSystem ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsProjectRecord ||--|o RdfsLiteral : "dct_identifier"
Fio-epa-frsProjectRecord ||--|o Fio-epa-frsLegacySystem : "fio-epa-frs_fromSystem"
Fio-epa-frsProjectRecord ||--|o Fio-epa-frsPermitSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsProjectRecord ||--|o Fio-epa-frsStateSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsProjectRecord ||--|o Fio-epa-frsProjectSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsProjectRecord ||--|o Fio-epa-frsComplianceSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsProjectRecord ||--|o Fio-epa-frsSiteSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsProjectRecord ||--|o RdfsResource : "fio-epa-frs_fromSystem"
Fio-epa-frsProjectRecord ||--|o Fio-epa-frsRegistrySystem : "fio-epa-frs_fromSystem"
Fio-epa-frsProjectRecord ||--|o Fio-epa-frsEnforcementSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsProjectRecord ||--|o Fio-epa-frsGrantSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsProjectRecord ||--|o Fio-epa-frsReportingSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsProjectRecord ||--|o Fio-epa-frsProgramInformationSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsProjectRecord ||--|o Fio-epa-frsTribalSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsProjectRecord ||--|o OwlThing : "fio-epa-frs_fromSystem"
Fio-epa-frsProjectRecord ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsProjectRecord ||--|o Bd7175f49ca206d160fdb4fee4dad2747 : "fio-epa-frs_ofInterestType"
Fio-epa-frsProjectRecord ||--|o Fio-epa-frsRadiationProtectionProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsProjectRecord ||--|o Fio-epa-frsEnforcementInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsProjectRecord ||--|o Fio-epa-frsGroundWaterProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsProjectRecord ||--|o Fio-epa-frsAssistanceSupportProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsProjectRecord ||--|o Fio-epa-frsCoastalOceanProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsProjectRecord ||--|o Fio-epa-frsHazardousWasteProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsProjectRecord ||--|o Bf500d8a8b0381e9decef451f20ba1677 : "fio-epa-frs_ofInterestType"
Fio-epa-frsProjectRecord ||--|o Fio-epa-frsReportingInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsProjectRecord ||--|o Fio-epa-frsAnimalOperation : "fio-epa-frs_ofInterestType"
Fio-epa-frsProjectRecord ||--|o Fio-epa-frsSolidWasteProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsProjectRecord ||--|o Fio-epa-frsComplianceInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsProjectRecord ||--|o Fio-epa-frsHealthSafetyProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsProjectRecord ||--|o Fio-epa-frsSiteInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsProjectRecord ||--|o Fio-epa-frsRemediationRedevelopmentProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsProjectRecord ||--|o Fio-epa-frsUndergroundStorageTankProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsProjectRecord ||--|o Fio-epa-frsDrinkingWaterProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsProjectRecord ||--|o Fio-epa-frsRegistryInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsProjectRecord ||--|o OwlThing : "fio-epa-frs_ofInterestType"
Fio-epa-frsProjectRecord ||--|o Fio-epa-frsWaterResourcesProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsProjectRecord ||--|o Fio-epa-frsChemicalReleaseProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsProjectRecord ||--|o Fio-epa-frsPermitInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsProjectRecord ||--|o RdfsResource : "fio-epa-frs_ofInterestType"
Fio-epa-frsProjectRecord ||--|o Fio-epa-frsAirProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsProjectRecord ||--|o Fio-epa-frsWasteWaterProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsProjectRecord ||--|o Fio-epa-frsPesticidesProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsProjectRecord ||--|o Fio-epa-frsRiskInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsProjectRecord ||--|o Fio-epa-frsEnvironmentalInterestByProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsProjectRecord ||--|o Fio-epa-frsLegalEnforcementActivities : "fio-epa-frs_ofInterestType"
Fio-epa-frsProjectRecord ||--|o Fio-epa-frsElectronicPermitSystem : "fio-epa-frs_ofInterestType"
Fio-epa-frsProjectRecord ||--|o Fio-epa-frsEnvironmentalInterestType : "fio-epa-frs_ofInterestType"
Fio-epa-frsProjectRecord ||--|o Fio-epa-frsFacilitySiteIdentification : "fio-epa-frs_ofInterestType"
Fio-epa-frsProjectRecord ||--|o Fio-epa-frsChemicalStorageProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsProjectRecord ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsProjectSystem ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsProjectSystem ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsRadiationProtectionProgram ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsRadiationProtectionProgram ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsRecord ||--|o Fio-epa-frsReportingRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsRecord ||--|o Fio-epa-frsStateTrackingRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsRecord ||--|o Fio-epa-frsRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsRecord ||--|o RdfsResource : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsRecord ||--|o Fio-epa-frsPermitRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsRecord ||--|o Fio-epa-frsSiteRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsRecord ||--|o Fio-epa-frsRegistrationRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsRecord ||--|o Fio-epa-frsEnforcementActivity : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsRecord ||--|o Fio-epa-frsRiskPlanRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsRecord ||--|o OwlThing : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsRecord ||--|o Fio-epa-frsEnforcementTrackingRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsRecord ||--|o Fio-epa-frsSupplementalRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsRecord ||--|o Fio-epa-frsFRS-Facility : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsRecord ||--|o RdfsLiteral : "dct_identifier"
Fio-epa-frsRecord ||--|o NaicsNAICS-IndustryGroup : "fio-epa-frs_ofSecondaryIndustry"
Fio-epa-frsRecord ||--|o RdfsResource : "fio-epa-frs_ofSecondaryIndustry"
Fio-epa-frsRecord ||--|o OwlNamedIndividual : "fio-epa-frs_ofSecondaryIndustry"
Fio-epa-frsRecord ||--|o NaicsNAICS-IndustryCode : "fio-epa-frs_ofSecondaryIndustry"
Fio-epa-frsRecord ||--|o OwlThing : "fio-epa-frs_ofSecondaryIndustry"
Fio-epa-frsRecord ||--|o FioIndustry : "fio-epa-frs_ofSecondaryIndustry"
Fio-epa-frsRecord ||--|o NaicsNAICS-IndustrySubsector : "fio-epa-frs_ofSecondaryIndustry"
Fio-epa-frsRecord ||--|o Fio-epa-frsLegacySystem : "fio-epa-frs_fromSystem"
Fio-epa-frsRecord ||--|o Fio-epa-frsPermitSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsRecord ||--|o Fio-epa-frsStateSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsRecord ||--|o Fio-epa-frsProjectSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsRecord ||--|o Fio-epa-frsComplianceSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsRecord ||--|o Fio-epa-frsSiteSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsRecord ||--|o RdfsResource : "fio-epa-frs_fromSystem"
Fio-epa-frsRecord ||--|o Fio-epa-frsRegistrySystem : "fio-epa-frs_fromSystem"
Fio-epa-frsRecord ||--|o Fio-epa-frsEnforcementSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsRecord ||--|o Fio-epa-frsGrantSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsRecord ||--|o Fio-epa-frsReportingSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsRecord ||--|o Fio-epa-frsProgramInformationSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsRecord ||--|o Fio-epa-frsTribalSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsRecord ||--|o OwlThing : "fio-epa-frs_fromSystem"
Fio-epa-frsRecord ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsRecord ||--|o Bd7175f49ca206d160fdb4fee4dad2747 : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRecord ||--|o Fio-epa-frsRadiationProtectionProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRecord ||--|o Fio-epa-frsEnforcementInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRecord ||--|o Fio-epa-frsGroundWaterProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRecord ||--|o Fio-epa-frsAssistanceSupportProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRecord ||--|o Fio-epa-frsCoastalOceanProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRecord ||--|o Fio-epa-frsHazardousWasteProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRecord ||--|o Bf500d8a8b0381e9decef451f20ba1677 : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRecord ||--|o Fio-epa-frsReportingInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRecord ||--|o Fio-epa-frsAnimalOperation : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRecord ||--|o Fio-epa-frsSolidWasteProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRecord ||--|o Fio-epa-frsHealthSafetyProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRecord ||--|o Fio-epa-frsComplianceInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRecord ||--|o Fio-epa-frsSiteInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRecord ||--|o Fio-epa-frsRemediationRedevelopmentProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRecord ||--|o Fio-epa-frsChemicalStorageProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRecord ||--|o Fio-epa-frsUndergroundStorageTankProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRecord ||--|o Fio-epa-frsDrinkingWaterProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRecord ||--|o Fio-epa-frsRegistryInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRecord ||--|o OwlThing : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRecord ||--|o Fio-epa-frsWaterResourcesProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRecord ||--|o Fio-epa-frsPermitInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRecord ||--|o RdfsResource : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRecord ||--|o Fio-epa-frsAirProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRecord ||--|o Fio-epa-frsWasteWaterProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRecord ||--|o Fio-epa-frsPesticidesProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRecord ||--|o Fio-epa-frsRiskInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRecord ||--|o Fio-epa-frsEnvironmentalInterestByProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRecord ||--|o Fio-epa-frsLegalEnforcementActivities : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRecord ||--|o Fio-epa-frsElectronicPermitSystem : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRecord ||--|o Fio-epa-frsEnvironmentalInterestType : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRecord ||--|o Fio-epa-frsFacilitySiteIdentification : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRecord ||--|o Fio-epa-frsChemicalReleaseProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRecord ||--|o NaicsNAICS-IndustryGroup : "fio_ofIndustry"
Fio-epa-frsRecord ||--|o RdfsResource : "fio_ofIndustry"
Fio-epa-frsRecord ||--|o NaicsNAICS-IndustrySector : "fio_ofIndustry"
Fio-epa-frsRecord ||--|o OwlNamedIndividual : "fio_ofIndustry"
Fio-epa-frsRecord ||--|o NaicsNAICS-IndustryCode : "fio_ofIndustry"
Fio-epa-frsRecord ||--|o OwlThing : "fio_ofIndustry"
Fio-epa-frsRecord ||--|o FioIndustry : "fio_ofIndustry"
Fio-epa-frsRecord ||--|o NaicsNAICS-IndustrySubsector : "fio_ofIndustry"
Fio-epa-frsRecord ||--|o Bd7175f49ca206d160fdb4fee4dad2747 : "fio-epa-frs_ofInterestType"
Fio-epa-frsRecord ||--|o Fio-epa-frsRadiationProtectionProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsRecord ||--|o Fio-epa-frsEnforcementInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsRecord ||--|o Fio-epa-frsGroundWaterProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsRecord ||--|o Fio-epa-frsAssistanceSupportProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsRecord ||--|o Fio-epa-frsCoastalOceanProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsRecord ||--|o Fio-epa-frsHazardousWasteProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsRecord ||--|o Bf500d8a8b0381e9decef451f20ba1677 : "fio-epa-frs_ofInterestType"
Fio-epa-frsRecord ||--|o Fio-epa-frsReportingInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsRecord ||--|o Fio-epa-frsAnimalOperation : "fio-epa-frs_ofInterestType"
Fio-epa-frsRecord ||--|o Fio-epa-frsSolidWasteProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsRecord ||--|o Fio-epa-frsComplianceInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsRecord ||--|o Fio-epa-frsHealthSafetyProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsRecord ||--|o Fio-epa-frsSiteInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsRecord ||--|o Fio-epa-frsRemediationRedevelopmentProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsRecord ||--|o Fio-epa-frsUndergroundStorageTankProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsRecord ||--|o Fio-epa-frsDrinkingWaterProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsRecord ||--|o Fio-epa-frsRegistryInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsRecord ||--|o OwlThing : "fio-epa-frs_ofInterestType"
Fio-epa-frsRecord ||--|o Fio-epa-frsWaterResourcesProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsRecord ||--|o Fio-epa-frsChemicalReleaseProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsRecord ||--|o Fio-epa-frsPermitInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsRecord ||--|o RdfsResource : "fio-epa-frs_ofInterestType"
Fio-epa-frsRecord ||--|o Fio-epa-frsAirProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsRecord ||--|o Fio-epa-frsWasteWaterProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsRecord ||--|o Fio-epa-frsPesticidesProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsRecord ||--|o Fio-epa-frsRiskInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsRecord ||--|o Fio-epa-frsEnvironmentalInterestByProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsRecord ||--|o Fio-epa-frsLegalEnforcementActivities : "fio-epa-frs_ofInterestType"
Fio-epa-frsRecord ||--|o Fio-epa-frsElectronicPermitSystem : "fio-epa-frs_ofInterestType"
Fio-epa-frsRecord ||--|o Fio-epa-frsEnvironmentalInterestType : "fio-epa-frs_ofInterestType"
Fio-epa-frsRecord ||--|o Fio-epa-frsFacilitySiteIdentification : "fio-epa-frs_ofInterestType"
Fio-epa-frsRecord ||--|o Fio-epa-frsChemicalStorageProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsRecord ||--|o Fio-epa-frsReportingRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsRecord ||--|o Fio-epa-frsStateTrackingRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsRecord ||--|o Fio-epa-frsTribalTrackingRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsRecord ||--|o Fio-epa-frsRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsRecord ||--|o RdfsResource : "fio-epa-frs_hasRecord"
Fio-epa-frsRecord ||--|o Fio-epa-frsPermitRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsRecord ||--|o Fio-epa-frsRegistrationRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsRecord ||--|o Fio-epa-frsSiteRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsRecord ||--|o Fio-epa-frsEnforcementActivity : "fio-epa-frs_hasRecord"
Fio-epa-frsRecord ||--|o Fio-epa-frsProjectRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsRecord ||--|o Fio-epa-frsComplianceRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsRecord ||--|o Fio-epa-frsRiskPlanRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsRecord ||--|o OwlThing : "fio-epa-frs_hasRecord"
Fio-epa-frsRecord ||--|o Fio-epa-frsEnforcementTrackingRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsRecord ||--|o Fio-epa-frsSupplementalRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsRecord ||--|o Fio-epa-frsFRS-Facility : "fio-epa-frs_hasRecord"
Fio-epa-frsRecord ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsRecord ||--|o NaicsNAICS-IndustryGroup : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsRecord ||--|o RdfsResource : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsRecord ||--|o NaicsNAICS-IndustrySector : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsRecord ||--|o OwlNamedIndividual : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsRecord ||--|o NaicsNAICS-IndustryCode : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsRecord ||--|o OwlThing : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsRecord ||--|o FioIndustry : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsRecord ||--|o NaicsNAICS-IndustrySubsector : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsReportingRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsStateTrackingRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsRegistrationRecord ||--|o RdfsResource : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsPermitRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsSiteRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsRegistrationRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsEnforcementActivity : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsRiskPlanRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsRegistrationRecord ||--|o OwlThing : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsEnforcementTrackingRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsSupplementalRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsFRS-Facility : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsRegistrationRecord ||--|o RdfsLiteral : "dct_identifier"
Fio-epa-frsRegistrationRecord ||--|o NaicsNAICS-IndustryGroup : "fio-epa-frs_ofSecondaryIndustry"
Fio-epa-frsRegistrationRecord ||--|o RdfsResource : "fio-epa-frs_ofSecondaryIndustry"
Fio-epa-frsRegistrationRecord ||--|o OwlNamedIndividual : "fio-epa-frs_ofSecondaryIndustry"
Fio-epa-frsRegistrationRecord ||--|o NaicsNAICS-IndustryCode : "fio-epa-frs_ofSecondaryIndustry"
Fio-epa-frsRegistrationRecord ||--|o OwlThing : "fio-epa-frs_ofSecondaryIndustry"
Fio-epa-frsRegistrationRecord ||--|o FioIndustry : "fio-epa-frs_ofSecondaryIndustry"
Fio-epa-frsRegistrationRecord ||--|o NaicsNAICS-IndustrySubsector : "fio-epa-frs_ofSecondaryIndustry"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsLegacySystem : "fio-epa-frs_fromSystem"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsPermitSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsStateSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsProjectSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsComplianceSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsSiteSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsRegistrationRecord ||--|o RdfsResource : "fio-epa-frs_fromSystem"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsRegistrySystem : "fio-epa-frs_fromSystem"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsEnforcementSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsGrantSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsReportingSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsProgramInformationSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsTribalSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsRegistrationRecord ||--|o OwlThing : "fio-epa-frs_fromSystem"
Fio-epa-frsRegistrationRecord ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsRegistrationRecord ||--|o Bd7175f49ca206d160fdb4fee4dad2747 : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsRadiationProtectionProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsEnforcementInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsGroundWaterProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsAssistanceSupportProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsCoastalOceanProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsHazardousWasteProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRegistrationRecord ||--|o Bf500d8a8b0381e9decef451f20ba1677 : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsReportingInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsAnimalOperation : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsSolidWasteProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsHealthSafetyProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsComplianceInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsSiteInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsRemediationRedevelopmentProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsChemicalStorageProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsUndergroundStorageTankProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsDrinkingWaterProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsRegistryInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRegistrationRecord ||--|o OwlThing : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsWaterResourcesProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsPermitInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRegistrationRecord ||--|o RdfsResource : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsAirProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsWasteWaterProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsPesticidesProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsRiskInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsEnvironmentalInterestByProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsLegalEnforcementActivities : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsElectronicPermitSystem : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsEnvironmentalInterestType : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsFacilitySiteIdentification : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsChemicalReleaseProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRegistrationRecord ||--|o NaicsNAICS-IndustryGroup : "fio_ofIndustry"
Fio-epa-frsRegistrationRecord ||--|o RdfsResource : "fio_ofIndustry"
Fio-epa-frsRegistrationRecord ||--|o NaicsNAICS-IndustrySector : "fio_ofIndustry"
Fio-epa-frsRegistrationRecord ||--|o OwlNamedIndividual : "fio_ofIndustry"
Fio-epa-frsRegistrationRecord ||--|o NaicsNAICS-IndustryCode : "fio_ofIndustry"
Fio-epa-frsRegistrationRecord ||--|o OwlThing : "fio_ofIndustry"
Fio-epa-frsRegistrationRecord ||--|o FioIndustry : "fio_ofIndustry"
Fio-epa-frsRegistrationRecord ||--|o NaicsNAICS-IndustrySubsector : "fio_ofIndustry"
Fio-epa-frsRegistrationRecord ||--|o Bd7175f49ca206d160fdb4fee4dad2747 : "fio-epa-frs_ofInterestType"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsRadiationProtectionProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsEnforcementInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsGroundWaterProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsAssistanceSupportProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsCoastalOceanProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsHazardousWasteProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsRegistrationRecord ||--|o Bf500d8a8b0381e9decef451f20ba1677 : "fio-epa-frs_ofInterestType"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsReportingInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsAnimalOperation : "fio-epa-frs_ofInterestType"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsSolidWasteProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsComplianceInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsHealthSafetyProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsSiteInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsRemediationRedevelopmentProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsUndergroundStorageTankProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsDrinkingWaterProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsRegistryInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsRegistrationRecord ||--|o OwlThing : "fio-epa-frs_ofInterestType"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsWaterResourcesProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsChemicalReleaseProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsPermitInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsRegistrationRecord ||--|o RdfsResource : "fio-epa-frs_ofInterestType"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsAirProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsWasteWaterProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsPesticidesProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsRiskInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsEnvironmentalInterestByProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsLegalEnforcementActivities : "fio-epa-frs_ofInterestType"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsElectronicPermitSystem : "fio-epa-frs_ofInterestType"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsEnvironmentalInterestType : "fio-epa-frs_ofInterestType"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsFacilitySiteIdentification : "fio-epa-frs_ofInterestType"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsChemicalStorageProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsReportingRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsStateTrackingRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsTribalTrackingRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsRegistrationRecord ||--|o RdfsResource : "fio-epa-frs_hasRecord"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsPermitRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsRegistrationRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsSiteRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsEnforcementActivity : "fio-epa-frs_hasRecord"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsProjectRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsComplianceRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsRiskPlanRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsRegistrationRecord ||--|o OwlThing : "fio-epa-frs_hasRecord"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsEnforcementTrackingRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsSupplementalRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsRegistrationRecord ||--|o Fio-epa-frsFRS-Facility : "fio-epa-frs_hasRecord"
Fio-epa-frsRegistrationRecord ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsRegistrationRecord ||--|o NaicsNAICS-IndustryGroup : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsRegistrationRecord ||--|o RdfsResource : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsRegistrationRecord ||--|o NaicsNAICS-IndustrySector : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsRegistrationRecord ||--|o OwlNamedIndividual : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsRegistrationRecord ||--|o NaicsNAICS-IndustryCode : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsRegistrationRecord ||--|o OwlThing : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsRegistrationRecord ||--|o FioIndustry : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsRegistrationRecord ||--|o NaicsNAICS-IndustrySubsector : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsRegistryInterest ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsRegistryInterest ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsRegistrySystem ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsRegistrySystem ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsRemediationRedevelopmentProgram ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsRemediationRedevelopmentProgram ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsReportingInterest ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsReportingInterest ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsReportingRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsStateTrackingRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsReportingRecord ||--|o RdfsResource : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsPermitRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsSiteRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsRegistrationRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsEnforcementActivity : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsRiskPlanRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsReportingRecord ||--|o OwlThing : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsEnforcementTrackingRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsSupplementalRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsFRS-Facility : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsReportingRecord ||--|o RdfsLiteral : "dct_identifier"
Fio-epa-frsReportingRecord ||--|o NaicsNAICS-IndustryGroup : "fio-epa-frs_ofSecondaryIndustry"
Fio-epa-frsReportingRecord ||--|o RdfsResource : "fio-epa-frs_ofSecondaryIndustry"
Fio-epa-frsReportingRecord ||--|o OwlNamedIndividual : "fio-epa-frs_ofSecondaryIndustry"
Fio-epa-frsReportingRecord ||--|o NaicsNAICS-IndustryCode : "fio-epa-frs_ofSecondaryIndustry"
Fio-epa-frsReportingRecord ||--|o OwlThing : "fio-epa-frs_ofSecondaryIndustry"
Fio-epa-frsReportingRecord ||--|o FioIndustry : "fio-epa-frs_ofSecondaryIndustry"
Fio-epa-frsReportingRecord ||--|o NaicsNAICS-IndustrySubsector : "fio-epa-frs_ofSecondaryIndustry"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsLegacySystem : "fio-epa-frs_fromSystem"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsPermitSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsStateSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsProjectSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsComplianceSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsSiteSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsReportingRecord ||--|o RdfsResource : "fio-epa-frs_fromSystem"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsRegistrySystem : "fio-epa-frs_fromSystem"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsEnforcementSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsGrantSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsReportingSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsProgramInformationSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsTribalSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsReportingRecord ||--|o OwlThing : "fio-epa-frs_fromSystem"
Fio-epa-frsReportingRecord ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsReportingRecord ||--|o Bd7175f49ca206d160fdb4fee4dad2747 : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsRadiationProtectionProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsEnforcementInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsGroundWaterProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsAssistanceSupportProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsCoastalOceanProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsHazardousWasteProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsReportingRecord ||--|o Bf500d8a8b0381e9decef451f20ba1677 : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsReportingInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsAnimalOperation : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsSolidWasteProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsHealthSafetyProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsComplianceInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsSiteInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsRemediationRedevelopmentProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsChemicalStorageProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsUndergroundStorageTankProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsDrinkingWaterProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsRegistryInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsReportingRecord ||--|o OwlThing : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsWaterResourcesProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsPermitInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsReportingRecord ||--|o RdfsResource : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsAirProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsWasteWaterProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsPesticidesProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsRiskInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsEnvironmentalInterestByProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsLegalEnforcementActivities : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsElectronicPermitSystem : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsEnvironmentalInterestType : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsFacilitySiteIdentification : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsChemicalReleaseProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsReportingRecord ||--|o NaicsNAICS-IndustryGroup : "fio_ofIndustry"
Fio-epa-frsReportingRecord ||--|o RdfsResource : "fio_ofIndustry"
Fio-epa-frsReportingRecord ||--|o NaicsNAICS-IndustrySector : "fio_ofIndustry"
Fio-epa-frsReportingRecord ||--|o OwlNamedIndividual : "fio_ofIndustry"
Fio-epa-frsReportingRecord ||--|o NaicsNAICS-IndustryCode : "fio_ofIndustry"
Fio-epa-frsReportingRecord ||--|o OwlThing : "fio_ofIndustry"
Fio-epa-frsReportingRecord ||--|o FioIndustry : "fio_ofIndustry"
Fio-epa-frsReportingRecord ||--|o NaicsNAICS-IndustrySubsector : "fio_ofIndustry"
Fio-epa-frsReportingRecord ||--|o Bd7175f49ca206d160fdb4fee4dad2747 : "fio-epa-frs_ofInterestType"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsRadiationProtectionProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsEnforcementInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsGroundWaterProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsAssistanceSupportProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsCoastalOceanProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsHazardousWasteProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsReportingRecord ||--|o Bf500d8a8b0381e9decef451f20ba1677 : "fio-epa-frs_ofInterestType"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsReportingInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsAnimalOperation : "fio-epa-frs_ofInterestType"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsSolidWasteProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsComplianceInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsHealthSafetyProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsSiteInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsRemediationRedevelopmentProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsUndergroundStorageTankProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsDrinkingWaterProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsRegistryInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsReportingRecord ||--|o OwlThing : "fio-epa-frs_ofInterestType"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsWaterResourcesProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsChemicalReleaseProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsPermitInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsReportingRecord ||--|o RdfsResource : "fio-epa-frs_ofInterestType"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsAirProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsWasteWaterProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsPesticidesProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsRiskInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsEnvironmentalInterestByProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsLegalEnforcementActivities : "fio-epa-frs_ofInterestType"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsElectronicPermitSystem : "fio-epa-frs_ofInterestType"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsEnvironmentalInterestType : "fio-epa-frs_ofInterestType"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsFacilitySiteIdentification : "fio-epa-frs_ofInterestType"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsChemicalStorageProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsReportingRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsStateTrackingRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsTribalTrackingRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsReportingRecord ||--|o RdfsResource : "fio-epa-frs_hasRecord"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsPermitRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsRegistrationRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsSiteRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsEnforcementActivity : "fio-epa-frs_hasRecord"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsProjectRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsComplianceRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsRiskPlanRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsReportingRecord ||--|o OwlThing : "fio-epa-frs_hasRecord"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsEnforcementTrackingRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsSupplementalRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsReportingRecord ||--|o Fio-epa-frsFRS-Facility : "fio-epa-frs_hasRecord"
Fio-epa-frsReportingRecord ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsReportingRecord ||--|o NaicsNAICS-IndustryGroup : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsReportingRecord ||--|o RdfsResource : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsReportingRecord ||--|o NaicsNAICS-IndustrySector : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsReportingRecord ||--|o OwlNamedIndividual : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsReportingRecord ||--|o NaicsNAICS-IndustryCode : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsReportingRecord ||--|o OwlThing : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsReportingRecord ||--|o FioIndustry : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsReportingRecord ||--|o NaicsNAICS-IndustrySubsector : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsReportingSystem ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsReportingSystem ||--|o RdfsResource : "fio-epa-frs_partOf"
Fio-epa-frsReportingSystem ||--|o Fio-epa-frsReportingSystem : "fio-epa-frs_partOf"
Fio-epa-frsReportingSystem ||--|o Fio-epa-frsProgramInformationSystem : "fio-epa-frs_partOf"
Fio-epa-frsReportingSystem ||--|o Fio-epa-frsPermitSystem : "fio-epa-frs_replacedBy"
Fio-epa-frsReportingSystem ||--|o Fio-epa-frsSiteSystem : "fio-epa-frs_replacedBy"
Fio-epa-frsReportingSystem ||--|o RdfsResource : "fio-epa-frs_replacedBy"
Fio-epa-frsReportingSystem ||--|o Fio-epa-frsProgramInformationSystem : "fio-epa-frs_replacedBy"
Fio-epa-frsReportingSystem ||--|o OwlThing : "fio-epa-frs_replacedBy"
Fio-epa-frsReportingSystem ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsRiskInterest ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsRiskInterest ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsReportingRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsStateTrackingRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsRiskPlanRecord ||--|o RdfsResource : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsPermitRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsSiteRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsRegistrationRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsEnforcementActivity : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsRiskPlanRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsRiskPlanRecord ||--|o OwlThing : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsEnforcementTrackingRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsSupplementalRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsFRS-Facility : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsRiskPlanRecord ||--|o RdfsLiteral : "dct_identifier"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsLegacySystem : "fio-epa-frs_fromSystem"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsPermitSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsStateSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsProjectSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsComplianceSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsSiteSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsRiskPlanRecord ||--|o RdfsResource : "fio-epa-frs_fromSystem"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsRegistrySystem : "fio-epa-frs_fromSystem"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsEnforcementSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsGrantSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsReportingSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsProgramInformationSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsTribalSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsRiskPlanRecord ||--|o OwlThing : "fio-epa-frs_fromSystem"
Fio-epa-frsRiskPlanRecord ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsRiskPlanRecord ||--|o Bd7175f49ca206d160fdb4fee4dad2747 : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsRadiationProtectionProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsEnforcementInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsGroundWaterProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsAssistanceSupportProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsCoastalOceanProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsHazardousWasteProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRiskPlanRecord ||--|o Bf500d8a8b0381e9decef451f20ba1677 : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsReportingInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsAnimalOperation : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsSolidWasteProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsHealthSafetyProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsComplianceInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsSiteInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsRemediationRedevelopmentProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsChemicalStorageProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsUndergroundStorageTankProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsDrinkingWaterProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsRegistryInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRiskPlanRecord ||--|o OwlThing : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsWaterResourcesProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsPermitInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRiskPlanRecord ||--|o RdfsResource : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsAirProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsWasteWaterProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsPesticidesProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsRiskInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsEnvironmentalInterestByProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsLegalEnforcementActivities : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsElectronicPermitSystem : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsEnvironmentalInterestType : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsFacilitySiteIdentification : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsChemicalReleaseProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsRiskPlanRecord ||--|o Bd7175f49ca206d160fdb4fee4dad2747 : "fio-epa-frs_ofInterestType"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsRadiationProtectionProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsEnforcementInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsGroundWaterProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsAssistanceSupportProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsCoastalOceanProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsHazardousWasteProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsRiskPlanRecord ||--|o Bf500d8a8b0381e9decef451f20ba1677 : "fio-epa-frs_ofInterestType"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsReportingInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsAnimalOperation : "fio-epa-frs_ofInterestType"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsSolidWasteProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsComplianceInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsHealthSafetyProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsSiteInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsRemediationRedevelopmentProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsUndergroundStorageTankProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsDrinkingWaterProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsRegistryInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsRiskPlanRecord ||--|o OwlThing : "fio-epa-frs_ofInterestType"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsWaterResourcesProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsChemicalReleaseProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsPermitInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsRiskPlanRecord ||--|o RdfsResource : "fio-epa-frs_ofInterestType"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsAirProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsWasteWaterProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsPesticidesProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsRiskInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsEnvironmentalInterestByProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsLegalEnforcementActivities : "fio-epa-frs_ofInterestType"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsElectronicPermitSystem : "fio-epa-frs_ofInterestType"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsEnvironmentalInterestType : "fio-epa-frs_ofInterestType"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsFacilitySiteIdentification : "fio-epa-frs_ofInterestType"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsChemicalStorageProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsReportingRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsStateTrackingRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsTribalTrackingRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsRiskPlanRecord ||--|o RdfsResource : "fio-epa-frs_hasRecord"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsPermitRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsRegistrationRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsSiteRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsEnforcementActivity : "fio-epa-frs_hasRecord"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsProjectRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsComplianceRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsRiskPlanRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsRiskPlanRecord ||--|o OwlThing : "fio-epa-frs_hasRecord"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsEnforcementTrackingRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsSupplementalRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsRiskPlanRecord ||--|o Fio-epa-frsFRS-Facility : "fio-epa-frs_hasRecord"
Fio-epa-frsRiskPlanRecord ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsSiteInterest ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsSiteInterest ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsReportingRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsStateTrackingRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsSiteRecord ||--|o RdfsResource : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsPermitRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsSiteRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsRegistrationRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsEnforcementActivity : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsRiskPlanRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsSiteRecord ||--|o OwlThing : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsEnforcementTrackingRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsSupplementalRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsFRS-Facility : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsSiteRecord ||--|o RdfsLiteral : "dct_identifier"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsLegacySystem : "fio-epa-frs_fromSystem"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsPermitSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsStateSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsProjectSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsComplianceSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsSiteSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsSiteRecord ||--|o RdfsResource : "fio-epa-frs_fromSystem"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsRegistrySystem : "fio-epa-frs_fromSystem"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsEnforcementSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsGrantSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsReportingSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsProgramInformationSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsTribalSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsSiteRecord ||--|o OwlThing : "fio-epa-frs_fromSystem"
Fio-epa-frsSiteRecord ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsSiteRecord ||--|o Bd7175f49ca206d160fdb4fee4dad2747 : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsRadiationProtectionProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsEnforcementInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsGroundWaterProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsAssistanceSupportProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsCoastalOceanProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsHazardousWasteProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSiteRecord ||--|o Bf500d8a8b0381e9decef451f20ba1677 : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsReportingInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsAnimalOperation : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsSolidWasteProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsHealthSafetyProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsComplianceInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsSiteInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsRemediationRedevelopmentProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsChemicalStorageProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsUndergroundStorageTankProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsDrinkingWaterProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsRegistryInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSiteRecord ||--|o OwlThing : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsWaterResourcesProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsPermitInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSiteRecord ||--|o RdfsResource : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsAirProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsWasteWaterProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsPesticidesProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsRiskInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsEnvironmentalInterestByProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsLegalEnforcementActivities : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsElectronicPermitSystem : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsEnvironmentalInterestType : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsFacilitySiteIdentification : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsChemicalReleaseProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSiteRecord ||--|o NaicsNAICS-IndustryGroup : "fio_ofIndustry"
Fio-epa-frsSiteRecord ||--|o RdfsResource : "fio_ofIndustry"
Fio-epa-frsSiteRecord ||--|o NaicsNAICS-IndustrySector : "fio_ofIndustry"
Fio-epa-frsSiteRecord ||--|o OwlNamedIndividual : "fio_ofIndustry"
Fio-epa-frsSiteRecord ||--|o NaicsNAICS-IndustryCode : "fio_ofIndustry"
Fio-epa-frsSiteRecord ||--|o OwlThing : "fio_ofIndustry"
Fio-epa-frsSiteRecord ||--|o FioIndustry : "fio_ofIndustry"
Fio-epa-frsSiteRecord ||--|o NaicsNAICS-IndustrySubsector : "fio_ofIndustry"
Fio-epa-frsSiteRecord ||--|o Bd7175f49ca206d160fdb4fee4dad2747 : "fio-epa-frs_ofInterestType"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsRadiationProtectionProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsEnforcementInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsGroundWaterProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsAssistanceSupportProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsCoastalOceanProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsHazardousWasteProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsSiteRecord ||--|o Bf500d8a8b0381e9decef451f20ba1677 : "fio-epa-frs_ofInterestType"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsReportingInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsAnimalOperation : "fio-epa-frs_ofInterestType"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsSolidWasteProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsComplianceInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsHealthSafetyProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsSiteInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsRemediationRedevelopmentProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsUndergroundStorageTankProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsDrinkingWaterProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsRegistryInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsSiteRecord ||--|o OwlThing : "fio-epa-frs_ofInterestType"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsWaterResourcesProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsChemicalReleaseProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsPermitInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsSiteRecord ||--|o RdfsResource : "fio-epa-frs_ofInterestType"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsAirProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsWasteWaterProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsPesticidesProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsRiskInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsEnvironmentalInterestByProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsLegalEnforcementActivities : "fio-epa-frs_ofInterestType"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsElectronicPermitSystem : "fio-epa-frs_ofInterestType"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsEnvironmentalInterestType : "fio-epa-frs_ofInterestType"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsFacilitySiteIdentification : "fio-epa-frs_ofInterestType"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsChemicalStorageProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsReportingRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsStateTrackingRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsTribalTrackingRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsSiteRecord ||--|o RdfsResource : "fio-epa-frs_hasRecord"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsPermitRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsRegistrationRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsSiteRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsEnforcementActivity : "fio-epa-frs_hasRecord"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsProjectRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsComplianceRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsRiskPlanRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsSiteRecord ||--|o OwlThing : "fio-epa-frs_hasRecord"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsEnforcementTrackingRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsSupplementalRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsSiteRecord ||--|o Fio-epa-frsFRS-Facility : "fio-epa-frs_hasRecord"
Fio-epa-frsSiteRecord ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsSiteRecord ||--|o NaicsNAICS-IndustryGroup : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsSiteRecord ||--|o RdfsResource : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsSiteRecord ||--|o NaicsNAICS-IndustrySector : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsSiteRecord ||--|o OwlNamedIndividual : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsSiteRecord ||--|o NaicsNAICS-IndustryCode : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsSiteRecord ||--|o OwlThing : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsSiteRecord ||--|o FioIndustry : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsSiteRecord ||--|o NaicsNAICS-IndustrySubsector : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsSiteSystem ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsSiteSystem ||--|o Fio-epa-frsPermitSystem : "fio-epa-frs_replacedBy"
Fio-epa-frsSiteSystem ||--|o Fio-epa-frsSiteSystem : "fio-epa-frs_replacedBy"
Fio-epa-frsSiteSystem ||--|o RdfsResource : "fio-epa-frs_replacedBy"
Fio-epa-frsSiteSystem ||--|o Fio-epa-frsProgramInformationSystem : "fio-epa-frs_replacedBy"
Fio-epa-frsSiteSystem ||--|o OwlThing : "fio-epa-frs_replacedBy"
Fio-epa-frsSiteSystem ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsSolidWasteProgram ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsSolidWasteProgram ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsStateSystem ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsStateSystem ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsReportingRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsStateTrackingRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsStateTrackingRecord ||--|o RdfsResource : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsPermitRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsSiteRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsRegistrationRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsEnforcementActivity : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsRiskPlanRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsStateTrackingRecord ||--|o OwlThing : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsEnforcementTrackingRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsSupplementalRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsFRS-Facility : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsStateTrackingRecord ||--|o RdfsLiteral : "dct_identifier"
Fio-epa-frsStateTrackingRecord ||--|o NaicsNAICS-IndustryGroup : "fio-epa-frs_ofSecondaryIndustry"
Fio-epa-frsStateTrackingRecord ||--|o RdfsResource : "fio-epa-frs_ofSecondaryIndustry"
Fio-epa-frsStateTrackingRecord ||--|o OwlNamedIndividual : "fio-epa-frs_ofSecondaryIndustry"
Fio-epa-frsStateTrackingRecord ||--|o NaicsNAICS-IndustryCode : "fio-epa-frs_ofSecondaryIndustry"
Fio-epa-frsStateTrackingRecord ||--|o OwlThing : "fio-epa-frs_ofSecondaryIndustry"
Fio-epa-frsStateTrackingRecord ||--|o FioIndustry : "fio-epa-frs_ofSecondaryIndustry"
Fio-epa-frsStateTrackingRecord ||--|o NaicsNAICS-IndustrySubsector : "fio-epa-frs_ofSecondaryIndustry"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsLegacySystem : "fio-epa-frs_fromSystem"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsPermitSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsStateSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsProjectSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsComplianceSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsSiteSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsStateTrackingRecord ||--|o RdfsResource : "fio-epa-frs_fromSystem"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsRegistrySystem : "fio-epa-frs_fromSystem"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsEnforcementSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsGrantSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsReportingSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsProgramInformationSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsTribalSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsStateTrackingRecord ||--|o OwlThing : "fio-epa-frs_fromSystem"
Fio-epa-frsStateTrackingRecord ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsStateTrackingRecord ||--|o Bd7175f49ca206d160fdb4fee4dad2747 : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsRadiationProtectionProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsEnforcementInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsGroundWaterProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsAssistanceSupportProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsCoastalOceanProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsHazardousWasteProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsStateTrackingRecord ||--|o Bf500d8a8b0381e9decef451f20ba1677 : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsReportingInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsAnimalOperation : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsSolidWasteProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsHealthSafetyProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsComplianceInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsSiteInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsRemediationRedevelopmentProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsChemicalStorageProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsUndergroundStorageTankProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsDrinkingWaterProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsRegistryInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsStateTrackingRecord ||--|o OwlThing : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsWaterResourcesProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsPermitInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsStateTrackingRecord ||--|o RdfsResource : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsAirProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsWasteWaterProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsPesticidesProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsRiskInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsEnvironmentalInterestByProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsLegalEnforcementActivities : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsElectronicPermitSystem : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsEnvironmentalInterestType : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsFacilitySiteIdentification : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsChemicalReleaseProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsStateTrackingRecord ||--|o NaicsNAICS-IndustryGroup : "fio_ofIndustry"
Fio-epa-frsStateTrackingRecord ||--|o RdfsResource : "fio_ofIndustry"
Fio-epa-frsStateTrackingRecord ||--|o NaicsNAICS-IndustrySector : "fio_ofIndustry"
Fio-epa-frsStateTrackingRecord ||--|o OwlNamedIndividual : "fio_ofIndustry"
Fio-epa-frsStateTrackingRecord ||--|o NaicsNAICS-IndustryCode : "fio_ofIndustry"
Fio-epa-frsStateTrackingRecord ||--|o OwlThing : "fio_ofIndustry"
Fio-epa-frsStateTrackingRecord ||--|o FioIndustry : "fio_ofIndustry"
Fio-epa-frsStateTrackingRecord ||--|o NaicsNAICS-IndustrySubsector : "fio_ofIndustry"
Fio-epa-frsStateTrackingRecord ||--|o Bd7175f49ca206d160fdb4fee4dad2747 : "fio-epa-frs_ofInterestType"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsRadiationProtectionProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsEnforcementInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsGroundWaterProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsAssistanceSupportProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsCoastalOceanProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsHazardousWasteProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsStateTrackingRecord ||--|o Bf500d8a8b0381e9decef451f20ba1677 : "fio-epa-frs_ofInterestType"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsReportingInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsAnimalOperation : "fio-epa-frs_ofInterestType"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsSolidWasteProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsComplianceInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsHealthSafetyProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsSiteInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsRemediationRedevelopmentProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsUndergroundStorageTankProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsDrinkingWaterProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsRegistryInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsStateTrackingRecord ||--|o OwlThing : "fio-epa-frs_ofInterestType"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsWaterResourcesProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsChemicalReleaseProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsPermitInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsStateTrackingRecord ||--|o RdfsResource : "fio-epa-frs_ofInterestType"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsAirProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsWasteWaterProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsPesticidesProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsRiskInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsEnvironmentalInterestByProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsLegalEnforcementActivities : "fio-epa-frs_ofInterestType"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsElectronicPermitSystem : "fio-epa-frs_ofInterestType"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsEnvironmentalInterestType : "fio-epa-frs_ofInterestType"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsFacilitySiteIdentification : "fio-epa-frs_ofInterestType"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsChemicalStorageProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsReportingRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsStateTrackingRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsTribalTrackingRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsStateTrackingRecord ||--|o RdfsResource : "fio-epa-frs_hasRecord"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsPermitRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsRegistrationRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsSiteRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsEnforcementActivity : "fio-epa-frs_hasRecord"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsProjectRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsComplianceRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsRiskPlanRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsStateTrackingRecord ||--|o OwlThing : "fio-epa-frs_hasRecord"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsEnforcementTrackingRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsSupplementalRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsStateTrackingRecord ||--|o Fio-epa-frsFRS-Facility : "fio-epa-frs_hasRecord"
Fio-epa-frsStateTrackingRecord ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsStateTrackingRecord ||--|o NaicsNAICS-IndustryGroup : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsStateTrackingRecord ||--|o RdfsResource : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsStateTrackingRecord ||--|o NaicsNAICS-IndustrySector : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsStateTrackingRecord ||--|o OwlNamedIndividual : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsStateTrackingRecord ||--|o NaicsNAICS-IndustryCode : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsStateTrackingRecord ||--|o OwlThing : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsStateTrackingRecord ||--|o FioIndustry : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsStateTrackingRecord ||--|o NaicsNAICS-IndustrySubsector : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsReportingRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsStateTrackingRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsSupplementalRecord ||--|o RdfsResource : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsPermitRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsSiteRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsRegistrationRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsEnforcementActivity : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsRiskPlanRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsSupplementalRecord ||--|o OwlThing : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsEnforcementTrackingRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsSupplementalRecord : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsFRS-Facility : "fio-epa-frs_hasSupplementalRecord"
Fio-epa-frsSupplementalRecord ||--|o RdfsLiteral : "dct_identifier"
Fio-epa-frsSupplementalRecord ||--|o NaicsNAICS-IndustryGroup : "fio-epa-frs_ofSecondaryIndustry"
Fio-epa-frsSupplementalRecord ||--|o RdfsResource : "fio-epa-frs_ofSecondaryIndustry"
Fio-epa-frsSupplementalRecord ||--|o OwlNamedIndividual : "fio-epa-frs_ofSecondaryIndustry"
Fio-epa-frsSupplementalRecord ||--|o NaicsNAICS-IndustryCode : "fio-epa-frs_ofSecondaryIndustry"
Fio-epa-frsSupplementalRecord ||--|o OwlThing : "fio-epa-frs_ofSecondaryIndustry"
Fio-epa-frsSupplementalRecord ||--|o FioIndustry : "fio-epa-frs_ofSecondaryIndustry"
Fio-epa-frsSupplementalRecord ||--|o NaicsNAICS-IndustrySubsector : "fio-epa-frs_ofSecondaryIndustry"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsLegacySystem : "fio-epa-frs_fromSystem"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsPermitSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsStateSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsProjectSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsComplianceSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsSiteSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsSupplementalRecord ||--|o RdfsResource : "fio-epa-frs_fromSystem"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsRegistrySystem : "fio-epa-frs_fromSystem"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsEnforcementSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsGrantSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsReportingSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsProgramInformationSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsTribalSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsSupplementalRecord ||--|o OwlThing : "fio-epa-frs_fromSystem"
Fio-epa-frsSupplementalRecord ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsSupplementalRecord ||--|o Bd7175f49ca206d160fdb4fee4dad2747 : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsRadiationProtectionProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsEnforcementInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsGroundWaterProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsAssistanceSupportProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsCoastalOceanProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsHazardousWasteProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSupplementalRecord ||--|o Bf500d8a8b0381e9decef451f20ba1677 : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsReportingInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsAnimalOperation : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsSolidWasteProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsHealthSafetyProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsComplianceInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsSiteInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsRemediationRedevelopmentProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsChemicalStorageProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsUndergroundStorageTankProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsDrinkingWaterProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsRegistryInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSupplementalRecord ||--|o OwlThing : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsWaterResourcesProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsPermitInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSupplementalRecord ||--|o RdfsResource : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsAirProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsWasteWaterProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsPesticidesProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsRiskInterest : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsEnvironmentalInterestByProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsLegalEnforcementActivities : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsElectronicPermitSystem : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsEnvironmentalInterestType : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsFacilitySiteIdentification : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsChemicalReleaseProgram : "fio-epa-frs_hasEnvironmentalInterest"
Fio-epa-frsSupplementalRecord ||--|o NaicsNAICS-IndustryGroup : "fio_ofIndustry"
Fio-epa-frsSupplementalRecord ||--|o RdfsResource : "fio_ofIndustry"
Fio-epa-frsSupplementalRecord ||--|o NaicsNAICS-IndustrySector : "fio_ofIndustry"
Fio-epa-frsSupplementalRecord ||--|o OwlNamedIndividual : "fio_ofIndustry"
Fio-epa-frsSupplementalRecord ||--|o NaicsNAICS-IndustryCode : "fio_ofIndustry"
Fio-epa-frsSupplementalRecord ||--|o OwlThing : "fio_ofIndustry"
Fio-epa-frsSupplementalRecord ||--|o FioIndustry : "fio_ofIndustry"
Fio-epa-frsSupplementalRecord ||--|o NaicsNAICS-IndustrySubsector : "fio_ofIndustry"
Fio-epa-frsSupplementalRecord ||--|o Bd7175f49ca206d160fdb4fee4dad2747 : "fio-epa-frs_ofInterestType"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsRadiationProtectionProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsEnforcementInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsGroundWaterProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsAssistanceSupportProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsCoastalOceanProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsHazardousWasteProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsSupplementalRecord ||--|o Bf500d8a8b0381e9decef451f20ba1677 : "fio-epa-frs_ofInterestType"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsReportingInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsAnimalOperation : "fio-epa-frs_ofInterestType"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsSolidWasteProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsComplianceInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsHealthSafetyProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsSiteInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsRemediationRedevelopmentProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsUndergroundStorageTankProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsDrinkingWaterProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsRegistryInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsSupplementalRecord ||--|o OwlThing : "fio-epa-frs_ofInterestType"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsWaterResourcesProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsChemicalReleaseProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsPermitInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsSupplementalRecord ||--|o RdfsResource : "fio-epa-frs_ofInterestType"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsAirProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsWasteWaterProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsPesticidesProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsRiskInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsEnvironmentalInterestByProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsLegalEnforcementActivities : "fio-epa-frs_ofInterestType"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsElectronicPermitSystem : "fio-epa-frs_ofInterestType"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsEnvironmentalInterestType : "fio-epa-frs_ofInterestType"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsFacilitySiteIdentification : "fio-epa-frs_ofInterestType"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsChemicalStorageProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsReportingRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsStateTrackingRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsTribalTrackingRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsSupplementalRecord ||--|o RdfsResource : "fio-epa-frs_hasRecord"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsPermitRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsRegistrationRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsSiteRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsEnforcementActivity : "fio-epa-frs_hasRecord"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsProjectRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsComplianceRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsRiskPlanRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsSupplementalRecord ||--|o OwlThing : "fio-epa-frs_hasRecord"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsEnforcementTrackingRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsSupplementalRecord : "fio-epa-frs_hasRecord"
Fio-epa-frsSupplementalRecord ||--|o Fio-epa-frsFRS-Facility : "fio-epa-frs_hasRecord"
Fio-epa-frsSupplementalRecord ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsSupplementalRecord ||--|o NaicsNAICS-IndustryGroup : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsSupplementalRecord ||--|o RdfsResource : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsSupplementalRecord ||--|o NaicsNAICS-IndustrySector : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsSupplementalRecord ||--|o OwlNamedIndividual : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsSupplementalRecord ||--|o NaicsNAICS-IndustryCode : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsSupplementalRecord ||--|o OwlThing : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsSupplementalRecord ||--|o FioIndustry : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsSupplementalRecord ||--|o NaicsNAICS-IndustrySubsector : "fio-epa-frs_ofPrimaryIndustry"
Fio-epa-frsTribalSystem ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsTribalSystem ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsTribalTrackingRecord ||--|o RdfsLiteral : "dct_identifier"
Fio-epa-frsTribalTrackingRecord ||--|o Fio-epa-frsLegacySystem : "fio-epa-frs_fromSystem"
Fio-epa-frsTribalTrackingRecord ||--|o Fio-epa-frsPermitSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsTribalTrackingRecord ||--|o Fio-epa-frsStateSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsTribalTrackingRecord ||--|o Fio-epa-frsProjectSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsTribalTrackingRecord ||--|o Fio-epa-frsComplianceSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsTribalTrackingRecord ||--|o Fio-epa-frsSiteSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsTribalTrackingRecord ||--|o RdfsResource : "fio-epa-frs_fromSystem"
Fio-epa-frsTribalTrackingRecord ||--|o Fio-epa-frsRegistrySystem : "fio-epa-frs_fromSystem"
Fio-epa-frsTribalTrackingRecord ||--|o Fio-epa-frsEnforcementSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsTribalTrackingRecord ||--|o Fio-epa-frsGrantSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsTribalTrackingRecord ||--|o Fio-epa-frsReportingSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsTribalTrackingRecord ||--|o Fio-epa-frsProgramInformationSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsTribalTrackingRecord ||--|o Fio-epa-frsTribalSystem : "fio-epa-frs_fromSystem"
Fio-epa-frsTribalTrackingRecord ||--|o OwlThing : "fio-epa-frs_fromSystem"
Fio-epa-frsTribalTrackingRecord ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsTribalTrackingRecord ||--|o Bd7175f49ca206d160fdb4fee4dad2747 : "fio-epa-frs_ofInterestType"
Fio-epa-frsTribalTrackingRecord ||--|o Fio-epa-frsRadiationProtectionProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsTribalTrackingRecord ||--|o Fio-epa-frsEnforcementInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsTribalTrackingRecord ||--|o Fio-epa-frsGroundWaterProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsTribalTrackingRecord ||--|o Fio-epa-frsAssistanceSupportProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsTribalTrackingRecord ||--|o Fio-epa-frsCoastalOceanProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsTribalTrackingRecord ||--|o Fio-epa-frsHazardousWasteProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsTribalTrackingRecord ||--|o Bf500d8a8b0381e9decef451f20ba1677 : "fio-epa-frs_ofInterestType"
Fio-epa-frsTribalTrackingRecord ||--|o Fio-epa-frsReportingInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsTribalTrackingRecord ||--|o Fio-epa-frsAnimalOperation : "fio-epa-frs_ofInterestType"
Fio-epa-frsTribalTrackingRecord ||--|o Fio-epa-frsSolidWasteProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsTribalTrackingRecord ||--|o Fio-epa-frsComplianceInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsTribalTrackingRecord ||--|o Fio-epa-frsHealthSafetyProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsTribalTrackingRecord ||--|o Fio-epa-frsSiteInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsTribalTrackingRecord ||--|o Fio-epa-frsRemediationRedevelopmentProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsTribalTrackingRecord ||--|o Fio-epa-frsUndergroundStorageTankProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsTribalTrackingRecord ||--|o Fio-epa-frsDrinkingWaterProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsTribalTrackingRecord ||--|o Fio-epa-frsRegistryInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsTribalTrackingRecord ||--|o OwlThing : "fio-epa-frs_ofInterestType"
Fio-epa-frsTribalTrackingRecord ||--|o Fio-epa-frsWaterResourcesProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsTribalTrackingRecord ||--|o Fio-epa-frsChemicalReleaseProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsTribalTrackingRecord ||--|o Fio-epa-frsPermitInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsTribalTrackingRecord ||--|o RdfsResource : "fio-epa-frs_ofInterestType"
Fio-epa-frsTribalTrackingRecord ||--|o Fio-epa-frsAirProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsTribalTrackingRecord ||--|o Fio-epa-frsWasteWaterProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsTribalTrackingRecord ||--|o Fio-epa-frsPesticidesProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsTribalTrackingRecord ||--|o Fio-epa-frsRiskInterest : "fio-epa-frs_ofInterestType"
Fio-epa-frsTribalTrackingRecord ||--|o Fio-epa-frsEnvironmentalInterestByProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsTribalTrackingRecord ||--|o Fio-epa-frsLegalEnforcementActivities : "fio-epa-frs_ofInterestType"
Fio-epa-frsTribalTrackingRecord ||--|o Fio-epa-frsElectronicPermitSystem : "fio-epa-frs_ofInterestType"
Fio-epa-frsTribalTrackingRecord ||--|o Fio-epa-frsEnvironmentalInterestType : "fio-epa-frs_ofInterestType"
Fio-epa-frsTribalTrackingRecord ||--|o Fio-epa-frsFacilitySiteIdentification : "fio-epa-frs_ofInterestType"
Fio-epa-frsTribalTrackingRecord ||--|o Fio-epa-frsChemicalStorageProgram : "fio-epa-frs_ofInterestType"
Fio-epa-frsTribalTrackingRecord ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsUndergroundStorageTankProgram ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsUndergroundStorageTankProgram ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsWasteWaterProgram ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsWasteWaterProgram ||--|o OwlThing : "owl_sameAs"
Fio-epa-frsWaterResourcesProgram ||--|o RdfsLiteral : "rdfs_label"
Fio-epa-frsWaterResourcesProgram ||--|o OwlThing : "owl_sameAs"
FioIndustry ||--|o OwlThing : "owl_sameAs"
KwgoS2CellLevel13 ||--|o OwlThing : "owl_sameAs"
KwgoS2CellLevel13 ||--|o Fio-epa-frsEPA-PFAS-Facility : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o KwgoAdministrativeRegion3 : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o KwgoRegion : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o RdfsResource : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o KwgoAdministrativeRegion : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o KwgoS2CellLevel13 : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o GeoSpatialObject : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o OwlThing : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o KwgoAdministrativeRegion2 : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o Fio-epa-frsFRS-Facility : "spatial_connectedTo"
KwgoS2CellLevel13 ||--|o Fio-epa-frsEPA-PFAS-Facility : "spatial_spatiallyRelatedTo"
KwgoS2CellLevel13 ||--|o KwgoAdministrativeRegion3 : "spatial_spatiallyRelatedTo"
KwgoS2CellLevel13 ||--|o KwgoRegion : "spatial_spatiallyRelatedTo"
KwgoS2CellLevel13 ||--|o RdfsResource : "spatial_spatiallyRelatedTo"
KwgoS2CellLevel13 ||--|o KwgoAdministrativeRegion : "spatial_spatiallyRelatedTo"
KwgoS2CellLevel13 ||--|o KwgoS2CellLevel13 : "spatial_spatiallyRelatedTo"
KwgoS2CellLevel13 ||--|o GeoSpatialObject : "spatial_spatiallyRelatedTo"
KwgoS2CellLevel13 ||--|o OwlThing : "spatial_spatiallyRelatedTo"
KwgoS2CellLevel13 ||--|o KwgoAdministrativeRegion2 : "spatial_spatiallyRelatedTo"
KwgoS2CellLevel13 ||--|o Fio-epa-frsFRS-Facility : "spatial_spatiallyRelatedTo"
NaicsNAICS-IndustryCode ||--|o RdfsLiteral : "dct_identifier"
NaicsNAICS-IndustryCode ||--|o OwlThing : "owl_sameAs"
NaicsNAICS-IndustryCode ||--|o NaicsNAICS-IndustryGroup : "fio_subcodeOf"
NaicsNAICS-IndustryCode ||--|o RdfsResource : "fio_subcodeOf"
NaicsNAICS-IndustryCode ||--|o NaicsNAICS-IndustrySector : "fio_subcodeOf"
NaicsNAICS-IndustryCode ||--|o OwlNamedIndividual : "fio_subcodeOf"
NaicsNAICS-IndustryCode ||--|o NaicsNAICS-IndustryCode : "fio_subcodeOf"
NaicsNAICS-IndustryCode ||--|o OwlThing : "fio_subcodeOf"
NaicsNAICS-IndustryCode ||--|o FioIndustry : "fio_subcodeOf"
NaicsNAICS-IndustryCode ||--|o NaicsNAICS-IndustrySubsector : "fio_subcodeOf"
NaicsNAICS-IndustryCode ||--|o XsdGYear : "fio_ofYear"
NaicsNAICS-IndustryCode ||--|o RdfsLiteral : "rdfs_label"
NaicsNAICS-IndustryGroup ||--|o RdfsLiteral : "dct_identifier"
NaicsNAICS-IndustryGroup ||--|o OwlThing : "owl_sameAs"
NaicsNAICS-IndustryGroup ||--|o NaicsNAICS-IndustryGroup : "fio_subcodeOf"
NaicsNAICS-IndustryGroup ||--|o RdfsResource : "fio_subcodeOf"
NaicsNAICS-IndustryGroup ||--|o NaicsNAICS-IndustrySector : "fio_subcodeOf"
NaicsNAICS-IndustryGroup ||--|o OwlNamedIndividual : "fio_subcodeOf"
NaicsNAICS-IndustryGroup ||--|o NaicsNAICS-IndustryCode : "fio_subcodeOf"
NaicsNAICS-IndustryGroup ||--|o OwlThing : "fio_subcodeOf"
NaicsNAICS-IndustryGroup ||--|o FioIndustry : "fio_subcodeOf"
NaicsNAICS-IndustryGroup ||--|o NaicsNAICS-IndustrySubsector : "fio_subcodeOf"
NaicsNAICS-IndustryGroup ||--|o XsdGYear : "fio_ofYear"
NaicsNAICS-IndustryGroup ||--|o RdfsLiteral : "rdfs_label"
NaicsNAICS-IndustrySector ||--|o RdfsLiteral : "dct_identifier"
NaicsNAICS-IndustrySector ||--|o XsdGYear : "fio_ofYear"
NaicsNAICS-IndustrySector ||--|o RdfsLiteral : "rdfs_label"
NaicsNAICS-IndustrySector ||--|o OwlThing : "owl_sameAs"
NaicsNAICS-IndustrySubsector ||--|o RdfsLiteral : "dct_identifier"
NaicsNAICS-IndustrySubsector ||--|o OwlThing : "owl_sameAs"
NaicsNAICS-IndustrySubsector ||--|o NaicsNAICS-IndustryGroup : "fio_subcodeOf"
NaicsNAICS-IndustrySubsector ||--|o RdfsResource : "fio_subcodeOf"
NaicsNAICS-IndustrySubsector ||--|o NaicsNAICS-IndustrySector : "fio_subcodeOf"
NaicsNAICS-IndustrySubsector ||--|o OwlNamedIndividual : "fio_subcodeOf"
NaicsNAICS-IndustrySubsector ||--|o NaicsNAICS-IndustryCode : "fio_subcodeOf"
NaicsNAICS-IndustrySubsector ||--|o OwlThing : "fio_subcodeOf"
NaicsNAICS-IndustrySubsector ||--|o FioIndustry : "fio_subcodeOf"
NaicsNAICS-IndustrySubsector ||--|o NaicsNAICS-IndustrySubsector : "fio_subcodeOf"
NaicsNAICS-IndustrySubsector ||--|o XsdGYear : "fio_ofYear"
NaicsNAICS-IndustrySubsector ||--|o RdfsLiteral : "rdfs_label"

```



## Imports


* okns:time
* okns:sdo
* okns:prov
* okns:owl-rdf-rdfs
* linkml:types
* okns:extended_types
* okns:kwg
* okns:geo
* okns:dc



## Classes

| Class | Description | Occurrences |
| --- | --- | --- |
| [Bd7175f49ca206d160fdb4fee4dad2747](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Bd7175f49ca206d160fdb4fee4dad2747.md) | None<br/>| 7 | 
| [Bf500d8a8b0381e9decef451f20ba1677](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Bf500d8a8b0381e9decef451f20ba1677.md) | None<br/>| 7 | 
| [OwlThing](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/OwlThing.md) | The class of OWL individuals.<br/>| 922366 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsAirProgram](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsAirProgram.md) | ENVIRONMENTAL PROGRAMS THAT REGULATE OR MONITOR AIR EMISSIONS FROM AREA, STATIONARY, AND MOBILE SOURCES, AS REQUIRED BY THE CLEAN AIR ACT<br/>| 34 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsAnimalOperation](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsAnimalOperation.md) | ENVIRONMENTAL PROGRAMS RELATED TO ANIMAL OPERATIONS E.G LIVESTOCK WASTE CONTROL<br/>| 4 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsAssistanceSupportProgram](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsAssistanceSupportProgram.md) | ENVIRONMENTAL PROGRAMS THAT PROVIDE ASSISTANCE TO THE REGULATED COMMUNITY AND THE GENERAL PUBLIC (E.G., ENVIRONMENTAL GRANTS, OUTREACH ACTIVITIES) OR ACTIVITIES THAT PROVIDE SUPPORT ACROSS ENVIRONMENTAL PROGRAMS.<br/>| 6 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsChemicalReleaseProgram](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsChemicalReleaseProgram.md) | ENVIRONMENTAL PROGRAMS THAT REGULATE OR MONITOR CHEMICALS RELEASED TO THE ENVIRONMENT (E.G., TOXIC RELEASE INVENTORY, RELEASE ASSESSMENTS).<br/>| 3 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsChemicalStorageProgram](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsChemicalStorageProgram.md) | ENVIRONMENTAL PROGRAMS THAT REGULATE OR MONITOR THE STORAGE OF CHEMICALS (E.G., RISK MANAGEMENT PROGRAM, SUPERFUND AMENDMENTS AND REAUTHORIZATION ACT (SARA) TITLE III PROGRAM).<br/>| 5 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsChemicalstorageprograms](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsChemicalstorageprograms.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsCoastalOceanProgram](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsCoastalOceanProgram.md) | ENVIRONMENTAL PROGRAMS THAT IMPROVE THE QUALITY OF COASTAL AND MARINE ECOSYSTEMS AND PROTECT BEACHES, COAST, AND OCEAN RESOURCES FROM POLLUTION.<br/>| 2 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsComplianceInterest](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsComplianceInterest.md) | None<br/>| 2 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsComplianceRecord](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsComplianceRecord.md) | None<br/>| 34710 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsComplianceSystem](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsComplianceSystem.md) | None<br/>| 3 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsDrinkingWaterProgram](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsDrinkingWaterProgram.md) | ENVIRONMENTAL PROGRAMS THAT PROTECT THE QUALITY OF DRINKING WATER IN THE UNITED STATES, AS REQUIRED BY THE SAFE DRINKING WATER ACT.<br/>| 5 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsEcologyOperation](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsEcologyOperation.md) | PROGRAMS THAT CONCENTRATE ON ECOLOGICAL SYSTEMS SUCH AS FOREST AND TREE EXPERTISE<br/>| 2 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsElectronicPermitSystem](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsElectronicPermitSystem.md) | ELECTRONIC PERMIT SYSTEM<br/>| 8 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsEnforcementActivity](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsEnforcementActivity.md) | A record that tracks a specific legal, corrective or assistance action taken against a facility<br/>| 23487 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsEnforcementInterest](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsEnforcementInterest.md) | None<br/>| 5 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsEnforcementSystem](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsEnforcementSystem.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsEnforcementTrackingRecord](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsEnforcementTrackingRecord.md) | None<br/>| 102720 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsEnvironmentalInterestByProgram](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsEnvironmentalInterestByProgram.md) | None<br/>| 7 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsEnvironmentalInterestByRecordType](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsEnvironmentalInterestByRecordType.md) | Interest classification based on the main subject of the record and what type of activity or entity it identifies.<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsEnvironmentalInterestType](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsEnvironmentalInterestType.md) | The environmental permit or regulatory program type that applies to the facility site<br/>| 24 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsEPA-PFAS-Facility](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsEPA-PFAS-Facility.md) | Facility identified as potentially handling PFAS in EPA PFAS Analytic tools based on industry.<br/>| 31147 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsFacilitySiteIdentification](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsFacilitySiteIdentification.md) | INCLUDES SYSTEMS THAT MAINTAIN BASIC IDENTIFICATION INFORMATION ABOUT FACILITIES/SITES AND LINKAGES TO ENVIRONMENTAL PERMITS AND PROGRAMS AT THE STATE, TRIBAL AND NATIONAL LEVEL.<br/>| 3 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsFacilityType](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsFacilityType.md) | Type of Facility as defined by EPA FRS facility type controlled vocabulary<br/>| 15 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsFRS-Facility](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsFRS-Facility.md) | Facility from EPA Facility Registry Service<br/>| 1299140 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsGrantSystem](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsGrantSystem.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsGroundWaterProgram](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsGroundWaterProgram.md) | ENVIRONMENTAL PROGRAMS DESIGNED TO PROTECT GROUND WATER (E.G., UNDERGROUND INJECTION CONTROL (UIC),  MINERAL EXPLORATION).<br/>| 4 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsHazardousWasteProgram](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsHazardousWasteProgram.md) | ENVIRONMENTAL PROGRAMS THAT REGULATE HAZARDOUS WASTE, INCLUDING THE GENERATION, TRANSPORTATION, TREATMENT, STORAGE, AND DISPOSAL OF HAZARDOUS WASTE, AS REQUIRED BY THE RESOURCE CONSERVATION AND RECOVERY ACT (RCRA).<br/>| 23 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsHealthSafetyProgram](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsHealthSafetyProgram.md) | PROGRAMS DESIGNED TO REDUCE HAZARDS AND PREVENT INJURIES, ILLNESSES AND DEATHS IN THE WORKPLACE.<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsLegacySystem](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsLegacySystem.md) | None<br/>| 3 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsLegalEnforcementActivities](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsLegalEnforcementActivities.md) | LEGAL OR ENFORCEMENT ACTIVITIES IN SUPPORT OF OTHER ENVIRONMENTAL PROGRAMS.<br/>| 5 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsMonitoringRecord](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsMonitoringRecord.md) | A record that monitors a facility on an ongoing basis<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsPermitInterest](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsPermitInterest.md) | Environmental Interests that create records that are permits or licenses<br/>| 16 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsPermitRecord](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsPermitRecord.md) | A record that tracks a permit or license awarded to the facility<br/>| 293732 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsPermitSystem](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsPermitSystem.md) | None<br/>| 3 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsPesticidesProgram](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsPesticidesProgram.md) | ENVIRONMENTAL PROGRAMS THAT MONITOR BUSINESSES, GOVERNMENT AGENCIES, AND INDIVIDUALS THAT HANDLE, STORE, SELL, AND/OR APPLY PESITICIDES.<br/>| 5 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsProgramInformationSystem](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsProgramInformationSystem.md) | An Information System maintained for an environmental program<br/>| 10 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsProjectRecord](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsProjectRecord.md) | None<br/>| 562 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsProjectSystem](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsProjectSystem.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsRadiationProtectionProgram](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsRadiationProtectionProgram.md) | ENVIRONMENTAL PROGRAMS DESIGNED TO PROTECT PEOPLE AND THE ENVIRONMENT FROM HARMFUL EXPOSURE TO RADIATION<br/>| 7 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsRecord](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsRecord.md) | None<br/>| 282215 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsRegistrationRecord](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsRegistrationRecord.md) | None<br/>| 42472 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsRegistryInterest](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsRegistryInterest.md) | None<br/>| 4 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsRegistrySystem](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsRegistrySystem.md) | None<br/>| 3 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsRemediationRedevelopmentProgram](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsRemediationRedevelopmentProgram.md) | ENVIRONMENTAL PROGRAMS AIMED AT CLEANING UP AND/OR REDEVELOPING UNCONTROLLED OR ABANDONED PLACES WHERE HAZARDOUS WASTE MAY BE LOCATED POSSIBLY AFFECTING LOCAL ECOSYSTEMS OR PEOPLE.<br/>| 17 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsReportingInterest](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsReportingInterest.md) | None<br/>| 6 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsReportingRecord](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsReportingRecord.md) | None<br/>| 487387 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsReportingSystem](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsReportingSystem.md) | None<br/>| 21 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsRiskInterest](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsRiskInterest.md) | None<br/>| 4 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsRiskPlanRecord](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsRiskPlanRecord.md) | None<br/>| 13687 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsSiteInterest](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsSiteInterest.md) | None<br/>| 16 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsSiteRecord](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsSiteRecord.md) | A record that monitors a site, beyond specific ownership of one organization and their activities, e.g. superfund site, air monitoring site<br/>| 35428 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsSiteSystem](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsSiteSystem.md) | None<br/>| 7 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsSolidWasteProgram](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsSolidWasteProgram.md) | ENVIRONMENTAL PROGRAMS THAT REGULATE SOLID WASTES (E.G., COMPOST SITES, LANDFILLS, TRANSFER STATIONS).<br/>| 17 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsStateSystem](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsStateSystem.md) | None<br/>| 48 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsStateTrackingRecord](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsStateTrackingRecord.md) | None<br/>| 461681 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsStationSystem](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsStationSystem.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsSupplementalRecord](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsSupplementalRecord.md) | Supplemental Record that relates to a facility but primarily identifies something other than the facility itself (e.g. permit, license, incident, enforcement action records)<br/>| 211436 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsTribalSystem](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsTribalSystem.md) | None<br/>| 6 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsTribalTrackingRecord](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsTribalTrackingRecord.md) | None<br/>| 80 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsUndergroundStorageTankProgram](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsUndergroundStorageTankProgram.md) | ENVIRONMENTAL PROGRAMS DESIGNED TO REDUCE THE CHANCE OF RELEASES FROM UNDERGROUND STORAGE TANKS (USTS), DETECT LEAKS AND SPILLS WHEN THEY DO OCCUR, AND SECURE PROMPT CLEANUP<br/>| 3 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsWasteWaterProgram](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsWasteWaterProgram.md) | ENVIRONMENTAL PROGRAMS THAT REGULATE DISCHARGES OF POLLUTANTS TO WATERS OF THE UNITED STATES, AS REQUIRED BY THE CLEAN WATER ACT.<br/>| 29 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsWaterResourcesProgram](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsWaterResourcesProgram.md) | ENVIRONMENTAL PROGRAMS THAT MANAGE WATER RESOURCES TO MEET THE NEEDS OF THE NATURAL ENVIRONMENT AND HUMAN COMMUNITIES, INCLUDING WATERSHED MANAGEMENT, STREAM FLOWS, WATER RIGHTS, WELL DRILLING, USE OF WATER SUPPLIES, AND DAM SAFETY.<br/>| 4 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[FioFacility](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/FioFacility.md) | Any physical building, building complex or site (e.g. an airstrip, a mine, or superfund site) at which a commercial or institutional activity occurs.<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[FioIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/FioIndustry.md) | A distinct group of productive or profit-making enterprises.<br/>| 1297 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[KwgoS2CellLevel13](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/KwgoS2CellLevel13.md) | None<br/>| 249509 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[KwgoStatisticalArea](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/KwgoStatisticalArea.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[NaicsNAICS-Industry](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/NaicsNAICS-Industry.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[NaicsNAICS-IndustryCode](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/NaicsNAICS-IndustryCode.md) | None<br/>| 1701 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[NaicsNAICS-IndustryGroup](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/NaicsNAICS-IndustryGroup.md) | None<br/>| 308 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[NaicsNAICS-IndustrySector](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/NaicsNAICS-IndustrySector.md) | None<br/>| 24 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[NaicsNAICS-IndustrySubsector](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/NaicsNAICS-IndustrySubsector.md) | None<br/>| 96 | 
| [ProvAgent](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/ProvAgent.md) | An agent is something that bears some form of responsibility for an activity taking place, for the existence of an entity, or for another agent's activity.<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsAgency](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsAgency.md) | Federal Agency as identified in EPA Facility Registry Service<br/>| 54 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsAgency.Agriculture](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsAgency.Agriculture.md) | None<br/>| 10 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsAgency.Commerce](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsAgency.Commerce.md) | None<br/>| 6 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsAgency.Congress](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsAgency.Congress.md) | None<br/>| 3 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsAgency.Defense](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsAgency.Defense.md) | None<br/>| 19 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsAgency.Energy](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsAgency.Energy.md) | None<br/>| 27 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsAgency.HealthandHumanServices](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsAgency.HealthandHumanServices.md) | None<br/>| 6 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsAgency.HomelandSecurity](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsAgency.HomelandSecurity.md) | None<br/>| 11 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsAgency.HousingandUrbanDevelopment](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsAgency.HousingandUrbanDevelopment.md) | None<br/>| 2 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsAgency.Interior](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsAgency.Interior.md) | None<br/>| 10 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsAgency.Judicial](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsAgency.Judicial.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsAgency.Justice](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsAgency.Justice.md) | None<br/>| 6 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsAgency.Labor](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsAgency.Labor.md) | None<br/>| 4 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsAgency.State](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsAgency.State.md) | None<br/>| 3 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsAgency.Transportation](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsAgency.Transportation.md) | None<br/>| 10 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsAgency.Treasury](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsAgency.Treasury.md) | None<br/>| 4 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Fio-epa-frsAgency.VeteransAffairs](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/Fio-epa-frsAgency.VeteransAffairs.md) | None<br/>| 3 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[FioOrganization](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/classes/FioOrganization.md) | <br/>|  | 





## Slots

| Slot | Description | Occurrences |
| --- | --- | --- |
| [dct_decription](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/slots/dct_decription.md) | <br/>|  |
| [dct_decscription](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/slots/dct_decscription.md) | <br/>|  |
| [fio_epa_frs_fromSystem](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/slots/fio_epa_frs_fromSystem.md) | <br/>| 2303313 |
| [fio_epa_frs_hasEnvironmentalInterest](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/slots/fio_epa_frs_hasEnvironmentalInterest.md) | <br/>| 1785047 |
| [fio_epa_frs_hasFRSId](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/slots/fio_epa_frs_hasFRSId.md) | has Identifier in EPA Facility Registry Service<br/>| 918005 |
| [fio_epa_frs_hasMonitoringRecord](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/slots/fio_epa_frs_hasMonitoringRecord.md) | <br/>|  |
| [fio_epa_frs_hasRecord](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/slots/fio_epa_frs_hasRecord.md) | <br/>| 2635271 |
| [fio_epa_frs_hasSupplementalRecord](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/slots/fio_epa_frs_hasSupplementalRecord.md) | <br/>| 720516 |
| [fio_epa_frs_ofFacilityType](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/slots/fio_epa_frs_ofFacilityType.md) | <br/>| 2517791 |
| [fio_epa_frs_ofInterestType](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/slots/fio_epa_frs_ofInterestType.md) | <br/>| 2027729 |
| [fio_epa_frs_ofPrimaryIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/slots/fio_epa_frs_ofPrimaryIndustry.md) | <br/>| 270322 |
| [fio_epa_frs_ofSecondaryIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/slots/fio_epa_frs_ofSecondaryIndustry.md) | <br/>| 20320 |
| [fio_epa_frs_partOf](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/slots/fio_epa_frs_partOf.md) | <br/>| 3 |
| [fio_epa_frs_replacedBy](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/slots/fio_epa_frs_replacedBy.md) | <br/>| 4 |
| [fio_hasFacility](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/slots/fio_hasFacility.md) | <br/>|  |
| [fio_ofIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/slots/fio_ofIndustry.md) | A relation between an entity and the industry it is classified under<br/>| 2113938 |
| [fio_ofYear](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/slots/fio_ofYear.md) | A relation between an industry code and the schema year it belongs to<br/>| 2129 |
| [fio_ownedBy](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/slots/fio_ownedBy.md) | <br/>| 2018 |
| [fio_sameCode](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/slots/fio_sameCode.md) | <br/>|  |
| [fio_subcodeOf](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/slots/fio_subcodeOf.md) | A hierarchical relation between an industry and its parent industry<br/>| 7847 |
| [fio_yearDeprecated](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/slots/fio_yearDeprecated.md) | A relation between an industry code and the schema year it was deprecated and...<br/>|  |
| [http___proton.semanticweb.org_protonsys#transitiveOver](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/slots/http___proton.semanticweb.org_protonsys#transitiveOver.md) | <br/>|  |
| [kwgo_administrativePartOf](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/slots/kwgo_administrativePartOf.md) | <br/>|  |
| [skos_description](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/slots/skos_description.md) | <br/>|  |
| [spatial_connectedTo](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/slots/spatial_connectedTo.md) | <br/>| 4315928 |
| [spatial_spatiallyRelatedTo](https://github.com/frink-okn/graph-descriptions/blob/main/fio-kg/slots/spatial_spatiallyRelatedTo.md) | <br/>| 4315928 |









## IRI prefixes

* dc: http://purl.org/dc/elements/1.1/
* dcgeoid: https://datacommons.org/browser/geoId/
* dct: http://purl.org/dc/terms/
* fio: http://w3id.org/fio/v1/fio#
* fio-epa-frs: http://w3id.org/fio/v1/epa-frs#
* fio-epa-frs-data: http://w3id.org/fio/v1/epa-frs-data#
* geo: http://www.opengis.net/ont/geosparql#
* kwgo: http://stko-kwg.geog.ucsb.edu/lod/ontology/
* kwgr: http://stko-kwg.geog.ucsb.edu/lod/resource/
* linkml: https://w3id.org/linkml/
* naics: http://w3id.org/fio/v1/naics#
* okn: https://purl.org/okn/
* okns: https://purl.org/okn/schema/
* owl: http://www.w3.org/2002/07/owl#
* prov: http://www.w3.org/ns/prov#
* rdf: http://www.w3.org/1999/02/22-rdf-syntax-ns#
* rdfs: http://www.w3.org/2000/01/rdf-schema#
* sdos: https://schema.org/
* skos: http://www.w3.org/2004/02/skos/core#
* spatial: http://purl.org/spatialai/spatial/spatial-full#
* xsd: http://www.w3.org/2001/XMLSchema#
