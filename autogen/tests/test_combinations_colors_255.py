import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
from hypothesis.strategies import lists, tuples
from hypothesis import given

def combinations_colors(l, n):
    return list(map(tuple, tuples(l, min_size=n, max_size=n)))

strategy = tuples(
    lists(
        elements=one_of("Red", "Green", "Blue"),
        min_size=1,
        max_size=3
    ),
    integers(min_value=1, max_value=2)
)
if not isinstance(strategy, tuple):
    strategy = (strategy,)

from itertools import combinations_with_replacement 
def combinations_colors(l, n):
    return list(combinations_with_replacement(l,n))


@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, combinations_colors, *args)
