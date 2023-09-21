from hypothesis.strategies import lists, one_of, integers, floats

xs = lists(one_of(integers(), floats()), min_size=1)

strategy = xs
