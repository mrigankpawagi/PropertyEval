import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
r = floats(min_value=0.0, max_value=MAX_FLOAT)

strategy = r
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import math
def volume_sphere(r):
  volume=(4/3)*math.pi*r*r*r
  return volume

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, volume_sphere, *args)
