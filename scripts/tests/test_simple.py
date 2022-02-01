from matplotlib.cbook import simple_linear_interpolation
from json_scorer import json_score
import os


def test_simple_scoring(simple_data):
    # unpack simple_data
    surv_data, path = simple_data
    # generate data using json_scorer, an interface to call survey
    json_score()
