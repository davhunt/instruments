## AMBI+RMBI

This repo contains the main PDF, REDCap import .zip, and REDCap survey PDF for the combined AMBI and RMBI questionnaire.


### Scoring Script
The combined AMBI and RMBI questionnaire is included in the repository scoring script.  Items that are reverse scored are indicated with an *. Threshold for scoring is 100%.

| Variable | Details |
| :--  | :--  |
| ambi_scrdTotal_sX_rX_eX | total score: sum of all items after items indicated below have been reverse scored (NaN if partial response prevents calculation of score) |
| ambi_scrdInh_sX_rX_eX | fearful inhibition subscore: sum of 1, 2, 3, 5, 8, 10, and 11 (NaN if partial response prevents calculation of subscore) |
| ambi_scrdNon_sX_rX_eX | non-approach subscore: sum of 4*, 6*, and 9* (NaN if partial response prevents calculation of subscore) |
| ambi_scrdLow_sX_rX_eX | low sociability subscore: sum of 12, 14, and 15* (NaN if partial response prevents calculation of subscore) |
| ambi_scrdRisk_sX_rX_eX | risk avoidance subscore: sum of 7, 13*, and 16* (NaN if partial response prevents calculation of subscore) |
| ambi_percTotal_sX_rX_eX | percentage of response for all items |
| ambi_percInh_sX_rX_eX | percentage of response for fearful inhibition subscore |
| ambi_percNon_sX_rX_eX | percentage of response for non-approach subscore |
| ambi_percLow_sX_rX_eX | percentage of response for low sociability subscore |
| ambi_percRisk_sX_rX_eX | percentage of response for risk avoidance subscore |
| rmbi_scrdTotal_sX_rX_eX | total score: sum of all items after items indicated below have been reverse scored (NaN if partial response prevents calculation of score) |
| rmbi_scrdNon_sX_rX_eX | non-approach subscore: sum of 2, 4*, 5*, 9, 11*, and 15* (NaN if partial response prevents calculation of subscore) |
| rmbi_scrdInh_sX_rX_eX | fearful inhibition subscore: sum of 1, 6, 10, 16, and 18 (NaN if partial response prevents calculation of subscore) |
| rmbi_scrdRisk_sX_rX_eX | risk avoidance subscore:7*, 8, and 13* (NaN if partial response prevents calculation of subscore) |
| rmbi_scrdShy_sX_rX_eX | shyness & sensitivity subscore: sum of 3, 12, 14, and 17 (NaN if partial response prevents calculation of subscore) |
| rmbi_percTotal_sX_rX_eX | percentage of response for all items |
| rmbi_percNon_sX_rX_eX | percentage of response for non-approach subscore |
| rmbi_percInh_sX_rX_eX | percentage of response for fearful inhibition subscore |
| rmbi_percRisk_sX_rX_eX | percentage of response for risk avoidance subscore |
| rmbi_percShy_sX_rX_eX | percentage of response for shyness & sensitivity subscore |