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
                
arr = lists(integers(), min_size=1, unique=True, ordered=True)
x = integers()

strategy = arr, x
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def last(arr,x):
    n = len(arr)
    low = 0
    high = n - 1
    res = -1  
    while (low <= high):
        mid = (low + high) // 2 
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            res = mid
            low = mid + 1
    return res

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, last, *args)
