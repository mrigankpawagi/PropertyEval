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
                
w = floats(min_value=1, max_value=10)
h = floats(min_value=1, max_value=10)

strategy = w, h
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import math
def otherside_rightangle(w,h):
  s=math.sqrt((w*w)+(h*h))
  return s

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, otherside_rightangle, *args)
