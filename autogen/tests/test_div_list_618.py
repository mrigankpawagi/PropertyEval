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
                
nums1 = lists(floats(min_value=0.0, allow_infinity=False, allow_nan=False), min_size=1, max_size=MAX_SEQUENCE_LEN)
nums2 = lists(floats(min_value=0.1, allow_infinity=False, allow_nan=False), min_size=1, max_size=MAX_SEQUENCE_LEN)

strategy = nums1, nums2
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def div_list(nums1,nums2):
  result = map(lambda x, y: x / y, nums1, nums2)
  return list(result)

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, div_list, *args)
