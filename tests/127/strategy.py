from limits.limits import *
from hypothesis.strategies import lists, integers

interval1 = lists(integers(min_value=0, max_value=MAX_INT), max_size=2, min_size=2).map(sorted)
interval2 = lists(integers(min_value=0, max_value=MAX_INT), max_size=2, min_size=2).map(sorted)

strategy = interval1, interval2
