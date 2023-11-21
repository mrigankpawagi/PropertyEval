import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
l = floats(min_value=0.0, exclude_min=True, allow_infinity=False, allow_nan=False)

strategy = l
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def volume_cube(l):
  volume = l * l * l
  return volume

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, volume_cube, *args)
