from limits.limits import MAX_INT, MIN_INT, MAX_FLOAT, MIN_FLOAT, MAX_SEQUENCE_LEN
from hypothesis.strategies import floats, lists

grades = lists(floats(min_value=0.0, max_value=4.0), max_size=MAX_SEQUENCE_LEN)

strategy = grades
