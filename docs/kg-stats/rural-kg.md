# ruralkg

An ontology which serves the schema for the cross-domain knowledge graph (Rural-KG) to integrate health and justice data for rural resilience.



## Schema Diagram

```mermaid
erDiagram
RuralAdministrativeareaAdministrativeArea {

}
RuralAdministrativeareaCity {
    float rural_administrativearea_latitude  
    string rural_administrativearea_name  
    float rural_administrativearea_longitude  
    integer rural_administrativearea_ranking  
}
RuralAdministrativeareaCounty {
    string rural_administrativearea_fips  
    string rural_administrativearea_name  
}
RuralAdministrativeareaState {
    string rural_administrativearea_abbreviation  
    string rural_administrativearea_fips  
    string rural_administrativearea_name  
}
RuralJusticeAdministrativeSegment {

}
RuralJusticeArresteeSegment {

}
RuralJusticeDataElement08A-BiasMotivation {

}
RuralJusticeDataElement1-ORI {

}
RuralJusticeDataElement10-NumberofPremisesEntered {

}
RuralJusticeDataElement11-MethodofEntry {

}
RuralJusticeDataElement12-TypeCriminalActivityGangInformation {

}
RuralJusticeDataElement13-TypeWeaponForceInvolved {

}
RuralJusticeDataElement14-TypePropertyLossEtc. {

}
RuralJusticeDataElement15-PropertyDescription {

}
RuralJusticeDataElement16-ValueofProperty {

}
RuralJusticeDataElement17-DateRecovered {

}
RuralJusticeDataElement18-NumberofStolenMotorVehicles {

}
RuralJusticeDataElement19-NumberofRecoveredMotorVehicles {

}
RuralJusticeDataElement1A-FederalJudicialDistrict {

}
RuralJusticeDataElement2-IncidentNumber {

}
RuralJusticeDataElement20 {

}
RuralJusticeDataElement20-SuspectedDrugType {

}
RuralJusticeDataElement21-EstimatedDrugQuantity {

}
RuralJusticeDataElement22-EstimatedDrugQuantity {

}
RuralJusticeDataElement23-VictimSequenceNumber {

}
RuralJusticeDataElement24-VictimConnectedtoUCROffenseCode {

}
RuralJusticeDataElement25-TypeofVictim {

}
RuralJusticeDataElement25A-TypeofOfficerActivityCircumstance {

}
RuralJusticeDataElement25B-OfficerAssignmentType {

}
RuralJusticeDataElement25C-Officer-ORIOtherJurisdiction {

}
RuralJusticeDataElement26-AgeofVictim {

}
RuralJusticeDataElement27-SexofVictim {

}
RuralJusticeDataElement28-RaceofVictim {

}
RuralJusticeDataElement29-EthnicityofVictim {

}
RuralJusticeDataElement2A-CargoTheft {

}
RuralJusticeDataElement30-ResidentStatusofVictim {

}
RuralJusticeDataElement31-AggravatedAssaultHomicideCircumstances {

}
RuralJusticeDataElement32-AdditionalJustifiableHomicideCircumstances {

}
RuralJusticeDataElement33-TypeInjury {

}
RuralJusticeDataElement34-OffenderNumbertobeRelated {

}
RuralJusticeDataElement35-RelationshipofVictimtoOffender {

}
RuralJusticeDataElement36-OffenderSequenceNumber {

}
RuralJusticeDataElement37-AgeofOffender {

}
RuralJusticeDataElement38-SexofOffender {

}
RuralJusticeDataElement39-RaceofOffender {

}
RuralJusticeDataElement39A-EthnicityofOffender {

}
RuralJusticeDataElement4-ClearedExceptionally {

}
RuralJusticeDataElement40-ArresteeSequenceNumber {

}
RuralJusticeDataElement41-ArrestTransactionNumber {

}
RuralJusticeDataElement42-ArrestDate {

}
RuralJusticeDataElement43-TypeofArrest {

}
RuralJusticeDataElement44-MultipleArresteeSegmentsIndicator {

}
RuralJusticeDataElement45-UCRArrestOffenseCode {

}
RuralJusticeDataElement46-ArresteeWasArmedWith {

}
RuralJusticeDataElement47-AgeofArrestee {

}
RuralJusticeDataElement48-SexofArrestee {

}
RuralJusticeDataElement49-RaceofArrestee {

}
RuralJusticeDataElement5-ExceptionalClearanceDate {

}
RuralJusticeDataElement50-EthnicityofArrestee {

}
RuralJusticeDataElement51-ResidentStatusofArrestee {

}
RuralJusticeDataElement52-DispositionofArresteeUnder18 {

}
RuralJusticeDataElement52-DispositionofArresteeUnder19 {

}
RuralJusticeDataElement52-DispositionofArresteeUnder20 {

}
RuralJusticeDataElement6-UCROffenseCode {

}
RuralJusticeDataElement7-OffenseAttemptedCompleted {

}
RuralJusticeDataElement8-OffenderSuspectedofUsing {

}
RuralJusticeDataElement9-LocationType {

}
RuralJusticeGroupBArrestReportSegment {

}
RuralJusticeJustice {

}
RuralJusticeOffenderSegment {

}
RuralJusticeOffenseSegment {

}
RuralJusticePropertySegment {

}
RuralJusticeVictimSegment {

}
RuralJusticeZeroReportSegment {

}
RuralSettlementtypeCountyStatus {
    integer rural_settlementtype_population  
    integer rural_settlementtype_year  
}
RuralSettlementtypeRUCC {
    string rural_settlementtype_code  
    integer rural_settlementtype_year  
    string rural_settlementtype_description  
}
RuralSettlementtypeSettlementType {

}
RuralSubstanceabuseConceptAdultDepression {

}
RuralSubstanceabuseConceptAlcoholUse {

}
RuralSubstanceabuseConceptCOVID19Impact {

}
RuralSubstanceabuseConceptCannabisUse {

}
RuralSubstanceabuseConceptCensusBlock {

}
RuralSubstanceabuseConceptCensusSegment {

}
RuralSubstanceabuseConceptCocaineUse {

}
RuralSubstanceabuseConceptCountyClassification {

}
RuralSubstanceabuseConceptCriminalJusticeInvolvement {

}
RuralSubstanceabuseConceptDemographics {

}
RuralSubstanceabuseConceptDepression {

}
RuralSubstanceabuseConceptEducation {

}
RuralSubstanceabuseConceptEmergingSubstances {

}
RuralSubstanceabuseConceptEmployment {

}
RuralSubstanceabuseConceptGeographicIndicators {

}
RuralSubstanceabuseConceptHallucinogenUse {

}
RuralSubstanceabuseConceptHealthInsurance {

}
RuralSubstanceabuseConceptHeroinUse {

}
RuralSubstanceabuseConceptHouseholdComposition {

}
RuralSubstanceabuseConceptIncomeAndPoverty {

}
RuralSubstanceabuseConceptInhalantUse {

}
RuralSubstanceabuseConceptMentalHealth {

}
RuralSubstanceabuseConceptMentalHealthStatus {

}
RuralSubstanceabuseConceptMentalHealthTreatment {

}
RuralSubstanceabuseConceptOpioidUse {

}
RuralSubstanceabuseConceptPhysicalHealth {

}
RuralSubstanceabuseConceptPrescriptionDrugMisuse {

}
RuralSubstanceabuseConceptSocialDeterminants {

}
RuralSubstanceabuseConceptStimulantUse {

}
RuralSubstanceabuseConceptSubstanceUse {

}
RuralSubstanceabuseConceptSubstanceUseDisorders {

}
RuralSubstanceabuseConceptSubstanceUsePatterns {

}
RuralSubstanceabuseConceptSubstanceUseTreatment {

}
RuralSubstanceabuseConceptSuicideRisk {

}
RuralSubstanceabuseConceptSurveyMethodology {

}
RuralSubstanceabuseConceptTobaccoUse {

}
RuralSubstanceabuseConceptYouthDepression {

}
RuralSubstanceabuseConceptYouthExperiences {

}
RuralSubstanceabuseConceptYouthMentalHealth {

}
RuralSubstanceabuseSubstance {
    string rural_substanceabuse_code  
    string rural_substanceabuse_identifier  
    string rural_substanceabuse_description  
    string rural_substanceabuse_name  
    integer rural_substanceabuse_year  
    string rural_substanceabuse_fromDataset  
}
RuralSubstanceabuseSubstanceAbuse {

}
RuralSubstanceabuseSubstanceRelatedIncident {
    integer rural_substanceabuse_year  
    string rural_substanceabuse_name  
    string rural_substanceabuse_fromDataset  
}
RuralTreatmentMentalHealthService {
    string rural_treatment_description  
    integer rural_treatment_year  
    string rural_treatment_code  
    string rural_treatment_name  
}
RuralTreatmentMentalHealthServiceCategory {
    integer rural_treatment_year  
    string rural_treatment_code  
    string rural_treatment_name  
}
RuralTreatmentTreatment {

}
RuralTreatmentTreatmentProvider {
    string rural_treatment_alias  
    string rural_treatment_zipcode  
    uri rural_treatment_inCity  
    string rural_treatment_name  
    string rural_treatment_phone  
    string rural_treatment_address  
}
RuralVariableAnswer {

}
RuralVariableNIBRS {
    string rural_variable_description  
    integer rural_variable_year  
    string rural_variable_content  
    string rural_variable_fromDataset  
    string rural_variable_generatedDescription  
    string rural_variable_code  
}
RuralVariableNIBRSAnswer {
    string rural_variable_answerContent  
    string rural_variable_answerCode  
}
RuralVariableNSDUH {
    string rural_variable_description  
    integer rural_variable_year  
    string rural_variable_content  
    string rural_variable_fromDataset  
    string rural_variable_generatedDescription  
    string rural_variable_code  
}
RuralVariableNSDUHAnswer {
    string rural_variable_answerContent  
    string rural_variable_answerCode  
}
RuralVariableVariable {

}

RuralAdministrativeareaCity ||--|o RuralAdministrativeareaCounty : "rural_administrativearea_primaryCounty"
RuralAdministrativeareaState ||--|o RuralAdministrativeareaCounty : "rural_administrativearea_containsPlace"
RuralSettlementtypeCountyStatus ||--|o RuralSettlementtypeRUCC : "rural_settlementtype_hasRUCC"
RuralSettlementtypeCountyStatus ||--|o RuralAdministrativeareaCounty : "rural_settlementtype_censusCounty"
RuralTreatmentMentalHealthServiceCategory ||--|o RuralTreatmentMentalHealthService : "rural_treatment_containsService"
RuralTreatmentTreatmentProvider ||--|o RuralTreatmentMentalHealthService : "rural_treatment_providesService"
RuralTreatmentTreatmentProvider ||--|o RuralAdministrativeareaCity : "rural_treatment_inCity"
RuralVariableNIBRS ||--|o RuralVariableNIBRSAnswer : "rural_variable_hasAnswer"
RuralVariableNIBRS ||--|o RuralVariableNSDUHAnswer : "rural_variable_hasAnswer"
RuralVariableNSDUH ||--|o RuralVariableNIBRSAnswer : "rural_variable_hasAnswer"
RuralVariableNSDUH ||--|o RuralVariableNSDUHAnswer : "rural_variable_hasAnswer"

```



