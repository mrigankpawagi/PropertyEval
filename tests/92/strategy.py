from limits.limits import *
from hypothesis.strategies import integers, shared, floats, booleans

n = integers() | floats() | booleans()
x = shared(n)
y = shared(n)
z = shared(n)

strategy = x, y, z
