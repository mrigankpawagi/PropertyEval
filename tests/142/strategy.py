from hypothesis.strategies import lists, integers

lst = lists(integers(min_value=-50, max_value=50), max_size=15)

strategy = lst
