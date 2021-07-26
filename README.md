# instruments

## Project Goal
A home for all surveys, questionnaires, and inventories used by the NDCLab, with an automatic scoring script.


## Background & Design
Each instrument used by the lab exists in the repo as a folder, containing (as applicable):
* the published instrument (in English and any other languages used for lab research)
* a REDCap import .zip for the instrument
* any translations completed by the NDCLab

Additionally, this repo holds the scoring script for all scorable instruments. For more information on development and planning, consult [CONTRIBUTING.md](https://github.com/NDCLab/instruments/blob/main/CONTRIBUTING.md).


## Roadmap
The following software iterations are planned for development. Each version comes with a list of requirements. Each iteration is subject to change as the project progresses.

### 0.01 

* Scripts to handle automatic scoring of the following surveys:
  * ADEXI
  * AMBI
  * RMBI
  * AQ-10
* Cron jobs on the labs personal HPC to handle manual run scripts on unprocessed data 
* Generate documentation `README` for usage

### 0.1

* Configure repository for proper packaging
* Generate comprehensive documentation on usage and functions
* Generate comprehensive testing suite to ensure stable release
  * Generate documentation on test-generation in `CONTRIBUTING`

### 1.0 

* Release for pip/conda usage

## Usage
When using an instrument from this repo in an NDCLab project on REDCap:
1. Use the PDF for submission to the FIU IRB.
2. Import the zip to REDCap. Note that the zip file uses "_s1_r1_e1". These numerical values may need to be adjusted to meet the specific needs of your study's protocol, but no other change should be made to the variable names (as other changes will break the link with the automated scoring script). See further details on the [lab's naming conventions for REDCap surveys](https://ndclab.github.io/wiki/docs/etiquette/naming-conventions.html#redcap).
3. Save REDCap data to the HPC in accordance with your study's IRB-approved protocol. Following release of version 0.01, the script will automatically output a copy of the data with the addition of all scoring columns.


## Work in Development
This `main` branch contains completed releases for this project. For all work-in-progress, please switch over to the `dev` branch.


## Contributors to the Scoring Script
| Name | Role |
| ---  | ---  |
| Osmany Pujol | created the original scoring script |
| Farukh Saidmuratov | collaborated on original script |

Learn more about us [here](www.ndclab.com/people).

## Contributing
If you are interested in contributing, please read our [CONTRIBUTING.md](CONTRIBUTING.md) file.
