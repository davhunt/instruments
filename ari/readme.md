## ARI (Affective Reactivity Index)

This repo contains the main PDF, REDCap import .zip, and REDCap survey PDF for the ARI questionnaire.


### Scoring Script
The ARI questionnaire is included in the repository scoring script. Threshold for scoring `scrdRaw` is 100%. If this threshold is not met, but `percRaw` is >83%, `scrdProrat` will be output.

| Variable | Details |
| :--  | :--  |
| ari_scrdRaw_sX_rX_eX | raw score: sum of items 1-6 (NA if partial response prevents calculation of score) |
| ari_scrdProrat_sX_rX_eX | prorated score: sum of items 1-6, multiplied by 6 and divided by 5, then rounded to the nearest whole number (only calculated if `percRaw` is > 0.83 and less than 1.0, otherwise NA) |
| ari_percRaw_sX_rX_eX | percentage of response for items 1-6 (NA if all items are blank; percAvg and percProrat are identical to percRaw) |
| ari_percProrat_sX_rX_eX | percentage of response for items 1-6 (NA if all items are blank) |

> Stringaris, A., Goodman, R., Ferdinando, S., Razdan, V., Muhrer, E., Leibenluft, E., & Brotman, M. A. (2012). The Affective Reactivity Index: a concise irritability scale for clinical and research settings. Journal of Child Psychology and Psychiatry, and Allied Disciplines, 53(11), 1109–1117. [[link]](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3484687/)