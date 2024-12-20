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
                
nums1 = lists(integers(), min_size=1, max_size=MAX_SEQUENCE_LEN)
nums2 = lists(integers(), min_size=1, max_size=MAX_SEQUENCE_LEN)
N = integers(min_value=1, max_value=MAX_SEQUENCE_LEN)

strategy = nums1, nums2, N
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def large_product(nums1, nums2, N):
    result = sorted([x*y for x in nums1 for y in nums2], reverse=True)[:N]
    return result

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, large_product, *args)
