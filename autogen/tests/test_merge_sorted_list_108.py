import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
num1 = lists(integers(min_value=MIN_INT, max_value=MAX_INT), max_size=MAX_SEQUENCE_LEN)
num2 = lists(integers(min_value=MIN_INT, max_value=MAX_INT), max_size=MAX_SEQUENCE_LEN)
num3 = lists(integers(min_value=MIN_INT, max_value=MAX_INT), max_size=MAX_SEQUENCE_LEN)

strategy = num1, num2, num3
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import heapq
def merge_sorted_list(num1,num2,num3):
  num1=sorted(num1)
  num2=sorted(num2)
  num3=sorted(num3)
  result = heapq.merge(num1,num2,num3)
  return list(result)

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, merge_sorted_list, *args)
