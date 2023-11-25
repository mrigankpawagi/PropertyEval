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

def geometric_sum(n):
  if n < 0:
    return 0
  else:
    return 1 / (pow(2, n)) + geometric_sum(n - 1)

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, geometric_sum, *args)
