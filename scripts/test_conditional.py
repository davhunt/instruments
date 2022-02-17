import json_scorer as jscore
import os


def test_cond_scoring(conditional_data_single):
    # unpack conditional_data
    surv_data, input_path, solutions = conditional_data_single
    sol_cols = list(solutions.columns)
    # generate data using json_scorer, an interface to call survey
    output_data = jscore.json_score(input_path, surv_data)

    for index, row in output_data.iterrows():
        for name in sol_cols:
            assert row[name] == solutions.loc[index][name]


def test_cond_mult_scoring(conditional_data_multiple):
    # unpack simple_data
    surv_data, input_path, solutions = conditional_data_multiple
    sol_cols = list(solutions.columns)
    # generate data using json_scorer, an interface to call survey
    output_data = jscore.json_score(input_path, surv_data, "test_data/test.csv")

    for index, row in output_data.iterrows():
        for name in sol_cols:
            assert row[name] == solutions.loc[index][name]
