from hypothesis.strategies import lists, integers, floats, one_of

l1 = lists(one_of(integers(), floats()))
l2 = lists(one_of(integers(), floats()))

strategy = l1, l2
