from limits.limits import *
from hypothesis.strategies import one_of, integers, floats

a = one_of(integers(min_value=1, max_value=MAX_INT), floats(min_value=0, exclude_min=True, max_value=MAX_FLOAT))
b = one_of(integers(min_value=1, max_value=MAX_INT), floats(min_value=0, exclude_min=True, max_value=MAX_FLOAT))
c = one_of(integers(min_value=1, max_value=MAX_INT), floats(min_value=0, exclude_min=True, max_value=MAX_FLOAT))

strategy = a, b, c
