from limits.limits import MAX_INT, MIN_INT, MAX_FLOAT, MIN_FLOAT, MAX_SEQUENCE_LEN
from hypothesis.strategies import integers

n = integers(min_value=0, max_value=MAX_INT)
p = integers(min_value=1, max_value=MAX_INT)

strategy = n, p
