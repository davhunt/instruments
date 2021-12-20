from instruments.subscore import Subscore

import pandas as pd
import regex as re


class Survey:
    """Class that utilizes Subscore class to score all available subscores.
    By default if the subscores are empty, simply scores total score and returns.

    Instance Variables
    ----------
    name:   str | None
            String that contains the survey name.
    versions:   list | None
                List that contains survey versions if listed
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
    _extract_versions(self):
            Extracts survey versions if available.
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
    VER_POS = 1
    SES_POS = -3
    RUN_POS = -2
    EVENT_POS = -1

    DELIM = Subscore.DELIMITER

    def __init__(self, name, file_name, subscores):
        self.name = name
        self.file_name = file_name
        self.subscores = subscores

        # init and filter data
        self.data = self._load_data()
        self._filter()

        # init default versions and extract potential versions
        self.versions = []
        self._extract_versions()

    def _load_data(self):
        # load filename into dataframe
        file = pd.read_csv(self.file_name, index_col="record_id")
        return file
        
    def _filter(self):
        # keep only survey data containing survey name
        self.data = self.data.filter(regex=rf"^{self.name}")
        # quit processing if survey data is not available 
        if(self.data.empty):
            raise RuntimeError("Data does not contain %s survey data."%(self.name))

        # Drop rows with incomplete values in timestamp
        timestamp_col = self.data.filter(regex=rf"_{Subscore.TIME_LABEL}").columns
        self.data.dropna(subset=timestamp_col, inplace=True)
        if(self.data.empty):
            raise RuntimeError("Survey %s does not contain any values."%(self.name))
    
    def _extract_versions(self):
        # init regex
        surv_reg = rf"{self.name}"
        ver_reg = rf"{self.name}_[a-z]_"

        # get timestamp column of all versions
        timestamp_col = self.data.filter(regex=rf"_{Subscore.TIME_LABEL}").columns
        # extract potential versions using timestamp
        for ver in timestamp_col:
            surv_res = re.search(surv_reg, ver)
            ver_res = re.search(ver_reg, ver)
            if ver_res is not None:
                self.versions.append(ver_res.group(0)[:-1])
            elif surv_res is not None:
                self.versions.append(surv_res.group(0))

        # if survey versions extracted, assign to instance var
        if len(self.versions):
            self.versions = list(set(self.versions))
        
    def score(self):
        # Iterate through subscores and score on data
        all_scores = pd.DataFrame()
        for subscore, params in self.subscores.items():
            # Score each subscore w/passed params, consider each version as a seperate survey
            for ver_surv in self.versions:  
                sub_obj = Subscore(name=ver_surv, sub_name=subscore, **params)
                single_score = sub_obj.gen_data(self.data, all_scores)
                all_scores = pd.concat([all_scores, single_score], axis=1)

            # Sort according to session, run, and event, in that order
            all_scores = all_scores.reindex(
                sorted(all_scores.columns, key=lambda x: \
                    (int(x.split(self.DELIM)[self.SES_POS][1]),\
                    int(x.split(self.DELIM)[self.RUN_POS][1]),\
                    int(x.split(self.DELIM)[self.EVENT_POS][1]))\
            ), axis=1)
        
        # if multiple versions exist, sort according to version
        if len(self.versions) > 2:  
            all_scores = all_scores.reindex(sorted(all_scores.columns, key=lambda x: \
                (x.split(self.DELIM)[self.VER_POS][1])), axis=1)

        return all_scores

