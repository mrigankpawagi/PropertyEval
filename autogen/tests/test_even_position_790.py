import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
import hypothesis.strategies as st

def even_position(nums):
    return all(num % 2 == 0 for idx, num in enumerate(nums) if idx % 2 == 0)

nums = st.lists(st.integers(min_value=1, max_value=100))

strategy = nums
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def even_position(nums):
	return all(nums[i]%2==i%2 for i in range(len(nums)))

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, even_position, *args)
