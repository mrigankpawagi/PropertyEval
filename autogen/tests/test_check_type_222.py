import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
@composite
def get_tuple(draw):
    elements = draw(lists(elements=integers() | floats() | text() | booleans(), min_size=1, max_size=MAX_SEQUENCE_LEN))
    return tuple(elements)

test_tuple = get_tuple()

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
