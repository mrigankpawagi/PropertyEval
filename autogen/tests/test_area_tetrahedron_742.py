import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
side = floats(min_value=0.1, max_value=10)

strategy = side
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import math
def area_tetrahedron(side):
  area = math.sqrt(3)*(side*side)
  return area

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, area_tetrahedron, *args)
