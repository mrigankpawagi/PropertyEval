from limits.limits import *
from hypothesis.strategies import text

_text = text(alphabet='ab ')

strategy = _text
