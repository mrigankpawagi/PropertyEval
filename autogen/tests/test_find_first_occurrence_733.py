import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
@composite
def create_array(draw):
    n = draw(integers(min_value=1, max_value=100))
    array = draw(sorted_lists(integers(), min_size=n, max_size=n))
    return array

A = create_array()
x = integers()

strategy = A, x
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def find_first_occurrence(A, x):
    (left, right) = (0, len(A) - 1)
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if x == A[mid]:
            result = mid
            right = mid - 1
        elif x < A[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return result

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, find_first_occurrence, *args)
