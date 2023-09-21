from hypothesis.strategies import integers, lists

lst = lists(lists(integers(min_value=-20, max_value=20), max_size=10), max_size=10)
x = integers(min_value=-20, max_value=20)

strategy = lst, x
