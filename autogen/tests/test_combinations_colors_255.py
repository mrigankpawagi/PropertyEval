import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
from hypothesis import strategies as st

strategy = st.lists(st.integers(), min_size=1, max_size=MAX_SEQUENCE_LEN), st.integers(min_value=1, max_value=5)
if not isinstance(strategy, tuple):
    strategy = (strategy,)

from itertools import combinations_with_replacement 
def combinations_colors(l, n):
    return list(combinations_with_replacement(l,n))


@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, combinations_colors, *args)
