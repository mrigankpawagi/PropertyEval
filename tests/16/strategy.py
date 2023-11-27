from limits.limits import *
from hypothesis.strategies import text

string = text(alphabet="abcdeABCDE", max_size=MAX_SEQUENCE_LEN)

strategy = string
