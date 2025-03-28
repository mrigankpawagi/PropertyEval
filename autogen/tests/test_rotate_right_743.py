import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given, settings
from timeout import run_with_timeout
from typing import *
import math
import string
                
lst = lists(integers(), max_size=MAX_SEQUENCE_LEN)
m = integers(min_value=0, exclude_min=True)

strategy = lst, m
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def rotate_right(list, m):
  result =  list[-m:] + list[:-m]
  return result

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, rotate_right, *args)
