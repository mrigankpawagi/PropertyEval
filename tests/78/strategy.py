from limits.limits import *
from hypothesis.strategies import text

num = text(alphabet="0123456789ABCDEF", max_size=MAX_SEQUENCE_LEN)

strategy = num
