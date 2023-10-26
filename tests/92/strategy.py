from limits.limits import MAX_INT, MIN_INT, MAX_FLOAT, MIN_FLOAT, MAX_SEQUENCE_LEN
from hypothesis.strategies import integers, shared, floats, booleans

n = integers() | floats() | booleans()
x = shared(n)
y = shared(n)
z = shared(n)

strategy = x, y, z
