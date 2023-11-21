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
    tuples = draw(
        tuples(integers(min_value=0, max_value=100), min_size=n, max_size=n),
        tuples(integers(min_value=1, max_value=10), min_size=n, max_size=n)
    )
    return tuples

test_tup1, test_tup2 = create_tuples()

strategy = test_tup1, test_tup2
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def tuple_modulo(test_tup1, test_tup2):
  res = tuple(ele1 % ele2 for ele1, ele2 in zip(test_tup1, test_tup2)) 
  return (res) 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, tuple_modulo, *args)
