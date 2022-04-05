## E-PEPQ-15 (Extended Post-Event Processing Questionnaire, 15-Item)

This repo contains the main PDF, REDCap import .zip, and REDCap survey PDF for the E-PEPQ-15 questionnaire.


### Scoring Script
The E-PEPQ-15 questionnaire is included in the repository scoring script. Threshold for scoring is 80%.

| Variable | Details |
| :--  | :--  |
| epepq15_scrdTotal_sX_rX_eX | total score: average of all items (NA if partial response prevents calculation of subscore) |
| epepq15_scrdCI_sX_rX_eX | cognitive interference subscore: average of 1, 2, 3, 4, 5, 6, and 13 (NA if partial response prevents calculation of subscore) |
| epepq15_scrdNS_sX_rX_eX | negative self subscore: average of 8, 9, 12, and 15 (NA if partial response prevents calculation of subscore) |
| epepq15_scrdTP_sX_rX_eX | thoughts about the past subscore: average of 7, 10, 11, and 14 (NA if partial response prevents calculation of subscore) |
| epepq15_percTotal_sX_rX_eX | percentage of responses for total score (NA if all items are blank) |
| epepq15_percCI_sX_rX_eX | percentage of responses for cognitive interference subscore (NA if all items are blank) |
| epepq15_percNS_sX_rX_eX | percentage of responses for negative self subscore (NA if all items are blank) |
| epepq15_percTP_sX_rX_eX | percentage of responses for thoughts about the past subscore (NA if all items are blank) |



Original PEP scale:
> Rachman, S., Grüter-Andrew, J., & Shafran, R. (2000). Post-event processing in social anxiety. Behaviour Research and Therapy, 38(6), 611–617.  [[link]](https://pubmed.ncbi.nlm.nih.gov/10846809/)

Extended PEPQ:
> Fehm, L., Hoyer, J., Schneider, G., Lindemann, C., & Klusmann, U. (2008). Assessing post-event processing after social situations: a measure based on the cognitive model for social phobia. Anxiety, Stress, and Coping, 21(2), 129–142. [[link]](https://pubmed.ncbi.nlm.nih.gov/18350392/)
The NDCLab version of this questionnaire is drawn from the appendix of this paper.

Factor analysis of E-PEPQ-15
> Wong Q. J. (2015). Psychometric evaluation of the English version of the Extended Post-event Processing Questionnaire. Anxiety, Stress, and Coping, 28(2), 215–225. [[link]](https://pubmed.ncbi.nlm.nih.gov/24841332/)
Based on this validation, the NDCLab uses an 11-point Likert scale (rather than a 0-100 visual analog scale) and scores the total score and subscores (cognitive interference, negative self, and thoughts about the past) by means of averaging.  Additionally, questions 9 and 10 are dropped from the questionnaire as described in the appendix of the Fems et al. (2008) paper, and the remaining items renumbered accordingly.