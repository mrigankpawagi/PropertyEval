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
                
arr = lists(integers(min_value=0, max_value=10), max_size=MAX_SEQUENCE_LEN)

strategy = arr
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def get_Inv_Count(arr): 
    inv_count = 0
    for i in range(len(arr)): 
        for j in range(i + 1, len(arr)): 
            if (arr[i] > arr[j]): 
                inv_count += 1
    return inv_count 

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, get_Inv_Count, *args)
