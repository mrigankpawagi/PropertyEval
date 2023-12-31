import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
l = floats(min_value=0.0, max_value=10.0)
strategy = l
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def surfacearea_cube(l):
  surfacearea= 6*l*l
  return surfacearea

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, surfacearea_cube, *args)
