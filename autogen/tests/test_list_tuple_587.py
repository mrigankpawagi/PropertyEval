import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
listx = lists(integers(), min_size=1)

strategy = listx
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def list_tuple(listx):
  tuplex = tuple(listx)
  return tuplex

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, list_tuple, *args)
