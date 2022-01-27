## ARI

This repo contains the main PDF, REDCap import .zip, and REDCap survey PDF for the ARI questionnaire.


### Scoring Script
The ARI questionnaire is included in the repository scoring script. Threshold for scoring `scrdRaw` and `scrdAvg` is 100%. If this threshold is not met, but `percRaw` is >83%, `scrdProrat` will be output.

| Variable | Details |
| :--  | :--  |
| ari_scrdRaw_sX_rX_eX | raw score: sum of items 1-6 |
| ari_scrdAvg_sX_rX_eX | average score: average of items 1-6 |
| ari_scrdProrat_sX_rX_eX | prorated score: sum of items 1-5, multiplied by 5 and divided by 6, then rounded to the nearest whole number (only calculated if `percRaw` is > 0.83 and less than 1.0) |
| ari_percRaw_sX_rX_eX | percentage of response for items 1-6 |