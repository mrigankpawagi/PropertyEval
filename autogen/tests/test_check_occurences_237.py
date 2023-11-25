import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
test_list = lists(tuples(integers(), integers()), min_size=0, max_size=MAX_SEQUENCE_LEN)
strategy = test_list
if not isinstance(strategy, tuple):
    strategy = (strategy,)

from collections import Counter 
def check_occurences(test_list):
  res = dict(Counter(tuple(ele) for ele in map(sorted, test_list)))
  return  (res) 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, check_occurences, *args)
