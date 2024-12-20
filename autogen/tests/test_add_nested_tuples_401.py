import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given, settings
from timeout import run_with_timeout
from typing import *
                
inner_tuple = tuples(integers(), integers())
nested_tuple = tuples(inner_tuple)
strategy = nested_tuple, nested_tuple
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def add_nested_tuples(test_tup1, test_tup2):
  res = tuple(tuple(a + b for a, b in zip(tup1, tup2))
   for tup1, tup2 in zip(test_tup1, test_tup2))
  return (res) 

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, add_nested_tuples, *args)
