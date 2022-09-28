# instruments

## Project Goal
A home for all surveys, questionnaires, and inventories used by the NDCLab, with an automatic scoring script.


## Background & Design
Each instrument used by the lab exists in the repo as a folder, containing (as applicable):
* the published instrument
* a REDCap import .zip for the instrument
* a PDF of the instrument exported from REDCap, showing survey title and header information
* any translations completed by the NDCLab or borrowed from elsewhere
* a data dictionary, with details of all items and scores produced
* an accompanying readme file with additional details

Additionally, this repo holds the scoring script for all scorable instruments. For more information on development and planning, consult [CONTRIBUTING.md](https://github.com/NDCLab/instruments/blob/main/CONTRIBUTING.md).


## Roadmap
The following software iterations are planned for development. Each iteration is subject to change as the project progresses.

### 0.01 

* Script to handle automatic scoring of: ADEXI, AQ-10
* Upload of PDFs and REDCap exports for many other instruments that are not yet included in the scoring script.

### 0.02

* Addition to the scoring script of: AMBIRMBI, ARI, BAARS4, BFNE, ERQ, SCAARED, SIAS6SPS6, SSSQ.
* Addition of unscored surveys: initStateB, postTaskB, postTaskC
* Initial wiki documentation.

### 0.03

* Addition to the scoring script of: BMIS, IERQ, IUS, PHQ8, SRQ.

### 0.04

* Addition to the scoring script of: BPSQI, EDSHVS, IDEA, PANASRTQ, SAS2, TEXI.

### 0.05

* Addition to the scoring script of: COVID, EPEPQ15, MASI, PINTS, RVQ, TAI.
* Addition of unscored surveys: demo_c, postTaskD, thq_b.
* Addition of initial data dictionaries.

### 0.06

* Modification of NA value to "NA" (previously "N/A").
* Support for double digit event numbers and double letter instrument versioning
* Modification of perc calculations for instruments with products to provide transparent percentage across all questions (not across products)
* Addition of flag to "hide" certain scores from the output (e.g., the interim products for AQ10).

### 0.1

* TBD
* Cron jobs on the lab's HPC queue to handle automatic running of scripts on unprocessed data
* Generate comprehensive documentation on usage and functions
* Generate comprehensive testing suite to ensure stable release

### Future Directions

* Configure repository for proper packaging
* Release for pip/conda usage


## Usage

Information on how to use existing questionnaires from this repository in a new data collection project, including IRB submission, REDCap project creation, and preprocessing, is available on the associated [wiki page](https://ndclab.github.io/wiki/docs/technical-docs/instruments.html).


## Work in Development
This `main` branch contains completed releases for this project. For all work-in-progress, please switch over to the `dev` branch.


## Contributors to the Scoring Script
| Name | Role |
| ---  | ---  |
| Farukh Saidmuratov, Brandon Lopez, Osmany Pujol | collaborated on original script |
| Jess Alexander, Ana Lopez-Nuñez  | testing and organization of initial releases |
| George A. Buzzell  | guidance and resources |

Learn more about us [here](https://www.ndclab.com/people).

## Contributing
If you are interested in contributing, please read our [CONTRIBUTING.md](CONTRIBUTING.md) file.
