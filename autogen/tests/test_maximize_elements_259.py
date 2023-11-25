import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
test_tup1 = lists(tuples(integers() | floats(), integers() | floats()), min_size=1, max_size=MAX_SEQUENCE_LEN).map(tuple)
test_tup2 = lists(tuples(integers() | floats(), integers() | floats()), min_size=1, max_size=MAX_SEQUENCE_LEN).map(tuple)

strategy = test_tup1, test_tup2
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def maximize_elements(test_tup1, test_tup2):
  res = tuple(tuple(max(a, b) for a, b in zip(tup1, tup2))
   for tup1, tup2 in zip(test_tup1, test_tup2))
  return (res) 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, maximize_elements, *args)
