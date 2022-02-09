## SIAS6 and SPS6

This repo contains the main PDF, REDCap import .zip, and REDCap survey PDF for the combined SIAS6 and SPS6 questionnaire.


### sias6sps6_b
The survey instructions were modified for online use, changing "circle a number" to "select the option."

### sias6sps6_a
This is the original version used by the NDCLab. It is now deprecated.


### Scoring Script
The combined SIAS6 and SPS6 questionnaire is included in the repository scoring script. Threshold for scoring is 100%.

| Variable | Details |
| :--  | :--  |
| sias6sps6_scrdSIAS_sX_rX_eX | total score for sias6: sum of 1, 2, 3, 4, 5, and 6  |
| sias6sps6_percSIAS_sX_rX_eX | percentage of response for sias6 total score (NaN if all items are blank) |
| sias6sps6_scrdSPS_sX_rX_eX | total score for sps6: sum of 7, 8, 9, 10, 11, and 12  |
| sias6sps6_percSPS_sX_rX_eX | percentage of response for spss6 total score (NaN if all items are blank) |