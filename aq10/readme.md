## AQ-10

This repo contains the main PDF, REDCap import .zip, and REDCap survey PDF for the AQ-10 questionnaire.


### Scoring Script
The English self-report is included in the repository scoring script.

| Variable | Details |
| :--  | :--  |
| aq10_scrdTotal_sX_rX_eX | total score: sum of `scrd-agreed` and `scrd-disagreed` (NaN if partial response prevents calculation of score) |
| aq10_percTotal_sX_rX_eX | percentage of response for all items |
| aq10_scrdAgr_sX_rX_eX | count of Definitely or Slightly Agree responses to items 1, 7, 8, and 10 (NaN if partial response prevents calculation of score) |
| aq10_percAgr_sX_rX_eX | percentage of response for all items included in `scrd-agreed` |
| aq10_scrdDis_sX_rX_eX | count of Definitely or Slightly Disagree responses to items 2, 3, 4, 5, 6, and 9 (NaN if partial response prevents calculation of score) |
| aq10_percDis_sX_rX_eX | percentage of response for all items included in `scrd-disagreed` |

