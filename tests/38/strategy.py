from limits.limits import *
from hypothesis.strategies import text

s = text(max_size=MAX_SEQUENCE_LEN)

strategy = s

# This inherently has a roundabout property-based test
