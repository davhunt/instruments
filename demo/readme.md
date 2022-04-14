## DEMO (Demographics)

This repo contains modifiable (.docx) and PDF versions of demographics questionnaires used by the NDCLab, along with the REDCap import .zip and survey PDF.

### demo_c
This version reduces the number of questions in demo_b and separates one English language history question into two more granular questions.

**Modified variables:** ageen

**Deleted variables:** pronouns, otherpron, location, otherloc, student, major, employment, children, kidages, religion, sleep, exercise, diet, caffeine, chronic, conditions

**Added variables:** engflu

### demo_b
The following were added in this revision:
- language history
- familiarity with the lab's work
- history of communication disorders

**Modified variables:** hand (added Other option)

**Renamed variables:** orient (was 'orientation'), othethnic (was 'otherethnic'), socclass (was 'socialclass'), meds (was 'medications')

**Deleted variables:** dob

**Added variables:** mob, yob, otherhand, eng, langs, langhis, otherhis, ageen, profen, familiar, neuro, neurodis, comdiskid, comdisteen, comdisad, diagchil, diagchilnow, diagteen, diateennow, diagad, diagadnow


### demo(_a)
This is the original questionnaire used by the NDCLab.  It covers a broad range of details, including: age, handedness, pronouns, sex, gender identity, sexual identity, ethnic self-categorization, regional location, educational background, current academic status, current employment status, family, religion/spirituality, social class identification, household income, sleep habits, exercise habits, diet, caffeine consumption, use of medications, history of neurological disorders, history of head trauma, history of mental health disorders, history of chronic medical conditions.

### Scoring Script
The demographics questionnaire is **not** included in the repository scoring script.
