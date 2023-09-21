from hypothesis.strategies import lists, text

strings = lists(text())
prefix = text()

strategy = strings, prefix
