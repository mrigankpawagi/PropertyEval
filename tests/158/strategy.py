from limits.limits import *
from hypothesis.strategies import text, lists

words = lists(text(alphabet='abc', max_size=MAX_SEQUENCE_LEN), min_size=1, max_size=MAX_SEQUENCE_LEN)

strategy = words
