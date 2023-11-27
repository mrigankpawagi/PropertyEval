from limits.limits import *
from hypothesis.strategies import text

string = text(alphabet='a', max_size=MAX_INT)

strategy = string
