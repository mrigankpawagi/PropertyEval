import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
nums = lists(
    tuples(
        integers(min_value=MIN_INT, max_value=MAX_INT),
        min_size=MIN_TUPLE_SIZE,
        max_size=MAX_TUPLE_SIZE,
    ),
    min_size=MIN_LIST_SIZE,
    max_size=MAX_LIST_SIZE,
)

strategy = nums
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def average_tuple(nums):
    result = [sum(x) / len(x) for x in zip(*nums)]
    return result

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, average_tuple, *args)
