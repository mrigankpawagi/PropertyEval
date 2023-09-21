from hypothesis.strategies import text, integers, composite, shared

@composite
def make(draw):
    n = draw(integers(min_value=1, max_value=10))
    a = draw(text(alphabet='01', min_size=n, max_size=n))
    b = draw(text(alphabet='01', min_size=n, max_size=n))
    return a, b

v = make()
a = shared(v, key='eval').map(lambda x: x[0])
b = shared(v, key='eval').map(lambda x: x[1])

strategy = a, b
