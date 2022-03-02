## SSSQ (Short Stress State Questionnaire)

This repo contains subfolders for the SSSQ pre-task and post-task questionnaires, which are used together.


### Scoring Script
The SSSQ questionnaire (including pre- and post-) is included in the repository scoring script. Threshold for scoring is 80%. The NDCLab scoring script does not compute any delta scores for SSSQ questionnaires; individual researchers may want to manually compute these for each subscore by subtracting the pre-task score from the post-task score.

| Variable | Details |
| :--  | :--  |
| sssqpre_scrdEng_sX_rX_eX | engagement subscore for pre-task: average of 2, 5, 11, 12, 13, 17, 21, and 22 from the sssqpre (NaN if partial response prevents calculation of score) |
| sssqpre_scrdDis_sX_rX_eX | distress subscore for pre-task: average of 1, 3, 4, 6, 7, 8, 9, and 10 from the sssqpre (NaN if partial response prevents calculation of score) |
| sssqpre_scrdWry_sX_rX_eX | worry subscore for pre-task: average of 14, 15, 16, 18, 19, 20, 23, and 24 from the sssqpre (NaN if partial response prevents calculation of score) |
| sssqpre_percEng_sX_rX_eX | percentage of response for engagement subscore for pre-task (NaN if all items are blank) |
| sssqpre_percDis_sX_rX_eX | percentage of response for distress subscore for pre-task (NaN if all items are blank) |
| sssqpre_percWry_sX_rX_eX | percentage of response for engagement subscore for pre-task (NaN if all items are blank) |
| sssqpost_scrdEng_sX_rX_eX | engagement subscore for post-task: average of 2, 5, 11, 12, 13, 17, 21, and 22 from the sssqpost (NaN if partial response prevents calculation of score) |
| sssqpost_scrdDis_sX_rX_eX | distress subscore for post-task: average of 1, 3, 4, 6, 7, 8, 9, and 10 from the sssqpost (NaN if partial response prevents calculation of score) |
| sssqpost_scrdWry_sX_rX_eX | worry subscore for post-task: average of 14, 15, 16, 18, 19, 20, 23, and 24 from the sssqpost (NaN if partial response prevents calculation of score) |
| sssqpost_percEng_sX_rX_eX | percentage of response for engagement subscore for post-task (NaN if all items are blank) |
| sssqpost_percDis_sX_rX_eX | percentage of response for distress subscore for post-task (NaN if all items are blank) |
| sssqpost_percWry_sX_rX_eX | percentage of response for worry subscore for post-task (NaN if all items are blank) |

> Helton, W. S., & Näswall, K. (2015). Short Stress State Questionnaire: Factor structure and state change assessment. European Journal of Psychological Assessment, 31(1), 20–30. [[link]](https://psycnet.apa.org/record/2014-09900-001)