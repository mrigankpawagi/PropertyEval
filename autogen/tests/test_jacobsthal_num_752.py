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
                
n = integers(min_value=0, max_value=13)
strategy = n
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def jacobsthal_num(n): 
	dp = [0] * (n + 1) 
	dp[0] = 0
	dp[1] = 1
	for i in range(2, n+1): 
		dp[i] = dp[i - 1] + 2 * dp[i - 2] 
	return dp[n]

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, jacobsthal_num, *args)
