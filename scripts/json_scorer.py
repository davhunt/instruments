import pandas as pd
import json
from instruments.survey import Survey

"""
Code to load in JSON file and score outlined surveys.
Simply run and get output! 

Output will be labeled "data/outputs/<survey_name>_data.csv"
"""

# Open and save data to dataframe
with open('scripts/surveys.json','r') as infile:
    surveys = json.load(infile)

# Get input and output paths
read_data = surveys["input"]

# Load in file specified from json
file = pd.read_csv(read_data,index_col="record_id")
data = pd.DataFrame(file)

# Get all surveys
surveys_wsub = surveys["surveys"]

# Iterate through survey names and generate data
for name, subscores in surveys_wsub.items():
    survey_obj = Survey(name, data, subscores)
    handle = survey_obj.score_write("data/outputs/" + name + "test.csv")
