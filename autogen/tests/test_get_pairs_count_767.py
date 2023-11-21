import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
arr = lists(integers(), min_size=2)
sum_value = integers()

strategy = arr, sum_value
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def get_pairs_count(arr, sum):
    count = 0  
    for i in range(len(arr)):
        for j in range(i + 1,len(arr)):
            if arr[i] + arr[j] == sum:
                count += 1
    return count

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, get_pairs_count, *args)
