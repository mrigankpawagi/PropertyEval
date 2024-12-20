import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given, settings
from timeout import run_with_timeout
from typing import *
                
test_list = lists(tuples(integers(), integers()), max_size=MAX_SEQUENCE_LEN)
K = integers(min_value=0)

strategy = test_list, K
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def trim_tuple(test_list, K):
  res = []
  for ele in test_list:
    N = len(ele)
    res.append(tuple(list(ele)[K: N - K]))
  return (str(res)) 

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, trim_tuple, *args)
