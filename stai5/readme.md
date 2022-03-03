## STAI5 (State-Trait Anxiety Inventory, Short Version)

This repo contains the main PDF, REDCap import .zip, and REDCap survey PDF for the combined STAIS-5 and STAIT-5 questionnaire.


### Scoring Script
The combined STAIS-5 and STAIT-5 questionnaire is included in the repository scoring script. Threshold for scoring is 100%.

| Variable | Details |
| :--  | :--  |
| stai5_scrdS_sX_rX_eX | stais5 (state anxiety): sum of items 1-5 (NaN if partial response prevents calculation of score) |
| stai5_scrdT_sX_rX_eX | stait5 (trait anxiety): sum of items 6-10 (NaN if partial response prevents calculation of score) |
| stai5_percS_sX_rX_eX | percentage of response for stais5 items (NaN if all items are blank) |
| stai5_percT_sX_rX_eX | percentage of response for stait5 items (NaN if all items are blank) |


> Zsido, A. N., Teleki, S. A., Csokasi, K., Rozsa, S., & Bandi, S. A. (2020). Development of the short version of the spielberger state-trait anxiety inventory. Psychiatry Research, 291, 113223. [[link]](https://pubmed.ncbi.nlm.nih.gov/32563747/)