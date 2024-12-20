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
                
test_tup = lists(integers(), min_size=2, max_size=MAX_SEQUENCE_LEN).map(tuple)
strategy = test_tup
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def add_pairwise(test_tup):
  res = tuple(i + j for i, j in zip(test_tup, test_tup[1:]))
  return (res) 

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, add_pairwise, *args)
