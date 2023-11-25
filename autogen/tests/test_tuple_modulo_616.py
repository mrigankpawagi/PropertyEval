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
    n = draw(integers(min_value=1, max_value=MAX_SEQUENCE_LEN))
    t1 = draw(lists(integers(), min_size=n, max_size=n).map(tuple))
    t2 = draw(lists(integers(min_value=1), min_size=n, max_size=n).map(tuple))
    return t1, t2

test_tup1 = shared(make_tuples().map(lambda x: x[0]), key="eval")
test_tup2 = shared(make_tuples().map(lambda x: x[1]), key="eval")

strategy = test_tup1, test_tup2
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def tuple_modulo(test_tup1, test_tup2):
  res = tuple(ele1 % ele2 for ele1, ele2 in zip(test_tup1, test_tup2)) 
  return (res) 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, tuple_modulo, *args)
