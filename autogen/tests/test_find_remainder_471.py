import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
arr = lists(integers(), min_size=1, max_size=MAX_SEQUENCE_LEN)
n = integers(min_value=1)

strategy = arr, n
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def find_remainder(arr, n): 
    mul = 1
    for i in range(len(arr)):  
        mul = (mul * (arr[i] % n)) % n 
    return mul % n 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, find_remainder, *args)
