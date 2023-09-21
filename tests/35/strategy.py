# Groundtruth is wrong because CONTRACT does not handle empty lists!

from hypothesis.strategies import lists, integers, floats, one_of

l = lists(one_of(integers(), floats()), max_size=50)

strategy = l
