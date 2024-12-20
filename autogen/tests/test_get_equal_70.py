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
                
from typing import List, Tuple

Input = lists(lists(integers()), max_size=MAX_SEQUENCE_LEN)

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
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, get_equal, *args)
