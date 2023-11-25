import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
n = integers(min_value=0, max_value=MAX_SEQUENCE_LEN)
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
def test_fuzz(args):
    run_with_timeout(0.3, count_binary_seq, *args)
