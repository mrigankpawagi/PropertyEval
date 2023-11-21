import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
base1 = integers(min_value=1, max_value=MAX_INT)
base2 = integers(min_value=1, max_value=MAX_INT)
height = integers(min_value=1, max_value=MAX_INT)

strategy = base1, base2, height
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def median_trapezium(base1,base2,height):
 median = 0.5 * (base1+ base2)
 return median

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, median_trapezium, *args)
