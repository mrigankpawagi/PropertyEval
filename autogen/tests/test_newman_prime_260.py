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
                
n = integers(min_value=0, max_value=10)
strategy = n
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def newman_prime(n): 
	if n == 0 or n == 1: 
		return 1
	return 2 * newman_prime(n - 1) + newman_prime(n - 2)

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, newman_prime, *args)
