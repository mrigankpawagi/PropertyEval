from limits.limits import *
from hypothesis.strategies import integers

a = integers()
b = integers()

strategy = a, b
