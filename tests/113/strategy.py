from hypothesis.strategies import lists, text

lst = lists(text(alphabet="0123456789", min_size=1, max_size=10), min_size=1, max_size=5)

strategy = lst
