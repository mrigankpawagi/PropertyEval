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
                
l = lists(integers(), max_size=MAX_SEQUENCE_LEN)
n = integers(min_value=0, exclude_min=True)

strategy = l, n
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def split_Arr(l, n):
  return l[n:] + l[:n]

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, split_Arr, *args)
