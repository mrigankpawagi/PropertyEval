import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
l = floats(min_value=0.0, allow_nan=False)
strategy = l
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def lateralsurface_cube(l):
  LSA = 4 * (l * l)
  return LSA

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, lateralsurface_cube, *args)
