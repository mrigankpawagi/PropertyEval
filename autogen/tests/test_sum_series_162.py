import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
n = integers(min_value=0, max_value=MAX_INT)

strategy = n
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def sum_series(n):
  if n < 1:
    return 0
  else:
    return n + sum_series(n - 2)

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, sum_series, *args)
