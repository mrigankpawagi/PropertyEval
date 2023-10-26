from limits.limits import MAX_INT, MIN_INT, MAX_FLOAT, MIN_FLOAT, MAX_SEQUENCE_LEN
from hypothesis.strategies import lists, text

lst = lists(text(alphabet="0123456789", min_size=1, max_size=MAX_SEQUENCE_LEN), min_size=1, max_size=MAX_SEQUENCE_LEN)

strategy = lst
