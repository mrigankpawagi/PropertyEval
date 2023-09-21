from hypothesis.strategies import one_of, integers, floats

a = one_of(integers(min_value=1, max_value=25), floats(min_value=0, exclude_min=True, max_value=25))
b = one_of(integers(min_value=1, max_value=25), floats(min_value=0, exclude_min=True, max_value=25))
c = one_of(integers(min_value=1, max_value=25), floats(min_value=0, exclude_min=True, max_value=25))

strategy = a, b, c
