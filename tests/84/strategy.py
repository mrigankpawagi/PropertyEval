from hypothesis.strategies import integers

N = integers(min_value=0, max_value=10000)

strategy = N
