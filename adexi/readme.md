## ADEXI (Adult Executive Functioning Inventory)

This repo contains modifiable (.docx) and PDF versions of the ADEXI.

For the English self-report, it also includes the REDCap import .zip and survey PDF.

In addition, this repo houses the translation of both the self-report and other-report into Spanish for Latin America; this translation was performed by members of the NDCLab in 2021.  Included is a .csv file providing transparency on the translation process.

| Name | Contribution |
| :--  | :--  |
| Aitana Fischer | performed the draft translation |
| Laura Gallardo | independently edited the draft |
| Emily Machado | back translated the translation to English |
| Jessica Alexander | reconciled the forward and back translations |

Please report any issues with the ADEXI translations by posting an issue in this GitHub repository.


### adexi_b
At the request of the original author, the word "sometimes" was removed from several items.  The NDCLab updated our own copy of the instrument as we were responsible for updating the Spanish translation. Details of which items were changed is available in the .csv file detailing the Spanish translation (in this subfolder).


### adexi(_a)
This is the original version of the ADEXI used by the NDCLab, draw directly from the then-current version available from [the author](https://chexi.se/).  This version is now deprecated.



### Scoring Script
The English self-report of the ADEXI is included in the repository scoring script. Threshold for scoring is 100%.

| Variable | Details |
| :--  | :--  |
| adexi_scrdTotal_sX_rX_eX | total score: sum of all items (NaN if partial response prevents calculation of score) |
| adexi_scrdInh_sX_rX_eX | inhibition subscore: sum of 3, 4, 6, 10, and 14 (NaN if partial response prevents calculation of subscore) |
| adexi_scrdWm_sX_rX_eX | working memory subscore: sum of 1, 2, 5, 7, 8, 9, 11, 12, and 13 (NaN if partial response prevents calculation of subscore) |
| adexi_percTotal_sX_rX_eX | percentage of response for all items (NaN if all items are blank) |
| adexi_percInh_sX_rX_eX | percentage of response for inhibition subscore (NaN if all items are blank) |
| adexi_percWm_sX_rX_eX | percentage of response for working memory subscore (NaN if all items are blank) |

> Holst, Y., & Thorell, L. B. (2018). Adult Executive Functioning Inventory (ADEXI): Validity, reliability, and relations to ADHD. International Journal of Methods in Psychiatric Research, 27(1), e1567. [[link]](https://pubmed.ncbi.nlm.nih.gov/28497641/)