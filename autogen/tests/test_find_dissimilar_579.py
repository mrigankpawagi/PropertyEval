import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
@composite
def create_tuple(draw, min_size=0, max_size=MAX_SEQUENCE_LEN):
    n = draw(integers(min_value=min_size, max_value=max_size))
    return tuple(draw(integers()), min_size=n, max_size=n)

test_tup1 = create_tuple()
test_tup2 = create_tuple()

strategy = test_tup1, test_tup2
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def find_dissimilar(test_tup1, test_tup2):
  res = tuple(set(test_tup1) ^ set(test_tup2))
  return (res) 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, find_dissimilar, *args)
