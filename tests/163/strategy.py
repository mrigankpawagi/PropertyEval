from hypothesis.strategies import integers

a = integers(min_value=1, max_value=50)
b = integers(min_value=1, max_value=50)

strategy = a, b
