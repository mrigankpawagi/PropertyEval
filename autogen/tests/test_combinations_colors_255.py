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
                
l = lists(elements=sampled_from(["Red", "Green", "Blue"]), min_size=1, max_size=MAX_SEQUENCE_LEN)
n = integers(min_value=1, max_value=MAX_SEQUENCE_LEN)

strategy = l, n
if not isinstance(strategy, tuple):
    strategy = (strategy,)

from itertools import combinations_with_replacement 
def combinations_colors(l, n):
    return list(combinations_with_replacement(l,n))


@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, combinations_colors, *args)
