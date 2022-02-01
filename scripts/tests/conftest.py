import pytest
import pandas as pd


@pytest.fixture
def conditional_data():
    cond_surv = {
        "aq10": {
            "sub1": {
                "questions": [1, 7, 8, 10],
                "criteria": [1, 2],
                "score_type": "count"
            }, 
            "sub2": {
                "questions": [2, 3, 4, 5, 6, 9],
                "criteria": [3, 4],
                "score_type": "count"
            },
            "total": {
                "questions": [],
                "products": ["sub1", "sub2"],
                "score_type": "sum"
            }
        }
    }
    cond_dat = "tests/test_data/cond_data.csv"
    return cond_surv, cond_dat

@pytest.fixture
def simple_data():
    simple_surv = {
        "adexi": {
            "sub1": {
                "questions": [1, 2, 5, 7, 8, 9, 11, 12, 13],
                "score_type": "sum"
            },
            "sub2": {
                "questions": [3, 4, 6, 10, 14], 
                "score_type": "sum"
            }
        }
    }
    simple_dat = "tests/test_data/simple_data.csv"
    return simple_surv, simple_dat

@pytest.fixture
def reverse_data():
    reverse_surv = {
        "ambi": {
            "sub1": {
                "questions": [9, 4, 6], 
                "rev_questions": [9, 4, 6],
                "max": 2,
                "score_type": "sum"
            },
            "sub2": {
                "questions": [12, 14, 15], 
                "rev_questions": [15],
                "max": 2,
                "score_type": "sum"
            },
            "total": {
                "questions": [],
                "products": ["sub1", "sub2"],
                "score_type": "sum"
            }
        }
    }
    reverse_dat = "tests/test_data/cond_data.csv"
    return reverse_surv, reverse_dat
