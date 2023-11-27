from limits.limits import *
from hypothesis.strategies import text

s0 = text(alphabet='abcde', max_size=MAX_SEQUENCE_LEN)
s1 = text(alphabet='abcde', max_size=MAX_SEQUENCE_LEN)

strategy = s0, s1
