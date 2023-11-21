import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
ele = tuples(integers(min_value=0, max_value=10), integers(min_value=0, max_value=10))
sub = lists(tuples(integers(min_value=0, max_value=10), integers(min_value=0, max_value=10)), min_size=0, max_size=10)

strategy = ele, sub
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def adjac(ele, sub = []): 
  if not ele: 
     yield sub 
  else: 
     yield from [idx for j in range(ele[0] - 1, ele[0] + 2) 
                for idx in adjac(ele[1:], sub + [j])] 
def get_coordinates(test_tup):
  return list(adjac(test_tup))

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, adjac, *args)
