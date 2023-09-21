from hypothesis.strategies import integers, floats, one_of, builds, booleans

def to_str(x, b):
    if isinstance(x, int):
        return str(x)
    elif isinstance(x, float):
        return str(x) if b else str(x).replace('.', ',')

a = one_of(integers(), floats(), builds(to_str, one_of(integers(), floats()), booleans()))
b = one_of(integers(), floats(), builds(to_str, one_of(integers(), floats()), booleans()))

strategy = a, b
