## SCAARED

This repo contains the main PDF, REDCap import .zip, and REDCap survey PDF for the SCAARED questionnaire.


### scaared_b
The survey instructions were modified for online use, changing "check the box" to "select the option."

### scaared_a
This is the original version used by the NDCLab. It is now deprecated.


### Scoring Script
The SCAARED questionnaire is included in the repository scoring script. Threshold for scoring is 100%.

| Variable | Details |
| :--  | :--  |
| scaared_scrdTotal_sX_rX_eX | total score: sum of all items (NaN if partial response prevents calculation of score) |
| scaared_scrdPaSo_sX_rX_eX | panic disorder score: sum of 1, 2, 6, 9, 11, 12, 15, 17, 18, 19, 22, 25, 28, 32, 36, 38, and 40 (NaN if partial response prevents calculation of score) |
| scaared_scrdGA_sX_rX_eX | generalized anxiety score: sum of 5, 7, 8, 14, 21, 23, 24, 29, 31, 35, 37, 39, and 44 (NaN if partial response prevents calculation of score) |
| scaared_scrdSep_sX_rX_eX | separation anxiety score: sum of 4, 13, 16, 20, 26, 30, and 33 (NaN if partial response prevents calculation of score) |
| scaared_scrdSoc_sX_rX_eX | social phobias score: sum of 3, 10, 27, 34, 41, 42, and 43 (NaN if partial response prevents calculation of score) |
| scaared_percTotal_sX_rX_eX | percentage of response for all items |
| scaared_percPaSo_sX_rX_eX | percentage of response for panic disorder subscore |
| scaared_percGA_sX_rX_eX | percentage of response for generalized anxiety subscore|
| scaared_percSep_sX_rX_eX | percentage of response for separation anxiety subscire |
| scaared_percSoc_sX_rX_eX | percentage of response for social phobias subscore |