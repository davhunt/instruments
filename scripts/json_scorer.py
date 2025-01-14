import json
from survey import Survey
import pandas as pd

import sys
import os


def score_tracker(output_data, scrd_columns, tracker):
    """
    Code to load in pandas dataframe of scored data and update tracker
    Parameters
    ----------
    output_data:    pd.df()
                    Dataframe containing scored surveys 
    scrd_columns:   list
                    list of columns to be check 
    tracker:    str 
                String pointing to tracker file. To be overwritten
    """
    tracker_df = pd.read_csv(tracker, index_col="id")

    for _, row in output_data.iterrows():
        id = row.name
        # check if id exists in tracker
        if id not in tracker_df.index:
            print(id, "missing in tracker file, skipping")
            continue
        for col in scrd_columns:
            if col in list(tracker_df.columns):
                try:
                    val = output_data.loc[id, col]
                    tracker_df.loc[id, col] = "1" if val != "NA" else "0"
                except Exception as e_msg:
                    tracker_df.loc[id, col] = 0

    # leave NA as blank
    tracker_df = tracker_df.fillna('')
    tracker_df.to_csv(tracker)
    print("Success: data tracker updated.")



def json_score(input_path, survey_dat, output_path=None, tracker=None):
    """
    Code to load in JSON file and score outlined surveys. Returns scored data joined with data.
    Writes to output_path if specified
    Parameters
    ----------
    input_path: str
                String pointing to input data
    survey_dat: str | dict
                Dictionary or path to json containing survey names and parameters
    output_path:    str | None
                    string pointing to output path. None if data should not be written out
    """
    # Open and save survey data
    if (isinstance(survey_dat, str)):
        with open(survey_dat,'r') as infile:
            survey_dat = json.load(infile)

    # Iterate through survey names and generate data
    all_surveys = pd.read_csv(input_path, index_col="record_id")
    scrd_columns = []
    for name, subscores in survey_dat.items():
        # Try to score, continue if fails
        try:
            survey_obj = Survey(name, input_path, subscores)
            handle = survey_obj.score()
            # collect all columns from handle that contains "scrd"
            scrd_columns += [col for col in list(handle.columns) if "scrd" in col]
            all_surveys = pd.concat([all_surveys, handle], axis=1)
        except RuntimeError:
            continue
    all_surveys.fillna(value="NA", inplace=True)

    if output_path is not None:  
        handle = os.path.basename(input_path)
        all_surveys.to_csv(os.path.join(output_path, handle.replace("DATA", "SCRD")))

    if tracker is not None:
        score_tracker(all_surveys, scrd_columns, tracker)

    return all_surveys
    
if __name__ == "__main__":
    input_file =  sys.argv[1]
    json_data = sys.argv[2]
    out_path = sys.argv[3]
    if len(sys.argv) == 5:
        tracker = sys.argv[4]
    else:
        tracker = None
    json_score(input_file, json_data, out_path, tracker)
