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
                
nums = lists(integers(), min_size=1, max_size=MAX_SEQUENCE_LEN)
n = integers(min_value=1)

strategy = nums, n
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import heapq as hq
def heap_queue_largest(nums,n):
  largest_nums = hq.nlargest(n, nums)
  return largest_nums

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, heap_queue_largest, *args)
