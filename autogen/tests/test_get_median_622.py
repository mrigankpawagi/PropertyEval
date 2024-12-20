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
                
arr1 = lists(integers(), min_size=1, max_size=MAX_SEQUENCE_LEN).map(sorted)
arr2 = arr1
n = len(arr1)

strategy = arr1, arr2, n
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def get_median(arr1, arr2, n):
  i = 0
  j = 0
  m1 = -1
  m2 = -1
  count = 0
  while count < n + 1:
    count += 1
    if i == n:
      m1 = m2
      m2 = arr2[0]
      break
    elif j == n:
      m1 = m2
      m2 = arr1[0]
      break
    if arr1[i] <= arr2[j]:
      m1 = m2
      m2 = arr1[i]
      i += 1
    else:
      m1 = m2
      m2 = arr2[j]
      j += 1
  return (m1 + m2)/2

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, get_median, *args)
