import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
n = integers(min_value=0, max_value=10)
m = integers(min_value=0, max_value=10)

strategy = n, m
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def eulerian_num(n, m): 
	if (m >= n or n == 0): 
		return 0 
	if (m == 0): 
		return 1 
	return ((n - m) * eulerian_num(n - 1, m - 1) +(m + 1) * eulerian_num(n - 1, m))

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, eulerian_num, *args)
