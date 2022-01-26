import json
from survey import Survey
from cond_scores import Ari
import pandas as pd

import sys

"""
Code to load in JSON file and score outlined surveys.
Simply run and get output! 

Output will be labeled "data/outputs/<survey_name>_data.csv"
"""

input = "data\inputs\input-ambirmbi_2022-01-21.csv" # sys.argv[1] # "data\inputs\input-to-test_2021-12-10.csv"
out_path = "data\outputs" # sys.argv[2] # "data\outputs"

# Open and save survey data
with open('scripts\surveys.json','r') as infile:
    surveys = json.load(infile)

# Iterate through survey names and generate data
all_surveys = pd.read_csv(input, index_col="record_id")
for name, subscores in surveys.items():
    # Try to score, continue if fails
    try:
        survey_obj = Survey(name, input, subscores)
        handle = survey_obj.score()
        all_surveys = pd.concat([all_surveys, handle], axis=1)
    except RuntimeError:
        continue
    
all_surveys.fillna(value="N/A", inplace=True)
all_surveys.to_csv(out_path + "/output.csv")

# Conditional scoring is a trickier beast and must be dealt with manually
subscores = {
    "raw": {
        "questions": [1, 2, 3, 4, 5, 6],
        "score_type": "sum"
    },
    "avg": {
        "questions": [1, 2, 3, 4, 5, 6],
        "score_type": "avg"
    },
    "prorat": {
        "questions": [1, 2, 3, 4, 5, 6],
        "score_type": "round(sum(row) * 6 / 5)",
        "threshold": 0.83
    }
}
ari_surveys = pd.read_csv("data\\inputs\\test_mult_ver.csv", index_col="record_id")
ari_obj = Ari("ari", "data\\inputs\\test_mult_ver.csv", subscores)

handle = ari_obj.score()
all_surveys = pd.concat([all_surveys, handle], axis=1)

all_surveys.to_csv(out_path + "/ari_output.csv")