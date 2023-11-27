from limits.limits import *
from hypothesis.strategies import text

_text = text(alphabet="ab", max_size=MAX_SEQUENCE_LEN)

strategy = _text
