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
                
a = lists(integers(), min_size=1, max_size=MAX_SEQUENCE_LEN)
n = integers(min_value=1, max_value=MAX_SEQUENCE_LEN)
index = integers(min_value=0, max_value=n-1)
k = integers(min_value=index+1, max_value=n-1)

strategy = a, n, index, k
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def max_sum_increasing_subseq(a, n, index, k):
	dp = [[0 for i in range(n)] 
			for i in range(n)]
	for i in range(n):
		if a[i] > a[0]:
			dp[0][i] = a[i] + a[0]
		else:
			dp[0][i] = a[i]
	for i in range(1, n):
		for j in range(n):
			if a[j] > a[i] and j > i:
				if dp[i - 1][i] + a[j] > dp[i - 1][j]:
					dp[i][j] = dp[i - 1][i] + a[j]
				else:
					dp[i][j] = dp[i - 1][j]
			else:
				dp[i][j] = dp[i - 1][j]
	return dp[index][k]

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, max_sum_increasing_subseq, *args)
