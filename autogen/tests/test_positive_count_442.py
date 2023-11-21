import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
nums = lists(integers(min_value=MIN_INT, max_value=MAX_INT), max_size=MAX_SEQUENCE_LEN)

strategy = nums
if not isinstance(strategy, tuple):
    strategy = (strategy,)

from array import array
def positive_count(nums):
    n = len(nums)
    n1 = 0
    for x in nums:
        if x > 0:
            n1 += 1
        else:
          None
    return round(n1/n,2)

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, positive_count, *args)
