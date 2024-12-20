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
                
n = integers(min_value=0)
strategy = n
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def sum_digits(n):
  if n == 0:
    return 0
  else:
    return n % 10 + sum_digits(int(n / 10))

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, sum_digits, *args)
