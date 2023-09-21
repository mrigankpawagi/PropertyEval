from hypothesis.strategies import lists, floats

numbers = lists(floats(), min_size=1, max_size=5)

strategy = numbers
