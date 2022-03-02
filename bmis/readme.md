## BMIS (Brief Mood Introspection Scale)

This repo contains the main PDF, REDCap import .zip, and REDCap survey PDF for the BMIS questionnaire.


### Scoring Script
The BMIS is included in the repository scoring script. Items that are reverse scored are indicated with an *. Threshold for scoring is 100%.

| Variable | Details |
| :--  | :--  |
| bmis_scrdVal_sX_rX_eX | pleasant-unpleasant (valence) score: sum of 1, 2, 3*, 4*, 5, 6, 7*, 8*, 9*, 10*, 11, 12*, 13, 14, 15*, and 16 (NaN if partial response prevents calculation of score) |
| bmis_scrdAro_sX_rX_eX | arousal-calm score: sum of 1, 3, 4*, 5, 7, 8, 11, 12, 13*, 14, 15, and 16 (NaN if partial response prevents calculation of score) |
| bmis_scrdTird_sX_rX_eX | positive-tired score: sum of 1, 4*, 5, 9*, 11, 14, and 16 (NaN if partial response prevents calculation of score) |
| bmis_scrdRlx_sX_rX_eX | negative-relaxed score: sum of 3, 7, 8, 12, 13*, and 15 (NaN if partial response prevents calculation of score) |
| bmis_percVal_sX_rX_eX | percentage of response for pleasant-unpleasant score (NaN if all items are blank) |
| bmis_percAro_sX_rX_eX | percentage of response for arousal-calm score (NaN if all items are blank) |
| bmis_percTird_sX_rX_eX | percentage of response for positive-tired score (NaN if all items are blank) |
| bmis_percRlx_sX_rX_eX | percentage of response for negative-relaxed score (NaN if all items are blank)

> Mayer, J. D., & Gaschke, Y. N. (1988). The experience and meta-experience of mood. Journal of Personality and Social Psychology, 55(1), 102–111. [[link]](https://pubmed.ncbi.nlm.nih.gov/3418484/) |