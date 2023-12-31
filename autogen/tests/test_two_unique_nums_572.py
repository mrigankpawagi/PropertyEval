import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
nums = lists(integers(), max_size=MAX_SEQUENCE_LEN)

strategy = nums
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def two_unique_nums(nums):
  return [i for i in nums if nums.count(i)==1]

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, two_unique_nums, *args)
