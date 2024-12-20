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
                
a = lists(integers(), min_size=1, max_size=MAX_SEQUENCE_LEN).map(sorted)
x = integers()

strategy = a, x
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import bisect
def left_insertion(a, x):
    i = bisect.bisect_left(a, x)
    return i

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, left_insertion, *args)
