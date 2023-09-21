from hypothesis.strategies import lists, integers, floats, one_of

xs = lists(one_of(integers(), floats()), min_size=1).filter(lambda x: len(x) % 2 == 0)

strategy = xs
