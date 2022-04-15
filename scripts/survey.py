from subscore import Subscore

import pandas as pd
import regex as re


class Survey:
    """Class that utilizes Subscore class to score all available subscores.

    Instance Variables
    ----------
    name:   str | None
            String that contains the survey name.
    versions:   list | None
                List that contains survey versions if listed. Initialized in _extract_versions(). 
    file_name:  str
                Filename that contains csv survey data.
    data:    pd.Dataframe
             Pandas dataframe that contains csv data. Created from private method _load_data().
    subscores:  dict() | None
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

                Alternatively, None if no subscores available.
    
    Private Methods
    ----------
    _filter(self):
            Firstly checks if subscores exist. Filter out non-survey data based on self.name, 
            called in init.
    _extract_versions(self):
            Extracts survey versions if available, called in init.
    _load_data(self):
            Use self.file_name to init pandas dataframe and returns.

    Public Methods
    ----------
    score(self):
            Function to iterate and score over all subscores, and generate dataframe containing 
            all subscores. Returns modified dataframe. 
    """
    DELIM = Subscore.DELIM

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
        if len(self.subscores) == 0:
            raise TypeError("Subscores for %s is empty. Skipping."%(self.name))
        # keep only survey data containing survey name
        self.data = self.data.filter(regex=rf"^{self.name}")
        # quit processing if survey data is not available 
        if(self.data.empty):
            raise RuntimeError("Data does not contain %s survey data. Skipping."%(self.name))

        # Drop rows with incomplete values in timestamp (indicating no data)
        timestamp_col = self.data.filter(regex=rf"_{Subscore.TIME_LABEL}").columns
        self.data.dropna(subset=timestamp_col, how='all', inplace=True)
        if(self.data.empty):
            raise RuntimeError("Survey %s does not contain any values. Skipping."%(self.name))
    
    def _extract_versions(self):
        # init regex
        surv_reg = rf"{self.name}"
        ver_reg = rf"{self.name}_[a-z]*_"

        # get timestamp column of all versions
        timestamp_col = self.data.filter(regex=rf"_{Subscore.TIME_LABEL}").columns
        # extract potential versions using timestamp
        for ver in timestamp_col:
            surv_res = re.search(surv_reg, ver)
            ver_res = re.search(ver_reg, ver)
            if ver_res is not None:
                if ver_res.group(0)[:-1] not in self.versions:
                    self.versions.append(ver_res.group(0)[:-1])
            elif surv_res is not None:
                if surv_res.group(0) not in self.versions:
                    self.versions.append(surv_res.group(0))
        self.versions.sort()
        
                    
    def _remove_meta(self, data):
        metadata_col = data.filter(regex=rf"{self.DELIM}{Subscore.TIME_LABEL}|{self.DELIM}{Subscore.COMP_LABEL}").columns
        return data.drop(metadata_col, axis=1)

    def _extract_sre_list(self, data):
        # init regex
        sre_reg = rf"s[0-9]+_r[0-9]+_e[0-9]+"
        # get timestamp columns of the version feautured in data
        timestamp_col = data.filter(regex=rf"_{Subscore.TIME_LABEL}").columns
        # init list of extracted unique sre that will be returned
        sre_list = []
        # extract unsorted sre_list using timestamp columns
        for col in timestamp_col:
            sre_res = re.search(sre_reg, col)
            if sre_res is not None:
                if sre_res.group(0) not in sre_list:
                    sre_list.append(sre_res.group(0))
        
        # sort the sre_list
        # keep in mind that when sorting by session, run, and event there is some priority associated to each
        # priority in descending order: s, r, e
        s_reg = rf"s[0-9]+"
        r_reg = rf"r[0-9]+"
        e_reg = rf"e[0-9]+"
        sre_dict_list = []
        for sre in sre_list:
            sre_dict = {
                "sre": sre,
                "s" : int(re.search(s_reg, sre).group(0)[1:]),
                "r" : int(re.search(r_reg, sre).group(0)[1:]),
                "e" : int(re.search(e_reg, sre).group(0)[1:])
            }
            sre_dict_list.append(sre_dict)
        sre_dict_list.sort(key=lambda x: x["e"])
        sre_dict_list.sort(key=lambda x: x["r"])
        sre_dict_list.sort(key=lambda x: x["s"])
        sre_list = []
        for sre_dict in sre_dict_list:
            sre_list.append(sre_dict["sre"])
        return sre_list

    def score(self):
        # Iterate through versions then sre then score on data
        all_scores = pd.DataFrame()
        for ver_surv in self.versions:
            # starting off with an empty dataframe for each version (so that future versions can't refer to past versions)
            ver_scores = pd.DataFrame()
            # filter data to only include columns pertaining to the current version
            ver_surv_data = self.data.filter(regex=rf"{ver_surv}_[a-z][0-9]")
            # extract each unique sre from filtered data into a list so that we can loop through each
            # the unique sre list extracted is sorted
            sre_list = self._extract_sre_list(ver_surv_data)
            # remove metadata
            ver_surv_data = self._remove_meta(ver_surv_data)
            for sre in sre_list:
                for subscore, params in self.subscores.items():
                    if len(params) == 0:
                        raise TypeError("No paramaters for %s. Skipping."%(subscore))
                    try:
                        sub_obj = Subscore(name=ver_surv, sub_name=subscore, **params)
                        if sub_obj.products == None:
                            single_score = sub_obj.gen_data(ver_surv, sre, ver_surv_data.filter(regex=rf"{sre}$"))
                            ver_scores = pd.concat([ver_scores, single_score], axis=1)
                        else:
                            single_score = sub_obj.gen_data_for_products(ver_surv, sre, ver_surv_data.filter(regex=rf"{sre}$"), ver_scores)
                            if sub_obj.hide != None:
                                if sub_obj.hide == True:
                                    for product in sub_obj.products:
                                        product = product[0].capitalize() +product[1:]
                                        product_col = ver_scores.filter(regex=rf"{product}").columns
                                        ver_scores = ver_scores.drop(product_col, axis=1)
                            ver_scores = pd.concat([ver_scores, single_score], axis=1)
                    except RuntimeError:
                        continue
            all_scores = pd.concat([all_scores, ver_scores], axis=1)
        perc_cols = all_scores.filter(regex=rf"{Subscore.PERCENT}").columns
        for perc_col in perc_cols:
            all_scores[perc_col] = all_scores[perc_col].apply(lambda x: Subscore.frac_to_perc(x))
        return all_scores
