from hypothesis.strategies import lists, text

lst = lists(text(alphabet='()', max_size=5), min_size=2, max_size=2)

strategy = lst
