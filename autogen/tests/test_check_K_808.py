import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
test_tup = tuples(integers(), min_size=1, max_size=5)
K = integers()

strategy = test_tup, K
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def check_K(test_tup, K):
  res = False
  for ele in test_tup:
    if ele == K:
      res = True
      break
  return res 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, check_K, *args)
