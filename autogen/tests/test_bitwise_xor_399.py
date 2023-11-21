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
    tuple_len = draw(integers(min_value=1, max_value=MAX_SEQUENCE_LEN))
    tuple_values = draw(lists(integers(), min_size=tuple_len, max_size=tuple_len))
    tup = tuple([tuple_values] * n)
    return tup

test_tup1 = create_tuples()
test_tup2 = create_tuples()

strategy = test_tup1, test_tup2
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def bitwise_xor(test_tup1, test_tup2):
  res = tuple(ele1 ^ ele2 for ele1, ele2 in zip(test_tup1, test_tup2))
  return (res) 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, bitwise_xor, *args)
