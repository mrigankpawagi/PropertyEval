from hypothesis.strategies import lists, integers, one_of, floats

q = lists(one_of(integers(), floats()))
w = one_of(integers(), floats())

strategy = q, w
