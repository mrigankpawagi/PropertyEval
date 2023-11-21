import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
arr = lists(integers(), max_size=MAX_SEQUENCE_LEN)

strategy = arr
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def find_sum(arr): 
    arr.sort() 
    sum = arr[0] 
    for i in range(len(arr)-1): 
        if (arr[i] != arr[i+1]): 
            sum = sum + arr[i+1]   
    return sum

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, find_sum, *args)
