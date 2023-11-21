import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
from hypothesis import assume

lst = lists(integers(min_value=MIN_INT, max_value=MAX_INT), min_size=1, max_size=MAX_SEQUENCE_LEN)
m = integers(min_value=0, max_value=MAX_SEQUENCE_LEN)

@given(lst, m)
def test(lst, m):
    assume(m < len(lst))
    return rotate_right(lst, m)

strategy = test()
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def rotate_right(list, m):
  result =  list[-m:] + list[:-m]
  return result

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, rotate_right, *args)
