import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
x = integers(min_value=-MAX_INT, max_value=MAX_INT)
y = integers(min_value=-MAX_INT, max_value=MAX_INT)

strategy = x, y
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def multiply_int(x, y):
    if y < 0:
        return -multiply_int(x, -y)
    elif y == 0:
        return 0
    elif y == 1:
        return x
    else:
        return x + multiply_int(x, y - 1)

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, multiply_int, *args)
