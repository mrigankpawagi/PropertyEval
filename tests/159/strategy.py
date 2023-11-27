from limits.limits import *
from hypothesis.strategies import integers

num = integers(min_value=0, max_value=1000)
need = integers(min_value=0, max_value=1000)
remaining = integers(min_value=0, max_value=1000)

strategy = num, need, remaining
