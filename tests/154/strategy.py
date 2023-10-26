from limits.limits import MAX_INT, MIN_INT, MAX_FLOAT, MIN_FLOAT, MAX_SEQUENCE_LEN, SMALL_SEQUENCE_LEN
from hypothesis.strategies import text

a = text(alphabet='abc', max_size=SMALL_SEQUENCE_LEN)
b = text(alphabet='abc', max_size=SMALL_SEQUENCE_LEN)

strategy = a, b
