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
                
arr = lists(integers(), min_size=1, max_size=MAX_SEQUENCE_LEN)
k = integers(min_value=1)

strategy = arr, k
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def kth_element(arr, k):
  n = len(arr)
  for i in range(n):
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] == arr[j+1], arr[j]
  return arr[k-1]

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, kth_element, *args)
