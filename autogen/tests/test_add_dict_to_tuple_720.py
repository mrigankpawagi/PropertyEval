import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
test_tup = lists(integers() | floats() | booleans() | text()).map(tuple)
test_dict = dictionaries(integers() | floats() | booleans() | text(), integers() | floats() | booleans() | text())

strategy = test_tup, test_dict
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def add_dict_to_tuple(test_tup, test_dict):
  test_tup = list(test_tup)
  test_tup.append(test_dict)
  test_tup = tuple(test_tup)
  return (test_tup) 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, add_dict_to_tuple, *args)
