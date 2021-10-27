from script.instruments.survey import Subscore

import pandas as pd
import numpy as np

class Survey:
    """Class that utilizes Subscore class to score all available subscores
    one survey

    Instance Variables
    ----------
    name:   str
            String that contains the survey name
    data:   pandas.Dataframe()
            Dataframe that contains csv survey data
    subscores:  dict()
                Dictionary object containing all subscores
    
    Private Methods
    ----------
    _filter(self):
            Private method to filter out non-survey data, called in init. 

    Public Methods
    ----------
    score_write(self, filename):
            Function to score all subscores and write to filename.
    """
    def __init__(self, name, data, subscores=None):
        self.name = name
        self.data = data
        self.subscores = subscores

        # Once data is initialized, filter out irrelevant data
        self._filter(self.data, self.name)
    
    def _filter(self, data, name):
        # keep only the relevant survey data
        data = data.filter(regex=rf"{name}_")

        # Drop columns with incomplete values in timestamp
        timestamp_col = data.filter(regex=rf"_{Subscore.TIME_LABEL}").columns
        data.dropna(subset=timestamp_col, inplace=True)
        return data
    
    def score_write(self, filename):
        pass