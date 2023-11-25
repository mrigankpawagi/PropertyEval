import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
a = lists(integers(), min_size=0, max_size=MAX_SEQUENCE_LEN)
x = integers()
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
