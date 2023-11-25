import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
test_list = lists(tuples(integers(), text()), max_size=MAX_SEQUENCE_LEN)
K = integers(min_value=0)

strategy = test_list, K
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def min_k(test_list, K):
  res = sorted(test_list, key = lambda x: x[1])[:K]
  return (res) 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, min_k, *args)
