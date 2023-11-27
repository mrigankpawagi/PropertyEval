from limits.limits import *
from hypothesis.strategies import integers

x = integers()
y = integers()

strategy = x, y
