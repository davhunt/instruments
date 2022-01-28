## SSSQ

This repo contains subfolders for the SSSQ pre-task and post-task questionnaires, which are used together.


### Scoring Script
The SSSQ questionnaire (including pre- and post-) is included in the repository scoring script. Threshold for scoring is 80%.

| Variable | Details |
| :--  | :--  |
| sssq_scrdPEng_sX_rX_eX | engagement subscore for pre-task: average of 2, 5, 11, 13, 17, 21, and 22 from the sssqpre (NaN if partial response prevents calculation of score) |
| sssq_scrdPoEng_sX_rX_eX | engagement subscore for post-task: average of 2, 5, 11, 13, 17, 21, and 22 from the sssqpost (NaN if partial response prevents calculation of score) |
| sssq_scrdDEng_sX_rX_eX | delta of engagement subscores: `scrdPoEng` - `scrdPEng` (NaN if partial response prevents calculation of score) |
| sssq_scrdPDis_sX_rX_eX | distress subscore for pre-task: average of 1, 3, 4, 6, 7, 8, 9, and 10 from the sssqpre (NaN if partial response prevents calculation of score) |
| sssq_scrdPoDis_sX_rX_eX | distress subscore for post-task: average of 1, 3, 4, 6, 7, 8, 9, and 10 from the sssqpost (NaN if partial response prevents calculation of score) |
| sssq_scrdDDis_sX_rX_eX | delta of distress subscores: `scrdPoDis` - `scrdPDis` (NaN if partial response prevents calculation of score) |
| sssq_scrdPWry_sX_rX_eX | worry subscore for pre-task: average of 14, 15, 16, 18, 19, 20, 23, and 24 from the sssqpre (NaN if partial response prevents calculation of score) |
| sssq_scrdPoWry_sX_rX_eX | worry subscore for post-task: average of 14, 15, 16, 18, 19, 20, 23, and 24 from the sssqpost (NaN if partial response prevents calculation of score) |
| sssq_scrdDWry_sX_rX_eX | delta of worry subscores: `scrdPoWry` - `scrdPWry` (NaN if partial response prevents calculation of score) |
| sssq_percPEng_sX_rX_eX | percentage of response for engagement subscore for pre-task |
| sssq_percPoEng_sX_rX_eX | percentage of response for engagement subscore for post-task |
| sssq_percPDis_sX_rX_eX | percentage of response for distress subscore for pre-task |
| sssq_percPoDis_sX_rX_eX | percentage of response for distress subscore for post-task |
| sssq_percPWry_sX_rX_eX | percentage of response for worry subscore for pre-task |
| sssq_percPoWry_sX_rX_eX | percentage of response for worry subscore for post-task |