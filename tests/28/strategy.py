from limits.limits import MAX_INT, MIN_INT, MAX_FLOAT, MIN_FLOAT, MAX_SEQUENCE_LEN
from hypothesis.strategies import lists, text

numbers = lists(text(alphabet='abcd', max_size=MAX_SEQUENCE_LEN), max_size=MAX_SEQUENCE_LEN)

strategy = numbers
