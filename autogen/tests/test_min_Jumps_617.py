import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
steps = tuples(integers(), integers())
d = floats(allow_infinity=False, allow_nan=False, min_value=0)

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
def test_fuzz(args):
    run_with_timeout(0.3, min_Jumps, *args)
