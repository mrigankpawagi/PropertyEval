import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
@composite
def create_nested_tuples(draw):
    n = draw(integers(min_value=1, max_value=10))
    tuples = draw(lists(tuples(integers(), integers()), min_size=n, max_size=n))
    return tuples

test_tup1 = create_nested_tuples()
test_tup2 = create_nested_tuples()

strategy = test_tup1, test_tup2
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def add_nested_tuples(test_tup1, test_tup2):
  res = tuple(tuple(a + b for a, b in zip(tup1, tup2))
   for tup1, tup2 in zip(test_tup1, test_tup2))
  return (res) 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, add_nested_tuples, *args)
