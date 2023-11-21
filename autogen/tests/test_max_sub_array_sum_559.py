import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
a = lists(integers(), min_size=size, max_size=size)
size = integers(min_value=1, max_value=MAX_SEQUENCE_LEN)

strategy = a, size
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def max_sub_array_sum(a, size):
  max_so_far = 0
  max_ending_here = 0
  for i in range(0, size):
    max_ending_here = max_ending_here + a[i]
    if max_ending_here < 0:
      max_ending_here = 0
    elif (max_so_far < max_ending_here):
      max_so_far = max_ending_here
  return max_so_far

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, max_sub_array_sum, *args)
