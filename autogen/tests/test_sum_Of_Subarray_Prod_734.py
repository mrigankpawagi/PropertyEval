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
                
arr = lists(integers(min_value=1, max_value=10), min_size=1, max_size=MAX_SEQUENCE_LEN)

strategy = arr
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def sum_Of_Subarray_Prod(arr):
    ans = 0
    res = 0
    i = len(arr) - 1
    while (i >= 0):
        incr = arr[i]*(1 + res)
        ans += incr
        res = incr
        i -= 1
    return (ans)

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, sum_Of_Subarray_Prod, *args)
