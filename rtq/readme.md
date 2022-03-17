## RTQ (Repetitive Thinking Questionnaire + PANAS-N)
This repo contains the main PDFs, combined REDCap import .zip, and combined REDCap survey PDF for the combined RTQ and the PANAS-N questionnaire.

For the full PANAS, please see the PANAS folder.


### Scoring Script
The RTQ+PANAS-N combo questionnaire is included in the repository scoring script. Threshold for scoring is 100%.

| Variable | Details |
| :--  | :--  |
| panasrtq_scrdPanas_sX_rX_eX | negative affect score: sum of items 1-10 (NaN if partial response prevents calculation of score) |
| panasrtq_scrdRtqArt_sX_rX_eX | absence of repetitive thinking score: sum of items 12, 24, 28, and 30 (NaN if partial response prevents calculation of score) |
| panasrtq_scrdRtqRnt_sX_rX_eX | repetitive negative thinking score: sum of items 11, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, and 41 (NaN if partial response prevents calculation of score) |
| panasrtq_percPanas_sX_rX_eX | percentage of response for negative affect score (NaN if all items are blank) |
| panasrtq_percRtqArt_sX_rX_eX | percentage of response for absence of repetitive thinking score (NaN if all items are blank) |
| panasrtq_percRtqRnt_sX_rX_eX | percentage of response for reptitive negative thinking score (NaN if all items are blank) |

> McEvoy, P. M., Mahoney, A. E., & Moulds, M. L. (2010). Are worry, rumination, and post-event processing one and the same? Development of the repetitive thinking questionnaire. Journal of Anxiety Disorders, 24(5), 509–519. [[link]](https://pubmed.ncbi.nlm.nih.gov/20409676/)