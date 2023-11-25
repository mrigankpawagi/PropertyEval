import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
a = floats(min_value=0.0, allow_infinity=False, allow_nan=False)
strategy = a
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import math
def perimeter_pentagon(a):
  perimeter=(5*a)
  return perimeter

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, perimeter_pentagon, *args)
