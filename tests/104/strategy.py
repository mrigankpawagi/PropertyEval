from hypothesis.strategies import lists, integers

x = lists(integers(min_value=1))

strategy = x
