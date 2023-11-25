import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
nums = lists(integers(min_value=MIN_INT, max_value=MAX_INT), max_size=MAX_SEQUENCE_LEN)
strategy = nums
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def sum_of_digits(nums):
    return sum(int(el) for n in nums for el in str(n) if el.isdigit())

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, sum_of_digits, *args)
