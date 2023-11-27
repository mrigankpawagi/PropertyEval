from limits.limits import *
from hypothesis.strategies import text

s = text(alphabet='abcde', max_size=MAX_SEQUENCE_LEN).filter(lambda x: x == "" or x.islower())

strategy = s

# This inherently has a roundabout property-based test
