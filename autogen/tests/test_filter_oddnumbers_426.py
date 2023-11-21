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

def filter_oddnumbers(nums):
 odd_nums = list(filter(lambda x: x%2 != 0, nums))
 return odd_nums

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, filter_oddnumbers, *args)
