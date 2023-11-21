import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
n1 = integers(min_value=MIN_INT, max_value=MAX_INT)
n2 = integers(min_value=MIN_INT, max_value=MAX_INT)

strategy = n1, n2
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def digit_distance_nums(n1, n2):
         return sum(map(int,str(abs(n1-n2))))

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, digit_distance_nums, *args)
