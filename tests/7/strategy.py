from hypothesis.strategies import lists, text

strings = lists(text(alphabet='ab'), max_size=5)
substring = text(alphabet='ab')

strategy = strings, substring
