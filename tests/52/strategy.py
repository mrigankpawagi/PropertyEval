from hypothesis.strategies import lists, integers, floats, booleans, one_of

l = lists(one_of(integers(), floats(), booleans()))
t = integers()

strategy = l, t
