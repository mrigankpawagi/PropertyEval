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
                
test_str = text(max_size=MAX_SEQUENCE_LEN).filter(lambda x: len(x) > 0)
K = integers(max_value=MAX_SEQUENCE_LEN).filter(lambda x: x >= 0)

strategy = test_str, K
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def remove_length(test_str, K):
  temp = test_str.split()
  res = [ele for ele in temp if len(ele) != K]
  res = ' '.join(res)
  return (res) 

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, remove_length, *args)
