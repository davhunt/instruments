## SIAS6 and SPS6
> Peters, L., Sunderland, M., Andrews, G., Rapee, R. M., & Mattick, R. P. (2012). [Development of a short form Social Interaction Anxiety (SIAS) and Social Phobia Scale (SPS) using nonparametric item response theory: the SIAS-6 and the SPS-6](https://pubmed.ncbi.nlm.nih.gov/21744971/). Psychological assessment, 24(1), 66–76. https://doi.org/10.1037/a0024544

This repo contains the main PDF, REDCap import .zip, and REDCap survey PDF for the combined SIAS6 and SPS6 questionnaire.


### sias6sps6_b
The survey instructions were modified for online use, changing "circle a number" to "select the option."

### sias6sps6_a
This is the original version used by the NDCLab. It is now deprecated.


### Scoring Script
The combined SIAS6 and SPS6 questionnaire is included in the repository scoring script. Threshold for scoring is 100%.

| Variable | Details |
| :--  | :--  |
| sias6sps6_scrdSIAS_sX_rX_eX | total score for sias6: sum of 1, 2, 3, 4, 5, and 6 (NaN if partial response prevents calculation of subscore)  |
| sias6sps6_percSIAS_sX_rX_eX | percentage of response for sias6 total score (NaN if all items are blank) |
| sias6sps6_scrdSPS_sX_rX_eX | total score for sps6: sum of 7, 8, 9, 10, 11, and 12 (NaN if partial response prevents calculation of subscore)  |
| sias6sps6_percSPS_sX_rX_eX | percentage of response for spss6 total score (NaN if all items are blank) |