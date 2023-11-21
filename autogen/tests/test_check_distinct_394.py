import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
test_tup = tuples(integers(min_value=MIN_INT, max_value=MAX_INT), max_size=MAX_SEQUENCE_LEN)

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
def test_fuzz(args):
    run_with_timeout(0.3, check_distinct, *args)
