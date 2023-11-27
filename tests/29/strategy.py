from limits.limits import *
from hypothesis.strategies import lists, text

strings = lists(text(alphabet='ab', max_size=MAX_SEQUENCE_LEN), max_size=MAX_SEQUENCE_LEN)
prefix = text(alphabet='ab', max_size=MAX_SEQUENCE_LEN)

strategy = strings, prefix
