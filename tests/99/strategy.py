from limits.limits import *
# CONTRACT must check for inf and nan!

from hypothesis.strategies import builds, floats

value = builds(str, floats(allow_infinity=False, allow_nan=False, min_value=MIN_FLOAT, max_value=MAX_FLOAT))

strategy = value
