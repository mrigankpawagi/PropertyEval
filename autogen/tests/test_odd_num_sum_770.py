import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
n = integers(min_value=1, max_value=100)

strategy = n
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def odd_num_sum(n) : 
    j = 0
    sm = 0
    for i in range(1,n + 1) : 
        j = (2*i-1) 
        sm = sm + (j*j*j*j)   
    return sm 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, odd_num_sum, *args)
