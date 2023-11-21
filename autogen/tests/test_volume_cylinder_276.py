import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
import math

r = floats(min_value=0)
h = floats(min_value=0)

strategy = r, h
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def volume_cylinder(r,h):
  volume=3.1415*r*r*h
  return volume

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, volume_cylinder, *args)
