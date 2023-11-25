import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
@composite
def create(draw):
  n = draw(integers(min_value=1, max_value=MAX_SEQUENCE_LEN))
  arr1 = draw(lists(integers(), min_size=n, max_size=n))
  arr2 = draw(lists(integers(), min_size=n, max_size=n))
  return arr1, arr2, n

arr1 = shared(create(), key='eval').map(lambda x: x[0])
arr2 = shared(create(), key='eval').map(lambda x: x[1])
n = shared(create(), key='eval').map(lambda x: x[2])

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
def test_fuzz(args):
    run_with_timeout(0.3, get_median, *args)
