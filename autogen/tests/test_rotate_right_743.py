import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
lst = lists(integers(), max_size=MAX_SEQUENCE_LEN)
m = integers(min_value=0, max_value=MAX_SEQUENCE_LEN)

strategy = lst, m
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def rotate_right(list, m):
  result =  list[-m:] + list[:-m]
  return result

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, rotate_right, *args)
