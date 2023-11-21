import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
@composite
def create_tuples(draw):
    n = draw(integers(min_value=1, max_value=10))
    tuple1 = draw(tuples(integers(min_value=1, max_value=100), min_size=n, max_size=n))
    tuple2 = draw(tuples(integers(min_value=1, max_value=100), min_size=n, max_size=n))
    return tuple1, tuple2

tuples = create_tuples()

strategy = tuples
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def division_elements(test_tup1, test_tup2):
  res = tuple(ele1 // ele2 for ele1, ele2 in zip(test_tup1, test_tup2))
  return (res) 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, division_elements, *args)
