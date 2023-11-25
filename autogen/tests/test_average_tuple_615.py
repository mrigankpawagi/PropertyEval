import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
nums = lists(lists(integers() | floats(), max_size=MAX_SEQUENCE_LEN).map(tuple), max_size=MAX_SEQUENCE_LEN).map(tuple)
strategy = nums
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def average_tuple(nums):
    result = [sum(x) / len(x) for x in zip(*nums)]
    return result

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, average_tuple, *args)
