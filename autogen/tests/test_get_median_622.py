import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
from typing import List
from hypothesis import given
from hypothesis.strategies import lists, integers

def get_median(arr1: List[int], arr2: List[int], n: int) -> float:
    """
    Finds the median of two sorted lists of the same size.

    Parameters:
    arr1 (List[int]): The first sorted list.
    arr2 (List[int]): The second sorted list.
    n (int): The size of the lists.

    Returns:
    float: The median of the two lists.

    """
    combined = arr1 + arr2
    combined.sort()
    mid = n - 1
    return combined[mid] if n % 2 != 0 else (combined[mid] + combined[mid + 1]) / 2

@given(arr1=lists(integers()), arr2=lists(integers()), n=integers(min_value=0))
def test_get_median(arr1, arr2, n):
    get_median(arr1, arr2, n)

test_get_median()

strategy = integers(min_value=0)
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
