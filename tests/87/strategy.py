from limits.limits import *
from hypothesis.strategies import integers, lists

lst = lists(lists(integers(min_value=MIN_INT, max_value=MAX_INT), max_size=MAX_SEQUENCE_LEN), max_size=MAX_SEQUENCE_LEN)
x = integers(min_value=MIN_INT, max_value=MAX_INT)

strategy = lst, x
