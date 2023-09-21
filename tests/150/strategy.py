from hypothesis.strategies import integers, floats, one_of

n = integers(min_value=-100, max_value=100)
x = one_of(integers(), floats())
y = one_of(integers(), floats())

strategy = n, x, y
