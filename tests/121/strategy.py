from hypothesis.strategies import lists, integers

lst = lists(integers(), min_size=1)

strategy = lst
