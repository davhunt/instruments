class Survey:
    """Base survey class that contain common methods for scoring surveys

    Instance Variables
    ----------
    data: pd.dataframe()
        Dataframe that contains survey
    name:   str()
            String that contains the survey name
    threshold:  float
                float 
    subscores:  dict() | None
                List of survey objects that represent subscores. Inherits data from original class.
                None if no subscores are available. 

                [ (data, "Sub1", [1, 3, 4], 1.0) ] ->
                Calculate subscore "Sub1" that select questions 1, 3, 4, 
                where 100% of scores must be answered
    range:  lst() | None
            List containing range to calculate. By default is None, indicates entire available range.
    
    Public Methods
    ----------
    filter(data, name)
            Function to filter out irrelevant survey data. Modifies data in place.
    perc_complete(self.data, self.range, self.subscores)
            Function to get percentage of complete questions for selected range and subscores. 
            Returns dict() object.
    score(self.data, self.range, self.threshold):
            General scoring function. 
    score_total(self.data, self.threshold)
            Function to get total score. Returns int representing total score.
    score_subscores(self.data, self.subscores):
            Function to score all available subcores. Returns dict() object where each key is 
            a subscore name and each value is the subscore.
    get_data()
            Returns dataframe of all total scores and subscores.
    """
    def __init__(self, data, name, threshold, subscores, range=None):
        self.data = data
        self.name = name
        self.range = range
        self.threshold = threshold
        self.subscores = subscores

        # After init is complete, filter out irrelevant data
        self.filter()
        
    def filter(self):
        self.data = self.data.filter(regex=rf"(record_id|{self.name}_)")
    
    def perc_complete(self):



    