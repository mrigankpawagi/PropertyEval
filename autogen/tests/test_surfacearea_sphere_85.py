import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
import math

radius = floats(min_value=0.0)

strategy = radius
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import math
def surfacearea_sphere(r):
  surfacearea=4*math.pi*r*r
  return surfacearea

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, surfacearea_sphere, *args)
