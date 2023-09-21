from hypothesis.strategies import lists, integers

arr = lists(integers(), unique=True)

strategy = arr
