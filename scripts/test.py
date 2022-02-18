import json_scorer as jscore
import pytest

def test_scoring(general_survey_key):
    # unpack answer key
    surv_data, input_path, solutions, non_solutions = general_survey_key
    sol_cols = list(solutions.columns)
    # generate data using json_scorer, an interface to call survey
    output_data = jscore.json_score(input_path, surv_data, "output_test.csv")

    # assert error columns not included
    for col in non_solutions:
        assert col not in list(solutions.columns)

    # assert data matches solution
    for index, row in output_data.iterrows():
        for name in sol_cols:
            assert row[name] == solutions.loc[index][name]


def test_empty_survey(empty_surv):
    # unpack answer key
    surv_data, input_path = empty_surv
    # attempt to score with invalid survey, should error out
    with pytest.raises(TypeError):
        _ = jscore.json_score(input_path, surv_data)


def test_nonexist_survey(nonexist_surv):
    # unpack answer key
    surv_data, input_path = nonexist_surv
    # attempt to score with non-existent survey, should not error out!
    _ = jscore.json_score(input_path, surv_data)
    assert True


def test_empty_params(empty_params):
    # unpack answer key
    surv_data, input_path = empty_params
    # attempt to score with invalid subscore, should error out
    with pytest.raises(TypeError):
        _ = jscore.json_score(input_path, surv_data)
