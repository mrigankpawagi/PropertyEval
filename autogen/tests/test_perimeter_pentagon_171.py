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
                
a = floats(min_value=0, allow_nan=False)
strategy = a
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import math
def perimeter_pentagon(a):
  perimeter=(5*a)
  return perimeter

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, perimeter_pentagon, *args)
