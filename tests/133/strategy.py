from hypothesis.strategies import integers, lists, floats, one_of

lst = lists(one_of(integers(min_value=-50, max_value=50), floats(min_value=-50, max_value=50)), max_size=10)

strategy = lst
