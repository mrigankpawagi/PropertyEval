import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
test_tup1 = lists(integers(), max_size=MAX_SEQUENCE_LEN)
test_tup2 = lists(integers(), max_size=MAX_SEQUENCE_LEN)

strategy = test_tup1, test_tup2
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def union_elements(test_tup1, test_tup2):
  res = tuple(set(test_tup1 + test_tup2))
  return (res) 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, union_elements, *args)
