from hypothesis.strategies import lists, integers

lst = lists(integers(min_value=1))

strategy = lst
