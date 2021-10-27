import pandas as pd
import scripts.instruments.ScoreType as ScoreType

class Subscore:
    """Base survey tools class that contain methods for scoring surveys.

    Instance Variables
    ----------
    name:   str
            String representing subscore name.
    type:   "sum" | "avg"
            String that represents calculation type
    threshold:  float | None 
                Float that represents threshold to score row. None by default, which indicates no threshold 
                required.
    select: list() | None
            List containing questions to calculate. By default is None, which indicates all available questions.
    reverse_select: list() | None
                    List containing questions which are scored via reverse score. By default is None,
                    which indicates no reverse scored questions.
    conditional:    dict() | None
                    Dictionary object containing keys as prompts and values as selected questions.
                    By default is none, which indicates no conditional questions. 

                    Ex: { 1: [3, 4] } -> If question 1 is answered in the positive, score questions 3 & 4

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
            Returns float.
    score(self, data):
            Function to get score and percenatage complete. Returns dataframe of indices and column of floats. 

    get_data(self, data):
            Function to get score, percentage complete and append to dataframe. Modifies dataframe in place. 
    """
    TIME_LABEL = "timestamp"
    COMP_LABEL = "complete"

    def __init__(self, name, type, threshold=None, select=None, reverse_select=None, conditional=None):
        self.name = name
        self.type = type
        self.threshold = threshold
        self.select = select
        self.reverse_select = reverse_select
        self.conditional=conditional
    
    def _perc_column(self):
        return "perc_" + self.name + "_complete"
    
    def _scored_column(self):
        return self.name + "_scored"
        
    def _remove_meta(self, data):
        # Create deep copy to prevent modification in place
        handle = data.copy()

        # Get column names that contain metadata labels
        metadata_col = handle.filter(regex=rf"_{self.TIME_LABEL}|_{self.COMP_LABEL}").columns
        # Drop the above column names
        handle = handle.drop(metadata_col, axis=1)

        return handle
    
    def _select_questions(self, data):
        # If there is no selection, return unmodified series
        if self.select is None:
            return data
        select_column = set()
        for num in self.select: 
            # For each selected question, find the corresponding column name
            select_column.add(data.filter(regex=rf"_i{num}_").columns)
        select_data = data.filter(items=list(select_column))

        return select_data 
    
    def _score_type(self, row):
        # TODO: Implement conditional and reverse scoring
        if not (self.reverse_select is None):
            return
        if not (self.conditional is None):
            return
        return row.mean() if self.type == ScoreType.avg.value else row.sum()
    
    def perc_complete(self, row):
        # Get total questions: all questions if no selection, else length of selection
        total_quest = row.shape[0] if self.select is None else len(self.select)
        # Get total answered questions 
        answered = row.count()
        # Calculate percentage and assign to index in new dataframe
        perc_complete = (answered / total_quest) * 100

        return perc_complete

    def score(self, data):
        # Filter out metadata
        surv_data = self._remove_meta(data)
        # Filter based on selected questions
        surv_data = self._select_questions(surv_data)

        # Create a dataframe of percentage complete for each index
        score = pd.DataFrame(index=surv_data.index, columns=[self._perc_column, self._scored_column])

        for index, row in surv_data.iterrows():
            # Calculate percentage complete of row and assign to colu,n
            percentage = self.perc_complete(row)
            score[index][self._perc_column] = percentage
            # Calculate score and assign to column if percentage complete is past threshold
            score[index][self._scored_column] = self._score_type(row) if percentage >= self.threshold else -1

        return score
    
    def get_data(self, data):
        # Calculate score
        score_data = self.score(data)

        # Append to passed data and return
        return data.join(score_data)
