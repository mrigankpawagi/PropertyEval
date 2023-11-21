import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
@composite
def create_tuple(draw):
    n = draw(integers(min_value=1, max_value=MAX_SEQUENCE_LEN))
    tup = draw(tuples(integers(min_value=MIN_INT, max_value=MAX_INT), min_size=n, max_size=n))
    return tup

test_tup1 = create_tuple()
test_tup2 = create_tuple()

strategy = test_tup1, test_tup2
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def and_tuples(test_tup1, test_tup2):
  res = tuple(ele1 & ele2 for ele1, ele2 in zip(test_tup1, test_tup2))
  return (res) 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, and_tuples, *args)
