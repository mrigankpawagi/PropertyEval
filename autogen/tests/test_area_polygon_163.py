import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given, settings
from timeout import run_with_timeout
from typing import *
                
s = floats(min_value=1e-5, exclude_min=True, max_value=MAX_FLOAT)
l = integers(min_value=3, max_value=10)

strategy = s, l
if not isinstance(strategy, tuple):
    strategy = (strategy,)

from math import tan, pi
def area_polygon(s, l):
  area = s * (l ** 2) / (4 * tan(pi / s))
  return area

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, area_polygon, *args)
