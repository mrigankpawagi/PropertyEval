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

def first_odd(nums):
  first_odd = next((el for el in nums if el%2!=0),-1)
  return first_odd

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, first_odd, *args)
