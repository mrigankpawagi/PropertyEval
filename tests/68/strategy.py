from limits.limits import *
from hypothesis.strategies import lists, integers

arr = lists(integers(min_value=0, max_value=MAX_INT), max_size=10000)

strategy = arr
