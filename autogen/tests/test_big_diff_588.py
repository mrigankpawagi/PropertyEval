import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
nums = lists(integers(), min_size=2, max_size=MAX_SEQUENCE_LEN)
strategy = nums
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def big_diff(nums):
     diff= max(nums)-min(nums)
     return diff

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, big_diff, *args)
