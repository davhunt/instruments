from enum import Enum 


class ScoreType(Enum):
    """Enum representing set types of scoring for Subscore class. 
    """
    sum = "sum"
    diff = "diff"
    avg = "avg"
    med = "med"
    min = "min"
    max = "max"
    count = "count"
