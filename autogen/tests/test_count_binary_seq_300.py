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
                
n = integers(min_value=1, max_value=10)
strategy = n
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def count_binary_seq(n): 
	nCr = 1
	res = 1
	for r in range(1, n + 1): 
		nCr = (nCr * (n + 1 - r)) / r 
		res += nCr * nCr 
	return res 

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, count_binary_seq, *args)
