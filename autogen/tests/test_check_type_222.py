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
                
test_tuple = lists(elements=one_of(integers(), text()), min_size=1, max_size=MAX_SEQUENCE_LEN).map(tuple)
strategy = test_tuple
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def check_type(test_tuple):
  res = True
  for ele in test_tuple:
    if not isinstance(ele, type(test_tuple[0])):
      res = False
      break
  return (res) 

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, check_type, *args)
