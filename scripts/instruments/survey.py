from instruments.subscore import Subscore

import pandas as pd


class Survey:
    """Class that utilizes Subscore class to score all available subscores.
    By default if the subscores are empty, simply scores total score and returns.

    Instance Variables
    ----------
    name:   str | None
            String that contains the survey name. If none, no file is written.
    file_name:  str
                Filename that contains csv survey data
    data:    pd.Dataframe
             Pandas dataframe that contains csv data. Created from private method _load_data()
    subscores:  dict() | list() | None
                Dictionary object containing all subscores and the parameters they go to.

                Ex: 
                {"subscore1": {
                        "select": [1, 2, 5],
                        "type": "sum"
                },
                "subscore2": {
                        "select": [3, 4, 6, 10, 14],
                        "type": "avg"
                }}

                Or list of subscore objects. Alternatively, None if no subscores available.
    
    Private Methods
    ----------
    _filter(self):
            Filter out non-survey data based on self.name, called in init.
    _load_data(self):
            Use self.file_name to init pandas dataframe and returns.

    Public Methods
    ----------
    score(self):
            Function to iterate and score over all subscores, and generate dataframe containing 
            all subscores. Returns modified dataframe. 
    score_write(self, filename):
            Function to call score() and write subsequent csv to filename.
            Modifies original data in place, and returns modified dataframe. 
    """
    SES_POS = 3
    RUN_POS = 4
    EVENT_POS = 5

    def __init__(self, name, file_name, subscores):
        self.name = name
        self.file_name = file_name
        self.subscores = subscores

        # Init and filter data
        self.data = self._load_data()
        self.data = self._filter(self.data.copy(), self.name)

    def _load_data(self):
        # load filename into dataframe
        file = pd.read_csv(self.file_name, index_col="record_id")
        return file
    
    def _filter(self, data, name):
        # keep only survey data containing survey name
        data = data.filter(regex=rf"{name}")

        # Drop columns with incomplete values in timestamp
        timestamp_col = data.filter(regex=rf"_{Subscore.TIME_LABEL}").columns
        data.dropna(subset=timestamp_col, inplace=True)
        return data

    def score(self):
        # Extract delimeter from subscore
        delim = Subscore.DELIMITER

        # If no subscores, return default total
        if not len(self.subscores):
            default = Subscore(name=self.name)
            scored_total_data = default.gen_data(self.data)
            return scored_total_data

        # Otherwise, iterate through subscores and score on data
        all_scores = pd.DataFrame()
        for subscore, params in self.subscores.items():
            sub_obj = Subscore(name=self.name, sub_name=subscore, **params)
            single_score = sub_obj.gen_data(self.data)
            all_scores = pd.concat([all_scores, single_score], axis=1)

        # Sort according to session, run, and event, in that order
        all_scores = all_scores.reindex(
            sorted(all_scores.columns, key=lambda x: \
                (int(x.split(delim)[self.SES_POS][1]),\
                int(x.split(delim)[self.RUN_POS][1]),\
                int(x.split(delim)[self.EVENT_POS][1]))\
        ), axis=1)

        return all_scores

