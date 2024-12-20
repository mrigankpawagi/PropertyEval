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
                
import math

degree = floats(min_value=0, max_value=360)

strategy = degree
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import math
def radian_degree(degree):
 radian = degree*(math.pi/180)
 return radian

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, radian_degree, *args)
