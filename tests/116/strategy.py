from hypothesis.strategies import lists, integers

arr = lists(integers(), max_size=10)

strategy = arr
