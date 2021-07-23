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
  * CHEXI
  * TEXI
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
Replace this text with a description of how a new user should install and use the tool.


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
