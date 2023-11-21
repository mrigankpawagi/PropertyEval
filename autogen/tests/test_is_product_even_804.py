import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
arr = lists(integers(), min_size=1)

strategy = arr
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def is_product_even(arr): 
    for i in range(len(arr)): 
        if (arr[i] & 1) == 0: 
            return True
    return False

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, is_product_even, *args)
