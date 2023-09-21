from hypothesis.strategies import lists, integers, floats, one_of

numbers = lists(one_of(integers(), floats()), min_size=2).filter(lambda x: max(x) > min(x))

strategy = numbers
