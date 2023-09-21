from hypothesis.strategies import integers, floats, one_of

a = one_of(integers(min_value=1), floats(min_value=1, exclude_min=True))
h = one_of(integers(min_value=1), floats(min_value=1, exclude_min=True))

strategy = a, h
