import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
xs = lists(integers(), min_size=1)
strategy = xs
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def smallest_num(xs):
  return min(xs)


@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, smallest_num, *args)
