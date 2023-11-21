import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
degree = floats(min_value=0, max_value=360)

strategy = degree
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import math
def radian_degree(degree):
 radian = degree*(math.pi/180)
 return radian

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, radian_degree, *args)
