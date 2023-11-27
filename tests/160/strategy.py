from limits.limits import *
from hypothesis.strategies import lists, composite, sampled_from, integers, shared

@composite
def make(draw):
    n = draw(integers(min_value=1, max_value=MAX_SEQUENCE_LEN))
    operators = draw(lists(sampled_from(["+", "-", "*", "//", "**"]), min_size=n, max_size=n).filter(lambda x: x.count("**") <= 1))
    operands = draw(lists(integers(min_value=0, max_value=20), min_size=n+1, max_size=n+1).filter(lambda x: not any([x[i] == 0 and operators[i-1] == "//" for i in range(1, len(x))])))
    
    return operators, operands

st = make()
operators = shared(st, key='eval').map(lambda x: x[0])
operands = shared(st, key='eval').map(lambda x: x[1])

strategy = operators, operands
