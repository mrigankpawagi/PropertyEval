import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
a = lists(integers(min_value=MIN_INT, max_value=MAX_INT), min_size=1, unique=True)
x = integers(min_value=MIN_INT, max_value=MAX_INT)

strategy = a, x
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import bisect
def left_insertion(a, x):
    i = bisect.bisect_left(a, x)
    return i

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, left_insertion, *args)
