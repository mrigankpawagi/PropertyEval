from limits.limits import *
from hypothesis.strategies import text

string = text(alphabet='abcdefghij01', max_size=MAX_SEQUENCE_LEN).filter(lambda x: x == "" or x.islower())

strategy = string
