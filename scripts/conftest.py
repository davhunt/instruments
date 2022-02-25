import pytest
import pandas as pd


@pytest.fixture
def id_col():
    ids =  [130079, 130080, 130081, 130082, 130083, 130084, 130085, 130086, 130087, 130088]
    return ids


@pytest.fixture
def test_data():
    data = "test_data/test_data.csv"
    return data


@pytest.fixture
def general_surv():
    general_surv = {
        "survey": {
            "sub1": {
                "questions": [1, 2, 3, 4],
                "score_type": "avg",
                "threshold": [0.01, 0.99],
                "rev_questions": [1, 2],
                "max": 5,
                "products": ["non-exist"], 
                "criteria": [1, 2]
            },
            "sub2": {
                "questions": [1, 2, 3, 4],
                "score_type": "avg",
                "threshold": [0.01, 0.99],
                "rev_questions": [1, 2],
                "max": 5,
                "criteria": [1, 2]
            },
            "sub3": {
                "questions": [1, 2, 3, 4],
                "score_type": "avg",
                "threshold": [0.01, 0.99],
                "rev_questions": [1, 2],
                "max": 5,
                "products": ["sub2"],
                "criteria": [1, 2]
            },
            "sub4": {
                "questions": [1, 2, 3, 4],
                "score_type": "avg",
                "threshold": [0.01, 0.99],
                "rev_questions": [1, 2],
                "products": ["sub2", "sub3"],
                "criteria": [1, 2]
            },
            "sub5": {
                "questions": [1, 2, 3, 4],
                "score_type": "avg",
                "threshold": 0.8,
                "rev_questions": [1, 2],
                "max": 5,
                "products": ["sub2", "sub3"],
                "criteria": [1, 2]
            },
            "sub6": {
                "questions": [1, 2, 3, 4],
                "score_type": "avg",
                "threshold": 0.8,
                "rev_questions": [1, 2],
                "products": ["sub2", "sub3"],
                "criteria": [1, 2]
            },
            "sub7": {
                "questions": [1, 2, 3, 4],
                "score_type": "round(sum(row) * 6 / 5)",
                "threshold": [0.01, 0.99],
                "rev_questions": [1, 2],
                "max": 5,
                "products": ["sub2", "sub3"],
                "criteria": [1, 2]
            },
            "sub8": {
                "questions": [1, 2, 3, 4],
                "score_type": "round(sum(row) * 6 / 5)",
                "threshold": [0.01, 0.99],
                "rev_questions": [1, 2],
                "products": ["sub2", "sub3"],
                "criteria": [1, 2]
            },
            "sub9": {
                "questions": [1, 2, 3, 4],
                "score_type": "round(sum(row) * 6 / 5)",
                "threshold": 0.8,
                "rev_questions": [1, 2],
                "max": 5,
                "products": ["sub2", "sub3"],
                "criteria": [1, 2]
            },
            "sub10": {
                "questions": [1, 2, 3, 4],
                "score_type": "round(sum(row) * 6 / 5)",
                "threshold": 0.8,
                "rev_questions": [1, 2],
                "products": ["sub2", "sub3"],
                "criteria": [1, 2]
            },
        }
    }
    return general_surv


@pytest.fixture
def empty_surv(test_data):
    empty_surv = {
        "survey": {
        }
    }
    return empty_surv, test_data


@pytest.fixture
def nonexist_surv(test_data):
    not_survey = {
        "not_survey": {
            "sub1": {
                "questions": [1, 2, 3, 4],
                "score_type": "avg",
                "threshold": [0.01, 0.99],
                "rev_questions": [1, 2],
                "max": 4,
                "products": ["non-exist"], 
                "criteria": [1, 2]
            },
        }
    }
    return not_survey, test_data


@pytest.fixture
def empty_params(test_data):
    empty_params = {
        "survey": {
            "sub_empty": {
            }
        }
    }
    return empty_params, test_data


@pytest.fixture
def general_survey_key(general_surv, id_col, test_data):
    # solutions for columns that should exist
    solutions = {
        "survey_scrdSub2_s1_r1_e1": 
                    ["N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A"],
        "survey_scrdSub2_s1_r2_e1":
                    ["N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A"],
        "survey_b_scrdSub2_s1_r2_e1": 
                    ["N/A", "N/A", "N/A", "N/A", "N/A", "N/A", 2, "N/A", "N/A", "N/A"],

        "survey_scrdSub3_s1_r1_e1": 
                        ["N/A", 2, "N/A", 2, "N/A", "N/A", 2, 2, "N/A", 2],
        "survey_scrdSub3_s1_r2_e1": 
                        ["N/A", 2, "N/A", 2, "N/A", "N/A", 2, 2, "N/A", 2],
        "survey_b_scrdSub3_s1_r2_e1": 
                        ["N/A", "N/A", "N/A", 2, "N/A", "N/A", 2, 2, "N/A", 2],
        
        "survey_scrdSub5_s1_r1_e1": 
                        ["N/A", 2, "N/A", 2, "N/A", "N/A", 2, 2, "N/A", 2],
        "survey_scrdSub5_s1_r2_e1": 
                        ["N/A", 2, "N/A", 2, "N/A", "N/A", 2, 2, "N/A", 2],
        "survey_b_scrdSub5_s1_r2_e1": 
                        ["N/A", "N/A", "N/A", 2, "N/A", "N/A", 2, 2, "N/A", 2],
        
        "survey_scrdSub7_s1_r1_e1": 
                        ["N/A", 5, "N/A", 5, "N/A", 0, 5, 7, "N/A", 10],
        "survey_scrdSub7_s1_r2_e1": 
                        ["N/A", 5, "N/A", 5, "N/A", 0, 5, 7, "N/A", 10],
        "survey_b_scrdSub7_s1_r2_e1": 
                        [0, 0, "N/A", 5, "N/A", 0, 7, 7, "N/A", 10],
        
        "survey_scrdSub9_s1_r1_e1": 
                        ["N/A", 5, "N/A", 5, "N/A", "N/A", 5, 7, "N/A", 10],
        "survey_scrdSub9_s1_r2_e1": 
                        ["N/A", 5, "N/A", 5, "N/A", "N/A", 5, 7, "N/A", 10],
        "survey_b_scrdSub9_s1_r2_e1": 
                        ["N/A", "N/A", "N/A", 5, "N/A", "N/A", 7, 7, "N/A", 10]
    }
    # columns that should not exist due to errors
    non_columns = ["survey_scrdSub1_s1_r1_e1", "survey_scrdSub1_s1_r2_e1", "survey_b_scrdSub1_s1_r1_e1",
                      "survey_scrdSub4_s1_r1_e1", "survey_scrdSub4_s1_r2_e1", "survey_b_scrdSub4_s1_r1_e1",
                      "survey_scrdSub6_s1_r1_e1", "survey_scrdSub6_s1_r2_e1", "survey_b_scrdSub6_s1_r1_e1"
                      "survey_scrdSub8_s1_r1_e1", "survey_scrdSub8_s1_r2_e1", "survey_b_scrdSub8_s1_r1_e1"
                      "survey_scrdSub10_s1_r1_e1", "survey_scrdSub10_s1_r2_e1", "survey_b_scrdSub10_s1_r1_e1"]
    solution_df = pd.DataFrame(data=solutions, index=id_col)
    return general_surv, test_data, solution_df, non_columns

