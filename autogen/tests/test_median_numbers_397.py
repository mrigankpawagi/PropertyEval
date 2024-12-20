import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given, settings
from timeout import run_with_timeout
from typing import *
import math
import string
                
a = floats(min_value=MIN_FLOAT, max_value=MAX_FLOAT)
b = floats(min_value=MIN_FLOAT, max_value=MAX_FLOAT)
c = floats(min_value=MIN_FLOAT, max_value=MAX_FLOAT)

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
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, median_numbers, *args)
