import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
@composite
def create_list_of_tuples(draw):
    n = draw(integers(min_value=1, max_value=10))
    tuples = draw(lists(tuples(integers(min_value=1, max_value=10)), min_size=n, max_size=n))
    return tuples

test_list = create_list_of_tuples()
K = integers(min_value=1, max_value=10)

strategy = test_list, K
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def find_tuples(test_list, K):
  res = [sub for sub in test_list if all(ele % K == 0 for ele in sub)]
  return res

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, find_tuples, *args)
