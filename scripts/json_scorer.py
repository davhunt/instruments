import json
from instruments.survey import Survey
import pandas as pd

"""
Code to load in JSON file and score outlined surveys.
Simply run and get output! 

Output will be labeled "data/outputs/<survey_name>_data.csv"
"""

# Open and save data to dataframe
with open('scripts/surveys.json','r') as infile:
    surveys = json.load(infile)

# Get file name and survey data
file_name = surveys["input"]
out_path = surveys["output"]
surveys_wsub = surveys["surveys"]

# Iterate through survey names and generate data
all_surveys = pd.read_csv(file_name, index_col="record_id")
for name, subscores in surveys_wsub.items():
    survey_obj = Survey(name, file_name, subscores)
    handle = survey_obj.score()
    all_surveys = pd.concat([all_surveys, handle], axis=1)
all_surveys.fillna(value="N/A", inplace=True)
all_surveys.to_csv(out_path + "/output.csv")