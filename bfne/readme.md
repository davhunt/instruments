## BFNE

This repo contains the main PDF, REDCap import .zip, and REDCap survey PDF for the BFNE questionnaire.


### bfne_b
The survey instructions were corrected and modified for online use, changing "Please complete the survey below. Thank you!" to "Please select the option that best corresponds to how much you agree with each item."

### bfne_a
This is the original version used by the NDCLab. It is now deprecated.


### Scoring Script
The BFNE questionnaire is included in the repository scoring script. Threshold for scoring is 100%.

| Variable | Details |
| :--  | :--  |
| bfne_scrdTotal_sX_rX_eX | total score: sum of all items (NaN if partial response prevents calculation of score) |
| bfne_percTotal_sX_rX_eX | percentage of response for all items (NaN if all items are blank) |