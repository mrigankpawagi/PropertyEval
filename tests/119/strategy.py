from limits.limits import *
from hypothesis.strategies import lists, text

lst = lists(text(alphabet='()', max_size=SMALL_SEQUENCE_LEN), min_size=2, max_size=2)

strategy = lst
