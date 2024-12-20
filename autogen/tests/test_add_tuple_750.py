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
                
test_list = lists(integers(), max_size=MAX_SEQUENCE_LEN)
test_tup = tuples(integers(), integers())

strategy = test_list, test_tup
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def add_tuple(test_list, test_tup):
  test_list += test_tup
  return test_list

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, add_tuple, *args)
