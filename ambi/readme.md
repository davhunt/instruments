## AMBI+RMBI

This repo contains the main PDF, REDCap import .zip, and REDCap survey PDF for the combined AMBI and RMBI questionnaire.


### Scoring Script
The combined AMBI and RMBI questionnaire is included in the repository scoring script.  Items that are reverse scored are indicated with an *. Threshold for scoring is 100%.

| Variable | Details |
| :--  | :--  |
| ambirmbi_scrdAMBI_sX_rX_eX | ambi total score: sum of all items after items indicated below have been reverse scored (NaN if partial response prevents calculation of score) |
| ambirmbi_scrdInhA_sX_rX_eX | ambi fearful inhibition subscore: sum of 1, 2, 3, 5, 8, 10, and 11 (NaN if partial response prevents calculation of subscore) |
| ambirmbi_scrdNonA_sX_rX_eX | ambi non-approach subscore: sum of 4*, 6*, and 9* (NaN if partial response prevents calculation of subscore) |
| ambirmbi_scrdLowA_sX_rX_eX | ambi low sociability subscore: sum of 12, 14, and 15* (NaN if partial response prevents calculation of subscore) |
| ambirmbi_scrdRiskA_sX_rX_eX | ambi risk avoidance subscore: sum of 7, 13*, and 16* (NaN if partial response prevents calculation of subscore) |
| ambirmbi_percAMBI_sX_rX_eX | percentage of response for all ambi items |
| ambirmbi_percInhA_sX_rX_eX | percentage of response for ambi fearful inhibition subscore |
| ambirmbi_percNonA_sX_rX_eX | percentage of response for ambi non-approach subscore |
| ambirmbi_percLowA_sX_rX_eX | percentage of response for ambi low sociability subscore |
| ambirmbi_percRiskA_sX_rX_eX | percentage of response for ambi risk avoidance subscore |
| ambirmbi_scrdRMBI_sX_rX_eX | rmbi total score: sum of all items after items indicated below have been reverse scored (NaN if partial response prevents calculation of score) |
| ambirmbi_scrdNonR_sX_rX_eX | rmbi non-approach subscore: sum of 2, 4*, 5*, 9, 11*, and 15* (NaN if partial response prevents calculation of subscore) |
| ambirmbi_scrdInhR_sX_rX_eX | rmbi fearful inhibition subscore: sum of 1, 6, 10, 16, and 18 (NaN if partial response prevents calculation of subscore) |
| ambirmbi_scrdRiskR_sX_rX_eX | rmbi risk avoidance subscore:7*, 8, and 13* (NaN if partial response prevents calculation of subscore) |
| ambirmbi_scrdShyR_sX_rX_eX | rmbi shyness & sensitivity subscore: sum of 3, 12, 14, and 17 (NaN if partial response prevents calculation of subscore) |
| ambirmbi_percRMBI_sX_rX_eX | percentage of response for all rmbi items |
| ambirmbi_percNonR_sX_rX_eX | percentage of response for rmbi non-approach subscore |
| ambirmbi_percInhR_sX_rX_eX | percentage of response for rmbi fearful inhibition subscore |
| ambirmbi_percRiskR_sX_rX_eX | percentage of response for rmbi risk avoidance subscore |
| ambirmbi_percShyR_sX_rX_eX | percentage of response for rmbi shyness & sensitivity subscore |