from limits.limits import MAX_INT, MIN_INT, MAX_FLOAT, MIN_FLOAT, MAX_SEQUENCE_LEN
# CONTRACT must check for inf and nan!

from hypothesis.strategies import builds, floats

value = builds(str, floats(allow_infinity=False, allow_nan=False, min_value=MIN_FLOAT, max_value=MAX_FLOAT))

strategy = value
