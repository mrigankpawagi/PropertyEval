from limits.limits import MAX_INT, MIN_INT, MAX_FLOAT, MIN_FLOAT, MAX_SEQUENCE_LEN
from hypothesis.strategies import lists, text

strings = lists(text(alphabet='ab', max_size=MAX_SEQUENCE_LEN), max_size=MAX_SEQUENCE_LEN)
prefix = text(alphabet='ab', max_size=MAX_SEQUENCE_LEN)

strategy = strings, prefix
