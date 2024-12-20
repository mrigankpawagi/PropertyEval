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

a = floats(min_value=-100, max_value=100)
b = floats(min_value=-100, max_value=100)

strategy = a, b
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import cmath
def angle_complex(a,b):
  cn=complex(a,b)
  angle=cmath.phase(a+b)
  return angle

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, angle_complex, *args)
