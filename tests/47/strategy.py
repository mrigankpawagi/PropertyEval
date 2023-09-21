from hypothesis.strategies import lists, integers, floats, one_of

l = lists(one_of(integers(), floats()), min_size=1, max_size=15)

strategy = l
