from hypothesis.strategies import integers

x = integers(min_value=0)
shift = integers(min_value=0)

strategy = x, shift
