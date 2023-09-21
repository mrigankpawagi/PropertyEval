from hypothesis.strategies import lists, composite, sampled_from, integers, shared

@composite
def make(draw):
    n = draw(integers(min_value=1, max_value=10))
    operators = draw(lists(sampled_from(["+", "-", "*", "//", "**"]), min_size=n, max_size=n))
    operands = draw(lists(integers(min_value=0, max_value=20), min_size=n+1, max_size=n+1))
    
    return operators, operands

st = make()
operators = shared(st, key='eval').map(lambda x: x[0])
operands = shared(st, key='eval').map(lambda x: x[1])

strategy = operators, operands
