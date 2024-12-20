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
                
nums = tuples(integers(min_value=1))
strategy = nums
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def tuple_to_int(nums):
    result = int(''.join(map(str,nums)))
    return result

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, tuple_to_int, *args)
