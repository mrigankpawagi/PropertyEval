import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
test_tup = tuples(integers(), tuples(integers()))

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
