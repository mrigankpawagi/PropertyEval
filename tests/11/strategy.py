from limits.limits import MAX_INT, MIN_INT, MAX_FLOAT, MIN_FLOAT, MAX_SEQUENCE_LEN
from hypothesis.strategies import text, integers, composite, shared

@composite
def make(draw):
    n = draw(integers(min_value=1, max_value=MAX_SEQUENCE_LEN))
    a = draw(text(alphabet='01', min_size=n, max_size=n))
    b = draw(text(alphabet='01', min_size=n, max_size=n))
    return a, b

v = make()
a = shared(v, key='eval').map(lambda x: x[0])
b = shared(v, key='eval').map(lambda x: x[1])

strategy = a, b
