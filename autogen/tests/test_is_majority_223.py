import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
from math import ceil

@composite
def make_arr(draw):
    n = draw(integers(min_value=1, max_value=MAX_SEQUENCE_LEN))
    arr = draw(lists(integers(), min_size=n, max_size=n))
    arr.sort()
    x = draw(sampled_from(arr))
    return arr, n, x

arr = shared(make_arr(), key="eval").map(lambda x: x[0])
n = shared(make_arr(), key="eval").map(lambda x: x[1])
x = shared(make_arr(), key="eval").map(lambda x: x[2])

strategy = arr, n, x
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def is_majority(arr, n, x):
	i = binary_search(arr, 0, n-1, x)
	if i == -1:
		return False
	if ((i + n//2) <= (n -1)) and arr[i + n//2] == x:
		return True
	else:
		return False
def binary_search(arr, low, high, x):
	if high >= low:
		mid = (low + high)//2 
		if (mid == 0 or x > arr[mid-1]) and (arr[mid] == x):
			return mid
		elif x > arr[mid]:
			return binary_search(arr, (mid + 1), high, x)
		else:
			return binary_search(arr, low, (mid -1), x)
	return -1

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, is_majority, *args)
