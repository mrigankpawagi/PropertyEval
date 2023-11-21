import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
test_list = lists(integers(), max_size=MAX_SEQUENCE_LEN)
test_tup = tuples(integers(), integers())

strategy = test_list, test_tup
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def add_tuple(test_list, test_tup):
  test_list += test_tup
  return test_list

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, add_tuple, *args)
