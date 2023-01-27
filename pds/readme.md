## PDS (Pubertal Development Scale)

There is a separate version of the PDS questionnaire for boys and for girls; display to participants must be controlled with conditional logic based upon an earlier question relating to biological sex (M/F).

### Versions
#### female
##### pdsf_b
This version includes the 6 questions from the original version, along with several additional questions drawn from Table 1 of the Cheng et al. (2021) paper (see below).
| Audience | Language |
| :--  | :--  |
| child self report | English |
| parent report | English; Spanish US/LatAM |

##### pdsf(_a)
This is the original version used by the NDCLab. It only included the English self report.

#### male
##### pdsm(_a)
The male report is on the initial release and contains only original five questions.
| Audience | Language |
| :--  | :--  |
| child self report | English |
| parent report | English; Spanish US/LatAM |


### Scoring Script
The PDS questionnaires are included in the repository scoring script. Threshold for scoring is 80%. See data dictionary for further details.


### Translations
The Spanish translations of the parent reports are based on translations available in the [NIMH Data Archive](https://nda.nih.gov/data_structure.html?short_name=abcd_ppdms01), consulted in January 2023. These were supplemented by additional translations performed by members of the NDCLab in 2023.  Included is a .csv file providing transparency on the translation process. Please report any issues with the PDS translation by posting an issue in this GitHub repository.


### References
Original paper and scoring:
> Carskadon, M. A., & Acebo, C. (1993). A self-administered rating scale for pubertal development. The Journal of Adolescent Health, 14(3), 190–195. [[link]](https://pubmed.ncbi.nlm.nih.gov/8323929/)

Expansion for pdsf_b was based on the questions in Table 1 of:
> Cheng, T. W., Magis-Weinberg, L., Guazzelli Williamson, V., Ladouceur, C. D., Whittle, S. L., Herting, M. M., Uban, K. A., Byrne, M. L., Barendse, M. E. A., Shirtcliff, E. A., & Pfeifer, J. H. (2021). A Researcher's Guide to the Measurement and Modeling of Puberty in the ABCD Study at Baseline. Frontiers in Endocrinology, 12, 608575. [[link]](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8131843/)