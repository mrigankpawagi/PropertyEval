import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
test_tup = lists(floats(min_value=MIN_FLOAT, max_value=MAX_FLOAT), min_size=2, max_size=MAX_SEQUENCE_LEN).map(tuple)
strategy = test_tup
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def multiply_elements(test_tup):
  res = tuple(i * j for i, j in zip(test_tup, test_tup[1:]))
  return (res) 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, multiply_elements, *args)
