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
                
test_tup = lists(integers(), max_size=MAX_SEQUENCE_LEN).map(tuple)
strategy = test_tup
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def check_distinct(test_tup):
  res = True
  temp = set()
  for ele in test_tup:
    if ele in temp:
      res = False
      break
    temp.add(ele)
  return res 

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, check_distinct, *args)
