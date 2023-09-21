from hypothesis.strategies import lists, integers

numbers = lists(integers())

strategy = numbers
