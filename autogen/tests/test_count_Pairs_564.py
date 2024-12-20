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
                
arr = lists(integers(), unique=True, min_size=1, max_size=MAX_SEQUENCE_LEN)
n = integers(min_value=0, max_value=MAX_SEQUENCE_LEN)

strategy = arr, n
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def count_Pairs(arr,n): 
    cnt = 0; 
    for i in range(n): 
        for j in range(i + 1,n): 
            if (arr[i] != arr[j]): 
                cnt += 1; 
    return cnt; 

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, count_Pairs, *args)
