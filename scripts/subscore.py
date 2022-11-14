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
    questions:  list() | none
                Which questions to select for scoring (includes forward and rev scored questions).
    sub_name:   str
                String representing subscore name
    score_type: String | custom_score()
                String scoretype that represents a ScoreType value. "Sum" by default.
    prev_data:  pd.DataFrame() | None
                Pandas dataframe containing previously generated data
    threshold:  float | list()
                Float that represents threshold to score row. 1.0 by default, which indicates all
                questions must be answered. Can be a list to represent a threshold range.
                Ex: [0.82, 1], Greater than 0.83, less than 1
    rev_questions:  list() | None
                    Which questions to select for reverse scoring.
    answers:    int | list()
            List of all possible answers. Must be included to guarantee correct
            reverse scoring.
    products:   list() | None
                List of products to score from "prev_data". "prev_data" must be included to score
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
            Function to score reverse score questions using rev_questions and answers params.
    _score_conditional(self, data):
            Function to score conditionally using conditional.
    _score_type(self, row):
            Function to score row based on type, conditional, and reverse scoring.
            Scores mean if self.type is "avg". Scores sum otherwise.
    _valid_thresh(self, perc):
            Function to check if percentage of row complete is valid using self.threshold

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

    def __init__(self, name, questions=None, sub_name="total", score_type="sum", threshold=1.0,
                 rev_questions=None, answers=None, products=None, conditional=None, criteria=None, hide=None):
        self.name = name
        self.sub_name = sub_name
        self.score_type = score_type
        self.threshold = threshold
        self.questions = questions
        self.rev_questions = rev_questions
        self.answers = answers
        self.products = products
        self.conditional = conditional
        self.criteria = criteria
        self.hide = hide

    def _perc_column(self, label):
        return self.name + self.DELIM + self.PERCENT + self.sub_name[0].capitalize() + self.sub_name[1:] \
            + self.DELIM + label

    def _scored_column(self, label):
        return self.name + self.DELIM + self.SCORED + self.sub_name[0].capitalize() + self.sub_name[1:] \
            + self.DELIM + label

    def _select_questions(self, data):
        # If there is no selection, return data with all questions
        if self.questions is None:
            return data
        # if list is empty return empty dataframe
        if self.questions == []:
            return pd.DataFrame()

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
        # If there is no selection, return empty dataframe
        if self.products is None:
            return pd.DataFrame()

        select_columns = []
        for name in self.products:
            prop_name = name[0].capitalize() + name[1:]
            # For each selected question, find the corresponding column name
            select_columns += list(
                data.filter(regex=rf"{self.SCORED}{prop_name}").columns
            )
        # Filter out all data except for selected columns
        select_data = data.filter(items=select_columns)

        # detect if products are empty, ie subscore doesn't exist or not generated yet
        if select_data.empty:
            raise RuntimeError("No products available for %s. Skipping."%(self.sub_name))

        return select_data

    def _reverse_score(self, data):
        # If there are no reverse questions specified, return data
        if self.rev_questions is None:
            return data
        if self.answers is None:
            raise RuntimeError("Answers param not included in %s. Cannot reliably reverse score."%(self.name))
            
        reversed_answers = self.answers.copy()
        reversed_answers.reverse()
        handle = data.copy()
        select_columns = []
        for num in self.rev_questions:
            # For each selected reverse question, find the corresponding column name
            select_columns += list(
                handle.filter(regex=rf"{self.name}{self.DELIM}i{num}{self.DELIM}").columns
            )
        # reverse each questions score according to max
        for rev_q in select_columns:
            handle[rev_q] = handle[rev_q].map(lambda s: reversed_answers[self.answers.index(s)] if not pd.isna(s) else s)

        return handle

    def _score_type(self, row):
        # filter series according to criteria, if applicable
        if self.criteria is not None:
            row.where(row.isin(self.criteria), inplace=True)

        # attempt to parse custom score
        if self.score_type not in ScoreType._member_names_:
            row = row.fillna(0)
            return eval(self.score_type)

        # Score according score_type
        if ScoreType[self.score_type] == ScoreType.avg:
            return row.mean()
        elif ScoreType[self.score_type] == ScoreType.sum:
            return row.sum()
        elif ScoreType[self.score_type] == ScoreType.diff:
            return row.diff()
        elif ScoreType[self.score_type] == ScoreType.count:
            return row.count()
        elif ScoreType[self.score_type] == ScoreType.med:
            return row.med()
        elif ScoreType[self.score_type] == ScoreType.min:
            return row.min()
        elif ScoreType[self.score_type] == ScoreType.max:
            return row.max()

    def _valid_thresh(self, perc):
        perc = Subscore.frac_to_perc(perc)
        if isinstance(self.threshold, (int, float)):
            return perc >= self.threshold
        if isinstance(self.threshold, list):
            return perc >= self.threshold[0] and perc <= self.threshold[1]
        return False

    def perc_complete(self, row):
        # Get total questions: all questions if no selection, else length of selection
        total_quest = row.shape[0]
        # Get total answered questions
        answered = row.count()

        perc_complete = rf"{answered}/{total_quest}"
        return perc_complete

    def perc_complete_for_products(self, row):
        num_sum = 0
        denom_sum = 0
        for index, value in row.items():
            numer_denom = value.split("/")
            num_sum += int(numer_denom[0])
            denom_sum += int(numer_denom[1])
        perc_complete = rf"{num_sum}/{denom_sum}"
        return perc_complete

    def perc_for_Q_and_P(self, percQ, percP):
        percQ_list = percQ.split("/")
        percP_list = percP.split("/")
        numer = int(percQ_list[0]) + int(percP_list[0])
        denom = int(percQ_list[1]) + int(percP_list[1])
        perc_complete = rf"{numer}/{denom}"
        return perc_complete

    def frac_to_perc(perc):
        numer_denom = perc.split("/")
        return int(numer_denom[0]) / int(numer_denom[1])

    def gen_data(self, ver_surv, sre, data):
        # Filter based on selected questions
        data = self._select_questions(data)
        data = self._reverse_score(data)
        unique_cols = []
        unique_cols.append(self._perc_column(sre))
        unique_cols.append(self._scored_column(sre))
        # Create a dataframe of percentage complete and scored column name
        score = pd.DataFrame(index=data.index, columns=unique_cols)

        for index, row in data.iterrows():
            # Create copy to prevent modification in place
            row_set = row.copy()
            # Calculate percentage complete of row and assign to column
            perc = self.perc_complete(row_set)
            score.loc[index, self._perc_column(sre)] = perc
            # Calculate score and assign column if percentage complete is past threshold
            score.loc[index, self._scored_column(sre)] = self._score_type(
                row_set) if self._valid_thresh(perc) else np.NaN
        return score

    def gen_data_for_products(self, ver_surv, sre, data, prev_products):
        # Filter data based on selected questions
        data = self._select_questions(data)
        data = self._reverse_score(data)
        # hot fix: default to 0 if None
        num_of_questions = 0 if self.questions is None else len(self.questions)
        combined_data = data

        # Filter prev_products based on contents of products
        for product in self.products:
            product = product[0].capitalize() + product[1:] + self.DELIM
            combined_data = pd.concat([combined_data, prev_products.filter(regex=rf"{product}")], axis=1)

        unique_cols = []
        unique_cols.append(self._perc_column(sre))
        unique_cols.append(self._scored_column(sre))
        # Create a dataframe of percentage complete and scored column name
        score = pd.DataFrame(index=combined_data.index, columns=unique_cols)

        for index, row in combined_data.iterrows():
            # Create copy to prevent modification in place
            row_set = row.copy()
            perc_row_set = row_set.filter(regex=rf"{self.PERCENT}")
            # Calculate percentage complete of row and assign to column
            perc = 0
            if num_of_questions != 0:
                perc_for_questions = self.perc_complete(row_set[:num_of_questions])
                perc_for_products = self.perc_complete_for_products(perc_row_set[num_of_questions:])
                perc = self.perc_for_Q_and_P(perc_for_questions, perc_for_products)
            else:
                perc = self.perc_complete_for_products(perc_row_set)

            score.loc[index, self._perc_column(sre)] = perc
            # Calculate score and assign column if percentage complete is past threshold
            score_row_set = row_set.drop(perc_row_set.keys())
            score.loc[index, self._scored_column(sre)] = self._score_type(
                score_row_set) if self._valid_thresh(perc) else np.NaN
        return score
