import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given, settings
from timeout import run_with_timeout
from typing import *
import math
import string
                
@composite
def make_tuples(draw):
    n = draw(integers(min_value=1, max_value=MAX_SEQUENCE_LEN))
    tuple1 = draw(tuple_(integers(max_value=MAX_INT), integers(max_value=MAX_INT), min_size=n, max_size=n))
    tuple2 = draw(tuple_(integers(max_value=MAX_INT), integers(max_value=MAX_INT), min_size=n, max_size=n))
    return tuple1, tuple2

tuples = make_tuples()

strategy = tuples, tuples
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def maximize_elements(test_tup1, test_tup2):
  res = tuple(tuple(max(a, b) for a, b in zip(tup1, tup2))
   for tup1, tup2 in zip(test_tup1, test_tup2))
  return (res) 

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, maximize_elements, *args)
