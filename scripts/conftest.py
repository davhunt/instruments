import pytest
import pandas as pd


@pytest.fixture
def id_col():
    ids =  [130079, 130080, 130081, 130082, 130083, 130084, 130085, 130086, 130087, 130088, 130089, 130090,
            130091, 130092, 130093, 130094, 130095, 130096, 130097, 130098, 130099, 130100, 130101, 130102, 130103,
            130104, 130105, 130106, 130107, 130108, 130109, 130110, 130111, 130112, 130113, 130114, 130115, 130116,
            130117, 130118]
    return ids


@pytest.fixture
def test_data():
    data = "test_data/test_data.csv"



@pytest.fixture
def general_surv():
    general_surv = {
        "survey": {
            "sub1": {
                "questions": [1, 2, 3, 4],
                "score_type": "avg",
                "threshold": [0.01, 0.99],
                "rev_questions": [1, 2],
                "max": 4,
                "products": ["non-exist"], 
                "criteria": [1, 2]
            },
            "sub2": {
                "questions": [1, 2, 3, 4],
                "score_type": "avg",
                "threshold": [0.01, 0.99],
                "rev_questions": [1, 2],
                "max": 4,
                "criteria": [1, 2]
            },
            "sub3": {
                "questions": [1, 2, 3, 4],
                "score_type": "avg",
                "threshold": [0.01, 0.99],
                "rev_questions": [1, 2],
                "max": 4,
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
                "max": 4,
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
                "max": 4,
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
                "max": 4,
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
    solutions = {
        "survey_scrdSub1_s1_r1_e1": 
                        ["N/A", 22, "N/A", 23, "N/A", 18, 11, 26, "N/A", 22, "N/A", 18, "N/A", "N/A", 26, "N/A",
                        "N/A", 26, "N/A", 26, "N/A", "N/A", 9, "N/A", "N/A", 17, "N/A", 33, "N/A", "N/A", 
                        "N/A", 23, 21, 23, "N/A", "N/A", 22, 27, 35, "N/A"],
        "survey_scrdSub1_s1_r2_e1": 
                        ["N/A", 22, "N/A", 23, "N/A", 18, 11, 26, "N/A", 22, "N/A", 18, "N/A", "N/A", 26, "N/A",
                        "N/A", 26, "N/A", 26, "N/A", "N/A", 9, "N/A", "N/A", 17, "N/A", 33, "N/A", "N/A", 
                        "N/A", 23, 21, 23, "N/A", "N/A", 22, 27, 35, "N/A"],
        "survey_scrdSub2_s1_r1_e1": 
                    ["N/A", 14, "N/A", 15, "N/A", 20, 10, 14, "N/A", 10, "N/A", 12, "N/A", "N/A", 20, "N/A", "N/A", 
                     17, "N/A", 16, "N/A", "N/A", 6, "N/A", "N/A", 11, "N/A", 14, "N/A", "N/A", "N/A", 19, 12,
                     9, "N/A", "N/A", 12, 15, 24, "N/A"],
        "survey_scrdSub2_s1_r2_e1": 
                    ["N/A", 14, "N/A", 15, "N/A", 20, 10, 14, "N/A", 10, "N/A", 12, "N/A", "N/A", 20, "N/A", "N/A", 
                     17, "N/A", 16, "N/A", "N/A", 6, "N/A", "N/A", 11, "N/A", 14, "N/A", "N/A", "N/A", 19, 12,
                     9, "N/A", "N/A", 12, 15, 24, "N/A"],
    }
    solution_df = pd.DataFrame(data=solutions, index=id_col)
    return general_surv, test_data, solution_df

