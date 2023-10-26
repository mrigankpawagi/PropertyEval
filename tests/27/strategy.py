from limits.limits import MAX_INT, MIN_INT, MAX_FLOAT, MIN_FLOAT, MAX_SEQUENCE_LEN
from hypothesis.strategies import text

string = text(alphabet="abcdABCD!01", max_size=MAX_SEQUENCE_LEN)

strategy = string
