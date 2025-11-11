# sudokn

SUDOKN Ontology is developed at the Semantic Computing Lab at Arizona State University. SUDOKN provides the necessary semantics for describing the capabilities of manufacturing companies. SUDOKN uses BFO as the top-level ontology and IOF Core and IOF Supply Chain as the mid-level ontologies



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
IoCapability {

}
IoGroupOfPersons {

}
IoIdentifier {

}
IoInformationContentEntity {

}
IoManufacturer {
    string sudokn_hasOrganizationYearOfEstablishment  
    uri sudokn_hasPostalAddress  
    int32 sudokn_hasNumberOfEmployees  
    string rdfs_label  
}
IoMaterialProduct {
    string rdfs_label  
}
IoOrganization {

}
IoPhysicalLocationIdentifier {

}
IoscGeospatialSite {

}
IoscIndustry {

}
IoscProductionCapability {

}
OboBFO0000019 {

}
OboBFO0000029 {

}
Sudokn2-AxisCNCTurningCapability {
    string rdfs_label  
}
Sudokn3DPrintingCapability {
    string rdfs_label  
}
SudoknAICS336999 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknAS9000Certificate {
    string rdfs_label  
}
SudoknAS9003Certificate {

}
SudoknAS9100 {
    string rdfs_label  
}
SudoknAS9100Certificate {
    string rdfs_label  
}
SudoknAS9102Certificate {
    string rdfs_label  
}
SudoknAS9120Certificate {

}
SudoknASCertificate {

}
SudoknASME {
    string rdfs_label  
}
SudoknASMECertificate {
    string rdfs_label  
}
SudoknAWSWelderCertificate {
    string rdfs_label  
}
SudoknAbrasiveCleaningCapability {
    string rdfs_label  
}
SudoknAbrassiveMachiningCapability {
    string rdfs_label  
}
SudoknAcetalProcessingCapability {
    string rdfs_label  
}
SudoknAcrylicFabricationCapability {
    string rdfs_label  
}
SudoknAdditiveManufacturingCapability {
    string rdfs_label  
}
SudoknAddtiveManufacturingCapability {
    string rdfs_label  
}
SudoknAdhesiveBondingCapability {
    string rdfs_label  
}
SudoknAerospaceIndustry {
    string rdfs_label  
}
SudoknAgricultureIndustry {
    string rdfs_label  
}
SudoknAlkalineOxideConversionCoatingCapability {
    string rdfs_label  
}
SudoknAlloySteelProcessingCapability {
    string rdfs_label  
}
SudoknAluminumProcessingCapability {
    string rdfs_label  
}
SudoknAnnealingCapability {
    string rdfs_label  
}
SudoknAnodizingCapability {
    string rdfs_label  
}
SudoknApparelIndustry {
    string rdfs_label  
}
SudoknAssemblyCapability {
    string rdfs_label  
}
SudoknAtomicHydrogenWeldingCapability {
    string rdfs_label  
}
SudoknAutomotiveIndustry {
    string rdfs_label  
}
SudoknBABACertificate {
    string rdfs_label  
}
SudoknBeltSandingCapability {
    string rdfs_label  
}
SudoknBendingCapability {
    string rdfs_label  
}
SudoknBerylliumProcessingCapability {
    string rdfs_label  
}
SudoknBeverageIndustry {
    string rdfs_label  
}
SudoknBlackOxideCoatingCapability {
    string rdfs_label  
}
SudoknBoringCapability {
    string rdfs_label  
}
SudoknBrandName {

}
SudoknBrassBlackeningCapability {
    string rdfs_label  
}
SudoknBrassProcessingCapability {
    string rdfs_label  
}
SudoknBrazeWeldingCapability {
    string rdfs_label  
}
SudoknBrazingCapability {
    string rdfs_label  
}
SudoknBritishRetailConsortiumAccreditation {
    string rdfs_label  
}
SudoknBritishRetailConsortiumCertificate {

}
SudoknBroachingCapability {
    string rdfs_label  
}
SudoknBronzeProcessingCapability {
    string rdfs_label  
}
SudoknBuffingCapability {
    string rdfs_label  
}
SudoknBuildingNumber {

}
SudoknBulgeFormingCapability {
    string rdfs_label  
}
SudoknBusinessDescription {

}
SudoknBusinessEquipmentIndustry {
    string rdfs_label  
}
SudoknButtWeldingCapability {
    string rdfs_label  
}
SudoknCADCAMCapability {

}
SudoknCADCapability {
    string rdfs_label  
}
SudoknCAECapability {

}
SudoknCAMCapability {

}
SudoknCNCBendingCapability {
    string rdfs_label  
}
SudoknCNCClyndricalGrindingCapability {
    string rdfs_label  
}
SudoknCNCCuttingCapability {
    string rdfs_label  
}
SudoknCNCCylindricalGrindingCapability {
    string rdfs_label  
}
SudoknCNCFormingCapability {
    string rdfs_label  
}
SudoknCNCGrindingCapability {
    string rdfs_label  
}
SudoknCNCHorizontalTurningCapability {
    string rdfs_label  
}
SudoknCNCLaserCuttingCapability {
    string rdfs_label  
}
SudoknCNCLatheCapability {
    string rdfs_label  
}
SudoknCNCMachiningCapability {
    string rdfs_label  
}
SudoknCNCMillingCapability {
    string rdfs_label  
}
SudoknCNCPlasmaCuttingCapability {
    string rdfs_label  
}
SudoknCNCPressBrakeCapability {
    string rdfs_label  
}
SudoknCNCRoutingCapability {
    string rdfs_label  
}
SudoknCNCTurningCapability {
    string rdfs_label  
}
SudoknCNCVerticalMillingCapability {
    string rdfs_label  
}
SudoknCNCWireBendingCapability {
    string rdfs_label  
}
SudoknCNCmillingCapability {
    string rdfs_label  
}
SudoknCarbideProcessingCapability {
    string rdfs_label  
}
SudoknCarbonArcBrazingCapability {
    string rdfs_label  
}
SudoknCarbonArcWeldingCapability {
    string rdfs_label  
}
SudoknCarbonGraphiteProcessingCapability {
    string rdfs_label  
}
SudoknCarbonProcessingCapability {

}
SudoknCarbonitridingCapability {
    string rdfs_label  
}
SudoknCarburizingCapability {
    string rdfs_label  
}
SudoknCastingCapability {
    string rdfs_label  
}
SudoknCenterlessGrindingCapability {
    string rdfs_label  
}
SudoknCentrifugalCastingCapability {
    string rdfs_label  
}
SudoknCerakoteCoatingCapability {
    string rdfs_label  
}
SudoknCeramicMoldCastingCapability {
    string rdfs_label  
}
SudoknCeramicProcessingCapability {
    string rdfs_label  
}
SudoknCertificate {

}
SudoknChemicalAndPetrochemicalIndustry {
    string rdfs_label  
}
SudoknChemicalCleaningCapability {
    string rdfs_label  
}
SudoknChemicalCoatingCapability {
    string rdfs_label  
}
SudoknChemicalConversionCoatingCapability {
    string rdfs_label  
}
SudoknChemicalEngravingCapability {
    string rdfs_label  
}
SudoknChemicalMachiningCapability {
    string rdfs_label  
}
SudoknChemicalProcessingCapability {
    string rdfs_label  
}
SudoknChemicalVaporDepositionCapability {
    string rdfs_label  
}
SudoknChemicalsProcessingCapability {
    string rdfs_label  
}
SudoknChromateConversionCoatingCapability {
    string rdfs_label  
}
SudoknChromiumProcessingCapability {
    string rdfs_label  
}
SudoknCity {
    string rdfs_label  
}
SudoknCityOfAddress {

}
SudoknClassifier {

}
SudoknClyndricalGrindingCapability {
    string rdfs_label  
}
SudoknCoalIndustry {

}
SudoknCoatingCapability {
    string rdfs_label  
}
SudoknCobaltProcessingCapability {
    string rdfs_label  
}
SudoknColdRolledSteelProcessingCapability {
    string rdfs_label  
}
SudoknCombustableGasWeldingCapability {
    string rdfs_label  
}
SudoknCommunicationAndElectronicPowerUtilitiesIndustry {
    string rdfs_label  
}
SudoknCommunicationIndustry {
    string rdfs_label  
}
SudoknCommunicationandElectronicPowerUtilitiesIndustry {
    string rdfs_label  
}
SudoknCommunicationsIndustry {

}
SudoknCompositeProcessingCapability {
    string rdfs_label  
}
SudoknCompressionMoldingCapability {
    string rdfs_label  
}
SudoknComputerIndustry {
    string rdfs_label  
}
SudoknComputersandElectronicProductsIndustry {
    string rdfs_label  
}
SudoknConstructionIndustry {
    string rdfs_label  
}
SudoknConsumerGoods {
    string rdfs_label  
}
SudoknConsumerGoodsIndustry {
    string rdfs_label  
}
SudoknContinuousCastingCapability {
    string rdfs_label  
}
SudoknCopperProcessingCapability {
    string rdfs_label  
}
SudoknCounterBoringCapability {
    string rdfs_label  
}
SudoknCounterSinkingCapability {
    string rdfs_label  
}
SudoknCountry {

}
SudoknCountryOfAddress {

}
SudoknCounty {

}
SudoknCreepFeedGrindingCapability {
    string rdfs_label  
}
SudoknCrochetCapability {

}
SudoknCurvicGrindingCapability {
    string rdfs_label  
}
SudoknCustomFoamCuttingCapability {
    string rdfs_label  
}
SudoknCuttingCapability {
    string rdfs_label  
}
SudoknCyanidingCapability {
    string rdfs_label  
}
SudoknCylindricalGrindingCapability {
    string rdfs_label  
}
SudoknDeburringCapability {
    string rdfs_label  
}
SudoknDeepFreezingCapability {
    string rdfs_label  
}
SudoknDeepHoleDrillingCapability {
    string rdfs_label  
}
SudoknDelrinProcessingCapability {
    string rdfs_label  
}
SudoknDesignativeName {

}
SudoknDiamondMachiningCapability {
    string rdfs_label  
}
SudoknDieCastingCapability {
    string rdfs_label  
}
SudoknDieDesignCapability {

}
SudoknDieMakingCapability {
    string rdfs_label  
}
SudoknDifficultToMachineMaterialsProcessingCapability {
    string rdfs_label  
}
SudoknDiffusionBondingCapability {
    string rdfs_label  
}
SudoknDiffusionHardeningCapability {
    string rdfs_label  
}
SudoknDigitalPrintingCapability {
    string rdfs_label  
}
SudoknDipBrazingCapability {
    string rdfs_label  
}
SudoknDisabledVeteranOwned {
    string rdfs_label  
}
SudoknDrawingCapability {
    string rdfs_label  
}
SudoknDrillingCapability {
    string rdfs_label  
}
SudoknDyeingCapability {

}
SudoknEDMCapability {
    string rdfs_label  
}
SudoknEducationIndustry {
    string rdfs_label  
}
SudoknEducationalInstitutionsIndustry {
    string rdfs_label  
}
SudoknElectolessNickelPlatingCapability {
    string rdfs_label  
}
SudoknElectricArcWeldingCapability {
    string rdfs_label  
}
SudoknElectricAutomotiveIndustry {
    string rdfs_label  
}
SudoknElectricVehiclesIndustry {
    string rdfs_label  
}
SudoknElectricalDischargeMachiningCapability {
    string rdfs_label  
}
SudoknElectricalResistanceWeldingCapability {
    string rdfs_label  
}
SudoknElectroPlatingCapability {
    string rdfs_label  
}
SudoknElectroSlagWeldingCapability {
    string rdfs_label  
}
SudoknElectrolessNickelPlating {
    string rdfs_label  
}
SudoknElectrolessNickelPlatingCapability {
    string rdfs_label  
}
SudoknElectrolessPlatingCapability {
    string rdfs_label  
}
SudoknElectronBeamMachiningCapability {
    string rdfs_label  
}
SudoknElectronBeamWeldingCapability {
    string rdfs_label  
}
SudoknElectronicAutomotiveInudstry {
    string rdfs_label  
}
SudoknElectronicProcessingCapability {

}
SudoknElectronicProductIndustry {
    string rdfs_label  
}
SudoknElectroplatingCapability {
    string rdfs_label  
}
SudoknElectropolishingCapability {
    string rdfs_label  
}
SudoknEmailAddress {

}
SudoknEmbossingCapability {
    string rdfs_label  
}
SudoknEndFormingCapability {
    string rdfs_label  
}
SudoknEndMillingCapability {
    string rdfs_label  
}
SudoknEnergyIndustry {

}
SudoknEngineeringCapability {

}
SudoknEngineeringDesignCapability {
    string rdfs_label  
}
SudoknEngravingCapability {
    string rdfs_label  
}
SudoknErosionMachiningCapability {
    string rdfs_label  
}
SudoknEtchingCapability {
    string rdfs_label  
}
SudoknExoticMaterialProcessingCapability {
    string rdfs_label  
}
SudoknExplosiveWeldingCapability {
    string rdfs_label  
}
SudoknExtremelyHardMaterialProcessingCapability {
    string rdfs_label  
}
SudoknExtrudingCapability {
    string rdfs_label  
}
SudoknExtrusionCapability {
    string rdfs_label  
}
SudoknFDACertificate {
    string rdfs_label  
}
SudoknFDAGMPCertificate {
    string rdfs_label  
}
SudoknFDAGMPCompliant {
    string rdfs_label  
}
SudoknFDAPMACertificate {
    string rdfs_label  
}
SudoknFabricatingCapability {
    string rdfs_label  
}
SudoknFabricationCapability {
    string rdfs_label  
}
SudoknFaceMillingCapability {
    string rdfs_label  
}
SudoknFasteningCapability {
    string rdfs_label  
}
SudoknFiberOpticLaserCuttingCapability {
    string rdfs_label  
}
SudoknFiberProcessingCapability {

}
SudoknFillingCapability {
    string rdfs_label  
}
SudoknFinishingCapability {
    string rdfs_label  
}
SudoknFiveAxixMachiningCapability {
    string rdfs_label  
}
SudoknFixtureDesignCapability {
    string rdfs_label  
}
SudoknFixturingCapability {
    string rdfs_label  
}
SudoknFlameSprayingCapability {
    string rdfs_label  
}
SudoknFluxCoredArcWeldingCapability {
    string rdfs_label  
}
SudoknFoamProcessingCapability {
    string rdfs_label  
}
SudoknFoodIndustry {
    string rdfs_label  
}
SudoknForgingCapability {
    string rdfs_label  
}
SudoknFormingCapability {
    string rdfs_label  
}
SudoknFrictionWeldingCapability {
    string rdfs_label  
}
SudoknFurnaceBrazingCapability {
    string rdfs_label  
}
SudoknFurnitureIndustry {
    string rdfs_label  
}
SudoknFusedDepositionModelingCapability {
    string rdfs_label  
}
SudoknFusedNitrateConversionCoatingCapability {
    string rdfs_label  
}
SudoknGWOCertificate {

}
SudoknGalvanizingCapability {
    string rdfs_label  
}
SudoknGasBrazingCapability {
    string rdfs_label  
}
SudoknGasMetalArcWeldingCapability {
    string rdfs_label  
}
SudoknGasTungstenArcWeldingCapability {
    string rdfs_label  
}
SudoknGasWeldingCapability {
    string rdfs_label  
}
SudoknGearCuttingCapability {
    string rdfs_label  
}
SudoknGearGashingCapability {
    string rdfs_label  
}
SudoknGearHobbingCapability {
    string rdfs_label  
}
SudoknGeopoliticalSite {

}
SudoknGeospatialLocation {
    uri sudokn_hasPostalAddress  
}
SudoknGlassProcessingCapability {
    string rdfs_label  
}
SudoknGoldProcessingCapability {
    string rdfs_label  
}
SudoknGovermentIndustry {
    string rdfs_label  
}
SudoknGovernmentIndustry {
    string rdfs_label  
}
SudoknGraphiteProcessingCapability {
    string rdfs_label  
}
SudoknGravityCastingCapability {
    string rdfs_label  
}
SudoknGrindingCapability {
    string rdfs_label  
}
SudoknGunDrillingCapability {
    string rdfs_label  
}
SudoknHAACPCertificate {
    string rdfs_label  
}
SudoknHardeningCapability {
    string rdfs_label  
}
SudoknHarperizingCapability {
    string rdfs_label  
}
SudoknHastelloyProcessingCapability {
    string rdfs_label  
}
SudoknHealthCareServicesIndustry {
    string rdfs_label  
}
SudoknHealthcareServices {

}
SudoknHealthcareServicesIndustry {
    string rdfs_label  
}
SudoknHeatTreatingCapability {
    string rdfs_label  
}
SudoknHighEnergyBeamMachiningCapability {
    string rdfs_label  
}
SudoknHighEnergyBeamWeldingCapability {
    string rdfs_label  
}
SudoknHighGradeAluminumProcessingCapability {
    string rdfs_label  
}
SudoknHoleDrillingEDMCapability {
    string rdfs_label  
}
SudoknHoleMakingCapability {
    string rdfs_label  
}
SudoknHoningCapability {
    string rdfs_label  
}
SudoknHorizontalBoringCapability {
    string rdfs_label  
}
SudoknHorizontalMillingCapability {
    string rdfs_label  
}
SudoknHotDipGalvanizingCapability {
    string rdfs_label  
}
SudoknIATF16949Certificate {
    string rdfs_label  
}
SudoknIATFCertificate {

}
SudoknIDODGrindingCapability {
    string rdfs_label  
}
SudoknIS-TS16949 {
    string rdfs_label  
}
SudoknISO13485 {
    string rdfs_label  
}
SudoknISO13485Certificate {
    string rdfs_label  
}
SudoknISO14000Certificate {
    string rdfs_label  
}
SudoknISO14001 {
    string rdfs_label  
}
SudoknISO14001Certificate {
    string rdfs_label  
}
SudoknISO17265Certificate {

}
SudoknISO27001Certificate {

}
SudoknISO45001Certificate {

}
SudoknISO9000 {
    string rdfs_label  
}
SudoknISO9000Certificate {

}
SudoknISO9001 {
    string rdfs_label  
}
SudoknISO9001Certificate {
    string rdfs_label  
}
SudoknISOCertificate {
    string rdfs_label  
}
SudoknISOQualityCertificate {

}
SudoknISTS16949Certificate {
    string rdfs_label  
}
SudoknISTSCertificate {

}
SudoknITARCertificate {
    string rdfs_label  
}
SudoknITARCompliant {
    string rdfs_label  
}
SudoknInconelProcessingCapability {
    string rdfs_label  
}
SudoknInductionBrazingCapability {
    string rdfs_label  
}
SudoknInductionHeatingCapability {
    string rdfs_label  
}
SudoknIndustrialMachineryandEquipmentIndustry {
    string rdfs_label  
}
SudoknIndustry {
    string rdfs_label  
}
SudoknInformationTechnologyIndustry {

}
SudoknInfraredBrazingCapability {
    string rdfs_label  
}
SudoknInjectionMoldingCapability {
    string rdfs_label  
}
SudoknInstallationCapability {
    string rdfs_label  
}
SudoknInvarProcessingCapability {
    string rdfs_label  
}
SudoknInvestmentCastingCapability {
    string rdfs_label  
}
SudoknIronProcessingCapability {
    string rdfs_label  
}
SudoknJoiningCapability {
    string rdfs_label  
}
SudoknKOSHERApproved {
    string rdfs_label  
}
SudoknKaptonProcessingCapability {
    string rdfs_label  
}
SudoknKittingCapability {
    string rdfs_label  
}
SudoknKnittingCapability {
    string rdfs_label  
}
SudoknKnurlingCapability {
    string rdfs_label  
}
SudoknKosherApprovedCertificate {

}
SudoknKovarProcessingCapability {
    string rdfs_label  
}
SudoknLEEDCertificate {
    string rdfs_label  
}
SudoknLabelingCapability {
    string rdfs_label  
}
SudoknLappingCapability {
    string rdfs_label  
}
SudoknLaserBeamWeldingCapability {
    string rdfs_label  
}
SudoknLaserCuttingCapability {
    string rdfs_label  
}
SudoknLaserEngravingCapability {
    string rdfs_label  
}
SudoknLaserEtchingCapability {
    string rdfs_label  
}
SudoknLaserProcessingCapability {
    string rdfs_label  
}
SudoknLaserWeldingCapability {
    string rdfs_label  
}
SudoknLatheWorkCapability {
    string rdfs_label  
}
SudoknLeadProcessingCapability {
    string rdfs_label  
}
SudoknLexanProcessingCapability {
    string rdfs_label  
}
SudoknLiquidCoatingCapability {
    string rdfs_label  
}
SudoknLiveToolingCapability {
    string rdfs_label  
}
SudoknLostFoamCastingCapability {
    string rdfs_label  
}
SudoknLowAlloySteelLeadProcessingCapability {
    string rdfs_label  
}
SudoknLowAlloySteelProcessingCapability {
    string rdfs_label  
}
SudoknMIGWeldinCapability {
    string rdfs_label  
}
SudoknMIGWeldingCapability {
    string rdfs_label  
}
SudoknMachinaryAndEquipmentIndustry {
    string rdfs_label  
}
SudoknMachineBuildingCapability {
    string rdfs_label  
}
SudoknMachiningCapability {
    string rdfs_label  
}
SudoknMagnesiumAlloyProcessingCapability {
    string rdfs_label  
}
SudoknMagnesiumProcessingCapability {
    string rdfs_label  
}
SudoknManMadeFiberProcessingCapability {
    string rdfs_label  
}
SudoknManufacturingProcessCapability {

}
SudoknMaterialProcessingCapability {

}
SudoknMechanicalAssemblyCapability {
    string rdfs_label  
}
SudoknMechanicalCoatingCapability {
    string rdfs_label  
}
SudoknMechanicalJoiningCapability {
    string rdfs_label  
}
SudoknMechanicalWeldingCapability {
    string rdfs_label  
}
SudoknMediaBlastingCapability {
    string rdfs_label  
}
SudoknMetalFabricationCapability {
    string rdfs_label  
}
SudoknMetalInjectionMoldingCapability {
    string rdfs_label  
}
SudoknMetalProcessingCapability {
    string rdfs_label  
}
SudoknMetalProductionIndustry {
    string rdfs_label  
}
SudoknMetalProductsIndustry {

}
SudoknMetalSpinningCapability {
    string rdfs_label  
}
SudoknMetalStampingCapability {
    string rdfs_label  
}
SudoknMetalsProductsIndustry {
    string rdfs_label  
}
SudoknMetalworkingCapability {
    string rdfs_label  
}
SudoknMicroDrillingCapability {
    string rdfs_label  
}
SudoknMigWeldingCapability {
    string rdfs_label  
}
SudoknMilitaryIndustry {
    string rdfs_label  
}
SudoknMillingCapability {
    string rdfs_label  
}
SudoknMiningIndustry {
    string rdfs_label  
}
SudoknMinorityOwned {
    string rdfs_label  
}
SudoknMoldDesignCapability {

}
SudoknMoldMakingCapability {
    string rdfs_label  
}
SudoknMoldingCapability {
    string rdfs_label  
}
SudoknMolybdenumProcessingCapability {
    string rdfs_label  
}
SudoknMultiPointCuttingCapability {
    string rdfs_label  
}
SudoknNADCAPAC7004 {
    string rdfs_label  
}
SudoknNADCAPCertificate {
    string rdfs_label  
}
SudoknNAICS33 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS331 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS331110 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS331210 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS331221 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS331222 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS331313 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS331314 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS331315 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS331318 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS331410 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS331420 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS331491 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS331492 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS331511 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS331512 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS331513 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS331523 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS331524 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS331529 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS332 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS332111 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS332112 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS332114 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS332115 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS332116 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS332117 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS332119 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS332211 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS332212 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS332213 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS332214 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS332215 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS332216 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS332311 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS332312 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS332313 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS332321 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS332322 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS332323 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS332410 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS332420 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS332431 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS332439 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS332510 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS332611 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS332612 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS332613 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS332618 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS332710 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS332721 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS332722 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS332811 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS332812 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS332813 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS332911 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS332912 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS332913 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS332919 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS332991 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS332992 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS332993 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS332994 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS332995 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS332996 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS332997 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS332998 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS332999 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS333 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS333111 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS333112 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS333120 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS333131 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS333132 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS333241 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS333242 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS333243 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS333248 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS333310 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS333413 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS333414 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS333415 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS333511 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS333514 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS333515 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS333517 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS333519 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS333611 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS333612 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS333613 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS333618 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS333912 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS333914 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS333921 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS333922 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS333923 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS333924 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS333991 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS333992 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS333993 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS333994 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS333995 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS333996 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS333998 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS334 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS334111 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS334112 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS334118 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS334210 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS334220 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS334290 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS334310 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS334412 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS334413 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS334416 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS334417 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS334418 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS334419 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS334510 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS334511 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS334512 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS334513 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS334514 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS334515 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS334516 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS334517 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS334519 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS334610 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS335 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS335131 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS335132 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS335139 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS335210 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS335220 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS335311 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS335312 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS335313 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS335314 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS335910 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS335921 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS335929 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS335931 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS335932 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS335991 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS335999 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS336 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS336110 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS336120 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS336211 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS336212 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS336213 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS336214 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS336310 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS336320 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS336330 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS336340 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS336350 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS336360 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS336370 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS336390 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS336411 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS336412 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS336413 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS336414 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS336415 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS336419 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS336510 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS336611 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS336612 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS336991 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS336992 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS337 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS337110 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS337121 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS337122 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS337126 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS337127 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS337211 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS337212 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS337214 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS337215 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS337910 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS337920 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS339 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS339112 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS339113 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS339114 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS339115 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS339116 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS339910 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS339920 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS339930 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS339940 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS339950 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS339991 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS339992 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS339993 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS339994 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS339995 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICS339999 {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNAICSClassifier {
    string sudokn_hasNAICSTextValue  
    integer sudokn_hasNAICSCodeValue  
}
SudoknNIST800171Certificate {

}
SudoknNISTCertificate {

}
SudoknNativeAmericanOwned {
    string rdfs_label  
}
SudoknNaturalFiberProcessingCapability {
    string rdfs_label  
}
SudoknNickelPlatingCapability {
    string rdfs_label  
}
SudoknNickelProcessingCapability {
    string rdfs_label  
}
SudoknNitridingCapability {
    string rdfs_label  
}
SudoknNomexProcessingCapability {
    string rdfs_label  
}
SudoknNotchingCapability {
    string rdfs_label  
}
SudoknNuclearEnergyIndustry {

}
SudoknNylonProcessingCapability {
    string rdfs_label  
}
SudoknOHSAS18001Certificate {

}
SudoknOccupationalHealthAndSafetyCertificate {

}
SudoknOffshoreWindIndustry {
    string rdfs_label  
}
SudoknOilAndGasIndustry {
    string rdfs_label  
}
SudoknOilGroovingCapability {
    string rdfs_label  
}
SudoknOrganizationName {

}
SudoknOwnershipStatusClassifier {
    string rdfs_label  
}
SudoknOxy-FuelCuttingCapability {
    string rdfs_label  
}
SudoknOxyFuelCutting {
    string rdfs_label  
}
SudoknPLCProgrammingCapability {
    string rdfs_label  
}
SudoknPackagingCapability {
    string rdfs_label  
}
SudoknPackingCapability {
    string rdfs_label  
}
SudoknPaintingCapability {
    string rdfs_label  
}
SudoknPalladiumProcessingCapability {
    string rdfs_label  
}
SudoknPaperIndustry {
    string rdfs_label  
}
SudoknPaperandPaperboardProductsIndustry {
    string rdfs_label  
}
SudoknPaperboardProductsIndustry {
    string rdfs_label  
}
SudoknPassivationCapability {
    string rdfs_label  
}
SudoknPemInsertionCapability {
    string rdfs_label  
}
SudoknPercussionWeldingCapability {
    string rdfs_label  
}
SudoknPermanentMoldCastingCapability {
    string rdfs_label  
}
SudoknPharmaceuticalIndustry {

}
SudoknPhosBronzeProcessingCapability {
    string rdfs_label  
}
SudoknPhosphateCoatingCapability {
    string rdfs_label  
}
SudoknPhosphateConversionCoatingCapability {
    string rdfs_label  
}
SudoknPhosphorBronzeProcessingCapability {
    string rdfs_label  
}
SudoknPhotochemicalMachiningProcess {
    string rdfs_label  
}
SudoknPhysicalVaporDepositionCapability {
    string rdfs_label  
}
SudoknPipingFabricationCapability {
    string rdfs_label  
}
SudoknPlaningCapability {
    string rdfs_label  
}
SudoknPlasmaArcWeldingCapability {
    string rdfs_label  
}
SudoknPlasmaCuttingCapability {
    string rdfs_label  
}
SudoknPlasmaSprayingCapability {
    string rdfs_label  
}
SudoknPlasterMoldCastingCapability {
    string rdfs_label  
}
SudoknPlasticAndRubberIndustry {
    string rdfs_label  
}
SudoknPlasticMachiningCapability {
    string rdfs_label  
}
SudoknPlasticProcessingCapability {
    string rdfs_label  
}
SudoknPlasticsandRubberProductsIndustry {
    string rdfs_label  
}
SudoknPlatingCapability {
    string rdfs_label  
}
SudoknPlatinumProcessingCapability {
    string rdfs_label  
}
SudoknPlungeGrindingCapability {
    string rdfs_label  
}
SudoknPolishingCapability {
    string rdfs_label  
}
SudoknPolycarbonateProcessingCapability {
    string rdfs_label  
}
SudoknPolycrystallineDiamondMachiningCapability {
    string rdfs_label  
}
SudoknPostalAddress {
    string iosc_hasTextValue  
}
SudoknPowderCoatingCapability {
    string rdfs_label  
}
SudoknPowderMetalFormingCapability {
    string rdfs_label  
}
SudoknPreciousMaterialProcessingCapability {
    string rdfs_label  
}
SudoknPressBrakingCapability {
    string rdfs_label  
}
SudoknPressFittingCapability {
    string rdfs_label  
}
SudoknPressingCapability {
    string rdfs_label  
}
SudoknPressureWeldingCapability {
    string rdfs_label  
}
SudoknPrintingAndInformationIndustry {
    string rdfs_label  
}
SudoknPrintingCapability {
    string rdfs_label  
}
SudoknProductDesignCapability {
    string rdfs_label  
}
SudoknProfessionalCertificate {

}
SudoknProfessionalServicesIndustry {
    string rdfs_label  
}
SudoknProjectionWeldingCapability {
    string rdfs_label  
}
SudoknPrototypeManufacturingCapability {
    string rdfs_label  
}
SudoknPrototypingCapability {
    string rdfs_label  
}
SudoknPulsedElectrochemicalMachiningCapability {
    string rdfs_label  
}
SudoknPunchingCapability {
    string rdfs_label  
}
SudoknQS9000 {
    string rdfs_label  
}
SudoknQS9000Certificate {
    string rdfs_label  
}
SudoknQSCertificate {

}
SudoknQualityCertificate {

}
SudoknQualityManagementCapability {

}
SudoknRAMEdmCapability {
    string rdfs_label  
}
SudoknRamEDMCapability {
    string rdfs_label  
}
SudoknRapidPrototypingCapability {
    string rdfs_label  
}
SudoknReactionInjectionMoldingCapability {
    string rdfs_label  
}
SudoknReamingCapability {
    string rdfs_label  
}
SudoknRecyclingIndustry {
    string rdfs_label  
}
SudoknRenewableEnergyIndustry {

}
SudoknResistanceBrazingCapability {
    string rdfs_label  
}
SudoknResistanceWeldingCapability {
    string rdfs_label  
}
SudoknRestaurantIndustry {
    string rdfs_label  
}
SudoknRetailIndustry {
    string rdfs_label  
}
SudoknRetailTradeIndustry {
    string rdfs_label  
}
SudoknReverseEngineeringCapability {
    string rdfs_label  
}
SudoknRivetingCapability {
    string rdfs_label  
}
SudoknRivettingCapability {
    string rdfs_label  
}
SudoknRoboticWeldingCapability {
    string rdfs_label  
}
SudoknRollDieEngravingCapability {
    string rdfs_label  
}
SudoknRollingCapability {
    string rdfs_label  
}
SudoknRotationalMoldingCapability {
    string rdfs_label  
}
SudoknRubberInjectionMoldingCapability {
    string rdfs_label  
}
SudoknRubberProcessingCapability {
    string rdfs_label  
}
SudoknSandBlastingCapability {
    string rdfs_label  
}
SudoknSandCastingCapability {
    string rdfs_label  
}
SudoknSanitaryWeldingCapability {
    string rdfs_label  
}
SudoknSawingCapability {
    string rdfs_label  
}
SudoknScreenPrintingCapability {
    string rdfs_label  
}
SudoknSeamWeldingCapability {
    string rdfs_label  
}
SudoknSelectiveLaserSinteringCapability {
    string rdfs_label  
}
SudoknSemiconductorFabricatingCapability {
    string rdfs_label  
}
SudoknSevenAxisMachiningCapability {
    string rdfs_label  
}
SudoknSewingCapability {
    string rdfs_label  
}
SudoknShapingCapability {
    string rdfs_label  
}
SudoknShearingCapability {
    string rdfs_label  
}
SudoknSheeringCapability {
    string rdfs_label  
}
SudoknSheetMetalFabricationCapability {
    string rdfs_label  
}
SudoknSheetMetalFormingCapability {
    string rdfs_label  
}
SudoknSheetMetalProcessingCapability {
    string rdfs_label  
}
SudoknShellMoldCastingCapability {
    string rdfs_label  
}
SudoknShellMoldingCapability {
    string rdfs_label  
}
SudoknShieldedMetalArcWeldingCapability {
    string rdfs_label  
}
SudoknShotPeeningCapability {
    string rdfs_label  
}
SudoknShrinkFittingCapability {
    string rdfs_label  
}
SudoknSiliconeProcessingCapability {
    string rdfs_label  
}
SudoknSilkScreeningCapability {
    string rdfs_label  
}
SudoknSilverProcessingCapability {
    string rdfs_label  
}
SudoknSinglePointCuttingCapability {
    string rdfs_label  
}
SudoknSinkerEDMCapability {
    string rdfs_label  
}
SudoknSinkerEdmCapability {
    string rdfs_label  
}
SudoknSinteringCapability {
    string rdfs_label  
}
SudoknSlabMillingCapability {
    string rdfs_label  
}
SudoknSmallDisadvantagedBusiness {
    string rdfs_label  
}
SudoknSmallHoleDrillingCapability {
    string rdfs_label  
}
SudoknSmeltingCapability {
    string rdfs_label  
}
SudoknSolderingCapability {
    string rdfs_label  
}
SudoknSparkPlasmaSinteringCapability {
    string rdfs_label  
}
SudoknSpecialBusinessStatusClassifier {

}
SudoknSpecialMaterialsProcessingCapability {
    string rdfs_label  
}
SudoknSpinningCapability {
    string rdfs_label  
}
SudoknSportsAndLeisureIndustry {
    string rdfs_label  
}
SudoknSportsandLeisureIndustry {
    string rdfs_label  
}
SudoknSpotWeldingCapability {
    string rdfs_label  
}
SudoknSqueezeCastingCapability {
    string rdfs_label  
}
SudoknStainlessSteelProcessingCapability {
    string rdfs_label  
}
SudoknStampingCapability {
    string rdfs_label  
}
SudoknState {
    string rdfs_label  
}
SudoknStateOfAddress {

}
SudoknSteelAlloyProcessingCapability {
    string rdfs_label  
}
SudoknSteelManufacturingCapability {
    string rdfs_label  
}
SudoknSteelProcessingCapability {
    string rdfs_label  
}
SudoknStereolithographyCapability {
    string rdfs_label  
}
SudoknStreetAddress {

}
SudoknStretchFormingCapability {
    string rdfs_label  
}
SudoknStudWeldingCapability {
    string rdfs_label  
}
SudoknSubmergedArcWeldingCapability {
    string rdfs_label  
}
SudoknSuperAlloyProcessingCapability {
    string rdfs_label  
}
SudoknSurfaceFinishingCapability {
    string rdfs_label  
}
SudoknSurfaceGrindingCapability {
    string rdfs_label  
}
SudoknSurfaceHardeningCapability {
    string rdfs_label  
}
SudoknSurfacePreparationCapability {
    string rdfs_label  
}
SudoknSustainabilityCertificate {

}
SudoknSwissMachiningCapability {
    string rdfs_label  
}
SudoknSwissTurningCapability {
    string rdfs_label  
}
SudoknTI-9000Certificate {

}
SudoknTI9000Certificate {
    string rdfs_label  
}
SudoknTICertificate {

}
SudoknTIGWeldingCapability {
    string rdfs_label  
}
SudoknTantalumProcessingCapability {
    string rdfs_label  
}
SudoknTappingCapability {
    string rdfs_label  
}
SudoknTeflonProcessingCapability {
    string rdfs_label  
}
SudoknTextileProcessCapability {

}
SudoknTextiles {
    string rdfs_label  
}
SudoknTextilesIndustry {
    string rdfs_label  
}
SudoknThermaJoiningCapability {
    string rdfs_label  
}
SudoknThermalCoatingCapability {
    string rdfs_label  
}
SudoknThermalSprayCoatingCapability {
    string rdfs_label  
}
SudoknThermalSubtractionCapability {
    string rdfs_label  
}
SudoknThermalWeldingCapability {
    string rdfs_label  
}
SudoknThermoformingCapability {
    string rdfs_label  
}
SudoknThreadMillingCapability {
    string rdfs_label  
}
SudoknThreadingCapability {
    string rdfs_label  
}
SudoknTinProcessingCapability {
    string rdfs_label  
}
SudoknTitaniumProcessingCapability {
    string rdfs_label  
}
SudoknToolDesignCapability {

}
SudoknToolMakingCapability {
    string rdfs_label  
}
SudoknTorchBrazingCapability {
    string rdfs_label  
}
SudoknTorchCuttingCapability {
    string rdfs_label  
}
SudoknTransferMoldingCapability {
    string rdfs_label  
}
SudoknTransportationIndustry {
    string rdfs_label  
}
SudoknTubeBendingCapability {
    string rdfs_label  
}
SudoknTubeFormingCapability {
    string rdfs_label  
}
SudoknTubingCapability {
    string rdfs_label  
}
SudoknTungstenProcessingCapability {
    string rdfs_label  
}
SudoknTurningCapability {
    string rdfs_label  
}
SudoknTurretPunchingCapability {
    string rdfs_label  
}
SudoknTwoDimensionalCartesianSpatialCoordinateDatum {
    float sudokn_hasLongitudeValue  
    string sudokn_hasLongitudeValue  
    float sudokn_hasLatitudeValue  
    string sudokn_hasLatitudeValue  
}
SudoknUSPostalCode {
    string sudokn_hasIntegerValue  
}
SudoknUltrasonicCleaningCapability {
    string rdfs_label  
}
SudoknUltrasonicWeldingCapability {
    string rdfs_label  
}
SudoknUrethaneProcessingCapability {
    string rdfs_label  
}
SudoknUtilitiesIndustry {
    string rdfs_label  
}
SudoknVacuumCastingCapability {
    string rdfs_label  
}
SudoknVacuumFormingCapability {
    string rdfs_label  
}
SudoknVacuumHardeningCapability {
    string rdfs_label  
}
SudoknVacuumMoldingCapability {
    string rdfs_label  
}
SudoknVacuumPackagingCapability {
    string rdfs_label  
}
SudoknVacuumPressingCapability {
    string rdfs_label  
}
SudoknVaporizedMetalCoatingCapability {
    string rdfs_label  
}
SudoknVerticalMillingCapability {
    string rdfs_label  
}
SudoknVeteranOwned {
    string rdfs_label  
}
SudoknVitualLocationIdentifier {

}
SudoknWarehousingAndStorage {

}
SudoknWarehousingAndStorageIndustry {
    string rdfs_label  
}
SudoknWaspaloyProcessingCapability {
    string rdfs_label  
}
SudoknWaterAndSewerUtilitiesIndustry {
    string rdfs_label  
}
SudoknWaterJetCuttingCapability {
    string rdfs_label  
}
SudoknWaterandSewerUtilitiesIndustry {
    string rdfs_label  
}
SudoknWaterjetCuttimgCapability {
    string rdfs_label  
}
SudoknWaterjetCuttingCapability {
    string rdfs_label  
}
SudoknWeavingCapability {

}
SudoknWebAddress {

}
SudoknWeldingCapability {
    string rdfs_label  
}
SudoknWetPaintingCapability {
    string rdfs_label  
}
SudoknWireBendingCapability {
    string rdfs_label  
}
SudoknWireEDMCapability {
    string rdfs_label  
}
SudoknWireFormingCapability {
    string rdfs_label  
}
SudoknWireHarnessAssemblyCapability {
    string rdfs_label  
}
SudoknWiringCapability {
    string rdfs_label  
}
SudoknWomenOwned {
    string rdfs_label  
}
SudoknWoodProcessingCapability {
    string rdfs_label  
}
SudoknWoodProductManufacturingIndustry {
    string rdfs_label  
}
SudoknWoodWorkingCapability {
    string rdfs_label  
}
SudoknWoodworkingCapability {
    string rdfs_label  
}
SudoknZeroStockMachiningCapability {
    string rdfs_label  
}
SudoknZincAlloyProcessingCapability {
    string rdfs_label  
}
SudoknZincArcSprayCapability {
    string rdfs_label  
}
SudoknZincProcessingCapability {
    string rdfs_label  
}
SudoknZirconProcessingCapability {
    string rdfs_label  
}
SudoknOrganizationSize {

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
IoManufacturer ||--|o SudoknGeospatialLocation : "sudokn_organizationLocatedIn"
IoManufacturer ||--|o SudoknNAICS332612 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332722 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332813 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332811 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332311 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332115 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332812 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332611 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332995 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332312 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332212 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332112 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332919 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332211 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332323 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332913 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332410 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332997 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332991 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332116 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332510 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332420 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332213 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332999 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332111 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332313 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332996 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332992 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332721 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICSClassifier : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332214 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332117 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332994 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332912 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332322 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332998 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332710 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332114 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332911 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332321 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332618 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332439 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknNAICS332431 : "sudokn_hasPrimaryNAICSClassifier"
IoManufacturer ||--|o SudoknOwnershipStatusClassifier : "sudokn_hasOwnershipStatusClassifier"
IoManufacturer ||--|o OwlClass : "sudokn_hasOwnershipStatusClassifier"
IoManufacturer ||--|o OwlNamedIndividual : "sudokn_hasOwnershipStatusClassifier"
IoManufacturer ||--|o SudoknISO13485Certificate : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknISO14000Certificate : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknASMECertificate : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknKOSHERApproved : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknFDAGMPCompliant : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknISO14001 : "sudokn_hasCertificate"
IoManufacturer ||--|o OwlNamedIndividual : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknAWSWelderCertificate : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknISO9001 : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknISOCertificate : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknNADCAPAC7004 : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknLEEDCertificate : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknISTS16949Certificate : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknISO9001Certificate : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknNADCAPCertificate : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknAS9100Certificate : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknISO13485 : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknISO14001Certificate : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknFDACertificate : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknCertificate : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknASME : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknIS-TS16949 : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknIATF16949Certificate : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknITARCertificate : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknBABACertificate : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknQS9000 : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknITARCompliant : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknAS9102Certificate : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknBritishRetailConsortiumAccreditation : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknQS9000Certificate : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknAS9000Certificate : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknISO9000Certificate : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknTI9000Certificate : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknAS9100 : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknHAACPCertificate : "sudokn_hasCertificate"
IoManufacturer ||--|o SudoknISO9000 : "sudokn_hasCertificate"
IoManufacturer ||--|o IoMaterialProduct : "sudokn_manufactures"
IoManufacturer ||--|o OwlNamedIndividual : "sudokn_hasManagementCapability"
IoManufacturer ||--|o SudoknQualityManagementCapability : "sudokn_hasManagementCapability"
IoManufacturer ||--|o SudoknCeramicProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknMetalProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknCobaltProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknWaspaloyProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknExtremelyHardMaterialProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknDifficultToMachineMaterialsProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknPhosBronzeProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknPolycarbonateProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknStainlessSteelProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknTungstenProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknSpecialMaterialsProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknZincProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknZirconProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o OwlNamedIndividual : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknGraphiteProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknPlasticProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknColdRolledSteelProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknManMadeFiberProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknNaturalFiberProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknBronzeProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknCopperProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknBerylliumProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknNomexProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknTitaniumProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknLexanProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknExoticMaterialProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknNylonProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknAcetalProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknDelrinProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknZincAlloyProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknSiliconeProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknLowAlloySteelProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknKaptonProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknInvarProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknHighGradeAluminumProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknGoldProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknSteelProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknAluminumProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknHastelloyProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknRubberProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknTeflonProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknPlatinumProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknAlloySteelProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknLeadProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknNickelProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknPhosphorBronzeProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknBrassProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknTantalumProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknTinProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknGlassProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknMagnesiumProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknFoamProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknCarbonGraphiteProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknMolybdenumProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknIronProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknUrethaneProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknSilverProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknChemicalsProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknMaterialProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknPalladiumProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknKovarProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknCarbideProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknWoodProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknInconelProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknCompositeProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknChromiumProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknPreciousMaterialProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o SudoknSteelAlloyProcessingCapability : "sudokn_hasMaterialCapability"
IoManufacturer ||--|o OwlNamedIndividual : "sudokn_hasEmailAddress"
IoManufacturer ||--|o SudoknEmailAddress : "sudokn_hasEmailAddress"
IoManufacturer ||--|o SudoknPostalAddress : "sudokn_hasPostalAddress"
IoManufacturer ||--|o OwlNamedIndividual : "sudokn_hasPostalAddress"
IoManufacturer ||--|o SudoknUSPostalCode : "sudokn_hasPostalAddress"
IoManufacturer ||--|o SudoknUtilitiesIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknMiningIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknPaperIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknPlasticsandRubberProductsIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknWaterandSewerUtilitiesIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknMetalsProductsIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknTextiles : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknGovernmentIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknConsumerGoodsIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknConsumerGoods : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknEducationalInstitutionsIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknConstructionIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknComputersandElectronicProductsIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o OwlNamedIndividual : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknApparelIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknMetalProductionIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknEducationIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknOffshoreWindIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknFurnitureIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknElectricVehiclesIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknGovermentIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknPlasticAndRubberIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknSportsAndLeisureIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknAerospaceIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknWarehousingAndStorageIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o IoscIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknHealthCareServicesIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknRetailIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknWoodProductManufacturingIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknPrintingAndInformationIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknMilitaryIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknElectronicProductIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknAutomotiveIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknChemicalAndPetrochemicalIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknTextilesIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknMachinaryAndEquipmentIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknFoodIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknRecyclingIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknProfessionalServicesIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknIndustrialMachineryandEquipmentIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknTransportationIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknCommunicationIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknHealthcareServicesIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknBusinessEquipmentIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknElectronicAutomotiveInudstry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknPaperandPaperboardProductsIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknSportsandLeisureIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknOilAndGasIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknCommunicationandElectronicPowerUtilitiesIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknAgricultureIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o SudoknRetailTradeIndustry : "sudokn_suppliesToIndustry"
IoManufacturer ||--|o OwlNamedIndividual : "sudokn_hasName"
IoManufacturer ||--|o SudoknOrganizationName : "sudokn_hasName"
IoManufacturer ||--|o SudoknNAICSClassifier : "sudokn_hasSecondaryNAICSClassifier"
IoManufacturer ||--|o OwlNamedIndividual : "sudokn_hasNAICSClassifier"
IoManufacturer ||--|o SudoknNAICSClassifier : "sudokn_hasNAICSClassifier"
IoManufacturer ||--|o RdfsLiteral : "rdfs_label"
IoManufacturer ||--|o OwlNamedIndividual : "sudokn_hasWebAddress"
IoManufacturer ||--|o SudoknWebAddress : "sudokn_hasWebAddress"
IoManufacturer ||--|o SudoknReverseEngineeringCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknCNCPlasmaCuttingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknSewingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknPressBrakingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknForgingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknExtrudingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknSwissMachiningCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknCylindricalGrindingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknChromateConversionCoatingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknCNCFormingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknTubingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknWiringCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknElectrolessPlatingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknFixtureDesignCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknSpinningCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknMechanicalJoiningCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknOilGroovingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknPlaningCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknBendingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknSurfacePreparationCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknCNCMachiningCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknDrillingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknElectrolessNickelPlatingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknPunchingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknMigWeldingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknCuttingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknCeramicMoldCastingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o Sudokn3DPrintingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknDeepFreezingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknFiberOpticLaserCuttingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknVaporizedMetalCoatingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknPressingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknFillingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknVacuumFormingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknToolMakingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknKittingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknSinkerEdmCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknEndFormingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknKnittingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknCenterlessGrindingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknTurningCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknManufacturingProcessCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknDrawingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknLaserCuttingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknPassivationCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknContinuousCastingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknInductionHeatingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknMachineBuildingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknHotDipGalvanizingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknCNCCylindricalGrindingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknSinteringCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknChemicalProcessingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknInstallationCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknBroachingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknDeburringCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknWireFormingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknPlasmaSprayingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknAssemblyCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknCNCLaserCuttingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknBrazingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknGearCuttingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknCoatingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o OwlNamedIndividual : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknHoningCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknSwissTurningCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknTubeFormingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknPrototypeManufacturingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknMIGWeldingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknGrindingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknTIGWeldingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknCNCBendingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknZincArcSprayCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknCNCTurningCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknFabricationCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknMetalSpinningCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknVacuumCastingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknRapidPrototypingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknMIGWeldinCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknCNCCuttingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknCNCGrindingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknFinishingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknSheetMetalProcessingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknLaserEtchingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknSheetMetalFabricationCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknElectricalDischargeMachiningCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknMillingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknAnodizingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknOxy-FuelCuttingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknRollingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknCastingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknPermanentMoldCastingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknElectronBeamWeldingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknElectroplatingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknThermoformingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknCarburizingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknLaserProcessingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknProductDesignCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknHardeningCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknPrintingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknMetalStampingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknWetPaintingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknBrassBlackeningCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknPackagingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknEngineeringDesignCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknShearingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknAddtiveManufacturingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknStampingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknFasteningCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknRivetingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknHorizontalMillingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknCerakoteCoatingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknSanitaryWeldingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknSolderingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknLatheWorkCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknSilkScreeningCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknAnnealingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknPLCProgrammingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknRoboticWeldingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknHeatTreatingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknAbrasiveCleaningCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknPaintingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknFormingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknElectropolishingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknSandBlastingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknWireEDMCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknFabricatingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknCADCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknMetalFabricationCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknWaterjetCuttimgCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknEmbossingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknCNCmillingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknInvestmentCastingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknTurretPunchingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknChemicalCoatingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknCNCHorizontalTurningCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknPolishingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknSandCastingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknSinkerEDMCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknCNCPressBrakeCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknPipingFabricationCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknVacuumPackagingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknSpotWeldingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknPlasticMachiningCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknPlasmaCuttingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknLiveToolingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknMachiningCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknWaterjetCuttingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknBoringCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknRamEDMCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknMechanicalAssemblyCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknCentrifugalCastingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknAcrylicFabricationCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknPlatingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknSmeltingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknCNCLatheCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknPulsedElectrochemicalMachiningCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknChemicalCleaningCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknScreenPrintingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknAdditiveManufacturingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknExtrusionCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknMediaBlastingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknSteelManufacturingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknJoiningCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknPowderCoatingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknDeepHoleDrillingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknNitridingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknSheetMetalFormingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknMetalworkingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknBlackOxideCoatingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknNotchingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknElectroPlatingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknPrototypingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknSurfaceGrindingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknFixturingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknGalvanizingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknTubeBendingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknResistanceWeldingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknEDMCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknCNCVerticalMillingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknMoldingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknShellMoldCastingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknPackingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknVacuumHardeningCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknCNCMillingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknWoodworkingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknRAMEdmCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknHarperizingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknSurfaceFinishingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknShapingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknPhysicalVaporDepositionCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknCarbonitridingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknNickelPlatingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknMoldMakingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknPlasterMoldCastingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknLaserWeldingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknCNCWireBendingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknEtchingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknKnurlingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknPhosphateCoatingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o Sudokn2-AxisCNCTurningCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknLiquidCoatingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknFlameSprayingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknWaterJetCuttingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknElectolessNickelPlatingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknPolycrystallineDiamondMachiningCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknRivettingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknPemInsertionCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknCustomFoamCuttingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknTappingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknWireHarnessAssemblyCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknDieCastingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknWoodWorkingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknReamingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknShrinkFittingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknCreepFeedGrindingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknWireBendingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknWeldingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknDigitalPrintingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknVerticalMillingCapability : "sudokn_hasProcessCapability"
IoManufacturer ||--|o SudoknDieMakingCapability : "sudokn_hasProcessCapability"
IoMaterialProduct ||--|o RdfsLiteral : "rdfs_label"
Sudokn2-AxisCNCTurningCapability ||--|o RdfsLiteral : "rdfs_label"
Sudokn3DPrintingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknAS9000Certificate ||--|o RdfsLiteral : "rdfs_label"
SudoknAS9100 ||--|o RdfsLiteral : "rdfs_label"
SudoknAS9100Certificate ||--|o IoCapability : "sudokn_attestsTo"
SudoknAS9100Certificate ||--|o OwlNamedIndividual : "sudokn_attestsTo"
SudoknAS9100Certificate ||--|o SudoknQualityManagementCapability : "sudokn_attestsTo"
SudoknAS9100Certificate ||--|o RdfsLiteral : "rdfs_label"
SudoknAS9102Certificate ||--|o RdfsLiteral : "rdfs_label"
SudoknASME ||--|o RdfsLiteral : "rdfs_label"
SudoknASMECertificate ||--|o RdfsLiteral : "rdfs_label"
SudoknAWSWelderCertificate ||--|o RdfsLiteral : "rdfs_label"
SudoknAbrasiveCleaningCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknAbrassiveMachiningCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknAcetalProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknAcrylicFabricationCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknAdditiveManufacturingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknAddtiveManufacturingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknAdhesiveBondingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknAerospaceIndustry ||--|o RdfsLiteral : "rdfs_label"
SudoknAgricultureIndustry ||--|o RdfsLiteral : "rdfs_label"
SudoknAlkalineOxideConversionCoatingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknAlloySteelProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknAluminumProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknAnnealingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknAnodizingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknApparelIndustry ||--|o RdfsLiteral : "rdfs_label"
SudoknAssemblyCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknAtomicHydrogenWeldingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknAutomotiveIndustry ||--|o RdfsLiteral : "rdfs_label"
SudoknBABACertificate ||--|o RdfsLiteral : "rdfs_label"
SudoknBeltSandingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknBendingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknBerylliumProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknBeverageIndustry ||--|o RdfsLiteral : "rdfs_label"
SudoknBlackOxideCoatingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknBoringCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknBrassBlackeningCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknBrassProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknBrazeWeldingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknBrazingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknBritishRetailConsortiumAccreditation ||--|o RdfsLiteral : "rdfs_label"
SudoknBroachingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknBronzeProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknBuffingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknBulgeFormingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknBusinessEquipmentIndustry ||--|o RdfsLiteral : "rdfs_label"
SudoknButtWeldingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknCADCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknCNCBendingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknCNCClyndricalGrindingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknCNCCuttingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknCNCCylindricalGrindingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknCNCFormingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknCNCGrindingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknCNCHorizontalTurningCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknCNCLaserCuttingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknCNCLatheCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknCNCMachiningCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknCNCMillingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknCNCPlasmaCuttingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknCNCPressBrakeCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknCNCRoutingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknCNCTurningCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknCNCVerticalMillingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknCNCWireBendingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknCNCmillingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknCarbideProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknCarbonArcBrazingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknCarbonArcWeldingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknCarbonGraphiteProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknCarbonitridingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknCarburizingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknCastingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknCenterlessGrindingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknCentrifugalCastingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknCerakoteCoatingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknCeramicMoldCastingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknCeramicProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknChemicalAndPetrochemicalIndustry ||--|o RdfsLiteral : "rdfs_label"
SudoknChemicalCleaningCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknChemicalCoatingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknChemicalConversionCoatingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknChemicalEngravingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknChemicalMachiningCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknChemicalProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknChemicalVaporDepositionCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknChemicalsProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknChromateConversionCoatingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknChromiumProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknCity ||--|o SudoknState : "sudokn_locatedInState"
SudoknCity ||--|o RdfsLiteral : "rdfs_label"
SudoknClyndricalGrindingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknCoatingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknCobaltProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknColdRolledSteelProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknCombustableGasWeldingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknCommunicationAndElectronicPowerUtilitiesIndustry ||--|o RdfsLiteral : "rdfs_label"
SudoknCommunicationIndustry ||--|o RdfsLiteral : "rdfs_label"
SudoknCommunicationandElectronicPowerUtilitiesIndustry ||--|o RdfsLiteral : "rdfs_label"
SudoknCompositeProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknCompressionMoldingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknComputerIndustry ||--|o RdfsLiteral : "rdfs_label"
SudoknComputersandElectronicProductsIndustry ||--|o RdfsLiteral : "rdfs_label"
SudoknConstructionIndustry ||--|o RdfsLiteral : "rdfs_label"
SudoknConsumerGoods ||--|o RdfsLiteral : "rdfs_label"
SudoknConsumerGoodsIndustry ||--|o RdfsLiteral : "rdfs_label"
SudoknContinuousCastingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknCopperProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknCounterBoringCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknCounterSinkingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknCreepFeedGrindingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknCurvicGrindingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknCustomFoamCuttingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknCuttingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknCyanidingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknCylindricalGrindingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknDeburringCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknDeepFreezingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknDeepHoleDrillingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknDelrinProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknDiamondMachiningCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknDieCastingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknDieMakingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknDifficultToMachineMaterialsProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknDiffusionBondingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknDiffusionHardeningCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknDigitalPrintingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknDipBrazingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknDisabledVeteranOwned ||--|o RdfsLiteral : "rdfs_label"
SudoknDrawingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknDrillingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknEDMCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknEducationIndustry ||--|o RdfsLiteral : "rdfs_label"
SudoknEducationalInstitutionsIndustry ||--|o RdfsLiteral : "rdfs_label"
SudoknElectolessNickelPlatingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknElectricArcWeldingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknElectricAutomotiveIndustry ||--|o RdfsLiteral : "rdfs_label"
SudoknElectricVehiclesIndustry ||--|o RdfsLiteral : "rdfs_label"
SudoknElectricalDischargeMachiningCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknElectricalResistanceWeldingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknElectroPlatingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknElectroSlagWeldingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknElectrolessNickelPlating ||--|o RdfsLiteral : "rdfs_label"
SudoknElectrolessNickelPlatingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknElectrolessPlatingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknElectronBeamMachiningCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknElectronBeamWeldingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknElectronicAutomotiveInudstry ||--|o RdfsLiteral : "rdfs_label"
SudoknElectronicProductIndustry ||--|o RdfsLiteral : "rdfs_label"
SudoknElectroplatingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknElectropolishingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknEmbossingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknEndFormingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknEndMillingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknEngineeringDesignCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknEngravingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknErosionMachiningCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknEtchingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknExoticMaterialProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknExplosiveWeldingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknExtremelyHardMaterialProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknExtrudingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknExtrusionCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknFDACertificate ||--|o RdfsLiteral : "rdfs_label"
SudoknFDAGMPCertificate ||--|o RdfsLiteral : "rdfs_label"
SudoknFDAGMPCompliant ||--|o RdfsLiteral : "rdfs_label"
SudoknFDAPMACertificate ||--|o RdfsLiteral : "rdfs_label"
SudoknFabricatingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknFabricationCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknFaceMillingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknFasteningCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknFiberOpticLaserCuttingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknFillingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknFinishingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknFiveAxixMachiningCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknFixtureDesignCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknFixturingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknFlameSprayingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknFluxCoredArcWeldingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknFoamProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknFoodIndustry ||--|o RdfsLiteral : "rdfs_label"
SudoknForgingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknFormingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknFrictionWeldingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknFurnaceBrazingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknFurnitureIndustry ||--|o RdfsLiteral : "rdfs_label"
SudoknFusedDepositionModelingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknFusedNitrateConversionCoatingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknGalvanizingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknGasBrazingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknGasMetalArcWeldingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknGasTungstenArcWeldingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknGasWeldingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknGearCuttingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknGearGashingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknGearHobbingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknGeospatialLocation ||--|o SudoknCity : "sudokn_locatedInCity"
SudoknGeospatialLocation ||--|o SudoknTwoDimensionalCartesianSpatialCoordinateDatum : "sudokn_hasSpatialCoordinates"
SudoknGeospatialLocation ||--|o SudoknUSPostalCode : "sudokn_hasZIPcode"
SudoknGeospatialLocation ||--|o SudoknPostalAddress : "sudokn_hasPostalAddress"
SudoknGeospatialLocation ||--|o OwlNamedIndividual : "sudokn_hasPostalAddress"
SudoknGeospatialLocation ||--|o SudoknUSPostalCode : "sudokn_hasPostalAddress"
SudoknGlassProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknGoldProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknGovermentIndustry ||--|o RdfsLiteral : "rdfs_label"
SudoknGovernmentIndustry ||--|o RdfsLiteral : "rdfs_label"
SudoknGraphiteProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknGravityCastingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknGrindingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknGunDrillingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknHAACPCertificate ||--|o RdfsLiteral : "rdfs_label"
SudoknHardeningCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknHarperizingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknHastelloyProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknHealthCareServicesIndustry ||--|o RdfsLiteral : "rdfs_label"
SudoknHealthcareServicesIndustry ||--|o RdfsLiteral : "rdfs_label"
SudoknHeatTreatingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknHighEnergyBeamMachiningCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknHighEnergyBeamWeldingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknHighGradeAluminumProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknHoleDrillingEDMCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknHoleMakingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknHoningCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknHorizontalBoringCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknHorizontalMillingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknHotDipGalvanizingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknIATF16949Certificate ||--|o RdfsLiteral : "rdfs_label"
SudoknIDODGrindingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknIS-TS16949 ||--|o RdfsLiteral : "rdfs_label"
SudoknISO13485 ||--|o RdfsLiteral : "rdfs_label"
SudoknISO13485Certificate ||--|o RdfsLiteral : "rdfs_label"
SudoknISO14000Certificate ||--|o RdfsLiteral : "rdfs_label"
SudoknISO14001 ||--|o RdfsLiteral : "rdfs_label"
SudoknISO14001Certificate ||--|o RdfsLiteral : "rdfs_label"
SudoknISO9000 ||--|o RdfsLiteral : "rdfs_label"
SudoknISO9000Certificate ||--|o IoCapability : "sudokn_attestsTo"
SudoknISO9000Certificate ||--|o OwlNamedIndividual : "sudokn_attestsTo"
SudoknISO9000Certificate ||--|o SudoknQualityManagementCapability : "sudokn_attestsTo"
SudoknISO9001 ||--|o RdfsLiteral : "rdfs_label"
SudoknISO9001Certificate ||--|o RdfsLiteral : "rdfs_label"
SudoknISOCertificate ||--|o RdfsLiteral : "rdfs_label"
SudoknISTS16949Certificate ||--|o RdfsLiteral : "rdfs_label"
SudoknITARCertificate ||--|o RdfsLiteral : "rdfs_label"
SudoknITARCompliant ||--|o RdfsLiteral : "rdfs_label"
SudoknInconelProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknInductionBrazingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknInductionHeatingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknIndustrialMachineryandEquipmentIndustry ||--|o RdfsLiteral : "rdfs_label"
SudoknIndustry ||--|o RdfsLiteral : "rdfs_label"
SudoknInfraredBrazingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknInjectionMoldingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknInstallationCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknInvarProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknInvestmentCastingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknIronProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknJoiningCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknKOSHERApproved ||--|o RdfsLiteral : "rdfs_label"
SudoknKaptonProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknKittingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknKnittingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknKnurlingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknKovarProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknLEEDCertificate ||--|o RdfsLiteral : "rdfs_label"
SudoknLabelingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknLappingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknLaserBeamWeldingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknLaserCuttingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknLaserEngravingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknLaserEtchingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknLaserProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknLaserWeldingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknLatheWorkCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknLeadProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknLexanProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknLiquidCoatingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknLiveToolingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknLostFoamCastingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknLowAlloySteelLeadProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknLowAlloySteelProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknMIGWeldinCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknMIGWeldingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknMachinaryAndEquipmentIndustry ||--|o RdfsLiteral : "rdfs_label"
SudoknMachineBuildingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknMachiningCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknMagnesiumAlloyProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknMagnesiumProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknManMadeFiberProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknMechanicalAssemblyCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknMechanicalCoatingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknMechanicalJoiningCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknMechanicalWeldingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknMediaBlastingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknMetalFabricationCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknMetalInjectionMoldingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknMetalProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknMetalProductionIndustry ||--|o RdfsLiteral : "rdfs_label"
SudoknMetalSpinningCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknMetalStampingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknMetalsProductsIndustry ||--|o RdfsLiteral : "rdfs_label"
SudoknMetalworkingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknMicroDrillingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknMigWeldingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknMilitaryIndustry ||--|o RdfsLiteral : "rdfs_label"
SudoknMillingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknMiningIndustry ||--|o RdfsLiteral : "rdfs_label"
SudoknMinorityOwned ||--|o RdfsLiteral : "rdfs_label"
SudoknMoldMakingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknMoldingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknMolybdenumProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknMultiPointCuttingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknNADCAPAC7004 ||--|o RdfsLiteral : "rdfs_label"
SudoknNADCAPCertificate ||--|o RdfsLiteral : "rdfs_label"
SudoknNativeAmericanOwned ||--|o RdfsLiteral : "rdfs_label"
SudoknNaturalFiberProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknNickelPlatingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknNickelProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknNitridingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknNomexProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknNotchingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknNylonProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknOffshoreWindIndustry ||--|o RdfsLiteral : "rdfs_label"
SudoknOilAndGasIndustry ||--|o RdfsLiteral : "rdfs_label"
SudoknOilGroovingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknOwnershipStatusClassifier ||--|o RdfsLiteral : "rdfs_label"
SudoknOxy-FuelCuttingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknOxyFuelCutting ||--|o RdfsLiteral : "rdfs_label"
SudoknPLCProgrammingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknPackagingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknPackingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknPaintingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknPalladiumProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknPaperIndustry ||--|o RdfsLiteral : "rdfs_label"
SudoknPaperandPaperboardProductsIndustry ||--|o RdfsLiteral : "rdfs_label"
SudoknPaperboardProductsIndustry ||--|o RdfsLiteral : "rdfs_label"
SudoknPassivationCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknPemInsertionCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknPercussionWeldingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknPermanentMoldCastingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknPhosBronzeProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknPhosphateCoatingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknPhosphateConversionCoatingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknPhosphorBronzeProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknPhotochemicalMachiningProcess ||--|o RdfsLiteral : "rdfs_label"
SudoknPhysicalVaporDepositionCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknPipingFabricationCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknPlaningCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknPlasmaArcWeldingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknPlasmaCuttingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknPlasmaSprayingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknPlasterMoldCastingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknPlasticAndRubberIndustry ||--|o RdfsLiteral : "rdfs_label"
SudoknPlasticMachiningCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknPlasticProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknPlasticsandRubberProductsIndustry ||--|o RdfsLiteral : "rdfs_label"
SudoknPlatingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknPlatinumProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknPlungeGrindingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknPolishingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknPolycarbonateProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknPolycrystallineDiamondMachiningCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknPowderCoatingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknPowderMetalFormingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknPreciousMaterialProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknPressBrakingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknPressFittingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknPressingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknPressureWeldingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknPrintingAndInformationIndustry ||--|o RdfsLiteral : "rdfs_label"
SudoknPrintingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknProductDesignCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknProfessionalServicesIndustry ||--|o RdfsLiteral : "rdfs_label"
SudoknProjectionWeldingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknPrototypeManufacturingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknPrototypingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknPulsedElectrochemicalMachiningCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknPunchingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknQS9000 ||--|o RdfsLiteral : "rdfs_label"
SudoknQS9000Certificate ||--|o RdfsLiteral : "rdfs_label"
SudoknRAMEdmCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknRamEDMCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknRapidPrototypingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknReactionInjectionMoldingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknReamingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknRecyclingIndustry ||--|o RdfsLiteral : "rdfs_label"
SudoknResistanceBrazingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknResistanceWeldingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknRestaurantIndustry ||--|o RdfsLiteral : "rdfs_label"
SudoknRetailIndustry ||--|o RdfsLiteral : "rdfs_label"
SudoknRetailTradeIndustry ||--|o RdfsLiteral : "rdfs_label"
SudoknReverseEngineeringCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknRivetingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknRivettingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknRoboticWeldingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknRollDieEngravingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknRollingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknRotationalMoldingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknRubberInjectionMoldingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknRubberProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknSandBlastingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknSandCastingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknSanitaryWeldingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknSawingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknScreenPrintingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknSeamWeldingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknSelectiveLaserSinteringCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknSemiconductorFabricatingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknSevenAxisMachiningCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknSewingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknShapingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknShearingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknSheeringCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknSheetMetalFabricationCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknSheetMetalFormingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknSheetMetalProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknShellMoldCastingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknShellMoldingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknShieldedMetalArcWeldingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknShotPeeningCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknShrinkFittingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknSiliconeProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknSilkScreeningCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknSilverProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknSinglePointCuttingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknSinkerEDMCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknSinkerEdmCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknSinteringCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknSlabMillingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknSmallDisadvantagedBusiness ||--|o RdfsLiteral : "rdfs_label"
SudoknSmallHoleDrillingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknSmeltingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknSolderingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknSparkPlasmaSinteringCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknSpecialMaterialsProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknSpinningCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknSportsAndLeisureIndustry ||--|o RdfsLiteral : "rdfs_label"
SudoknSportsandLeisureIndustry ||--|o RdfsLiteral : "rdfs_label"
SudoknSpotWeldingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknSqueezeCastingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknStainlessSteelProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknStampingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknState ||--|o RdfsLiteral : "rdfs_label"
SudoknSteelAlloyProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknSteelManufacturingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknSteelProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknStereolithographyCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknStretchFormingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknStudWeldingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknSubmergedArcWeldingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknSuperAlloyProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknSurfaceFinishingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknSurfaceGrindingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknSurfaceHardeningCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknSurfacePreparationCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknSwissMachiningCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknSwissTurningCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknTI9000Certificate ||--|o RdfsLiteral : "rdfs_label"
SudoknTIGWeldingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknTantalumProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknTappingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknTeflonProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknTextiles ||--|o RdfsLiteral : "rdfs_label"
SudoknTextilesIndustry ||--|o RdfsLiteral : "rdfs_label"
SudoknThermaJoiningCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknThermalCoatingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknThermalSprayCoatingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknThermalSubtractionCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknThermalWeldingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknThermoformingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknThreadMillingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknThreadingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknTinProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknTitaniumProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknToolMakingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknTorchBrazingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknTorchCuttingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknTransferMoldingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknTransportationIndustry ||--|o RdfsLiteral : "rdfs_label"
SudoknTubeBendingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknTubeFormingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknTubingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknTungstenProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknTurningCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknTurretPunchingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknUltrasonicCleaningCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknUltrasonicWeldingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknUrethaneProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknUtilitiesIndustry ||--|o RdfsLiteral : "rdfs_label"
SudoknVacuumCastingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknVacuumFormingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknVacuumHardeningCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknVacuumMoldingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknVacuumPackagingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknVacuumPressingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknVaporizedMetalCoatingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknVerticalMillingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknVeteranOwned ||--|o RdfsLiteral : "rdfs_label"
SudoknWarehousingAndStorageIndustry ||--|o RdfsLiteral : "rdfs_label"
SudoknWaspaloyProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknWaterAndSewerUtilitiesIndustry ||--|o RdfsLiteral : "rdfs_label"
SudoknWaterJetCuttingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknWaterandSewerUtilitiesIndustry ||--|o RdfsLiteral : "rdfs_label"
SudoknWaterjetCuttimgCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknWaterjetCuttingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknWeldingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknWetPaintingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknWireBendingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknWireEDMCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknWireFormingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknWireHarnessAssemblyCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknWiringCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknWomenOwned ||--|o RdfsLiteral : "rdfs_label"
SudoknWoodProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknWoodProductManufacturingIndustry ||--|o RdfsLiteral : "rdfs_label"
SudoknWoodWorkingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknWoodworkingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknZeroStockMachiningCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknZincAlloyProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknZincArcSprayCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknZincProcessingCapability ||--|o RdfsLiteral : "rdfs_label"
SudoknZirconProcessingCapability ||--|o RdfsLiteral : "rdfs_label"

```



## Imports


* okns:extended_types
* linkml:types
* okns:owl-rdf-rdfs



## Classes

| Class | Description | Occurrences |
| --- | --- | --- |
| [IoCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/IoCapability.md) | None<br/>|  | 
| [IoGroupOfPersons](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/IoGroupOfPersons.md) | None<br/>|  | 
| [IoIdentifier](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/IoIdentifier.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknDesignativeName](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknDesignativeName.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknBrandName](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknBrandName.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknOrganizationName](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknOrganizationName.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknVitualLocationIdentifier](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknVitualLocationIdentifier.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknEmailAddress](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknEmailAddress.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknWebAddress](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknWebAddress.md) | None<br/>| 1 | 
| [IoInformationContentEntity](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/IoInformationContentEntity.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknBusinessDescription](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknBusinessDescription.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCertificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCertificate.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknOccupationalHealthAndSafetyCertificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknOccupationalHealthAndSafetyCertificate.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknISO45001Certificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknISO45001Certificate.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknOHSAS18001Certificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknOHSAS18001Certificate.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknProfessionalCertificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknProfessionalCertificate.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknAWSWelderCertificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknAWSWelderCertificate.md) | None<br/>| 48 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknQualityCertificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknQualityCertificate.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknASCertificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknASCertificate.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknAS9000Certificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknAS9000Certificate.md) | None<br/>| 5 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknAS9003Certificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknAS9003Certificate.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknAS9100Certificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknAS9100Certificate.md) | None<br/>| 1220 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknAS9102Certificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknAS9102Certificate.md) | None<br/>| 9 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknAS9120Certificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknAS9120Certificate.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknASMECertificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknASMECertificate.md) | None<br/>| 804 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknBABACertificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknBABACertificate.md) | None<br/>| 3 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknBritishRetailConsortiumCertificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknBritishRetailConsortiumCertificate.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknFDACertificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknFDACertificate.md) | None<br/>| 5 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknFDAGMPCertificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknFDAGMPCertificate.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknFDAPMACertificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknFDAPMACertificate.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknGWOCertificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknGWOCertificate.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknHAACPCertificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknHAACPCertificate.md) | None<br/>| 2 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknIATFCertificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknIATFCertificate.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknIATF16949Certificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknIATF16949Certificate.md) | None<br/>| 330 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknISOQualityCertificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknISOQualityCertificate.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknISO13485Certificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknISO13485Certificate.md) | None<br/>| 326 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknISO14000Certificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknISO14000Certificate.md) | None<br/>| 12 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknISO14001Certificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknISO14001Certificate.md) | None<br/>| 321 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknISO17265Certificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknISO17265Certificate.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknISO27001Certificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknISO27001Certificate.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknISO9000Certificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknISO9000Certificate.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknISO9001Certificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknISO9001Certificate.md) | None<br/>| 3466 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknISTSCertificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknISTSCertificate.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknISTS16949Certificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknISTS16949Certificate.md) | None<br/>| 4 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknITARCertificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknITARCertificate.md) | None<br/>| 127 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknKosherApprovedCertificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknKosherApprovedCertificate.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNADCAPCertificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNADCAPCertificate.md) | None<br/>| 467 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNISTCertificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNISTCertificate.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNIST800171Certificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNIST800171Certificate.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknQSCertificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknQSCertificate.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknQS9000Certificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknQS9000Certificate.md) | None<br/>| 41 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknTICertificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknTICertificate.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknTI-9000Certificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknTI-9000Certificate.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknSustainabilityCertificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSustainabilityCertificate.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknLEEDCertificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknLEEDCertificate.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknClassifier](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknClassifier.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICSClassifier](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICSClassifier.md) | None<br/>| 23 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS33](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS33.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS331](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS331.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS331110](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS331110.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS331210](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS331210.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS331221](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS331221.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS331222](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS331222.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS331313](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS331313.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS331314](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS331314.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS331315](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS331315.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS331318](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS331318.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS331410](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS331410.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS331420](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS331420.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS331491](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS331491.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS331492](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS331492.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS331511](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS331511.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS331512](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS331512.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS331513](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS331513.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS331523](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS331523.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS331524](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS331524.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS331529](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS331529.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS332](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS332111](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332111.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS332112](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332112.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS332114](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332114.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS332117](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332117.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS332119](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332119.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS332215](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332215.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS332216](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332216.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS332311](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332311.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS332312](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332312.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS332313](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332313.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS332321](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332321.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS332322](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332322.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS332323](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332323.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS332410](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332410.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS332420](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332420.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS332431](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332431.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS332439](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332439.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS332510](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332510.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS332613](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332613.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS332618](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332618.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS332710](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332710.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS332721](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332721.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS332722](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332722.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS332811](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332811.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS332812](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332812.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS332813](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332813.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS332911](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332911.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS332912](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332912.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS332913](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332913.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS332919](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332919.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS332991](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332991.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS332992](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332992.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS333](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS333.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS332993](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332993.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS332994](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332994.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS332996](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332996.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS332999](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332999.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS333111](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS333111.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS333112](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS333112.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS333120](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS333120.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS333131](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS333131.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS333132](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS333132.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS333241](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS333241.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS333242](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS333242.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS333243](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS333243.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS333248](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS333248.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS333310](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS333310.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS333413](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS333413.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS333414](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS333414.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS333415](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS333415.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS333511](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS333511.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS333514](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS333514.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS333515](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS333515.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS333517](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS333517.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS333519](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS333519.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS333611](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS333611.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS333612](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS333612.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS333613](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS333613.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS333618](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS333618.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS333912](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS333912.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS333914](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS333914.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS333921](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS333921.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS333922](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS333922.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS333923](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS333923.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS333924](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS333924.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS333991](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS333991.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS333992](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS333992.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS333993](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS333993.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS333994](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS333994.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS333995](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS333995.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS333996](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS333996.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS333998](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS333998.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS334](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS334.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS334111](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS334111.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS334112](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS334112.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS334118](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS334118.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS334210](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS334210.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS334220](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS334220.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS334290](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS334290.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS334310](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS334310.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS334412](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS334412.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS334413](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS334413.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS334416](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS334416.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS334417](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS334417.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS334418](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS334418.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS334419](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS334419.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS334510](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS334510.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS334511](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS334511.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS334512](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS334512.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS334513](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS334513.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS334514](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS334514.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS334515](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS334515.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS334516](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS334516.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS334517](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS334517.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS334519](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS334519.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS334610](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS334610.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS335](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS335.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS335131](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS335131.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS335132](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS335132.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS335139](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS335139.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS335210](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS335210.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS335220](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS335220.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS335311](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS335311.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS335312](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS335312.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS335313](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS335313.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS335314](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS335314.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS335910](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS335910.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS335921](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS335921.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS335929](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS335929.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS335931](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS335931.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS335932](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS335932.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS335991](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS335991.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS335999](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS335999.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS336](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS336.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknAICS336999](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknAICS336999.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS336110](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS336110.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS336120](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS336120.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS336211](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS336211.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS336212](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS336212.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS336213](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS336213.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS336214](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS336214.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS336310](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS336310.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS336320](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS336320.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS336330](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS336330.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS336340](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS336340.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS336350](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS336350.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS336360](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS336360.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS336370](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS336370.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS336390](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS336390.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS336411](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS336411.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS336412](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS336412.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS336413](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS336413.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS336414](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS336414.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS336415](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS336415.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS336419](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS336419.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS336510](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS336510.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS336611](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS336611.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS336612](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS336612.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS336991](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS336991.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS336992](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS336992.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS337](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS337.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS337110](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS337110.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS337121](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS337121.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS337122](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS337122.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS337126](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS337126.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS337127](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS337127.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS337211](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS337211.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS337212](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS337212.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS337214](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS337214.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS337215](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS337215.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS337910](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS337910.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS337920](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS337920.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS339](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS339.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS339112](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS339112.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS339113](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS339113.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS339114](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS339114.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS339115](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS339115.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS339116](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS339116.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS339910](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS339910.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS339920](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS339920.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS339930](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS339930.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS339940](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS339940.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS339950](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS339950.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS339991](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS339991.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS339992](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS339992.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS339993](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS339993.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS339994](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS339994.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS339995](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS339995.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNAICS339999](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS339999.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknSpecialBusinessStatusClassifier](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSpecialBusinessStatusClassifier.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknOwnershipStatusClassifier](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknOwnershipStatusClassifier.md) | None<br/>| 6 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknDisabledVeteranOwned](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknDisabledVeteranOwned.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknMinorityOwned](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMinorityOwned.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNativeAmericanOwned](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNativeAmericanOwned.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknSmallDisadvantagedBusiness](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSmallDisadvantagedBusiness.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknVeteranOwned](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknVeteranOwned.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknWomenOwned](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknWomenOwned.md) | None<br/>|  | 
| [IoManufacturer](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/IoManufacturer.md) | None<br/>| 11367 | 
| [IoMaterialProduct](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/IoMaterialProduct.md) | None<br/>| 44818 | 
| [IoOrganization](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/IoOrganization.md) | None<br/>|  | 
| [IoPhysicalLocationIdentifier](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/IoPhysicalLocationIdentifier.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknBuildingNumber](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknBuildingNumber.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCityOfAddress](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCityOfAddress.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCountryOfAddress](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCountryOfAddress.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknPostalAddress](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPostalAddress.md) | None<br/>| 20728 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknStateOfAddress](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknStateOfAddress.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknStreetAddress](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknStreetAddress.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknTwoDimensionalCartesianSpatialCoordinateDatum](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknTwoDimensionalCartesianSpatialCoordinateDatum.md) | None<br/>| 20728 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknUSPostalCode](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknUSPostalCode.md) | None<br/>| 20425 | 
| [IoscGeospatialSite](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/IoscGeospatialSite.md) | None<br/>|  | 
| [IoscIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/IoscIndustry.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknAerospaceIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknAerospaceIndustry.md) | None<br/>| 2 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknAgricultureIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknAgricultureIndustry.md) | None<br/>| 2 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknApparelIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknApparelIndustry.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknAutomotiveIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknAutomotiveIndustry.md) | None<br/>| 2 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknElectricAutomotiveIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknElectricAutomotiveIndustry.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknBusinessEquipmentIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknBusinessEquipmentIndustry.md) | None<br/>| 2 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknChemicalAndPetrochemicalIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknChemicalAndPetrochemicalIndustry.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCommunicationsIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCommunicationsIndustry.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknConstructionIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknConstructionIndustry.md) | None<br/>| 2 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknConsumerGoodsIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknConsumerGoodsIndustry.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknEducationIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknEducationIndustry.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknElectronicProductIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknElectronicProductIndustry.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknComputerIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknComputerIndustry.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknEnergyIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknEnergyIndustry.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCoalIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCoalIndustry.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNuclearEnergyIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNuclearEnergyIndustry.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknOilAndGasIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknOilAndGasIndustry.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknRenewableEnergyIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknRenewableEnergyIndustry.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknOffshoreWindIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknOffshoreWindIndustry.md) | None<br/>| 2 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknFoodIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknFoodIndustry.md) | None<br/>| 2 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknBeverageIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknBeverageIndustry.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknRestaurantIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknRestaurantIndustry.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknFurnitureIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknFurnitureIndustry.md) | None<br/>| 2 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknGovernmentIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknGovernmentIndustry.md) | None<br/>| 2 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknHealthcareServices](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknHealthcareServices.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknInformationTechnologyIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknInformationTechnologyIndustry.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknMachinaryAndEquipmentIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMachinaryAndEquipmentIndustry.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknMetalProductsIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMetalProductsIndustry.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknMilitaryIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMilitaryIndustry.md) | None<br/>| 2 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknMiningIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMiningIndustry.md) | None<br/>| 2 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknPaperIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPaperIndustry.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknPaperboardProductsIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPaperboardProductsIndustry.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknPharmaceuticalIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPharmaceuticalIndustry.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknPlasticAndRubberIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPlasticAndRubberIndustry.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknPrintingAndInformationIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPrintingAndInformationIndustry.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknProfessionalServicesIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknProfessionalServicesIndustry.md) | None<br/>| 2 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknRecyclingIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknRecyclingIndustry.md) | None<br/>| 2 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknRetailIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknRetailIndustry.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknSportsAndLeisureIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSportsAndLeisureIndustry.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknTextilesIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknTextilesIndustry.md) | None<br/>| 2 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknTransportationIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknTransportationIndustry.md) | None<br/>| 2 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknUtilitiesIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknUtilitiesIndustry.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCommunicationAndElectronicPowerUtilitiesIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCommunicationAndElectronicPowerUtilitiesIndustry.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknWaterAndSewerUtilitiesIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknWaterAndSewerUtilitiesIndustry.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknWarehousingAndStorage](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknWarehousingAndStorage.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknWoodProductManufacturingIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknWoodProductManufacturingIndustry.md) | None<br/>| 1 | 
| [IoscProductionCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/IoscProductionCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknEngineeringCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknEngineeringCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCADCAMCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCADCAMCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCADCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCADCapability.md) | None<br/>| 3 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCAECapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCAECapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCAMCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCAMCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknEngineeringDesignCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknEngineeringDesignCapability.md) | None<br/>| 28 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknPLCProgrammingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPLCProgrammingCapability.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknRapidPrototypingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknRapidPrototypingCapability.md) | None<br/>| 256 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknReverseEngineeringCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknReverseEngineeringCapability.md) | None<br/>| 2 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknToolDesignCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknToolDesignCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknDieDesignCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknDieDesignCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknFixtureDesignCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknFixtureDesignCapability.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknMoldDesignCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMoldDesignCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknManufacturingProcessCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknManufacturingProcessCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknAdditiveManufacturingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknAdditiveManufacturingCapability.md) | None<br/>| 209 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknFusedDepositionModelingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknFusedDepositionModelingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknSelectiveLaserSinteringCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSelectiveLaserSinteringCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknStereolithographyCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknStereolithographyCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknAssemblyCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknAssemblyCapability.md) | None<br/>| 2932 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknFabricatingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknFabricatingCapability.md) | None<br/>| 2518 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknSemiconductorFabricatingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSemiconductorFabricatingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknKittingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknKittingCapability.md) | None<br/>| 2 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknWireHarnessAssemblyCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknWireHarnessAssemblyCapability.md) | None<br/>| 23 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCastingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCastingCapability.md) | None<br/>| 1195 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCentrifugalCastingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCentrifugalCastingCapability.md) | None<br/>| 17 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCeramicMoldCastingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCeramicMoldCastingCapability.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknContinuousCastingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknContinuousCastingCapability.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknDieCastingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknDieCastingCapability.md) | None<br/>| 220 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknGravityCastingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknGravityCastingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknPermanentMoldCastingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPermanentMoldCastingCapability.md) | None<br/>| 10 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknInvestmentCastingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknInvestmentCastingCapability.md) | None<br/>| 83 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknLostFoamCastingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknLostFoamCastingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknPlasterMoldCastingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPlasterMoldCastingCapability.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknSandCastingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSandCastingCapability.md) | None<br/>| 4 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknShellMoldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknShellMoldingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknSqueezeCastingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSqueezeCastingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknVacuumCastingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknVacuumCastingCapability.md) | None<br/>| 16 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknChemicalProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknChemicalProcessingCapability.md) | None<br/>| 194 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknForgingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknForgingCapability.md) | None<br/>| 609 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknFormingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknFormingCapability.md) | None<br/>| 1802 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknDrawingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknDrawingCapability.md) | None<br/>| 1449 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknExtrudingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknExtrudingCapability.md) | None<br/>| 602 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknKnurlingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknKnurlingCapability.md) | None<br/>| 64 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknPowderMetalFormingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPowderMetalFormingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknSparkPlasmaSinteringCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSparkPlasmaSinteringCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknRollDieEngravingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknRollDieEngravingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknRollingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknRollingCapability.md) | None<br/>| 605 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknThermoformingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknThermoformingCapability.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknVacuumPressingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknVacuumPressingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknTubingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknTubingCapability.md) | None<br/>| 533 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknHeatTreatingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknHeatTreatingCapability.md) | None<br/>| 923 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknAnnealingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknAnnealingCapability.md) | None<br/>| 99 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknHardeningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknHardeningCapability.md) | None<br/>| 269 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknSurfaceHardeningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSurfaceHardeningCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCyanidingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCyanidingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknDiffusionHardeningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknDiffusionHardeningCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCarbonitridingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCarbonitridingCapability.md) | None<br/>| 43 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCarburizingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCarburizingCapability.md) | None<br/>| 81 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNitridingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNitridingCapability.md) | None<br/>| 45 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknVacuumHardeningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknVacuumHardeningCapability.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknSinteringCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSinteringCapability.md) | None<br/>| 56 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknJoiningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknJoiningCapability.md) | None<br/>| 437 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknAdhesiveBondingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknAdhesiveBondingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknMechanicalJoiningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMechanicalJoiningCapability.md) | None<br/>| 3 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknMechanicalWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMechanicalWeldingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknExplosiveWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknExplosiveWeldingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknFrictionWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknFrictionWeldingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknPressureWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPressureWeldingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknUltrasonicWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknUltrasonicWeldingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknPressFittingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPressFittingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknShrinkFittingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknShrinkFittingCapability.md) | None<br/>| 9 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknRivetingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknRivetingCapability.md) | None<br/>| 2 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknThermaJoiningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknThermaJoiningCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknBrazingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknBrazingCapability.md) | None<br/>| 147 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknDipBrazingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknDipBrazingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknFurnaceBrazingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknFurnaceBrazingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknInductionBrazingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknInductionBrazingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknInfraredBrazingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknInfraredBrazingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknResistanceBrazingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknResistanceBrazingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknTorchBrazingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknTorchBrazingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknSolderingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSolderingCapability.md) | None<br/>| 271 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknThermalWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknThermalWeldingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknBrazeWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknBrazeWeldingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCarbonArcBrazingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCarbonArcBrazingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknGasBrazingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknGasBrazingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknDiffusionBondingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknDiffusionBondingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknElectricalResistanceWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknElectricalResistanceWeldingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknButtWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknButtWeldingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknElectroSlagWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknElectroSlagWeldingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknPercussionWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPercussionWeldingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknProjectionWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknProjectionWeldingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknSeamWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSeamWeldingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknSpotWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSpotWeldingCapability.md) | None<br/>| 3 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknElectricArcWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknElectricArcWeldingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCarbonArcWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCarbonArcWeldingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknFluxCoredArcWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknFluxCoredArcWeldingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknGasMetalArcWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknGasMetalArcWeldingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknMIGWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMIGWeldingCapability.md) | None<br/>| 2 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknGasTungstenArcWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknGasTungstenArcWeldingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknTIGWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknTIGWeldingCapability.md) | None<br/>| 3 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknShieldedMetalArcWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknShieldedMetalArcWeldingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknStudWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknStudWeldingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknSubmergedArcWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSubmergedArcWeldingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknGasWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknGasWeldingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknAtomicHydrogenWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknAtomicHydrogenWeldingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCombustableGasWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCombustableGasWeldingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknHighEnergyBeamWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknHighEnergyBeamWeldingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknElectronBeamWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknElectronBeamWeldingCapability.md) | None<br/>| 6 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknLaserBeamWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknLaserBeamWeldingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknPlasmaArcWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPlasmaArcWeldingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknMachiningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMachiningCapability.md) | None<br/>| 3494 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknAbrassiveMachiningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknAbrassiveMachiningCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknBuffingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknBuffingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknGrindingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknGrindingCapability.md) | None<br/>| 1654 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCenterlessGrindingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCenterlessGrindingCapability.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknClyndricalGrindingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknClyndricalGrindingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCNCClyndricalGrindingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCNCClyndricalGrindingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCreepFeedGrindingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCreepFeedGrindingCapability.md) | None<br/>| 8 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCurvicGrindingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCurvicGrindingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknIDODGrindingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknIDODGrindingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknPlungeGrindingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPlungeGrindingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknHoningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknHoningCapability.md) | None<br/>| 460 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknLappingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknLappingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknChemicalMachiningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknChemicalMachiningCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknChemicalEngravingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknChemicalEngravingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknEtchingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknEtchingCapability.md) | None<br/>| 487 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknPhotochemicalMachiningProcess](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPhotochemicalMachiningProcess.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCNCMachiningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCNCMachiningCapability.md) | None<br/>| 1427 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCNCRoutingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCNCRoutingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknFiveAxixMachiningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknFiveAxixMachiningCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknSevenAxisMachiningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSevenAxisMachiningCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknDeburringCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknDeburringCapability.md) | None<br/>| 86 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknEngravingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknEngravingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknLaserEngravingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknLaserEngravingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknErosionMachiningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknErosionMachiningCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknWaterjetCuttingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknWaterjetCuttingCapability.md) | None<br/>| 373 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknMultiPointCuttingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMultiPointCuttingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknBroachingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknBroachingCapability.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknGearCuttingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknGearCuttingCapability.md) | None<br/>| 2 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknGearHobbingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknGearHobbingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknHoleMakingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknHoleMakingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCounterBoringCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCounterBoringCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCounterSinkingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCounterSinkingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknDrillingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknDrillingCapability.md) | None<br/>| 1361 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknDeepHoleDrillingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknDeepHoleDrillingCapability.md) | None<br/>| 81 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknGunDrillingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknGunDrillingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknMicroDrillingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMicroDrillingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknSmallHoleDrillingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSmallHoleDrillingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknReamingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknReamingCapability.md) | None<br/>| 278 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknTappingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknTappingCapability.md) | None<br/>| 860 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknMillingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMillingCapability.md) | None<br/>| 2311 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCNCMillingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCNCMillingCapability.md) | None<br/>| 1105 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknGearGashingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknGearGashingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknHorizontalMillingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknHorizontalMillingCapability.md) | None<br/>| 181 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknSlabMillingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSlabMillingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknThreadMillingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknThreadMillingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknVerticalMillingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknVerticalMillingCapability.md) | None<br/>| 437 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknEndMillingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknEndMillingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknFaceMillingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknFaceMillingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknSawingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSawingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknPlasticMachiningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPlasticMachiningCapability.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknPolycrystallineDiamondMachiningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPolycrystallineDiamondMachiningCapability.md) | None<br/>| 70 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknSinglePointCuttingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSinglePointCuttingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknDiamondMachiningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknDiamondMachiningCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknOilGroovingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknOilGroovingCapability.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknPlaningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPlaningCapability.md) | None<br/>| 17 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknShapingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknShapingCapability.md) | None<br/>| 504 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknTurningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknTurningCapability.md) | None<br/>| 2077 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknBoringCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknBoringCapability.md) | None<br/>| 857 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknHorizontalBoringCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknHorizontalBoringCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCNCTurningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCNCTurningCapability.md) | None<br/>| 16 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknLiveToolingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknLiveToolingCapability.md) | None<br/>| 287 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknSwissMachiningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSwissMachiningCapability.md) | None<br/>| 19 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknThermalSubtractionCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknThermalSubtractionCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknEDMCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknEDMCapability.md) | None<br/>| 1114 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknHoleDrillingEDMCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknHoleDrillingEDMCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknRamEDMCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknRamEDMCapability.md) | None<br/>| 28 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknSinkerEDMCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSinkerEDMCapability.md) | None<br/>| 148 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknWireEDMCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknWireEDMCapability.md) | None<br/>| 644 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknHighEnergyBeamMachiningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknHighEnergyBeamMachiningCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknElectronBeamMachiningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknElectronBeamMachiningCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknLaserCuttingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknLaserCuttingCapability.md) | None<br/>| 581 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCNCLaserCuttingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCNCLaserCuttingCapability.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknLaserEtchingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknLaserEtchingCapability.md) | None<br/>| 81 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknTorchCuttingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknTorchCuttingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknOxyFuelCutting](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknOxyFuelCutting.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknPlasmaCuttingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPlasmaCuttingCapability.md) | None<br/>| 235 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknThreadingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknThreadingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknZeroStockMachiningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknZeroStockMachiningCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknMoldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMoldingCapability.md) | None<br/>| 644 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCompressionMoldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCompressionMoldingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknInjectionMoldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknInjectionMoldingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknMetalInjectionMoldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMetalInjectionMoldingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknReactionInjectionMoldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknReactionInjectionMoldingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknRubberInjectionMoldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknRubberInjectionMoldingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknRotationalMoldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknRotationalMoldingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknTransferMoldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknTransferMoldingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknVacuumMoldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknVacuumMoldingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknPackingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPackingCapability.md) | None<br/>| 1765 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknLabelingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknLabelingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknVacuumPackagingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknVacuumPackagingCapability.md) | None<br/>| 2 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknSheetMetalProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSheetMetalProcessingCapability.md) | None<br/>| 28 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknBendingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknBendingCapability.md) | None<br/>| 945 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknTubeBendingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknTubeBendingCapability.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknWireBendingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknWireBendingCapability.md) | None<br/>| 3 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknBulgeFormingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknBulgeFormingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknEmbossingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknEmbossingCapability.md) | None<br/>| 69 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNotchingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNotchingCapability.md) | None<br/>| 109 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknPunchingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPunchingCapability.md) | None<br/>| 7 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknSheeringCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSheeringCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknSpinningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSpinningCapability.md) | None<br/>| 38 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknStampingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknStampingCapability.md) | None<br/>| 1216 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknStretchFormingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknStretchFormingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknSurfaceFinishingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSurfaceFinishingCapability.md) | None<br/>| 77 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCoatingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCoatingCapability.md) | None<br/>| 1744 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknBlackOxideCoatingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknBlackOxideCoatingCapability.md) | None<br/>| 228 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknChemicalCoatingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknChemicalCoatingCapability.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknAnodizingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknAnodizingCapability.md) | None<br/>| 659 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknChemicalConversionCoatingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknChemicalConversionCoatingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknAlkalineOxideConversionCoatingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknAlkalineOxideConversionCoatingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknChromateConversionCoatingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknChromateConversionCoatingCapability.md) | None<br/>| 139 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknFusedNitrateConversionCoatingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknFusedNitrateConversionCoatingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknPhosphateConversionCoatingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPhosphateConversionCoatingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknPlatingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPlatingCapability.md) | None<br/>| 2 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknElectroPlatingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknElectroPlatingCapability.md) | None<br/>| 1339 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknElectrolessNickelPlating](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknElectrolessNickelPlating.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknGalvanizingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknGalvanizingCapability.md) | None<br/>| 72 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknMechanicalCoatingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMechanicalCoatingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknPowderCoatingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPowderCoatingCapability.md) | None<br/>| 679 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknPassivationCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPassivationCapability.md) | None<br/>| 280 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknPhosphateCoatingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPhosphateCoatingCapability.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknPrintingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPrintingCapability.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknWetPaintingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknWetPaintingCapability.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknThermalCoatingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknThermalCoatingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknThermalSprayCoatingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknThermalSprayCoatingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknFlameSprayingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknFlameSprayingCapability.md) | None<br/>| 6 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknPlasmaSprayingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPlasmaSprayingCapability.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknVaporizedMetalCoatingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknVaporizedMetalCoatingCapability.md) | None<br/>| 13 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknChemicalVaporDepositionCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknChemicalVaporDepositionCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknPhysicalVaporDepositionCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPhysicalVaporDepositionCapability.md) | None<br/>| 10 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknSurfacePreparationCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSurfacePreparationCapability.md) | None<br/>| 550 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknBeltSandingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknBeltSandingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknHarperizingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknHarperizingCapability.md) | None<br/>| 2 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknPolishingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPolishingCapability.md) | None<br/>| 456 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknElectropolishingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknElectropolishingCapability.md) | None<br/>| 61 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknSandBlastingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSandBlastingCapability.md) | None<br/>| 340 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknShotPeeningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknShotPeeningCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknUltrasonicCleaningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknUltrasonicCleaningCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknTextileProcessCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknTextileProcessCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCrochetCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCrochetCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknDyeingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknDyeingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknKnittingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknKnittingCapability.md) | None<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknWeavingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknWeavingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknToolMakingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknToolMakingCapability.md) | None<br/>| 6 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknMoldMakingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMoldMakingCapability.md) | None<br/>| 8 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknWoodWorkingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknWoodWorkingCapability.md) | None<br/>| 12 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknMaterialProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMaterialProcessingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCarbideProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCarbideProcessingCapability.md) | None<br/>| 786 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCarbonProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCarbonProcessingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknGraphiteProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknGraphiteProcessingCapability.md) | None<br/>| 472 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCeramicProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCeramicProcessingCapability.md) | None<br/>| 1051 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknChemicalsProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknChemicalsProcessingCapability.md) | None<br/>| 1344 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCompositeProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCompositeProcessingCapability.md) | None<br/>| 1196 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknElectronicProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknElectronicProcessingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknExoticMaterialProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknExoticMaterialProcessingCapability.md) | None<br/>| 317 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknFiberProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknFiberProcessingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknManMadeFiberProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknManMadeFiberProcessingCapability.md) | None<br/>| 2 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNaturalFiberProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNaturalFiberProcessingCapability.md) | None<br/>| 15 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknFoamProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknFoamProcessingCapability.md) | None<br/>| 1065 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknGlassProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknGlassProcessingCapability.md) | None<br/>| 2866 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknMetalProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMetalProcessingCapability.md) | None<br/>| 6560 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknAluminumProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknAluminumProcessingCapability.md) | None<br/>| 5647 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknBerylliumProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknBerylliumProcessingCapability.md) | None<br/>| 360 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknBrassProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknBrassProcessingCapability.md) | None<br/>| 2596 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknBronzeProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknBronzeProcessingCapability.md) | None<br/>| 1754 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknPhosphorBronzeProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPhosphorBronzeProcessingCapability.md) | phosphor bronze processing capability<br/>| 1 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknChromiumProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknChromiumProcessingCapability.md) | None<br/>| 551 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCobaltProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCobaltProcessingCapability.md) | None<br/>| 303 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCopperProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCopperProcessingCapability.md) | None<br/>| 2784 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknHastelloyProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknHastelloyProcessingCapability.md) | None<br/>| 321 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknInconelProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknInconelProcessingCapability.md) | None<br/>| 906 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknInvarProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknInvarProcessingCapability.md) | None<br/>| 219 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknIronProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknIronProcessingCapability.md) | None<br/>| 5903 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknKaptonProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknKaptonProcessingCapability.md) | None<br/>| 32 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknKovarProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknKovarProcessingCapability.md) | None<br/>| 197 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknLeadProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknLeadProcessingCapability.md) | None<br/>| 2484 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknLexanProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknLexanProcessingCapability.md) | None<br/>| 461 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknMagnesiumAlloyProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMagnesiumAlloyProcessingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknMolybdenumProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMolybdenumProcessingCapability.md) | None<br/>| 382 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknNickelProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNickelProcessingCapability.md) | None<br/>| 1603 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknPalladiumProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPalladiumProcessingCapability.md) | None<br/>| 78 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknPlatinumProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPlatinumProcessingCapability.md) | None<br/>| 225 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknSilverProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSilverProcessingCapability.md) | None<br/>| 1251 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknSteelProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSteelProcessingCapability.md) | None<br/>| 7200 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknAlloySteelProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknAlloySteelProcessingCapability.md) | None<br/>| 825 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknLowAlloySteelLeadProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknLowAlloySteelLeadProcessingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknColdRolledSteelProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknColdRolledSteelProcessingCapability.md) | None<br/>| 252 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknStainlessSteelProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknStainlessSteelProcessingCapability.md) | None<br/>| 4796 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknSuperAlloyProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSuperAlloyProcessingCapability.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknWaspaloyProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknWaspaloyProcessingCapability.md) | None<br/>| 66 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknTitaniumProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknTitaniumProcessingCapability.md) | None<br/>| 1349 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknTungstenProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknTungstenProcessingCapability.md) | None<br/>| 820 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknZincAlloyProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknZincAlloyProcessingCapability.md) | None<br/>| 80 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknPlasticProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPlasticProcessingCapability.md) | None<br/>| 4159 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknAcetalProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknAcetalProcessingCapability.md) | None<br/>| 362 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknDelrinProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknDelrinProcessingCapability.md) | None<br/>| 289 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknPolycarbonateProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPolycarbonateProcessingCapability.md) | None<br/>| 693 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknRubberProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknRubberProcessingCapability.md) | None<br/>| 1830 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknSiliconeProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSiliconeProcessingCapability.md) | None<br/>| 690 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknTeflonProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknTeflonProcessingCapability.md) | None<br/>| 538 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknUrethaneProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknUrethaneProcessingCapability.md) | None<br/>| 1039 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknWoodProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknWoodProcessingCapability.md) | None<br/>| 2918 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknQualityManagementCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknQualityManagementCapability.md) | None<br/>| 1 | 
| [OboBFO0000019](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/OboBFO0000019.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknOrganizationSize](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknOrganizationSize.md) | None<br/>| 1 | 
| [OboBFO0000029](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/OboBFO0000029.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknGeopoliticalSite](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknGeopoliticalSite.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCity](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCity.md) | None<br/>| 2994 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCountry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCountry.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknCounty](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCounty.md) | None<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SudoknState](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknState.md) | None<br/>| 129 | 
| [Sudokn2-AxisCNCTurningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/Sudokn2-AxisCNCTurningCapability.md) | None<br/>| 1 | 
| [Sudokn3DPrintingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/Sudokn3DPrintingCapability.md) | None<br/>| 1 | 
| [SudoknAbrasiveCleaningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknAbrasiveCleaningCapability.md) | None<br/>| 9 | 
| [SudoknAcrylicFabricationCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknAcrylicFabricationCapability.md) | None<br/>| 1 | 
| [SudoknAddtiveManufacturingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknAddtiveManufacturingCapability.md) | None<br/>| 337 | 
| [SudoknAS9100](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknAS9100.md) | None<br/>| 20 | 
| [SudoknASME](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknASME.md) | None<br/>| 10 | 
| [SudoknBrassBlackeningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknBrassBlackeningCapability.md) | None<br/>| 1 | 
| [SudoknBritishRetailConsortiumAccreditation](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknBritishRetailConsortiumAccreditation.md) | None<br/>| 1 | 
| [SudoknCarbonGraphiteProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCarbonGraphiteProcessingCapability.md) | None<br/>| 13 | 
| [SudoknCerakoteCoatingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCerakoteCoatingCapability.md) | None<br/>| 1 | 
| [SudoknChemicalCleaningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknChemicalCleaningCapability.md) | None<br/>| 1 | 
| [SudoknCNCBendingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCNCBendingCapability.md) | None<br/>| 1 | 
| [SudoknCNCCuttingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCNCCuttingCapability.md) | None<br/>| 1 | 
| [SudoknCNCCylindricalGrindingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCNCCylindricalGrindingCapability.md) | None<br/>| 1 | 
| [SudoknCNCFormingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCNCFormingCapability.md) | None<br/>| 1 | 
| [SudoknCNCGrindingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCNCGrindingCapability.md) | None<br/>| 1 | 
| [SudoknCNCHorizontalTurningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCNCHorizontalTurningCapability.md) | None<br/>| 1 | 
| [SudoknCNCLatheCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCNCLatheCapability.md) | None<br/>| 1 | 
| [SudoknCNCmillingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCNCmillingCapability.md) | None<br/>| 1 | 
| [SudoknCNCPlasmaCuttingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCNCPlasmaCuttingCapability.md) | None<br/>| 1 | 
| [SudoknCNCPressBrakeCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCNCPressBrakeCapability.md) | None<br/>| 1 | 
| [SudoknCNCVerticalMillingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCNCVerticalMillingCapability.md) | None<br/>| 1 | 
| [SudoknCNCWireBendingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCNCWireBendingCapability.md) | None<br/>| 1 | 
| [SudoknCommunicationandElectronicPowerUtilitiesIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCommunicationandElectronicPowerUtilitiesIndustry.md) | None<br/>| 1 | 
| [SudoknCommunicationIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCommunicationIndustry.md) | None<br/>| 2 | 
| [SudoknComputersandElectronicProductsIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknComputersandElectronicProductsIndustry.md) | None<br/>| 1 | 
| [SudoknConsumerGoods](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknConsumerGoods.md) | None<br/>| 1 | 
| [SudoknCustomFoamCuttingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCustomFoamCuttingCapability.md) | None<br/>| 1 | 
| [SudoknCuttingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCuttingCapability.md) | None<br/>| 19 | 
| [SudoknCylindricalGrindingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknCylindricalGrindingCapability.md) | None<br/>| 1 | 
| [SudoknDeepFreezingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknDeepFreezingCapability.md) | None<br/>| 1 | 
| [SudoknDieMakingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknDieMakingCapability.md) | None<br/>| 6 | 
| [SudoknDifficultToMachineMaterialsProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknDifficultToMachineMaterialsProcessingCapability.md) | None<br/>| 28 | 
| [SudoknDigitalPrintingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknDigitalPrintingCapability.md) | None<br/>| 1 | 
| [SudoknEducationalInstitutionsIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknEducationalInstitutionsIndustry.md) | None<br/>| 1 | 
| [SudoknElectolessNickelPlatingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknElectolessNickelPlatingCapability.md) | None<br/>| 1 | 
| [SudoknElectricalDischargeMachiningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknElectricalDischargeMachiningCapability.md) | None<br/>| 197 | 
| [SudoknElectricVehiclesIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknElectricVehiclesIndustry.md) | None<br/>| 1 | 
| [SudoknElectrolessNickelPlatingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknElectrolessNickelPlatingCapability.md) | None<br/>| 214 | 
| [SudoknElectrolessPlatingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknElectrolessPlatingCapability.md) | None<br/>| 1 | 
| [SudoknElectronicAutomotiveInudstry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknElectronicAutomotiveInudstry.md) | None<br/>| 1 | 
| [SudoknElectroplatingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknElectroplatingCapability.md) | None<br/>| 3 | 
| [SudoknEndFormingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknEndFormingCapability.md) | None<br/>| 1 | 
| [SudoknExtremelyHardMaterialProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknExtremelyHardMaterialProcessingCapability.md) | None<br/>| 12 | 
| [SudoknExtrusionCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknExtrusionCapability.md) | None<br/>| 1 | 
| [SudoknFabricationCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknFabricationCapability.md) | None<br/>| 121 | 
| [SudoknFasteningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknFasteningCapability.md) | None<br/>| 1 | 
| [SudoknFDAGMPCompliant](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknFDAGMPCompliant.md) | None<br/>| 2 | 
| [SudoknFiberOpticLaserCuttingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknFiberOpticLaserCuttingCapability.md) | None<br/>| 1 | 
| [SudoknFillingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknFillingCapability.md) | None<br/>| 1 | 
| [SudoknFinishingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknFinishingCapability.md) | None<br/>| 1614 | 
| [SudoknFixturingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknFixturingCapability.md) | None<br/>| 1 | 
| [SudoknGeospatialLocation](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknGeospatialLocation.md) | None<br/>| 20728 | 
| [SudoknGoldProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknGoldProcessingCapability.md) | None<br/>| 1302 | 
| [SudoknGovermentIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknGovermentIndustry.md) | None<br/>| 1 | 
| [SudoknHealthcareServicesIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknHealthcareServicesIndustry.md) | None<br/>| 1 | 
| [SudoknHealthCareServicesIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknHealthCareServicesIndustry.md) | None<br/>| 1 | 
| [SudoknHighGradeAluminumProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknHighGradeAluminumProcessingCapability.md) | None<br/>| 5 | 
| [SudoknHotDipGalvanizingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknHotDipGalvanizingCapability.md) | None<br/>| 1 | 
| [SudoknInductionHeatingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknInductionHeatingCapability.md) | None<br/>| 1 | 
| [SudoknIndustrialMachineryandEquipmentIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknIndustrialMachineryandEquipmentIndustry.md) | None<br/>| 1 | 
| [SudoknIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknIndustry.md) | None<br/>| 1 | 
| [SudoknInstallationCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknInstallationCapability.md) | None<br/>| 2 | 
| [SudoknIS-TS16949](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknIS-TS16949.md) | None<br/>| 6 | 
| [SudoknISO13485](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknISO13485.md) | None<br/>| 1 | 
| [SudoknISO14001](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknISO14001.md) | None<br/>| 7 | 
| [SudoknISO9000](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknISO9000.md) | None<br/>| 31 | 
| [SudoknISO9001](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknISO9001.md) | None<br/>| 82 | 
| [SudoknISOCertificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknISOCertificate.md) | None<br/>| 67 | 
| [SudoknITARCompliant](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknITARCompliant.md) | None<br/>| 8 | 
| [SudoknKOSHERApproved](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknKOSHERApproved.md) | None<br/>| 1 | 
| [SudoknLaserProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknLaserProcessingCapability.md) | None<br/>| 1 | 
| [SudoknLaserWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknLaserWeldingCapability.md) | None<br/>| 1 | 
| [SudoknLatheWorkCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknLatheWorkCapability.md) | None<br/>| 1 | 
| [SudoknLiquidCoatingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknLiquidCoatingCapability.md) | None<br/>| 1 | 
| [SudoknLowAlloySteelProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknLowAlloySteelProcessingCapability.md) | None<br/>| 120 | 
| [SudoknMachineBuildingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMachineBuildingCapability.md) | None<br/>| 1 | 
| [SudoknMagnesiumProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMagnesiumProcessingCapability.md) | None<br/>| 419 | 
| [SudoknMechanicalAssemblyCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMechanicalAssemblyCapability.md) | None<br/>| 1 | 
| [SudoknMediaBlastingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMediaBlastingCapability.md) | None<br/>| 1 | 
| [SudoknMetalFabricationCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMetalFabricationCapability.md) | None<br/>| 6 | 
| [SudoknMetalProductionIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMetalProductionIndustry.md) | None<br/>| 1 | 
| [SudoknMetalSpinningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMetalSpinningCapability.md) | None<br/>| 1 | 
| [SudoknMetalsProductsIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMetalsProductsIndustry.md) | None<br/>| 1 | 
| [SudoknMetalStampingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMetalStampingCapability.md) | None<br/>| 2 | 
| [SudoknMetalworkingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMetalworkingCapability.md) | None<br/>| 1 | 
| [SudoknMIGWeldinCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMIGWeldinCapability.md) | None<br/>| 1 | 
| [SudoknMigWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknMigWeldingCapability.md) | None<br/>| 1 | 
| [SudoknNADCAPAC7004](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNADCAPAC7004.md) | None<br/>| 1 | 
| [SudoknNAICS332115](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332115.md) | None<br/>| 1 | 
| [SudoknNAICS332116](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332116.md) | None<br/>| 1 | 
| [SudoknNAICS332211](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332211.md) | None<br/>| 1 | 
| [SudoknNAICS332212](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332212.md) | None<br/>| 1 | 
| [SudoknNAICS332213](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332213.md) | None<br/>| 1 | 
| [SudoknNAICS332214](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332214.md) | None<br/>| 1 | 
| [SudoknNAICS332611](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332611.md) | None<br/>| 1 | 
| [SudoknNAICS332612](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332612.md) | None<br/>| 1 | 
| [SudoknNAICS332995](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332995.md) | None<br/>| 1 | 
| [SudoknNAICS332997](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332997.md) | None<br/>| 1 | 
| [SudoknNAICS332998](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNAICS332998.md) | None<br/>| 1 | 
| [SudoknNickelPlatingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNickelPlatingCapability.md) | None<br/>| 1 | 
| [SudoknNomexProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNomexProcessingCapability.md) | None<br/>| 58 | 
| [SudoknNylonProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknNylonProcessingCapability.md) | None<br/>| 1177 | 
| [SudoknOxy-FuelCuttingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknOxy-FuelCuttingCapability.md) | None<br/>| 27 | 
| [SudoknPackagingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPackagingCapability.md) | None<br/>| 3 | 
| [SudoknPaintingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPaintingCapability.md) | None<br/>| 3 | 
| [SudoknPaperandPaperboardProductsIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPaperandPaperboardProductsIndustry.md) | None<br/>| 1 | 
| [SudoknPemInsertionCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPemInsertionCapability.md) | None<br/>| 1 | 
| [SudoknPhosBronzeProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPhosBronzeProcessingCapability.md) | None<br/>| 12 | 
| [SudoknPipingFabricationCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPipingFabricationCapability.md) | None<br/>| 1 | 
| [SudoknPlasticsandRubberProductsIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPlasticsandRubberProductsIndustry.md) | None<br/>| 1 | 
| [SudoknPreciousMaterialProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPreciousMaterialProcessingCapability.md) | None<br/>| 6 | 
| [SudoknPressBrakingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPressBrakingCapability.md) | None<br/>| 1 | 
| [SudoknPressingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPressingCapability.md) | None<br/>| 6 | 
| [SudoknProductDesignCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknProductDesignCapability.md) | None<br/>| 1 | 
| [SudoknPrototypeManufacturingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPrototypeManufacturingCapability.md) | None<br/>| 1 | 
| [SudoknPrototypingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPrototypingCapability.md) | None<br/>| 1 | 
| [SudoknPulsedElectrochemicalMachiningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknPulsedElectrochemicalMachiningCapability.md) | None<br/>| 1 | 
| [SudoknQS9000](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknQS9000.md) | None<br/>| 1 | 
| [SudoknRAMEdmCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknRAMEdmCapability.md) | None<br/>| 1 | 
| [SudoknResistanceWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknResistanceWeldingCapability.md) | None<br/>| 1 | 
| [SudoknRetailTradeIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknRetailTradeIndustry.md) | None<br/>| 1 | 
| [SudoknRivettingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknRivettingCapability.md) | None<br/>| 1 | 
| [SudoknRoboticWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknRoboticWeldingCapability.md) | None<br/>| 2 | 
| [SudoknSanitaryWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSanitaryWeldingCapability.md) | None<br/>| 1 | 
| [SudoknScreenPrintingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknScreenPrintingCapability.md) | None<br/>| 1 | 
| [SudoknSewingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSewingCapability.md) | None<br/>| 1 | 
| [SudoknShearingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknShearingCapability.md) | None<br/>| 13 | 
| [SudoknSheetMetalFabricationCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSheetMetalFabricationCapability.md) | None<br/>| 5 | 
| [SudoknSheetMetalFormingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSheetMetalFormingCapability.md) | None<br/>| 2 | 
| [SudoknShellMoldCastingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknShellMoldCastingCapability.md) | None<br/>| 2 | 
| [SudoknSilkScreeningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSilkScreeningCapability.md) | None<br/>| 1 | 
| [SudoknSinkerEdmCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSinkerEdmCapability.md) | None<br/>| 1 | 
| [SudoknSmeltingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSmeltingCapability.md) | None<br/>| 1 | 
| [SudoknSpecialMaterialsProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSpecialMaterialsProcessingCapability.md) | None<br/>| 71 | 
| [SudoknSportsandLeisureIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSportsandLeisureIndustry.md) | None<br/>| 1 | 
| [SudoknSteelAlloyProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSteelAlloyProcessingCapability.md) | None<br/>| 365 | 
| [SudoknSteelManufacturingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSteelManufacturingCapability.md) | None<br/>| 1 | 
| [SudoknSurfaceGrindingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSurfaceGrindingCapability.md) | None<br/>| 2 | 
| [SudoknSwissTurningCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknSwissTurningCapability.md) | None<br/>| 1 | 
| [SudoknTantalumProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknTantalumProcessingCapability.md) | None<br/>| 234 | 
| [SudoknTextiles](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknTextiles.md) | None<br/>| 1 | 
| [SudoknTI9000Certificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknTI9000Certificate.md) | None<br/>| 1 | 
| [SudoknTinProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknTinProcessingCapability.md) | None<br/>| 417 | 
| [SudoknTubeFormingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknTubeFormingCapability.md) | None<br/>| 1 | 
| [SudoknTurretPunchingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknTurretPunchingCapability.md) | None<br/>| 1 | 
| [SudoknVacuumFormingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknVacuumFormingCapability.md) | None<br/>| 1 | 
| [SudoknWarehousingAndStorageIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknWarehousingAndStorageIndustry.md) | None<br/>| 1 | 
| [SudoknWaterandSewerUtilitiesIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknWaterandSewerUtilitiesIndustry.md) | None<br/>| 1 | 
| [SudoknWaterjetCuttimgCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknWaterjetCuttimgCapability.md) | None<br/>| 1 | 
| [SudoknWaterJetCuttingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknWaterJetCuttingCapability.md) | None<br/>| 2 | 
| [SudoknWeldingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknWeldingCapability.md) | None<br/>| 2700 | 
| [SudoknWireFormingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknWireFormingCapability.md) | None<br/>| 1 | 
| [SudoknWiringCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknWiringCapability.md) | None<br/>| 1 | 
| [SudoknWoodworkingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknWoodworkingCapability.md) | None<br/>| 1 | 
| [SudoknZincArcSprayCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknZincArcSprayCapability.md) | None<br/>| 1 | 
| [SudoknZincProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknZincProcessingCapability.md) | None<br/>| 1266 | 
| [SudoknZirconProcessingCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/classes/SudoknZirconProcessingCapability.md) | None<br/>| 240 | 





## Slots

| Slot | Description | Occurrences |
| --- | --- | --- |
| [https___spec.industrialontologies.org_ontology_core_meta_AnnotationVocabulary_replacedBy](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/https___spec.industrialontologies.org_ontology_core_meta_AnnotationVocabulary_replacedBy.md) | <br/>|  |
| [io_denotedBy](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/io_denotedBy.md) | <br/>|  |
| [iosc_hasTextValue](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/iosc_hasTextValue.md) | <br/>| 19102 |
| [obo_BFO_0000124](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/obo_BFO_0000124.md) | <br/>|  |
| [obo_BFO_0000171](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/obo_BFO_0000171.md) | <br/>|  |
| [obo_BFO_0000178](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/obo_BFO_0000178.md) | <br/>|  |
| [sudokn_attestsTo](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_attestsTo.md) | <br/>| 2 |
| [sudokn_CityOf](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_CityOf.md) | <br/>|  |
| [sudokn_hasAddressPart](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_hasAddressPart.md) | <br/>|  |
| [sudokn_hasCertificate](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_hasCertificate.md) | <br/>| 7430 |
| [sudokn_hasEmailAddress](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_hasEmailAddress.md) | <br/>| 1 |
| [sudokn_hasIntegerValue](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_hasIntegerValue.md) | <br/>| 18729 |
| [sudokn_hasLatitudeValue](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_hasLatitudeValue.md) | <br/>| 19082 |
| [sudokn_hasLongitudeValue](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_hasLongitudeValue.md) | <br/>| 19083 |
| [sudokn_hasManagementCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_hasManagementCapability.md) | <br/>| 1 |
| [sudokn_hasMaterialCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_hasMaterialCapability.md) | <br/>| 77383 |
| [sudokn_hasNAICSClassifier](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_hasNAICSClassifier.md) | <br/>| 1 |
| [sudokn_hasNAICSCodeValue](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_hasNAICSCodeValue.md) | <br/>| 64 |
| [sudokn_hasNAICSTextValue](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_hasNAICSTextValue.md) | <br/>| 65 |
| [sudokn_hasName](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_hasName.md) | <br/>| 1 |
| [sudokn_hasNumberOfEmployees](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_hasNumberOfEmployees.md) | <br/>| 6931 |
| [sudokn_hasOrganizationYearOfEstablishment](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_hasOrganizationYearOfEstablishment.md) | <br/>| 280 |
| [sudokn_hasOwnershipStatusClassifier](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_hasOwnershipStatusClassifier.md) | <br/>| 1120 |
| [sudokn_hasPostalAddress](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_hasPostalAddress.md) | <br/>| 20729 |
| [sudokn_hasPrimaryNAICSClassifier](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_hasPrimaryNAICSClassifier.md) | <br/>| 6624 |
| [sudokn_hasProcessCapability](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_hasProcessCapability.md) | <br/>| 53953 |
| [sudokn_hasSecondaryNAICSClassifier](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_hasSecondaryNAICSClassifier.md) | <br/>| 112 |
| [sudokn_hasSecondaryNIACSClassifier](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_hasSecondaryNIACSClassifier.md) | <br/>|  |
| [sudokn_hasSpatialCoordinates](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_hasSpatialCoordinates.md) | <br/>| 20728 |
| [sudokn_hasSpecialBusinessStatusClassifier](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_hasSpecialBusinessStatusClassifier.md) | <br/>|  |
| [sudokn_hasWebAddress](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_hasWebAddress.md) | <br/>| 1 |
| [sudokn_hasZIPCode](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_hasZIPCode.md) | has ZIP code<br/>|  |
| [sudokn_hasZIPcode](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_hasZIPcode.md) | <br/>| 20424 |
| [sudokn_locatedInCity](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_locatedInCity.md) | <br/>| 19022 |
| [sudokn_locatedInState](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_locatedInState.md) | <br/>| 3734 |
| [sudokn_manufactures](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_manufactures.md) | <br/>| 71660 |
| [sudokn_OrganizationLocatedIn](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_OrganizationLocatedIn.md) | <br/>|  |
| [sudokn_organizationLocatedIn](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_organizationLocatedIn.md) | <br/>| 20728 |
| [sudokn_stateOf](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_stateOf.md) | <br/>|  |
| [sudokn_suppliesToIndustry](https://github.com/frink-okn/graph-descriptions/blob/main/sudokn-kg/slots/sudokn_suppliesToIndustry.md) | <br/>| 26411 |









## IRI prefixes

* io: https://spec.industrialontologies.org/ontology/core/Core/
* iosc: https://spec.industrialontologies.org/ontology/supplychain/SupplyChain/
* linkml: https://w3id.org/linkml/
* obo: http://purl.obolibrary.org/obo/
* okn: https://purl.org/okn/
* okns: https://purl.org/okn/schema/
* owl: http://www.w3.org/2002/07/owl#
* rdf: http://www.w3.org/1999/02/22-rdf-syntax-ns#
* rdfs: http://www.w3.org/2000/01/rdf-schema#
* sudokn: http://asu.edu/semantics/SUDOKN/
* xsd: http://www.w3.org/2001/XMLSchema#
