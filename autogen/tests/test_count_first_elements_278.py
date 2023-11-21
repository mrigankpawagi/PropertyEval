import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
@composite
def nested_tuples(draw):
    n = draw(integers(min_value=1, max_value=10))
    if n == 1:
        return draw(integers())
    else:
        return draw(tuples(nested_tuples(), min_size=n, max_size=n))

test_tup = nested_tuples()

strategy = test_tup
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def count_first_elements(test_tup):
  for count, ele in enumerate(test_tup):
    if isinstance(ele, tuple):
      break
  return (count) 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, count_first_elements, *args)
