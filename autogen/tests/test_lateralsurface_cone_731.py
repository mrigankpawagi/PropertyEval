import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
r = floats(min_value=0.0, exclude_min=True)
h = floats(min_value=0.0, exclude_min=True)

strategy = r, h
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import math
def lateralsurface_cone(r,h):
  l = math.sqrt(r * r + h * h)
  LSA = math.pi * r  * l
  return LSA

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, lateralsurface_cone, *args)
