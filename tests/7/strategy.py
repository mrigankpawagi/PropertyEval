from limits.limits import *
from hypothesis.strategies import lists, text

strings = lists(text(alphabet='ab'), max_size=MAX_SEQUENCE_LEN)
substring = text(alphabet='ab')

strategy = strings, substring
