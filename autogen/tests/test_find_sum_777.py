import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given, settings
from timeout import run_with_timeout
from typing import *
import math
import string
                
arr = lists(integers(min_value=MIN_INT, max_value=MAX_INT), max_size=MAX_SEQUENCE_LEN)
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
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, find_sum, *args)
