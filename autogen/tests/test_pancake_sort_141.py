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
                
nums = lists(integers(), max_size=MAX_SEQUENCE_LEN)
strategy = nums
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def pancake_sort(nums):
    arr_len = len(nums)
    while arr_len > 1:
        mi = nums.index(max(nums[0:arr_len]))
        nums = nums[mi::-1] + nums[mi+1:len(nums)]
        nums = nums[arr_len-1::-1] + nums[arr_len:len(nums)]
        arr_len -= 1
    return nums

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, pancake_sort, *args)
