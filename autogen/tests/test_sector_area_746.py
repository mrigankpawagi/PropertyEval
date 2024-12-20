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
                
r = floats(min_value=0, allow_nan=False, allow_infinity=False)
a = floats(min_value=0)
strategy = r, a
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import math
def sector_area(r,a):
    if a > 360:
        return None
    return (math.pi*r**2) * (a/360)

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, sector_area, *args)
