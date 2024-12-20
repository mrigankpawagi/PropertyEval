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
                
x = floats(min_value=0.0, exclude_min=True)
y = floats(min_value=0.0, exclude_min=True)

strategy = x, y
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import cmath
def polar_rect(x,y):
 cn = complex(x,y)
 cn=cmath.polar(cn)
 cn1 = cmath.rect(2, cmath.pi)
 return (cn,cn1)

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, polar_rect, *args)
