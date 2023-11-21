import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
arr = lists(integers(min_value=MIN_INT, max_value=MAX_INT), min_size=n, max_size=n)
n = integers(min_value=2, max_value=MAX_SEQUENCE_LEN)

strategy = arr, n
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def find_min_diff(arr,n): 
    arr = sorted(arr) 
    diff = 10**20 
    for i in range(n-1): 
        if arr[i+1] - arr[i] < diff: 
            diff = arr[i+1] - arr[i]  
    return diff 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, find_min_diff, *args)
