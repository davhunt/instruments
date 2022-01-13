import pandas as pd
import numpy as np
import re

from instruments.score_type import ScoreType


class Subscore:
    """Base subscore class that contains methods for scoring surveys according to parameters.
    If all params are empty, scores total sum as default. 

    Instance Variables
    ----------
    name:   str 
            String representing survey name.
    sub_name:   str
                String representing subscore name
    score_type: String
                String scoretype that represents a ScoreType value. "Sum" by default. 
    threshold:  float 
                Float that represents threshold to score row. 1.0 by default, which indicates all 
                questions must be answered.
    select: list() | None
            List containing questions to calculate. By default is None, which indicates all available questions.
    reverse_select: dict() | RevQuestion | None
                    List containing questions which are scored via reverse score. By default is None,
                    which indicates no reverse scored questions.

                    Ex: 
                    {
                        select: [1, 2, 3]
                        max_score: 5
                    }
    conditional:    dict() | ConditionScore | None
                    Dictionary object containing anticedent, answer, and consequent keys.
                    By default is none, which indicates no conditional questions. 

                    Ex: 
                    { 
                        "ante": [perc_complete]
                        "answer": [< 1.0]
                        "conseq": [other_subscore]
                     } -> 
                     "If question 1 is answered as 5, score questions 3 & 4"
    custom_score:   str | None
                    A string representing a custom scoring. None indicates that no custom score is used.

    Private Methods
    ----------
    _perc_column(self):
            Function to return string name of percentage complete columns.
    _scored_column(self):
            Function to return string name of scored columns.

    _remove_meta(self, data):
            Function to remove metadata columns timestamp & complete. Returns modified dataframe.

    _select_questions(self, data):
            Function to select subset of questions on passed data based on self.select.
            Returns modified dataframe. 
    _get_unique(self, row):
            Function to get unique sessions, rows, and events.
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

    get_data(self, data):
            Function to get score, percentage complete and append to dataframe. Modifies dataframe in place. 
    """
    TIME_LABEL = "timestamp"
    COMP_LABEL = "complete"

    def __init__(self, name, sub_name="total", score_type="sum", threshold=1.0, select=None,
                 reverse_select=None, conditional=None, custom_score=None):
        self.name = name
        self.sub_name = sub_name
        self.score_type = score_type
        self.threshold = threshold
        self.select = select
        self.reverse_select = reverse_select
        self.conditional = conditional
        self.custom_score = custom_score

    def _perc_column(self, label):
        return self.name + "_" + self.sub_name + "_" + label + "_perc_complete"

    def _scored_column(self, label):
        return self.name + "_" + self.sub_name + "_" + label + "_scored"

    def _remove_meta(self, data):
        # Create deep copy to prevent modification in place
        handle = data.copy()

        # Get column names that contain metadata labels
        metadata_col = handle.filter(
            regex=rf"_{self.TIME_LABEL}|_{self.COMP_LABEL}").columns
        # Drop the above column names
        handle = handle.drop(metadata_col, axis=1)

        return handle

    def _select_questions(self, data):
        # If there is no selection, return data with all questions
        # TODO: DRY!
        if self.select is None:
            return data.filter(items=list(data.filter(regex=rf"_i[0-9]+_").columns))

        select_columns = []
        for num in self.select:
            # For each selected question, find the corresponding column name
            select_columns += list(data.filter(regex=rf"_i{num}_").columns)
        # Filter out all data except for selected columns
        select_data = data.filter(items=select_columns)

        return select_data

    def _get_unique(self, data):
        # Get column names
        ind_names = list(data.columns)
        # Filter unique sessions, runs, and events
        unique_vals = set(
            [re.sub(rf"{self.name}_i[0-9]+_", "", ind) for ind in ind_names])
        return unique_vals

    def _score_type(self, row):
        # TODO: Implement conditional and reverse scoring
        # TODO: Remove these conditionals in favor for DRY principles
        if not (self.reverse_select is None):
            return
        if not (self.conditional is None):
            return
        if not (self.custom_score is None):
            self.custom_score = self.custom_score.replace("select", "row")
            return eval(self.custom_score)
        return row.mean() if ScoreType[self.score_type] == ScoreType.avg else row.sum()

    def perc_complete(self, row):
        # Get total questions: all questions if no selection, else length of selection
        total_quest = row.shape[0] if self.select is None else len(self.select)
        # Get total answered questions
        answered = row.count()

        perc_complete = (answered / total_quest)
        return perc_complete

    def score(self, data):
        # Filter out metadata
        surv_data = self._remove_meta(data)
        # Filter based on selected questions
        surv_data = self._select_questions(surv_data)

        # Create a column for each unique session, row, and event
        unique_vals = self._get_unique(surv_data)
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
                row_set = row_set.filter(regex=rf"_{unique}")

                # Calculate percentage complete of row and assign to column
                percentage = self.perc_complete(row_set)
                score.loc[index, self._perc_column(unique)] = percentage
                # Calculate score and assign to column if percentage complete is past threshold
                score.loc[index, self._scored_column(unique)] = self._score_type(
                    row_set) if percentage >= self.threshold else np.NaN

        return score

    def join_data(self, data):
        # Calculate score
        score_data = self.score(data)

        # Append to passed data and return
        return data.join(score_data)
