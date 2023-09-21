from hypothesis.strategies import lists, integers, floats, one_of

lst = lists(one_of(integers(), floats()), max_size=10, unique=True)

strategy = lst
