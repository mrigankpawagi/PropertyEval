from limits.limits import MAX_INT, MIN_INT, MAX_FLOAT, MIN_FLOAT, MAX_SEQUENCE_LEN
from hypothesis.strategies import text

s0 = text(alphabet='abcde', max_size=MAX_SEQUENCE_LEN)
s1 = text(alphabet='abcde', max_size=MAX_SEQUENCE_LEN)

strategy = s0, s1
