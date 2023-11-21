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
    n = draw(integers(min_value=1, max_value=10))
    a = draw(lists(integers(min_value=-100, max_value=100), min_size=n, max_size=n))
    return a

a = create_array()
n = integers(min_value=1, max_value=10)
k = integers(min_value=1, max_value=10)

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
def test_fuzz(args):
    run_with_timeout(0.3, max_sub_array_sum_repeated, *args)
