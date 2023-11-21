import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
r = floats(min_value=0, max_value=MAX_FLOAT)
h = floats(min_value=0, max_value=MAX_FLOAT)

strategy = r, h
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import math
def volume_cone(r,h):
  volume = (1.0/3) * math.pi * r * r * h
  return volume

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, volume_cone, *args)
