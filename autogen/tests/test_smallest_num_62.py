import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
from typing import List
smallest_num = min(xs)
# Using the min function to find the smallest number in the list

strategy = lists(integers(min_value=MIN_INT, max_value=MAX_INT), min_size=1)
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def smallest_num(xs):
  return min(xs)


@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, smallest_num, *args)
