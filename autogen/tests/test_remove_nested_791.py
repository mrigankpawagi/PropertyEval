import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
@composite
def nested_tuple(draw):
    inner_tuple = draw(tuples(integers(), integers()))
    outer_tuple = draw(tuples(integers(), integers()))
    return outer_tuple + (inner_tuple,)

test_tup = nested_tuple()

strategy = test_tup
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def remove_nested(test_tup):
  res = tuple()
  for count, ele in enumerate(test_tup):
    if not isinstance(ele, tuple):
      res = res + (ele, )
  return (res) 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, remove_nested, *args)
