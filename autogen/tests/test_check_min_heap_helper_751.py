import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
@composite
def create(draw):
  n = draw(integers(min_value=1, max_value=MAX_SEQUENCE_LEN))
  arr = draw(lists(integers(), min_size=n, max_size=n))
  i = draw(integers(min_value=0, max_value=n-1))
  return arr, i

arr = shared(create(), key='eval').map(lambda x: x[0])
i = shared(create(), key='eval').map(lambda x: x[1])

strategy = arr, i
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
def test_fuzz(args):
    run_with_timeout(0.3, check_min_heap_helper, *args)
