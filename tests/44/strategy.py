from limits.limits import *
from hypothesis.strategies import integers

x = integers(min_value=0)
base = integers(min_value=2, max_value=9)

strategy = x, base
