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
                
test_tup1 = tuples(integers(min_value=MIN_INT, max_value=MAX_INT), integers(min_value=MIN_INT, max_value=MAX_INT), integers(min_value=MIN_INT, max_value=MAX_INT))
test_tup2 = tuples(integers(min_value=MIN_INT, max_value=MAX_INT), integers(min_value=MIN_INT, max_value=MAX_INT), integers(min_value=MIN_INT, max_value=MAX_INT))

strategy = test_tup1, test_tup2
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def check_smaller(test_tup1, test_tup2):
  return all(x > y for x, y in zip(test_tup1, test_tup2))

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, check_smaller, *args)
