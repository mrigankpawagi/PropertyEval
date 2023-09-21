from hypothesis.strategies import text, lists

words = lists(text(alphabet='abc', max_size=10), min_size=1, max_size=20)

strategy = words
