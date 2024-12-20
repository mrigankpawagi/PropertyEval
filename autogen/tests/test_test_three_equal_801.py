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
                
x = integers(min_value=MIN_INT, max_value=MAX_INT)
y = integers(min_value=MIN_INT, max_value=MAX_INT)
z = integers(min_value=MIN_INT, max_value=MAX_INT)

strategy = x, y, z
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def test_three_equal(x,y,z):
  result = set([x,y,z])
  if len(result)==3:
    return 0
  else:
    return 4-len(result)

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, test_three_equal, *args)
