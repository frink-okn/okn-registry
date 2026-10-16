---
template: overrides/kg.html
shortname: fda-tobacco-kg
title: FDA Tobacco Knowledge Graph
description: FDA Center for Tobacco Products data as RDF: tobacco marketing orders, tobacco product problem reports and the Center's published research datasets on harm perception, prevention advertising and the smokefree.gov program.
stats: https://registry.okn.us/kg-stats/fda-tobacco-kg
homepage: https://github.com/medical-device-design/FDA-kg
funding: https://www.nsf.gov/awardsearch/showAward?AWD_ID=2535091
license: "https://creativecommons.org/publicdomain/zero/1.0/"
frink-options:
  lakefs-repo: fda-tobacco-kg
  documentation-path: fda-tobacco-kg
  kgf:
    semantics:
      prefixes:
        fdatob: "https://bmedesign.org/fda-tobacco-kg/ns/"
        fdatob-id: "https://bmedesign.org/fda-tobacco-kg/id/"
      roles:
        label:
          - "http://www.w3.org/2000/01/rdf-schema#label"
      authoritative_namespaces:
        - fdatob
        - fdatob-id
contacts:
  - email: roche0619@outlook.com
    github: Roche619
    label: "Roche de Guzman"
---
The FDA Tobacco Knowledge Graph publishes the Center for Tobacco Products' public datasets as linked data, about 0.2 million triples in the first release. Every source field is kept, and every record carries its source dataset, record ID, source URL and download date.

**Main classes.**
- Tobacco marketing orders (1,226 orders, from FDA's published list at https://www.fda.gov/media/112123): the product, applicant, order type and decision date of each marketing granted order.
- `fdatob:TobaccoProblemReport` (1,383 reports), IRI `https://bmedesign.org/fda-tobacco-kg/id/tobacco-problem/<report id>`: `fdatob:dateSubmitted` (xsd:date), `fdatob:tobaccoProducts` (one value per product type, for example e-cigarettes, cigarettes, smokeless), `fdatob:reportedProductProblems` and `fdatob:reportedHealthProblems` (one value each), `fdatob:nonuserAffected` and the counts of products and problems.
- `fdatob:TobaccoHarmPerceptionRecord` (1,004 survey records, `.../tobacco-harm-record/<record>`): perceived relative risk and addictiveness of vaping, smokeless and menthol products, quit intentions, methods and barriers, as child nodes per question group.
- `fdatob:TobaccoPreventionAdStudy` (42 study rows, `.../tobacco-prevention-ad/<study>_<ad>`): effect sizes with confidence bounds for cigarette and vape beliefs and attitudes, by risk status, gender, age group and race or ethnicity.
- `fdatob:TobaccoDigitalAdStudyRow` (12 rows) and `fdatob:SmokefreeMetric` (22 rows): digital ad performance measures and smokefree.gov traffic metrics.

**Planned additions.** The Searchable Tobacco Products Database (about 17,000 products with their STN) and compliance check outcomes, which will give the problem reports product nodes to link to.

**Source and license.** openFDA tobacco/problem, the research/tobacco* datasets and FDA's list of tobacco marketing orders: public domain U.S. government works. Funded under NSF award 2535091 (Proto-OKN Theme 2: OKN-Fabric) through subaward 5136002. The graph is released under CC0 1.0.


```
provenance:
  - derivedFrom:
      label: openFDA tobacco/problem and research/tobacco datasets
      uri: https://open.fda.gov/apis/tobacco/problem/
      kind: Database
      license:
        data:
          label: Public Domain
          spdx: CC0-1.0
          uri: https://open.fda.gov/license/
  - derivedFrom:
      label: FDA tobacco marketing orders
      uri: https://www.fda.gov/media/112123
      kind: Database
      license:
        data:
          label: Public Domain
          spdx: CC0-1.0
```
