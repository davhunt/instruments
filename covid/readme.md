## COVID Questionnaires

This repo contains versions of COVID questionnaires used by the NDCLab, including REDCap import .zips and survey PDFs.

### covid_c
The NDCLab pivoted from using an in-house questionnaire to this short version of the COVID Impacts Questionnaire from the University of Montana.

The covid_c questionnaire is included in the repository scoring script. Threshold for scoring is 100%.

| Variable | Details |
| :--  | :--  |
| covid_c_scrdTotal_sX_rX_eX | sum of all items (NA if partial response prevents calculation of subscore) |
| covid_c_percTotal_sX_rX_eX | percentage of responses for all items (NA if all items are blank) |

> Conway, L. G., III, Woodard, S. R., & Zubrod, A. (2020, April 7). Social Psychological Measurements of COVID-19: Coronavirus Perceived Threat, Government Response, Impacts, and Experiences Questionnaires. [[link]](https://doi.org/10.31234/osf.io/z2x9a)


### covid_b
This revision is a truncation of the original questionnaire.  Most questions were reworded to ensure logical section headers.
**Reworded variables:** i1-i6
**Renumbered variables:** i15>i7, i16>i8, i17>i9, i21>i10
**Deleted variables:** i7-i14, i18-i20, i22-i24
This version is now deprecated.

### covid(_a)
This is the original questionnaire used by the NDCLab.  It covers a broad range of questions relating to experiences during, or otherwise associated with, the COVID-19 pandemic.  It is now deprecated.