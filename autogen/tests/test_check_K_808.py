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
                
test_tup = lists(integers(), max_size=MAX_SEQUENCE_LEN)
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
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, check_K, *args)
