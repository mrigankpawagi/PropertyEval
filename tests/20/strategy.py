from hypothesis.strategies import lists, floats, integers, one_of

numbers = lists(one_of(floats(), integers()), min_size=2)

strategy = numbers
