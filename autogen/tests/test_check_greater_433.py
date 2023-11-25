import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
arr = lists(integers(), min_size=1, max_size=MAX_SEQUENCE_LEN)
number = integers()
strategy = arr, number
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def check_greater(arr, number):
  arr.sort()
  return number > arr[-1]

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, check_greater, *args)
