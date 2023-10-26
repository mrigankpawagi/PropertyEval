from limits.limits import MAX_INT, MIN_INT, MAX_FLOAT, MIN_FLOAT, MAX_SEQUENCE_LEN, SMALL_SEQUENCE_LEN
from hypothesis.strategies import lists, text

lst = lists(text(alphabet='()', max_size=SMALL_SEQUENCE_LEN), min_size=2, max_size=2)

strategy = lst
