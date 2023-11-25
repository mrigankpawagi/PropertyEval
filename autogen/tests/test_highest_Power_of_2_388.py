import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
n = integers(min_value=0, max_value=10**9)
strategy = n
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def highest_Power_of_2(n): 
    res = 0 
    for i in range(n, 0, -1): 
        if ((i & (i - 1)) == 0): 
            res = i 
            break 
    return res 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, highest_Power_of_2, *args)
