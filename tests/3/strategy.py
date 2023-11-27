from limits.limits import *
from hypothesis.strategies import integers, lists

operations = lists(integers(), max_size=MAX_SEQUENCE_LEN)

strategy = operations
