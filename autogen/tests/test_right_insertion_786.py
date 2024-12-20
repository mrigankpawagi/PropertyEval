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
                
a = lists(integers(), unique=True, max_size=50).map(sorted)
x = integers(min_value=0)

strategy = a, x
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import bisect
def right_insertion(a, x):
    return bisect.bisect_right(a, x)

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, right_insertion, *args)
