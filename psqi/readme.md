## (B)PSQI

This repo contains the main PDF, REDCap import .zip, and REDCap survey PDF for the full PSQI questionnaire and the shorter BPSQI.


### Scoring Script
The BPSQI questionnaire is included in the repository scoring script. Threshold for scoring is 100%.

| Variable | Details |
| :--  | :--  |
| bpsqi_scrdTotal_sX_rX_eX | total score: sum of `Slp`, `Sd`, `Hse`, item 5, and item 6 (NA if partial response prevents calculation of score) |
| bpsqi_scrdSlp_sX_rX_eX | sleep latency subscore: weighted response to item 3 (x<16≡0, 16<=x<31≡1, 31<=x<61≡2, x>=61≡3) (NA if partial response prevents calculation of score) |
| bpsqi_scrdSd_sX_rX_eX | sleep duration subscore: weighted response to item 4 (x<5≡3, 5<=x<6≡2, 6<=x<7≡1, x>=7≡0) (NA if partial response prevents calculation of score) |
| bpsqi_scrdHse_sX_rX_eX | habitual sleep efficiency subscore: weighted response result of [(100 * item 4 (in hours))/(item 2 - item 1)] (x<65≡3, 65<=x<75≡2, 75<=x85≡1, x>=85≡0) (NA if partial response prevents calculation of score) |
| bpsqi_percTotal_sX_rX_eX | percentage of response for all items (NA if all items are blank) |
| bpsqi_percSld_sX_rX_eX | percentage of response for sleep latency subscore (NA if all items are blank) |
| bpsqi_percSd_sX_rX_eX | percentage of response for sleep duration subscore (NA if all items are blank) |
| bpsqi_percHse_sX_rX_eX | percentage of response for habitual sleep efficiency subscore (NA if all items are blank) |