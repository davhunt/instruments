import pandas as pd
import numpy as np
import re

from score_type import ScoreType


class Subscore:
    """Base subscore class that contains methods for scoring surveys according to parameters.
    If all params are empty, scores total sum as default. 

    Instance Variables
    ----------
    name:   str 
            String representing survey name.
    sub_name:   str
                String representing subscore name
    score_type: String | custom_score()
                String scoretype that represents a ScoreType value. "Sum" by default.
    prev_data:  pd.DataFrame() | None
                Pandas dataframe containing previously generated data
    threshold:  float 
                Float that represents threshold to score row. 1.0 by default, which indicates all 
                questions must be answered.
    questions:  list()
                Which questions to select
    products:   list() | None
                List of products to score from "prev_data". "prev_data" must be included to score
    conditional:    condition_score() | None
                    TO BE IMPLEMENTED
                    Object containing anticedent, answer, and consequent keys.
                    By default is none, which indicates no conditional questions. 

                    Ex: 
                    { 
                        "ante": [perc_complete]
                        "answer": [< 1.0]
                        "conseq": [other_subscore]
                     } -> 
                     "If question 1 is answered as 5, score questions 3 & 4"
    criteria:   list() | None  
                list of valid answers. None if any answer is valid
    
    Private Methods
    ----------
    _perc_column(self):
            Function to return string name of percentage complete columns.
    _scored_column(self):
            Function to return string name of scored columns.

    _remove_meta(self, data):
            Function to remove metadata columns timestamp & complete. Returns modified dataframe.

    _select_questions(self, data):
            Function to select subset of questions on passed data based on self.select_questions.
            Returns modified dataframe. 
    _get_unique_sre(self, row):
            Function to get unique sessions, rows, and events, sorted in mentioned order.
            Returns list of labels.
    _reverse_score(self, data):
            To be implemented
    _score_conditional(self, data):
            To be implemented
    _score_type(self, row):
            Function to score row based on type, conditional, and reverse scoring.
            Scores mean if self.type is "avg". Scores sum otherwise. 

    Public Methods
    ----------
    perc_complete(self, row):
            Function to get percentage of complete questions for selected questions on passed row. 
            Returns float representing percentage.
    score(self, data):
            Function to get score and percenatage complete. Returns dataframe of indices and column of floats. 

    gen_data(self, data, prev_products=None):
            Function to get score, percentage complete as dataframe for subscore. Optionally 
            include previous subscores.
    """
    SCORED = "scrd"
    PERCENT = "perc"

    TIME_LABEL = "timestamp"
    COMP_LABEL = "complete"
    DELIM = "_"

    def __init__(self, name, sub_name="total", score_type="sum", threshold=1.0, questions=None,
                 products=None, conditional=None, criteria=None):
        self.name = name
        self.sub_name = sub_name
        self.score_type = score_type
        self.threshold = threshold
        self.questions = questions
        self.products = products
        self.conditional = conditional
        self.criteria = criteria
        
    def _perc_column(self, label):
        return self.name + self.DELIM + self.PERCENT + self.DELIM + \
            self.sub_name + self.DELIM + label

    def _scored_column(self, label):
        return self.name + self.DELIM + self.SCORED + self.DELIM \
             + self.sub_name + self.DELIM + label

    def _remove_meta(self, data):
        # Create deep copy to prevent modification in place
        handle = data.copy()

        # Get column names that contain metadata labels
        metadata_col = handle.filter(
            regex=rf"{self.DELIM}{self.TIME_LABEL}|{self.DELIM}{self.COMP_LABEL}").columns
        # Drop the above column names
        handle = handle.drop(metadata_col, axis=1)

        return handle

    def _select_questions(self, data):
        # If there is no selection, return data with all questions
        if self.questions is None:
            return data

        select_columns = []
        for num in self.questions:
            # For each selected question, find the corresponding column name
            select_columns += list(
                data.filter(regex=rf"{self.name}{self.DELIM}i{num}{self.DELIM}").columns
            )
        # Filter out all data except for selected columns
        select_data = data.filter(items=select_columns)

        return select_data
    
    def _select_products(self, data):
        # If there is no selection, return regular data
        if self.products is None:
            return data

        select_columns = []
        for name in self.products:
            # For each selected question, find the corresponding column name
            select_columns += list(
                data.filter(regex=rf"{self.SCORED}{self.DELIM}{name}").columns
            )
        # Filter out all data except for selected columns
        select_data = data.filter(items=select_columns)

        return select_data

    def _get_unique_sre(self, data):
        # init regex to get unique sessions, events, and runs
        sre_reg = rf"s[0-9]+_r[0-9]+_e[0-9]+"
        # Get column names
        ind_names = list(data.columns)
        # Filter unique sessions, runs, and events
        unique_vals = set([re.search(sre_reg, ind).group(0) for ind in ind_names])
        return unique_vals

    def _score_type(self, row):
        # filter series according to criteria, if applicable
        if self.criteria is not None:   
            row.where(row.isin(self.criteria), inplace=True)

        # Score according score_type
        if ScoreType[self.score_type] == ScoreType.avg:
            return row.mean()  
        elif ScoreType[self.score_type] == ScoreType.sum:
            return row.sum()
        elif ScoreType[self.score_type] == ScoreType.count:
            return row.count()

    def perc_complete(self, row):
        # Get total questions: all questions if no selection, else length of selection
        total_quest = row.shape[0] if self.questions is None else len(self.questions)
        # Get total answered questions
        answered = row.count()

        perc_complete = (answered / total_quest)
        return perc_complete

    def gen_data(self, data, prev_products=None):
        # Append previous products optionally
        if (prev_products is not None) and not (prev_products.empty):
            data = pd.concat([data, prev_products], axis=1)

        # Filter out metadata
        surv_data = self._remove_meta(data)
        # Filter based on selected questions
        surv_data = self._select_questions(surv_data)

        # select product columns if available
        if (prev_products is not None) and not (prev_products.empty):
            surv_data = self._select_products(surv_data)

        # Create a column for each unique session, row, and event
        unique_vals = self._get_unique_sre(surv_data)
        unique_cols = []
        for val in unique_vals:
            unique_cols.append(self._perc_column(val))
            unique_cols.append(self._scored_column(val))

        # Create a dataframe of percentage complete and scored column name
        score = pd.DataFrame(index=surv_data.index, columns=unique_cols)

        for index, row in surv_data.iterrows():
            # Calculate score for every unique group of metadata found
            for unique in unique_vals:
                # Create copy to prevent modification in place
                row_set = row.copy()
                # Filter row according to unique s_r_e
                row_set = row_set.filter(regex=rf"{unique}")

                # Calculate percentage complete of row and assign to column
                percentage = self.perc_complete(row_set)
                score.loc[index, self._perc_column(unique)] = percentage
                # Calculate score and assign to column if percentage complete is past threshold
                score.loc[index, self._scored_column(unique)] = self._score_type(
                    row_set) if percentage >= self.threshold else np.NaN

        return score
