from hypothesis.strategies import integers

n = integers(min_value=0)
p = integers(min_value=1)

strategy = n, p
