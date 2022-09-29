## THQ (Trauma History Questionnaire)

This repo contains the THQ questionnaire.  Given the sensitive nature of these questions, special care must be taken in its administration and the NDCLab uses additional information in the survey header to point study participants to mental health resources in the event that they become distressed when reflecting upon their past traumatic experiences.

### Versions
##### thq_b
This version of the questionnaire drops all "Number of times/Repeated?" and "Please specify" sub-questions. As such, only the main question and the "Approximate age(s)" sub-question remain for each item.  All age-related questions were simplified to "Approximate age(s)" (removing "and frequency" from questions in the Physical and Sexual Experiences section). To simplify the output file, the variable for the age question was renamed to "iX_age." Only the English self report is available.

##### thq(_a)
This is the original, complete questionnaire. Only the English self report is available.


### Scoring Script
The THQ questionnaire is **not** included in the repository scoring script.


### References
> Hooper, L. M., Stockton, P., Krupnick, J. L., & Green, B. L. (2011). Development, use, and psychometric properties of the Trauma History Questionnaire. Journal of Loss and Trauma, 16(3), 258–283. [[link]](https://psycnet.apa.org/record/2011-10871-005)