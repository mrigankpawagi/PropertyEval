import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
lst = lists(integers(min_value=MIN_INT, max_value=MAX_INT))

strategy = lst
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def pos_count(list):
  pos_count= 0
  for num in list: 
    if num >= 0: 
      pos_count += 1
  return pos_count 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, pos_count, *args)
