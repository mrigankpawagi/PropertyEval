import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
nums1 = lists(integers(), min_size=1, max_size=MAX_SEQUENCE_LEN)
nums2 = shared(nums1)

strategy = nums1, nums2
if not isinstance(strategy, tuple):
    strategy = (strategy,)

from operator import eq
def count_same_pair(nums1, nums2):
    result = sum(map(eq, nums1, nums2))
    return result

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, count_same_pair, *args)
