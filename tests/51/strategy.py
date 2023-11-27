from limits.limits import *
from hypothesis.strategies import text

_text = text(alphabet='abcABC', max_size=MAX_SEQUENCE_LEN)

strategy = _text
