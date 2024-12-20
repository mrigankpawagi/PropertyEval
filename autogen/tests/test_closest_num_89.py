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
                
N = integers(min_value=1, max_value=MAX_INT)
strategy = N
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def closest_num(N):
  return (N - 1)

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, closest_num, *args)
