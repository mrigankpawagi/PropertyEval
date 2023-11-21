import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
a = lists(integers(), min_size=1, unique=True)
x = integers()

strategy = a, x
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import bisect
def right_insertion(a, x):
    return bisect.bisect_right(a, x)

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, right_insertion, *args)
