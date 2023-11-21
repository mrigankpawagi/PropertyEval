import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
test_tup1 = tuples(integers())
test_tup2 = tuples(integers()).filter(lambda t: all(x < y for x, y in zip(t, test_tup1)))

strategy = test_tup1, test_tup2
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def check_smaller(test_tup1, test_tup2):
  return all(x > y for x, y in zip(test_tup1, test_tup2))

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, check_smaller, *args)
