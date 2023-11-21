import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
a = integers(min_value=1, max_value=100)

strategy = a
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def square_perimeter(a):
  perimeter=4*a
  return perimeter

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, square_perimeter, *args)
