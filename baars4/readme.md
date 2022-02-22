## BAARS4 (Barkley Adult ADHD Rating Scale-IV)

This repo contains the main PDF, REDCap import .zip, and REDCap survey PDF for the BAARS4 questionnaire.


### Scoring Script
The BAARS4 questionnaire is included in the repository scoring script. Threshold for scoring is 100%.

| Variable | Details |
| :--  | :--  |
| baars4_scrdAdhdSM | total ADHD score: sum of items 1-18 (NaN if partial response prevents calculation of subscore) |
| baars4_scrdAdhdCT | total ADHD symptom count: count of items in `scrdAdhdSM` where participants responded with either "3" or "4" (NaN if partial response prevents calculation of subscore) |
| baars4_scrdInatSM | inattention subscore: sum of items 1-9 (NaN if partial response prevents calculation of subscore) |
| baars4_scrdInatCT | inattention symptom count: count of items in `scrdInatSM` where participants responded with either "3" or "4" (NaN if partial response prevents calculation of subscore) |
| baars4_scrdHypSM | hyperactivity subscore: sum of items 10-14 (NaN if partial response prevents calculation of subscore) |
| baars4_scrdHypCT | hyperactivity symptom count: count of items in `scrdHypSM` where participants responded with either "3" or "4" (NaN if partial response prevents calculation of subscore) |
| baars4_scrdImpSM | impulsivity subscore: sum of items 15-18 (NaN if partial response prevents calculation of subscore) |
| baars4_scrdImpCT | impulsivity symptom count: count of items in `scrdImpSM` where participants responded with either "3" or "4" (NaN if partial response prevents calculation of subscore) |
| baars4_scrdSctSM | sluggish cognitive tempo subscore: sum of items 19-27 (NaN if partial response prevents calculation of subscore) |
| baars4_scrdSctCT | sluggish cognitive tempo symptom count: count of items in `scrdSctSM` where participants responded with either "3" or "4" (NaN if partial response prevents calculation of subscore) |
| baars4_percAdhdSM | percentage of responses for total ADHD score (NaN if all items are blank) |
| baars4_percAdhdCT | percentage of responses for total ADHD symptom count (NaN if all items are blank) |
| baars4_percInatSM | percentage of responses for inattention subscore (NaN if all items are blank) |
| baars4_percInatCT | percentage of responses for inattention symptom count (NaN if all items are blank) |
| baars4_percHypSM | percentage of responses for hyperactivity subscore (NaN if all items are blank) |
| baars4_percHypCT | percentage of responses for hyperactivity symptom count (NaN if all items are blank) |
| baars4_percImpSM | percentage of responses for impulsivity subscore (NaN if all items are blank) |
| baars4_percImpCT | percentage of responses for impulsivity symptom count (NaN if all items are blank) |
| baars4_percSctSM | percentage of responses for sluggish cognitive tempo subscore (NaN if all items are blank) |
| baars4_percSctCT | percentage of responses for sluggish cognitive tempo symptom count (NaN if all items are blank) |

> Barkley, R.A. (2011). Barkley Adult ADHD Rating Scale—IV (BAARS-IV). Guilford Press. [[link]](https://www.guilford.com/books/Barkley-Adult-ADHD-Rating-Scale-IV-BAARS-IV/Russell-Barkley/9781609182038)