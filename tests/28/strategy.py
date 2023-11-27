from limits.limits import *
from hypothesis.strategies import lists, text

numbers = lists(text(alphabet='abcd', max_size=MAX_SEQUENCE_LEN), max_size=MAX_SEQUENCE_LEN)

strategy = numbers
