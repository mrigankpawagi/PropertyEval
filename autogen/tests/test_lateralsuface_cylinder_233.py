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
                
r = floats(min_value=0.0, min_value_exclusive=True, max_value=10.0)
h = floats(min_value=0.0, min_value_exclusive=True, max_value=10.0)

strategy = r, h
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def lateralsuface_cylinder(r,h):
  lateralsurface= 2*3.1415*r*h
  return lateralsurface

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, lateralsuface_cylinder, *args)
