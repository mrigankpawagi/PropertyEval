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
                
arr = lists(integers(min_value=1, max_value=100), min_size=1, max_size=MAX_SEQUENCE_LEN)
strategy = arr
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def max_product(arr):   
  n = len(arr)
  mpis = arr[:]
  for i in range(n): 
    current_prod = arr[i]
    j = i + 1
    while j < n:
      if arr[j-1] > arr[j]: 
        break
      current_prod *= arr[j]
      if current_prod > mpis[j]:
        mpis[j] = current_prod 
      j = j + 1
  return max(mpis)

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, max_product, *args)
