import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
arr1 = lists(integers(), unique=True, max_size=MAX_SEQUENCE_LEN)
arr2 = lists(integers(), unique=True, max_size=MAX_SEQUENCE_LEN)
k = integers(min_value=1)

strategy = arr1, arr2, k
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def find_kth(arr1, arr2, k):
	m = len(arr1)
	n = len(arr2)
	sorted1 = [0] * (m + n)
	i = 0
	j = 0
	d = 0
	while (i < m and j < n):
		if (arr1[i] < arr2[j]):
			sorted1[d] = arr1[i]
			i += 1
		else:
			sorted1[d] = arr2[j]
			j += 1
		d += 1
	while (i < m):
		sorted1[d] = arr1[i]
		d += 1
		i += 1
	while (j < n):
		sorted1[d] = arr2[j]
		d += 1
		j += 1
	return sorted1[k - 1]

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, find_kth, *args)
