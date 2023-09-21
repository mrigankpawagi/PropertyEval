from hypothesis.strategies import integers

a = integers(min_value=1)
b = integers(min_value=1)

strategy = a, b
