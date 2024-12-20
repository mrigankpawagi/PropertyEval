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
                
arr = lists(integers(min_value=MIN_INT, max_value=MAX_INT), min_size=n, max_size=n)
n = integers(min_value=1, max_value=MAX_SEQUENCE_LEN)

strategy = arr, n
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def re_arrange_array(arr, n):
  j=0
  for i in range(0, n):
    if (arr[i] < 0):
      temp = arr[i]
      arr[i] = arr[j]
      arr[j] = temp
      j = j + 1
  return arr

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, re_arrange_array, *args)
