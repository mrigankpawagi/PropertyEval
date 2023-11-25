import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
arr = lists(integers(), max_size=MAX_SEQUENCE_LEN)
n = integers(min_value=0, exclude_min=True)

strategy = arr, n
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def pair_xor_Sum(arr,n) : 
    ans = 0 
    for i in range(0,n) :    
        for j in range(i + 1,n) :   
            ans = ans + (arr[i] ^ arr[j])          
    return ans 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, pair_xor_Sum, *args)
