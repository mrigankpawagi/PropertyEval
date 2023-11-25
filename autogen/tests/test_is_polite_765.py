import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
n = integers(min_value=0, max_value=10**6)
strategy = n
if not isinstance(strategy, tuple):
    strategy = (strategy,)

import math 
def is_polite(n): 
	n = n + 1
	return (int)(n+(math.log((n + math.log(n, 2)), 2))) 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, is_polite, *args)
