import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
x = integers()

strategy = x
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def find_Parity(x): 
    y = x ^ (x >> 1); 
    y = y ^ (y >> 2); 
    y = y ^ (y >> 4); 
    y = y ^ (y >> 8); 
    y = y ^ (y >> 16); 
    if (y & 1): 
        return True
    return False

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, find_Parity, *args)
