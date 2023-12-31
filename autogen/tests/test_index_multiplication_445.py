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
    n = draw(integers(min_value=1, max_value=MAX_SEQUENCE_LEN))
    tup1 = draw(lists(integers(), min_size=n, max_size=n))
    tup2 = draw(lists(integers(), min_size=n, max_size=n))
    return tuple(tup1), tuple(tup2)

test_tup1 = shared(create_tuples(), key="eval").map(lambda x: x[0])
test_tup2 = shared(create_tuples(), key="eval").map(lambda x: x[1])

strategy = test_tup1, test_tup2
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def index_multiplication(test_tup1, test_tup2):
  res = tuple(tuple(a * b for a, b in zip(tup1, tup2))
   for tup1, tup2 in zip(test_tup1, test_tup2))
  return (res) 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, index_multiplication, *args)
