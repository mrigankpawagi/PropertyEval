from hypothesis.strategies import lists, text

lst1 = lists(text())
lst2 = lists(text())

strategy = lst1, lst2
