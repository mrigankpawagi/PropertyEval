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
                
listx = lists(integers(), min_size=0, max_size=MAX_SEQUENCE_LEN)

strategy = listx
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def list_tuple(listx):
  tuplex = tuple(listx)
  return tuplex

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, list_tuple, *args)
