from limits.limits import *
from hypothesis.strategies import lists, integers

lst1 = lists(integers(), min_size=1, max_size=MAX_SEQUENCE_LEN)
lst2 = lists(integers(), min_size=1, max_size=MAX_SEQUENCE_LEN)

strategy = lst1, lst2
