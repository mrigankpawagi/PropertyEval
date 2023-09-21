from hypothesis.strategies import lists, text

numbers = lists(text())

strategy = numbers
