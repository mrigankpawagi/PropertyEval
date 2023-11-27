from limits.limits import *
from hypothesis.strategies import text

string = text(alphabet='abcd ', max_size=MAX_INT)

strategy = string
