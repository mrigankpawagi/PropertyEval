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
                
base = integers(min_value=1, max_value=9)
power = integers(min_value=1, max_value=100)

strategy = base, power
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def power_base_sum(base, power):
    return sum([int(i) for i in str(pow(base, power))])

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, power_base_sum, *args)
