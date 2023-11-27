from limits.limits import *
from hypothesis.strategies import text

s = text(alphabet="abcdefghij", max_size=MAX_SEQUENCE_LEN)
c = text(alphabet="abcdefghij", max_size=MAX_SEQUENCE_LEN)

strategy = s, c
