import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
a = floats(min_value=MIN_FLOAT, max_value=MAX_FLOAT)
b = floats(min_value=MIN_FLOAT, max_value=MAX_FLOAT)
c = floats(min_value=MIN_FLOAT, max_value=MAX_FLOAT)

strategy = a, b, c
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def parabola_directrix(a, b, c): 
  directrix=((int)(c - ((b * b) + 1) * 4 * a ))
  return directrix

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, parabola_directrix, *args)
