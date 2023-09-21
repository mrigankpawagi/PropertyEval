from hypothesis.strategies import lists, integers

lst1 = lists(integers(), min_size=1)
lst2 = lists(integers(), min_size=1)

strategy = lst1, lst2
