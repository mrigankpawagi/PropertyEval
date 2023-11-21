import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
@composite
def create_mixed_tuple(draw):
    n = draw(integers(min_value=1, max_value=MAX_SEQUENCE_LEN))
    elements = draw(lists(one_of(integers(), floats(), text())), min_size=n, max_size=n)
    return tuple(elements)

test_tuple = create_mixed_tuple()

strategy = test_tuple
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def check_type(test_tuple):
  res = True
  for ele in test_tuple:
    if not isinstance(ele, type(test_tuple[0])):
      res = False
      break
  return (res) 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, check_type, *args)
