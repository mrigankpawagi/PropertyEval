from limits.limits import MAX_INT, MIN_INT, MAX_FLOAT, MIN_FLOAT, MAX_SEQUENCE_LEN
# Ambiguous purpose statement
from hypothesis.strategies import text

brackets = text(alphabet="()", max_size=MAX_SEQUENCE_LEN)

strategy = brackets
