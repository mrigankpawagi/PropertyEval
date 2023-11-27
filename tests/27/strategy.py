from limits.limits import *
from hypothesis.strategies import text

string = text(alphabet="abcdABCD!01", max_size=MAX_SEQUENCE_LEN)

strategy = string
