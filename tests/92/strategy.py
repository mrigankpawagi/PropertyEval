from hypothesis.strategies import integers, floats, booleans, one_of

x = one_of(integers(), floats(), booleans())
y = one_of(integers(), floats(), booleans())
z = one_of(integers(), floats(), booleans())

strategy = x, y, z
