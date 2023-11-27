from limits.limits import *
from hypothesis.strategies import text

s = text(alphabet="abcdeyABCDEY", max_size=MAX_SEQUENCE_LEN)

strategy = s
