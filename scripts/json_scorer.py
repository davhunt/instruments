import pandas as pd
import json
from instruments import Survey

"""
Code to load in JSON file and score outlined surveys.
Simply run and get output! 

Output will be labeled "<survey_name>_data.csv"
"""

# Open and save data to dataframe
with open('scripts/surveys.json','r') as infile:
    surveys = json.load(infile)

# Get input and output paths
read_data = surveys["input"]

# Load in file specified from json
file = pd.read_csv(read_data,index_col="record_id")
dataframe = pd.DataFrame(file)

# Get all surveys
surveys_wsub = surveys["surveys"]

# Iterate through survey names and generate data
for name, subscores in surveys_wsub.items():
    print(name)
    print(subscores)
    # survey_obj = Survey(name, read_data, subscores)
    # survey_obj.score_write(name + "_data.csv")
