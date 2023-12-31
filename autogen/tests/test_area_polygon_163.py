import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
s = floats(min_value=0.0, exclude_min=True)
l = integers(min_value=3, max_value=10)

strategy = s, l
if not isinstance(strategy, tuple):
    strategy = (strategy,)

from math import tan, pi
def area_polygon(s, l):
  area = s * (l ** 2) / (4 * tan(pi / s))
  return area

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, area_polygon, *args)
