import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
nums = tuples(integers(min_value=1))

strategy = nums
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def tuple_to_int(nums):
    result = int(''.join(map(str,nums)))
    return result

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, tuple_to_int, *args)
