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
                
arr = lists(integers(), max_size=MAX_SEQUENCE_LEN)

strategy = arr
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def max_sum(arr): 
	MSIBS = arr[:] 
	for i in range(len(arr)): 
		for j in range(0, i): 
			if arr[i] > arr[j] and MSIBS[i] < MSIBS[j] + arr[i]: 
				MSIBS[i] = MSIBS[j] + arr[i] 
	MSDBS = arr[:] 
	for i in range(1, len(arr) + 1): 
		for j in range(1, i): 
			if arr[-i] > arr[-j] and MSDBS[-i] < MSDBS[-j] + arr[-i]: 
				MSDBS[-i] = MSDBS[-j] + arr[-i] 
	max_sum = float("-Inf") 
	for i, j, k in zip(MSIBS, MSDBS, arr): 
		max_sum = max(max_sum, i + j - k) 
	return max_sum

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, max_sum, *args)
