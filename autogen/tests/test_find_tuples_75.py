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
                
test_list = lists(integers(), max_size=MAX_SEQUENCE_LEN).map(lambda x: [(x, x+1, x+2)])
k = integers(min_value=1)

strategy = test_list, k
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def find_tuples(test_list, K):
  res = [sub for sub in test_list if all(ele % K == 0 for ele in sub)]
  return res

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, find_tuples, *args)
