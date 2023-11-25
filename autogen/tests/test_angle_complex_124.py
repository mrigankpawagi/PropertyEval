import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
a = complex_numbers()
b = complex_numbers()

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
