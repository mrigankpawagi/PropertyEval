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
                
test_tup = lists(integers() | floats() | lists(integers() | floats(), max_size=MAX_SEQUENCE_LEN).map(tuple), max_size=MAX_SEQUENCE_LEN).map(tuple)

strategy = test_tup
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def count_first_elements(test_tup):
  for count, ele in enumerate(test_tup):
    if isinstance(ele, tuple):
      break
  return (count) 

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, count_first_elements, *args)