## Imports


* linkml:types
* okns:extended_types



## Classes

| Class | Description | Occurrences |
| --- | --- | --- |
| [RuralAdministrativeareaAdministrativeArea](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralAdministrativeareaAdministrativeArea.md) | Covers all administrative regions, including State, City, County, and MSA (undergoing).<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralAdministrativeareaCity](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralAdministrativeareaCity.md) | City entities within a county or state.<br/>| 31120 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralAdministrativeareaCounty](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralAdministrativeareaCounty.md) | Defines counties within a state.<br/>| 3253 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralAdministrativeareaState](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralAdministrativeareaState.md) | Represents individual states within U.S.<br/>| 56 | 
| [RuralJusticeJustice](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeJustice.md) | Justice data, including crime data, extracted from National Incident-Based Reporting System (NIBRS).<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeAdministrativeSegment](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeAdministrativeSegment.md) | NIBRS Administrative Segment<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeDataElement1-ORI](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeDataElement1-ORI.md) | NIBRS data element: Data Element 1 - ORI<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeDataElement1A-FederalJudicialDistrict](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeDataElement1A-FederalJudicialDistrict.md) | NIBRS data element: Data Element 1A - Federal Judicial District<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeDataElement2-IncidentNumber](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeDataElement2-IncidentNumber.md) | NIBRS data element: Data Element 2 - Incident Number<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeDataElement2A-CargoTheft](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeDataElement2A-CargoTheft.md) | NIBRS data element: Data Element 2A - Cargo Theft<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeDataElement4-ClearedExceptionally](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeDataElement4-ClearedExceptionally.md) | NIBRS data element: Data Element 4 - Cleared Exceptionally<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeDataElement5-ExceptionalClearanceDate](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeDataElement5-ExceptionalClearanceDate.md) | NIBRS data element: Data Element 5 - Exceptional Clearance Date<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeArresteeSegment](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeArresteeSegment.md) | NIBRS Arrestee Segment<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeDataElement40-ArresteeSequenceNumber](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeDataElement40-ArresteeSequenceNumber.md) | NIBRS data element: Data Element 40 - Arrestee Sequence Number<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeDataElement41-ArrestTransactionNumber](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeDataElement41-ArrestTransactionNumber.md) | NIBRS data element: Data Element 41 - Arrest Transaction Number<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeDataElement42-ArrestDate](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeDataElement42-ArrestDate.md) | NIBRS data element: Data Element 42 - Arrest Date<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeDataElement43-TypeofArrest](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeDataElement43-TypeofArrest.md) | NIBRS data element: Data Element 43 - Type of Arrest<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeDataElement44-MultipleArresteeSegmentsIndicator](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeDataElement44-MultipleArresteeSegmentsIndicator.md) | NIBRS data element: Data Element 44 - Multiple Arrestee Segments Indicator<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeDataElement45-UCRArrestOffenseCode](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeDataElement45-UCRArrestOffenseCode.md) | NIBRS data element: Data Element 45 - UCR Arrest Offense Code<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeDataElement46-ArresteeWasArmedWith](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeDataElement46-ArresteeWasArmedWith.md) | NIBRS data element: Data Element 46 - Arrestee Was Armed With<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeDataElement47-AgeofArrestee](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeDataElement47-AgeofArrestee.md) | NIBRS data element: Data Element 47 - Age of Arrestee<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeDataElement48-SexofArrestee](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeDataElement48-SexofArrestee.md) | NIBRS data element: Data Element 48 - Sex of Arrestee<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeDataElement49-RaceofArrestee](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeDataElement49-RaceofArrestee.md) | NIBRS data element: Data Element 49 - Race of Arrestee<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeDataElement50-EthnicityofArrestee](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeDataElement50-EthnicityofArrestee.md) | NIBRS data element: Data Element 50 - Ethnicity of Arrestee<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeDataElement51-ResidentStatusofArrestee](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeDataElement51-ResidentStatusofArrestee.md) | NIBRS data element: Data Element 51 - Resident Status of Arrestee<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeDataElement52-DispositionofArresteeUnder18](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeDataElement52-DispositionofArresteeUnder18.md) | NIBRS data element: Data Element 52 - Disposition of Arrestee Under 18<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeDataElement52-DispositionofArresteeUnder19](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeDataElement52-DispositionofArresteeUnder19.md) | NIBRS data element: Data Element 52 - Disposition of Arrestee Under 19<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeDataElement52-DispositionofArresteeUnder20](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeDataElement52-DispositionofArresteeUnder20.md) | NIBRS data element: Data Element 52 - Disposition of Arrestee Under 20<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeGroupBArrestReportSegment](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeGroupBArrestReportSegment.md) | NIBRS Group B Arrest Report Segment<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeOffenderSegment](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeOffenderSegment.md) | NIBRS Offender Segment<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeDataElement36-OffenderSequenceNumber](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeDataElement36-OffenderSequenceNumber.md) | NIBRS data element: Data Element 36 - Offender Sequence Number<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeDataElement37-AgeofOffender](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeDataElement37-AgeofOffender.md) | NIBRS data element: Data Element 37 - Age of Offender<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeDataElement38-SexofOffender](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeDataElement38-SexofOffender.md) | NIBRS data element: Data Element 38 - Sex of Offender<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeDataElement39-RaceofOffender](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeDataElement39-RaceofOffender.md) | NIBRS data element: Data Element 39 - Race of Offender<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeDataElement39A-EthnicityofOffender](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeDataElement39A-EthnicityofOffender.md) | NIBRS data element: Data Element 39A - Ethnicity of Offender<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeOffenseSegment](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeOffenseSegment.md) | NIBRS Offense Segment<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeDataElement08A-BiasMotivation](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeDataElement08A-BiasMotivation.md) | NIBRS data element: Data Element 08A - Bias Motivation<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeDataElement10-NumberofPremisesEntered](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeDataElement10-NumberofPremisesEntered.md) | NIBRS data element: Data Element 10 - Number of Premises Entered<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeDataElement11-MethodofEntry](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeDataElement11-MethodofEntry.md) | NIBRS data element: Data Element 11 - Method of Entry<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeDataElement12-TypeCriminalActivityGangInformation](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeDataElement12-TypeCriminalActivityGangInformation.md) | NIBRS data element: Data Element 12 - Type Criminal Activity/Gang Information<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeDataElement13-TypeWeaponForceInvolved](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeDataElement13-TypeWeaponForceInvolved.md) | NIBRS data element: Data Element 13 - Type Weapon/Force Involved<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeDataElement6-UCROffenseCode](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeDataElement6-UCROffenseCode.md) | NIBRS data element: Data Element 6 - UCR Offense Code<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeDataElement7-OffenseAttemptedCompleted](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeDataElement7-OffenseAttemptedCompleted.md) | NIBRS data element: Data Element 7 - Offense Attempted/Completed<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeDataElement8-OffenderSuspectedofUsing](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeDataElement8-OffenderSuspectedofUsing.md) | NIBRS data element: Data Element 8 - Offender Suspected of Using<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeDataElement9-LocationType](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeDataElement9-LocationType.md) | NIBRS data element: Data Element 9 - Location Type<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticePropertySegment](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticePropertySegment.md) | NIBRS Property Segment<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeDataElement14-TypePropertyLossEtc.](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeDataElement14-TypePropertyLossEtc..md) | NIBRS data element: Data Element 14 - Type Property Loss/Etc.<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeDataElement15-PropertyDescription](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeDataElement15-PropertyDescription.md) | NIBRS data element: Data Element 15 - Property Description<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeDataElement16-ValueofProperty](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeDataElement16-ValueofProperty.md) | NIBRS data element: Data Element 16 - Value of Property<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeDataElement17-DateRecovered](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeDataElement17-DateRecovered.md) | NIBRS data element: Data Element 17 - Date Recovered<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeDataElement18-NumberofStolenMotorVehicles](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeDataElement18-NumberofStolenMotorVehicles.md) | NIBRS data element: Data Element 18 - Number of Stolen Motor Vehicles<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeDataElement19-NumberofRecoveredMotorVehicles](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeDataElement19-NumberofRecoveredMotorVehicles.md) | NIBRS data element: Data Element 19 - Number of Recovered Motor Vehicles<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeDataElement20](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeDataElement20.md) | NIBRS data element: Data Element 20<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeDataElement20-SuspectedDrugType](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeDataElement20-SuspectedDrugType.md) | NIBRS data element: Data Element 20 - Suspected Drug Type<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeDataElement21-EstimatedDrugQuantity](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeDataElement21-EstimatedDrugQuantity.md) | NIBRS data element: Data Element 21 - Estimated Drug Quantity<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeDataElement22-EstimatedDrugQuantity](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeDataElement22-EstimatedDrugQuantity.md) | NIBRS data element: Data Element 22 - Estimated Drug Quantity<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeVictimSegment](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeVictimSegment.md) | NIBRS Victim Segment<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeDataElement23-VictimSequenceNumber](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeDataElement23-VictimSequenceNumber.md) | NIBRS data element: Data Element 23 - Victim Sequence Number<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeDataElement24-VictimConnectedtoUCROffenseCode](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeDataElement24-VictimConnectedtoUCROffenseCode.md) | NIBRS data element: Data Element 24 - Victim Connected to UCR Offense Code<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeDataElement25-TypeofVictim](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeDataElement25-TypeofVictim.md) | NIBRS data element: Data Element 25 - Type of Victim<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeDataElement25A-TypeofOfficerActivityCircumstance](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeDataElement25A-TypeofOfficerActivityCircumstance.md) | NIBRS data element: Data Element 25A - Type of Officer Activity/Circumstance<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeDataElement25B-OfficerAssignmentType](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeDataElement25B-OfficerAssignmentType.md) | NIBRS data element: Data Element 25B - Officer Assignment Type<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeDataElement25C-Officer-ORIOtherJurisdiction](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeDataElement25C-Officer-ORIOtherJurisdiction.md) | NIBRS data element: Data Element 25C - Officer-ORI Other Jurisdiction<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeDataElement26-AgeofVictim](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeDataElement26-AgeofVictim.md) | NIBRS data element: Data Element 26 - Age of Victim<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeDataElement27-SexofVictim](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeDataElement27-SexofVictim.md) | NIBRS data element: Data Element 27 - Sex of Victim<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeDataElement28-RaceofVictim](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeDataElement28-RaceofVictim.md) | NIBRS data element: Data Element 28 - Race of Victim<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeDataElement29-EthnicityofVictim](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeDataElement29-EthnicityofVictim.md) | NIBRS data element: Data Element 29 - Ethnicity of Victim<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeDataElement30-ResidentStatusofVictim](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeDataElement30-ResidentStatusofVictim.md) | NIBRS data element: Data Element 30 - Resident Status of Victim<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeDataElement31-AggravatedAssaultHomicideCircumstances](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeDataElement31-AggravatedAssaultHomicideCircumstances.md) | NIBRS data element: Data Element 31 - Aggravated Assault/Homicide Circumstances<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeDataElement32-AdditionalJustifiableHomicideCircumstances](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeDataElement32-AdditionalJustifiableHomicideCircumstances.md) | NIBRS data element: Data Element 32 - Additional Justifiable Homicide Circumstances<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeDataElement33-TypeInjury](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeDataElement33-TypeInjury.md) | NIBRS data element: Data Element 33 - Type Injury<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeDataElement34-OffenderNumbertobeRelated](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeDataElement34-OffenderNumbertobeRelated.md) | NIBRS data element: Data Element 34 - Offender Number to be Related<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeDataElement35-RelationshipofVictimtoOffender](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeDataElement35-RelationshipofVictimtoOffender.md) | NIBRS data element: Data Element 35 - Relationship of Victim to Offender<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralJusticeZeroReportSegment](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralJusticeZeroReportSegment.md) | NIBRS Zero Report Segment<br/>|  | 
| [RuralSettlementtypeSettlementType](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralSettlementtypeSettlementType.md) | Rural-Urban Continuum Code (RUCC) is incorporated. Categorize county-level areas into Metro or Nonmetro. It is an indicator for determining the rural-urban continuum code (RUCC) classification<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralSettlementtypeCountyStatus](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralSettlementtypeCountyStatus.md) | Status of a county in terms of rural or urban classification.<br/>| 3234 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralSettlementtypeRUCC](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralSettlementtypeRUCC.md) | Rural-Urban Continuum Code classification.<br/>| 10 | 
| [RuralSubstanceabuseSubstanceAbuse](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralSubstanceabuseSubstanceAbuse.md) | Categories of substance type and related incident types, extracted from National Survey on Drug Use and Health (NSDUH).<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralSubstanceabuseConceptGeographicIndicators](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralSubstanceabuseConceptGeographicIndicators.md) | Geographic units and location identifiers used in survey sampling and analysis<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralSubstanceabuseConceptCensusBlock](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralSubstanceabuseConceptCensusBlock.md) | Census block identifiers and American Indian Area indicators<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralSubstanceabuseConceptCensusSegment](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralSubstanceabuseConceptCensusSegment.md) | Census segment identifiers with majority American Indian Area classification<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralSubstanceabuseConceptCountyClassification](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralSubstanceabuseConceptCountyClassification.md) | County-level geographic classifications including urbanization and population density<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralSubstanceabuseConceptMentalHealth](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralSubstanceabuseConceptMentalHealth.md) | Mental health conditions, symptoms, and treatment across adult and youth populations<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralSubstanceabuseConceptDepression](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralSubstanceabuseConceptDepression.md) | Major depressive episode and depression symptoms across adult and youth populations<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralSubstanceabuseConceptAdultDepression](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralSubstanceabuseConceptAdultDepression.md) | Adult-specific depression measures including symptoms, severity, and functional impairment<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralSubstanceabuseConceptYouthDepression](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralSubstanceabuseConceptYouthDepression.md) | Adolescent depression measures adapted for youth populations<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralSubstanceabuseConceptMentalHealthStatus](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralSubstanceabuseConceptMentalHealthStatus.md) | Overall mental health status, psychological distress, and functional impairment<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralSubstanceabuseConceptMentalHealthTreatment](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralSubstanceabuseConceptMentalHealthTreatment.md) | Mental health service utilization, treatment types, and unmet need<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralSubstanceabuseConceptSuicideRisk](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralSubstanceabuseConceptSuicideRisk.md) | Suicidal ideation, plans, and attempts across age groups<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralSubstanceabuseConceptYouthMentalHealth](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralSubstanceabuseConceptYouthMentalHealth.md) | Youth-specific mental health measures including school-based services<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralSubstanceabuseConceptSocialDeterminants](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralSubstanceabuseConceptSocialDeterminants.md) | Social, economic, and environmental factors that influence health outcomes<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralSubstanceabuseConceptCOVID19Impact](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralSubstanceabuseConceptCOVID19Impact.md) | COVID-19 pandemic effects on substance use, mental health, and service access<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralSubstanceabuseConceptCriminalJusticeInvolvement](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralSubstanceabuseConceptCriminalJusticeInvolvement.md) | Arrests, bookings, probation, parole, and other criminal justice system contacts<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralSubstanceabuseConceptDemographics](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralSubstanceabuseConceptDemographics.md) | Core demographic characteristics including age, gender, race, ethnicity, and marital status<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralSubstanceabuseConceptEducation](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralSubstanceabuseConceptEducation.md) | Educational attainment, enrollment status, and academic performance<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralSubstanceabuseConceptEmployment](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralSubstanceabuseConceptEmployment.md) | Employment status, occupation, work patterns, and workplace characteristics<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralSubstanceabuseConceptHealthInsurance](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralSubstanceabuseConceptHealthInsurance.md) | Health insurance coverage, types, and gaps in coverage<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralSubstanceabuseConceptHouseholdComposition](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralSubstanceabuseConceptHouseholdComposition.md) | Family structure, household size, and living arrangements<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralSubstanceabuseConceptIncomeAndPoverty](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralSubstanceabuseConceptIncomeAndPoverty.md) | Household income, family income, poverty status, and economic hardship<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralSubstanceabuseConceptPhysicalHealth](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralSubstanceabuseConceptPhysicalHealth.md) | General health status, chronic conditions, and health service utilization<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralSubstanceabuseConceptYouthExperiences](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralSubstanceabuseConceptYouthExperiences.md) | Youth-specific factors including school engagement, activities, and peer influences<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralSubstanceabuseConceptSubstanceUse](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralSubstanceabuseConceptSubstanceUse.md) | All substance use related measures including alcohol, tobacco, illicit drugs, and prescription drug misuse<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralSubstanceabuseConceptAlcoholUse](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralSubstanceabuseConceptAlcoholUse.md) | Comprehensive alcohol use measures including consumption patterns, disorders, and age of initiation<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralSubstanceabuseConceptCannabisUse](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralSubstanceabuseConceptCannabisUse.md) | Marijuana and cannabis product use including blunts, with measures of frequency and disorders<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralSubstanceabuseConceptCocaineUse](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralSubstanceabuseConceptCocaineUse.md) | Cocaine and crack cocaine use patterns, disorders, and treatment<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralSubstanceabuseConceptEmergingSubstances](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralSubstanceabuseConceptEmergingSubstances.md) | Emerging and novel substances including illegally made fentanyl, kratom, and synthetic drugs<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralSubstanceabuseConceptHallucinogenUse](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralSubstanceabuseConceptHallucinogenUse.md) | Use of hallucinogenic substances including LSD, PCP, peyote, and other psychedelics<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralSubstanceabuseConceptHeroinUse](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralSubstanceabuseConceptHeroinUse.md) | Heroin use patterns, injection drug use, and associated disorders<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralSubstanceabuseConceptInhalantUse](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralSubstanceabuseConceptInhalantUse.md) | Use of inhalants and volatile substances for intoxication purposes<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralSubstanceabuseConceptOpioidUse](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralSubstanceabuseConceptOpioidUse.md) | Combined measures for heroin and prescription opioid misuse, including disorders and overdose risk<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralSubstanceabuseConceptPrescriptionDrugMisuse](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralSubstanceabuseConceptPrescriptionDrugMisuse.md) | Non-medical use of prescription medications including pain relievers, tranquilizers, stimulants, and sedatives<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralSubstanceabuseConceptStimulantUse](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralSubstanceabuseConceptStimulantUse.md) | Use of stimulants including methamphetamine and prescription stimulants for non-medical purposes<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralSubstanceabuseConceptSubstanceUseDisorders](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralSubstanceabuseConceptSubstanceUseDisorders.md) | DSM-based substance use disorder diagnoses across all substance categories<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralSubstanceabuseConceptSubstanceUsePatterns](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralSubstanceabuseConceptSubstanceUsePatterns.md) | Cross-substance patterns including polysubstance use, age of first use, and recency of use<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralSubstanceabuseConceptSubstanceUseTreatment](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralSubstanceabuseConceptSubstanceUseTreatment.md) | Treatment receipt, need, and barriers for substance use disorders<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralSubstanceabuseConceptTobaccoUse](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralSubstanceabuseConceptTobaccoUse.md) | All tobacco product use including cigarettes, smokeless tobacco, cigars, and pipe tobacco<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralSubstanceabuseConceptSurveyMethodology](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralSubstanceabuseConceptSurveyMethodology.md) | Survey administration, weighting, and methodological variables<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralSubstanceabuseSubstance](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralSubstanceabuseSubstance.md) | Types of substances that can be abused.<br/>| 23 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralSubstanceabuseSubstanceRelatedIncident](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralSubstanceabuseSubstanceRelatedIncident.md) | Types of incidents related to substance abuse.<br/>| 17 | 
| [RuralTreatmentTreatment](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralTreatmentTreatment.md) | Mental health services and treatment providers, sourcing from National Directory Of Mental Health Treatment Facilities.<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralTreatmentMentalHealthService](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralTreatmentMentalHealthService.md) | Specific mental health services offered.<br/>| 176 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralTreatmentMentalHealthServiceCategory](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralTreatmentMentalHealthServiceCategory.md) | Categories of mental health services.<br/>| 21 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralTreatmentTreatmentProvider](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralTreatmentTreatmentProvider.md) | Entities that provide treatment services.<br/>| 9037 | 
| [RuralVariableVariable](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralVariableVariable.md) | Survey variables and their associated answer options from NSDUH and NIBRS datasets.<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralVariableAnswer](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralVariableAnswer.md) | Answer options for survey variables.<br/>|  | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralVariableNIBRSAnswer](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralVariableNIBRSAnswer.md) | Answer options for NIBRS variables.<br/>| 2258 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralVariableNSDUHAnswer](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralVariableNSDUHAnswer.md) | Answer options for NSDUH variables.<br/>| 14923 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralVariableNIBRS](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralVariableNIBRS.md) | Variables from the National Incident-Based Reporting System dataset.<br/>| 469 | 
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RuralVariableNSDUH](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/classes/RuralVariableNSDUH.md) | Variables from the National Survey on Drug Use and Health dataset.<br/>| 2464 | 





