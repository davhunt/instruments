## PHQ-8 (Patient Health Questionnaire)

This repo contains the main PDF, REDCap import .zip, and REDCap survey PDF for the modified PHQ questionnaire used by the NDCLab: the question relating to self-harm has been deleted from the original PHQ-9.


### Scoring Script
The PHQ-8 is included in the repository scoring script. Threshold for scoring is 100%. 

| Variable | Details |
| :--  | :--  |
| phq8_scrdTotal_sX_rX_eX | sum of all items (NaN if partial response prevents calculation of score) |
| phq8_percTotal_sX_rX_eX | percentage of response for all items (NaN if all items are blank) |

> Kroenke, K., Strine, T. W., Spitzer, R. L., Williams, J. B., Berry, J. T., & Mokdad, A. H. (2009). The PHQ-8 as a measure of current depression in the general population. Journal of Affective Disorders, 114(1-3), 163–173. [[link]](https://pubmed.ncbi.nlm.nih.gov/18752852/)
