import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
L = lists(integers(), min_size=1)
strategy = L
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def multiple_to_single(L):
  x = int("".join(map(str, L)))
  return x

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, multiple_to_single, *args)
