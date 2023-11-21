import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
n = integers(min_value=1, max_value=10)
k = integers(min_value=1, max_value=10)

strategy = n, k
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def count_no_of_ways(n, k): 
	dp = [0] * (n + 1) 
	total = k 
	mod = 1000000007
	dp[1] = k 
	dp[2] = k * k	 
	for i in range(3,n+1): 
		dp[i] = ((k - 1) * (dp[i - 1] + dp[i - 2])) % mod 
	return dp[n]

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, count_no_of_ways, *args)
