from enum import Enum 


class ScoreType(Enum):
    """Enum representing set types of scoring for Subscore class. 
    """
    sum = "sum"
    avg = "avg"
    med = "med"
    min = "min"
    max = "max"
    count = "count"
