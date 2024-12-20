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

def check_min_heap_helper(arr, i):
    if 2 * i + 2 > len(arr):
        return True
    left_child = (arr[i] <= arr[2 * i + 1]) and check_min_heap_helper(arr, 2 * i + 1)
    right_child = (2 * i + 2 == len(arr)) or (arr[i] <= arr[2 * i + 2] 
                                      and check_min_heap_helper(arr, 2 * i + 2))
    return left_child and right_child

def check_min_heap(arr):
  return check_min_heap_helper(arr, 0)

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, check_min_heap, *args)
