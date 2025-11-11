# climatemodelskg





## Schema Diagram

```mermaid
erDiagram
HttpsClimatepub4kg.github.ioOntology#Activity {
    string https___climatepub4kg.github.io_ontology#names  
    string https___climatepub4kg.github.io_ontology#uuid  
    string https___climatepub4kg.github.io_ontology#name  
}
HttpsClimatepub4kg.github.ioOntology#City {
    string https___climatepub4kg.github.io_ontology#country_code  
    string https___climatepub4kg.github.io_ontology#name  
    string https___climatepub4kg.github.io_ontology#population  
    string https___climatepub4kg.github.io_ontology#cc2  
    string https___climatepub4kg.github.io_ontology#timezone  
    string https___climatepub4kg.github.io_ontology#admin4_code  
    string https___climatepub4kg.github.io_ontology#asciiname  
    string https___climatepub4kg.github.io_ontology#admin2_code  
    string https___climatepub4kg.github.io_ontology#admin3_code  
    string https___climatepub4kg.github.io_ontology#uuid  
    string https___climatepub4kg.github.io_ontology#geonameid  
    string https___climatepub4kg.github.io_ontology#longitude  
    string https___climatepub4kg.github.io_ontology#alternatenames  
    string https___climatepub4kg.github.io_ontology#modification_date  
    string https___climatepub4kg.github.io_ontology#dem  
    string https___climatepub4kg.github.io_ontology#latitude  
    string https___climatepub4kg.github.io_ontology#feature_class  
    string https___climatepub4kg.github.io_ontology#admin1_code  
    string https___climatepub4kg.github.io_ontology#elevation  
    string https___climatepub4kg.github.io_ontology#feature_code  
}
HttpsClimatepub4kg.github.ioOntology#Continent {
    string https___climatepub4kg.github.io_ontology#name  
    string https___climatepub4kg.github.io_ontology#uuid  
    string https___climatepub4kg.github.io_ontology#iso  
    string https___climatepub4kg.github.io_ontology#geonameid  
}
HttpsClimatepub4kg.github.ioOntology#Country {
    string https___climatepub4kg.github.io_ontology#neighbours  
    string https___climatepub4kg.github.io_ontology#tld  
    string https___climatepub4kg.github.io_ontology#name  
    string https___climatepub4kg.github.io_ontology#capital  
    string https___climatepub4kg.github.io_ontology#population  
    string https___climatepub4kg.github.io_ontology#currencycode  
    string https___climatepub4kg.github.io_ontology#iso3  
    string https___climatepub4kg.github.io_ontology#continent  
    string https___climatepub4kg.github.io_ontology#fips  
    string https___climatepub4kg.github.io_ontology#uuid  
    string https___climatepub4kg.github.io_ontology#currencyname  
    string https___climatepub4kg.github.io_ontology#geonameid  
    string https___climatepub4kg.github.io_ontology#isonumeric  
    string https___climatepub4kg.github.io_ontology#phone  
    string https___climatepub4kg.github.io_ontology#area_sqkm  
    string https___climatepub4kg.github.io_ontology#country  
    string https___climatepub4kg.github.io_ontology#west  
    string https___climatepub4kg.github.io_ontology#iso  
    string https___climatepub4kg.github.io_ontology#equivalent_fips_code  
    string https___climatepub4kg.github.io_ontology#postal_code_format  
    string https___climatepub4kg.github.io_ontology#postal_code_regex  
    string https___climatepub4kg.github.io_ontology#languages  
    string https___climatepub4kg.github.io_ontology#north  
    string https___climatepub4kg.github.io_ontology#east  
    string https___climatepub4kg.github.io_ontology#south  
}
HttpsClimatepub4kg.github.ioOntology#CountrySubdivision {
    string https___climatepub4kg.github.io_ontology#asciiname  
    string https___climatepub4kg.github.io_ontology#west  
    string https___climatepub4kg.github.io_ontology#uuid  
    string https___climatepub4kg.github.io_ontology#code  
    string https___climatepub4kg.github.io_ontology#name  
    string https___climatepub4kg.github.io_ontology#geonameid  
    string https___climatepub4kg.github.io_ontology#north  
    string https___climatepub4kg.github.io_ontology#east  
    string https___climatepub4kg.github.io_ontology#south  
}
HttpsClimatepub4kg.github.ioOntology#Domain {
    string https___climatepub4kg.github.io_ontology#uuid  
    string https___climatepub4kg.github.io_ontology#name  
    string https___climatepub4kg.github.io_ontology#names  
}
HttpsClimatepub4kg.github.ioOntology#Ensemble {
    string https___climatepub4kg.github.io_ontology#uuid  
    string https___climatepub4kg.github.io_ontology#name  
    string https___climatepub4kg.github.io_ontology#names  
}
HttpsClimatepub4kg.github.ioOntology#Experiment {
    string https___climatepub4kg.github.io_ontology#names  
    string https___climatepub4kg.github.io_ontology#uuid  
    string https___climatepub4kg.github.io_ontology#name  
    string https___climatepub4kg.github.io_ontology#experiment_title  
}
HttpsClimatepub4kg.github.ioOntology#ExperimentFamily {
    string https___climatepub4kg.github.io_ontology#uuid  
    string https___climatepub4kg.github.io_ontology#name  
    string https___climatepub4kg.github.io_ontology#names  
}
HttpsClimatepub4kg.github.ioOntology#Field {
    string https___climatepub4kg.github.io_ontology#uuid  
    string https___climatepub4kg.github.io_ontology#paper_id  
    string https___climatepub4kg.github.io_ontology#name  
}
HttpsClimatepub4kg.github.ioOntology#Forcing {
    string https___climatepub4kg.github.io_ontology#uuid  
    string https___climatepub4kg.github.io_ontology#name  
    string https___climatepub4kg.github.io_ontology#names  
}
HttpsClimatepub4kg.github.ioOntology#Frequency {
    string https___climatepub4kg.github.io_ontology#uuid  
    string https___climatepub4kg.github.io_ontology#name  
    string https___climatepub4kg.github.io_ontology#names  
}
HttpsClimatepub4kg.github.ioOntology#GridLabel {

}
HttpsClimatepub4kg.github.ioOntology#Innovation {
    string https___climatepub4kg.github.io_ontology#uuid  
    string https___climatepub4kg.github.io_ontology#paper_id  
    string https___climatepub4kg.github.io_ontology#name  
}
HttpsClimatepub4kg.github.ioOntology#Institute {
    string https___climatepub4kg.github.io_ontology#uuid  
    string https___climatepub4kg.github.io_ontology#name  
    string https___climatepub4kg.github.io_ontology#names  
}
HttpsClimatepub4kg.github.ioOntology#Instrument {
    string https___climatepub4kg.github.io_ontology#added_from_paper_id  
    string https___climatepub4kg.github.io_ontology#uuid  
    string https___climatepub4kg.github.io_ontology#name  
}
HttpsClimatepub4kg.github.ioOntology#Keyword {
    string https___climatepub4kg.github.io_ontology#uuid  
    string https___climatepub4kg.github.io_ontology#name  
}
HttpsClimatepub4kg.github.ioOntology#MIPEra {
    string https___climatepub4kg.github.io_ontology#uuid  
    string https___climatepub4kg.github.io_ontology#name  
    string https___climatepub4kg.github.io_ontology#names  
}
HttpsClimatepub4kg.github.ioOntology#Member {
    string https___climatepub4kg.github.io_ontology#uuid  
    string https___climatepub4kg.github.io_ontology#name  
    string https___climatepub4kg.github.io_ontology#names  
}
HttpsClimatepub4kg.github.ioOntology#Method {
    string https___climatepub4kg.github.io_ontology#uuid  
    string https___climatepub4kg.github.io_ontology#paper_id  
    string https___climatepub4kg.github.io_ontology#name  
}
HttpsClimatepub4kg.github.ioOntology#Metric {
    string https___climatepub4kg.github.io_ontology#added_from_paper_id  
    string https___climatepub4kg.github.io_ontology#uuid  
    string https___climatepub4kg.github.io_ontology#name  
}
HttpsClimatepub4kg.github.ioOntology#Model {
    string https___climatepub4kg.github.io_ontology#uuid  
    string https___climatepub4kg.github.io_ontology#paper_id  
    string https___climatepub4kg.github.io_ontology#name  
}
HttpsClimatepub4kg.github.ioOntology#NaturalHazardType {

}
HttpsClimatepub4kg.github.ioOntology#NaturalHazard {
    string https___climatepub4kg.github.io_ontology#added_from_paper_id  
    string https___climatepub4kg.github.io_ontology#uuid  
    string https___climatepub4kg.github.io_ontology#name  
}
HttpsClimatepub4kg.github.ioOntology#NoCountryRegion {
    string https___climatepub4kg.github.io_ontology#country_code  
    string https___climatepub4kg.github.io_ontology#name  
    string https___climatepub4kg.github.io_ontology#population  
    string https___climatepub4kg.github.io_ontology#cc2  
    string https___climatepub4kg.github.io_ontology#timezone  
    string https___climatepub4kg.github.io_ontology#admin4_code  
    string https___climatepub4kg.github.io_ontology#asciiname  
    string https___climatepub4kg.github.io_ontology#admin2_code  
    string https___climatepub4kg.github.io_ontology#admin3_code  
    string https___climatepub4kg.github.io_ontology#uuid  
    string https___climatepub4kg.github.io_ontology#geonameid  
    string https___climatepub4kg.github.io_ontology#longitude  
    string https___climatepub4kg.github.io_ontology#alternatenames  
    string https___climatepub4kg.github.io_ontology#modification_date  
    string https___climatepub4kg.github.io_ontology#dem  
    string https___climatepub4kg.github.io_ontology#latitude  
    string https___climatepub4kg.github.io_ontology#feature_class  
    string https___climatepub4kg.github.io_ontology#admin1_code  
    string https___climatepub4kg.github.io_ontology#elevation  
    string https___climatepub4kg.github.io_ontology#feature_code  
}
HttpsClimatepub4kg.github.ioOntology#ObservationalDataset {
    string https___climatepub4kg.github.io_ontology#uuid  
    string https___climatepub4kg.github.io_ontology#name  
}
HttpsClimatepub4kg.github.ioOntology#OceanCirculation {
    string https___climatepub4kg.github.io_ontology#added_from_paper_id  
    string https___climatepub4kg.github.io_ontology#uuid  
    string https___climatepub4kg.github.io_ontology#name  
}
HttpsClimatepub4kg.github.ioOntology#Paper {
    string https___climatepub4kg.github.io_ontology#id  
    string https___climatepub4kg.github.io_ontology#name  
    string https___climatepub4kg.github.io_ontology#uuid  
    string https___climatepub4kg.github.io_ontology#title  
}
HttpsClimatepub4kg.github.ioOntology#PhysicalFeature {
    string https___climatepub4kg.github.io_ontology#added_from_paper_id  
    string https___climatepub4kg.github.io_ontology#uuid  
    string https___climatepub4kg.github.io_ontology#name  
}
HttpsClimatepub4kg.github.ioOntology#PhysicalScheme {
    string https___climatepub4kg.github.io_ontology#added_from_paper_id  
    string https___climatepub4kg.github.io_ontology#uuid  
    string https___climatepub4kg.github.io_ontology#name  
}
HttpsClimatepub4kg.github.ioOntology#Platform {
    string https___climatepub4kg.github.io_ontology#added_from_paper_id  
    string https___climatepub4kg.github.io_ontology#uuid  
    string https___climatepub4kg.github.io_ontology#name  
}
HttpsClimatepub4kg.github.ioOntology#Problem {
    string https___climatepub4kg.github.io_ontology#uuid  
    string https___climatepub4kg.github.io_ontology#paper_id  
    string https___climatepub4kg.github.io_ontology#name  
}
HttpsClimatepub4kg.github.ioOntology#Project {
    string https___climatepub4kg.github.io_ontology#uuid  
    string https___climatepub4kg.github.io_ontology#name  
    string https___climatepub4kg.github.io_ontology#names  
}
HttpsClimatepub4kg.github.ioOntology#RCM {
    string https___climatepub4kg.github.io_ontology#names  
    string https___climatepub4kg.github.io_ontology#uuid  
    string https___climatepub4kg.github.io_ontology#name  
    string https___climatepub4kg.github.io_ontology#rcm_version  
}
HttpsClimatepub4kg.github.ioOntology#Realm {
    string https___climatepub4kg.github.io_ontology#uuid  
    string https___climatepub4kg.github.io_ontology#name  
    string https___climatepub4kg.github.io_ontology#names  
}
HttpsClimatepub4kg.github.ioOntology#Resolution {
    string https___climatepub4kg.github.io_ontology#uuid  
    string https___climatepub4kg.github.io_ontology#name  
    string https___climatepub4kg.github.io_ontology#names  
}
HttpsClimatepub4kg.github.ioOntology#Result {
    string https___climatepub4kg.github.io_ontology#uuid  
    string https___climatepub4kg.github.io_ontology#name  
}
HttpsClimatepub4kg.github.ioOntology#SimulationType {
    string https___climatepub4kg.github.io_ontology#added_from_paper_id  
    string https___climatepub4kg.github.io_ontology#uuid  
    string https___climatepub4kg.github.io_ontology#name  
}
HttpsClimatepub4kg.github.ioOntology#Source {
    string https___climatepub4kg.github.io_ontology#name  
    string https___climatepub4kg.github.io_ontology#uuid  
    string https___climatepub4kg.github.io_ontology#names  
}
HttpsClimatepub4kg.github.ioOntology#SourceComponent {
    string https___climatepub4kg.github.io_ontology#uuid  
    string https___climatepub4kg.github.io_ontology#name  
    string https___climatepub4kg.github.io_ontology#added_from_paper_id  
}
HttpsClimatepub4kg.github.ioOntology#SourceType {
    string https___climatepub4kg.github.io_ontology#uuid  
    string https___climatepub4kg.github.io_ontology#name  
    string https___climatepub4kg.github.io_ontology#names  
}
HttpsClimatepub4kg.github.ioOntology#SubExperiment {
    string https___climatepub4kg.github.io_ontology#uuid  
    string https___climatepub4kg.github.io_ontology#name  
    string https___climatepub4kg.github.io_ontology#names  
}
HttpsClimatepub4kg.github.ioOntology#Task {
    string https___climatepub4kg.github.io_ontology#uuid  
    string https___climatepub4kg.github.io_ontology#paper_id  
    string https___climatepub4kg.github.io_ontology#name  
}
HttpsClimatepub4kg.github.ioOntology#Teleconnection {
    string https___climatepub4kg.github.io_ontology#added_from_paper_id  
    string https___climatepub4kg.github.io_ontology#uuid  
    string https___climatepub4kg.github.io_ontology#name  
}
HttpsClimatepub4kg.github.ioOntology#Variable {
    string https___climatepub4kg.github.io_ontology#names  
    string https___climatepub4kg.github.io_ontology#uuid  
    string https___climatepub4kg.github.io_ontology#name  
    string https___climatepub4kg.github.io_ontology#variable_units  
    string https___climatepub4kg.github.io_ontology#variable_long_name  
    string https___climatepub4kg.github.io_ontology#cf_standard_name  
}
HttpsClimatepub4kg.github.ioOntology#WaterBodies {
    string https___climatepub4kg.github.io_ontology#west  
    string https___climatepub4kg.github.io_ontology#uuid  
    string https___climatepub4kg.github.io_ontology#name  
    string https___climatepub4kg.github.io_ontology#Name  
    string https___climatepub4kg.github.io_ontology#geonameid  
    string https___climatepub4kg.github.io_ontology#north  
    string https___climatepub4kg.github.io_ontology#east  
    string https___climatepub4kg.github.io_ontology#south  
}
HttpsClimatepub4kg.github.ioOntology#WeatherEvent {
    string https___climatepub4kg.github.io_ontology#added_from_paper_id  
    string https___climatepub4kg.github.io_ontology#uuid  
    string https___climatepub4kg.github.io_ontology#name  
}
HttpsClimatepub4kg.github.ioOntology#GraphConfig {

}
HttpsClimatepub4kg.github.ioOntology#MapDef {

}
HttpsClimatepub4kg.github.ioOntology#MapNs {

}
HttpsClimatepub4kg.github.ioOntology#NsPrefDef {

}

HttpsClimatepub4kg.github.ioOntology#Activity ||--|o HttpsClimatepub4kg.github.ioOntology#Realm : "https___climatepub4kg.github.io_ontology#FOCUSES_ON_REALM"
HttpsClimatepub4kg.github.ioOntology#Activity ||--|o HttpsClimatepub4kg.github.ioOntology#Project : "https___climatepub4kg.github.io_ontology#PART_OF_PROJECT"
HttpsClimatepub4kg.github.ioOntology#City ||--|o HttpsClimatepub4kg.github.ioOntology#Country : "https___climatepub4kg.github.io_ontology#IN_COUNTRY"
HttpsClimatepub4kg.github.ioOntology#Country ||--|o HttpsClimatepub4kg.github.ioOntology#Continent : "https___climatepub4kg.github.io_ontology#IN_CONTINENT"
HttpsClimatepub4kg.github.ioOntology#CountrySubdivision ||--|o HttpsClimatepub4kg.github.ioOntology#Country : "https___climatepub4kg.github.io_ontology#IN_COUNTRY"
HttpsClimatepub4kg.github.ioOntology#Experiment ||--|o HttpsClimatepub4kg.github.ioOntology#Realm : "https___climatepub4kg.github.io_ontology#APPLIES_TO_REALM"
HttpsClimatepub4kg.github.ioOntology#Experiment ||--|o HttpsClimatepub4kg.github.ioOntology#SubExperiment : "https___climatepub4kg.github.io_ontology#HAS_SUB_EXPERIMENT"
HttpsClimatepub4kg.github.ioOntology#Experiment ||--|o HttpsClimatepub4kg.github.ioOntology#Forcing : "https___climatepub4kg.github.io_ontology#USES_FORCING"
HttpsClimatepub4kg.github.ioOntology#Experiment ||--|o HttpsClimatepub4kg.github.ioOntology#Project : "https___climatepub4kg.github.io_ontology#PART_OF_PROJECT"
HttpsClimatepub4kg.github.ioOntology#Experiment ||--|o HttpsClimatepub4kg.github.ioOntology#Resolution : "https___climatepub4kg.github.io_ontology#HAS_SPATIAL_RESOLUTION"
HttpsClimatepub4kg.github.ioOntology#Experiment ||--|o HttpsClimatepub4kg.github.ioOntology#Ensemble : "https___climatepub4kg.github.io_ontology#INCLUDES_ENSEMBLE_MEMBER"
HttpsClimatepub4kg.github.ioOntology#Experiment ||--|o HttpsClimatepub4kg.github.ioOntology#Institute : "https___climatepub4kg.github.io_ontology#PERFORMED_BY_INSTITUTE"
HttpsClimatepub4kg.github.ioOntology#ExperimentFamily ||--|o HttpsClimatepub4kg.github.ioOntology#Experiment : "https___climatepub4kg.github.io_ontology#INCLUDES_EXPERIMENT"
HttpsClimatepub4kg.github.ioOntology#Institute ||--|o HttpsClimatepub4kg.github.ioOntology#Project : "https___climatepub4kg.github.io_ontology#PARTICIPATED_IN"
HttpsClimatepub4kg.github.ioOntology#Method ||--|o HttpsClimatepub4kg.github.ioOntology#Model : "https___climatepub4kg.github.io_ontology#METHOD_USES_MODEL"
HttpsClimatepub4kg.github.ioOntology#Method ||--|o HttpsClimatepub4kg.github.ioOntology#Problem : "https___climatepub4kg.github.io_ontology#METHOD_SOLVES_PROBLEM"
HttpsClimatepub4kg.github.ioOntology#Method ||--|o HttpsClimatepub4kg.github.ioOntology#Innovation : "https___climatepub4kg.github.io_ontology#METHOD_HAS_INNOVATION"
HttpsClimatepub4kg.github.ioOntology#Method ||--|o HttpsClimatepub4kg.github.ioOntology#Result : "https___climatepub4kg.github.io_ontology#METHOD_HAS_RESULT"
HttpsClimatepub4kg.github.ioOntology#Method ||--|o HttpsClimatepub4kg.github.ioOntology#ObservationalDataset : "https___climatepub4kg.github.io_ontology#METHOD_EXPERIMENTS_ON_OBSERVATIONAL_DATASET"
HttpsClimatepub4kg.github.ioOntology#Method ||--|o HttpsClimatepub4kg.github.ioOntology#Metric : "https___climatepub4kg.github.io_ontology#METHOD_USES_METRIC"
HttpsClimatepub4kg.github.ioOntology#Method ||--|o HttpsClimatepub4kg.github.ioOntology#Task : "https___climatepub4kg.github.io_ontology#METHOD_WORKS_ON_TASK"
HttpsClimatepub4kg.github.ioOntology#Model ||--|o HttpsClimatepub4kg.github.ioOntology#Source : "https___climatepub4kg.github.io_ontology#CORRESPONDS_TO"
HttpsClimatepub4kg.github.ioOntology#Model ||--|o HttpsClimatepub4kg.github.ioOntology#Result : "https___climatepub4kg.github.io_ontology#MODEL_HAS_RESULT"
HttpsClimatepub4kg.github.ioOntology#Model ||--|o HttpsClimatepub4kg.github.ioOntology#Problem : "https___climatepub4kg.github.io_ontology#MODEL_SOLVES_PROBLEM"
HttpsClimatepub4kg.github.ioOntology#Model ||--|o HttpsClimatepub4kg.github.ioOntology#ObservationalDataset : "https___climatepub4kg.github.io_ontology#MODEL_EXPERIMENTS_ON_OBSERVATIONAL_DATASET"
HttpsClimatepub4kg.github.ioOntology#Model ||--|o HttpsClimatepub4kg.github.ioOntology#Metric : "https___climatepub4kg.github.io_ontology#MODEL_USES_METRIC"
HttpsClimatepub4kg.github.ioOntology#Model ||--|o HttpsClimatepub4kg.github.ioOntology#Task : "https___climatepub4kg.github.io_ontology#MODEL_WORKS_FOR_TASK"
HttpsClimatepub4kg.github.ioOntology#Paper ||--|o HttpsClimatepub4kg.github.ioOntology#Field : "https___climatepub4kg.github.io_ontology#PAPER_BELONGS_TO_FIELD"
HttpsClimatepub4kg.github.ioOntology#Paper ||--|o HttpsClimatepub4kg.github.ioOntology#Metric : "https___climatepub4kg.github.io_ontology#PAPER_USES_METRIC"
HttpsClimatepub4kg.github.ioOntology#Paper ||--|o HttpsClimatepub4kg.github.ioOntology#ObservationalDataset : "https___climatepub4kg.github.io_ontology#PAPER_EXPERIMENTS_ON_OBSERVATIONAL_DATASET"
HttpsClimatepub4kg.github.ioOntology#Paper ||--|o HttpsClimatepub4kg.github.ioOntology#Innovation : "https___climatepub4kg.github.io_ontology#PAPER_HAS_INNOVATION"
HttpsClimatepub4kg.github.ioOntology#Paper ||--|o HttpsClimatepub4kg.github.ioOntology#Member : "https___climatepub4kg.github.io_ontology#PAPER_MENTIONS"
HttpsClimatepub4kg.github.ioOntology#Paper ||--|o HttpsClimatepub4kg.github.ioOntology#ExperimentFamily : "https___climatepub4kg.github.io_ontology#PAPER_MENTIONS"
HttpsClimatepub4kg.github.ioOntology#Paper ||--|o HttpsClimatepub4kg.github.ioOntology#Country : "https___climatepub4kg.github.io_ontology#PAPER_MENTIONS"
HttpsClimatepub4kg.github.ioOntology#Paper ||--|o HttpsClimatepub4kg.github.ioOntology#Activity : "https___climatepub4kg.github.io_ontology#PAPER_MENTIONS"
HttpsClimatepub4kg.github.ioOntology#Paper ||--|o HttpsClimatepub4kg.github.ioOntology#WeatherEvent : "https___climatepub4kg.github.io_ontology#PAPER_MENTIONS"
HttpsClimatepub4kg.github.ioOntology#Paper ||--|o HttpsClimatepub4kg.github.ioOntology#Resolution : "https___climatepub4kg.github.io_ontology#PAPER_MENTIONS"
HttpsClimatepub4kg.github.ioOntology#Paper ||--|o HttpsClimatepub4kg.github.ioOntology#Variable : "https___climatepub4kg.github.io_ontology#PAPER_MENTIONS"
HttpsClimatepub4kg.github.ioOntology#Paper ||--|o HttpsClimatepub4kg.github.ioOntology#NaturalHazard : "https___climatepub4kg.github.io_ontology#PAPER_MENTIONS"
HttpsClimatepub4kg.github.ioOntology#Paper ||--|o HttpsClimatepub4kg.github.ioOntology#OceanCirculation : "https___climatepub4kg.github.io_ontology#PAPER_MENTIONS"
HttpsClimatepub4kg.github.ioOntology#Paper ||--|o HttpsClimatepub4kg.github.ioOntology#PhysicalFeature : "https___climatepub4kg.github.io_ontology#PAPER_MENTIONS"
HttpsClimatepub4kg.github.ioOntology#Paper ||--|o HttpsClimatepub4kg.github.ioOntology#CountrySubdivision : "https___climatepub4kg.github.io_ontology#PAPER_MENTIONS"
HttpsClimatepub4kg.github.ioOntology#Paper ||--|o HttpsClimatepub4kg.github.ioOntology#Instrument : "https___climatepub4kg.github.io_ontology#PAPER_MENTIONS"
HttpsClimatepub4kg.github.ioOntology#Paper ||--|o HttpsClimatepub4kg.github.ioOntology#Teleconnection : "https___climatepub4kg.github.io_ontology#PAPER_MENTIONS"
HttpsClimatepub4kg.github.ioOntology#Paper ||--|o HttpsClimatepub4kg.github.ioOntology#Platform : "https___climatepub4kg.github.io_ontology#PAPER_MENTIONS"
HttpsClimatepub4kg.github.ioOntology#Paper ||--|o HttpsClimatepub4kg.github.ioOntology#MIPEra : "https___climatepub4kg.github.io_ontology#PAPER_MENTIONS"
HttpsClimatepub4kg.github.ioOntology#Paper ||--|o HttpsClimatepub4kg.github.ioOntology#Metric : "https___climatepub4kg.github.io_ontology#PAPER_MENTIONS"
HttpsClimatepub4kg.github.ioOntology#Paper ||--|o HttpsClimatepub4kg.github.ioOntology#Realm : "https___climatepub4kg.github.io_ontology#PAPER_MENTIONS"
HttpsClimatepub4kg.github.ioOntology#Paper ||--|o HttpsClimatepub4kg.github.ioOntology#SourceComponent : "https___climatepub4kg.github.io_ontology#PAPER_MENTIONS"
HttpsClimatepub4kg.github.ioOntology#Paper ||--|o HttpsClimatepub4kg.github.ioOntology#Source : "https___climatepub4kg.github.io_ontology#PAPER_MENTIONS"
HttpsClimatepub4kg.github.ioOntology#Paper ||--|o HttpsClimatepub4kg.github.ioOntology#WaterBodies : "https___climatepub4kg.github.io_ontology#PAPER_MENTIONS"
HttpsClimatepub4kg.github.ioOntology#Paper ||--|o HttpsClimatepub4kg.github.ioOntology#Project : "https___climatepub4kg.github.io_ontology#PAPER_MENTIONS"
HttpsClimatepub4kg.github.ioOntology#Paper ||--|o HttpsClimatepub4kg.github.ioOntology#SourceType : "https___climatepub4kg.github.io_ontology#PAPER_MENTIONS"
HttpsClimatepub4kg.github.ioOntology#Paper ||--|o HttpsClimatepub4kg.github.ioOntology#NoCountryRegion : "https___climatepub4kg.github.io_ontology#PAPER_MENTIONS"
HttpsClimatepub4kg.github.ioOntology#Paper ||--|o HttpsClimatepub4kg.github.ioOntology#PhysicalScheme : "https___climatepub4kg.github.io_ontology#PAPER_MENTIONS"
HttpsClimatepub4kg.github.ioOntology#Paper ||--|o HttpsClimatepub4kg.github.ioOntology#City : "https___climatepub4kg.github.io_ontology#PAPER_MENTIONS"
HttpsClimatepub4kg.github.ioOntology#Paper ||--|o HttpsClimatepub4kg.github.ioOntology#Institute : "https___climatepub4kg.github.io_ontology#PAPER_MENTIONS"
HttpsClimatepub4kg.github.ioOntology#Paper ||--|o HttpsClimatepub4kg.github.ioOntology#Experiment : "https___climatepub4kg.github.io_ontology#PAPER_MENTIONS"
HttpsClimatepub4kg.github.ioOntology#Paper ||--|o HttpsClimatepub4kg.github.ioOntology#Continent : "https___climatepub4kg.github.io_ontology#PAPER_MENTIONS"
HttpsClimatepub4kg.github.ioOntology#Paper ||--|o HttpsClimatepub4kg.github.ioOntology#SimulationType : "https___climatepub4kg.github.io_ontology#PAPER_MENTIONS"
HttpsClimatepub4kg.github.ioOntology#Paper ||--|o HttpsClimatepub4kg.github.ioOntology#Keyword : "https___climatepub4kg.github.io_ontology#PAPER_HAS_KEYWORD"
HttpsClimatepub4kg.github.ioOntology#Paper ||--|o HttpsClimatepub4kg.github.ioOntology#Task : "https___climatepub4kg.github.io_ontology#PAPER_WORKS_ON_TASK"
HttpsClimatepub4kg.github.ioOntology#Paper ||--|o HttpsClimatepub4kg.github.ioOntology#Result : "https___climatepub4kg.github.io_ontology#PAPER_HAS_RESULT"
HttpsClimatepub4kg.github.ioOntology#Paper ||--|o HttpsClimatepub4kg.github.ioOntology#Problem : "https___climatepub4kg.github.io_ontology#PAPER_SOLVES_PROBLEM"
HttpsClimatepub4kg.github.ioOntology#Paper ||--|o HttpsClimatepub4kg.github.ioOntology#Model : "https___climatepub4kg.github.io_ontology#PAPER_HAS_MODEL"
HttpsClimatepub4kg.github.ioOntology#Paper ||--|o HttpsClimatepub4kg.github.ioOntology#Method : "https___climatepub4kg.github.io_ontology#PAPER_APPLIES_METHOD"
HttpsClimatepub4kg.github.ioOntology#Project ||--|o HttpsClimatepub4kg.github.ioOntology#Domain : "https___climatepub4kg.github.io_ontology#COVERS_DOMAIN"
HttpsClimatepub4kg.github.ioOntology#RCM ||--|o HttpsClimatepub4kg.github.ioOntology#Source : "https___climatepub4kg.github.io_ontology#DRIVEN_BY_SOURCE"
HttpsClimatepub4kg.github.ioOntology#RCM ||--|o HttpsClimatepub4kg.github.ioOntology#Experiment : "https___climatepub4kg.github.io_ontology#USED_IN_EXPERIMENT"
HttpsClimatepub4kg.github.ioOntology#RCM ||--|o HttpsClimatepub4kg.github.ioOntology#Country : "https___climatepub4kg.github.io_ontology#COVERS_REGION"
HttpsClimatepub4kg.github.ioOntology#RCM ||--|o HttpsClimatepub4kg.github.ioOntology#WaterBodies : "https___climatepub4kg.github.io_ontology#COVERS_REGION"
HttpsClimatepub4kg.github.ioOntology#RCM ||--|o HttpsClimatepub4kg.github.ioOntology#NoCountryRegion : "https___climatepub4kg.github.io_ontology#COVERS_REGION"
HttpsClimatepub4kg.github.ioOntology#RCM ||--|o HttpsClimatepub4kg.github.ioOntology#CountrySubdivision : "https___climatepub4kg.github.io_ontology#COVERS_REGION"
HttpsClimatepub4kg.github.ioOntology#RCM ||--|o HttpsClimatepub4kg.github.ioOntology#City : "https___climatepub4kg.github.io_ontology#COVERS_REGION"
HttpsClimatepub4kg.github.ioOntology#RCM ||--|o HttpsClimatepub4kg.github.ioOntology#Continent : "https___climatepub4kg.github.io_ontology#COVERS_REGION"
HttpsClimatepub4kg.github.ioOntology#RCM ||--|o HttpsClimatepub4kg.github.ioOntology#Project : "https___climatepub4kg.github.io_ontology#PART_OF_PROJECT"
HttpsClimatepub4kg.github.ioOntology#RCM ||--|o HttpsClimatepub4kg.github.ioOntology#Variable : "https___climatepub4kg.github.io_ontology#PRODUCES_VARIABLE"
HttpsClimatepub4kg.github.ioOntology#RCM ||--|o HttpsClimatepub4kg.github.ioOntology#Domain : "https___climatepub4kg.github.io_ontology#COVERS_DOMAIN"
HttpsClimatepub4kg.github.ioOntology#Result ||--|o HttpsClimatepub4kg.github.ioOntology#Metric : "https___climatepub4kg.github.io_ontology#RESULT_HAS_METRIC"
HttpsClimatepub4kg.github.ioOntology#Source ||--|o HttpsClimatepub4kg.github.ioOntology#MIPEra : "https___climatepub4kg.github.io_ontology#BELONGS_TO_MIP_ERA"
HttpsClimatepub4kg.github.ioOntology#Source ||--|o HttpsClimatepub4kg.github.ioOntology#Variable : "https___climatepub4kg.github.io_ontology#PRODUCES_VARIABLE"
HttpsClimatepub4kg.github.ioOntology#Source ||--|o HttpsClimatepub4kg.github.ioOntology#SourceType : "https___climatepub4kg.github.io_ontology#IS_OF_TYPE"
HttpsClimatepub4kg.github.ioOntology#Source ||--|o HttpsClimatepub4kg.github.ioOntology#Ensemble : "https___climatepub4kg.github.io_ontology#PART_OF_ENSEMBLE"
HttpsClimatepub4kg.github.ioOntology#Source ||--|o HttpsClimatepub4kg.github.ioOntology#PhysicalScheme : "https___climatepub4kg.github.io_ontology#USES_PHYSICAL_SCHEME"
HttpsClimatepub4kg.github.ioOntology#Source ||--|o HttpsClimatepub4kg.github.ioOntology#Experiment : "https___climatepub4kg.github.io_ontology#USED_IN_EXPERIMENT"
HttpsClimatepub4kg.github.ioOntology#Source ||--|o HttpsClimatepub4kg.github.ioOntology#Frequency : "https___climatepub4kg.github.io_ontology#SAMPLED_AT_FREQUENCY"
HttpsClimatepub4kg.github.ioOntology#Source ||--|o HttpsClimatepub4kg.github.ioOntology#PhysicalFeature : "https___climatepub4kg.github.io_ontology#HAS_PHYSICAL_FEATURE"
HttpsClimatepub4kg.github.ioOntology#Source ||--|o HttpsClimatepub4kg.github.ioOntology#Metric : "https___climatepub4kg.github.io_ontology#HAS_METRIC"
HttpsClimatepub4kg.github.ioOntology#Source ||--|o HttpsClimatepub4kg.github.ioOntology#Project : "https___climatepub4kg.github.io_ontology#PART_OF_PROJECT"
HttpsClimatepub4kg.github.ioOntology#Source ||--|o HttpsClimatepub4kg.github.ioOntology#Resolution : "https___climatepub4kg.github.io_ontology#HAS_SPATIAL_RESOLUTION"
HttpsClimatepub4kg.github.ioOntology#Source ||--|o HttpsClimatepub4kg.github.ioOntology#SourceComponent : "https___climatepub4kg.github.io_ontology#HAS_SOURCE_COMPONENT"
HttpsClimatepub4kg.github.ioOntology#Source ||--|o HttpsClimatepub4kg.github.ioOntology#Source : "https___climatepub4kg.github.io_ontology#HAS_SUBSEQUENT_VERSION"
HttpsClimatepub4kg.github.ioOntology#Source ||--|o HttpsClimatepub4kg.github.ioOntology#SourceComponent : "https___climatepub4kg.github.io_ontology#HAS_SUBSEQUENT_VERSION"
HttpsClimatepub4kg.github.ioOntology#Source ||--|o HttpsClimatepub4kg.github.ioOntology#Realm : "https___climatepub4kg.github.io_ontology#APPLIES_TO_REALM"
HttpsClimatepub4kg.github.ioOntology#Source ||--|o HttpsClimatepub4kg.github.ioOntology#Member : "https___climatepub4kg.github.io_ontology#ASSOCIATED_WITH_MEMBER"
HttpsClimatepub4kg.github.ioOntology#Source ||--|o HttpsClimatepub4kg.github.ioOntology#Source : "https___climatepub4kg.github.io_ontology#INHERITED_FROM"
HttpsClimatepub4kg.github.ioOntology#Source ||--|o HttpsClimatepub4kg.github.ioOntology#SimulationType : "https___climatepub4kg.github.io_ontology#HAS_SIMULATION_TYPE"
HttpsClimatepub4kg.github.ioOntology#Source ||--|o HttpsClimatepub4kg.github.ioOntology#Activity : "https___climatepub4kg.github.io_ontology#GENERATED_BY_ACTIVITY"
HttpsClimatepub4kg.github.ioOntology#Source ||--|o HttpsClimatepub4kg.github.ioOntology#Institute : "https___climatepub4kg.github.io_ontology#PRODUCED_BY_INSTITUTE"
HttpsClimatepub4kg.github.ioOntology#SourceComponent ||--|o HttpsClimatepub4kg.github.ioOntology#Realm : "https___climatepub4kg.github.io_ontology#APPLIES_TO_REALM"
HttpsClimatepub4kg.github.ioOntology#SourceComponent ||--|o HttpsClimatepub4kg.github.ioOntology#Variable : "https___climatepub4kg.github.io_ontology#PRODUCES_VARIABLE"
HttpsClimatepub4kg.github.ioOntology#SourceComponent ||--|o HttpsClimatepub4kg.github.ioOntology#SourceComponent : "https___climatepub4kg.github.io_ontology#HAS_SOURCE_COMPONENT"
HttpsClimatepub4kg.github.ioOntology#SourceComponent ||--|o HttpsClimatepub4kg.github.ioOntology#Source : "https___climatepub4kg.github.io_ontology#HAS_SUBSEQUENT_VERSION"
HttpsClimatepub4kg.github.ioOntology#SourceComponent ||--|o HttpsClimatepub4kg.github.ioOntology#SourceComponent : "https___climatepub4kg.github.io_ontology#HAS_SUBSEQUENT_VERSION"
HttpsClimatepub4kg.github.ioOntology#Task ||--|o HttpsClimatepub4kg.github.ioOntology#Problem : "https___climatepub4kg.github.io_ontology#TASK_FACES_PROBLEM"
HttpsClimatepub4kg.github.ioOntology#Task ||--|o HttpsClimatepub4kg.github.ioOntology#ObservationalDataset : "https___climatepub4kg.github.io_ontology#TASK_EXPERIMENTS_ON_OBSERVATIONAL_DATASET"
HttpsClimatepub4kg.github.ioOntology#Task ||--|o HttpsClimatepub4kg.github.ioOntology#Metric : "https___climatepub4kg.github.io_ontology#TASK_USES_METRIC"
HttpsClimatepub4kg.github.ioOntology#Variable ||--|o HttpsClimatepub4kg.github.ioOntology#Resolution : "https___climatepub4kg.github.io_ontology#HAS_SPATIAL_RESOLUTION"

```



