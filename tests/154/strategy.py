from limits.limits import *
from hypothesis.strategies import text

a = text(alphabet='abc', max_size=SMALL_SEQUENCE_LEN)
b = text(alphabet='abc', max_size=SMALL_SEQUENCE_LEN)

strategy = a, b
