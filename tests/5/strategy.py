from limits.limits import *
from hypothesis.strategies import integers, lists

numbers = lists(integers(), max_size=MAX_SEQUENCE_LEN)
delimiter = integers()

strategy = numbers, delimiter
