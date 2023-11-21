import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
from cmath import phase

a = complex(floats(min_value=MIN_FLOAT, max_value=MAX_FLOAT), floats(min_value=MIN_FLOAT, max_value=MAX_FLOAT))
b = complex(floats(min_value=MIN_FLOAT, max_value=MAX_FLOAT), floats(min_value=MIN_FLOAT, max_value=MAX_FLOAT))

strategy = a, b
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import cmath
def angle_complex(a,b):
  cn=complex(a,b)
  angle=cmath.phase(a+b)
  return angle

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, angle_complex, *args)
