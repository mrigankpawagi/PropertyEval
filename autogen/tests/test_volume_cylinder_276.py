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
                
r = floats(min_value=0, exclude_min=True, allow_nan=False, allow_infinity=False)
h = floats(min_value=0, exclude_min=True, allow_nan=False, allow_infinity=False)

strategy = r, h
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def volume_cylinder(r,h):
  volume=3.1415*r*r*h
  return volume

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, volume_cylinder, *args)
