from limits.limits import *
from hypothesis.strategies import text

strings = text(alphabet='ab', max_size=MAX_SEQUENCE_LEN)

strategy = strings
