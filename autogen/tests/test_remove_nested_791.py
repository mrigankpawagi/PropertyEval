import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
@composite
def create_nested_tuple(draw):
    n = draw(integers(min_value=0, max_value=10))
    elements = draw(lists(integers(), min_size=n, max_size=n))
    nested = draw(just(tuple(elements)))
    return tuple(elements + [nested])

test_tup = create_nested_tuple()

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
