import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
arr = lists(integers(), min_size=2, max_size=MAX_SEQUENCE_LEN)
n = builds(lambda x: len(x), arr)

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
def test_fuzz(args):
    run_with_timeout(0.3, count_Pairs, *args)
