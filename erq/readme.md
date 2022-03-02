## ERQ (Emotion Regulation Questionnaire)

This repo contains the main PDF, REDCap import .zip, and REDCap survey PDF for the ERQ questionnaire.


### Scoring Script
The ERQ questionnaire is included in the repository scoring script. Threshold for scoring is 80%.

| Variable | Details |
| :--  | :--  |
| erq_scrdCogRea_sX_rX_eX | cognitive reappraisal subscore: average of 1, 3, 5, 7, 8, and 10 (NaN if partial response prevents calculation of subscore) |
| erq_scrdExpSup_sX_rX_eX | expressive suppression subscore: average of 2, 4, 6, and 9 (NaN if partial response prevents calculation of subscore) |
| erq_percCogRea_sX_rX_eX | percentage of responses for cognitive reappraisal subscore (NaN if all items are blank) |
| erq_percExpSup_sX_rX_eX | percentage of responses for expressive suppression subscore (NaN if all items are blank) |

> Gross, J. J., & John, O. P. (2003). Individual differences in two emotion regulation processes: implications for affect, relationships, and well-being. Journal of Personality and Social Psychology, 85(2), 348–362. [[link]](https://pubmed.ncbi.nlm.nih.gov/12916575/)