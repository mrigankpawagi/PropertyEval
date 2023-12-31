import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
test_list = lists(lists(integers() | floats(), max_size=MAX_SEQUENCE_LEN).map(tuple), max_size=MAX_SEQUENCE_LEN)
strategy = test_list
if not isinstance(strategy, tuple):
    strategy = (strategy,)

from itertools import combinations 
def find_combinations(test_list):
  res = [(b1 + a1, b2 + a2) for (a1, a2), (b1, b2) in combinations(test_list, 2)]
  return (res) 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, find_combinations, *args)
