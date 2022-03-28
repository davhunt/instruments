## TAI (Test Anxiety Inventory)

This repo contains the main PDF, REDCap import .zip, and REDCap survey PDF for the TAI questionnaire.

### tai_b
The REDCap survey was modified to ensure proper scoring thresholding was possible. This entailed making all questions required and changing the single "Check if it applies to you" radio button to two (Yes/No) radio button options. Survey instructions were also modified for online use, changing "place a checkmark on the line next to the number of the statement" to "choose 'Yes' next to the statement."

### tai(_a)
This is the original version used by the NDCLab and **cannot be scored using the scoring script**. The original instructions were modified to provide clarity within the REDCap platform with "If you incorrectly marked an item, click "Reset" for the corresponding item." This version is now deprecated.


### Scoring Script
The TAI questionnaire is included in the repository scoring script. Threshold for scoring is 100%. In essence, given that all questions are yes/no, "sum" scoring is a count of all items that are true for a given participant.

| Variable | Details |
| :--  | :--  |
| tai_scrdOther_sX_rX_eX | 'concerns about how others will view you if you do poorly' subscore: sum of 3, 10, 17, 25, 32, 41, 46, and 47 (NA if partial response prevents calculation of subscore) |
| tai_scrdSelf_sX_rX_eX | 'concerns about your own self-image' subscore: sum of 2, 9, 16, 24, 31, 38, and 40 (NA if partial response prevents calculation of subscore) |
| tai_scrdFut_sX_rX_eX | 'concerns about your future security' subscore: sum of 1, 8, 15, 23, 30, and 49 (NA if partial response prevents calculation of subscore) |
| tai_scrdPrep_sX_rX_eX | 'concerns about not being prepared for a test' subscore: sum of 6, 11, 18, 26, 33, and 47 (NA if partial response prevents calculation of subscore) |
| tai_scrdBody_sX_rX_eX | bodily reactions subscore: sum of 5, 12, 19, 27, 34, 39, and 43 (NA if partial response prevents calculation of subscore) |
| tai_scrdMind_sX_rX_eX | thought disruptions subscore: sum of 4, 13, 20, 21, 28, 35, 36, 37, 48, and 50 (NA if partial response prevents calculation of subscore) |
| tai_scrdGen_sX_rX_eX | general test-taking anxiety subscore: sum of 7, 14, 22, 29, 44, and 45 (NA if partial response prevents calculation of subscore) |
| tai_percOther_sX_rX_eX | percentage of responses for 'concerns about how others will view you if you do poorly' subscore (NA if all items are blank) |
| tai_percSelf_sX_rX_eX | percentage of responses for 'concerns about your own self-image' subscore (NA if all items are blank) |
| tai_percFut_sX_rX_eX | percentage of responses for 'concerns about your future security' subscore (NA if all items are blank) |
| tai_percPrep_sX_rX_eX | percentage of responses for 'concerns about not being prepared for a test' subscore (NA if all items are blank) |
| tai_percBody_sX_rX_eX | percentage of responses for bodily reactions subscore (NA if all items are blank) |
| tai_percMind_sX_rX_eX | percentage of responses for thought disruptions subscore (NA if all items are blank) |
| tai_percGen_sX_rX_eX | percentage of responses for general test-taking anxiety subscore (NA if all items are blank) |

> Spielberger, C. D. (1980). The Test Anxiety Inventory. Palo Alto, CA: Consulting Psychologist Press Inc.
