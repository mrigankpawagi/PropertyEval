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
                
a = lists(integers(), max_size=MAX_SEQUENCE_LEN)
strategy = a
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def largest_subset(a):
	n = len(a)
	dp = [0 for i in range(n)]
	dp[n - 1] = 1; 
	for i in range(n - 2, -1, -1):
		mxm = 0;
		for j in range(i + 1, n):
			if a[j] % a[i] == 0 or a[i] % a[j] == 0:
				mxm = max(mxm, dp[j])
		dp[i] = 1 + mxm
	return max(dp)

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, largest_subset, *args)
