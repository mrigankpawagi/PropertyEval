import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
nums = lists(integers(), max_size=MAX_SEQUENCE_LEN)
n = integers(min_value=0, max_value=10)

strategy = nums, n
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def nth_nums(nums,n):
 nth_nums = list(map(lambda x: x ** n, nums))
 return nth_nums

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, nth_nums, *args)
