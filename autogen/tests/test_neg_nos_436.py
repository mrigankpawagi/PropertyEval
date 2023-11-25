import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
list1 = lists(integers(), max_size=MAX_SEQUENCE_LEN)
strategy = list1
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def neg_nos(list1):
  out = []
  for num in list1: 
    if num < 0: 
      out.append(num)
  return out 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, neg_nos, *args)
