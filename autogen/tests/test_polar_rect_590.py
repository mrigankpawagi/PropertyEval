import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
@composite
def polar_coordinates(draw):
    r = draw(floats(min_value=0))
    theta = draw(floats(min_value=0, max_value=2 * math.pi))
    return r, theta

x, y = polar_coordinates(), polar_coordinates()

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
def test_fuzz(args):
    run_with_timeout(0.3, polar_rect, *args)
