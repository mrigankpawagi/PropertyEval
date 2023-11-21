import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
n = integers(min_value=1, max_value=100)

strategy = n
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def is_num_decagonal(n): 
	return 4 * n * n - 3 * n 

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, is_num_decagonal, *args)
