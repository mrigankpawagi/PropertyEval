import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
Input = lists(
    tuples(
        integers(min_value=MIN_INT, max_value=MAX_INT),
        min_size=1,
        max_size=MAX_TUPLE_SIZE
    ),
    min_size=1,
    max_size=MAX_LIST_SIZE
)

strategy = Input
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def find_equal_tuple(Input):
  k = 0 if not Input else len(Input[0])
  flag = 1
  for tuple in Input:
    if len(tuple) != k:
      flag = 0
      break
  return flag
def get_equal(Input):
  return find_equal_tuple(Input) == 1

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, find_equal_tuple, *args)
