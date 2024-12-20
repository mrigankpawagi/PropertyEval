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
                
test_tup = lists(integers() | tuples(integers()), max_size=MAX_SEQUENCE_LEN).map(tuple)
strategy = test_tup
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def remove_nested(test_tup):
  res = tuple()
  for count, ele in enumerate(test_tup):
    if not isinstance(ele, tuple):
      res = res + (ele, )
  return (res) 

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, remove_nested, *args)
