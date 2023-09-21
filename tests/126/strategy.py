from hypothesis.strategies import lists, integers

lst = lists(integers(min_value=0), max_size=10)

strategy = lst
 