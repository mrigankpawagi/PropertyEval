import sys; sys.path.append("../.."); from groundtruth_fuzzer.limits import MAX_INT, MIN_INT, MAX_FLOAT, MIN_FLOAT, MAX_SEQUENCE_LEN
# Grount truth is incorrect! What about nan and inf?

from hypothesis.strategies import floats

number = floats(min_value=0.0, exclude_min=True, allow_nan=False, allow_infinity=False)

strategy = number
