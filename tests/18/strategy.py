from limits.limits import MAX_INT, MIN_INT, MAX_FLOAT, MIN_FLOAT, MAX_SEQUENCE_LEN
from hypothesis.strategies import text

string = text(alphabet="abcd", max_size=MAX_SEQUENCE_LEN)
substring = text(alphabet="abcd", max_size=MAX_SEQUENCE_LEN).filter(lambda s: len(s) > 0)

strategy = string, substring
