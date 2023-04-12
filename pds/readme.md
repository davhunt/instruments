## PDS (Pubertal Development Scale)

### Versions
The current version used by NDCLab is a combination questionnaire, suitable for any biological sex. The NDCLab versions were extracted from the NIMH Data Archive in April 2023. See below for details of modifications made.
| Audience | Language |
| :--  | :--  |
| child self report | English |
| parent report | English; Spanish US/LatAM |

| Version | Base | Modifications |
| :--  | :--  | :--  |
| child self report | [ABCD Youth Survey](https://nda.nih.gov/data_structure.html?short_name=abcd_ypdms01) | capitalization of response options; handling of "I don't know" responses; modification of "brain imaging results" to "brain activity" in survey instructions; addition of question i0 and associated display logic; questions ordered according to the original paper; response options for question i2 matched to parent survey |
| parent report (English) | [ABCD Parent Survey](https://nda.nih.gov/data_structure.html?short_name=abcd_ppdms01) | capitalization of response options; handling of "I don't know" responses; addition of "on the original birth certificate" to question i0; addition of intersex options and associated display logic; questions ordered according to the original paper; addition of missing "hair" in response option #4 to question i8 |
| parent report (Spanish US/LatAm) | [ABCD Parent Survey](https://nda.nih.gov/data_structure.html?short_name=abcd_ppdms01) | capitalization of response options; handling of "I don't know" responses; addition of "on the original birth certificate" to question i0 (translation drawn from demo_d; addition of intersex options and associated display logic; translation of questions i5 and i6 (not available from ABCD survey) |


Previously, the PDS was split into separate versions for boys (pdsm) and for girls (pdsf). These versions are all deprecated:

##### pdsf_b
This version included the 6 questions from the original version, along with several additional questions drawn from Table 1 of the Cheng et al. (2021) paper (see below).
| Audience | Language |
| :--  | :--  |
| child self report | English |
| parent report | English; Spanish US/LatAM |

##### pdsf(_a)
This is the original female version used by the NDCLab, as provided by CAPP. It only included the English self report.

##### pdsm(_a)
The male report contained the original five questions, as provided by CAPP.
| Audience | Language |
| :--  | :--  |
| child self report | English |
| parent report | English; Spanish US/LatAM |


### Scoring Script
The PDS questionnaires are included in the repository scoring script. Threshold for scoring is 80%. Note that scores are not calculated for respondents who do not indicate either male or female sex (as only the three generic questions are shown to these respondents). See data dictionary for further details.


### Translations
The Spanish translations of the parent reports are based on translations available in the [NIMH Data Archive](https://nda.nih.gov/data_structure.html?short_name=abcd_ppdms01), consulted in January 2023. These were supplemented by additional translations performed by members of the NDCLab in 2023.  Included is a .csv file providing transparency on the translation process. Please report any issues with the PDS translation by posting an issue in this GitHub repository.


### References
Original paper and scoring:
> Carskadon, M. A., & Acebo, C. (1993). A self-administered rating scale for pubertal development. The Journal of Adolescent Health, 14(3), 190–195. [[link]](https://pubmed.ncbi.nlm.nih.gov/8323929/)

Expansion for pdsf_b was based on the questions in Table 1 of:
> Cheng, T. W., Magis-Weinberg, L., Guazzelli Williamson, V., Ladouceur, C. D., Whittle, S. L., Herting, M. M., Uban, K. A., Byrne, M. L., Barendse, M. E. A., Shirtcliff, E. A., & Pfeifer, J. H. (2021). A Researcher's Guide to the Measurement and Modeling of Puberty in the ABCD Study at Baseline. Frontiers in Endocrinology, 12, 608575. [[link]](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8131843/)