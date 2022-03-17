## IUS (Intolerance of Uncertainty Scale)

This repo contains the main PDF, REDCap import .zip, and REDCap survey PDF for the IUS questionnaire.


### Scoring Script
The IUS questionnaire is included in the repository scoring script. Threshold for scoring is 100%.

| Variable | Details |
| :--  | :--  |
| ius_scrdTotal_sX_rX_eX | total score: sum of all items (NaN if partial response prevents calculation of subscore) |
| ius_scrdPas_sX_rX_eX | prospective anxiety subscore: sum of 1, 2, 4, 5, 8, 9, and 11 (NaN if partial response prevents calculation of subscore) |
| ius_scrdIas_sX_rX_eX | inhibitory anxiety subscore: sum of 3, 6, 7, 10, and 12 (NaN if partial response prevents calculation of subscore) |
| ius_percTotal_sX_rX_eX | percentage of responses for all items (NaN if all items are blank) |
| ius_percPas_sX_rX_eX | percentage of responses for prospective anxiety subscore (NaN if all items are blank) |
| ius_percIas_sX_rX_eX | percentage of responses for inhibitory anxiety subscore (NaN if all items are blank) |

> Carleton, R. N., Norton, M. A., & Asmundson, G. J. (2007). Fearing the unknown: a short version of the Intolerance of Uncertainty Scale. Journal of Anxiety Disorders, 21(1), 105–117. [[link]](https://pubmed.ncbi.nlm.nih.gov/16647833/)