## TEXI (Teenage Executive Functioning Inventory)

This repository contains modifiable (.docx) and PDF versions of the TEXI, including both the self-report and other-report, in English, as well as translations into Spanish for Latin America (ESLA) and Spanish for Spain (ESEU). These translations were performed by members of the NDCLab in 2021; a .csv file providing transparency on the translation process is included for each translation.

    | Name | Contribution |
    | :--  | :--  |
    | Aitana Fischer | performed the draft translation (ESLA, ESEU) |
    | Laura Gallardo | independently edited the draft (ESLA) |
    | Emily Machado | back translated the translation to English (ESLA, ESEU) |
    | Jessica Alexander | reconciled the forward and back translations (ESLA, ESEU) |

Please report any issues with the TEXI translations by posting an issue in this GitHub repository.


### texi_b
At the request of the original author, the word "sometimes" was removed from several items.  The NDCLab updated our own copy of the instrument as we were responsible for updating the Spanish translation. Details of which items were changed is available in the .csv file detailing the Spanish translation (in this subfolder).

### texi(_a)
This is the original version of the ADEXI used by the NDCLab, draw directly from the then-current version available from [the author](https://chexi.se/).  Prior to translation by members of the NDCLab, several clarifying modifications were made; these are recorded in the 'modifications' subfolder for English and were notified to the team at the Karolinska Institutet.  This version of the TEXI is now deprecated.


### Scoring Script
The English self-report of the modified TEXI is included in the repository scoring script. Threshold for scoring is 80%.

| Variable | Details |
| :--  | :--  |
| texi_scrdInh_sX_rX_eX | inhibition subscore: average of 3, 4, 6, 10, 14, 15, 16, 17, 18, 19, and 20 (NaN if partial response prevents calculation of subscore) |
| texi_scrdWm_sX_rX_eX | working memory subscore: average of , 2, 5, 7, 8, 9, 11, 12, and 13 (NaN if partial response prevents calculation of subscore) |
| texi_percInh_sX_rX_eX | percentage of response for inhibition subscore (NaN if all items are blank) |
| texi_percWm_sX_rX_eX | percentage of response for working memory subscore (NaN if all items are blank) |

> Thorell, L. B., Lazarević, N., Milovanović, I., & Bugarski Ignjatović, V. (2020). Psychometric properties of the Teenage Executive Functioning Inventory (TEXI): A freely available questionnaire for assessing deficits in working memory and inhibition among adolescents. Child Neuropsychology: A Journal on Normal and Abnormal Development in Childhood and Adolescence, 26(6), 857–864. [[link]](https://pubmed.ncbi.nlm.nih.gov/32090688/)