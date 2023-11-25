import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
n = integers(min_value=1, max_value=MAX_INT)

strategy = n
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def set_left_most_unset_bit(n): 
    if not (n & (n + 1)): 
        return n 
    pos, temp, count = 0, n, 0 
    while temp: 
        if not (temp & 1): 
            pos = count      
        count += 1; temp>>=1
    return (n | (1 << (pos))) 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, set_left_most_unset_bit, *args)
