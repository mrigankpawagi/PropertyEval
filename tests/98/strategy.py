from limits.limits import *
from hypothesis.strategies import text

s = text(alphabet="abcdeABCDE", max_size=MAX_SEQUENCE_LEN)

strategy = s
