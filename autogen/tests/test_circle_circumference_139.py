import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
r = floats(min_value=0, allow_nan=False, allow_infinity=False)

strategy = r
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def circle_circumference(r):
  perimeter=2*3.1415*r
  return perimeter

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, circle_circumference, *args)
