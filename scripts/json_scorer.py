import json
from survey import Survey
import pandas as pd

import sys


def json_score(name=None):
    """
    Code to load in JSON file and score outlined surveys.
    Simply run and get output! 

    Output will be labeled "data/outputs/<survey_name>_data.csv"
    """

    input = "data\inputs\input-to-test_2022-01-21.csv" # sys.argv[1] # "data\inputs\input-to-test_2021-12-10.csv"
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
    if name is not None:  
        all_surveys.to_csv(out_path + "/" + name)
    return all_surveys

if __name__ == "__main__":
    json_score(name="output.csv")