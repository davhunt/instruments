from scripts.instruments.subscore import Subscore

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
    subscores:  dict() | None
                Dictionary object containing all subscores and the parameters they go to.
                If no subscores have been specified, scores total sum automatically. 

                Ex: 
                {"subscore1": {
                        "select": [1, 2, 5],
                        "type": "sum"
                },
                "subscore2": {
                        "select": [3, 4, 6, 10, 14],
                        "type": "avg"
                }}
    
    Private Methods
    ----------
    _filter(self):
            Filter out non-survey data based on self.name, called in init. 

    Public Methods
    ----------
    score_write(self, filename):
            Function to iterate and score over all subscores, create dataframe,
            and write to filename.
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
        if self.subscores is None:
            # If no subscores, score total as default
            default = Subscore()
            scored_data = default.get_data(self.data)
            # Write out to filename and return
            scored_data.to_csv(filename)
            return 
        for sub in self.subscores:
            pass
