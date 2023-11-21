import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
test_tup = tuples(integers(), integers(), integers(), integers(), none())

strategy = test_tup
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def check_none(test_tup):
  res = any(map(lambda ele: ele is None, test_tup))
  return res 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, check_none, *args)
