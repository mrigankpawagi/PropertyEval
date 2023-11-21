import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
import math

r = floats(min_value=0, exclude_min=True)
h = floats(min_value=0, exclude_min=True)

strategy = r, h
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def lateralsuface_cylinder(r,h):
  lateralsurface= 2*3.1415*r*h
  return lateralsurface

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, lateralsuface_cylinder, *args)
