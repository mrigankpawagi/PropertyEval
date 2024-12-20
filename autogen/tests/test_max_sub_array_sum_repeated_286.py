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
                
a = lists(integers(min_value=-1000000000, max_value=1000000000), min_size=1, max_size=MAX_SEQUENCE_LEN).filter(lambda x: any(x))
n = integers(min_value=1, max_value=MAX_SEQUENCE_LEN)
k = integers(min_value=1, max_value=100)

strategy = a, n, k
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def max_sub_array_sum_repeated(a, n, k): 
	max_so_far = -2147483648
	max_ending_here = 0
	for i in range(n*k): 
		max_ending_here = max_ending_here + a[i%n] 
		if (max_so_far < max_ending_here): 
			max_so_far = max_ending_here 
		if (max_ending_here < 0): 
			max_ending_here = 0
	return max_so_far

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, max_sub_array_sum_repeated, *args)
