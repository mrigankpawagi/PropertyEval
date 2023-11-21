import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
nums = lists(integers(min_value=MIN_INT, max_value=MAX_INT), min_size=1)

strategy = nums
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def cube_nums(nums):
 cube_nums = list(map(lambda x: x ** 3, nums))
 return cube_nums

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, cube_nums, *args)
