import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
l = lists(min_size=1, max_size=MAX_SEQUENCE_LEN)
n = integers(min_value=1)

strategy = l, n
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def split_Arr(l, n):
  return l[n:] + l[:n]

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, split_Arr, *args)
