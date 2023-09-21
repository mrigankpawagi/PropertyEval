from hypothesis.strategies import lists, integers, floats, one_of

lst = lists(one_of(integers(), floats()), max_size=15)

strategy = lst
