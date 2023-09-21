from hypothesis.strategies import lists, integers

lst = lists(integers(), max_size=10)

strategy = lst
