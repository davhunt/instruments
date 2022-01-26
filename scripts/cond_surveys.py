import pandas as pd

from subscore import Subscore
from survey import Survey
import re

class Ari(Survey):

    def _get_unique_sre(self, data):
        # init regex to get unique sessions, events, and runs
        sre_reg = rf"s[0-9]+_r[0-9]+_e[0-9]+"
        # Get column names
        ind_names = list(data.columns)
        # Filter unique sessions, runs, and events
        unique_vals = set([re.search(sre_reg, ind).group(0) for ind in ind_names])
        return unique_vals

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

        unique_vals = self._get_unique_sre(all_scores)

        for index, row in all_scores.iterrows():
            for ver_surv in self.versions:  
                for unique in unique_vals:
                    if row[ver_surv+"_percProrat_"+unique] < 1 and row[ver_surv+"_percProrat_"+unique] >= 0.83:
                        all_scores.loc[index, ver_surv+"_scrdRaw_"+unique] = None
                        all_scores.loc[index, ver_surv+"_scrdAvg_"+unique] = None
                    else:
                        all_scores.loc[index, ver_surv+"_scrdProrat_"+unique] = None

        return all_scores
