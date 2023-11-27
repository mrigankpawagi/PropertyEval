from limits.limits import *
# Ambiguous purpose statement
from hypothesis.strategies import text

brackets = text(alphabet="()", max_size=MAX_SEQUENCE_LEN)

strategy = brackets
