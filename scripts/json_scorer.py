import json
from survey import Survey
import pandas as pd

import sys
import os
import re
import numpy as np


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
        rc_id = row.name # ID of child or respective parent in redcap
        project_id = str(rc_id)[0:2]
        # map parent data to child
        if (str(rc_id).startswith(project_id+'8') or str(rc_id).startswith(project_id+'9')) and len(str(rc_id)) == 7:
            id = int(project_id+'0' + str(rc_id)[3:])
        else:
            id = rc_id
        # check if id exists in tracker
        if id not in tracker_df.index:
            print(id, "missing in tracker file, skipping")
            continue
        for col in scrd_columns:
            col_re = re.match('^([a-zA-Z0-9\-].*)es(_[a-z])?(_scrd.*)$', col)
            if col_re:
                surv_version = "" if col_re.group(2) is None else col_re.group(2)
                tracker_col = col_re.group(1) + surv_version + col_re.group(3)
            else:
                tracker_col = col
            if tracker_col in list(tracker_df.columns):
                try:
                    if tracker_df.loc[id, tracker_col] == 1 or tracker_df.loc[id, tracker_col] == "1":
                        continue
                    else:
                        vals = output_data.loc[rc_id, col]
                        if not isinstance(vals, pd.Series):
                            tracker_df.loc[id, tracker_col] = "1" if vals != "NA" else "0"
                        else:
                            tracker_df.loc[id, tracker_col] = "1" if any(v != "NA" for v in list(vals)) else "0"
                except Exception as e_msg:
                    tracker_df.loc[id, tracker_col] = "0"

    data_tracker_filename = os.path.splitext(tracker)[0]
    tracker_df_no_blank_columns = tracker_df.loc[:, tracker_df.notnull().any(axis=0)]
    tracker_df_no_blank_columns = tracker_df_no_blank_columns.fillna("NA")
    tracker_df_no_blank_columns.to_csv(data_tracker_filename + "_viewable.csv")

    # leave NA as blank
    tracker_df = tracker_df.fillna('')
    tracker_df.to_csv(tracker)
    print("Success: data tracker updated.")


def json_score(input_path, survey_dat, datadict, output_path=None, tracker=None):
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
    all_surveys = pd.read_csv(input_path, index_col=id_col)
    datadict_df = pd.read_csv(datadict)
    scrd_columns = []
    for name, subscores in survey_dat.items():
        parent_col = False
        for _, row in datadict_df[datadict_df['dataType'] == 'redcap_data'].iterrows():
            multiple_reports_flag = False
            prov = row["provenance"].split(" ")
            if "file:" in prov and "variable:" in prov:
                idx = prov.index("file:")
                rc_filename = prov[idx+1].strip("\";,")
                idx = prov.index("variable:")
                rc_variable = prov[idx+1].strip("\";,")
                if rc_variable == "":
                    rc_variable = row["variable"]
                else:
                    multiple_reports_flag = True
                rc_variable_re = re.match('^([a-zA-Z0-9\-]+)(_[a-z])?$',rc_variable)
                # a tracker column like "masi_b_parent_scrdTotal_s1_r1_e1" should be updated by looking at "masi_b_scrdTotal_s1_r1_e1" and "masies_b_scrdTotal_s1_r1_e1" in the parent redcap
                spanish_surv = re.match('^([a-zA-Z0-9\-]+)es$', name)
                if spanish_surv:
                    eng_surv_name = spanish_surv.group(1)
                else:
                    eng_surv_name = name
                if rc_filename in os.path.basename(input_file).lower() and rc_variable_re and rc_variable_re.group(1) == eng_surv_name and multiple_reports_flag:
                    parent_col = True
                    parent_varname = row["variable"] # e.g. "masi_b_parent"
                    break
        # Try to score, continue if fails
        try:
            survey_obj = Survey(name, input_path, id_col, subscores)
            handle = survey_obj.score()
            if parent_col:
                remapping = dict()
                for i in list(handle.columns):
                    surv_reg = re.match('^([a-zA-Z0-9]+)(_[a-z])?(_[a-zA-Z0-9]+)(_s[0-9]+_r[0-9]+_e[0-9]+)', i)
                    # preprocessed column should be something like "{survey_name}_{version (optional)}_{scrd/percTotal}_s1_r1_e1"
                    if not surv_reg:
                        print("unexpected column name format in " + i + ", skipping.")
                        continue
                    surv_version = "" if surv_reg.group(2) is None else surv_reg.group(2)
                    remapping[i] = i.replace(surv_reg.group(1) + surv_version, parent_varname)
                handle = handle.rename(columns=remapping)
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
    id_col = sys.argv[4]
    datadict = sys.argv[5]
    if len(sys.argv) == 7:
        tracker = sys.argv[6]
    else:
        tracker = None
    json_score(input_file, json_data, datadict, out_path, tracker)
