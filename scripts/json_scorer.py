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

# Get file name and survey data
file_name = surveys["input"]
surveys_wsub = surveys["surveys"]

# Iterate through survey names and generate data
for name, subscores in surveys_wsub.items():
    survey_obj = Survey(name, file_name, subscores)
    handle = survey_obj.score_write("data/outputs/" + name + ".csv")
