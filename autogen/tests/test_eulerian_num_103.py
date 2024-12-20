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
                
from hypothesis import strategies as st

n = st.integers(min_value=0, max_value=10)
m = st.integers(min_value=0, max_value=10)

strategy = n, m
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def eulerian_num(n, m): 
	if (m >= n or n == 0): 
		return 0 
	if (m == 0): 
		return 1 
	return ((n - m) * eulerian_num(n - 1, m - 1) +(m + 1) * eulerian_num(n - 1, m))

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, eulerian_num, *args)
