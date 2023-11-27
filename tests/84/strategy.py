from limits.limits import *
from hypothesis.strategies import integers

N = integers(min_value=1, max_value=10000)

strategy = N
