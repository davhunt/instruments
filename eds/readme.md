## EDS+HVS (Everyday Discrimination + Hypervigilance Scales)

This repo contains the main PDF, REDCap import .zip, and REDCap survey PDF for the combined EDS and HVS questionnaire.


### Scoring Script
The combined EDS+HVS questionnaire is included in the repository scoring script. Threshold for scoring is 100%.

| Variable | Details |
| :--  | :--  |
| edshvs_scrdEdsEver_sX_rX_eX | EDS ever/never score: count of items 1-5 that are >0 (NaN if partial response prevents calculation of score) |
| edshvs_scrdEdsFreq_sX_rX_eX | EDS frequency score: sum of items 1-5 (NaN if partial response prevents calculation of score) |
| edshvs_scrdEdsChron_sX_rX_eX | EDS chronicity score: sum of weighted responses to items 1-5 (0=0, 1=0.5, 2=3, 3=36, 4=104, 5=260) (NaN if partial response prevents calculation of score) |
| edshvs_scrdHvsEver_sX_rX_eX | HVS ever/never score: count of items 8-13 that are >0 (NaN if partial response prevents calculation of score) |
| edshvs_scrdHvsFreq_sX_rX_eX | HVS frequency score: sum of items 8-13 (NaN if partial response prevents calculation of score) |
| edshvs_percEdsEver_sX_rX_eX | percentage of response for EDS ever/never score (NaN if all items are blank, percEdsFreq and percEdsChron are identical to percEver) |
| edshvs_percHvsEver_sX_rX_eX | percentage of response for HVS ever/never score (NaN if all items are blank, percHvsFreq is identical to percHvsEver) |

> Williams, D. R., Yan Yu, Jackson, J. S., & Anderson, N. B. (1997). Racial Differences in Physical and Mental Health: Socio-economic Status, Stress and Discrimination. Journal of Health Psychology, 2(3), 335–351. [[link]](https://pubmed.ncbi.nlm.nih.gov/22013026/)

Citation for the scoring mechanism:
> Michaels, E., Thomas, M., Reeves, A., Price, M., Hasson, R., Chae, D., & Allen, A. (2019). Coding the Everyday Discrimination Scale: implications for exposure assessment and associations with hypertension and depression among a cross section of mid-life African American women. Journal of Epidemiology and Community Health, 73(6), 577–584. https://doi.org/10.1136/jech-2018-211230. [[link]](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7200149/)


