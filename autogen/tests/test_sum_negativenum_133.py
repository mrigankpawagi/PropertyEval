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

def sum_negativenum(nums):
  sum_negativenum = list(filter(lambda nums:nums<0,nums))
  return sum(sum_negativenum)

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, sum_negativenum, *args)
