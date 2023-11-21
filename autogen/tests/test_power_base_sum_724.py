import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
base = integers(min_value=1, max_value=MAX_INT)
power = integers(min_value=0)

strategy = base, power
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def power_base_sum(base, power):
    return sum([int(i) for i in str(pow(base, power))])

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, power_base_sum, *args)
