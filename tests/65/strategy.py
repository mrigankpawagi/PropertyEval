from limits.limits import MAX_INT, MIN_INT, MAX_FLOAT, MIN_FLOAT, MAX_SEQUENCE_LEN, VERY_LARGE_INT
from hypothesis.strategies import integers

x = integers(min_value=0, max_value=VERY_LARGE_INT)
shift = integers(min_value=0, max_value=MAX_INT)

strategy = x, shift
