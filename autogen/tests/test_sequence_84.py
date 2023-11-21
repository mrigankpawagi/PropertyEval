import sys
sys.path.append("../..")
sys.path.append("..")

from limits.limits import *
from hypothesis.strategies import *
from hypothesis import given
from timeout import run_with_timeout
from typing import *
                
n = integers(min_value=1, max_value=MAX_SEQUENCE_LEN)

strategy = n
if not isinstance(strategy, tuple):
    strategy = (strategy,)

def sequence(n): 
	if n == 1 or n == 2: 
		return 1
	else: 
		return sequence(sequence(n-1)) + sequence(n-sequence(n-1))

@given(tuples(*strategy))
def test_fuzz(args):
    run_with_timeout(0.3, sequence, *args)
