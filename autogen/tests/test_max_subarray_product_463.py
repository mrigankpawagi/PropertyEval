import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
arr = lists(integers(), min_size=1, max_size=MAX_SEQUENCE_LEN)

strategy = arr
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def max_subarray_product(arr):
	n = len(arr)
	max_ending_here = 1
	min_ending_here = 1
	max_so_far = 0
	flag = 0
	for i in range(0, n):
		if arr[i] > 0:
			max_ending_here = max_ending_here * arr[i]
			min_ending_here = min (min_ending_here * arr[i], 1)
			flag = 1
		elif arr[i] == 0:
			max_ending_here = 1
			min_ending_here = 1
		else:
			temp = max_ending_here
			max_ending_here = max (min_ending_here * arr[i], 1)
			min_ending_here = temp * arr[i]
		if (max_so_far < max_ending_here):
			max_so_far = max_ending_here
	if flag == 0 and max_so_far == 0:
		return 0
	return max_so_far

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, max_subarray_product, *args)
