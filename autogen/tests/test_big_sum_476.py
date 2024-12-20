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
                
nums = lists(integers(), min_size=1)
strategy = nums
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def big_sum(nums):
      sum= max(nums)+min(nums)
      return sum

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, big_sum, *args)
