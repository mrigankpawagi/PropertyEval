import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
a = integers(min_value=MIN_INT, max_value=MAX_INT)
b = integers(min_value=MIN_INT, max_value=MAX_INT)
c = integers(min_value=MIN_INT, max_value=MAX_INT)

strategy = a, b, c
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def median_numbers(a,b,c):
 if a > b:
    if a < c:
        median = a
    elif b > c:
        median = b
    else:
        median = c
 else:
    if a > c:
        median = a
    elif b < c:
        median = b
    else:
        median = c
 return median

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, median_numbers, *args)
