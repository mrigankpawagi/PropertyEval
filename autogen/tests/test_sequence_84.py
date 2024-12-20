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

def sequence(n): 
	if n == 1 or n == 2: 
		return 1
	else: 
		return sequence(sequence(n-1)) + sequence(n-sequence(n-1))

@given(tuples(*strategy))
@settings(max_examples=1000)
def test_fuzz(args):
    run_with_timeout(0.3, sequence, *args)
