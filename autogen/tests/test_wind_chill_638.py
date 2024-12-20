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
                
v = integers(min_value=1, max_value=120)
t = integers(min_value=-50, max_value=50)

strategy = v, t
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import math
def wind_chill(v,t):
 windchill = 13.12 + 0.6215*t -  11.37*math.pow(v, 0.16) + 0.3965*t*math.pow(v, 0.16)
 return int(round(windchill, 0))

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, wind_chill, *args)