## Slots

| Slot | Description | Occurrences |
| --- | --- | --- |
| [rural_administrativearea_abbreviation](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/slots/rural_administrativearea_abbreviation.md) | <br/>| 56 |
| [rural_administrativearea_containsPlace](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/slots/rural_administrativearea_containsPlace.md) | <br/>| 3253 |
| [rural_administrativearea_fips](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/slots/rural_administrativearea_fips.md) | <br/>| 3309 |
| [rural_administrativearea_latitude](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/slots/rural_administrativearea_latitude.md) | <br/>| 31120 |
| [rural_administrativearea_longitude](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/slots/rural_administrativearea_longitude.md) | <br/>| 31120 |
| [rural_administrativearea_name](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/slots/rural_administrativearea_name.md) | <br/>| 34429 |
| [rural_administrativearea_primaryCounty](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/slots/rural_administrativearea_primaryCounty.md) | <br/>| 31120 |
| [rural_administrativearea_ranking](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/slots/rural_administrativearea_ranking.md) | <br/>| 31120 |
| [rural_settlementtype_censusCounty](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/slots/rural_settlementtype_censusCounty.md) | <br/>| 3234 |
| [rural_settlementtype_code](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/slots/rural_settlementtype_code.md) | <br/>| 10 |
| [rural_settlementtype_description](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/slots/rural_settlementtype_description.md) | <br/>| 10 |
| [rural_settlementtype_hasRUCC](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/slots/rural_settlementtype_hasRUCC.md) | <br/>| 3234 |
| [rural_settlementtype_population](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/slots/rural_settlementtype_population.md) | <br/>| 3234 |
| [rural_settlementtype_year](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/slots/rural_settlementtype_year.md) | <br/>| 3244 |
| [rural_substanceabuse_code](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/slots/rural_substanceabuse_code.md) | <br/>| 23 |
| [rural_substanceabuse_description](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/slots/rural_substanceabuse_description.md) | <br/>| 23 |
| [rural_substanceabuse_fromDataset](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/slots/rural_substanceabuse_fromDataset.md) | <br/>| 40 |
| [rural_substanceabuse_identifier](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/slots/rural_substanceabuse_identifier.md) | <br/>| 23 |
| [rural_substanceabuse_name](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/slots/rural_substanceabuse_name.md) | <br/>| 40 |
| [rural_substanceabuse_year](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/slots/rural_substanceabuse_year.md) | <br/>| 40 |
| [rural_treatment_address](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/slots/rural_treatment_address.md) | <br/>| 9037 |
| [rural_treatment_alias](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/slots/rural_treatment_alias.md) | <br/>| 9037 |
| [rural_treatment_code](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/slots/rural_treatment_code.md) | <br/>| 197 |
| [rural_treatment_containsService](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/slots/rural_treatment_containsService.md) | <br/>| 176 |
| [rural_treatment_description](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/slots/rural_treatment_description.md) | <br/>| 176 |
| [rural_treatment_inCity](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/slots/rural_treatment_inCity.md) | <br/>| 9037 |
| [rural_treatment_name](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/slots/rural_treatment_name.md) | <br/>| 9234 |
| [rural_treatment_phone](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/slots/rural_treatment_phone.md) | <br/>| 9037 |
| [rural_treatment_providesService](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/slots/rural_treatment_providesService.md) | <br/>| 442841 |
| [rural_treatment_year](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/slots/rural_treatment_year.md) | <br/>| 197 |
| [rural_treatment_zipcode](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/slots/rural_treatment_zipcode.md) | <br/>| 9037 |
| [rural_variable_answerCode](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/slots/rural_variable_answerCode.md) | <br/>| 17181 |
| [rural_variable_answerContent](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/slots/rural_variable_answerContent.md) | <br/>| 17181 |
| [rural_variable_code](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/slots/rural_variable_code.md) | <br/>| 2933 |
| [rural_variable_content](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/slots/rural_variable_content.md) | <br/>| 2934 |
| [rural_variable_description](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/slots/rural_variable_description.md) | <br/>| 2933 |
| [rural_variable_fromDataset](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/slots/rural_variable_fromDataset.md) | <br/>| 2933 |
| [rural_variable_generatedDescription](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/slots/rural_variable_generatedDescription.md) | <br/>| 2934 |
| [rural_variable_hasAnswer](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/slots/rural_variable_hasAnswer.md) | <br/>| 17181 |
| [rural_variable_year](https://github.com/frink-okn/graph-descriptions/blob/main/rural-kg/slots/rural_variable_year.md) | <br/>| 2933 |









## IRI prefixes

* linkml: https://w3id.org/linkml/
* okn: https://purl.org/okn/
* okns: https://purl.org/okn/schema/
* owl: http://www.w3.org/2002/07/owl#
* rdfs: http://www.w3.org/2000/01/rdf-schema#
* rural: http://sail.ua.edu/ruralkg/
