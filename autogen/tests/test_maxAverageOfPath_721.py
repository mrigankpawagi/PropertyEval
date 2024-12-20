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
                
N = integers(min_value=1, max_value=MAX_SEQUENCE_LEN)
cost = lists(lists(floats(min_value=0.0, max_value=100.0), min_size=N, max_size=N), min_size=N, max_size=N)

strategy = cost
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def maxAverageOfPath(cost):
  N = len(cost)
  dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
  dp[0][0] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, N):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 1][j],
                     dp[i][j - 1]) + cost[i][j]
  return dp[N - 1][N - 1] / (2 * N - 1)

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, maxAverageOfPath, *args)
