from limits.limits import *
from hypothesis.strategies import lists, integers

nums = lists(integers(), min_size=1, max_size=MAX_SEQUENCE_LEN)

strategy = nums
