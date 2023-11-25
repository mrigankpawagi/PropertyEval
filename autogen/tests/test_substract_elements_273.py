import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
@composite
def make_tuples(draw):
    n = draw(integers(min_value=0, max_value=MAX_SEQUENCE_LEN))
    tup1 = draw(tuples(integers(), min_size=n, max_size=n))
    tup2 = draw(tuples(integers(), min_size=n, max_size=n))
    return tup1, tup2

tup1, tup2 = make_tuples()

strategy = tup1, tup2
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def substract_elements(test_tup1, test_tup2):
  res = tuple(map(lambda i, j: i - j, test_tup1, test_tup2))
  return (res) 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, substract_elements, *args)
