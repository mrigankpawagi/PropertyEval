from hypothesis.strategies import lists, integers

arr = lists(integers(min_value=-50, max_value=50), max_size=10)

strategy = arr
