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
    t1 = draw(tuples(integers(min_value=1, max_value=10), min_size=n, max_size=n))
    t2 = draw(tuples(integers(min_value=1, max_value=10), min_size=n, max_size=n))
    return t1, t2

test_tup1 = shared(create_tuples(), key="eval").map(lambda x: x[0])
test_tup2 = shared(create_tuples(), key="eval").map(lambda x: x[1])

strategy = test_tup1, test_tup2
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def find_dissimilar(test_tup1, test_tup2):
  res = tuple(set(test_tup1) ^ set(test_tup2))
  return (res) 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, find_dissimilar, *args)
