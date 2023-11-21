import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
from math import sqrt

w = floats(min_value=0.0, exclude_min=True)
h = floats(min_value=0.0, exclude_min=True)

strategy = w, h
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import math
def otherside_rightangle(w,h):
  s=math.sqrt((w*w)+(h*h))
  return s

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, otherside_rightangle, *args)
