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
                
test_list = lists(tuples(text(), integers()), max_size=MAX_SEQUENCE_LEN)
K = integers(min_value=0, max_value=MAX_SEQUENCE_LEN)

strategy = test_list, K
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def min_k(test_list, K):
  res = sorted(test_list, key = lambda x: x[1])[:K]
  return (res) 

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, min_k, *args)
