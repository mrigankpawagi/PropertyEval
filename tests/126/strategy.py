from limits.limits import *
from hypothesis.strategies import lists, integers

lst = lists(integers(min_value=0), max_size=MAX_SEQUENCE_LEN)

strategy = lst
 
