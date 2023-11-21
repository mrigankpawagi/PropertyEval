import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
nums = lists(integers(), min_size=1, max_size=MAX_SEQUENCE_LEN)

strategy = nums
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def odd_position(nums):
	return all(nums[i]%2==i%2 for i in range(len(nums)))

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, odd_position, *args)
