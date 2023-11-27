from limits.limits import *
from hypothesis.strategies import floats, lists

grades = lists(floats(min_value=0.0, max_value=4.0), max_size=MAX_SEQUENCE_LEN)

strategy = grades
