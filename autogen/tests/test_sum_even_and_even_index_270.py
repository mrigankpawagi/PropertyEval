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
                
arr = lists(integers(), min_size=1, max_size=MAX_SEQUENCE_LEN)
strategy = arr
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def sum_even_and_even_index(arr):  
    i = 0
    sum = 0
    for i in range(0, len(arr),2): 
        if (arr[i] % 2 == 0) : 
            sum += arr[i]  
    return sum

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, sum_even_and_even_index, *args)