## Imports


* linkml:types
* okns:extended_types



## Classes

| Class | Description | Occurrences |
| --- | --- | --- |
| [HttpsClimatepub4kg.github.ioOntology#GraphConfig](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/classes/HttpsClimatepub4kg.github.ioOntology#GraphConfig.md) | None<br/>|  | 
| [HttpsClimatepub4kg.github.ioOntology#MapDef](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/classes/HttpsClimatepub4kg.github.ioOntology#MapDef.md) | None<br/>|  | 
| [HttpsClimatepub4kg.github.ioOntology#MapNs](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/classes/HttpsClimatepub4kg.github.ioOntology#MapNs.md) | None<br/>|  | 
| [HttpsClimatepub4kg.github.ioOntology#NsPrefDef](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/classes/HttpsClimatepub4kg.github.ioOntology#NsPrefDef.md) | None<br/>|  | 
| [HttpsClimatepub4kg.github.ioOntology#Activity](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/classes/HttpsClimatepub4kg.github.ioOntology#Activity.md) | None<br/>| 26 | 
| [HttpsClimatepub4kg.github.ioOntology#City](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/classes/HttpsClimatepub4kg.github.ioOntology#City.md) | None<br/>| 30062 | 
| [HttpsClimatepub4kg.github.ioOntology#Continent](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/classes/HttpsClimatepub4kg.github.ioOntology#Continent.md) | None<br/>| 7 | 
| [HttpsClimatepub4kg.github.ioOntology#Country](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/classes/HttpsClimatepub4kg.github.ioOntology#Country.md) | None<br/>| 252 | 
| [HttpsClimatepub4kg.github.ioOntology#CountrySubdivision](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/classes/HttpsClimatepub4kg.github.ioOntology#CountrySubdivision.md) | None<br/>| 3893 | 
| [HttpsClimatepub4kg.github.ioOntology#Domain](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/classes/HttpsClimatepub4kg.github.ioOntology#Domain.md) | None<br/>| 39 | 
| [HttpsClimatepub4kg.github.ioOntology#Ensemble](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/classes/HttpsClimatepub4kg.github.ioOntology#Ensemble.md) | None<br/>| 552 | 
| [HttpsClimatepub4kg.github.ioOntology#Experiment](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/classes/HttpsClimatepub4kg.github.ioOntology#Experiment.md) | None<br/>| 481 | 
| [HttpsClimatepub4kg.github.ioOntology#ExperimentFamily](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/classes/HttpsClimatepub4kg.github.ioOntology#ExperimentFamily.md) | None<br/>| 9 | 
| [HttpsClimatepub4kg.github.ioOntology#Field](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/classes/HttpsClimatepub4kg.github.ioOntology#Field.md) | None<br/>| 15 | 
| [HttpsClimatepub4kg.github.ioOntology#Forcing](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/classes/HttpsClimatepub4kg.github.ioOntology#Forcing.md) | None<br/>| 204 | 
| [HttpsClimatepub4kg.github.ioOntology#Frequency](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/classes/HttpsClimatepub4kg.github.ioOntology#Frequency.md) | None<br/>| 16 | 
| [HttpsClimatepub4kg.github.ioOntology#GridLabel](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/classes/HttpsClimatepub4kg.github.ioOntology#GridLabel.md) | None<br/>|  | 
| [HttpsClimatepub4kg.github.ioOntology#Innovation](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/classes/HttpsClimatepub4kg.github.ioOntology#Innovation.md) | None<br/>| 38 | 
| [HttpsClimatepub4kg.github.ioOntology#Institute](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/classes/HttpsClimatepub4kg.github.ioOntology#Institute.md) | None<br/>| 132 | 
| [HttpsClimatepub4kg.github.ioOntology#Instrument](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/classes/HttpsClimatepub4kg.github.ioOntology#Instrument.md) | None<br/>| 49 | 
| [HttpsClimatepub4kg.github.ioOntology#Keyword](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/classes/HttpsClimatepub4kg.github.ioOntology#Keyword.md) | None<br/>| 85 | 
| [HttpsClimatepub4kg.github.ioOntology#Member](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/classes/HttpsClimatepub4kg.github.ioOntology#Member.md) | None<br/>| 5929 | 
| [HttpsClimatepub4kg.github.ioOntology#Method](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/classes/HttpsClimatepub4kg.github.ioOntology#Method.md) | None<br/>| 38 | 
| [HttpsClimatepub4kg.github.ioOntology#Metric](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/classes/HttpsClimatepub4kg.github.ioOntology#Metric.md) | None<br/>| 699 | 
| [HttpsClimatepub4kg.github.ioOntology#MIPEra](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/classes/HttpsClimatepub4kg.github.ioOntology#MIPEra.md) | None<br/>| 4 | 
| [HttpsClimatepub4kg.github.ioOntology#Model](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/classes/HttpsClimatepub4kg.github.ioOntology#Model.md) | None<br/>| 37 | 
| [HttpsClimatepub4kg.github.ioOntology#NaturalHazard](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/classes/HttpsClimatepub4kg.github.ioOntology#NaturalHazard.md) | None<br/>| 16 | 
| [HttpsClimatepub4kg.github.ioOntology#NaturalHazardType](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/classes/HttpsClimatepub4kg.github.ioOntology#NaturalHazardType.md) | None<br/>|  | 
| [HttpsClimatepub4kg.github.ioOntology#NoCountryRegion](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/classes/HttpsClimatepub4kg.github.ioOntology#NoCountryRegion.md) | None<br/>| 6722 | 
| [HttpsClimatepub4kg.github.ioOntology#ObservationalDataset](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/classes/HttpsClimatepub4kg.github.ioOntology#ObservationalDataset.md) | None<br/>| 99 | 
| [HttpsClimatepub4kg.github.ioOntology#OceanCirculation](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/classes/HttpsClimatepub4kg.github.ioOntology#OceanCirculation.md) | None<br/>| 113 | 
| [HttpsClimatepub4kg.github.ioOntology#Paper](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/classes/HttpsClimatepub4kg.github.ioOntology#Paper.md) | None<br/>| 38 | 
| [HttpsClimatepub4kg.github.ioOntology#PhysicalFeature](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/classes/HttpsClimatepub4kg.github.ioOntology#PhysicalFeature.md) | None<br/>| 281 | 
| [HttpsClimatepub4kg.github.ioOntology#PhysicalScheme](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/classes/HttpsClimatepub4kg.github.ioOntology#PhysicalScheme.md) | None<br/>| 700 | 
| [HttpsClimatepub4kg.github.ioOntology#Platform](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/classes/HttpsClimatepub4kg.github.ioOntology#Platform.md) | None<br/>| 27 | 
| [HttpsClimatepub4kg.github.ioOntology#Problem](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/classes/HttpsClimatepub4kg.github.ioOntology#Problem.md) | None<br/>| 38 | 
| [HttpsClimatepub4kg.github.ioOntology#Project](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/classes/HttpsClimatepub4kg.github.ioOntology#Project.md) | None<br/>| 33 | 
| [HttpsClimatepub4kg.github.ioOntology#RCM](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/classes/HttpsClimatepub4kg.github.ioOntology#RCM.md) | None<br/>| 42 | 
| [HttpsClimatepub4kg.github.ioOntology#Realm](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/classes/HttpsClimatepub4kg.github.ioOntology#Realm.md) | None<br/>| 14 | 
| [HttpsClimatepub4kg.github.ioOntology#Resolution](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/classes/HttpsClimatepub4kg.github.ioOntology#Resolution.md) | None<br/>| 15 | 
| [HttpsClimatepub4kg.github.ioOntology#Result](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/classes/HttpsClimatepub4kg.github.ioOntology#Result.md) | None<br/>| 607 | 
| [HttpsClimatepub4kg.github.ioOntology#SimulationType](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/classes/HttpsClimatepub4kg.github.ioOntology#SimulationType.md) | None<br/>| 76 | 
| [HttpsClimatepub4kg.github.ioOntology#Source](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/classes/HttpsClimatepub4kg.github.ioOntology#Source.md) | None<br/>| 394 | 
| [HttpsClimatepub4kg.github.ioOntology#SourceComponent](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/classes/HttpsClimatepub4kg.github.ioOntology#SourceComponent.md) | None<br/>| 559 | 
| [HttpsClimatepub4kg.github.ioOntology#SourceType](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/classes/HttpsClimatepub4kg.github.ioOntology#SourceType.md) | None<br/>| 16 | 
| [HttpsClimatepub4kg.github.ioOntology#SubExperiment](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/classes/HttpsClimatepub4kg.github.ioOntology#SubExperiment.md) | None<br/>| 63 | 
| [HttpsClimatepub4kg.github.ioOntology#Task](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/classes/HttpsClimatepub4kg.github.ioOntology#Task.md) | None<br/>| 38 | 
| [HttpsClimatepub4kg.github.ioOntology#Teleconnection](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/classes/HttpsClimatepub4kg.github.ioOntology#Teleconnection.md) | None<br/>| 121 | 
| [HttpsClimatepub4kg.github.ioOntology#Variable](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/classes/HttpsClimatepub4kg.github.ioOntology#Variable.md) | None<br/>| 2907 | 
| [HttpsClimatepub4kg.github.ioOntology#WaterBodies](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/classes/HttpsClimatepub4kg.github.ioOntology#WaterBodies.md) | None<br/>| 123 | 
| [HttpsClimatepub4kg.github.ioOntology#WeatherEvent](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/classes/HttpsClimatepub4kg.github.ioOntology#WeatherEvent.md) | None<br/>| 100 | 





## Slots

| Slot | Description | Occurrences |
| --- | --- | --- |
| [https___climatepub4kg.github.io_ontology#_applyNeo4jNaming](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#_applyNeo4jNaming.md) | <br/>|  |
| [https___climatepub4kg.github.io_ontology#_classLabel](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#_classLabel.md) | <br/>|  |
| [https___climatepub4kg.github.io_ontology#_classNamePropName](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#_classNamePropName.md) | <br/>|  |
| [https___climatepub4kg.github.io_ontology#_dataTypePropertyLabel](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#_dataTypePropertyLabel.md) | <br/>|  |
| [https___climatepub4kg.github.io_ontology#_domainRel](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#_domainRel.md) | <br/>|  |
| [https___climatepub4kg.github.io_ontology#_handleMultival](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#_handleMultival.md) | <br/>|  |
| [https___climatepub4kg.github.io_ontology#_handleRDFTypes](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#_handleRDFTypes.md) | <br/>|  |
| [https___climatepub4kg.github.io_ontology#_handleVocabUris](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#_handleVocabUris.md) | <br/>|  |
| [https___climatepub4kg.github.io_ontology#_IN](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#_IN.md) | <br/>|  |
| [https___climatepub4kg.github.io_ontology#_keepCustomDataTypes](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#_keepCustomDataTypes.md) | <br/>|  |
| [https___climatepub4kg.github.io_ontology#_keepLangTag](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#_keepLangTag.md) | <br/>|  |
| [https___climatepub4kg.github.io_ontology#_key](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#_key.md) | <br/>|  |
| [https___climatepub4kg.github.io_ontology#_local](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#_local.md) | <br/>|  |
| [https___climatepub4kg.github.io_ontology#_ns](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#_ns.md) | <br/>|  |
| [https___climatepub4kg.github.io_ontology#_objectPropertyLabel](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#_objectPropertyLabel.md) | <br/>|  |
| [https___climatepub4kg.github.io_ontology#_prefix](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#_prefix.md) | <br/>|  |
| [https___climatepub4kg.github.io_ontology#_rangeRel](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#_rangeRel.md) | <br/>|  |
| [https___climatepub4kg.github.io_ontology#_relNamePropName](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#_relNamePropName.md) | <br/>|  |
| [https___climatepub4kg.github.io_ontology#_subClassOfRel](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#_subClassOfRel.md) | <br/>|  |
| [https___climatepub4kg.github.io_ontology#_subPropertyOfRel](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#_subPropertyOfRel.md) | <br/>|  |
| [https___climatepub4kg.github.io_ontology#added_from_paper_id](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#added_from_paper_id.md) | <br/>| 2204 |
| [https___climatepub4kg.github.io_ontology#admin1_code](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#admin1_code.md) | <br/>| 36784 |
| [https___climatepub4kg.github.io_ontology#admin2_code](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#admin2_code.md) | <br/>| 36784 |
| [https___climatepub4kg.github.io_ontology#admin3_code](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#admin3_code.md) | <br/>| 36784 |
| [https___climatepub4kg.github.io_ontology#admin4_code](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#admin4_code.md) | <br/>| 36784 |
| [https___climatepub4kg.github.io_ontology#alternatenames](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#alternatenames.md) | <br/>| 36784 |
| [https___climatepub4kg.github.io_ontology#APPLIES_TO_REALM](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#APPLIES_TO_REALM.md) | <br/>| 3820 |
| [https___climatepub4kg.github.io_ontology#area_sqkm](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#area_sqkm.md) | <br/>| 252 |
| [https___climatepub4kg.github.io_ontology#asciiname](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#asciiname.md) | <br/>| 40677 |
| [https___climatepub4kg.github.io_ontology#ASSOCIATED_WITH_MEMBER](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#ASSOCIATED_WITH_MEMBER.md) | <br/>| 11903 |
| [https___climatepub4kg.github.io_ontology#BELONGS_TO_MIP_ERA](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#BELONGS_TO_MIP_ERA.md) | <br/>| 318 |
| [https___climatepub4kg.github.io_ontology#capital](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#capital.md) | <br/>| 252 |
| [https___climatepub4kg.github.io_ontology#cc2](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#cc2.md) | <br/>| 36784 |
| [https___climatepub4kg.github.io_ontology#cf_standard_name](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#cf_standard_name.md) | <br/>| 2401 |
| [https___climatepub4kg.github.io_ontology#clm](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#clm.md) | <br/>|  |
| [https___climatepub4kg.github.io_ontology#clmid](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#clmid.md) | <br/>|  |
| [https___climatepub4kg.github.io_ontology#code](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#code.md) | <br/>| 3893 |
| [https___climatepub4kg.github.io_ontology#continent](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#continent.md) | <br/>| 252 |
| [https___climatepub4kg.github.io_ontology#CORRESPONDS_TO](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#CORRESPONDS_TO.md) | <br/>| 15 |
| [https___climatepub4kg.github.io_ontology#country](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#country.md) | <br/>| 252 |
| [https___climatepub4kg.github.io_ontology#country_code](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#country_code.md) | <br/>| 36784 |
| [https___climatepub4kg.github.io_ontology#COVERS_DOMAIN](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#COVERS_DOMAIN.md) | <br/>| 125 |
| [https___climatepub4kg.github.io_ontology#COVERS_REGION](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#COVERS_REGION.md) | <br/>| 397621 |
| [https___climatepub4kg.github.io_ontology#currencycode](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#currencycode.md) | <br/>| 252 |
| [https___climatepub4kg.github.io_ontology#currencyname](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#currencyname.md) | <br/>| 252 |
| [https___climatepub4kg.github.io_ontology#dem](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#dem.md) | <br/>| 36784 |
| [https___climatepub4kg.github.io_ontology#DRIVEN_BY_SOURCE](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#DRIVEN_BY_SOURCE.md) | <br/>| 139 |
| [https___climatepub4kg.github.io_ontology#east](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#east.md) | <br/>| 4268 |
| [https___climatepub4kg.github.io_ontology#elevation](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#elevation.md) | <br/>| 36784 |
| [https___climatepub4kg.github.io_ontology#equivalent_fips_code](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#equivalent_fips_code.md) | <br/>| 252 |
| [https___climatepub4kg.github.io_ontology#experiment_title](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#experiment_title.md) | <br/>| 261 |
| [https___climatepub4kg.github.io_ontology#feature_class](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#feature_class.md) | <br/>| 36784 |
| [https___climatepub4kg.github.io_ontology#feature_code](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#feature_code.md) | <br/>| 36784 |
| [https___climatepub4kg.github.io_ontology#fips](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#fips.md) | <br/>| 252 |
| [https___climatepub4kg.github.io_ontology#FOCUSES_ON_REALM](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#FOCUSES_ON_REALM.md) | <br/>| 170 |
| [https___climatepub4kg.github.io_ontology#GENERATED_BY_ACTIVITY](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#GENERATED_BY_ACTIVITY.md) | <br/>| 623 |
| [https___climatepub4kg.github.io_ontology#geonameid](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#geonameid.md) | <br/>| 41059 |
| [https___climatepub4kg.github.io_ontology#HAS_METRIC](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#HAS_METRIC.md) | <br/>| 49 |
| [https___climatepub4kg.github.io_ontology#HAS_PHYSICAL_FEATURE](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#HAS_PHYSICAL_FEATURE.md) | <br/>| 43 |
| [https___climatepub4kg.github.io_ontology#HAS_SIMULATION_TYPE](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#HAS_SIMULATION_TYPE.md) | <br/>| 37 |
| [https___climatepub4kg.github.io_ontology#HAS_SOURCE_COMPONENT](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#HAS_SOURCE_COMPONENT.md) | <br/>| 504 |
| [https___climatepub4kg.github.io_ontology#HAS_SPATIAL_RESOLUTION](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#HAS_SPATIAL_RESOLUTION.md) | <br/>| 6708 |
| [https___climatepub4kg.github.io_ontology#HAS_SUB_EXPERIMENT](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#HAS_SUB_EXPERIMENT.md) | <br/>| 72 |
| [https___climatepub4kg.github.io_ontology#HAS_SUBSEQUENT_VERSION](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#HAS_SUBSEQUENT_VERSION.md) | <br/>| 44 |
| [https___climatepub4kg.github.io_ontology#id](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#id.md) | <br/>| 38 |
| [https___climatepub4kg.github.io_ontology#IN_CONTINENT](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#IN_CONTINENT.md) | <br/>| 210 |
| [https___climatepub4kg.github.io_ontology#IN_COUNTRY](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#IN_COUNTRY.md) | <br/>| 33923 |
| [https___climatepub4kg.github.io_ontology#INCLUDES_ENSEMBLE_MEMBER](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#INCLUDES_ENSEMBLE_MEMBER.md) | <br/>| 3069 |
| [https___climatepub4kg.github.io_ontology#INCLUDES_EXPERIMENT](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#INCLUDES_EXPERIMENT.md) | <br/>| 328 |
| [https___climatepub4kg.github.io_ontology#INHERITED_FROM](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#INHERITED_FROM.md) | <br/>| 2 |
| [https___climatepub4kg.github.io_ontology#IS_OF_TYPE](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#IS_OF_TYPE.md) | <br/>| 295 |
| [https___climatepub4kg.github.io_ontology#iso](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#iso.md) | <br/>| 259 |
| [https___climatepub4kg.github.io_ontology#iso3](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#iso3.md) | <br/>| 252 |
| [https___climatepub4kg.github.io_ontology#isonumeric](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#isonumeric.md) | <br/>| 252 |
| [https___climatepub4kg.github.io_ontology#languages](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#languages.md) | <br/>| 252 |
| [https___climatepub4kg.github.io_ontology#latitude](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#latitude.md) | <br/>| 36784 |
| [https___climatepub4kg.github.io_ontology#longitude](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#longitude.md) | <br/>| 36784 |
| [https___climatepub4kg.github.io_ontology#METHOD_EXPERIMENTS_ON_OBSERVATIONAL_DATASET](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#METHOD_EXPERIMENTS_ON_OBSERVATIONAL_DATASET.md) | <br/>| 127 |
| [https___climatepub4kg.github.io_ontology#METHOD_HAS_INNOVATION](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#METHOD_HAS_INNOVATION.md) | <br/>| 38 |
| [https___climatepub4kg.github.io_ontology#METHOD_HAS_RESULT](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#METHOD_HAS_RESULT.md) | <br/>| 669 |
| [https___climatepub4kg.github.io_ontology#METHOD_SOLVES_PROBLEM](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#METHOD_SOLVES_PROBLEM.md) | <br/>| 38 |
| [https___climatepub4kg.github.io_ontology#METHOD_USES_METRIC](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#METHOD_USES_METRIC.md) | <br/>| 438 |
| [https___climatepub4kg.github.io_ontology#METHOD_USES_MODEL](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#METHOD_USES_MODEL.md) | <br/>| 38 |
| [https___climatepub4kg.github.io_ontology#METHOD_WORKS_ON_TASK](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#METHOD_WORKS_ON_TASK.md) | <br/>| 38 |
| [https___climatepub4kg.github.io_ontology#MODEL_EXPERIMENTS_ON_OBSERVATIONAL_DATASET](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#MODEL_EXPERIMENTS_ON_OBSERVATIONAL_DATASET.md) | <br/>| 127 |
| [https___climatepub4kg.github.io_ontology#MODEL_HAS_RESULT](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#MODEL_HAS_RESULT.md) | <br/>| 669 |
| [https___climatepub4kg.github.io_ontology#MODEL_SOLVES_PROBLEM](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#MODEL_SOLVES_PROBLEM.md) | <br/>| 38 |
| [https___climatepub4kg.github.io_ontology#MODEL_USES_METRIC](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#MODEL_USES_METRIC.md) | <br/>| 438 |
| [https___climatepub4kg.github.io_ontology#MODEL_WORKS_FOR_TASK](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#MODEL_WORKS_FOR_TASK.md) | <br/>| 38 |
| [https___climatepub4kg.github.io_ontology#modification_date](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#modification_date.md) | <br/>| 36784 |
| [https___climatepub4kg.github.io_ontology#Name](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#Name.md) | <br/>| 123 |
| [https___climatepub4kg.github.io_ontology#name](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#name.md) | <br/>| 55709 |
| [https___climatepub4kg.github.io_ontology#names](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#names.md) | <br/>| 10876 |
| [https___climatepub4kg.github.io_ontology#neighbours](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#neighbours.md) | <br/>| 252 |
| [https___climatepub4kg.github.io_ontology#north](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#north.md) | <br/>| 4268 |
| [https___climatepub4kg.github.io_ontology#PAPER_APPLIES_METHOD](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#PAPER_APPLIES_METHOD.md) | <br/>| 38 |
| [https___climatepub4kg.github.io_ontology#PAPER_BELONGS_TO_FIELD](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#PAPER_BELONGS_TO_FIELD.md) | <br/>| 38 |
| [https___climatepub4kg.github.io_ontology#PAPER_EXPERIMENTS_ON_OBSERVATIONAL_DATASET](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#PAPER_EXPERIMENTS_ON_OBSERVATIONAL_DATASET.md) | <br/>| 127 |
| [https___climatepub4kg.github.io_ontology#PAPER_HAS_INNOVATION](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#PAPER_HAS_INNOVATION.md) | <br/>| 38 |
| [https___climatepub4kg.github.io_ontology#PAPER_HAS_KEYWORD](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#PAPER_HAS_KEYWORD.md) | <br/>| 176 |
| [https___climatepub4kg.github.io_ontology#PAPER_HAS_MODEL](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#PAPER_HAS_MODEL.md) | <br/>| 38 |
| [https___climatepub4kg.github.io_ontology#PAPER_HAS_RESULT](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#PAPER_HAS_RESULT.md) | <br/>| 669 |
| [https___climatepub4kg.github.io_ontology#paper_id](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#paper_id.md) | <br/>| 204 |
| [https___climatepub4kg.github.io_ontology#PAPER_MENTIONS](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#PAPER_MENTIONS.md) | <br/>| 4462 |
| [https___climatepub4kg.github.io_ontology#PAPER_SOLVES_PROBLEM](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#PAPER_SOLVES_PROBLEM.md) | <br/>| 38 |
| [https___climatepub4kg.github.io_ontology#PAPER_USES_METRIC](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#PAPER_USES_METRIC.md) | <br/>| 438 |
| [https___climatepub4kg.github.io_ontology#PAPER_WORKS_ON_TASK](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#PAPER_WORKS_ON_TASK.md) | <br/>| 38 |
| [https___climatepub4kg.github.io_ontology#PART_OF_ENSEMBLE](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#PART_OF_ENSEMBLE.md) | <br/>| 53 |
| [https___climatepub4kg.github.io_ontology#PART_OF_PROJECT](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#PART_OF_PROJECT.md) | <br/>| 1048 |
| [https___climatepub4kg.github.io_ontology#PARTICIPATED_IN](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#PARTICIPATED_IN.md) | <br/>| 213 |
| [https___climatepub4kg.github.io_ontology#PERFORMED_BY_INSTITUTE](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#PERFORMED_BY_INSTITUTE.md) | <br/>| 2762 |
| [https___climatepub4kg.github.io_ontology#phone](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#phone.md) | <br/>| 252 |
| [https___climatepub4kg.github.io_ontology#population](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#population.md) | <br/>| 37036 |
| [https___climatepub4kg.github.io_ontology#postal_code_format](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#postal_code_format.md) | <br/>| 252 |
| [https___climatepub4kg.github.io_ontology#postal_code_regex](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#postal_code_regex.md) | <br/>| 252 |
| [https___climatepub4kg.github.io_ontology#PRODUCED_BY_INSTITUTE](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#PRODUCED_BY_INSTITUTE.md) | <br/>| 503 |
| [https___climatepub4kg.github.io_ontology#PRODUCES_VARIABLE](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#PRODUCES_VARIABLE.md) | <br/>| 30757 |
| [https___climatepub4kg.github.io_ontology#rcm_version](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#rcm_version.md) | <br/>| 42 |
| [https___climatepub4kg.github.io_ontology#RESULT_HAS_METRIC](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#RESULT_HAS_METRIC.md) | <br/>| 724 |
| [https___climatepub4kg.github.io_ontology#SAMPLED_AT_FREQUENCY](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#SAMPLED_AT_FREQUENCY.md) | <br/>| 828 |
| [https___climatepub4kg.github.io_ontology#south](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#south.md) | <br/>| 4268 |
| [https___climatepub4kg.github.io_ontology#TASK_EXPERIMENTS_ON_OBSERVATIONAL_DATASET](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#TASK_EXPERIMENTS_ON_OBSERVATIONAL_DATASET.md) | <br/>| 127 |
| [https___climatepub4kg.github.io_ontology#TASK_FACES_PROBLEM](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#TASK_FACES_PROBLEM.md) | <br/>| 38 |
| [https___climatepub4kg.github.io_ontology#TASK_USES_METRIC](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#TASK_USES_METRIC.md) | <br/>| 438 |
| [https___climatepub4kg.github.io_ontology#timezone](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#timezone.md) | <br/>| 36784 |
| [https___climatepub4kg.github.io_ontology#title](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#title.md) | <br/>| 38 |
| [https___climatepub4kg.github.io_ontology#tld](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#tld.md) | <br/>| 252 |
| [https___climatepub4kg.github.io_ontology#USED_IN_EXPERIMENT](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#USED_IN_EXPERIMENT.md) | <br/>| 2019 |
| [https___climatepub4kg.github.io_ontology#USES_FORCING](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#USES_FORCING.md) | <br/>| 986 |
| [https___climatepub4kg.github.io_ontology#USES_PHYSICAL_SCHEME](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#USES_PHYSICAL_SCHEME.md) | <br/>| 89 |
| [https___climatepub4kg.github.io_ontology#uuid](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#uuid.md) | <br/>| 55709 |
| [https___climatepub4kg.github.io_ontology#variable_long_name](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#variable_long_name.md) | <br/>| 2899 |
| [https___climatepub4kg.github.io_ontology#variable_units](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#variable_units.md) | <br/>| 2906 |
| [https___climatepub4kg.github.io_ontology#west](https://github.com/frink-okn/graph-descriptions/blob/main/climatepub4-kg/slots/https___climatepub4kg.github.io_ontology#west.md) | <br/>| 4268 |









## IRI prefixes

* linkml: https://w3id.org/linkml/
* okn: https://purl.org/okn/
* okns: https://purl.org/okn/schema/
* owl: http://www.w3.org/2002/07/owl#
* xsd: http://www.w3.org/2001/XMLSchema#
