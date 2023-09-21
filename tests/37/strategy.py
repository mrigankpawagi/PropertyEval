# Groundtruth is incorrect! Does not handle empty lists in CONSTRACT

from hypothesis.strategies import lists, integers, floats, one_of

l = lists(one_of(integers(), floats()))

strategy = l
