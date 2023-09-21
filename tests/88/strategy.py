from hypothesis.strategies import lists, integers

array = lists(integers(min_value=0))

strategy = array
