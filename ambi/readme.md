## AMBI+RMBI

This repo contains the main PDF, REDCap import .zip, and REDCap survey PDF for the combined AMBI and RMBI questionnaire.


### Scoring Script
The combined AMBI and RMBI questionnaire is included in the repository scoring script.  Items that are reverse scored are indicated with an *. Threshold for scoring is 100%.

| Variable | Details |
| :--  | :--  |
| ambirmbi_scrdAMBI_sX_rX_eX | ambi total score: sum of all items 1-16 after items indicated below have been reverse scored (NaN if partial response prevents calculation of score) |
| ambirmbi_scrdInhA_sX_rX_eX | ambi fearful inhibition subscore: sum of 1, 2, 3, 5, 8, 10, and 11 (NaN if partial response prevents calculation of subscore) |
| ambirmbi_scrdNonA_sX_rX_eX | ambi non-approach subscore: sum of 4*, 6*, and 9* (NaN if partial response prevents calculation of subscore) |
| ambirmbi_scrdLowA_sX_rX_eX | ambi low sociability subscore: sum of 12, 14, and 15* (NaN if partial response prevents calculation of subscore) |
| ambirmbi_scrdRiskA_sX_rX_eX | ambi risk avoidance subscore: sum of 7, 13*, and 16* (NaN if partial response prevents calculation of subscore) |
| ambirmbi_percAMBI_sX_rX_eX | percentage of response for all ambi items (NaN if all items are blank) |
| ambirmbi_percInhA_sX_rX_eX | percentage of response for ambi fearful inhibition subscore (NaN if all items are blank) |
| ambirmbi_percNonA_sX_rX_eX | percentage of response for ambi non-approach subscore (NaN if all items are blank) |
| ambirmbi_percLowA_sX_rX_eX | percentage of response for ambi low sociability subscore (NaN if all items are blank) |
| ambirmbi_percRiskA_sX_rX_eX | percentage of response for ambi risk avoidance subscore (NaN if all items are blank) |
| ambirmbi_scrdRMBI_sX_rX_eX | rmbi total score: sum of all items 17-34 after items indicated below have been reverse scored (NaN if partial response prevents calculation of score) |
| ambirmbi_scrdNonR_sX_rX_eX | rmbi non-approach subscore: sum of 18, 20*, 21*, 25, 27*, and 31* (NaN if partial response prevents calculation of subscore) |
| ambirmbi_scrdInhR_sX_rX_eX | rmbi fearful inhibition subscore: sum of 17, 22, 26, 32, and 34 (NaN if partial response prevents calculation of subscore) |
| ambirmbi_scrdRiskR_sX_rX_eX | rmbi risk avoidance subscore: 23*, 24, and 29* (NaN if partial response prevents calculation of subscore) |
| ambirmbi_scrdShyR_sX_rX_eX | rmbi shyness & sensitivity subscore: sum of 19, 28, 30, and 33 (NaN if partial response prevents calculation of subscore) |
| ambirmbi_percRMBI_sX_rX_eX | percentage of response for all rmbi items (NaN if all items are blank) |
| ambirmbi_percNonR_sX_rX_eX | percentage of response for rmbi non-approach subscore (NaN if all items are blank) |
| ambirmbi_percInhR_sX_rX_eX | percentage of response for rmbi fearful inhibition subscore (NaN if all items are blank) |
| ambirmbi_percRiskR_sX_rX_eX | percentage of response for rmbi risk avoidance subscore (NaN if all items are blank) |
| ambirmbi_percShyR_sX_rX_eX | percentage of response for rmbi shyness & sensitivity subscore (NaN if all items are blank) |


> Gladstone, G., & Parker, G. (2005). Measuring a behaviorally inhibited temperament style: development and initial validation of new self-report measures. Psychiatry research, 135(2), 133–143. [[link]](https://pubmed.ncbi.nlm.nih.gov/15922458/)