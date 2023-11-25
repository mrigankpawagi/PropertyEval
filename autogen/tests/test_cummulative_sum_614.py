import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
test_list = lists(lists(integers() | floats(), max_size=MAX_SEQUENCE_LEN).map(tuple), max_size=MAX_SEQUENCE_LEN)
strategy = test_list
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def cummulative_sum(test_list):
  res = sum(map(sum, test_list))
  return (res)

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, cummulative_sum, *args)
