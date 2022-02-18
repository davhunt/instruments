import json_scorer as jscore
import os


def test_scoring(general_survey_key):
    # unpack answer key
    surv_data, input_path, solutions = general_survey_key
    sol_cols = list(solutions.columns)
    # generate data using json_scorer, an interface to call survey
    output_data = jscore.json_score(input_path, surv_data, "output_test.csv")

    for index, row in output_data.iterrows():
        for name in sol_cols:
            assert row[name] == solutions.loc[index][name]


def test_empty_survey(empty_surv):
    # unpack answer key
    surv_data, input_path = empty_surv
    # generate data using json_scorer, an interface to call survey
    output_data = jscore.json_score(input_path, surv_data)


def test_nonexist_survey(nonexist_surv):
    # unpack answer key
    surv_data, input_path = nonexist_surv
    # generate data using json_scorer, an interface to call survey
    output_data = jscore.json_score(input_path, surv_data)


def test_empty_params(empty_params):
    # unpack answer key
    surv_data, input_path, solutions = general_survey_key
    sol_cols = list(solutions.columns)
    # generate data using json_scorer, an interface to call survey
    output_data = jscore.json_score(input_path, surv_data)

    for index, row in output_data.iterrows():
        for name in sol_cols:
            assert row[name] == solutions.loc[index][name]
