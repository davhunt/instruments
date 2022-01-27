## AQ-10
### Autism Spectrum Quotient

This repo contains the main PDF, REDCap import .zip, and REDCap survey PDF for the AQ-10 questionnaire.


#### Scoring Script
The AQ-10 is included in the repository scoring script. Threshold for scoring is 100%.

| Variable | Details |
| :--  | :--  |
| aq10_scrd_total_sX_rX_eX | total score: sum of `scrdAgr` and `scrdDis` (NaN if partial response prevents calculation of score) |
| aq10_perc_total_sX_rX_eX | percentage of response for all items |
| aq10_scrd_agreed_sX_rX_eX | count of Definitely or Slightly Agree responses to items 1, 7, 8, and 10 (NaN if partial response prevents calculation of score) |
| aq10_perc_agreed_sX_rX_eX | percentage of response for all items included in `scrd_agreed` |
| aq10_scrd_disagreed_sX_rX_eX | count of Definitely or Slightly Disagree responses to items 2, 3, 4, 5, 6, and 9 (NaN if partial response prevents calculation of score) |
| aq10_perc_disagreed_sX_rX_eX | percentage of response for all items included in `scrd_disagreed` |

