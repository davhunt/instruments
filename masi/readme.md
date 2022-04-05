## MASI (Multidimensional Acculturative Stress Inventory)

This repo contains the main PDF, REDCap import .zip, and REDCap survey PDF for the MASI questionnaire.  This questionnaire only pertains to participants who identify as being multicultural; therefore, only participants who have selected a non-White ethnic/racial identification in the demographics survey should be presented with this questionnaire.


### Scoring Script
The MASI questionnaire is included in the repository scoring script. Threshold for scoring is 100%.

| Variable | Details |
| :--  | :--  |
| masi_scrdTotal_sX_rX_eX | total score: sum of all items (NA if partial response prevents calculation of subscore) |
| masi_scrdHLComp_sX_rX_eX | heritage language competence pressure subscore: sum of items 1-7 (NA if partial response prevents calculation of subscore) |
| masi_scrdENComp_sX_rX_eX | English competence pressure subscore: sum of items 8-14 (NA if partial response prevents calculation of subscore) |
| masi_scrdENAccPro_sX_rX_eX | pressure to acculturate subscore: sum of items 15-21 (NA if partial response prevents calculation of subscore) |
| masi_scrdENAccCon_sX_rX_eX | pressure against acculturation subscore: sum of items 22-25 (NA if partial response prevents calculation of subscore) |
| masi_percTotal_sX_rX_eX | percentage of responses for all items (NA if all items are blank) |
| masi_percHLComp_sX_rX_eX | percentage of responses for heritage language competence pressure subscore (NA if all items are blank) |
| masi_percENComp_sX_rX_eX | percentage of responses for English competence pressure subscore (NA if all items are blank) |
| masi_percAccPro_sX_rX_eX | percentage of responses for pressure to acculturate subscore (NA if all items are blank) |
| masi_percAccCon_sX_rX_eX | percentage of responses for pressure against acculturation subscore (NA if all items are blank) |


Original MASI:
> Rodriguez, N., Myers, H. F., Mira, C. B., Flores, T., & Garcia-Hernandez, L. (2002). Development of the Multidimensional Acculturative Stress Inventory for adults of Mexican origin. Psychological Assessment, 14(4), 451-461. [[link]](https://pubmed.ncbi.nlm.nih.gov/12501570/)
This instrument references a stressfulness rating of particular events, in addition to the 25 item questionnaire.  The NDCLab was unable to find more detail and has therefore not included any additional items in our use of the instrument.

Revised MASI:
> Castillo, L. G., Cano, M. A., Yoon, M., Jung, E., Brown, E. J., Zamboanga, B. L., . . . Whitbourne, S. K. (2015). Factor structure and factorial invariance of the Multidimensional Acculturative Stress Inventory. Psychological Assessment, 27(3), 915-924. [[link]](https://pubmed.ncbi.nlm.nih.gov/25730163/)
The original instrument was constructed specifically for adults of Mexican origin.  In this revision, "my family's heritage language" was substituted for "Spanish."  The NDCLab uses this version.  As no information was found regarding the preamble to introduce the questions to participants, we use a generic "Please rate how strongly you agree/disagree with the following statements."