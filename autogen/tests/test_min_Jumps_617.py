import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given, settings
from timeout import run_with_timeout
from typing import *
                
steps = integers(min_value=1, max_value=10)
d = integers(min_value=1, max_value=10)

strategy = steps, d
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def min_Jumps(steps, d): 
    (a, b) = steps
    temp = a 
    a = min(a, b) 
    b = max(temp, b) 
    if (d >= b): 
        return (d + b - 1) / b 
    if (d == 0): 
        return 0
    if (d == a): 
        return 1
    else:
        return 2

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, min_Jumps, *args)
