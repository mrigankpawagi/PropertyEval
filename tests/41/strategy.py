from limits.limits import *
from hypothesis.strategies import integers

n = integers(min_value=1)

strategy = n
