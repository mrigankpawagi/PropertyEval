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
                
xs = lists(integers(), min_size=1, max_size=MAX_SEQUENCE_LEN)
strategy = xs
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def smallest_num(xs):
  return min(xs)


@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, smallest_num, *args)
