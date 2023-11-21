import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
test_list = lists(
    tuples(
        integers(min_value=MIN_INT, max_value=MAX_INT), 
        integers(min_value=MIN_INT, max_value=MAX_INT), 
        integers(min_value=MIN_INT, max_value=MAX_INT)
    ),
    min_size=1, max_size=MAX_SEQUENCE_LEN
)

K = integers(min_value=MIN_INT, max_value=MAX_INT)

strategy = test_list, K
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def find_tuples(test_list, K):
  res = [sub for sub in test_list if all(ele % K == 0 for ele in sub)]
  return res

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, find_tuples, *args)
