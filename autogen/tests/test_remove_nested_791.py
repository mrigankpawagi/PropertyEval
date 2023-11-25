import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
@composite
def tuple_with_nested(draw):
    nested = draw(lists(one_of(tuples(integers(), integers()), lists(integers()))))
    return tuple(nested)

test_tup = tuple_with_nested()
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
