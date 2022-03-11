## PANAS (Positive and Negative Affect Schedule)

This repo contains the main PDF, REDCap import .zip, and REDCap survey PDF for the PANAS questionnaire.


### panasNOW
This REDCap survey PDF and import .zip use the "moment" time instructions.


### Scoring Script
The PANAS questionnaire is included in the repository scoring script. Threshold for scoring is 100%.

| Variable | Details |
| :--  | :--  |
| panasnow_scrdPA_sX_rX_eX | positive affect (PA) score: sum of 1, 3, 5, 9, 10, 12, 14, 16, 17, and 19 (NaN if partial response prevents calculation of score) |
| panasnow_scrdNA_sX_rX_eX | negative affect (PA) score: sum of 2, 4, 6, 7, 8, 11, 13, 15, 18, and 20 (NaN if partial response prevents calculation of score) |
| panasnow_percPA_sX_rX_eX | percentage of response for PA items (NaN if all items are blank) |
| panasnow_percNA_sX_rX_eX | percentage of response for NA items (NaN if all items are blank) |

> Watson, D., Clark, L. A., & Tellegen, A. (1988). Development and validation of brief measures of positive and negative affect: the PANAS scales. Journal of Personality and Social Psychology, 54(6), 1063–1070. [[link]](https://pubmed.ncbi.nlm.nih.gov/3397865/)